"""Cut a one-take recording of a chapter into cleaned clips, one per script sentence.

Usage: takes.py STEM [--debug N]

Reads audio/hanh/STEM.wav, the script audio/scripts/STEM.txt, and any pickup
recordings audio/hanh/STEM-pickups*.wav, each with its reading list in the .txt
of the same name (numbered sentences, in the order they were read). A later
pickup file wins over an earlier one.
Writes one clip per sentence to audio/hanh/STEM/NNN.wav, a manifest.tsv beside
them, and prints the sentences that still need a retake. The manifest gives each
clip's source recording and times, how well the reading matched the script
(score), how well the finished clip matches when transcribed again (clip score),
the reader's pause after it where that could be measured, and what the
transcription heard. --debug N explains sentence N instead.

Finding the sentences. Two Whisper models transcribe each recording (large-v3-turbo
through MLX, and base.en), because each one mishears different words. Whisper
only guesses when each word was spoken, so a forced aligner (wav2vec2) then finds
each transcript word's true place in the audio. The transcript is aligned to the
script, and the words between a sentence's neighbours are its attempts. A
sentence's clip is its last complete attempt, or its last attempt if none is
complete. A pickup recording's reading replaces the main take's. Readings that
match the script below MISREAD are reported as retakes to record.

Cleaning. The whole recording goes once through a high-pass filter, a de-clicker
and a mild noise reducer. Each clip runs from its first word to its last, with up
to MARGIN of room tone kept on either side. Pauses longer than LONG_PAUSE inside
it are shortened to PAUSE, and its speech is brought to LEVEL. The pauses between
sentences are measured and left to render.py, which keeps the reader's own.
"""
import difflib
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

import numpy as np
import soundfile as sf

MISREAD = 0.85  # similarity below which a reading is reported for a retake
COMPLETE = 0.8  # similarity from which a reading counts as a whole attempt
MARGIN, LONG_PAUSE, PAUSE = 0.15, 0.6, 0.4  # seconds; pauses inside a sentence longer than LONG_PAUSE shrink to PAUSE
LEAD, TRAIL, FADE = 0.06, 0.08, 0.01  # seconds before a first word, after a last word, and of fade at each end
LEVEL = -20.0  # dBFS, RMS of the speech
FRAME = 0.01  # seconds, for the loudness envelope
PACE = 14  # characters per second this speaker reads at, for expected clip lengths

stem = sys.argv[1]
debug = int(sys.argv[sys.argv.index("--debug") + 1]) - 1 if "--debug" in sys.argv else None
here = Path(__file__).resolve().parent
takes = here / "hanh"
sentences = [s for p in (here / "scripts" / f"{stem}.txt").read_text().split("\n\n") if re.search(r"[A-Za-z]", p)
             for s in re.split(r"(?<=[.!?])\s+", p.strip())]

from whisper.normalizers import EnglishTextNormalizer  # noqa: E402

normalize = EnglishTextNormalizer()


def distance(a, b):
    row = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        diagonal, row[0] = row[0], i
        for j, y in enumerate(b, 1):
            diagonal, row[j] = row[j], min(row[j] + 1, row[j - 1] + 1, diagonal + (x != y))
    return row[-1]


def similarity(text, heard):
    want = normalize(text).replace(" ", "")
    return 1 - distance(want, normalize(heard).replace(" ", "")) / max(len(want), 1)


def spell(n):
    """A number in words, since the aligner knows only letters."""
    ones = ("zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen "
            "fifteen sixteen seventeen eighteen nineteen").split()
    tens = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()
    if n < 20:
        return ones[n]
    if n < 100:
        return tens[n // 10] + ("" if n % 10 == 0 else " " + ones[n % 10])
    if n < 1000:
        return ones[n // 100] + " hundred" + ("" if n % 100 == 0 else " " + spell(n % 100))
    return spell(n // 1000) + " thousand" + ("" if n % 1000 == 0 else " " + spell(n % 1000))


def letters(word):
    """A word as the aligner's labels: capital letters and apostrophes, digits spelled out."""
    word = re.sub(r"\d+", lambda m: " " + spell(int(m.group())) + " ", word.replace(",", ""))
    return re.sub(r"[^A-Z']", "", word.upper())


class Aligner:
    """Finds where each word of a known text is spoken, by wav2vec2 forced alignment."""

    def __init__(self):
        import torchaudio

        self.bundle = torchaudio.pipelines.WAV2VEC2_ASR_BASE_960H
        self.model = self.bundle.get_model().eval()
        self.index = {c: i for i, c in enumerate(self.bundle.get_labels())}

    def align(self, audio, rate, words):
        """Each word's (start, end) in seconds within the audio, or None when the words don't fit it."""
        import torch
        import torchaudio
        from torchaudio.functional import forced_align, merge_tokens

        tokens, owner = [], []
        for i, word in enumerate(words):
            for c in letters(word):
                tokens.append(self.index[c])
                owner.append(i)
            tokens.append(self.index["|"])
            owner.append(None)
        tokens, owner = tokens[:-1], owner[:-1]
        if not tokens or len(audio) < rate * 0.1:
            return None
        x = torchaudio.functional.resample(torch.from_numpy(np.ascontiguousarray(audio)), rate, 16000)
        with torch.inference_mode():
            emission, _ = self.model(x[None])
            emission = emission.log_softmax(-1)
        if emission.shape[1] < len(tokens) * 2:
            return None
        try:
            labels, scores = forced_align(emission, torch.tensor([tokens], dtype=torch.int32), blank=0)
        except RuntimeError:
            return None
        spans = merge_tokens(labels[0], scores[0].exp(), blank=0)
        if len(spans) != len(tokens):
            return None
        per_frame = len(x) / 16000 / emission.shape[1]
        times, confidence = [None] * len(words), [[] for _ in words]
        for k, span in enumerate(spans):
            if owner[k] is None:
                continue
            first = times[owner[k]][0] if times[owner[k]] else span.start * per_frame
            times[owner[k]] = (first, span.end * per_frame)
            confidence[owner[k]].append(span.score)
        if np.mean([c for cs in confidence for c in cs]) < 0.3:  # the words were not really said here
            return None
        # A word the aligner could not place, such as a hallucinated one, keeps its rough time.
        return [t if cs and np.mean(cs) >= 0.2 else None for t, cs in zip(times, confidence)]


def transcribe(wav, recording):
    """Return the two transcripts' words as (word, start, end), computing and caching each once.

    Whisper's own word times are replaced by the forced aligner's wherever the
    aligner finds the segment's words in the audio.
    """
    results = []
    for model in ("turbo", "base"):
        cache = wav.with_suffix(f".{model}.json")
        if not cache.exists() or cache.stat().st_mtime < wav.stat().st_mtime:
            print(f"transcribing {wav.name} with {model}", flush=True)
            if model == "turbo":
                import mlx_whisper
                r = mlx_whisper.transcribe(str(wav), path_or_hf_repo="mlx-community/whisper-large-v3-turbo",
                                           word_timestamps=True, language="en")
            else:
                import whisper
                r = whisper.load_model("base.en").transcribe(str(wav), fp16=False, word_timestamps=True)
            cache.write_text(json.dumps(r["segments"]))
        aligned = wav.with_suffix(f".{model}.aligned.json")
        if not aligned.exists() or aligned.stat().st_mtime < cache.stat().st_mtime:
            print(f"aligning the {model} transcript of {wav.name}", flush=True)
            words = []
            segments = [[(w["word"].strip(), w["start"], w["end"]) for w in seg["words"]]
                        for seg in json.loads(cache.read_text())]
            segments = [seg for seg in segments if seg]
            for seg_words, following in zip(segments, segments[1:] + [None]):
                # Each segment is aligned within its own stretch of audio, padded a little
                # but never into the words already placed before it, or the first word
                # could latch onto the end of the previous sentence.
                lo = max(0.0, seg_words[0][1] - 0.5, words[-1][2] if words else 0.0)
                hi = min(seg_words[-1][2] + 0.5, following[0][1] + 0.2 if following else np.inf)
                audio = recording.audio[int(lo * recording.rate):int(hi * recording.rate)]
                times = aligner.align(audio, recording.rate, [w for w, _, _ in seg_words]) if hi > lo else None
                for i, (word, start, end) in enumerate(seg_words):
                    if times and times[i]:
                        start, end = lo + times[i][0], lo + times[i][1]
                    if words and start < words[-1][2]:  # keep the transcript's order in time
                        start = words[-1][2]
                        end = max(end, start)
                    words.append((word, start, end))
            aligned.write_text(json.dumps(words))
        results.append([tuple(w) for w in json.loads(aligned.read_text())])
    return results


def attempts(words, order):
    """For each sentence (by index into `order`), list its readings as (similarity, start, end), in time order."""
    heard = [normalize(w) for w, _, _ in words]
    squashed = [h.replace(" ", "") for h in heard]
    script, owner = [], []
    for k, i in enumerate(order):
        for w in normalize(sentences[i]).split():
            script.append(w)
            owner.append(k)
    # A monotonic alignment anchors each sentence somewhere in the transcript. Only
    # runs of a few words count, since a stray "the" matches anywhere.
    anchor = [None] * len(order)
    for a, b, n in difflib.SequenceMatcher(None, script, heard, autojunk=False).get_matching_blocks():
        if n < 3:
            continue
        for j in range(a, a + n):
            lo, hi = anchor[owner[j]] or (b, b)
            anchor[owner[j]] = (min(lo, b + j - a), max(hi, b + j - a + 1))
    found = []
    for k, i in enumerate(order):
        want = normalize(sentences[i]).replace(" ", "")
        n = owner.count(k)
        # Everything between the neighbours' anchors is attempts at this sentence.
        lo = max((anchor[j][1] for j in range(k) if anchor[j]), default=0)
        hi = min((anchor[j][0] for j in range(k + 1, len(order)) if anchor[j]), default=len(heard))
        if anchor[k]:
            lo, hi = min(lo, anchor[k][0]), max(hi, anchor[k][1])
        windows = []
        for a in range(lo, max(lo, hi - n // 2) + 1):
            # The transcript may use more words than the normalized script, as "4, 11, 3"
            # for "four, eleven, three", so try windows up to half as long again.
            for b in {min(hi, a + n + d) for d in range(-2, n // 2 + 4)}:
                if b > a:
                    got = "".join(squashed[a:b])
                    windows.append((1 - distance(want, got) / max(len(want), 1), a, b))
        windows.sort(key=lambda w: -w[0])
        readings = []  # distinct readings start at least half a sentence apart
        for score, a, b in windows:
            if score < max(0.6, windows[0][0] - 0.35):
                break
            if all(abs(a - a2) > max(2, n // 2) for _, a2, _ in readings):
                readings.append((score, a, b))
        readings.sort(key=lambda r: r[1])
        found.append([(score, words[a][1], words[b - 1][2]) for score, a, b in readings])
    return found


def choose(text, per_model):
    """Order the two transcripts' readings of a sentence by preference, as (score, start, end, note).

    The first is the one to cut; the rest are tried when its clip fails the check.
    """
    readings = [r for one in per_model for r in one]
    if not readings:
        return []
    complete = [r for r in readings if r[0] >= COMPLETE]
    last = max(complete or readings, key=lambda r: r[1])
    # The two transcripts hear the same reading at about the same time. Prefer
    # the better score, then the likelier length.
    near = [r for r in readings if abs(r[1] - last[1]) < 1.5]
    expected = len(text) / PACE
    pick = max(near, key=lambda r: (r[0], -abs(r[2] - r[1] - expected)))
    best = max(readings, key=lambda r: r[0])
    note = "an earlier reading scored higher" if best[0] > pick[0] + 0.1 else ""
    others = sorted((r for r in readings if r != pick), key=lambda r: (r[0] < COMPLETE, -r[1]))
    return [(*pick, note)] + [(*r, "fell back to another reading") for r in others]


def clean(wav):
    """Filter the whole recording once, and return it as float32 with its rate.

    The filters delay the sound by a few tens of milliseconds, so the result is
    shifted back to line up with the original's times.
    """
    from scipy.signal import correlate

    target = wav.with_suffix(".clean.wav")
    if not target.exists() or target.stat().st_mtime < wav.stat().st_mtime:
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(wav),
                        "-af", "highpass=f=80,adeclick,afftdn=nf=-60:nr=10", str(target)], check=True)
    raw, rate = sf.read(wav, dtype="float32")
    audio, _ = sf.read(target, dtype="float32")
    a, b = len(raw) // 2, len(raw) // 2 + 10 * rate
    lag = int(np.argmax(correlate(audio[a:b], raw[a:b], mode="full", method="fft"))) - (b - a - 1)
    return np.concatenate([audio[max(lag, 0):], np.zeros(max(lag, 0), np.float32)]), rate


class Recording:
    """A cleaned recording with its loudness envelope."""

    def __init__(self, wav):
        self.audio, self.rate = clean(wav)
        self.step = int(FRAME * self.rate)
        frames = self.audio[: len(self.audio) // self.step * self.step].reshape(-1, self.step)
        self.env = 20 * np.log10(np.sqrt((frames ** 2).mean(axis=1)) + 1e-9)
        self.quiet = self.env < np.percentile(self.env, 10) + 22  # room tone, below breaths and word tails

    def cut(self, start, end):
        """Cut a clip from the first word's onset to the last word's end, tidy its pauses, and level it.

        Returns the clip, the time in the recording where it begins, and the room
        tone it keeps before and after the speech, in seconds.
        """
        env, quiet, step = self.env, self.quiet, self.step
        first = max(0, int((start - LEAD) / FRAME))
        last = min(len(env), int((end + TRAIL) / FRAME))
        if last <= first:
            return None
        # Keep room tone around the speech, as far as it is quiet, up to MARGIN.
        before = 0
        while before < min(int(MARGIN / FRAME), first) and quiet[first - before - 1]:
            before += 1
        after = 0
        while after < min(int(MARGIN / FRAME), len(env) - last) and quiet[last + after]:
            after += 1
        # Shrink long pauses inside the speech to PAUSE.
        long, half = int(LONG_PAUSE / FRAME), int(PAUSE / FRAME) // 2
        segments, begin, run = [], first - before, 0
        for f in range(first, last):
            if quiet[f]:
                run += 1
                continue
            if run >= long:
                segments.append((begin, f - run + half))
                begin = f - half
            run = 0
        segments.append((begin, last + after))
        clip = self.audio[segments[0][0] * step:segments[0][1] * step]
        for s, e in segments[1:]:  # join with a short crossfade, so the cut is silent
            piece = self.audio[s * step:e * step]
            n = int(0.01 * self.rate)
            ramp = np.linspace(0, 1, n, dtype=np.float32)
            clip = np.concatenate([clip[:-n], clip[-n:] * (1 - ramp) + piece[:n] * ramp, piece[n:]])
        speech = env[first:last][~quiet[first:last]]
        if len(speech) == 0:
            return None
        gain = 10 ** ((LEVEL - 10 * np.log10(np.mean(10 ** (speech / 10)))) / 20)
        gain = min(gain, 0.95 / (np.abs(clip).max() + 1e-9))
        clip = clip * gain
        fade = min(int(FADE * self.rate), len(clip) // 2)
        clip[:fade] *= np.linspace(0, 1, fade, dtype=np.float32)
        clip[-fade:] *= np.linspace(1, 0, fade, dtype=np.float32)
        return clip, (first - before) * FRAME, (before * FRAME, after * FRAME)


def heard_in(clip, rate):
    """Transcribe a finished clip, returning its text and words as (word, start, end).

    Transcribing is the slow step, so results are kept by the clip's content in
    audio/hanh/STEM/checks.json, and a rerun only transcribes clips that changed.
    """
    import mlx_whisper
    from scipy.signal import resample_poly

    key = hashlib.sha1(clip.tobytes()).hexdigest()
    if key not in checks:
        audio = resample_poly(clip, 160, 441).astype(np.float32)
        r = mlx_whisper.transcribe(audio, path_or_hf_repo="mlx-community/whisper-large-v3-turbo",
                                   language="en", word_timestamps=True)
        checks[key] = [r["text"].strip(), [(w["word"].strip(), w["start"], w["end"])
                                           for s in r["segments"] for w in s["words"]]]
        checks_file.write_text(json.dumps(checks))
    return checks[key]


def spill(text, heard):
    """Whether the clip's transcription has extra words before the sentence's first or after its last.

    A misheard first or last word ("the" for "a") is not a spill; words before a
    correctly heard first word, or after a correctly heard last word, are.
    """
    want, got = normalize(text).split(), normalize(heard).split()
    blocks = [b for b in difflib.SequenceMatcher(None, want, got, autojunk=False).get_matching_blocks() if b.size]
    if not want or not blocks:
        return False
    first, last = blocks[0], blocks[-1]
    return (first.a == 0 and first.b > 0) or (last.a + last.size == len(want) and last.b + last.size < len(got))


def restart(text, words):
    """The index of the word that last restarts a sentence inside a clip, when its opening recurs."""
    opening = " ".join(normalize(text).split()[:5])
    starts, i = [], 0
    while i < len(words):
        if similarity(opening, " ".join(x[0] for x in words[i:i + 5])) >= 0.7:
            starts.append(i)
            i += 5  # past this occurrence, so its own later words don't count again
        else:
            i += 1
    return starts[-1] if len(starts) > 1 else None


aligner = Aligner()
main = Recording(takes / f"{stem}.wav")
order = list(range(len(sentences)))
per_model = [attempts(words, order) for words in transcribe(takes / f"{stem}.wav", main)]
chosen = [(choose(sentences[k], [m[k] for m in per_model]), main) for k in order]

for pickups in sorted(f for f in takes.glob(f"{stem}-pickups*.wav") if not f.stem.endswith(".clean")):
    listed = [int(n) - 1 for n in re.findall(r"^(\d+)\. ", pickups.with_suffix(".txt").read_text(), re.M)]
    extra = Recording(pickups)
    per_model = [attempts(words, listed) for words in transcribe(pickups, extra)]
    for j, k in enumerate(listed):
        candidates = choose(sentences[k], [m[j] for m in per_model])
        if candidates and candidates[0][0] >= MISREAD:
            chosen[k] = (candidates, extra)

out = takes / stem
out.mkdir(exist_ok=True)
checks_file = out / "checks.json"
checks = json.loads(checks_file.read_text()) if checks_file.exists() else {}
rows, retakes, cuts = [], [], {}
for k, (candidates, recording) in enumerate(chosen):
    text = sentences[k]
    source = "main" if recording is main else "pickups"
    if debug is not None and k != debug:
        continue
    if debug is not None:
        print(f"{source}: candidates {candidates}")
    if not candidates:
        rows.append((k + 1, "", "", "", "", "", "not found", text, ""))
        retakes.append(k)
        continue
    best = None
    for score, start, end, note in candidates[:3]:
        cut = recording.cut(start, end)
        if cut is None:
            continue
        clip, origin, margins = cut
        heard, words = heard_in(clip, recording.rate)
        again = restart(text, words)
        if again is not None:
            # The reader started the sentence over inside this stretch, so keep the last start.
            times = aligner.align(clip, recording.rate, [w for w, _, _ in words])
            at = times[again][0] if times and times[again] else words[again][1]
            if recording.cut(origin + at, end):
                clip, origin, margins = recording.cut(origin + at, end)
                heard, words = heard_in(clip, recording.rate)
                note = (note + "; " if note else "") + "cut from a restart"
        final = similarity(text, heard)
        if debug is not None:
            print(f"  cut {start:.2f}-{end:.2f} -> clip from {origin:.2f}, {len(clip) / recording.rate:.2f}s, "
                  f"restart at {again}\n  heard: {heard}")
        clean_edges = not spill(text, heard)
        if best is None or (clean_edges, final) > (best[0], best[1]):
            best = (clean_edges, final, clip, heard, score, start, end, note, margins)
        if final >= MISREAD and clean_edges:
            break
    if best is None:
        rows.append((k + 1, source, "", "", "", "", "no speech found", text, ""))
        retakes.append(k)
        continue
    _, final, clip, heard, score, start, end, note, margins = best
    sf.write(out / f"{k + 1:03d}.wav", clip, recording.rate)
    cuts[k] = (recording, start, end, margins)
    pace = len(text) / (len(clip) / recording.rate)
    if not 7 < pace < 19 and len(text) > 30 and final < 0.95:  # a stumble or a bad cut shows as an odd length
        note = (note + "; " if note else "") + "check length"
    if max(score, final) < MISREAD:
        note = (note + "; " if note else "") + "retake"
        retakes.append(k)
    elif final < MISREAD or spill(text, heard):
        note = (note + "; " if note else "") + "check cut"
    rows.append((k + 1, source, f"{start:.2f}", f"{end:.2f}", f"{score:.2f}", f"{final:.2f}", note, text, heard))
    print(f"\r{k + 1}/{len(sentences)}", end="", flush=True)
print()
if debug is not None:
    sys.exit()
# The reader's own pause after each sentence, beyond the room tone the clips keep,
# where the next sentence follows it in the same recording.
pauses = {}
for k in cuts:
    if k + 1 in cuts and cuts[k][0] is cuts[k + 1][0] and cuts[k][2] <= cuts[k + 1][1] <= cuts[k][2] + 5:
        pauses[k] = max(0.0, cuts[k + 1][1] - cuts[k][2] - cuts[k][3][1] - cuts[k + 1][3][0])
rows = [(*r[:7], f"{pauses[r[0] - 1]:.2f}" if r[0] - 1 in pauses else "", *r[7:]) for r in rows]
(out / "manifest.tsv").write_text("n\tsource\tstart\tend\tscore\tclip score\tnote\tpause\ttext\theard\n"
                                  + "".join("\t".join(map(str, r)) + "\n" for r in rows))
print(f"{len(rows) - len(retakes)} of {len(sentences)} sentences cut to {out}")
if retakes:
    print(f"{len(retakes)} to record again:")
    for k in retakes:
        print(f"  {k + 1}. {sentences[k]}")
