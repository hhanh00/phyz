"""Render listening scripts to AAC with Kokoro, one chapter at a time.

Usage: render.py MODEL_DIR SCRIPTS_DIR OUT_DIR [--force] [--only STEM]

The environment variables VOICE (default am_michael) and SPEED (default 1.0)
choose the Kokoro voice and pace. VOICE=hanh instead uses the recorded clips that
takes.py cut into video/hanh/STEM/, one per sentence, separated by SENTENCE_PAUSE
of silence, and has Kokoro's FILL voice read any sentence that has no clip.
VOICE=transfer has Kokoro's BASE voice read every sentence, reshaped by prosody.py
to the timing, pitch and stress of the recorded clip where there is one; it needs
the video/.venv environment, which has torch and Praat.

VOICE=azure has an Azure Speech voice read every sentence once (see azure_tts.py).
A voice left to itself reads long stretches without a breath, so the text it gets
carries extra commas where a reader would pause. If video/prosody/STEM.pauses.txt
exists, it is the script with those commas written in, and no recording is needed:
the chapter title is read, the section headings are not, and the silence after a
sentence is PAUSE_INSIDE within a paragraph and PAUSE_AFTER at its end. Without
that file the commas go wherever the recorded clip pauses, and the silence after
each sentence is the reader's own, from the clips' manifest.tsv. Either way the
pace, the stress and the length of a pause inside a sentence are the voice's.

Skips chapters whose .m4a is newer than their script, so an interrupted run
can restart, and an edited script re-renders on the next run. Writes each
sentence's timing to video/timings/STEM.json for the slide videos.
"""
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

import numpy as np
import soundfile as sf

VOICE = os.environ.get("VOICE", "am_michael")
FILL = os.environ.get("FILL", "am_michael")
BASE = os.environ.get("BASE", "bm_fable")
SPEED = float(os.environ.get("SPEED", "1.0"))
RECORDED = VOICE == "hanh"
TRANSFER = VOICE == "transfer"
AZURE = VOICE == "azure"
GUIDED = TRANSFER or AZURE  # a synthetic voice that follows the recorded clips
if TRANSFER:
    import prosody
if AZURE:
    import azure_tts
RATE = 44100 if RECORDED else 24000  # the recordings' rate, or Kokoro's
HEADING_MAX_WORDS = 7
SENTENCE_PAUSE = 1.0  # seconds between recorded sentences, headings and paragraphs included
PAUSE_INSIDE, PAUSE_AFTER = 0.9, 1.5  # seconds after a sentence within a paragraph and at its end, for a pause file
model_dir, scripts_dir, out_dir = map(Path, sys.argv[1:4])
force = "--force" in sys.argv
only = sys.argv[sys.argv.index("--only") + 1] if "--only" in sys.argv else None
out_dir.mkdir(parents=True, exist_ok=True)
kokoro = None  # loaded on first use, so the Azure voice runs without Kokoro installed


def kokoro_voice():
    global kokoro
    if kokoro is None:
        from kokoro_onnx import Kokoro
        kokoro = Kokoro(str(model_dir / "kokoro-v1.0.onnx"), str(model_dir / "voices-v1.0.bin"))
    return kokoro
takes = Path(__file__).resolve().parent / "hanh"
filled = failed = 0
written = None  # the current chapter's sentences from its pause file, when it has one


def silence(seconds):
    return np.zeros(int(seconds * RATE), dtype=np.float32)


def split(text):
    """The script's paragraphs that hold speech, each as its list of sentences."""
    return [re.split(r"(?<=[.!?])\s+", p.strip()) for p in text.split("\n\n") if re.search(r"[A-Za-z]", p)]


def written_pauses(stem, text):
    """{sentence number: the sentence with its extra commas} from video/prosody/STEM.pauses.txt, or None.

    The file has to be the script itself with nothing changed but commas added after
    words, so an edit to the script that the pause file missed stops the render.
    """
    path = Path(__file__).resolve().parent / "prosody" / f"{stem}.pauses.txt"
    if not path.exists():
        return None
    plain = [s for para in split(text) for s in para]
    marked = [s for para in split(path.read_text()) for s in para]
    if len(plain) != len(marked):
        raise SystemExit(f"{path.name} has {len(marked)} sentences and the script has {len(plain)}")
    for number, (a, b) in enumerate(zip(plain, marked), 1):
        words, with_commas = a.split(), b.split()
        if len(words) != len(with_commas) or any(m not in (w, w + ",") for w, m in zip(words, with_commas)):
            raise SystemExit(f"{path.name}, sentence {number} differs from the script by more than commas:\n  {a}\n  {b}")
    return dict(enumerate(marked, 1))


def speak(sentence, stem, number):
    """The sentence's audio: its recorded clip, a synthetic voice shaped to that clip, or the voice's own reading."""
    global filled, failed
    clip = takes / stem / f"{number:03d}.wav"
    if RECORDED and clip.exists():
        return sf.read(clip, dtype="float32")[0]
    if AZURE and written is not None:
        return azure_tts.trimmed(azure_tts.read(azure_tts.spoken(written[number])))
    if AZURE:
        import prosody
        after = set()
        if clip.exists():
            try:
                after = prosody.pauses(prosody.load(clip, RATE), sentence, RATE)
            except Exception as e:  # an alignment that fails leaves the sentence as written
                print(f"  sentence {number}: read as written ({type(e).__name__})", flush=True)
                failed += 1
        else:
            filled += 1
        return azure_tts.trimmed(azure_tts.read(azure_tts.paused(sentence, after)))
    voice = BASE if TRANSFER else FILL if RECORDED else VOICE
    lang = "en-gb" if voice.startswith("b") else "en-us"
    samples, rate = kokoro_voice().create(sentence, voice=voice, speed=SPEED, lang=lang)
    if TRANSFER:
        if not clip.exists():
            filled += 1
            return samples
        try:
            return prosody.transfer(samples, prosody.load(clip, rate), sentence, rate)
        except Exception as e:  # an alignment that fails leaves Kokoro's own reading
            print(f"  sentence {number}: kept Kokoro's reading ({type(e).__name__})", flush=True)
            failed += 1
            return samples
    if rate != RATE:  # a stopgap sentence among recorded ones, so plain interpolation will do
        samples = np.interp(np.arange(0, len(samples), rate / RATE), np.arange(len(samples)), samples)
        samples = samples.astype(np.float32)
        filled += 1
    return samples


def render(text, stem):
    """Return the audio and each sentence's start and end time in seconds."""
    chunks, timings, position, number = [], [], 0, 0
    global written
    written = written_pauses(stem, text) if AZURE else None
    own = {}
    if AZURE and written is None:
        import prosody
        own = prosody.sentence_gaps(takes / stem / "manifest.tsv")
    first = True

    def add(samples):
        nonlocal position
        chunks.append(samples)
        position += len(samples)

    def gap(fixed):
        """Silence after a sentence: one fixed pause for a recorded voice, Kokoro's pattern otherwise."""
        return SENTENCE_PAUSE if RECORDED or GUIDED else fixed

    for para in (p.strip() for p in text.split("\n\n")):
        if not re.search(r"[A-Za-z]", para):  # a line of symbols is a reading marker, not speech
            continue
        is_heading = len(para.split()) <= HEADING_MAX_WORDS
        title, first = first, False
        if is_heading and not (RECORDED or GUIDED):
            add(silence(0.9))
        sentences = re.split(r"(?<=[.!?])\s+", para)
        for i, sentence in enumerate(sentences):
            number += 1
            unread = is_heading and not title if written is not None else \
                is_heading and (RECORDED or GUIDED) and not (takes / stem / f"{number:03d}.wav").exists()
            if unread:
                # A heading the narrator chose not to read stays silent; its slide still starts here.
                timings.append({"text": sentence, "start": position / RATE, "end": position / RATE, "heading": True})
                continue
            samples = speak(sentence, stem, number)
            begin = position / RATE
            add(samples)
            timings.append({"text": sentence, "start": begin, "end": position / RATE, "heading": is_heading})
            last = i == len(sentences) - 1
            if written is not None:
                add(silence(PAUSE_AFTER if last else PAUSE_INSIDE))
            else:
                add(silence(own.get(number, gap(0.12 + (0.7 if is_heading else 0.35) if last else 0.12))))
    return np.concatenate(chunks), timings


total = 0.0
timings_dir = out_dir.parent / "timings"
timings_dir.mkdir(exist_ok=True)
for script in sorted(scripts_dir.glob("*.txt")):
    if only and script.stem != only:
        continue
    target = out_dir / script.stem / f"{script.stem}.m4a"
    target.parent.mkdir(exist_ok=True)
    if not force and target.exists() and target.stat().st_mtime > script.stat().st_mtime:
        print(f"skip {script.stem}", flush=True)
        continue
    start, filled, failed = time.time(), 0, 0
    audio, timings = render(script.read_text(), script.stem)
    (timings_dir / f"{script.stem}.json").write_text(json.dumps(timings, indent=1))
    wav = target.with_suffix(".wav")
    sf.write(wav, audio, RATE)
    subprocess.run(
        ["afconvert", "-f", "m4af", "-d", "aac", "-b", "64000", str(wav), str(target)],
        check=True,
    )
    wav.unlink()
    seconds = len(audio) / RATE
    total += seconds
    gaps = f", {filled} sentences read by Kokoro" if RECORDED else ""
    if TRANSFER:
        gaps = f", {filled} sentences without a recording, {failed} transfers that fell back to Kokoro"
    if AZURE and written is not None:
        gaps = f", pauses from prosody/{script.stem}.pauses.txt, {azure_tts.requested} characters sent to Azure"
        azure_tts.requested = 0
    elif AZURE:
        gaps = (f", {filled} sentences without a recording, {failed} read as written after a failed alignment, "
                f"{azure_tts.requested} characters sent to Azure")
        azure_tts.requested = 0
    print(f"done {script.stem}: {seconds/60:.1f} min audio in {(time.time()-start)/60:.1f} min{gaps}", flush=True)

print(f"finished: {total/3600:.2f} h rendered this run", flush=True)
