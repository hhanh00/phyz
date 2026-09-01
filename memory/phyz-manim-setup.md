---
name: phyz-manim-setup
description: Manim + TinyTeX toolchain for rendering physics diagrams in the Phyz docs
metadata: 
  node_type: memory
  type: reference
  originSessionId: b7f03ddf-5a19-4e00-a467-087bf4052f77
---

Manim is set up for rendering diagrams for the Phyz docs (e.g. `docs/manim/boost.py` → `docs/manim/boost-diagrams.png`, used on the special-relativity page).

- venv: `/Users/hanhhuynhhuu/projects/phyz/.manim-venv` (manim Community v0.21.0, Python 3.14)
- LaTeX: TinyTeX at `~/Library/TinyTeX` (TeX Live 2026, installed user-level — no sudo; `basictex` cask needs sudo and was not used). Extra packages installed via `tlmgr`: `standalone`, `preview`, `babel-english` (TinyTeX's minimal scheme lacks these — first render fails without them).
- Render a static frame:
  ```
  PATH=$PATH:~/Library/TinyTeX/bin/universal-darwin .manim-venv/bin/manim render -s -r 2400,1350 -q m docs/manim/boost.py BoostDiagrams
  ```
  Then copy the PNG from `docs/manim/media/images/boost/` to `docs/manim/boost-diagrams.png` — the markdown references that stable path (`![...](./manim/boost-diagrams.png)`, must keep the `./` prefix or Vite can't resolve it).
- The user's preferred convention for spacetime diagrams here: **x vertical, t horizontal** — see [[phyz-vuepress-quirks]] and [[phyz-static-over-interactive]].
- Known quirk: this session's model cannot view images — verify manim renders via pixel sampling (PIL) instead.
