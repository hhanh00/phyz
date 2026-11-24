"""Prosody transfer: a TTS reading of a sentence, reshaped to the timing and emphasis of a recorded reading.

Both readings are force-aligned word by word with wav2vec2. By default only the
coarse shape of the recording is copied: its overall pace, its pauses, and the one
or two words per sentence the speaker clearly stressed, which get a small pitch and
loudness boost. The TTS voice keeps its own word lengths, its own intonation and its
own pronunciation. Copying every word's pitch and loudness (pitch="word",
loudness=True) made the voice jump from word to word in testing, and copying the
recorded pitch curve and word lengths in full (pitch="contour", timing="word") also
carried over the speaker's accent.
"""
import re

import numpy as np
import parselmouth
import soundfile as sf
import torch
import torchaudio
from parselmouth.praat import call
from torchaudio.functional import forced_align, merge_tokens

PITCH_SCALE = 1.0  # share of the recorded pitch movement to keep, measured in semitones around its mean
GAIN_LIMIT = (0.6, 1.7)  # bounds on each word's loudness change
STRETCH_LIMIT = (0.25, 4.0)  # bounds on how far a stretch of speech may be slowed or sped up
RATE_LIMIT = (90, 110)  # percent of the voice's own pace; a sentence's recorded pace is clamped to this
MIN_BREAK = 0.25  # seconds; shorter recorded pauses are left out of the SSML, as the engine's own gaps cover them
MAX_PAUSE = 0.6  # seconds; a longer recorded pause inside a sentence is a hesitation, so it is capped
OCTAVE_GUARD = 9.0  # semitones; pitch readings this far from the sentence's median are tracking errors
MAX_SHIFT = 6.0  # semitones; the most a word may sit above or below the sentence, or be moved
BOOST = (2.0, 2.0)  # semitones and dB added to a stressed word in emphasis mode
SMALL_WORDS = set("""a an the of to in on at by for from with and or but so if as is are was were be been it its
this that these those there here we you they he she i our your their his her my me us them not no do does
did has have had will would can could just than then into onto over under up out about each every""".split())


def stressed(recording, rate, spans, tokens):
    """The one or two words the speaker clearly stressed: high in pitch and not quiet, never a small word."""
    pitch = parselmouth.Sound(recording.astype(np.float64), rate).to_pitch(0.01, 60, 400)
    level = word_levels(pitch.selected_array["frequency"], pitch.xs(), spans)
    loud = np.array([_rms(recording, rate, *h) for h in spans])
    volume = 20 * np.log10(np.maximum(loud, 1e-6) / (loud.mean() or 1))
    score = np.where(np.isnan(level), -np.inf, level + 0.5 * volume)
    candidates = [i for i in np.argsort(-score) if score[i] > -np.inf and level[i] >= 1.5 and volume[i] >= 0
                  and _letters(tokens[i]).lower().strip("'") not in SMALL_WORDS]
    return sorted(candidates[:1 if len(tokens) <= 6 else 2])

_aligner = None


def _letters(word):
    return re.sub(r"[^A-Z']", "", word.upper())


def align(audio, rate, words):
    """Each word's (start, end) in seconds, by forced alignment against the known words."""
    global _aligner
    if _aligner is None:
        bundle = torchaudio.pipelines.WAV2VEC2_ASR_BASE_960H
        _aligner = bundle.get_model().eval(), {c: i for i, c in enumerate(bundle.get_labels())}
    model, index = _aligner
    tokens, owner = [], []
    for i, word in enumerate(words):
        for c in _letters(word):
            tokens.append(index[c])
            owner.append(i)
        tokens.append(index["|"])
        owner.append(None)
    tokens, owner = tokens[:-1], owner[:-1]
    x = torchaudio.functional.resample(torch.from_numpy(np.ascontiguousarray(audio, dtype=np.float32)), rate, 16000)
    with torch.inference_mode():
        emission = model(x[None])[0].log_softmax(-1)
    labels, scores = forced_align(emission, torch.tensor([tokens], dtype=torch.int32), blank=0)
    spans = merge_tokens(labels[0], scores[0].exp(), blank=0)
    per_frame = len(x) / 16000 / emission.shape[1]
    times = [None] * len(words)
    for k, span in enumerate(spans):
        if owner[k] is None:
            continue
        t = times[owner[k]]
        times[owner[k]] = (t[0] if t else span.start * per_frame, span.end * per_frame)
    return times


def load(path, rate):
    """A recording as mono float32 at the given rate."""
    audio, r = sf.read(path, dtype="float32")
    if audio.ndim > 1:
        audio = audio.mean(1)
    if r != rate:
        audio = torchaudio.functional.resample(torch.from_numpy(audio), r, rate).numpy()
    return audio


def _rms(audio, rate, a, b):
    seg = audio[int(a * rate):int(b * rate)]
    return float(np.sqrt(np.mean(seg ** 2))) if len(seg) else 0.0


def _semitones(f):
    return 12 * np.log2(f / 100)


def word_levels(frequency, times, spans):
    """Each span's pitch relative to the sentence's typical word, in semitones, or NaN where unvoiced.

    Pitch trackers jump an octave on creaky or breathy voice, mostly at the ends of sentences,
    so readings far from the sentence's median are dropped, each word takes the median of its
    remaining readings, and the result is capped at MAX_SHIFT.
    """
    voiced = frequency > 0
    if voiced.sum() < 3:
        return np.full(len(spans), np.nan)
    st = np.where(voiced, _semitones(np.maximum(frequency, 1)), np.nan)
    keep = voiced & (np.abs(st - np.nanmedian(st)) <= OCTAVE_GUARD)
    levels = np.array([np.median(st[keep & (times >= a) & (times <= b)])
                       if (keep & (times >= a) & (times <= b)).sum() >= 3 else np.nan for a, b in spans])
    if np.isnan(levels).all():
        return levels
    return np.clip(levels - np.nanmedian(levels), -MAX_SHIFT, MAX_SHIFT)


def transfer(tts, recording, sentence, rate, timing="phrase", pitch="emphasis", loudness="emphasis"):
    """The TTS reading `tts` of `sentence`, reshaped to the prosody of `recording`, both at `rate`.

    timing="word" gives every word the recorded duration; "phrase" keeps the voice's own
    word lengths, scaled to the recorded overall pace, and inserts the recorded pauses.
    pitch="contour" copies the recorded pitch curve; "word" keeps the voice's own curve and
    only raises or lowers each word by as much as the recording did, relative to its mean;
    "emphasis" raises only the stressed words chosen by stressed(). loudness=True copies each
    word's relative loudness; "emphasis" boosts only the stressed words. False leaves that
    aspect as the TTS voice had it.
    """
    words = [w for w in sentence.split() if _letters(w)]
    kt, ht = align(tts, rate, words), align(recording, rate, words)
    index = [i for i, (k, h) in enumerate(zip(kt, ht)) if k and h]
    index = [i for n, i in enumerate(index) if n == 0 or (kt[i][0] > kt[index[n - 1]][0] and ht[i][0] > ht[index[n - 1]][0])]
    pairs = [(kt[i], ht[i]) for i in index]
    end_k, end_h = len(tts) / rate, len(recording) / rate
    chosen = []  # pairs stressed in emphasis mode

    sound = parselmouth.Sound(tts.astype(np.float64), rate)
    manipulation = call(sound, "To Manipulation", 0.01, 60, 300)

    # Timing. kmap -> omap maps TTS time to output time, before any inserted pauses.
    duration = call("Create DurationTier", "d", 0, end_k)
    if timing == "word":
        kp, hp = [0.0], [0.0]
        for k, h in pairs:
            if k[0] > kp[-1] + 0.005 and h[0] > hp[-1] + 0.005:
                kp += [k[0], k[1]]
                hp += [h[0], h[1]]
        kp.append(end_k)
        hp.append(end_h)
        for (a, b), (c, d) in zip(zip(kp, kp[1:]), zip(hp, hp[1:])):
            if b - a >= 0.002:
                ratio = float(np.clip((d - c) / (b - a), *STRETCH_LIMIT))
                call(duration, "Add point", a + 0.001, ratio)
                call(duration, "Add point", b - 0.001, ratio)
        kmap, omap = kp, hp
    elif timing == "phrase":
        spoken_k = sum(k[1] - k[0] for k, _ in pairs) or 1
        spoken_h = sum(h[1] - h[0] for _, h in pairs)
        pace = float(np.clip(spoken_h / spoken_k, 100 / RATE_LIMIT[1], 100 / RATE_LIMIT[0]))
        call(duration, "Add point", 0, pace)
        kmap, omap = [0.0, end_k], [0.0, pace * end_k]
    else:
        kmap, omap = [0.0, end_k], [0.0, end_k]
    if timing:
        call([manipulation, duration], "Replace duration tier")

    # Pitch, as a PitchTier on the TTS timeline.
    kpitch = sound.to_pitch(0.01, 60, 400)
    kf = kpitch.selected_array["frequency"]
    if pitch == "contour":
        recorded = parselmouth.Sound(recording.astype(np.float64), rate).to_pitch(0.01, 60, 400)
        rf = recorded.selected_array["frequency"]
        if (rf > 0).sum() > 5 and (kf > 0).sum() > 5:
            hp_all = [0.0] + [x for _, h in pairs for x in h] + [end_h]
            kp_all = [0.0] + [x for k, _ in pairs for x in k] + [end_k]
            rmean, kmean = np.mean(_semitones(rf[rf > 0])), np.mean(_semitones(kf[kf > 0]))
            tier = call("Create PitchTier", "p", 0, end_k)
            for t, f in zip(recorded.xs(), rf):
                if f > 0:
                    semis = kmean + PITCH_SCALE * (_semitones(f) - rmean)
                    call(tier, "Add point", float(np.interp(t, hp_all, kp_all)), 100 * 2 ** (semis / 12))
            call([manipulation, tier], "Replace pitch tier")
    elif pitch == "emphasis":
        chosen = stressed(recording, rate, [h for _, h in pairs], [words[i] for i in index])
        if chosen:
            centers = np.array([(k[0] + k[1]) / 2 for k, _ in pairs])
            bump = np.array([BOOST[0] if n in chosen else 0.0 for n in range(len(pairs))])
            tier = call("Create PitchTier", "p", 0, end_k)
            for t, f in zip(kpitch.xs(), kf):
                if f > 0:
                    call(tier, "Add point", float(t), float(f * 2 ** (np.interp(t, centers, bump) / 12)))
            call([manipulation, tier], "Replace pitch tier")
    elif pitch == "word":
        rpitch = parselmouth.Sound(recording.astype(np.float64), rate).to_pitch(0.01, 60, 400)
        rf, rx = rpitch.selected_array["frequency"], rpitch.xs()
        kx = kpitch.xs()

        rw = word_levels(rf, rx, [h for _, h in pairs])
        kw = word_levels(kf, kx, [k for k, _ in pairs])
        ok = ~np.isnan(rw) & ~np.isnan(kw)
        if ok.sum() >= 2:
            shift = np.clip(PITCH_SCALE * (rw - kw), -MAX_SHIFT, MAX_SHIFT)[ok]
            centers = np.array([(k[0] + k[1]) / 2 for k, _ in pairs])[ok]
            tier = call("Create PitchTier", "p", 0, end_k)
            for t, f in zip(kx, kf):
                if f > 0:
                    call(tier, "Add point", float(t), float(f * 2 ** (np.interp(t, centers, shift) / 12)))
            call([manipulation, tier], "Replace pitch tier")

    out = call(manipulation, "Get resynthesis (overlap-add)").values[0].astype(np.float32)

    def to_out(t):
        return float(np.interp(t, kmap, omap))

    # Pauses: in phrase mode, lengthen each gap between words to the recorded pause.
    if timing == "phrase":
        pieces, cursor, inserted, shifts = [], 0, 0.0, []
        for (k1, h1), (k2, h2) in zip(pairs, pairs[1:]):
            extra = min(h2[0] - h1[1], MAX_PAUSE) - (to_out(k2[0]) - to_out(k1[1]))
            if extra > 0.08:
                cut = int(rate * (to_out(k1[1]) + to_out(k2[0])) / 2)
                pieces += [out[cursor:cut], np.zeros(int(rate * extra), dtype=np.float32)]
                cursor = cut
                shifts.append((cut / rate, extra))
        out = np.concatenate(pieces + [out[cursor:]])

        def to_out(t, base=to_out):  # noqa: F811, including the inserted silences
            o = base(t)
            return o + sum(e for c, e in shifts if c <= o)

    if not loudness:
        return (out / max(1.0, np.abs(out).max() / 0.95)).astype(np.float32)
    if loudness == "emphasis":
        gain = np.ones(len(out), dtype=np.float32)
        for n in chosen:
            a, b = to_out(pairs[n][0][0]), to_out(pairs[n][0][1])
            gain[int(a * rate):int(b * rate)] = 10 ** (BOOST[1] / 20)
        ramp = int(0.03 * rate)
        out = out * np.convolve(gain, np.ones(ramp) / ramp, mode="same")
        return (out / max(1.0, np.abs(out).max() / 0.95)).astype(np.float32)

    # Loudness: each word gets the recording's relative loudness, with 20 ms ramps between words.
    outs = [(to_out(k[0]), to_out(k[1])) for k, _ in pairs]
    rmean = np.mean([_rms(recording, rate, *h) for _, h in pairs]) or 1
    omean = np.mean([_rms(out, rate, *o) for o in outs]) or 1
    gain = np.ones(len(out), dtype=np.float32)
    for (_, h), o in zip(pairs, outs):
        g = (_rms(recording, rate, *h) / rmean) / max(_rms(out, rate, *o) / omean, 1e-4)
        gain[int(o[0] * rate):int(o[1] * rate)] = np.clip(g, *GAIN_LIMIT)
    ramp = int(0.02 * rate)
    out = out * np.convolve(gain, np.ones(ramp) / ramp, mode="same")
    return (out / max(1.0, np.abs(out).max() / 0.95)).astype(np.float32)


# --- Recording the measured prosody as SSML -------------------------------------------------

def measure(tts, recording, sentence, rate):
    """What transfer() takes from `recording` in its default mode, as numbers: one plan for the sentence.

    rate      the recorded pace as a percentage of the TTS voice's own pace (below 100 is slower)
    words     the sentence's words, as transfer() aligns them
    stressed  indices into words of the stressed words
    breaks    {index of the word before the pause: seconds}, recorded pauses inside the sentence
    """
    tokens = [w for w in sentence.split() if _letters(w)]
    kt, ht = align(tts, rate, tokens), align(recording, rate, tokens)
    pairs = [i for i in range(len(tokens)) if kt[i] and ht[i]]
    pairs = [i for n, i in enumerate(pairs) if n == 0 or (kt[i][0] > kt[pairs[n - 1]][0] and ht[i][0] > ht[pairs[n - 1]][0])]
    spoken_k = sum(kt[i][1] - kt[i][0] for i in pairs) or 1
    spoken_h = sum(ht[i][1] - ht[i][0] for i in pairs) or 1
    pace = float(np.clip(spoken_h / spoken_k, 100 / RATE_LIMIT[1], 100 / RATE_LIMIT[0]))
    chosen = [pairs[n] for n in stressed(recording, rate, [ht[i] for i in pairs], [tokens[i] for i in pairs])] if pairs else []
    breaks = {}
    for i, j in zip(pairs, pairs[1:]):
        gap = ht[j][0] - ht[i][1]
        if gap >= MIN_BREAK:
            breaks[j - 1] = min(gap, MAX_PAUSE)
    return {"rate": 100 / pace, "words": tokens, "stressed": chosen, "breaks": breaks}


def pauses(recording, sentence, rate):
    """Indices of the words in `sentence` after which `recording` pauses for at least MIN_BREAK.

    The indices count only the words that contain letters, as align() sees them.
    """
    words = [w for w in sentence.split() if _letters(w)]
    times = align(recording, rate, words)
    return {i for i in range(len(words) - 1)
            if times[i] and times[i + 1] and times[i + 1][0] - times[i][1] >= MIN_BREAK}


def sentence_gaps(manifest, longest=1.5):
    """{sentence number: seconds from its last word to the next sentence's first word} from a takes.py manifest.

    Only gaps takes.py could measure are included, and a gap over `longest` seconds
    is a break in the reading, not a pause, so it is capped.
    """
    if not manifest.exists():
        return {}
    rows = [dict(zip(("n", "source", "start", "end", "score", "clip", "note", "pause"), line.split("\t")))
            for line in manifest.read_text().splitlines()[1:]]
    return {int(row["n"]): min(max(0.0, float(following["start"]) - float(row["end"])), longest)
            for row, following in zip(rows, rows[1:]) if row["pause"] and row["source"] == following["source"]}


def to_ssml(plans, voice, source):
    """An SSML document from {sentence number: plan}, one <s> per sentence."""
    from xml.sax.saxutils import escape
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<speak version="1.1" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US">',
           f"<!-- Prosody measured from {source}.",
           f"     rate: the reading's pace as a percentage of Kokoro {voice}'s own pace.",
           f"     pitch, volume: a +{BOOST[0]:g} st, +{BOOST[1]:g} dB boost on the one or two words per sentence",
           "     the speaker clearly stressed. Every other word keeps the voice's own intonation.",
           f"     break: pauses inside a sentence of at least {int(MIN_BREAK * 1000)} ms, capped at {int(MAX_PAUSE * 1000)} ms.",
           "     n: the sentence's number in the script, counting headings. -->"]
    for n in sorted(plans):
        plan = plans[n]
        parts = []
        for i, w in enumerate(plan["words"]):
            parts.append(f'<prosody pitch="+{BOOST[0]:g}st" volume="+{BOOST[1]:g}dB">{escape(w)}</prosody>'
                         if i in plan["stressed"] else escape(w))
            if i in plan["breaks"]:
                parts.append(f'<break time="{round(plan["breaks"][i] * 100) * 10}ms"/>')
        out.append(f'<s n="{n}"><prosody rate="{plan["rate"]:.0f}%">{" ".join(parts)}</prosody></s>')
    out.append("</speak>")
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    # Usage: prosody.py STEM   (from video/, in video/.venv) writes video/prosody/STEM.ssml
    import os
    import sys
    from pathlib import Path

    from kokoro_onnx import Kokoro

    stem = sys.argv[1]
    here = Path(__file__).resolve().parent
    voice = os.environ.get("BASE", "bm_fable")
    kokoro = Kokoro(str(here.parent / ".kokoro" / "kokoro-v1.0.onnx"), str(here.parent / ".kokoro" / "voices-v1.0.bin"))
    clips = here / "hanh" / stem
    sentences = [s for p in (here / "scripts" / f"{stem}.txt").read_text().split("\n\n") if re.search(r"[A-Za-z]", p)
                 for s in re.split(r"(?<=[.!?])\s+", p.strip())]
    plans = {}
    for n, sentence in enumerate(sentences, 1):
        clip = clips / f"{n:03d}.wav"
        if not clip.exists():
            continue
        samples, rate = kokoro.create(sentence, voice=voice, speed=1.0, lang="en-gb" if voice[0] == "b" else "en-us")
        try:
            plans[n] = measure(samples, load(clip, rate), sentence, rate)
        except Exception as e:
            print(f"  sentence {n}: could not measure ({type(e).__name__})", flush=True)
        if n % 50 == 0:
            print(f"{n}/{len(sentences)}", flush=True)
    target = here / "prosody" / f"{stem}.ssml"
    target.parent.mkdir(exist_ok=True)
    target.write_text(to_ssml(plans, voice, f"video/hanh/{stem}"))
    print(f"wrote {target.relative_to(here.parent)}: {len(plans)} of {len(sentences)} sentences", flush=True)
