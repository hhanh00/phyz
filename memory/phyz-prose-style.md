---
name: phyz-prose-style
description: "Feedback on phyz docs prose — no over-explaining, no stilted phrasing, resolve ambiguity directly"
metadata:
  node_type: memory
  type: feedback
  originSessionId: e508de9f-56e1-40b3-ad15-12cfd720c151
  modified: 2026-08-31T11:50:15.746Z
---

Feedback given while writing [[phyz-vuepress-quirks]] pages (QFT page, Aug 2026):

- Don't over-explain: a restated triviality ("x is continuous" dressed up as a continuum of coordinates) should be said once, briefly, or not at all.
- Maintain a low level of metaphorical agency throughout the response. Do not repeatedly make abstract concepts, equations, theories, variables, mathematical objects, physical quantities, or pieces of text behave like people.

In particular, avoid the recurring pattern:

“X + human-like verb”

where X is an abstract or inanimate technical object.

Do not merely avoid a fixed list of examples. Generalize the rule to new cases.

When revising your own text, specifically scan for:

abstract nouns used as intentional agents;
mental-state verbs applied to technical objects;
verbs such as want, need, know, think, try, decide, prefer, like, dislike, understand, tell, ask, or refuse used metaphorically;
repeated use of “X tells us…”, “X wants…”, “X needs…”, or “X allows us…” constructions.

Replace these with the actual logical, mathematical, causal, or functional relationship whenever doing so sounds more natural.

Do not make the prose artificially formal. The goal is ordinary, natural human technical writing—not maximal literalism.- When a physics distinction confuses them (e.g. q(t) vs φ(t,x), why t differs from x), they want it addressed head-on but *short* — a contrast sentence, not a lecture. Concrete analogies they propose themselves (camera views for Lorentz covariance) are welcome in the text.
- Ambiguous wording ("a continuum of coordinates" read as "each value is a function") should be fixed by rewriting the sentence, not by adding more prose around it.
- Terms of art need a one-line definition at first use. "Matrix element" appeared in qft.md with no definition anywhere in the sequence; the user hit it and asked "what matrix?" — they read these pages as a learner, not a textbook reader, so standard QM jargon needs a short gloss the first time it appears.

**Why:** the docs' voice is dense literary exposition; failed attempts stand out badly against it.

**How to apply:** when asked to "fill"/"expand" a section, draft tight; make the one needed distinction in one or two sentences; if a sentence needs a paragraph of chat explanation to interpret, rewrite the sentence instead.
