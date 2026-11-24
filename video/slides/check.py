"""Check a listening script against its deck and the format rules in video/BRIEF.md.

Usage: check.py NN [NN ...]

For each chapter number NN, reports slide anchors in deck_NN.py that no longer
match the script in order, paragraphs or sentences that break the file format,
and spoken numbers that differ from the committed version of the script (git
HEAD), so a rewrite can confirm it kept every number. Exits nonzero on any
anchor or format problem.
"""
import importlib
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import engine  # noqa: E402

NUMBER_WORDS = set("""zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen
fifteen sixteen seventeen eighteen nineteen twenty thirty forty fifty sixty seventy eighty ninety hundred
thousand million billion trillion half halves third thirds quarter quarters""".split())
ALLOWED = re.compile(r"[A-Za-z .,;'?\-\n]*")


def numbers(text):
    """Every maximal run of number words, such as 'forty-three' or 'two to the two hundred fifty-five'."""
    runs, run = [], []
    for word in re.findall(r"[A-Za-z]+(?:-[A-Za-z]+)*", text.lower()):
        parts = word.split("-")
        if all(p in NUMBER_WORDS for p in parts):
            run.append(word)
        elif word in ("and", "to", "the") and run:
            run.append(word)
        else:
            while run and run[-1] in ("and", "to", "the"):
                run.pop()
            if run:
                runs.append(" ".join(run))
            run = []
    if run:
        runs.append(" ".join(run))
    return Counter(r for r in runs if r not in ("one",))  # "one" is too often a pronoun


def check(nn):
    module = importlib.import_module(f"deck_{nn}")
    path = HERE.parent / "scripts" / f"{module.STEM}.txt"
    text = path.read_text()
    problems = []

    sentences = engine.script_sentences(path)
    cursor = 0
    for slide in module.deck.slides:
        for i in range(cursor, len(sentences)):
            if sentences[i].startswith(slide["at"]):
                cursor = i + 1
                break
        else:
            problems.append(f"anchor not found after sentence {cursor}: {slide['at']!r} ({slide['title']})")

    text = "\n\n".join(p for p in text.split("\n\n") if re.search(r"[A-Za-z]", p))  # drop reading markers
    if not ALLOWED.fullmatch(text):
        bad = sorted(set(re.sub(r"[A-Za-z .,;'?\-\n]", "", text)))
        problems.append(f"characters outside the allowed set: {' '.join(bad)!r}")
    for para in (p.strip() for p in text.split("\n\n")):
        if not para:
            continue
        if "\n" in para:
            problems.append(f"line break inside a paragraph: {para[:60]!r}")
        if len(para.split()) <= 7 and not para.endswith("."):
            problems.append(f"heading without a final period: {para!r}")
        for s in re.split(r"(?<=[.!?])\s+", para):
            if len(s.split()) > 20:
                problems.append(f"sentence of {len(s.split())} words: {s[:70]!r}")

    try:
        old = subprocess.run(["git", "show", f"HEAD:video/scripts/{path.name}"], capture_output=True, text=True,
                             check=True, cwd=HERE).stdout
        before, after = numbers(old), numbers(text)
        lost, gained = before - after, after - before
        notes = [f"  number lost:   {n} (x{c})" for n, c in sorted(lost.items())]
        notes += [f"  number gained: {n} (x{c})" for n, c in sorted(gained.items())]
    except subprocess.CalledProcessError:
        notes = []

    words = len(text.split())
    print(f"chapter {nn}: {len(module.deck.slides)} anchors, {len(sentences)} sentences, {words} words, "
          f"{len(problems)} problems")
    for p in problems:
        print(f"  {p}")
    if notes:
        print("  numbers differ from git HEAD (fine if only reworded, such as 'three quarters' kept as a phrase):")
        print("\n".join(notes))
    return not problems


ok = all([check(nn.zfill(2)) for nn in sys.argv[1:]])
sys.exit(0 if ok else 1)
