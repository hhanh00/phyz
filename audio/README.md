# Audio and video

Each chapter in `docs/` can have a listening script in `scripts/` and an animated slide deck in `slides/`. From these, the tools here produce a narrated video with subtitles. They were copied from the Ragu and Tachyon site's `audio/` folder, which uses the same pipeline.

| Step | Tool | Output in `audio/out/` |
| --- | --- | --- |
| Narration | `render.py`, with an Azure Speech voice (`azure_tts.py`) | `STEM.m4a`, plus sentence timings in `audio/timings/STEM.json` |
| Slides | `slides/build.py` (Manim), timed to the narration | `STEM-slides.mp4`, silent |
| Subtitles | `slides/subtitles.py` | `STEM-slides.srt` and `STEM-slides-subtitled.mp4` |
| Cover | `slides/cover.py` | `STEM-cover.png`, held for the video's first seconds |
| Final video | `make_video.sh` (ffmpeg) | `STEM-video.mp4` and `STEM-video.srt`, timed to the final video |

`STEM` is a script's file name without `.txt`, such as `01-classical-mechanics`. The deck for it is `slides/deck_01.py`, named by the stem's first two digits. Everything in `audio/out/`, `audio/timings/` and `audio/azure-cache/` is generated and not committed.

`BRIEF.md` covers writing scripts, `REVIEW.md` checking them against their chapters, and `slides/BRIEF.md` writing decks.

## One-time setup

Run these from the repository root. You need [uv](https://docs.astral.sh/uv/) and ffmpeg (`brew install ffmpeg`).

The Manim environment, which the site's diagrams already use, also renders the slides. The slides need two more packages:

```sh
uv pip install --python .manim-venv/bin/python av pillow
```

The narration runs in its own small environment:

```sh
uv venv audio/.venv --python 3.12
uv pip install --python audio/.venv/bin/python numpy soundfile
```

The Azure key and region are read from `~/.azure-speech`, a file with two lines:

```
AZURE_SPEECH_KEY=...
AZURE_SPEECH_REGION=eastus
```

`AZURE_VOICE` chooses the voice (default `en-US-BrianNeural`). Each sentence is read once and cached in `audio/azure-cache/`, so a re-render only pays for sentences that changed. If the voice mispronounces a word, add it to `PRONOUNCE` in `azure_tts.py`.

## Breath pauses

A voice left to itself reads long stretches without a breath. Before rendering a chapter, write `audio/prosody/STEM.pauses.txt`: the script with extra commas where a reader would pause, and no other change. `render.py` refuses a pause file that differs from the script by anything but added commas. With a pause file, the chapter title is read, section headings are silent, and the silence after a sentence is 0.9 s within a paragraph and 1.5 s at its end.

## Making a video

```sh
VOICE=azure audio/make_video.sh 01-classical-mechanics
```

After a change to a deck but not to its script, skip the narration:

```sh
audio/make_video.sh --skip-audio 01-classical-mechanics
```

Any change to a script needs the narration rendered again, because the slides are timed to it.

To check a deck before any audio exists, render the last frame of every slide to contact sheets:

```sh
cd audio/slides
../../.manim-venv/bin/python build.py deck_01 preview
../../.manim-venv/bin/python build.py deck_01 preview --only 4,5
../../.manim-venv/bin/python check.py 01
```

`check.py` reports slide anchors that no longer match the script, and format problems in the script.

## Other voices

`render.py` and `takes.py` also support the Kokoro voice and a narration recorded by hand, as on the Ragu and Tachyon site. Those modes need the Kokoro model files and a larger environment with torch and Praat; see that site's `audio/README.md` before using them.
