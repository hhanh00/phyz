#!/usr/bin/env zsh
# Regenerate a chapter's narration, slide video, subtitles and final video.
#
# Usage: audio/make_video.sh [--skip-audio] STEM [STEM ...]
#
# STEM is a script name without .txt, such as 03-statements-and-challenges.
# The deck is audio/slides/deck_NN.py, where NN is the stem's first two digits.
# Environment: VOICE, BASE and SPEED (passed to render.py; VOICE=transfer and VOICE=azure run it in audio/.venv), KOKORO (model directory,
# default .kokoro), WORK (slide clip cache, default /tmp/slides-work). If
# audio/out/STEM-cover.png exists (see slides/cover.py), the video opens on it
# for COVER seconds (default 5), then crossfades over FADE seconds (default 1).
# See audio/README.md for the one-time setup.
set -e

ROOT=${0:A:h:h}
AUDIO=$ROOT/audio
WORK=${WORK:-/tmp/slides-work}
KOKORO=${KOKORO:-$ROOT/.kokoro}
SKIP_AUDIO=0
COVER=${COVER:-5}
FADE=${FADE:-1}
if [[ $1 == --skip-audio ]]; then SKIP_AUDIO=1; shift; fi
(( $# )) || { sed -n '2,12p' $0; exit 1; }

for STEM in "$@"; do
  NN=${STEM[1,2]}
  [[ -f $AUDIO/scripts/$STEM.txt ]] || { echo "no script audio/scripts/$STEM.txt"; exit 1; }
  [[ -f $AUDIO/slides/deck_$NN.py ]] || { echo "no deck audio/slides/deck_$NN.py"; exit 1; }
  echo "== $STEM"

  if (( ! SKIP_AUDIO )); then
    # The transfer and azure modes need torch and Praat, which live in audio/.venv rather than .tts-venv.
    PY=$ROOT/.tts-venv/bin/python
    [[ ${VOICE:-} == (transfer|azure) ]] && PY=$AUDIO/.venv/bin/python
    (cd $AUDIO && $PY render.py $KOKORO scripts out --force --only $STEM | tail -1)
  fi
  (cd $AUDIO/slides && $ROOT/.manim-venv/bin/python build.py deck_$NN video --work $WORK | tail -1)
  (cd $AUDIO && $ROOT/.manim-venv/bin/python slides/subtitles.py $STEM | tail -1)

  OUT=$AUDIO/out
  if [[ -f $OUT/$STEM-cover.png ]]; then
    # Hold the cover for COVER seconds, then crossfade into the slides over FADE
    # seconds, with the narration and subtitles starting as the slides appear.
    ffmpeg -y -loglevel error \
      -loop 1 -framerate 30 -t $((COVER + FADE)) -i $OUT/$STEM-cover.png \
      -i $OUT/$STEM-slides.mp4 -i $OUT/$STEM.m4a -itsoffset $COVER -i $OUT/$STEM-slides.srt \
      -filter_complex "[0:v]fps=30,format=yuv420p,setsar=1,settb=1/30[c];[1:v]fps=30,format=yuv420p,setsar=1,settb=1/30[s];[c][s]xfade=transition=fade:duration=${FADE}:offset=${COVER}[v];[2:a]adelay=$((COVER * 1000)):all=1[a]" \
      -map "[v]" -map "[a]" -map 3 -c:v libx264 -preset fast -crf 20 -c:a aac -b:a 128k -c:s mov_text \
      -metadata:s:s:0 language=eng -movflags +faststart $OUT/$STEM-video.mp4
  else
    ffmpeg -y -loglevel error \
      -i $OUT/$STEM-slides.mp4 -i $OUT/$STEM.m4a -i $OUT/$STEM-slides.srt \
      -map 0:v -map 1:a -map 2 -c:v copy -c:a copy -c:s mov_text \
      -metadata:s:s:0 language=eng -shortest $OUT/$STEM-video.mp4
  fi
  # Subtitles timed to the final video (after the cover), for uploading alongside it.
  ffmpeg -y -loglevel error -i $OUT/$STEM-video.mp4 -map 0:s:0 $OUT/$STEM-video.srt
  echo "wrote audio/out/$STEM-video.mp4 ($(ffprobe -v error -show_entries format=duration -of csv=p=0 $OUT/$STEM-video.mp4 | cut -d. -f1) s)"
done
