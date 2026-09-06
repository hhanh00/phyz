import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { renderFeynmanSvg } from '../docs/.vuepress/lib/feynman-svg.js'

const __dirname = path.dirname(fileURLToPath(import.meta.url))
const docsDir = path.join(__dirname, '..', 'docs')

const fenceRe = /```feynman\s*\n([\s\S]*?)```/g

function* markdownFiles(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name)
    if (entry.isDirectory()) {
      if (entry.name !== 'manim' && entry.name !== '.vuepress') {
        yield* markdownFiles(full)
      }
    } else if (entry.name.endsWith('.md')) {
      yield full
    }
  }
}

let ok = 0
let failed = 0
for (const file of markdownFiles(docsDir)) {
  const src = fs.readFileSync(file, 'utf8')
  let match
  while ((match = fenceRe.exec(src)) !== null) {
    const body = match[1].trim()
    const out = renderFeynmanSvg(body)
    if (out.includes('compile error') || out.includes('empty feynman diagram')) {
      failed++
      console.error(`FAIL ${file}: ${out.slice(0, 200)}`)
    } else {
      ok++
      console.log(`ok   ${file}`)
    }
  }
}
console.log(`\n${ok} diagram(s) rendered, ${failed} failed.`)
if (failed > 0) process.exitCode = 1
