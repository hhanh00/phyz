<script setup>
import { computed, ref } from 'vue'

const overviewQuestions = [
  {
    topic: 'Fields',
    question: 'What does a classical field assign to each spacetime point?',
    choices: [
      'A value that can vary with position and time',
      'A single particle with a fixed momentum',
      'Only a probability of finding an electron',
      'A Feynman diagram',
    ],
    answer: 0,
    explanation: 'A field is a function that assigns a value to every point in spacetime. The value may be a scalar, vector, or spinor, depending on the field type.',
    link: '/qft.html',
    linkText: 'Fields and Quanta',
  },
  {
    topic: 'Quantum fields',
    question: 'In quantum field theory, what is a particle?',
    choices: [
      'A term in the Lagrangian',
      'A quantized excitation of a field',
      'A field value at one point',
      'A classical wave with no quantum description',
    ],
    answer: 1,
    explanation: 'A particle is a quantum of a field. A creation operator acting on the vacuum produces a one-particle state.',
    link: '/qft.html',
    linkText: 'Fields and Quanta',
  },
  {
    topic: 'Lagrangians',
    question: 'What does the quadratic part of a free-field Lagrangian determine?',
    choices: [
      'Only the field’s electric charge',
      'The free modes and their masses',
      'The number of spacetime dimensions',
      'Which gauge we must choose',
    ],
    answer: 1,
    explanation: 'Quadratic terms describe free propagation. Their kinetic and mass terms identify the field’s modes and dispersion relation; higher-order terms describe interactions.',
    link: '/qft-action.html',
    linkText: 'Action and Lagrangians',
  },
  {
    topic: 'Symmetry',
    question: 'What is spontaneous symmetry breaking?',
    choices: [
      'The Lagrangian explicitly loses all of its symmetries',
      'A symmetric law has a ground state that does not share the full symmetry',
      'A field is forced to vanish everywhere',
      'A gauge field is removed from the theory',
    ],
    answer: 1,
    explanation: 'The laws remain symmetric, but the chosen lowest-energy configuration is not invariant under the full symmetry.',
    link: '/higgs-mechanism.html#spontaneous-symmetry-breaking',
    linkText: 'Spontaneous symmetry breaking',
  },
  {
    topic: 'Higgs mechanism',
    question: 'What does the parameter v represent in the Higgs potential?',
    choices: [
      'The radius of the circle of minima, up to the chosen normalization',
      'The speed of the Higgs boson',
      'The electric charge of the vacuum',
      'The number of Higgs particles present',
    ],
    answer: 0,
    explanation: 'With the normalization used here, the minima satisfy |φ| = v/√2. The chosen vacuum is ⟨φ⟩ = v/√2.',
    link: '/higgs-mechanism.html#spontaneous-symmetry-breaking',
    linkText: 'The Higgs vacuum',
  },
  {
    topic: 'Higgs mechanism',
    question: 'In φ = (v + h + iχ)/√2, what do h and χ describe?',
    choices: [
      'Two spatial directions',
      'The radial and angular fluctuations in field-value space',
      'The particle and antiparticle momenta',
      'The electric and magnetic fields',
    ],
    answer: 1,
    explanation: 'h is the radial fluctuation and χ is the angular or phase fluctuation. These directions refer to the complex field-value plane, not physical space.',
    link: '/higgs-mechanism.html#spontaneous-symmetry-breaking',
    linkText: 'Higgs-field fluctuations',
  },
  {
    topic: 'Gauge symmetry',
    question: 'What is introduced when a global phase symmetry becomes local?',
    choices: [
      'A gauge field and a covariant derivative',
      'A second time coordinate',
      'A new spatial dimension',
      'A probability wavefunction for the vacuum',
    ],
    answer: 0,
    explanation: 'A local phase α(x) produces derivative terms that must be compensated by a gauge field. We replace ∂μ with Dμ = ∂μ + iqAμ.',
    link: '/higgs-mechanism.html#higgs-mechanism-u1',
    linkText: 'The U(1) Higgs mechanism',
  },
  {
    topic: 'Gauge fields',
    question: 'Why does Aμ → Aμ − ∂μα/q leave Fμν unchanged?',
    choices: [
      'Because Aμ has no physical components',
      'Because mixed partial derivatives cancel',
      'Because the Higgs field is real',
      'Because the field strength contains no derivatives',
    ],
    answer: 1,
    explanation: 'The added contribution is ∂μ∂να − ∂ν∂μα, which vanishes when mixed partial derivatives commute.',
    link: '/qed.html',
    linkText: 'Quantum electrodynamics',
  },
  {
    topic: 'Fermion masses',
    question: 'What does a Yukawa coupling become after the Higgs field gets a vacuum value?',
    choices: [
      'A fermion mass term plus a Higgs–fermion interaction',
      'A photon kinetic term only',
      'A condition that removes the fermion field',
      'A new conserved spacetime dimension',
    ],
    answer: 0,
    explanation: 'For the electron, −yₑ L̄φeᵣ becomes −mₑ ēe − (mₑ/v)h ēe, with mₑ = yₑv/√2.',
    link: '/higgs-mechanism.html#fermion-masses',
    linkText: 'Fermion masses',
  },
  {
    topic: 'Gauge-boson masses',
    question: 'Where do the gauge-boson mass terms come from in the Higgs mechanism?',
    choices: [
      'They are inserted directly by hand',
      'The Higgs potential contains a term for each gauge boson',
      'The Higgs kinetic term is evaluated around a nonzero vacuum',
      'They come from the photon field strength alone',
    ],
    answer: 2,
    explanation: 'The gauge-field pieces in (Dμφ)†Dμφ remain when Dμ acts on the constant vacuum. Squaring them produces terms quadratic in the gauge fields.',
    link: '/higgs-mechanism.html#higgs-mechanism-u1',
    linkText: 'Gauge-boson masses',
  },
  {
    topic: 'Electroweak theory',
    question: 'Why does the photon remain massless in the Standard Model Higgs mechanism?',
    choices: [
      'The photon does not interact with any field',
      'The Higgs vacuum is electrically neutral, so electric charge remains unbroken',
      'The photon is not a gauge field',
      'The photon has a negative mass squared',
    ],
    answer: 1,
    explanation: 'The Higgs vacuum is annihilated by the electric-charge generator Q. The electromagnetic U(1) remains unbroken, leaving the photon massless.',
    link: '/higgs-mechanism.html#standard-model-higgs-su-2-l-u-1-y',
    linkText: 'Standard Model Higgs field',
  },
  {
    topic: 'Degrees of freedom',
    question: 'What happens to the Goldstone mode in the gauged U(1) example?',
    choices: [
      'It becomes a second photon',
      'It becomes the longitudinal polarization of the massive gauge field',
      'It is destroyed, reducing the total degrees of freedom',
      'It becomes the radial Higgs fluctuation',
    ],
    answer: 1,
    explanation: 'The complex scalar has two real degrees of freedom and the massless vector has two polarizations. Afterward there is one scalar plus three polarizations of the massive vector.',
    link: '/higgs-mechanism.html#higgs-mechanism-u1',
    linkText: 'The U(1) Higgs mechanism',
  },
]

const makeQuestion = (text, choices, answer, explanation, link, linkText) => ({
  question: text,
  choices,
  answer,
  explanation,
  link,
  linkText,
})

const chapterQuizzes = [
  ['Classical Mechanics', '/classical-mechanics.html', [
    makeQuestion('What quantity describes an object’s position and motion in phase space?', ['The action only', 'Its position and momentum', 'Its electric charge', 'Its wavefunction only'], 1, 'Classical phase space uses position and momentum to specify the state of a system.', '/classical-mechanics.html', 'Classical Mechanics'),
    makeQuestion('What principle determines the path taken by a classical system?', ['Stationary action', 'Charge conservation alone', 'The uncertainty principle', 'Gauge fixing'], 0, 'The principle of stationary action leads to the Euler–Lagrange equations.', '/classical-mechanics.html', 'Classical Mechanics'),
  ]],
  ['First Quantization', '/first-quantization.html', [
    makeQuestion('In first quantization, what becomes an operator?', ['The classical action', 'Physical quantities such as position and momentum', 'The spacetime metric', 'Every probability'], 1, 'First quantization represents observables such as position and momentum by operators acting on states.', '/first-quantization.html', 'First Quantization'),
    makeQuestion('What does the wavefunction provide when squared in magnitude?', ['A force', 'A probability density', 'A particle mass', 'A gauge transformation'], 1, 'The Born rule interprets |ψ|² as a probability density.', '/first-quantization.html', 'First Quantization'),
  ]],
  ['The Harmonic Oscillator', '/harmonic-oscillator.html', [
    makeQuestion('What is special about the harmonic oscillator’s energy levels?', ['They are equally spaced', 'They are all zero', 'They depend only on charge', 'They are continuous only'], 0, 'The quantum harmonic oscillator has evenly spaced levels, separated by ℏω.', '/harmonic-oscillator.html', 'The Harmonic Oscillator'),
    makeQuestion('What does a creation operator do?', ['Lowers the energy level', 'Creates one excitation in a mode', 'Changes the spacetime dimension', 'Removes the vacuum'], 1, 'A creation operator raises the occupation number of an oscillator by one.', '/harmonic-oscillator.html', 'The Harmonic Oscillator'),
  ]],
  ['Special Relativity', '/special-relativity.html', [
    makeQuestion('Which quantity is invariant for all inertial observers?', ['Coordinate time', 'The spacetime interval', 'The three-momentum alone', 'The speed of every object'], 1, 'Lorentz transformations preserve the spacetime interval.', '/special-relativity.html', 'Special Relativity'),
    makeQuestion('What does E² = p² + m² express?', ['Energy–momentum relation in natural units', 'Newton’s second law', 'A gauge condition', 'A probability rule'], 0, 'It is the relativistic dispersion relation with ℏ = c = 1.', '/special-relativity.html', 'Special Relativity'),
  ]],
  ['Relativistic QM', '/relativistic-qm.html', [
    makeQuestion('Why is a relativistic quantum wave equation needed?', ['To remove spacetime', 'To respect Lorentz symmetry', 'To make all particles massless', 'To avoid operators'], 1, 'A relativistic wave equation must transform consistently between inertial frames.', '/relativistic-qm.html', 'Relativistic QM'),
    makeQuestion('What difficulty appears when interpreting the Klein–Gordon density as a probability density?', ['It is always too large', 'It can be negative', 'It has no derivatives', 'It is not Lorentz covariant'], 1, 'The conserved Klein–Gordon density is not positive definite, so the field interpretation is needed.', '/relativistic-qm.html', 'Relativistic QM'),
  ]],
  ['The Dirac Equation', '/dirac-equation.html', [
    makeQuestion('What does the Dirac equation describe naturally?', ['Spin-½ relativistic fields', 'Only classical particles', 'A scalar potential', 'The Higgs vacuum only'], 0, 'The Dirac equation is first order in time and describes spin-½ matter.', '/dirac-equation.html', 'The Dirac Equation'),
    makeQuestion('What did the negative-frequency solutions lead us to recognize?', ['Antiparticles', 'A second time dimension', 'Massless photons only', 'The loss of spin'], 0, 'Quantum field theory interprets the negative-frequency family through antiparticle creation.', '/dirac-equation.html', 'The Dirac Equation'),
  ]],
  ['Fields and Quanta', '/qft.html', [
    makeQuestion('What is a particle in quantum field theory?', ['A term in the Lagrangian', 'A quantized excitation of a field', 'A point in spacetime', 'A classical force'], 1, 'A particle is a quantum of a field, created by a creation operator acting on the vacuum.', '/qft.html', 'Fields and Quanta'),
    makeQuestion('What does a field configuration describe?', ['A field’s values over a spatial slice', 'Only one particle’s position', 'A single coupling constant', 'A Feynman rule'], 0, 'At fixed time, a field configuration assigns a field value to every point in space.', '/qft.html', 'Fields and Quanta'),
  ]],
  ['Action and Lagrangians', '/qft-action.html', [
    makeQuestion('What is varied to derive the Euler–Lagrange field equation?', ['The action', 'The particle number', 'The gauge charge', 'The final state only'], 0, 'The action is stationary under allowed variations of the field.', '/qft-action.html', 'Action and Lagrangians'),
    makeQuestion('What is the Lagrangian density integrated over?', ['Momentum space only', 'Spacetime', 'Spin space only', 'The vacuum circle'], 1, 'The action is S = ∫ d⁴x ℒ in relativistic field theory.', '/qft-action.html', 'Action and Lagrangians'),
  ]],
  ['Field Quantization', '/field-quantization.html', [
    makeQuestion('What is promoted to an operator during field quantization?', ['The classical field', 'The spacetime coordinate', 'The speed of light', 'The metric signature'], 0, 'The classical field becomes an operator-valued field with an associated operator algebra.', '/field-quantization.html', 'Field Quantization'),
    makeQuestion('What does a creation operator create?', ['A new spacetime point', 'One quantum of a field mode', 'A new gauge symmetry', 'A classical action'], 1, 'Acting on the vacuum, a creation operator produces a one-particle state in a selected mode.', '/field-quantization.html', 'Field Quantization'),
  ]],
  ['Quantum Electrodynamics', '/qed.html', [
    makeQuestion('What symmetry underlies QED?', ['Local U(1) phase symmetry', 'Global rotations of space', 'SU(3) color only', 'Time reversal only'], 0, 'QED is built from local phase symmetry and its compensating electromagnetic gauge field.', '/qed.html', 'Quantum Electrodynamics'),
    makeQuestion('What is the photon field strength?', ['Fμν = ∂μAν − ∂νAμ', 'Fμν = AμAν', 'Fμν = ψ̄ψ', 'Fμν = m²φ'], 0, 'The electromagnetic field strength is the curl of the gauge potential.', '/qed.html', 'Quantum Electrodynamics'),
  ]],
  ['From Lagrangian to Experiment', '/lagrangian-to-experiment.html', [
    makeQuestion('What does a scattering amplitude describe?', ['A contribution to a transition between initial and final states', 'Only a classical trajectory', 'A field’s mass alone', 'A coordinate transformation'], 0, 'The amplitude is the quantum quantity used to calculate transition probabilities and rates.', '/lagrangian-to-experiment.html', 'From Lagrangian to Experiment'),
    makeQuestion('What connects a calculated amplitude to an experimental rate?', ['Phase space and flux factors', 'A gauge rotation only', 'The field’s name', 'The metric signature alone'], 0, 'Cross sections and decay rates combine amplitudes with kinematics and normalization factors.', '/lagrangian-to-experiment.html', 'From Lagrangian to Experiment'),
  ]],
  ['Perturbation Theory', '/perturbation-theory.html', [
    makeQuestion('What is expanded in perturbation theory?', ['The interaction contribution in powers of its coupling', 'The number of dimensions', 'The vacuum into particles only', 'The speed of light'], 0, 'Weak interactions can be approximated by organizing terms in powers of a small coupling.', '/perturbation-theory.html', 'Perturbation Theory'),
    makeQuestion('What does each additional order generally represent?', ['More interaction vertices and corrections', 'A new spacetime dimension', 'A different metric signature', 'A new particle species automatically'], 0, 'Higher orders add more detailed interaction processes and quantum corrections.', '/perturbation-theory.html', 'Perturbation Theory'),
  ]],
  ['Feynman Rules for QED', '/feynman-rules.html', [
    makeQuestion('What does a vertex factor encode?', ['The mathematical factor associated with an interaction', 'A particle’s position', 'A choice of vacuum', 'A field configuration only'], 0, 'Feynman rules translate each diagram component into a factor in the amplitude.', '/feynman-rules.html', 'Feynman Rules for QED'),
    makeQuestion('What do internal lines represent in a diagram?', ['Propagators connecting interaction vertices', 'External detectors', 'Gauge choices only', 'Classical field minima'], 0, 'An internal line contributes a propagator for the field exchanged between vertices.', '/feynman-rules.html', 'Feynman Rules for QED'),
  ]],
  ['Weak Interaction', '/weak-interaction.html', [
    makeQuestion('What feature distinguishes the charged weak current?', ['It couples to left-chiral fermions', 'It couples only to photons', 'It preserves parity exactly', 'It carries electric charge zero only'], 0, 'The charged weak interaction is chiral and selects left-chiral fermion fields.', '/weak-interaction.html', 'Weak Interaction'),
    makeQuestion('What particle mediates charged weak interactions?', ['The W boson', 'The photon', 'The gluon', 'The Higgs only'], 0, 'W⁺ and W⁻ exchange changes fermion species and carries charged weak interactions.', '/weak-interaction.html', 'Weak Interaction'),
  ]],
  ['Electroweak Unification', '/electroweak-unification.html', [
    makeQuestion('Which gauge group describes the electroweak theory?', ['SU(2)L × U(1)Y', 'SU(3)C only', 'U(1) × U(1) with no weak fields', 'SO(3) only'], 0, 'The electroweak theory combines weak isospin SU(2)L and hypercharge U(1)Y.', '/electroweak-unification.html', 'Electroweak Unification'),
    makeQuestion('What are the photon and Z boson before electroweak mixing?', ['The W³ and B fields’ mass eigenstate combinations', 'Two scalar fields', 'Two quarks', 'The charged W fields'], 0, 'The neutral gauge fields W³ and B mix to produce A and Z.', '/electroweak-unification.html', 'Electroweak Unification'),
  ]],
  ['Higgs Mechanism', '/higgs-mechanism.html', [
    makeQuestion('What does the Higgs vacuum value generate?', ['Mass terms from gauge-invariant interactions', 'A preferred spatial direction', 'Only massless particles', 'A new spacetime coordinate'], 0, 'Expanding invariant kinetic and Yukawa terms around the nonzero vacuum produces effective masses.', '/higgs-mechanism.html', 'Higgs Mechanism'),
    makeQuestion('What happens to the three Goldstone modes in the Standard Model?', ['They become longitudinal modes of W⁺, W⁻, and Z', 'They become photons', 'They disappear without changing degrees of freedom', 'They become quarks'], 0, 'Three scalar degrees of freedom supply the additional polarizations of the three massive weak bosons.', '/higgs-mechanism.html', 'Higgs Mechanism'),
  ]],
  ['Quantum Chromodynamics', '/qcd.html', [
    makeQuestion('What is the gauge group of QCD?', ['SU(3)C', 'U(1)EM', 'SU(2)L only', 'SO(1,3)'], 0, 'QCD is the SU(3) color gauge theory of quarks and gluons.', '/qcd.html', 'Quantum Chromodynamics'),
    makeQuestion('What property prevents isolated colored particles from being observed?', ['Confinement', 'Electromagnetic neutrality', 'Spontaneous parity restoration', 'The Higgs phase'], 0, 'Color confinement keeps quarks and gluons inside color-neutral hadrons.', '/qcd.html', 'Quantum Chromodynamics'),
  ]],
  ['The Standard Model', '/standard-model.html', [
    makeQuestion('What does the Standard Model organize?', ['Matter fields, gauge fields, interactions, and the Higgs field', 'Only classical mechanics', 'Only gravitational waves', 'Only atomic orbitals'], 0, 'The Standard Model combines the known quarks, leptons, gauge interactions, and Higgs sector.', '/standard-model.html', 'The Standard Model'),
    makeQuestion('Which interaction is not included in the Standard Model?', ['Gravity', 'Electromagnetism', 'The weak interaction', 'The strong interaction'], 0, 'The Standard Model does not provide a quantum theory of gravity.', '/standard-model.html', 'The Standard Model'),
  ]],
  ['Path Integrals in Quantum Mechanics', '/path-integrals.html', [
    makeQuestion('What does the path integral sum over?', ['Possible histories between initial and final states', 'Only the classical path', 'Only particle masses', 'Gauge charges only'], 0, 'Each history contributes an amplitude weighted by its action phase.', '/path-integrals.html', 'Path Integrals in Quantum Mechanics'),
    makeQuestion('What makes different histories interfere?', ['Their complex amplitudes', 'Their rest masses being equal', 'A gauge field being absent', 'The action being zero always'], 0, 'The path integral adds complex amplitudes, allowing constructive and destructive interference.', '/path-integrals.html', 'Path Integrals in Quantum Mechanics'),
  ]],
  ['Path Integrals for Fields', '/path-integrals-fields.html', [
    makeQuestion('What is integrated over in a field path integral?', ['Field configurations or histories', 'Only particle positions', 'Only Feynman vertices', 'Only the vacuum value'], 0, 'The field path integral sums over possible spacetime field configurations.', '/path-integrals-fields.html', 'Path Integrals for Fields'),
    makeQuestion('What does the generating functional help calculate?', ['Correlation functions', 'Only classical orbits', 'The speed of light', 'The number of dimensions'], 0, 'Functional derivatives of the generating functional produce field correlation functions.', '/path-integrals-fields.html', 'Path Integrals for Fields'),
  ]],
  ['Fermionic Path Integrals', '/path-integrals-fermions.html', [
    makeQuestion('What kind of variables represent fermions in a path integral?', ['Grassmann-valued anticommuting variables', 'Ordinary commuting numbers only', 'Vectors in physical space', 'Gauge potentials only'], 0, 'Grassmann variables encode the anticommutation of fermionic fields.', '/path-integrals-fermions.html', 'Fermionic Path Integrals'),
    makeQuestion('Why must fermionic variables anticommute?', ['To reproduce fermion exchange statistics', 'To make photons massive', 'To break Lorentz symmetry', 'To remove antiparticles'], 0, 'Anticommutation gives the required sign change when fermions are exchanged.', '/path-integrals-fermions.html', 'Fermionic Path Integrals'),
  ]],
  ['Gauge Fixing', '/path-integrals-gauge-fixing.html', [
    makeQuestion('Why is gauge fixing used in gauge-field calculations?', ['Gauge descriptions contain redundant variables', 'Gauge fields have no dynamics', 'It removes all interactions', 'It makes every field real'], 0, 'Different gauge potentials can describe the same physical configuration, so a calculational condition is needed.', '/path-integrals-gauge-fixing.html', 'Gauge Fixing'),
    makeQuestion('What does a gauge transformation leave unchanged in electromagnetism?', ['The field strength Fμν', 'The potential Aμ itself', 'Every field value separately', 'The gauge choice'], 0, 'Adding a gradient to Aμ leaves its curl, Fμν, unchanged.', '/path-integrals-gauge-fixing.html', 'Gauge Fixing'),
  ]],
  ['Renormalization at One Loop', '/path-integrals-renormalization.html', [
    makeQuestion('What problem does renormalization address?', ['Divergent intermediate quantum corrections', 'The lack of classical trajectories', 'The number of polarizations only', 'The existence of gauge symmetry'], 0, 'Renormalization reorganizes divergent loop calculations in terms of measured parameters.', '/path-integrals-renormalization.html', 'Renormalization at One Loop'),
    makeQuestion('What is a loop correction?', ['A quantum contribution involving an internal momentum integration', 'A classical circular orbit', 'A gauge transformation', 'A new spacetime axis'], 0, 'Loop diagrams represent virtual quantum corrections and typically involve momentum integrals.', '/path-integrals-renormalization.html', 'Renormalization at One Loop'),
  ]],
  ['Final Recap', '/recap.html', [
    makeQuestion('What is the overall route developed by the site?', ['Classical mechanics → quantum theory → quantum fields → interactions', 'Gravity → thermodynamics only', 'Particles → classical fields only', 'Geometry → chemistry only'], 0, 'The chapters build the concepts progressively from mechanics to the Standard Model.', '/recap.html', 'Final Recap'),
    makeQuestion('What does a successful field-theory calculation connect?', ['A Lagrangian to measurable predictions', 'A vacuum to a new dimension', 'A diagram to a coordinate choice only', 'A particle to a classical orbit only'], 0, 'The Lagrangian determines amplitudes, which lead to observable rates and cross sections.', '/recap.html', 'Final Recap'),
  ]],
]

const quizSets = [
  { title: 'Mixed review', link: '/', questions: overviewQuestions },
  ...chapterQuizzes.map(([title, link, questions]) => ({ title, link, questions })),
]

const selectedQuiz = ref(0)
const current = ref(0)
const selected = ref(null)
const score = ref(0)
const finished = ref(false)

const activeQuiz = computed(() => quizSets[selectedQuiz.value])
const questions = computed(() => activeQuiz.value.questions)
const question = computed(() => questions.value[current.value])
const progress = computed(() => ((current.value + (selected.value === null ? 0 : 1)) / questions.value.length) * 100)
const isCorrect = computed(() => selected.value === question.value.answer)

function choose(index) {
  if (selected.value !== null) return
  selected.value = index
  if (index === question.value.answer) score.value += 1
}

function next() {
  if (selected.value === null) return
  if (current.value === questions.value.length - 1) {
    finished.value = true
    return
  }
  current.value += 1
  selected.value = null
}

function selectQuiz() {
  current.value = 0
  selected.value = null
  score.value = 0
  finished.value = false
}

function restart() {
  current.value = 0
  selected.value = null
  score.value = 0
  finished.value = false
}
</script>

<template>
  <main class="quiz-page" aria-labelledby="quiz-title">
    <header class="quiz-header">
      <p class="quiz-kicker"><span class="quiz-kicker-dot"></span>Phyz / Check your understanding</p>
      <h1 id="quiz-title">Physics checkpoint</h1>
      <p>Test the ideas from the path so far. Choose an answer, read the explanation, and move at your own pace.</p>
    </header>

    <div class="quiz-picker">
      <label for="quiz-select">Choose a quiz</label>
      <select id="quiz-select" v-model.number="selectedQuiz" @change="selectQuiz">
        <option v-for="(quiz, index) in quizSets" :key="quiz.title" :value="index">{{ quiz.title }}</option>
      </select>
    </div>

    <section v-if="!finished" class="quiz-card" aria-live="polite">
      <div class="quiz-meta">
        <span>{{ question.topic }}</span>
        <span>Question {{ current + 1 }} of {{ questions.length }}</span>
      </div>

      <div class="progress-track" aria-hidden="true">
        <div class="progress-bar" :style="{ width: progress + '%' }"></div>
      </div>

      <h2>{{ question.question }}</h2>

      <div class="choices" role="radiogroup" :aria-label="question.question">
        <button
          v-for="(choice, index) in question.choices"
          :key="choice"
          class="choice"
          :class="{
            selected: selected === index,
            correct: selected !== null && index === question.answer,
            incorrect: selected === index && index !== question.answer,
          }"
          type="button"
          role="radio"
          :aria-checked="selected === index"
          @click="choose(index)"
        >
          <span class="choice-marker">{{ String.fromCharCode(65 + index) }}</span>
          <span>{{ choice }}</span>
          <span v-if="selected !== null && index === question.answer" class="choice-status" aria-label="Correct">✓</span>
          <span v-else-if="selected === index" class="choice-status" aria-label="Incorrect">×</span>
        </button>
      </div>

      <div v-if="selected !== null" class="feedback" :class="{ 'feedback-correct': isCorrect }">
        <strong>{{ isCorrect ? 'Correct.' : 'Not quite.' }}</strong>
        <p>{{ question.explanation }}</p>
        <a :href="question.link">Review: {{ question.linkText }} <span aria-hidden="true">↗</span></a>
      </div>

      <button class="next-button" type="button" :disabled="selected === null" @click="next">
        {{ current === questions.length - 1 ? 'See results' : 'Next question' }}
        <span aria-hidden="true">→</span>
      </button>
    </section>

    <section v-else class="quiz-card results-card" aria-live="polite">
      <p class="results-eyebrow">Checkpoint complete</p>
      <div class="score-ring" :style="{ '--score': (score / questions.length) * 100 + '%' }">
        <strong>{{ score }}</strong>
        <span>/ {{ questions.length }}</span>
      </div>
      <h2>{{ score === questions.length ? 'Perfect run.' : score >= questions.length * 0.7 ? 'Strong foundation.' : 'Good place to review.' }}</h2>
      <p class="results-copy">You got {{ score }} of {{ questions.length }} questions correct in the {{ activeQuiz.title }} quiz. Revisit the linked chapters for anything you want to reinforce.</p>
      <div class="results-actions">
        <button class="next-button" type="button" @click="restart">Try again <span aria-hidden="true">↻</span></button>
        <a class="secondary-button" href="/">Back to chapters</a>
      </div>
    </section>
  </main>
</template>

<style>
.quiz-page {
  --quiz-ink: #152238;
  --quiz-muted: #5f6b7c;
  --quiz-line: #dce3ec;
  --quiz-blue: #2563eb;
  max-width: 760px;
  margin: 0 auto;
  padding: 4.5rem 1.5rem 6rem;
  color: var(--quiz-ink);
}

.quiz-header { max-width: 620px; margin-bottom: 2.25rem; }
.quiz-kicker, .results-eyebrow { color: var(--quiz-blue); font-size: .78rem; font-weight: 700; letter-spacing: .11em; text-transform: uppercase; }
.quiz-kicker { display: flex; align-items: center; gap: .55rem; margin: 0 0 1.1rem; }
.quiz-kicker-dot { width: .5rem; height: .5rem; border-radius: 50%; background: var(--quiz-blue); box-shadow: 0 0 0 .28rem #dbeafe; }
.quiz-header h1 { margin: 0 0 .8rem; font-size: clamp(2rem, 5vw, 3.2rem); letter-spacing: -.04em; }
.quiz-header > p:last-child { color: var(--quiz-muted); font-size: 1.05rem; line-height: 1.7; }
.quiz-picker { display: flex; align-items: center; gap: .8rem; margin-bottom: 1rem; color: var(--quiz-muted); font-size: .9rem; font-weight: 700; }
.quiz-picker select { min-width: 230px; padding: .65rem 2rem .65rem .75rem; border: 1px solid var(--quiz-line); border-radius: 8px; color: var(--quiz-ink); background: #fff; font: inherit; font-size: .9rem; cursor: pointer; }

.quiz-card { border: 1px solid var(--quiz-line); border-radius: 18px; padding: clamp(1.25rem, 4vw, 2.25rem); box-shadow: 0 18px 45px rgba(21, 34, 56, .08); background: #fff; }
.quiz-meta { display: flex; justify-content: space-between; gap: 1rem; color: var(--quiz-muted); font-size: .82rem; font-weight: 700; letter-spacing: .03em; }
.quiz-meta span:first-child { color: var(--quiz-blue); }
.progress-track { height: 5px; margin: 1.25rem 0 2rem; overflow: hidden; border-radius: 99px; background: #edf1f6; }
.progress-bar { height: 100%; border-radius: inherit; background: var(--quiz-blue); transition: width .25s ease; }
.quiz-card h2 { margin: 0 0 1.5rem; font-size: clamp(1.35rem, 3vw, 1.85rem); line-height: 1.3; letter-spacing: -.025em; }
.choices { display: grid; gap: .75rem; }
.choice { display: flex; align-items: center; gap: .85rem; width: 100%; padding: .95rem 1rem; border: 1px solid var(--quiz-line); border-radius: 11px; color: var(--quiz-ink); background: #fff; font: inherit; text-align: left; cursor: pointer; transition: border-color .18s ease, background .18s ease, transform .18s ease; }
.choice:hover:not(.selected):not(.correct) { border-color: #93b4f8; background: #f8fbff; transform: translateY(-1px); }
.choice-marker { display: grid; flex: 0 0 1.7rem; place-items: center; width: 1.7rem; height: 1.7rem; border: 1px solid #cbd5e1; border-radius: 50%; color: var(--quiz-muted); font-size: .78rem; font-weight: 700; }
.choice.selected { border-color: #93b4f8; background: #eff6ff; }
.choice.correct { border-color: #6ee7b7; background: #ecfdf5; }
.choice.incorrect { border-color: #fca5a5; background: #fff1f2; }
.choice-status { margin-left: auto; font-size: 1.1rem; font-weight: 800; }
.choice.correct .choice-status { color: #059669; }
.choice.incorrect .choice-status { color: #e11d48; }

.feedback { margin-top: 1.35rem; padding: 1rem 1.1rem; border-left: 3px solid #f59e0b; border-radius: 0 9px 9px 0; background: #fffbeb; color: var(--quiz-ink); }
.feedback-correct { border-color: #10b981; background: #ecfdf5; }
.feedback strong { font-size: .92rem; }
.feedback p { margin: .35rem 0 .6rem; color: var(--quiz-muted); line-height: 1.6; }
.feedback a { color: var(--quiz-blue); font-size: .88rem; font-weight: 700; text-decoration: none; }
.feedback a:hover { text-decoration: underline; }
.next-button, .secondary-button { display: inline-flex; align-items: center; justify-content: center; gap: .6rem; min-height: 2.8rem; padding: .65rem 1rem; border: 1px solid var(--quiz-blue); border-radius: 9px; font: inherit; font-size: .9rem; font-weight: 700; text-decoration: none; cursor: pointer; }
.next-button { margin-top: 1.5rem; color: #fff; background: var(--quiz-blue); }
.next-button:disabled { opacity: .45; cursor: not-allowed; }
.next-button:not(:disabled):hover { background: #1d4ed8; }
.secondary-button { color: var(--quiz-blue); background: #fff; }
.secondary-button:hover { background: #eff6ff; }

.results-card { text-align: center; }
.results-eyebrow { margin: 0 0 1.25rem; }
.score-ring { display: flex; align-items: baseline; justify-content: center; gap: .15rem; width: 142px; height: 142px; margin: 0 auto 1.5rem; border: 10px solid #dbeafe; border-top-color: var(--quiz-blue); border-right-color: var(--quiz-blue); border-radius: 50%; transform: rotate(25deg); }
.score-ring strong, .score-ring span { transform: rotate(-25deg); }
.score-ring strong { font-size: 2.3rem; letter-spacing: -.06em; }
.score-ring span { color: var(--quiz-muted); font-size: 1rem; }
.results-card h2 { margin-bottom: .6rem; }
.results-copy { max-width: 480px; margin: 0 auto; color: var(--quiz-muted); line-height: 1.7; }
.results-actions { display: flex; flex-wrap: wrap; justify-content: center; gap: .75rem; margin-top: 1.5rem; }
.results-actions .next-button { margin-top: 0; }

@media (max-width: 600px) {
  .quiz-page { padding-top: 2.5rem; }
  .quiz-picker { align-items: stretch; flex-direction: column; gap: .4rem; }
  .quiz-picker select { width: 100%; }
  .quiz-meta { align-items: flex-start; flex-direction: column; gap: .35rem; }
  .quiz-card { border-radius: 14px; }
}
</style>
