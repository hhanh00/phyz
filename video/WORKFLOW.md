# Chapter workflow, from page to video

This file records the steps used to bring chapter 1 (Classical Mechanics) to its current state, so that a later session can repeat them on another chapter. It covers the page itself, the listening script, the slide deck and the video. `video/README.md` explains the tools; this file explains the order to use them in and the checks between steps.

The work runs as review loops. A fresh agent reviews, the main session applies the findings, and a new fresh agent reviews again. Fresh reviewers matter because an agent that wrote or fixed the text tends to confirm its own work.

The loop stops only on a fresh review of the final text. That review runs after the last edit, including any `/bro` fixes or should-fixes applied after an earlier clean round. It gets no list of what earlier rounds fixed, so it judges the text as a first-time reader would. It returns no must-fix items. If anything is edited after it, run another. A clean round followed by unreviewed edits doesn't count, and neither does a score from a reviewer who was told what to expect: chapter 2's page scored 9 that way, and on reading, Hanh found it well below that.

## Standing preferences

These came from Hanh while working on chapter 1. They apply to every step below.

- A question asked during review is a question. Answer it first, and edit only when asked.
- The text has to pass the "bro test", run with the `/bro` skill (installed at `~/.claude/skills/bro/`, from github.com/luchasarie/bro-skill). `/bro` gives an ELI5-style simplification, so its output is expected to differ from the text, and a difference alone is not a problem. Use it to find gaps: a step, reason or definition `/bro` had to supply that the text never gives, a passage `/bro` misreads because the text is ambiguous, or a passage whose purpose `/bro` cannot state. Close each gap with the smallest fix in the chapter's own register. Don't rewrite passages toward the `/bro` version.
- Give the reason for each step. Saying how something is done isn't enough; say why it's needed before doing it.
- A reader skimming the page should get the flow from headers, a short roadmap and goal boxes. Headers have to make sense to someone who doesn't know the topic yet.
- Put worked examples in tables, displayed equations or figures, never in a dense numeric paragraph.
- Don't render the deck after every script review. Get the script right first, then build the deck, then review the deck, then render once.
- Rank the script against the page. The page may hold more detail, but the script must not leave out an important fact.
- Commit only when asked, and push only when asked. Leave unrelated changes, such as personal notes in `docs/`, out of the commit.

## 1. The page

1. Read the chapter in `docs/` in full and rate it out of 10. Say what works and what doesn't, without editing yet.
2. Run review loops with fresh agents. Each review checks facts and numbers, missing reasons, terms used before they're defined, experiments or examples used before they're presented, the project style rules in `CLAUDE.md`, and the bro test. It also scores how the page reads as a whole against chapter 1, not only whether gaps remain, because gap fixes accumulate into dense, patched paragraphs. Apply each round's findings in the main session.
3. Once the reviews are stable, do one `/bro` pass over the whole page, passage by passage, as described above. A fresh agent can run it: give it the skill file and ask for a count of passages checked and gaps found, and for each gap the sentence, what `/bro` had to add or got wrong, and the smallest fix.
4. Run the closing fresh review described above, on the text as it now stands. Repeat until it returns no must-fix items with nothing edited after it.
5. Fix the figures. The Manim sources are in `docs/manim/page_diagrams.py`. Render with `.manim-venv/bin/manim render -s -r 2400,1350 -q m`, copy the PNG to `docs/manim/`, and delete the `media/` folder Manim leaves at the repo root. Look at each figure after rendering.
6. If a header changed, update the anchors that link to it from other chapters.
7. Build the site, then commit when asked.

## 2. The script

1. Write `video/scripts/STEM.txt` from the finished page, following `video/BRIEF.md`. Check the format with a short script or with `check.py`. Only these characters are allowed: letters, space, `. , ; ' ? -`. Numbers are in words, sentences have at most 20 words, and headings have at most 7 words and end with a period.
2. Keep a copy of each version in the scratchpad, because the deck step later diffs against the version the deck was built from.
3. Run review rounds with a fresh agent each time. Use the prompt below. Apply the must-fix items and the should-fix items that fix a real problem, and skip pure preferences that undo an earlier round's fix.
4. Stop only after a fresh review of the final script, run after the last edit, returns no must-fix items. Chapter 1 took four rounds, and its fidelity score went from 7 to 9.5.

### Script review prompt

> You are reviewing a narration script for a video, against the site chapter it is based on. Do not edit any file; report only.
>
> Files: the script `video/scripts/STEM.txt`, the chapter `docs/CHAPTER.md` (the source of truth), the rules `video/BRIEF.md` and `video/REVIEW.md`, and `CLAUDE.md`. Read them all in full.
>
> The listener hears the script once, with slides, and cannot read the page. Say what they already know and what they don't.
>
> Deliver, in this order:
> 1. Fidelity ranking. List every important fact, definition, result and worked number in the chapter, and mark each COVERED, CHANGED (quote both versions) or OMITTED. The site may hold more detail. Flag an omission only when the listener would miss something needed to follow the argument, or something the chapter treats as a key takeaway. Check every number. Give a fidelity score out of 10.
> 2. Must-fix items: factual errors, contradictions with the chapter, a term used before it's defined, a step a listener can't follow by ear, format violations. Quote the exact sentence, say why, and give a replacement that obeys the format rules.
> 3. Should-fix items, kept short. Label pure preferences as such.
> 4. Bro test: up to five sentences a friend would answer with "bro, what?", with plain replacements. Zero is a valid answer.
> 5. Overall score out of 10, and whether the script is ready to record.
>
> Be calibrated. A must-fix needs a concrete listener failure or a factual error, not a wording preference. Keep the report under 1,500 words.

Middle rounds may list what earlier rounds already fixed, to avoid repeats. The closing review must not get that list.

## 3. The pause file

Write `video/prosody/STEM.pauses.txt`: the final script with extra commas where a reader would breathe, and no other change. When the script changes, carry the old commas over to every sentence that didn't change, and add commas to new long sentences that have none. `render.py` refuses the file if it differs from the script by more than commas, and its `written_pauses` check can be run on its own before rendering.

## 4. The deck

1. Build `video/slides/deck_NN.py` following `video/slides/BRIEF.md`. Each slide is anchored to the first words of a script sentence. A new slide starts at every spoken heading, and numbers appear on screen when the narration reaches them, not before.
2. Run `cd video/slides && ../../.manim-venv/bin/python check.py NN` until it reports no anchor problems.
3. Render contact sheets with `build.py deck_NN preview --work DIR`, and look at them. Use `--only N,N` to re-render single slides after a fix.
4. Run one review with a fresh agent, using the prompt below. Apply its findings, re-render only the changed slides, and look at them.
5. After any later script edit, run `check.py` again, because changed openings break anchors.

A long deck update can go to one agent, with a brief that lists the stale anchors, the content the script gained (diff against the version the deck was built from) and the open review findings. Send that same agent the next review's findings, since it already knows the file.

### Deck review prompt

> Review the slide deck for chapter NN. Report only; do not edit files.
>
> Read `video/slides/BRIEF.md`, the script, the chapter (the source of truth for facts and notation) and `deck_NN.py`. Look at every contact sheet image with the Read tool.
>
> Deliver:
> 1. Sync and fidelity: slides whose content contradicts the narration or runs ahead of it, facts or numbers that differ from the chapter, and key results the narration states but no slide shows, where a visual would clearly help.
> 2. Readability: overlaps, clipping, text too small, unlabelled axes, symbols shown before they're explained, clutter, colour inconsistencies.
> 3. Pacing: slides that stay up a long time with nothing changing, and slides that flash by.
>
> For each item give the slide number, its anchor, the problem and a concrete fix. Split the items into MUST-FIX and SHOULD-FIX. End with a score out of 10 and whether the deck is ready to render. Keep the report under 1,200 words.

## 5. The video

1. Render the narration once the script is final. Deck changes don't touch the audio, so the narration can render while the deck is being fixed. Run it from `video/`, in the background:
   `VOICE=azure caffeinate -i .venv/bin/python render.py ../.kokoro scripts out --force --only STEM`
   The Azure key is in `~/.azure-speech`. Never print it, and never ask Hanh to paste it.
2. Add the chapter to `COVERS` in `slides/cover.py` if it has no cover yet, render the cover and look at it.
3. Build the slides and the final video from the repo root, in the background:
   `VOICE=azure WORK=DIR caffeinate -i video/make_video.sh --skip-audio STEM`
4. Write `video/out/STEM/STEM-description.txt`. Take the chapter timestamps from the heading entries in `video/timings/STEM.json`, and add the cover hold (`COVER` in `make_video.sh`, 5 s). Headings are silent in the final video, so the subtitle file won't show them.
5. Commit the script, the pause file and the deck when asked. Everything in `video/out/`, `video/timings/` and `video/azure-cache/` is generated and not committed.
