---
name: phyz-manim-setup
description: Manim + TinyTeX toolchain for rendering physics diagrams in the Phyz docs
metadata: 
  node_type: memory
  type: reference
  originSessionId: b7f03ddf-5a19-4e00-a467-087bf4052f77
---

Manim is set up for rendering diagrams for the Phyz docs (e.g. `docs/manim/boost.py` → `docs/manim/boost-diagrams.png`, used on the special-relativity page).

- venv: `.manim-venv` at the project root (manim Community v0.21.0, Python 3.14). Create with `uv venv .manim-venv --python 3.14` then `uv pip install --python .manim-venv/bin/python manim`.
- LaTeX: Homebrew TeX Live. `brew install dvisvgm` pulls the `texlive` bottle (4.6 GB) as a dependency and links `latex`, `dvisvgm`, `tlmgr`, `kpsewhich` into `/opt/homebrew/bin`. That TeX Live already ships `standalone`, `preview`, `amsmath`, `babel`, `dvisvgm.def`, so no extra packages are needed. (`tlmgr install` fails with "action not allowed in system mode" because brew owns the tree — not required anyway.) System deps also needed: `brew install pango pkg-config cmake` (for manimpango/pycairo builds).
- Render a static frame from the project root:
  ```
  .manim-venv/bin/manim render -s -r 2400,1350 -q m docs/manim/foo.py FooScene
  ```
  Output lands at `./media/images/foo/FooScene_ManimCE_v0.21.0.png` (root `media/`, not `docs/manim/media/`). Copy it to `docs/manim/foo.png` and delete the root `media/` dir. Markdown references the stable path (`![...](./manim/foo.png)`, must keep the `./` prefix or Vite can't resolve it).
- The user's preferred convention for spacetime diagrams here: **x vertical, t horizontal** — see [[phyz-vuepress-quirks]] and [[phyz-static-over-interactive]].
- Known quirk: this session's model cannot view images — verify manim renders via pixel sampling (PIL) instead.
