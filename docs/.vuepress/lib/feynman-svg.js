// TikZ-Feynman → inline SVG renderer for the docs.
//
// Compiles a ```feynman code fence (the body is raw TikZ-Feynman source)
// with lualatex + dvisvgm and returns a self-contained <svg> fragment, the
// same "static diagram baked at build time" pattern as the excalidraw
// renderer. Output is cached by content hash so a diagram compiles once.
//
// Requires: lualatex and dvisvgm on PATH, with the tikz and tikz-feynman
// packages (both ship in the Homebrew TeX Live this site already uses).

import { execFileSync } from 'node:child_process'
import { createHash } from 'node:crypto'
import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const __dirname = path.dirname(fileURLToPath(import.meta.url))
const CACHE_DIR = path.join(__dirname, '..', '.feynman-cache')

const PREAMBLE = `\\documentclass[border=6pt]{standalone}
\\usepackage[compat=1.1.0]{tikz-feynman}
\\begin{document}
`

const POSTAMBLE = `\n\\end{document}\n`

// The natural dvisvgm output is a few hundred px at hairline thickness;
// bump the intrinsic size so it reads clearly inline.
const SCALE = 2

// lualatex/dvisvgm live in the Homebrew prefix on this machine.
const env = { ...process.env, PATH: `/opt/homebrew/bin:${process.env.PATH || ''}` }

const hash = (code) => createHash('sha1').update(code).digest('hex').slice(0, 16)

function scaleSvg(svg) {
  return svg
    // Vue's template compiler rejects the XML declaration dvisvgm emits.
    .replace(/<\?xml[^>]*\?>\s*/g, '')
    .replace(/width='([\d.]+)pt'/g, (_, n) => `width='${(parseFloat(n) * SCALE).toFixed(2)}pt'`)
    .replace(/height='([\d.]+)pt'/g, (_, n) => `height='${(parseFloat(n) * SCALE).toFixed(2)}pt'`)
    .replace('<svg ', '<svg style="max-width:100%;height:auto;display:block;margin:1.5rem auto" ')
}

export function renderFeynmanSvg(code) {
  const body = String(code ?? '').trim()
  if (!body) return '<!-- empty feynman diagram -->'

  const id = hash(body)
  fs.mkdirSync(CACHE_DIR, { recursive: true })

  const tex = path.join(CACHE_DIR, `${id}.tex`)
  const dvi = path.join(CACHE_DIR, `${id}.dvi`)
  const svg = path.join(CACHE_DIR, `${id}.svg`)

  if (!fs.existsSync(svg)) {
    fs.writeFileSync(tex, PREAMBLE + body + POSTAMBLE)
    try {
      execFileSync('lualatex', [
        '--output-format=dvi',
        '-interaction=nonstopmode',
        '-halt-on-error',
        path.basename(tex),
      ], { cwd: CACHE_DIR, env, stdio: ['ignore', 'ignore', 'pipe'] })

      execFileSync('dvisvgm', [path.basename(dvi), '-o', path.basename(svg)],
        { cwd: CACHE_DIR, env, stdio: ['ignore', 'ignore', 'pipe'] })
    } catch (err) {
      const log = err.stderr ? String(err.stderr).slice(0, 500) : String(err.message)
      return `<!-- feynman compile error: ${log.replace(/-->/g, '').replace(/\n+/g, ' ')} -->`
    }
  }

  const out = fs.readFileSync(svg, 'utf8')
  return `<div class="feynman-diagram">${scaleSvg(out)}</div>`
}
