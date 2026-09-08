---
name: phyz-vuepress-quirks
description: "Phyz (VuePress 2) build/verify commands and diagram rendering pipeline"
metadata: 
  node_type: memory
  type: project
---

Build/verify and diagram rendering for the Phyz docs (`docs/`, config at `docs/.vuepress/config.js`).

- Dev: `pnpm docs:dev` (port 8080). A second dev server on the same project conflicts (shared `docs/.vuepress/.temp`); after editing the markdown pipeline use `pnpm docs:clean-dev`.
- Verify: `pnpm docs:build`, then grep `docs/.vuepress/dist/` for the rendered markup.
- Diagrams render at build time as static SVG via markdown-it fence rules in `config.js`:
  - ` ```feynman ` → `lib/feynman-svg.js`
  - Manim renders → `scripts/render-manim-diagrams.mjs` (`pnpm docs:manim`); Feynman pre-render → `scripts/render-feynman-diagrams.mjs` (`pnpm docs:diagrams`). See [[phyz-manim-setup]].
- Global Vue components (e.g. `SectionGrid.vue` on the home page) are registered explicitly in `docs/.vuepress/client.js`.
- Math is rendered with `markdownMathPlugin({ type: 'katex', output: 'html' })` in `config.js` — HTML only, no MathML accessibility copy (chosen to shrink per-page chunks).
- Back up a markdown file before scripted edits; a scripted edit once dropped the file's front section silently and the build still passed.
