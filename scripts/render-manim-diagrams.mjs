import { spawnSync } from 'node:child_process'
import fs from 'node:fs'
import path from 'node:path'
import os from 'node:os'
import { fileURLToPath } from 'node:url'

const __dirname = path.dirname(fileURLToPath(import.meta.url))
const root = path.join(__dirname, '..')
const manimDir = path.join(root, 'docs', 'manim')
const venvManim = path.join(root, '.manim-venv', 'bin', 'manim')

const diagrams = [
  { source: 'boost.py', scene: 'BoostDiagrams', output: 'boost-diagrams.png', page: 'special-relativity' },
  { source: 'hamiltonian_flow.py', scene: 'HamiltonianFlow', output: 'hamiltonian-flow.png', page: 'qft-action' },
  { source: 'occupation_states.py', scene: 'OccupationStates', output: 'occupation-states.png', page: 'field-quantization' },
  { source: 'concept_diagrams.py', scene: 'PhotonPolarizations', output: 'photon-polarizations.png', page: 'qed' },
  { source: 'concept_diagrams.py', scene: 'GaugeDescriptions', output: 'gauge-descriptions.png', page: 'qed' },
  { source: 'concept_diagrams.py', scene: 'PhotonQuantizationRoute', output: 'photon-quantization-route.png', page: 'qed' },
  { source: 'concept_diagrams.py', scene: 'FieldModes', output: 'field-modes.png', page: 'field-quantization' },
  { source: 'concept_diagrams.py', scene: 'ContractionsToDiagram', output: 'contractions-to-diagram.png', page: 'perturbation-theory' },
  { source: 'concept_diagrams.py', scene: 'StateAndField', output: 'state-and-field.png', page: 'qft' },
  { source: 'concept_diagrams.py', scene: 'AmplitudeInterference', output: 'amplitude-interference.png', page: 'feynman-rules' },
  { source: 'concept_diagrams.py', scene: 'OscillatorApproximation', output: 'oscillator-approximation.png', page: 'harmonic-oscillator' },
  { source: 'concept_diagrams.py', scene: 'ClassicalOscillatorEnergy', output: 'classical-oscillator-energy.png', page: 'harmonic-oscillator' },
  { source: 'concept_diagrams.py', scene: 'OscillatorLadder', output: 'oscillator-ladder.png', page: 'harmonic-oscillator' },
  { source: 'concept_diagrams.py', scene: 'OscillatorGroundState', output: 'oscillator-ground-state.png', page: 'harmonic-oscillator' },
  { source: 'page_diagrams.py', scene: 'NewtonMotion', output: 'newton-motion.png', page: 'classical-mechanics' },
  { source: 'page_diagrams.py', scene: 'StationaryActionPaths', output: 'stationary-action-paths.png', page: 'classical-mechanics' },
  { source: 'page_diagrams.py', scene: 'PhaseSpaceStates', output: 'phase-space-states.png', page: 'classical-mechanics' },
  { source: 'page_diagrams.py', scene: 'BornDensity', output: 'born-density.png', page: 'first-quantization' },
  { source: 'page_diagrams.py', scene: 'EigenbasisProbabilities', output: 'eigenbasis-probabilities.png', page: 'first-quantization' },
  { source: 'page_diagrams.py', scene: 'FourierUncertainty', output: 'fourier-uncertainty.png', page: 'first-quantization' },
  { source: 'page_diagrams.py', scene: 'RelativeSimultaneity', output: 'relative-simultaneity.png', page: 'special-relativity' },
  { source: 'page_diagrams.py', scene: 'LightConeIntervals', output: 'light-cone-intervals.png', page: 'special-relativity' },
  { source: 'page_diagrams.py', scene: 'RelativisticEnergySolutions', output: 'relativistic-energy-solutions.png', page: 'relativistic-qm' },
  { source: 'page_diagrams.py', scene: 'KleinGordonDensity', output: 'klein-gordon-density.png', page: 'relativistic-qm' },
  { source: 'page_diagrams.py', scene: 'DiracLinearization', output: 'dirac-linearization.png', page: 'relativistic-qm' },
  { source: 'page_diagrams.py', scene: 'SpinMeasurement', output: 'spin-measurement.png', page: 'dirac-equation' },
  { source: 'page_diagrams.py', scene: 'SpinorRotationSign', output: 'spinor-rotation-sign.png', page: 'dirac-equation' },
  { source: 'page_diagrams.py', scene: 'RestSpinorBasis', output: 'rest-spinor-basis.png', page: 'dirac-equation' },
  { source: 'page_diagrams.py', scene: 'FieldTransformationTypes', output: 'field-transformation-types.png', page: 'qft' },
  { source: 'page_diagrams.py', scene: 'QuantumPictures', output: 'quantum-pictures.png', page: 'qft' },
  { source: 'page_diagrams.py', scene: 'FieldHistorySlice', output: 'field-history-slice.png', page: 'qft-action' },
  { source: 'page_diagrams.py', scene: 'LocalFieldVariation', output: 'local-field-variation.png', page: 'qft-action' },
  { source: 'page_diagrams.py', scene: 'BosonFermionOccupancy', output: 'boson-fermion-occupancy.png', page: 'field-quantization' },
  { source: 'page_diagrams.py', scene: 'GlobalLocalPhase', output: 'global-local-phase.png', page: 'qed' },
  { source: 'page_diagrams.py', scene: 'ScatteringEventRate', output: 'scattering-event-rate.png', page: 'lagrangian-to-experiment' },
  { source: 'page_diagrams.py', scene: 'TwoBodyPhaseSpace', output: 'two-body-phase-space.png', page: 'lagrangian-to-experiment' },
  { source: 'page_diagrams.py', scene: 'PredictionWorkflow', output: 'prediction-workflow.png', page: 'lagrangian-to-experiment' },
  { source: 'page_diagrams.py', scene: 'OperatorOrdering', output: 'operator-ordering.png', page: 'perturbation-theory' },
  { source: 'page_diagrams.py', scene: 'FeynmanPolePrescription', output: 'feynman-pole-prescription.png', page: 'perturbation-theory' },
  { source: 'page_diagrams.py', scene: 'LoopMomentumFreedom', output: 'loop-momentum-freedom.png', page: 'feynman-rules' },
  { source: 'electroweak.py', scene: 'W3PhotonMismatch', output: 'w3-photon-mismatch.png', page: 'electroweak-unification' },
  { source: 'electroweak.py', scene: 'HyperchargeOffset', output: 'hypercharge-offset.png', page: 'electroweak-unification' },
  { source: 'electroweak.py', scene: 'NeutralFieldMixing', output: 'neutral-field-mixing.png', page: 'electroweak-unification' },
  { source: 'higgs.py', scene: 'MexicanHatPotential', output: 'mexican-hat-potential.png', page: 'higgs-mechanism' },
  { source: 'higgs.py', scene: 'GoldstoneModes', output: 'goldstone-modes.png', page: 'higgs-mechanism' },
  { source: 'math_refresher.py', scene: 'EulerCircle', output: 'euler-circle.png', page: 'appendix-math-complex' },
  { source: 'math_refresher.py', scene: 'EigenvectorScaling', output: 'eigenvector-scaling.png', page: 'appendix-math-linear-algebra' },
  { source: 'math_refresher.py', scene: 'RotationGenerator', output: 'rotation-generator.png', page: 'appendix-math-groups' },
]

const args = process.argv.slice(2)
if (args.length && (args.length !== 2 || args[0] !== '--page')) {
  console.error('Usage: pnpm docs:manim [--page <chapter-slug>]')
  process.exit(1)
}
const selected = args.length ? diagrams.filter((d) => d.page === args[1]) : diagrams
if (!selected.length) {
  console.error(`No diagrams registered for page: ${args[1]}`)
  process.exit(1)
}

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

// Render into an isolated directory; never remove a user's existing media.
const mediaDir = fs.mkdtempSync(path.join(os.tmpdir(), 'phyz-manim-'))
let ok = 0
let failed = 0
for (const { source, scene, output } of selected) {
  const result = spawnSync(
    venvManim,
    ['render', '-s', '--tex_template', path.join(manimDir, 'template.tex'), '--media_dir', mediaDir, '-r', '2400,1350', '-q', 'm', path.join('docs', 'manim', source), scene],
    { cwd: root, stdio: 'pipe', encoding: 'utf8' },
  )
  if (result.status !== 0) {
    failed++
    console.error(`FAIL ${source}\n${result.stderr || result.stdout}`)
    continue
  }
  const imagesDir = path.join(mediaDir, 'images', path.basename(source, '.py'))
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

fs.rmSync(mediaDir, { recursive: true, force: true })

console.log(`\n${ok} diagram(s) rendered, ${failed} failed.`)
if (failed > 0) process.exitCode = 1
