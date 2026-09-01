---
name: phyz-static-over-interactive
description: User prefers static/display-only diagrams over interactive editor embeds in the Phyz docs
metadata: 
  node_type: memory
  type: feedback
  originSessionId: b7f03ddf-5a19-4e00-a467-087bf4052f77
---

When asked how diagrams should appear in the Phyz docs, the user explicitly said "I don't care about editing" — they want the diagram **displayed**, not an editor embedded in the page.

**Why:** An earlier attempt embedded the live Excalidraw editor (React-in-Vue, ~2 MB lazy chunk) and it crashed in dev; the user's priority is a reliable, visible diagram in the docs, with editing happening externally (excalidraw.com → copy JSON back into the markdown block).

**How to apply:** Default to static rendering (baked SVG, no client JS) for Phyz markdown diagrams — see [[phyz-vuepress-quirks]]. Don't propose interactive/editable embeds for this site unless asked. This also applies generally: prefer zero-dependency, build-time solutions for this project.
