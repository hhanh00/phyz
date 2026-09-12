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

// Six additional checks per chapter bring the static bank to eight questions
// per chapter. Keeping these as data makes the quiz deterministic and easy to
// extend without changing the quiz logic.
const extraByChapter = {
  'Classical Mechanics': [
    makeQuestion('What is the purpose of a Lagrangian?', ['To encode the system’s dynamics in one function', 'To list only its particles', 'To choose a gauge', 'To define electric charge'], 0, 'The Lagrangian combines kinetic and potential information and generates the equations of motion.', '/classical-mechanics.html', 'Classical Mechanics'),
    makeQuestion('What does momentum measure in Lagrangian mechanics?', ['Sensitivity of the Lagrangian to velocity', 'The field’s spin', 'The number of particles', 'The value of the action'], 0, 'Canonical momentum is defined by the derivative of the Lagrangian with respect to velocity.', '/classical-mechanics.html', 'Classical Mechanics'),
    makeQuestion('What is the action?', ['The time integral of the Lagrangian', 'The instantaneous velocity', 'A force divided by mass', 'A quantum commutator'], 0, 'The action is S = ∫ L dt, and stationary action determines the classical path.', '/classical-mechanics.html', 'Classical Mechanics'),
    makeQuestion('What does Hamilton’s formulation use as state variables?', ['Coordinates and conjugate momenta', 'Only accelerations', 'Only forces', 'Only energies'], 0, 'Hamiltonian mechanics evolves positions or coordinates together with their conjugate momenta.', '/classical-mechanics.html', 'Classical Mechanics'),
    makeQuestion('What is a conserved quantity usually associated with?', ['A continuous symmetry', 'A coordinate singularity', 'A random fluctuation', 'A choice of units'], 0, 'Noether’s idea connects continuous symmetries with conserved quantities.', '/classical-mechanics.html', 'Classical Mechanics'),
    makeQuestion('What does the Euler–Lagrange equation determine?', ['The equations of motion', 'The number of dimensions', 'The particle’s charge', 'The field’s quantization'], 0, 'Varying the action gives the Euler–Lagrange equation for the path or field.', '/classical-mechanics.html', 'Classical Mechanics'),
  ],
  'First Quantization': [
    makeQuestion('What is a quantum state?', ['A vector in a state space', 'A classical trajectory only', 'A force field only', 'A coordinate system'], 0, 'Quantum states are vectors, represented by kets, on which observables act as operators.', '/first-quantization.html', 'First Quantization'),
    makeQuestion('What is the role of an observable operator?', ['It represents a measurable quantity', 'It creates spacetime', 'It removes normalization', 'It fixes a gauge'], 0, 'Position, momentum, and energy are represented by operators in quantum mechanics.', '/first-quantization.html', 'First Quantization'),
    makeQuestion('What does a measurement do to a superposition?', ['It yields one possible outcome with a probability', 'It always returns every value', 'It removes the Hamiltonian', 'It turns the state classical everywhere'], 0, 'The Born rule assigns probabilities to possible measurement outcomes.', '/first-quantization.html', 'First Quantization'),
    makeQuestion('What equation governs time evolution in nonrelativistic quantum mechanics?', ['The Schrödinger equation', 'The Klein–Gordon equation only', 'Maxwell’s equations', 'The Euler identity'], 0, 'The Schrödinger equation determines how a quantum state evolves in time.', '/first-quantization.html', 'First Quantization'),
    makeQuestion('What is a commutator used to express?', ['The order dependence of two operators', 'A particle’s rest mass', 'A field’s spatial value', 'A conserved current alone'], 0, 'Nonzero commutators encode the incompatibility of certain observables.', '/first-quantization.html', 'First Quantization'),
    makeQuestion('What does normalization of a wavefunction ensure?', ['Total probability is one', 'Energy is always zero', 'Momentum is fixed', 'The state is classical'], 0, 'A normalized wavefunction gives total probability one when integrated over space.', '/first-quantization.html', 'First Quantization'),
  ],
  'The Harmonic Oscillator': [
    makeQuestion('What is the ground state?', ['The lowest-energy state', 'The state with infinite energy', 'A classical path', 'A gauge field'], 0, 'The ground state is the oscillator’s minimum-energy quantum state.', '/harmonic-oscillator.html', 'The Harmonic Oscillator'),
    makeQuestion('What is zero-point energy?', ['The nonzero ground-state energy', 'The energy of no field at all', 'The maximum energy', 'A potential’s slope'], 0, 'Quantum uncertainty leaves the harmonic oscillator with energy even in its ground state.', '/harmonic-oscillator.html', 'The Harmonic Oscillator'),
    makeQuestion('What does an annihilation operator do to the ground state?', ['It gives zero', 'It creates two quanta', 'It changes the mass', 'It reverses time'], 0, 'There is no lower occupation number than zero, so a|0⟩ = 0.', '/harmonic-oscillator.html', 'The Harmonic Oscillator'),
    makeQuestion('What labels an oscillator’s energy eigenstates?', ['An occupation number', 'A gauge parameter', 'A spacetime index only', 'A Lagrangian density'], 0, 'The number state |n⟩ records how many quanta occupy the oscillator mode.', '/harmonic-oscillator.html', 'The Harmonic Oscillator'),
    makeQuestion('What is the commutator [a, a†] for the oscillator?', ['1', '0 for every oscillator', 'The mass', 'The Hamiltonian'], 0, 'The canonical oscillator algebra is [a, a†] = 1.', '/harmonic-oscillator.html', 'The Harmonic Oscillator'),
    makeQuestion('What happens when a† acts repeatedly?', ['It raises the occupation number', 'It removes the vacuum', 'It fixes position', 'It changes spin to zero'], 0, 'Each creation operator raises the oscillator’s excitation number by one.', '/harmonic-oscillator.html', 'The Harmonic Oscillator'),
  ],
  'Special Relativity': [
    makeQuestion('What is a Lorentz transformation?', ['A change between inertial frames preserving the interval', 'A quantum measurement', 'A gauge fixing condition', 'A field interaction'], 0, 'Lorentz transformations relate inertial observers while preserving spacetime geometry.', '/special-relativity.html', 'Special Relativity'),
    makeQuestion('What is proper time?', ['Time measured along an object’s worldline', 'Universal coordinate time', 'The time in a gauge choice', 'A particle’s energy'], 0, 'Proper time is the invariant time interval along a timelike path.', '/special-relativity.html', 'Special Relativity'),
    makeQuestion('What is the light cone used to classify?', ['Causal relationships between events', 'Particle spin only', 'Gauge charges', 'Potential minima'], 0, 'The light cone separates timelike, lightlike, and spacelike separations.', '/special-relativity.html', 'Special Relativity'),
    makeQuestion('What does c represent in special relativity?', ['The invariant speed of light', 'A particle’s charge', 'A coupling constant only', 'A coordinate label'], 0, 'All inertial observers measure the same speed c for light in vacuum.', '/special-relativity.html', 'Special Relativity'),
    makeQuestion('What is four-momentum?', ['The energy and three-momentum combined', 'Four independent masses', 'A spinor', 'A gauge potential'], 0, 'Four-momentum is pμ = (E, p) in natural units.', '/special-relativity.html', 'Special Relativity'),
    makeQuestion('What does mass shell mean?', ['The relativistic relation between energy, momentum, and mass', 'A particle’s physical surface', 'A potential minimum', 'A coordinate frame'], 0, 'On-shell four-momenta satisfy p² = m² in the chosen units and signature.', '/special-relativity.html', 'Special Relativity'),
  ],
  'Relativistic QM': [
    makeQuestion('What does Lorentz covariance require?', ['Equations keep the same form between inertial frames', 'All fields be scalars', 'All masses vanish', 'Coordinates stop changing'], 0, 'Relativistic equations must transform consistently under Lorentz transformations.', '/relativistic-qm.html', 'Relativistic QM'),
    makeQuestion('What is the Klein–Gordon equation for?', ['A relativistic scalar field', 'Only a classical orbit', 'A gauge choice', 'A spin-½ current'], 0, 'The Klein–Gordon equation is the relativistic wave equation for spin-0 fields.', '/relativistic-qm.html', 'Relativistic QM'),
    makeQuestion('What does a conserved current express?', ['A locally conserved quantity', 'A particle’s position only', 'A choice of phase', 'A mass eigenstate only'], 0, 'A continuity equation expresses local conservation of a charge or density.', '/relativistic-qm.html', 'Relativistic QM'),
    makeQuestion('Why is a field interpretation needed for the Klein–Gordon equation?', ['Its conserved density is not a probability density', 'It has no solutions', 'It is not relativistic', 'It contains no mass'], 0, 'The density can be negative, so it is interpreted as charge density in a field theory.', '/relativistic-qm.html', 'Relativistic QM'),
    makeQuestion('What relation does a free relativistic field satisfy?', ['A dispersion relation between E, p, and m', 'A gauge-fixing equation only', 'A thermodynamic identity', 'A classical orbit equation'], 0, 'Free modes obey E² = p² + m² in natural units.', '/relativistic-qm.html', 'Relativistic QM'),
    makeQuestion('What does a plane wave have?', ['Definite momentum', 'Definite position', 'No energy', 'No phase'], 0, 'A plane wave is a momentum eigenmode and is spread throughout space.', '/relativistic-qm.html', 'Relativistic QM'),
  ],
  'The Dirac Equation': [
    makeQuestion('Why was the Dirac equation made first order in time?', ['To give a suitable relativistic quantum evolution equation', 'To remove spin', 'To make particles classical', 'To eliminate antimatter'], 0, 'Dirac’s construction gives a relativistic equation compatible with quantum evolution and spin-½.', '/dirac-equation.html', 'The Dirac Equation'),
    makeQuestion('What do gamma matrices act on?', ['Spinor components', 'Spacetime points directly', 'Particle positions only', 'Gauge group elements only'], 0, 'Gamma matrices act on the components of a spinor field.', '/dirac-equation.html', 'The Dirac Equation'),
    makeQuestion('What is a spinor?', ['An object with a spin-½ Lorentz transformation law', 'A scalar potential', 'A vector field strength', 'A classical trajectory'], 0, 'Spinors transform differently from scalars and vectors and describe fermions.', '/dirac-equation.html', 'The Dirac Equation'),
    makeQuestion('What does γ⁵ help distinguish?', ['Left- and right-chiral parts', 'Energy from momentum', 'Space from time', 'Particles from fields'], 0, 'The γ⁵ operator defines the chiral projectors PL and PR.', '/dirac-equation.html', 'The Dirac Equation'),
    makeQuestion('What is an antiparticle?', ['A corresponding excitation with opposite conserved charges', 'A particle moving backward in time literally', 'A negative-energy detector', 'A gauge transformation'], 0, 'Quantum fields reinterpret negative-frequency solutions as positive-energy antiparticle excitations.', '/dirac-equation.html', 'The Dirac Equation'),
    makeQuestion('What statistics do fermions obey?', ['Fermi–Dirac statistics', 'Bose–Einstein statistics', 'Classical statistics only', 'No exchange rule'], 0, 'Fermions are described by anticommuting operators and obey the exclusion principle.', '/dirac-equation.html', 'The Dirac Equation'),
  ],
  'Fields and Quanta': [
    makeQuestion('What does a field configuration contain?', ['The field value at every point of a spatial slice', 'One particle only', 'One number for the whole universe', 'Only a field’s mass'], 0, 'A configuration is an entire spatial assignment, not a value at just one point.', '/qft.html', 'Fields and Quanta'),
    makeQuestion('What is a real scalar field’s value space?', ['The real numbers', 'Four-vectors', 'Spinor space', 'Matrices only'], 0, 'A real scalar assigns one real number to each spacetime point.', '/qft.html', 'Fields and Quanta'),
    makeQuestion('What is a complex scalar equivalent to?', ['Two real scalar degrees of freedom', 'Two vector fields', 'One spinor', 'Four gauge bosons'], 0, 'The real and imaginary parts of a complex scalar are two real fields.', '/qft.html', 'Fields and Quanta'),
    makeQuestion('What is a mode in free space?', ['An independent wave pattern labeled by momentum', 'A particle detector', 'A potential minimum only', 'A gauge transformation'], 0, 'Fourier modes provide independent wave patterns for a translationally invariant free field.', '/qft.html', 'Fields and Quanta'),
    makeQuestion('What does the vacuum contain in the particle description?', ['No excitations', 'Every particle equally', 'Only photons', 'Infinite energy particles'], 0, 'The vacuum is the lowest-energy state annihilated by all annihilation operators.', '/qft.html', 'Fields and Quanta'),
    makeQuestion('What does a creation operator do to the vacuum?', ['Creates a one-particle state', 'Makes the field classical', 'Removes all modes', 'Changes the metric'], 0, 'For a mode p, a†(p)|0⟩ is a one-particle state with that momentum.', '/qft.html', 'Fields and Quanta'),
  ],
  'Action and Lagrangians': [
    makeQuestion('What is a Lagrangian density?', ['A local function of fields and derivatives', 'A particle’s wavefunction', 'A gauge parameter', 'A probability value'], 0, 'The Lagrangian density is integrated over spacetime to form the action.', '/qft-action.html', 'Action and Lagrangians'),
    makeQuestion('What condition does the physical field history satisfy?', ['Stationary action', 'Maximum potential everywhere', 'Zero momentum everywhere', 'Fixed gauge charge'], 0, 'The physical history makes the action stationary under allowed variations.', '/qft-action.html', 'Action and Lagrangians'),
    makeQuestion('What is a kinetic term associated with?', ['Spacetime derivatives of a field', 'Only the field’s charge', 'A boundary condition only', 'A particle label'], 0, 'Derivative terms govern how a field propagates and varies through spacetime.', '/qft-action.html', 'Action and Lagrangians'),
    makeQuestion('What does a mass term do in a scalar Lagrangian?', ['Sets the free field’s mass scale', 'Creates a gauge symmetry', 'Removes all interactions', 'Defines spatial coordinates'], 0, 'The quadratic mass term determines the mass in the free equation of motion.', '/qft-action.html', 'Action and Lagrangians'),
    makeQuestion('What are higher-order field terms usually responsible for?', ['Interactions', 'Changing the number of dimensions', 'Removing the vacuum', 'Defining spinor space'], 0, 'Cubic and quartic terms produce interaction vertices among field excitations.', '/qft-action.html', 'Action and Lagrangians'),
    makeQuestion('What is a total derivative often related to?', ['A boundary contribution', 'A new particle species', 'A massless mode always', 'A change of spin'], 0, 'Total derivatives affect boundary terms and often do not change local equations of motion.', '/qft-action.html', 'Action and Lagrangians'),
  ],
  'Field Quantization': [
    makeQuestion('What replaces classical mode amplitudes after quantization?', ['Operators', 'Coordinates only', 'Classical probabilities', 'Fixed numbers forever'], 0, 'Mode amplitudes become creation and annihilation operators.', '/field-quantization.html', 'Field Quantization'),
    makeQuestion('What algebra do bosonic creation and annihilation operators satisfy?', ['Commutation relations', 'Anticommutation relations only', 'No algebra', 'Lorentz transformations only'], 0, 'Bosonic operators commute in the appropriate mode algebra.', '/field-quantization.html', 'Field Quantization'),
    makeQuestion('What does a real quantum field satisfy?', ['Hermiticity', 'Vanishing energy', 'Fixed position', 'Anticommutation with itself'], 0, 'A real field operator obeys φ̂† = φ̂.', '/field-quantization.html', 'Field Quantization'),
    makeQuestion('Why does a mode expansion contain positive and negative frequencies?', ['They form the general solution and pair with lowering and raising operators', 'Only to add dimensions', 'To remove momentum', 'Because all fields are real'], 0, 'The two frequency parts reflect the second-order mode equation and quantum creation/annihilation roles.', '/field-quantization.html', 'Field Quantization'),
    makeQuestion('What is the occupation number operator used for?', ['Counting quanta in a mode', 'Measuring spacetime curvature', 'Choosing a vacuum orientation', 'Defining a gauge field'], 0, 'The number operator has eigenvalues n for states with n excitations.', '/field-quantization.html', 'Field Quantization'),
    makeQuestion('What determines whether a field’s quanta are bosons or fermions?', ['The field’s operator algebra and spin-statistics connection', 'Its color only', 'Its vacuum value only', 'The choice of coordinates'], 0, 'Commutators describe bosons, anticommutators describe fermions, consistently with spin.', '/field-quantization.html', 'Field Quantization'),
  ],
  'Quantum Electrodynamics': [
    makeQuestion('What does Aμ represent in QED?', ['The electromagnetic gauge potential', 'The electron spinor', 'The Higgs vacuum', 'A scalar mass'], 0, 'Aμ is the electromagnetic gauge field, or four-potential.', '/qed.html', 'Quantum Electrodynamics'),
    makeQuestion('What does local phase invariance require?', ['A compensating gauge potential', 'A massive photon', 'A fixed particle number', 'A broken Lorentz symmetry'], 0, 'The gauge field compensates derivatives of a spacetime-dependent phase.', '/qed.html', 'Quantum Electrodynamics'),
    makeQuestion('What particle is the quantum of the electromagnetic field?', ['The photon', 'The electron', 'The gluon', 'The Higgs boson'], 0, 'Photon states are excitations of the electromagnetic gauge field.', '/qed.html', 'Quantum Electrodynamics'),
    makeQuestion('What charge does the photon carry?', ['Zero electric charge', 'One electron charge', 'Color charge only', 'Weak isospin only'], 0, 'The photon is electrically neutral, although it mediates electromagnetic interactions.', '/qed.html', 'Quantum Electrodynamics'),
    makeQuestion('What does the QED interaction couple?', ['The electron current to the electromagnetic field', 'Two Higgs potentials only', 'Two spacetime metrics', 'Only photon fields to themselves'], 0, 'The interaction term couples the fermion current to Aμ.', '/qed.html', 'Quantum Electrodynamics'),
    makeQuestion('Why is a photon mass term absent in QED?', ['It would violate electromagnetic gauge symmetry', 'Photons have spin zero', 'The field strength is zero', 'Electrons are neutral'], 0, 'A direct photon mass term is not invariant under the QED gauge transformation.', '/qed.html', 'Quantum Electrodynamics'),
  ],
  'From Lagrangian to Experiment': [
    makeQuestion('What are initial and final states used for?', ['Specifying a transition or scattering process', 'Defining a gauge group', 'Choosing a field value', 'Setting a particle’s spin only'], 0, 'An amplitude connects a specified initial state to a specified final state.', '/lagrangian-to-experiment.html', 'From Lagrangian to Experiment'),
    makeQuestion('What does squaring an amplitude help produce?', ['A transition probability or rate', 'A Lagrangian symmetry', 'A field operator', 'A coordinate transformation'], 0, 'Probabilities and rates depend on the squared magnitude of the amplitude.', '/lagrangian-to-experiment.html', 'From Lagrangian to Experiment'),
    makeQuestion('What is phase space?', ['The space of allowed final-state kinematics', 'The space of gauge choices only', 'A field’s internal plane', 'A vacuum state'], 0, 'Phase-space integration sums over allowed final momenta and their kinematic measure.', '/lagrangian-to-experiment.html', 'From Lagrangian to Experiment'),
    makeQuestion('What does a cross section measure?', ['The likelihood of a scattering process per incident flux', 'A particle’s rest energy', 'A field’s value', 'The number of gauge parameters'], 0, 'A cross section converts a scattering probability into an experimentally useful rate per flux.', '/lagrangian-to-experiment.html', 'From Lagrangian to Experiment'),
    makeQuestion('What does a decay rate measure?', ['How quickly an unstable state decays', 'The size of a field configuration', 'A particle’s wavelength only', 'A gauge transformation'], 0, 'The decay rate is the probability per unit time for an unstable state to decay.', '/lagrangian-to-experiment.html', 'From Lagrangian to Experiment'),
    makeQuestion('Why are identical-particle final states special?', ['Their amplitudes require appropriate exchange symmetrization', 'They have no phase space', 'They cannot interact', 'They are always classical'], 0, 'Quantum amplitudes must respect the statistics of identical bosons or fermions.', '/lagrangian-to-experiment.html', 'From Lagrangian to Experiment'),
  ],
  'Perturbation Theory': [
    makeQuestion('What is the interaction picture useful for?', ['Separating free evolution from interactions', 'Removing all operators', 'Making particles classical', 'Changing the metric'], 0, 'Perturbation theory treats the interaction as an expansion around solvable free evolution.', '/perturbation-theory.html', 'Perturbation Theory'),
    makeQuestion('What is a small coupling used for?', ['Organizing an approximation series', 'Defining a new field type', 'Removing conservation laws', 'Making every diagram exact'], 0, 'When the coupling is suitably small, successive orders can approximate the full result.', '/perturbation-theory.html', 'Perturbation Theory'),
    makeQuestion('What does the Dyson series expand?', ['The time-evolution or S operator', 'The spacetime metric', 'The vacuum circle', 'The number of dimensions'], 0, 'The Dyson expansion orders interaction insertions in time.', '/perturbation-theory.html', 'Perturbation Theory'),
    makeQuestion('What is a tree-level diagram?', ['A diagram with no closed loops', 'A diagram with no vertices', 'A classical tree', 'A gauge choice'], 0, 'Tree diagrams are the leading diagrams without loop integrations.', '/perturbation-theory.html', 'Perturbation Theory'),
    makeQuestion('What do loop diagrams contribute?', ['Quantum corrections', 'Only classical trajectories', 'New coordinates', 'The vacuum’s electric charge'], 0, 'Loops encode virtual quantum effects beyond the tree approximation.', '/perturbation-theory.html', 'Perturbation Theory'),
    makeQuestion('Why can perturbation theory fail?', ['The coupling may not be small or the series may not converge usefully', 'Fields stop existing', 'Energy becomes imaginary always', 'All symmetries disappear'], 0, 'Perturbative results rely on an expansion that is useful only in an appropriate regime.', '/perturbation-theory.html', 'Perturbation Theory'),
  ],
  'Feynman Rules for QED': [
    makeQuestion('What does an external line represent?', ['A specified incoming or outgoing particle state', 'An internal momentum integral only', 'A gauge choice', 'A vacuum minimum'], 0, 'External legs connect the diagram to the initial and final particle states.', '/feynman-rules.html', 'Feynman Rules for QED'),
    makeQuestion('What does a fermion propagator connect?', ['Fermion fields between interaction points', 'Two gauge choices', 'Two vacua', 'Only external detectors'], 0, 'A propagator describes the free field’s contribution between vertices.', '/feynman-rules.html', 'Feynman Rules for QED'),
    makeQuestion('What is momentum conservation at a vertex?', ['The momenta entering equal the momenta leaving', 'All particles have zero momentum', 'Only photons conserve momentum', 'Momentum is not integrated'], 0, 'Translation symmetry gives a momentum-conserving delta function at each vertex.', '/feynman-rules.html', 'Feynman Rules for QED'),
    makeQuestion('What does a closed fermion loop require?', ['A trace over spinor indices and a loop momentum integral', 'No signs', 'A classical source', 'A Higgs vacuum'], 0, 'Closed fermion lines produce traces and an additional minus sign from fermion statistics.', '/feynman-rules.html', 'Feynman Rules for QED'),
    makeQuestion('Why sum multiple Feynman diagrams?', ['They are different contributions to the same amplitude', 'Only one can ever be physical', 'They define different universes', 'They are alternative gauges only'], 0, 'Quantum amplitudes add before taking their squared magnitude.', '/feynman-rules.html', 'Feynman Rules for QED'),
    makeQuestion('What does a photon propagator describe?', ['The free propagation of the gauge field between vertices', 'The electron mass', 'A vacuum expectation value', 'A particle detector'], 0, 'The photon propagator is the internal-line factor for the electromagnetic field.', '/feynman-rules.html', 'Feynman Rules for QED'),
  ],
  'Weak Interaction': [
    makeQuestion('What does beta decay change at quark level?', ['A down quark into an up quark', 'An electron into a photon', 'A gluon into a quark', 'A neutrino into a proton'], 0, 'At quark level, d → u through charged-current weak interaction.', '/weak-interaction.html', 'Weak Interaction'),
    makeQuestion('What does parity reverse?', ['Spatial coordinates and momentum direction', 'Time only', 'Electric charge only', 'Particle number only'], 0, 'Parity maps x to −x and reverses polar vectors such as momentum.', '/weak-interaction.html', 'Weak Interaction'),
    makeQuestion('What did the Wu experiment demonstrate?', ['Parity violation in beta decay', 'Photon mass', 'Color confinement', 'Higgs production'], 0, 'The observed angular asymmetry in polarized beta decay showed that the weak interaction violates parity.', '/weak-interaction.html', 'Weak Interaction'),
    makeQuestion('What is a charged current?', ['A current coupled to W⁺ or W⁻ exchange', 'A current of electric charge only', 'A photon field strength', 'A scalar potential'], 0, 'Charged weak currents change fermion species through charged W bosons.', '/weak-interaction.html', 'Weak Interaction'),
    makeQuestion('What accompanies an electron in neutron beta decay?', ['An electron antineutrino', 'A photon necessarily', 'A gluon', 'A muon neutrino necessarily'], 0, 'The decay n → p + e⁻ + ν̄ₑ includes an electron antineutrino.', '/weak-interaction.html', 'Weak Interaction'),
    makeQuestion('Why are neutrinos difficult to detect?', ['They have no electric charge and interact weakly', 'They are always massive and slow', 'They carry color', 'They cannot carry energy'], 0, 'Neutrinos lack electromagnetic interactions and have only weak interactions in this framework.', '/weak-interaction.html', 'Weak Interaction'),
  ],
  'Electroweak Unification': [
    makeQuestion('What does weak isospin label?', ['The SU(2)L representation of a field', 'Spatial spin only', 'Electric field strength', 'A particle’s position'], 0, 'Weak isospin is an internal quantum number associated with SU(2)L.', '/electroweak-unification.html', 'Electroweak Unification'),
    makeQuestion('What does hypercharge contribute to?', ['Electric charge together with T³', 'Only spin', 'Only color', 'The Higgs mass alone'], 0, 'The charge relation is Q = T³ + Y/2 in the conventions used here.', '/electroweak-unification.html', 'Electroweak Unification'),
    makeQuestion('How many SU(2) gauge fields are there?', ['Three', 'One', 'Two', 'Eight'], 0, 'SU(2) has three generators and therefore three gauge fields W¹, W², and W³.', '/electroweak-unification.html', 'Electroweak Unification'),
    makeQuestion('What are W⁺ and W⁻ combinations of?', ['W¹ and W²', 'W³ and B', 'The photon and gluon', 'Two Higgs fields'], 0, 'The charged fields are W± = (W¹ ∓ iW²)/√2.', '/electroweak-unification.html', 'Electroweak Unification'),
    makeQuestion('What does the Weinberg angle describe?', ['Neutral gauge-field mixing', 'Fermion spin', 'QCD confinement', 'The Higgs self-coupling only'], 0, 'The weak mixing angle relates the W³ and B fields to A and Z.', '/electroweak-unification.html', 'Electroweak Unification'),
    makeQuestion('Which gauge bosons are electrically charged?', ['W⁺ and W⁻', 'The photon and Z', 'The gluons only', 'The Higgs components after gauge fixing'], 0, 'The W± fields carry electric charge, while A and Z are neutral.', '/electroweak-unification.html', 'Electroweak Unification'),
  ],
  'Higgs Mechanism': [
    makeQuestion('What is the Higgs field in the Standard Model?', ['An SU(2)L scalar doublet', 'A color octet', 'A spacetime vector', 'A fermion singlet only'], 0, 'The Higgs field is a complex scalar doublet with four real degrees of freedom.', '/higgs-mechanism.html', 'Higgs Mechanism'),
    makeQuestion('Why is the lower Higgs component chosen for the vacuum?', ['It is electrically neutral for Y = 1', 'It carries color', 'It is the heaviest component', 'It has spin one'], 0, 'The lower component has T³ = −1/2, so Q = T³ + Y/2 = 0.', '/higgs-mechanism.html', 'Higgs Mechanism'),
    makeQuestion('What is the Higgs boson in unitary gauge?', ['The remaining radial scalar fluctuation h', 'The photon', 'The Goldstone phase', 'The Z field'], 0, 'After three Goldstone modes are absorbed, the radial fluctuation remains physical.', '/higgs-mechanism.html', 'Higgs Mechanism'),
    makeQuestion('What does the Higgs potential’s λ control?', ['The Higgs self-interaction and mass relation', 'The photon charge', 'The number of colors', 'The spacetime metric'], 0, 'At tree level, mh² = 2λv² in the potential used here.', '/higgs-mechanism.html', 'Higgs Mechanism'),
    makeQuestion('What is the electron mass in this construction?', ['me = yev/√2', 'me = gv/2', 'me = 0 always', 'me = λv²'], 0, 'The electron Yukawa interaction gives me = yev/√2.', '/higgs-mechanism.html', 'Higgs Mechanism'),
    makeQuestion('What remains unbroken in the Standard Model Higgs vacuum?', ['Electromagnetic U(1)', 'All of SU(2)L', 'Color SU(3) only as a new symmetry', 'No symmetry'], 0, 'The neutral Higgs vacuum is preserved by electric charge, leaving electromagnetism unbroken.', '/higgs-mechanism.html', 'Higgs Mechanism'),
  ],
  'Quantum Chromodynamics': [
    makeQuestion('What is color in QCD?', ['An internal SU(3) charge', 'A visual wavelength', 'A spin direction', 'A spacetime coordinate'], 0, 'Color is the internal charge associated with the SU(3)C gauge symmetry.', '/qcd.html', 'Quantum Chromodynamics'),
    makeQuestion('How many color states does a quark have?', ['Three', 'One', 'Two', 'Eight'], 0, 'Quarks transform in the three-dimensional fundamental representation of SU(3).', '/qcd.html', 'Quantum Chromodynamics'),
    makeQuestion('What particles mediate the strong interaction?', ['Gluons', 'Photons', 'W bosons', 'Higgs bosons'], 0, 'Gluons are the gauge bosons of SU(3)C.', '/qcd.html', 'Quantum Chromodynamics'),
    makeQuestion('Why do gluons self-interact?', ['They carry color charge', 'They are scalars', 'They are electrically charged', 'They have no gauge group'], 0, 'The non-Abelian SU(3) gauge fields carry the charge they mediate.', '/qcd.html', 'Quantum Chromodynamics'),
    makeQuestion('What is asymptotic freedom?', ['The strong coupling becomes weaker at high energy', 'Quarks move freely at all distances', 'Gluons become massive from the Higgs', 'Color disappears from the Lagrangian'], 0, 'QCD becomes perturbatively weaker at short distances or high energies.', '/qcd.html', 'Quantum Chromodynamics'),
    makeQuestion('What are hadrons?', ['Color-neutral bound states of quarks and gluons', 'Free gluons only', 'Gauge choices', 'Scalar field modes'], 0, 'Observed hadrons are composite color-neutral states such as baryons and mesons.', '/qcd.html', 'Quantum Chromodynamics'),
  ],
  'The Standard Model': [
    makeQuestion('What are the Standard Model gauge groups?', ['SU(3)C × SU(2)L × U(1)Y', 'SO(3) × U(1) only', 'SU(5) only', 'U(1)EM alone'], 0, 'The Standard Model has color, weak-isospin, and hypercharge gauge symmetries.', '/standard-model.html', 'The Standard Model'),
    makeQuestion('What are leptons?', ['Fermions that do not carry color charge', 'The gauge bosons of QCD', 'Scalar particles only', 'Composite gluons'], 0, 'Leptons participate in electroweak interactions but are not colored.', '/standard-model.html', 'The Standard Model'),
    makeQuestion('What are quarks?', ['Colored spin-½ matter fields', 'Massless gauge fields only', 'Higgs excitations only', 'Classical waves'], 0, 'Quarks are fermions carrying color and electroweak quantum numbers.', '/standard-model.html', 'The Standard Model'),
    makeQuestion('What does the Higgs field add to the Standard Model?', ['A scalar sector that generates masses after symmetry breaking', 'A quantum theory of gravity', 'A fifth force necessarily', 'Only a new color charge'], 0, 'The Higgs sector supplies the vacuum value and mass-generating interactions.', '/standard-model.html', 'The Standard Model'),
    makeQuestion('What is a generation of matter?', ['A repeated family of quarks and leptons', 'A gauge transformation', 'A gluon polarization', 'A vacuum minimum'], 0, 'The Standard Model contains three generations with analogous gauge assignments.', '/standard-model.html', 'The Standard Model'),
    makeQuestion('What remains an open problem outside the Standard Model?', ['A complete quantum theory of gravity', 'The existence of photons', 'The QED gauge symmetry', 'The use of fermions'], 0, 'Gravity is not incorporated into the Standard Model as a quantum gauge theory.', '/standard-model.html', 'The Standard Model'),
  ],
  'Path Integrals in Quantum Mechanics': [
    makeQuestion('What is each path’s contribution weighted by?', ['A phase involving the action', 'Its electric charge only', 'Its final position only', 'A fixed probability with no phase'], 0, 'A history contributes with a factor proportional to exp(iS/ℏ).', '/path-integrals.html', 'Path Integrals in Quantum Mechanics'),
    makeQuestion('What happens near the classical path?', ['Phases tend to reinforce by stationary action', 'All paths vanish exactly', 'The action becomes undefined', 'Particles stop moving'], 0, 'Nearby paths can interfere constructively where the action is stationary.', '/path-integrals.html', 'Path Integrals in Quantum Mechanics'),
    makeQuestion('What does a propagator represent?', ['The amplitude for propagation between events', 'A particle’s classical speed', 'A gauge charge', 'A vacuum expectation only'], 0, 'A propagator is a transition amplitude or Green function for a field or particle.', '/path-integrals.html', 'Path Integrals in Quantum Mechanics'),
    makeQuestion('What is the role of boundary conditions?', ['They specify the initial and final data being connected', 'They remove all paths', 'They set every mass to zero', 'They define color'], 0, 'The path integral sums histories satisfying the chosen endpoint conditions.', '/path-integrals.html', 'Path Integrals in Quantum Mechanics'),
    makeQuestion('Why are amplitudes complex?', ['Their phases allow interference', 'Energy is imaginary', 'Coordinates are complex necessarily', 'Particles have no probabilities'], 0, 'Complex phases are essential for constructive and destructive interference.', '/path-integrals.html', 'Path Integrals in Quantum Mechanics'),
    makeQuestion('What is the classical limit associated with?', ['Rapid phase cancellation away from stationary action', 'The disappearance of all fields', 'Infinite particle number', 'A broken gauge group'], 0, 'For small ℏ, nonstationary paths tend to cancel, leaving stationary-action paths dominant.', '/path-integrals.html', 'Path Integrals in Quantum Mechanics'),
  ],
  'Path Integrals for Fields': [
    makeQuestion('What replaces a particle path in a field path integral?', ['A spacetime field history', 'A single momentum vector', 'A gauge parameter only', 'A detector track'], 0, 'The integral sums over complete field configurations through spacetime.', '/path-integrals-fields.html', 'Path Integrals for Fields'),
    makeQuestion('What is a source J used for?', ['Generating field correlation functions', 'Giving every particle mass', 'Fixing spatial coordinates', 'Removing interactions'], 0, 'Coupling a source to a field lets functional derivatives generate correlators.', '/path-integrals-fields.html', 'Path Integrals for Fields'),
    makeQuestion('What is a correlation function?', ['An expectation value of products of fields', 'A particle’s electric charge', 'A gauge transformation', 'A classical orbit only'], 0, 'Correlation functions measure how field operators at different points are related.', '/path-integrals-fields.html', 'Path Integrals for Fields'),
    makeQuestion('What does the free-field path integral produce?', ['A Gaussian functional integral', 'Only nonlinear equations', 'A finite number of paths', 'A broken symmetry automatically'], 0, 'Quadratic actions lead to Gaussian integrals and calculable propagators.', '/path-integrals-fields.html', 'Path Integrals for Fields'),
    makeQuestion('What does the effective action summarize?', ['Quantum effects as a functional of background fields', 'Only classical particle positions', 'A gauge group’s generators', 'The number of dimensions'], 0, 'The effective action packages quantum corrections into an action-like functional.', '/path-integrals-fields.html', 'Path Integrals for Fields'),
    makeQuestion('What does functional differentiation with respect to J do?', ['It inserts field factors into correlators', 'It removes the source permanently', 'It changes spin', 'It fixes the vacuum phase'], 0, 'Differentiating the generating functional with respect to J brings down fields.', '/path-integrals-fields.html', 'Path Integrals for Fields'),
  ],
  'Fermionic Path Integrals': [
    makeQuestion('What is the Grassmann rule for two variables?', ['η₁η₂ = −η₂η₁', 'η₁η₂ = η₂η₁ always', 'η₁η₂ = 1', 'η₁η₂ is a vector'], 0, 'Grassmann variables anticommute, so exchanging them introduces a minus sign.', '/path-integrals-fermions.html', 'Fermionic Path Integrals'),
    makeQuestion('What is η² for a Grassmann variable?', ['Zero', 'One', 'Its mass', 'A gauge field'], 0, 'Anticommutation implies ηη = −ηη, hence η² = 0.', '/path-integrals-fermions.html', 'Fermionic Path Integrals'),
    makeQuestion('What replaces an ordinary determinant for fermionic integration?', ['A determinant structure with Grassmann-specific signs', 'A classical action only', 'A spatial Fourier series', 'A photon polarization'], 0, 'Grassmann Gaussian integrals generate determinants and signs appropriate to fermions.', '/path-integrals-fermions.html', 'Fermionic Path Integrals'),
    makeQuestion('What do fermion fields anticommute under exchange?', ['Their operator or path-integral variables', 'Only their masses', 'Spacetime coordinates', 'Gauge potentials'], 0, 'Anticommutation encodes the exchange statistics of fermions.', '/path-integrals-fermions.html', 'Fermionic Path Integrals'),
    makeQuestion('What is a fermionic bilinear?', ['A product such as ψ̄ψ or ψ̄γμψ', 'A scalar potential only', 'Two commuting coordinates', 'A field-strength tensor only'], 0, 'Bilinears combine fermion fields into Lorentz-covariant quantities.', '/path-integrals-fermions.html', 'Fermionic Path Integrals'),
    makeQuestion('Why do closed fermion loops have a minus sign?', ['Because of fermion anticommutation', 'Because fermions are massless', 'Because loops are classical', 'Because photons carry color'], 0, 'Reordering anticommuting fermion variables around a closed loop produces a minus sign.', '/path-integrals-fermions.html', 'Fermionic Path Integrals'),
  ],
  'Gauge Fixing': [
    makeQuestion('What is a gauge orbit?', ['The set of gauge-related descriptions of one physical configuration', 'A particle trajectory', 'A field’s energy spectrum', 'A loop integral'], 0, 'Gauge transformations move along redundant descriptions of the same physics.', '/path-integrals-gauge-fixing.html', 'Gauge Fixing'),
    makeQuestion('What does a gauge condition select?', ['One representative from each set of redundant descriptions', 'A new particle species', 'A unique classical force', 'Only the vacuum state'], 0, 'Gauge fixing chooses a calculational representative without changing observables.', '/path-integrals-gauge-fixing.html', 'Gauge Fixing'),
    makeQuestion('What is the Lorenz gauge condition?', ['∂μAμ = 0', 'AμAμ = 0 always', 'Fμν = 0', '∂μφ = 0 for every field'], 0, 'The Lorenz gauge imposes a divergence condition on the electromagnetic potential.', '/path-integrals-gauge-fixing.html', 'Gauge Fixing'),
    makeQuestion('What does gauge fixing prevent in a path integral?', ['Overcounting equivalent gauge configurations', 'All quantum interference', 'Fermion creation', 'Mass generation'], 0, 'Without gauge fixing, the integral would integrate repeatedly over the same physical configurations.', '/path-integrals-gauge-fixing.html', 'Gauge Fixing'),
    makeQuestion('Are gauge-dependent potentials directly observable?', ['No; gauge-invariant quantities are physical', 'Yes, every component separately', 'Only the time component', 'Only in classical mechanics'], 0, 'Observables must be invariant under the gauge redundancy.', '/path-integrals-gauge-fixing.html', 'Gauge Fixing'),
    makeQuestion('What is Fμν physically associated with?', ['The electromagnetic fields and gauge-invariant field strength', 'A gauge choice only', 'A scalar vacuum value', 'A fermion occupation number'], 0, 'The field strength is unchanged by adding a gradient to Aμ.', '/path-integrals-gauge-fixing.html', 'Gauge Fixing'),
  ],
  'Renormalization at One Loop': [
    makeQuestion('What is an ultraviolet divergence?', ['A contribution that grows without bound at high momentum', 'A low-energy particle', 'A gauge rotation', 'A finite classical force'], 0, 'Loop integrals can diverge from contributions at arbitrarily large momentum.', '/path-integrals-renormalization.html', 'Renormalization at One Loop'),
    makeQuestion('What is a regulator?', ['A temporary device for controlling a divergence', 'A new physical particle always', 'A gauge generator', 'A vacuum orientation'], 0, 'A regulator makes intermediate expressions well-defined before renormalization.', '/path-integrals-renormalization.html', 'Renormalization at One Loop'),
    makeQuestion('What is a counterterm?', ['A parameter term introduced to absorb a divergence', 'A detector correction only', 'A new spacetime dimension', 'A conserved current'], 0, 'Counterterms redefine bare parameters so predictions can be expressed in measured ones.', '/path-integrals-renormalization.html', 'Renormalization at One Loop'),
    makeQuestion('What does a renormalized parameter represent?', ['A finite parameter tied to a measurement scheme', 'An unobservable infinite number only', 'A gauge redundancy', 'A classical path'], 0, 'Renormalized masses and couplings are defined through finite physical or scheme-dependent conditions.', '/path-integrals-renormalization.html', 'Renormalization at One Loop'),
    makeQuestion('What is a self-energy correction?', ['A loop correction to a propagating particle or field', 'A vacuum rotation', 'A spatial derivative only', 'A new particle count'], 0, 'Self-energy diagrams modify the two-point function and can shift masses.', '/path-integrals-renormalization.html', 'Renormalization at One Loop'),
    makeQuestion('What does the renormalization scale describe?', ['The scale at which parameters are defined', 'A particle’s position', 'The number of polarizations', 'A gauge orbit'], 0, 'Renormalized couplings can depend on the scale used to define them.', '/path-integrals-renormalization.html', 'Renormalization at One Loop'),
  ],
  'Final Recap': [
    makeQuestion('What is the role of symmetry in a field theory?', ['It constrains allowed terms and relates physical quantities', 'It removes all interactions', 'It fixes every numerical parameter', 'It makes fields classical'], 0, 'Symmetries organize the Lagrangian and imply important conservation laws and relations.', '/recap.html', 'Final Recap'),
    makeQuestion('What is the relationship between a field and its quanta?', ['Quanta are excitations of the field', 'They are unrelated objects', 'The field is always one particle', 'A particle is a gauge choice'], 0, 'Quantization turns field modes into excitations interpreted as particles.', '/recap.html', 'Final Recap'),
    makeQuestion('What does a gauge field do?', ['Mediates a gauge interaction and compensates local symmetry changes', 'It always has mass', 'It is a scalar only', 'It removes conservation laws'], 0, 'Gauge fields enforce local symmetry and carry the associated interactions.', '/recap.html', 'Final Recap'),
    makeQuestion('What does spontaneous symmetry breaking require?', ['A symmetric theory with a less-symmetric chosen ground state', 'An explicitly asymmetric Lagrangian only', 'No vacuum', 'A classical particle trajectory'], 0, 'The laws retain the symmetry while the selected vacuum does not.', '/recap.html', 'Final Recap'),
    makeQuestion('What do Feynman diagrams organize?', ['Terms in a perturbative amplitude', 'Exact particle trajectories', 'Gauge orbits only', 'Classical field configurations only'], 0, 'Diagrams are a bookkeeping language for perturbative contributions to amplitudes.', '/recap.html', 'Final Recap'),
    makeQuestion('What is the final goal of a quantum field theory calculation?', ['A comparison with observable predictions', 'A list of all coordinates', 'A choice of notation only', 'A field with no interactions'], 0, 'The theory connects fields and a Lagrangian to measurable rates and cross sections.', '/recap.html', 'Final Recap'),
  ],
}

const completeChapterQuizzes = chapterQuizzes.map(([title, link, questions]) => ({
  title,
  link,
  questions: [...questions, ...extraByChapter[title]],
}))

const quizSets = [
  { title: 'Mixed review', link: '/', questions: overviewQuestions.slice(0, 8) },
  ...completeChapterQuizzes,
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
