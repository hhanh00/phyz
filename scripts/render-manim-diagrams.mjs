import { spawnSync } from 'node:child_process'
import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const __dirname = path.dirname(fileURLToPath(import.meta.url))
const root = path.join(__dirname, '..')
const manimDir = path.join(root, 'docs', 'manim')
const venvManim = path.join(root, '.manim-venv', 'bin', 'manim')

const diagrams = [
  { source: 'boost.py', scene: 'BoostDiagrams', output: 'boost-diagrams.png' },
  { source: 'hamiltonian_flow.py', scene: 'HamiltonianFlow', output: 'hamiltonian-flow.png' },
  { source: 'occupation_states.py', scene: 'OccupationStates', output: 'occupation-states.png' },
]

if (!fs.existsSync(venvManim)) {
  console.error(`manim not found at ${venvManim}`)
  console.error('Create it with: uv venv .manim-venv --python 3.14 && uv pip install --python .manim-venv/bin/python manim')
  process.exit(1)
}

const missing = ['latex', 'dvisvgm'].filter((cmd) => spawnSync('which', [cmd]).status !== 0)
if (missing.length > 0) {
  console.error(`missing on PATH: ${missing.join(', ')}`)
  console.error('Install TeX Live with: brew install dvisvgm')
  process.exit(1)
}

let ok = 0
let failed = 0
for (const { source, scene, output } of diagrams) {
  const result = spawnSync(
    venvManim,
    ['render', '-s', '-r', '2400,1350', '-q', 'm', path.join('docs', 'manim', source), scene],
    { cwd: root, stdio: 'pipe', encoding: 'utf8' },
  )
  if (result.status !== 0) {
    failed++
    console.error(`FAIL ${source}\n${result.stderr || result.stdout}`)
    continue
  }
  const imagesDir = path.join(root, 'media', 'images', path.basename(source, '.py'))
  const rendered = fs
    .readdirSync(imagesDir)
    .find((f) => f.startsWith(`${scene}_ManimCE_v`) && f.endsWith('.png'))
  if (!rendered) {
    failed++
    console.error(`FAIL ${source}: no rendered PNG found in ${imagesDir}`)
    continue
  }
  fs.copyFileSync(path.join(imagesDir, rendered), path.join(manimDir, output))
  ok++
  console.log(`ok   ${source} -> docs/manim/${output}`)
}

fs.rmSync(path.join(root, 'media'), { recursive: true, force: true })

console.log(`\n${ok} diagram(s) rendered, ${failed} failed.`)
if (failed > 0) process.exitCode = 1
