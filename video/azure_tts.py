"""Azure Speech as a narration voice: one request per sentence, cached on disk.

The key and region come from ~/.azure-speech, which holds two lines:

    AZURE_SPEECH_KEY=...
    AZURE_SPEECH_REGION=eastus

AZURE_VOICE (default en-US-BrianNeural) chooses the voice. The voice reads each
sentence as written, with one addition: a comma wherever the reader's recording
pauses, so that it breathes where the reader did (see paused()). Each reading is cached in
video/azure-cache/ under a hash of the voice and the SSML sent, so a re-render only
pays for sentences whose text or prosody changed.
"""
import hashlib
import http.client
import io
import os
import re
import time
import urllib.error
import urllib.request
from pathlib import Path
from xml.sax.saxutils import escape

import numpy as np
import soundfile as sf

VOICE = os.environ.get("AZURE_VOICE", "en-US-BrianNeural")
RATE = 24000
CACHE = Path(__file__).resolve().parent / "azure-cache"
requested = 0  # characters sent to Azure in this run, cached readings excluded
# Words the voice misreads, with the pronunciation to use in IPA. Matching ignores case.
# A possessive needs its own entry, because the voice reads an 's left outside the phoneme as a separate word.
PRONOUNCE = {}  # for example {"Zcash": "ˈziːkæʃ"}; add words the voice gets wrong
_MISREAD = re.compile("|".join(sorted(PRONOUNCE, key=len, reverse=True)) or "(?!)", re.IGNORECASE)
_IPA = {word.lower(): ipa for word, ipa in PRONOUNCE.items()}


def _settings():
    path = Path.home() / ".azure-speech"
    if not path.exists():
        raise SystemExit("VOICE=azure needs ~/.azure-speech with AZURE_SPEECH_KEY and AZURE_SPEECH_REGION")
    pairs = dict(line.strip().split("=", 1) for line in path.read_text().splitlines() if "=" in line)
    return pairs["AZURE_SPEECH_KEY"].strip(), pairs["AZURE_SPEECH_REGION"].strip()


def read(body):
    """Azure's reading of an SSML fragment (the content of the <voice> element) as float32 samples at RATE."""
    global requested
    ssml = (f'<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="{VOICE[:5]}">'
            f'<voice name="{VOICE}">{body}</voice></speak>')
    cached = CACHE / f"{hashlib.sha256(ssml.encode()).hexdigest()[:24]}.wav"
    if not cached.exists():
        key, region = _settings()
        request = urllib.request.Request(
            f"https://{region}.tts.speech.microsoft.com/cognitiveservices/v1",
            data=ssml.encode(),
            headers={"Ocp-Apim-Subscription-Key": key, "Content-Type": "application/ssml+xml",
                     "X-Microsoft-OutputFormat": "riff-24khz-16bit-mono-pcm", "User-Agent": "narration"})
        for attempt in range(6):
            try:
                audio = urllib.request.urlopen(request, timeout=60).read()
                break
            except urllib.error.HTTPError as e:
                if e.code not in (429, 500, 502, 503) or attempt == 5:
                    raise SystemExit(f"Azure refused the request ({e.code} {e.reason}) for: {body}")
                time.sleep(2 ** attempt)  # the free tier limits requests per minute
            except (urllib.error.URLError, http.client.IncompleteRead):  # a dropped connection
                if attempt == 5:
                    raise
                time.sleep(2 ** attempt)
        CACHE.mkdir(exist_ok=True)
        cached.write_bytes(audio)
        requested += len(body)
    return sf.read(io.BytesIO(cached.read_bytes()), dtype="float32")[0]


def trimmed(samples, keep=0.05, floor=0.01):
    """A reading without the silence Azure puts around it (about 0.2 s before and 0.8 s after)."""
    loud = np.nonzero(np.abs(samples) > floor)[0]
    if not len(loud):
        return samples
    edge = int(keep * RATE)
    out = samples[max(0, loud[0] - edge):loud[-1] + edge].copy()
    fade = min(len(out) // 2, int(0.01 * RATE))  # so a breath or a decaying tail does not end on a step
    out[:fade] *= np.linspace(0, 1, fade, dtype=np.float32)
    out[len(out) - fade:] *= np.linspace(1, 0, fade, dtype=np.float32)
    return out


def spoken(text):
    """Text escaped for SSML, with each word in PRONOUNCE wrapped in its pronunciation."""
    out, done = [], 0
    for match in _MISREAD.finditer(text):
        out.append(escape(text[done:match.start()]))
        out.append(f'<phoneme alphabet="ipa" ph="{_IPA[match.group().lower()]}">{escape(match.group())}</phoneme>')
        done = match.end()
    return "".join(out) + escape(text[done:])


def plain(sentence):
    return spoken(sentence)


def with_commas(sentence, after):
    """The sentence with a comma after each word whose index is in `after`.

    `after` comes from prosody.pauses(), which numbers only the words that contain
    letters. The comma makes the voice pause where the reader did, and lead into the
    pause the way it would at any comma. A word that already ends in punctuation is
    left as it is. Only Azure sees these commas; the script file does not change.
    """
    parts, index = [], -1
    for token in sentence.split():
        if re.search(r"[A-Za-z]", token):
            index += 1
            if index in after and token[-1] not in ",;:.!?":
                token += ","
        parts.append(token)
    return " ".join(parts)


def paused(sentence, after):
    """The SSML for a sentence that pauses after the words in `after`."""
    return spoken(with_commas(sentence, after))


if __name__ == "__main__":
    # Usage: azure_tts.py STEM   (from video/, in video/.venv) writes video/prosody/STEM.azure.txt for review:
    # the text VOICE=azure sends for each sentence, and the silence it leaves after it. Sends nothing to Azure.
    import sys

    import prosody

    stem = sys.argv[1]
    here = Path(__file__).resolve().parent
    clips = here / "hanh" / stem
    gaps = prosody.sentence_gaps(clips / "manifest.tsv")
    out, number = [], 0
    for para in (p.strip() for p in (here / "scripts" / f"{stem}.txt").read_text().split("\n\n")):
        if not re.search(r"[A-Za-z]", para):
            continue
        heading = len(para.split()) <= 7
        out.append("")
        for sentence in re.split(r"(?<=[.!?])\s+", para):
            number += 1
            clip = clips / f"{number:03d}.wav"
            if not clip.exists():
                note = "heading, not read" if heading else "no recording, read as written"
                out.append(f"{number:>4}  [{note}]  {sentence}")
                continue
            try:
                text = with_commas(sentence, prosody.pauses(prosody.load(clip, RATE), sentence, RATE))
            except Exception as e:
                text = f"[could not align ({type(e).__name__}), read as written]  {sentence}"
            gap = f"{gaps[number]:.2f} s" if number in gaps else "default"
            out.append(f"{number:>4}  {text}   [then {gap}]")
    target = here / "prosody" / f"{stem}.azure.txt"
    target.write_text("\n".join(out).lstrip("\n") + "\n")
    print(f"wrote {target.relative_to(here.parent)}")
