---
name: phyz-vuepress-quirks
description: "Phyz site (VuePress 2) setup quirks — component registration, dev server usage, diagram rendering"
metadata: 
  node_type: memory
  type: project
  originSessionId: b7f03ddf-5a19-4e00-a467-087bf4052f77
---

The Phyz docs site is VuePress 2 (`docs/` dir, config at `docs/.vuepress/config.js`), user runs it with `pnpm docs:dev` (port 8080).

Non-obvious facts learned:
- VuePress 2 does **not** auto-register components from `docs/.vuepress/components/` (the existing `SpacetimeDiagram.vue` there is an orphan, rendered nowhere — if the user expects it on the special-relativity page, it needs explicit registration or a reference).
- The user found the standalone `.vuepress/components/ExcalidrawScene.vue` approach unnecessary; diagrams are now rendered as static inline SVG at build time by a dependency-free renderer at `docs/.vuepress/lib/excalidraw-svg.js`, hooked into the markdown-it `fence` rule in `config.js` for ```` ```excalidraw ```` blocks.
- excalidraw.com's current app no longer loads scenes from the `#json=` hash (backend share links only) — if iframe embeds are ever reconsidered, the `#url=` + data-URI loader is the only client-side path.
- Port 8080 being in use usually means the user's own `pnpm docs:dev` is running; don't start a second dev server on the same project — they share `docs/.vuepress/.temp` and conflict.

**Why:** These quirks cost real debugging time (stale config, `.temp` conflict, orphan component). A scripted md edit once silently dropped the file's front section (`slice` bug) — build still passed, so always **back up a markdown file before scripted edits** and re-read the top of the file afterwards.

**How to apply:** When editing this site's markdown pipeline or components, restart with `pnpm docs:clean-dev`; verify via `npm --prefix . run docs:build` and grepping `docs/.vuepress/dist/` for the rendered markup.
