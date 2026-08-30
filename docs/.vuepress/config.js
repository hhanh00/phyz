import { defaultTheme } from '@vuepress/theme-default'
import { viteBundler } from '@vuepress/bundler-vite'
import { markdownMathPlugin } from '@vuepress/plugin-markdown-math'
import markdownItFootnote from 'markdown-it-footnote'
import { renderExcalidrawSvg } from './lib/excalidraw-svg.js'

export default {
  lang: 'en-US',
  title: 'Phyz',
  description: 'A VuePress site with math markdown support',
  // Served from GitHub Pages at https://hhanh00.github.io/phyz/
  base: '/phyz/',

  bundler: viteBundler(),

  theme: defaultTheme({
    navbar: [
      { text: 'Home', link: '/' },
      {
        text: 'Quantum Mech',
        children: [
          { text: 'Classical Mechanics', link: '/classical-mechanics.html' },
          { text: 'First Quantization', link: '/first-quantization.html' },
        ],
      },
      { text: 'Special Relativity', link: '/special-relativity.html' },
      { text: 'Relativistic QM', link: '/relativistic-qm.html' },
      { text: 'Dirac Equation', link: '/dirac-equation.html' },
      { text: 'QFT: Quantum Field Theory', link: '/qft.html' },
    ],
  }),

  plugins: [
    markdownMathPlugin({ type: 'katex' }),
  ],

  extendsMarkdown(md) {
    md.use(markdownItFootnote)

    // ```excalidraw fenced blocks → static inline SVG, baked into the page
    // at build/render time (see lib/excalidraw-svg.js). No client JS, no
    // iframe — the diagram is part of the HTML itself.
    const defaultFence = md.renderer.rules.fence.bind(md.renderer.rules)

    md.renderer.rules.fence = (tokens, idx, options, env, self) => {
      const token = tokens[idx]
      if (token.info.trim() === 'excalidraw') {
        return `${renderExcalidrawSvg(token.content)}\n`
      }
      return defaultFence(tokens, idx, options, env, self)
    }
  },
}
