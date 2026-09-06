import fs from 'node:fs'
import path from 'node:path'
import crypto from 'node:crypto'
import { fileURLToPath } from 'node:url'
import { renderFeynmanSvg } from '../docs/.vuepress/lib/feynman-svg.js'

const __dirname = path.dirname(fileURLToPath(import.meta.url))
const docsDir = path.join(__dirname, '..', 'docs')
const cacheDir = path.join(__dirname, '..', 'docs', '.vuepress', '.feynman-cache')

const hash = (code) => crypto.createHash('sha1').update(code).digest('hex').slice(0, 16)

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

const liveIds = new Set()
let ok = 0
let failed = 0
for (const file of markdownFiles(docsDir)) {
  const src = fs.readFileSync(file, 'utf8')
  let match
  while ((match = fenceRe.exec(src)) !== null) {
    const body = match[1].trim()
    liveIds.add(hash(body))
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

for (const entry of fs.readdirSync(cacheDir)) {
  const id = entry.split('.')[0]
  if (!liveIds.has(id)) {
    fs.rmSync(path.join(cacheDir, entry), { force: true })
    console.log(`rm   ${entry}`)
  }
}

console.log(`\n${ok} diagram(s) rendered, ${failed} failed.`)
if (failed > 0) process.exitCode = 1
