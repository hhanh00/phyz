import { defaultTheme } from '@vuepress/theme-default'
import { viteBundler } from '@vuepress/bundler-vite'
import { markdownMathPlugin } from '@vuepress/plugin-markdown-math'
import markdownItFootnote from 'markdown-it-footnote'
import { renderExcalidrawSvg } from './lib/excalidraw-svg.js'
import { renderFeynmanSvg } from './lib/feynman-svg.js'

export default {
  lang: 'en-US',
  title: 'Phyz',
  description: 'A connected path from classical mechanics to the Standard Model',
  // Served from custom domain https://phyz.methyl.cc
  base: '/',
  head: [
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/favicon.svg' }],
  ],

  bundler: viteBundler(),

  theme: defaultTheme({
    navbar: [
      { text: 'Home', link: '/' },
      {
        text: 'Foundations',
        children: [
          { text: 'Classical Mechanics', link: '/classical-mechanics.html' },
          { text: 'First Quantization', link: '/first-quantization.html' },
          { text: 'Harmonic Oscillator', link: '/harmonic-oscillator.html' },
        ],
      },
      {
        text: 'Relativity',
        children: [
          { text: 'Special Relativity', link: '/special-relativity.html' },
          { text: 'Relativistic QM', link: '/relativistic-qm.html' },
          { text: 'Dirac Equation', link: '/dirac-equation.html' },
        ],
      },
      {
        text: 'Quantum Fields',
        children: [
          { text: 'Fields and Quanta', link: '/qft.html' },
          { text: 'Action and Lagrangians', link: '/qft-action.html' },
          { text: 'Field Quantization', link: '/field-quantization.html' },
        ],
      },
      {
        text: 'Quantum Electrodynamics',
        children: [
          { text: 'Quantum Electrodynamics', link: '/qed.html' },
          { text: 'From Lagrangian to Experiment', link: '/lagrangian-to-experiment.html' },
          { text: 'Perturbation Theory', link: '/perturbation-theory.html' },
          { text: 'Feynman Rules for QED', link: '/feynman-rules.html' },
        ],
      },
      {
        text: 'Electroweak',
        children: [
          { text: 'Weak Interaction', link: '/weak-interaction.html' },
          { text: 'Electroweak Unification', link: '/electroweak-unification.html' },
          { text: 'Higgs Mechanism', link: '/higgs-mechanism.html' },
        ],
      },
      {
        text: 'Strong & Standard Model',
        children: [
          { text: 'Quantum Chromodynamics', link: '/qcd.html' },
          { text: 'The Standard Model', link: '/standard-model.html' },
        ],
      },
    ],
    // Reading order for the Prev/Next footer links on each page.
    sidebar: [
      { text: 'Classical Mechanics', link: '/classical-mechanics.html' },
      { text: 'First Quantization', link: '/first-quantization.html' },
      { text: 'Harmonic Oscillator', link: '/harmonic-oscillator.html' },
      { text: 'Special Relativity', link: '/special-relativity.html' },
      { text: 'Relativistic QM', link: '/relativistic-qm.html' },
      { text: 'Dirac Equation', link: '/dirac-equation.html' },
      { text: 'Fields and Quanta', link: '/qft.html' },
      { text: 'Action and Lagrangians', link: '/qft-action.html' },
      { text: 'Field Quantization', link: '/field-quantization.html' },
      { text: 'Quantum Electrodynamics', link: '/qed.html' },
      { text: 'From Lagrangian to Experiment', link: '/lagrangian-to-experiment.html' },
      { text: 'Perturbation Theory', link: '/perturbation-theory.html' },
      { text: 'Feynman Rules for QED', link: '/feynman-rules.html' },
      { text: 'Weak Interaction', link: '/weak-interaction.html' },
      { text: 'Electroweak Unification', link: '/electroweak-unification.html' },
      { text: 'Higgs Mechanism', link: '/higgs-mechanism.html' },
      { text: 'Quantum Chromodynamics', link: '/qcd.html' },
      { text: 'The Standard Model', link: '/standard-model.html' },
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
      if (token.info.trim() === 'feynman') {
        return `${renderFeynmanSvg(token.content)}\n`
      }
      return defaultFence(tokens, idx, options, env, self)
    }
  },
}
