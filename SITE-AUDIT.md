# Phyz Site Audit

A full read of the 24 markdown pages in `docs/` (plus `.vuepress/config.js`), producing three things:

1. An inventory ("memory") of every topic, term, and equation the site introduces.
2. A list of logic gaps — information the text relies on without explaining, and without flagging that it is omitted.
3. A math-level audit against the stated target ("math at the high school level").

Page order follows the reading order in `.vuepress/config.js`. Line references are `file:line`.

---

## 1. Summary of findings

The site is a coherent, carefully cross-linked path from Newton's laws to QED, with optional path-integral pages and several planned-but-empty chapters. The prose is unusually good at glossing terms of art at first use (e.g. "matrix element" is now defined at `qft.md:38`, "on shell" at `field-quantization.md:307`).

Three structural problems stand out:

1. **The math target is not met, and cannot be met as the site stands.** The site teaches from the top down: it *uses* calculus, linear algebra, complex analysis, tensor calculus, and group theory as prerequisites from the very first pages, and never teaches them. "High school level" is not just exceeded; the foundational prerequisites are never even acknowledged as prerequisites. See §4.

2. **A handful of load-bearing steps are asserted without proof and without a "given without proof" flag.** The most serious are Noether's theorem (invoked to get charge conservation), the phase-space measure (never given a formula, so a cross section cannot actually be computed), and the g=2/Pauli-equation limit. See §5.

3. **The site stops short of a completed calculation.** The reader reaches the Feynman rules for Compton scattering but never assembles a numeric cross section, because the spin/polarization sums and the phase-space measure are never supplied. See §5.

Notation and terminology are largely consistent (with one known exception: "branch" vs "term" for the two dispersion sheets — see `memory/phyz-terminology.md`).

---

## 2. Inventory: topics, terms, equations by page

### 2.1 Classical Mechanics (`classical-mechanics.md`, 65 lines)

Topics: Newton's second law; constrained motion; generalized coordinates; Lagrangian; action; stationary action; Euler–Lagrange equation; conjugate momentum; Hamiltonian; Hamilton's equations; phase space; Poisson bracket; canonical quantization (preview).

Key equations:
- Action: $S = \int L(q,\dot q,t)\,dt$
- Euler–Lagrange: $\frac{d}{dt}\frac{\partial L}{\partial \dot q} - \frac{\partial L}{\partial q} = 0$
- Hamilton's equations: $\dot q = \partial H/\partial p$, $\dot p = -\partial H/\partial q$
- Poisson bracket: $\{f,g\} = \frac{\partial f}{\partial q}\frac{\partial g}{\partial p} - \frac{\partial f}{\partial p}\frac{\partial g}{\partial q}$

Terms introduced: generalized coordinates, action, stationary action, Euler–Lagrange equation, conjugate momentum, Legendre transform (named only), Hamilton equations, phase space, Poisson bracket, bilinear, antisymmetric, Jacobi identity (named only).

### 2.2 First Quantization (`first-quantization.md`, 136 lines)

Topics: Hilbert space; first quantization; Schrödinger equation; wave function and Born rule; Copenhagen interpretation; operators; observables; eigenvectors/eigenvalues; commutators; superposition; uncertainty principle.

Key equations:
- Schrödinger: $i\hbar\,\partial\Psi/\partial t = [-\frac{\hbar^2}{2m}\partial_x^2 + V]\Psi$
- Canonical commutator: $[\hat x,\hat p] = i\hbar$
- Uncertainty: $\Delta x\,\Delta p \ge \hbar/2$
- General: $\Delta A\,\Delta B \ge \tfrac12|\langle[\hat A,\hat B]\rangle|$

Terms introduced: Hilbert space, first quantization, Schrödinger equation, wave function, Born rule, Copenhagen interpretation, collapse, complementarity, operator, linear, observable, Hermitian, unitary (footnote), eigenstate/eigenvalue, commutator, superposition, uncertainty relation, expectation value, hidden variables, Bell's inequality (footnote), position/momentum representation (footnote).

### 2.3 Harmonic Oscillator (`harmonic-oscillator.md`, 103 lines)

Topics: quadratic approximation near equilibrium; classical oscillator; quantization; ladder operators; number operator; energy spectrum; zero-point energy.

Key equations:
- $H = \frac{p^2}{2m} + \tfrac12 m\omega^2 x^2$
- Ladder: $\hat a = \sqrt{\frac{m\omega}{2\hbar}}\hat x + \frac{i}{\sqrt{2m\hbar\omega}}\hat p$
- $[\hat a,\hat a^\dagger]=1$
- $\hat H = \hbar\omega(\hat a^\dagger\hat a + \tfrac12)$
- $E_n = \hbar\omega(n+\tfrac12)$
- $\hat a|n\rangle = \sqrt n\,|n{-}1\rangle$, $\hat a^\dagger|n\rangle = \sqrt{n{+}1}\,|n{+}1\rangle$

Terms introduced: harmonic oscillator, restoring force, angular frequency, ladder operators (creation/annihilation), number operator, quantum, zero-point energy, ground state, vacuum (preview).

### 2.4 Special Relativity (`special-relativity.md`, 187 lines)

Topics: postulates; inertial frame; Galilean vs Lorentz transformation; simultaneity; spacetime interval; four-vectors; metric; covariant/contravariant indices; tensors; energy–momentum relation; Maxwell equations in tensor form; Schrödinger non-invariance.

Key equations:
- Lorentz transform (boost along $x$), Lorentz factor $\gamma=1/\sqrt{1-v^2/c^2}$
- Velocity addition: $u' = \frac{u-v}{1-uv/c^2}$
- Interval: $s^2 = c^2\Delta t^2 - \Delta x^2 - \Delta y^2 - \Delta z^2$
- Metric: $\eta_{\mu\nu}=\mathrm{diag}(+1,-1,-1,-1)$
- Four-momentum: $p^\mu = (E/c, \mathbf p)$
- Energy–momentum: $E^2 = (mc^2)^2 + (pc)^2$
- Maxwell: $\partial_\mu F^{\mu\nu}=J^\nu$; $F^{\mu\nu}=\partial^\mu A^\nu-\partial^\nu A^\mu$

Terms introduced: inertial frame, principle of relativity, invariance of light speed, Lorentz factor, simultaneity, spacetime interval (timelike/lightlike/spacelike), four-vector, Minkowski metric, Lorentz scalar, proper time, four-velocity, four-momentum, covariant/contravariant, Einstein summation, tensor, contraction, d'Alembertian, four-current, field tensor, dispersion relation.

### 2.5 Relativistic QM (`relativistic-qm.md`, 225 lines)

Topics: plane waves; separation of variables; Klein–Gordon equation; negative energies; probability/current; Dirac equation construction.

Key equations:
- Plane wave $\psi = e^{i(\mathbf p\cdot\mathbf x - Et)/\hbar}$
- Klein–Gordon: $(\Box + m^2/\hbar^2)\psi = 0$, $E^2=\mathbf p^2+m^2$
- Klein–Gordon current: $j^\mu = i(\psi^*\partial^\mu\psi - \psi\,\partial^\mu\psi^*)$
- Dirac: $i\hbar\partial_t\psi = (-i\hbar\boldsymbol\alpha\cdot\nabla + \beta m)\psi$
- Covariant: $(i\hbar\gamma^\mu\partial_\mu - m)\psi = 0$

Terms introduced: plane wave, time-independent Schrödinger equation, Klein–Gordon equation, negative energy, antiparticle, Stückelberg–Feynman interpretation, continuity equation, Klein–Gordon current, second quantization (named), Dirac equation, anticommutation relations, spinor, small components, Dirac adjoint.

### 2.6 Dirac Equation (`dirac-equation.md`, 371 lines)

Topics: spin from orbital+intrinsic angular momentum; Heisenberg equation; antiparticles; rest and moving solutions; charge conjugation; spinor Lorentz transformations (incl. two detailed derivations); general solution.

Key equations:
- $\mathbf J = \mathbf L + \mathbf S$
- Heisenberg: $d\mathbf A/dt = \frac{i}{\hbar}[H,\mathbf A]$
- $\mathbf S = \frac{\hbar}{2}\boldsymbol\Sigma$
- $[S_i,S_j]=i\hbar\varepsilon_{ijk}S_k$
- $u_s(p)$, $v_s(p)$ spinors
- $\psi_c = \eta\psi^*$, $\eta=i\gamma^2$
- $S(\Lambda)=\exp(-\frac{i}{4}\omega_{\mu\nu}\sigma^{\mu\nu})$, $\sigma^{\mu\nu}=\frac{i}{2}[\gamma^\mu,\gamma^\nu]$
- Rotation: $S=\exp(-\frac{i}{2}\boldsymbol\theta\cdot\boldsymbol\Sigma)$; boost: $S=\exp(-\frac{\varphi}{2}\alpha^1)$, rapidity $v=\tanh\varphi$
- General solution expansion with $a_s(p)$, $b_s^*(p)$

Terms introduced: spin, orbital vs intrinsic angular momentum, gyromagnetic factor, minimal substitution, Heisenberg equation, hole theory, spinor, double-valued (2π vs 4π), Weyl spinor, chiral basis, rapidity, generators, charge conjugation, antiparticle, positron.

### 2.7 QFT — Fields and Quanta (`qft.md`, 176 lines)

Topics: promotion of amplitudes to operators; electron field operator; field classification (scalar/vector/spinor); second quantization; Schrödinger vs Heisenberg picture; state vs field; building one-particle states; spin–statistics preview.

Key equations:
- $\hat\psi(x) = \sum_s\int\frac{d^3p}{(2\pi\hbar)^3}\frac{1}{\sqrt{2E_p}}[\hat a_s u_s e^{-ip\cdot x/\hbar} + \hat b_s^\dagger v_s e^{+ip\cdot x/\hbar}]$
- Free equations restated (Klein–Gordon, Dirac, Maxwell)
- Heisenberg field: $\hat\phi(t,\mathbf x)=e^{i\hat Ht/\hbar}\hat\phi(0,\mathbf x)e^{-i\hat Ht/\hbar}$

Terms introduced: field operator, positive/negative frequency, matrix element, promotion, vacuum, adjoint, scalar/vector/spinor field, second quantization, operator-valued distribution, Schrödinger/Heisenberg picture, wave functional, spin–statistics.

### 2.8 QFT — Action and Lagrangians (`qft-action.md`, 265 lines)

Topics: principle of least action (recap); from particles to fields; Lagrangian density; Euler–Lagrange for fields; Hamiltonian and state space; functional derivative; Noether (named); Klein–Gordon/Maxwell/Dirac Lagrangians.

Key equations:
- $S[\phi]=\int d^4x\,\mathcal L(\phi,\partial_\mu\phi)$
- Field E-L: $\partial_\mu\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)} - \frac{\partial\mathcal L}{\partial\phi}=0$
- $\mathcal H = \pi\dot\phi - \mathcal L$
- $\mathcal L_{\mathrm{KG}} = \tfrac12(\partial_\mu\phi)(\partial^\mu\phi) - \frac{m^2}{2\hbar^2}\phi^2$
- $\mathcal L_{\mathrm{Maxwell}} = -\tfrac14 F_{\mu\nu}F^{\mu\nu}$
- $\mathcal L_{\mathrm{Dirac}} = \bar\psi(i\hbar\gamma^\mu\partial_\mu - m)\psi$

Terms introduced: Lagrangian density, functional derivative, conjugate momentum density, Noether's theorem (named), d'Alembertian, Dirac adjoint (invariant pairing), spinor (etymology), unitarity of rotations vs boosts.

### 2.9 QFT — Field Quantization (`field-quantization.md`, 307 lines)

Topics: scalar mode expansion; canonical commutator; ladder commutators; one oscillator per momentum; particle creation; spinor field quantization (anticommutators); Pauli exclusion; antiparticles; propagator (preview).

Key equations:
- $\hat\phi(x) = \int\frac{d^3p}{(2\pi\hbar)^3}\frac{\hbar}{\sqrt{2E_p}}[\hat a(p)e^{-ip\cdot x/\hbar} + \hat a^\dagger(p)e^{+ip\cdot x/\hbar}]$
- $[\hat\phi(t,\mathbf x),\hat\pi(t,\mathbf x')]=i\hbar\,\delta^3(\mathbf x-\mathbf x')$
- $[\hat a(p),\hat a^\dagger(p')]=(2\pi\hbar)^3\delta^3(p-p')$
- $\hat H = \int\frac{d^3p}{(2\pi\hbar)^3}E_p\,\hat a^\dagger\hat a + \text{const}$
- $\{\hat a_s(p),\hat a_{s'}^\dagger(p')\}=(2\pi\hbar)^3\delta_{ss'}\delta^3(p-p')$
- Spinor propagator preview: $i(\not r+m)/(r^2-m^2+i\epsilon)$

Terms introduced: on-shell/mass-shell (footnote), equal-time canonical commutator, Dirac delta function, occupation numbers, bosons, Pauli exclusion, Fermi–Dirac statistics, antiparticles, propagator, Wick contraction (preview).

### 2.10 QED (`qed.md`, 393 lines)

Topics: QED Lagrangian; U(1) global symmetry; local gauge symmetry; covariant derivative; minimal coupling; photon quantization (polarizations, gauge fixing, Gupta–Bleuler); photon propagator.

Key equations:
- $\mathcal L_{\mathrm{QED}} = -\tfrac14 F^{\mu\nu}F_{\mu\nu} + \bar\psi(i\hbar\gamma^\mu D_\mu - m)\psi$, $D_\mu=\partial_\mu+\frac{iq}{\hbar}A_\mu$
- Interaction: $-q\bar\psi\gamma^\mu\psi A_\mu$
- Gauge transform: $A_\mu\to A_\mu-\frac{\hbar}{q}\partial_\mu\alpha$
- Gupta–Bleuler: $(\partial_\mu\hat A^\mu)^{(+)}|\mathrm{phys}\rangle=0$
- Photon propagator (Feynman gauge): $D_{\mu\nu}(k)=\frac{-ig_{\mu\nu}}{k^2+i\epsilon}$

Terms introduced: QED, minimal coupling, global vs local symmetry, U(1), Noether's theorem (invoked), gauge symmetry, covariant derivative, pure gauge, transversality, Lorenz condition, Feynman gauge, Gupta–Bleuler condition, negative norm, photon propagator.

### 2.11 From Lagrangian to Experiment (`lagrangian-to-experiment.md`, 73 lines)

Topics: cross section; decay rate; S-matrix; invariant amplitude; phase-space measure (schematic).

Key equations:
- rate = $\Phi N\sigma$
- $\langle f|S|i\rangle = \langle f|i\rangle + (2\pi)^4\delta^4(P_f-P_i)\,i\mathcal M$
- $\sigma = \frac{1}{\Phi}\int|\mathcal M|^2 d\Pi$

Terms introduced: cross section, flux, barn, decay rate, S-matrix, matrix element, invariant amplitude, phase-space measure.

### 2.12 Perturbation Theory (`perturbation-theory.md`, 173 lines)

Topics: interacting scalar (φ³); Dyson series; time ordering; Wick's theorem; propagator from free field; vertex factor; QED rule dictionary.

Key equations:
- $\mathcal L = \mathcal L_0 - \frac{g}{3!}\phi^3$
- $S = T\exp[i\int d^4x\,\mathcal L_{\mathrm{int}}(x)]$
- Wick: $T[\phi(x)\phi(y)] = :\!\phi(x)\phi(y)\!: + \langle 0|T\phi(x)\phi(y)|0\rangle$
- Propagator: $\frac{i}{p^2-m^2+i\epsilon}$
- Scalar vertex $-ig$

Terms introduced: Dyson series, interaction picture, time ordering, normal ordering, Wick's theorem, contraction, propagator, vertex, external/internal line, symmetry factor (named), on-shell, Mandelstam variables (footnote), LSZ reduction (footnote).

### 2.13 Feynman Rules for QED (`feynman-rules.md`, 284 lines)

Topics: Feynman diagrams; Compton scattering (s- and u-channel); QED Feynman rules; full algebraic derivation; loops; ultraviolet/infrared divergences; renormalization (preview).

Key equations:
- Electron propagator: $\frac{i(\not r+m)}{r^2-m^2+i\epsilon}$
- Vertex: $-iq\gamma^\mu$
- $\mathcal M_s$, $\mathcal M_u$ for Compton
- $|\mathcal M_{\mathrm{tree}}|^2 = |\mathcal M_s|^2+|\mathcal M_u|^2+2\,\mathrm{Re}(\mathcal M_s\mathcal M_u^*)$
- Loop integral $\int\frac{d^4\ell}{(2\pi)^4}$

Terms introduced: Feynman diagram, s-/u-channel, fermion/photon line, vertex, external/internal line, virtual particle, off-shell, Feynman slash notation $\not r$, Mandelstam variables, interference, tree/loop diagram, ultraviolet/infrared divergence, regulator, dimensional regularization, counterterm, renormalization, helicity (footnote).

### 2.14 Weak Interaction (`weak-interaction.md`, 451 lines)

Topics: beta decay; neutrinos; nucleons/leptons/quarks; parity violation; γ⁵ and chiral projectors; helicity vs chirality; SU(2) global/local symmetry; Yang–Mills field strength and self-interactions; charged current; CKM mixing; low-energy (Fermi) limit.

Key equations:
- $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3$, $P_L=\frac{1-\gamma^5}{2}$
- $D_\mu=\partial_\mu+igW_\mu$, $W_\mu=W_\mu^a T^a$
- $W_{\mu\nu}^a = \partial_\mu W_\nu^a - \partial_\nu W_\mu^a - g\epsilon^{abc}W_\mu^b W_\nu^c$
- $\mathcal L_{\mathrm{YM}}=-\tfrac14 W_{\mu\nu}^a W^{a\mu\nu}$
- $W^\pm_\mu = \frac{W^1_\mu \mp iW^2_\mu}{\sqrt 2}$
- $\mathcal L_{\mathrm{CC}} = -\frac{g}{\sqrt2}(\bar\nu_{eL}\gamma^\mu e_L W_\mu^+ + \bar e_L\gamma^\mu\nu_{eL}W_\mu^-)$
- $G_F/\sqrt2 = g^2/(8m_W^2)$ (tree level)

Terms introduced: nucleon, lepton, quark, neutrino, flavour, beta decay, valence-quark content, parity, polarized, chirality, helicity, projector, doublet, singlet, weak isospin, SU(2), generator, non-Abelian, Yang–Mills, structure constants, charged current, V−A, generation, CKM matrix, Fermi constant, unitary gauge.

### 2.15–2.18 Planned chapters (stubs)

- `electroweak-unification.md` (11 lines) — planned: chiral states, GSW model, SU(2)L×U(1)Y, electroweak Lagrangian.
- `higgs-mechanism.md` (13 lines) — planned: SSB, Higgs U(1), SM Higgs, fermion/gauge-boson masses.
- `qcd.md` (13 lines) — planned: quarks, confinement, color, SU(3)C, gauge structure.
- `standard-model.md` (17 lines) — planned: gauge self-interactions, quarks/leptons, Higgs, Yukawa, generations/flavor mixing.

These pages are placeholders; the material is referenced from earlier pages (e.g. weak-interaction.md refers forward to Higgs and electroweak chapters for gauge-boson masses and the Z/photon relation).

### 2.19 Path Integrals — QM (`path-integrals.md`, 73 lines)

Topics: sum over paths; action phase; classical limit; free-particle propagator.

Key equations:
- $K = \int\mathcal D x\,e^{iS[x]/\hbar}$
- Free particle: $K_0 = \sqrt{\frac{m}{2\pi i\hbar T}}\exp[\frac{im(x_f-x_i)^2}{2\hbar T}]$

Terms introduced: sum over paths, propagation amplitude, functional integration (notation only).

### 2.20 Path Integrals — Fields (`path-integrals-fields.md`, 72 lines)

Topics: field histories; two-point function; Gaussian integrals/pairings; Wick's theorem via path integrals; vertices; Compton recovery.

Key equations:
- $\int\mathcal D\phi\,e^{iS[\phi]}$
- Pairings of four fields; $\frac{i}{p^2-m^2+i\epsilon}$

Terms introduced: two-point correlation function, Gaussian integral, pairing, symmetry factor, vertex/propagator/external-line correspondence.

### 2.21 Fermionic Path Integrals (`path-integrals-fermions.md`, 59 lines)

Topics: Grassmann variables; Berezin integration; fermion propagator; closed-loop minus sign; trace; determinant.

Key equations:
- $\theta_1\theta_2=-\theta_2\theta_1$; $\int d\theta(a+b\theta)=b$
- $(\not p-m)(\not p+m)=p^2-m^2$

Terms introduced: Grassmann variable, Berezin integration (implicit), fermion propagator, closed fermion loop, trace, determinant.

### 2.22 Gauge Fixing (`path-integrals-gauge-fixing.md`, 73 lines)

Topics: gauge orbits; Lorenz gauge; Faddeev–Popov determinant; covariant gauges; current conservation; ghosts.

Key equations:
- $\mathcal L_{\mathrm{gf}}=-\frac{1}{2\xi}(\partial_\mu A^\mu)^2$; Feynman gauge $\xi=1$
- $k_\mu J^\mu=0$

Terms introduced: gauge orbit, Faddeev–Popov determinant, covariant gauge, ghost, current conservation.

### 2.23 Renormalization at One Loop (`path-integrals-renormalization.md`, 79 lines)

Topics: regulator; bare vs renormalized parameter; counterterm; running scale; RG equations; infrared vs ultraviolet.

Key equations:
- $M^2 = m_0^2(\Lambda) + \Delta m_{\mathrm{loop}}^2(\Lambda)$
- $m_0^2 = m_R^2 + \delta m^2(\Lambda)$
- vertex $= \lambda_R + F(Q) - F(Q_*)$

Terms introduced: regulator, cutoff, dimensional regularization, bare/renormalized parameter, counterterm, on-shell convention, renormalization scale, renormalization-group equations, infrared divergence, inclusive rate.

---

## 3. Cross-cutting term glossary (with where each is introduced)

| Term | First defined at | Notes |
| --- | --- | --- |
| action / stationary action | `classical-mechanics.md:17-21` | good |
| Lagrangian (density) | `classical-mechanics.md:17` / `qft-action.md:27` | good |
| phase space | `classical-mechanics.md:43` | good |
| Poisson bracket | `classical-mechanics.md:55` | good; Jacobi identity named but never written |
| Hilbert space / vector / inner product | `first-quantization.md:5` | *named*, not explained (see §5) |
| bra-ket notation $\langle \cdot \vert \cdot \rangle$ | never | used from `first-quantization.md:91` on; see §5 |
| operator / linear / adjoint / Hermitian / unitary | `first-quantization.md:37-103` | footnotes are dense; assume matrices |
| eigenvalue / eigenstate | `first-quantization.md:49` | good |
| commutator / anticommutator | `first-quantization.md:59` / `relativistic-qm.md:169` | good |
| wave function / Born rule | `first-quantization.md:21-23` | good |
| uncertainty relation | `first-quantization.md:71-77` | "standard deviation" assumed |
| ladder / creation / annihilation | `harmonic-oscillator.md:45-77` | good |
| zero-point energy / vacuum | `harmonic-oscillator.md:85` | good |
| Lorentz factor / interval / four-vector | `special-relativity.md` | good |
| metric / covariant / contravariant / Einstein sum | `special-relativity.md:66-122` | advanced; see §4 |
| tensor / contraction | `special-relativity.md:108-118` | advanced |
| d'Alembertian | `special-relativity.md:183` | good |
| field tensor | `special-relativity.md:153` | advanced |
| plane wave | `relativistic-qm.md:37` | good |
| Klein–Gordon / Dirac equation | `relativistic-qm.md:69` / `:155` | good |
| antiparticle / Stückelberg–Feynman / hole theory | `relativistic-qm.md:93`, `dirac-equation.md:165` | good |
| spin / spinor / small components | `dirac-equation.md:9-55` | good |
| helicity / chirality | `weak-interaction.md:103-105` | helicity→chirality statement flagged |
| rapidity / hyperbolic functions | `dirac-equation.md:295` | functions never defined |
| second quantization / field operator | `qft.md:104-110` | good |
| operator-valued distribution | `qft.md:110` | named, not explained |
| Schrödinger/Heisenberg picture | `qft.md:116-130` | good |
| matrix element | `qft.md:38` | good (previously missing, now fixed) |
| on shell / mass shell | `field-quantization.md:307` | good (footnote) |
| delta function $\delta$ | `field-quantization.md:171` | glossed as "continuous Kronecker" |
| boson / fermion / Pauli exclusion | `field-quantization.md:237-289` | good |
| propagator | `perturbation-theory.md:109` | good |
| U(1) / group / symmetry | `qed.md:45-53` | "group" never defined (see §5) |
| gauge symmetry / covariant derivative / minimal coupling | `qed.md:57-97` | good |
| Lorenz condition / Feynman gauge / Gupta–Bleuler | `qed.md:235-335` | good |
| cross section / S-matrix / invariant amplitude | `lagrangian-to-experiment.md` | good |
| phase-space measure | `lagrangian-to-experiment.md:59` | schematic only (see §5) |
| Dyson series / Wick's theorem / contraction | `perturbation-theory.md:53-81` | good |
| symmetry factor | `perturbation-theory.md:127` | named, never computed |
| Feynman diagram / virtual particle / off-shell | `feynman-rules.md:85-91` | good |
| Mandelstam variables | `feynman-rules.md` footnote | defined only in a footnote |
| ultraviolet/infrared divergence / regulator / renormalization | `feynman-rules.md:264-274` | advanced |
| $\gamma^5$ / projector / V−A | `weak-interaction.md:75-142` | good |
| SU(2) / generator / doublet / non-Abelian / Yang–Mills | `weak-interaction.md:148-277` | "group"/"generator" assumed |
| CKM matrix / Fermi constant / unitary gauge | `weak-interaction.md:349-426` | good; propagator flagged "given without proof" |
| Grassmann variable / Faddeev–Popov / ghost / RG | path-integral pages | advanced |

---

## 4. Math-level audit (target: high school)

The site *requires* the following beyond high school, essentially from page 1, and does not teach any of it:

### 4.1 Calculus (used as prerequisite, never taught)
- Derivatives and partial derivatives — `classical-mechanics.md:17` onward; partial-derivative notation $\partial L/\partial q$ is never explained.
- Definite integrals and integration by parts — `classical-mechanics.md:23`.
- Taylor series — `harmonic-oscillator.md:5` ("a Taylor expansion gives…").
- Separation of variables for a PDE — `relativistic-qm.md:19-29`.
- Vector calculus ($\nabla$, $\nabla\cdot$, $\nabla\times$) — Maxwell equations at `special-relativity.md:147`; the continuity equation at `relativistic-qm.md:107`.
- Functional derivative $\delta H/\delta\pi$ — `qft-action.md:67`.
- Contour integration / residue theorem — the propagator derivation at `perturbation-theory.md:103-107` and footnote `:167` ("close the contour in the lower half-plane"). This is complex analysis, fully unexplained.
- Gaussian integrals — `path-integrals-fields.md:35`.
- Matrix exponentials — `dirac-equation.md:223`, `first-quantization.md:103`.

### 4.2 Linear algebra and functional analysis (used, never taught)
- Hilbert space, inner products, norms — `first-quantization.md:5`.
- Bra-ket notation — `first-quantization.md:91` (never defined).
- Operators, adjoint, Hermitian, unitary — `first-quantization.md:89-103`.
- Spectral theorem, orthonormal eigenbasis — `first-quantization.md:95`.
- Dirac delta function — `field-quantization.md:51`.
- Operator-valued distributions — `qft.md:110`.
- Matrix trace (for closed fermion loops) — `feynman-rules.md:245`.

### 4.3 Tensor calculus / index notation
- Four-vectors, covariant vs contravariant indices, Einstein summation, tensors of type $(r,s)$, the general tensor transformation law — `special-relativity.md:66-122`. This is a full tensor-calculus unit compressed into ~50 lines.
- Exterior derivative / differential geometry — `special-relativity.md:169` ("In differential-geometric language, the field tensor is the exterior derivative of the potential"). A passing reference, unexplained and entirely outside high school.

### 4.4 Complex numbers and Fourier analysis
- Complex numbers are gestured at (`first-quantization.md:129` "visualize a complex number as a point in a plane") but **Euler's formula $e^{i\theta}=\cos\theta+i\sin\theta$ is never stated**, and complex exponentials are used constantly from `relativistic-qm.md` onward.
- Fourier transforms — `first-quantization.md:133`, `field-quantization.md:25,125` — named, never explained.

### 4.5 Group theory / abstract algebra
- Groups, generators, non-Abelian, structure constants — `weak-interaction.md:148-277`. The word "group" is never defined (`qed.md:53` "the phase factors form the group U(1)").
- Pauli matrices, gamma matrices, Clifford algebra — `relativistic-qm.md`, `dirac-equation.md`.

### 4.6 Path-integral machinery (optional pages)
- Functional integration and measure $\mathcal D x$ — `path-integrals.md:40`.
- Grassmann variables and Berezin integration — `path-integrals-fermions.md:13-27`.
- Faddeev–Popov determinant — `path-integrals-gauge-fixing.md:35`.
- Renormalization group equations — `path-integrals-renormalization.md:69`.

### 4.7 Statistics
- Standard deviation ($\Delta x$, $\Delta p$) and expectation value $\langle\cdot\rangle$ — `first-quantization.md:75-77`. Mild, but "standard deviation" is not formally defined.

### Assessment

High school math alone (algebra, geometry, trigonometry, basic functions) is insufficient for **every** page except, partially, `special-relativity.md` §1–§4 and the qualitative parts of `lagrangian-to-experiment.md`. The single most important omission relative to the stated goal is that the site never declares these prerequisites. If the intended audience is a high-school learner, then either (a) the calculus/linear-algebra/tensor prerequisites need their own foundational pages, or (b) the target should be restated ("calculus and linear algebra assumed").

---

## 5. Logic gaps (relied on but unexplained, *not* flagged in the text)

These differ from the site's own honest "Given without proof" flags (massive-vector propagator, helicity relation) — these are silent.

1. **Bra-ket notation is never defined.** $\langle \phi | \hat A^\dagger \psi \rangle$, $|0\rangle$, $\langle n | n \rangle$ appear from `first-quantization.md:91` onward with no introduction of what $|\cdot\rangle$ and $\langle\cdot|$ mean or how an inner product is computed. This is the most basic object of the whole sequence and it is assumed.

2. **Noether's theorem is invoked but never stated or derived.** `qed.md:47` ("Applying Noether's theorem … gives the conserved current $j^\mu=q\bar\psi\gamma^\mu\psi$") links to `qft-action.md`, which only *mentions* the theorem (`qft-action.md:73`), never proves or even states it. The conserved-current result is central to QED and arrives from nowhere. A reader cannot verify the one claim that "this symmetry gives charge conservation."

3. **The phase-space measure $d\Pi$ is never given.** `lagrangian-to-experiment.md:57-59` writes $\sigma = \frac1\Phi\int|\mathcal M|^2 d\Pi$ and says $d\Pi$ "integrates over final momenta and includes energy and momentum conservation," but no formula is ever provided. Consequence: a reader who has followed every step to the Feynman rules still cannot compute an actual cross section. The site's central promise ("from Lagrangian to experiment") is never cashed out numerically.

4. **Spin/polarization sums are never given.** `feynman-rules.md:144` says to "average over two electron spins and two photon polarizations" and "sum over unobserved final spins and polarizations," but the required identities ($\sum_s u_s\bar u_s = \not p + m$, $\sum_\lambda \varepsilon_\mu^{(\lambda)}\varepsilon_\nu^{(\lambda)*}$) never appear. Combined with (3), the Compton cross section is uncomputable from the site's own text.

5. **The g=2 / Pauli-equation limit is asserted, not shown.** `dirac-equation.md:59-61` ("Taking the nonrelativistic limit gives the Pauli equation and $\boldsymbol\mu=-\frac em\mathbf S$, $g=2$") and `relativistic-qm.md:205`. This is a famous, non-obvious result; the intermediate steps are absent and it is not flagged as omitted.

6. **Minimal substitution "reproduces the classical Lorentz force"** — `dirac-equation.md:57`. Asserted, never demonstrated.

7. **Charge conjugation is not fully derived.** `dirac-equation.md:139-145` states that $\psi_c=\eta\psi^*$ maps to a negative-energy solution and obeys the charge-conjugated equation "up to phase," but does not actually perform the algebra. The reader must trust the result.

8. **Euler's formula is never stated.** Every plane wave uses $e^{i(\mathbf p\cdot\mathbf x - Et)/\hbar}$, and later pages rely on "$e^{i\theta}$ has angle $\theta$," but the identity connecting this to $\cos\theta + i\sin\theta$ never appears.

9. **Fourier transforms are named but never explained.** `first-quantization.md:133` ("A Fourier transform relates these representations") and the mode expansions of `field-quantization.md` assume the reader already knows what a Fourier transform does. The entire particle-interpretation of QFT hangs on this step.

10. **Contour integration is unexplained.** The propagator's pole structure and the "close the contour" step (`perturbation-theory.md:107,167`) assume complex analysis. The footnote *describes* what to do but not *why* it works (residue theorem).

11. **The word "group" is never defined.** U(1) (`qed.md:53`), SU(2) (`weak-interaction.md:158`), generators, "non-Abelian" — the abstract-algebra vocabulary is used as if known. "Generators" is at least partially glossed in `weak-interaction.md:160`, but "group" itself is not.

12. **Symmetry factors are named but never computed.** `perturbation-theory.md:127,151` — "Diagrams with equivalent pairings can also require symmetry factors." No rule for computing them is given, so the reader cannot handle any diagram with an internal symmetry.

13. **The S-matrix-to-probability link is implicit.** `lagrangian-to-experiment.md` defines $\langle f|S|i\rangle$ and references the Born rule, but never states that $|\langle f|S|i\rangle|^2$ (suitably normalized) is the transition probability. The chain "amplitude → probability → rate" is asserted in a diagram but not written.

14. **Jacobi identity is named but never written.** `classical-mechanics.md:57` — "It also satisfies the Jacobi identity, a consistency relation between nested brackets." The identity itself is not shown.

15. **Dimensional regularization "in $d=4-2\delta$ dimensions"** — `feynman-rules.md:266` and `path-integrals-renormalization.md:17`. The idea of analytically continuing to non-integer dimension is unexplained (this one is arguably beyond the site's own scope and is flagged only loosely).

16. **"Trace over spinor indices"** — `feynman-rules.md:245`. Matrix trace is never defined anywhere in the sequence.

17. **Unit consistency / natural units.** The sequence switches between keeping $\hbar$ explicit and setting $\hbar=c=1$, sometimes mid-page (`qed.md:307` "from here to the end of this section we also set $\hbar=1$"). The concept of "natural units" (why setting $c=1$ is a choice of units, not an approximation) is never explained; the phrase "natural units" first appears at `perturbation-theory.md:11` without a definition. A novice will not understand why a velocity can be "set to 1."

18. **The free-particle propagator $K_0$** — `path-integrals.md:60` "Evaluating the free-particle path integral gives …" — stated without derivation (optional page, but unflagged).

19. **"Exterior derivative"** — `special-relativity.md:169` — differential-geometry reference dropped in without explanation or necessity.

20. **Spin sums / helicity-basis projection** — `weak-interaction.md:105` gives the massless helicity rule; it *is* flagged "given without proof" (good), but the sentence immediately after ("Proving it requires solving the Dirac equation in a helicity basis…") does not supply enough for the reader to reconstruct even the outline.

---

## 6. Explicitly-flagged gaps (the site already acknowledges these)

For completeness — these are *not* problems of silence, but they are load-bearing results deferred elsewhere:

- Massive-vector propagator "given without proof" — `weak-interaction.md:400`.
- Helicity↔chirality particle/antiparticle relation "given without proof" — `weak-interaction.md:107`.
- LSZ reduction formula "we do not derive it here" — `perturbation-theory.md:171` (footnote).
- Spin–statistics theorem "requires further assumptions, including locality" — `qft.md:172`, `field-quantization.md:293`.
- Four planned chapters are empty stubs: `electroweak-unification.md`, `higgs-mechanism.md`, `qcd.md`, `standard-model.md`. Their content is referenced from earlier pages (gauge-boson masses, the $Z$/$W^3$/photon relation, quark confinement, Yukawa couplings) but not yet present.

---

## 7. Terminology / consistency notes

- "Branch" vs "term": `memory/phyz-terminology.md` records a preference for "term"/"the negative-energy solutions" over "branch." Several pages still use "branch" (`dirac-equation.md:101-137`, `relativistic-qm.md`), which is consistent with the note's instruction to leave existing pages alone unless asked to sweep.
- "Matrix element" is now glossed at `qft.md:38` (this was a previously-reported gap and has been fixed).
- Consistent conventions observed: metric signature $(+,-,-,-)$; $D_\mu=\partial_\mu+igW_\mu$ (plus-sign convention, noted at `weak-interaction.md:262`); $c=1$ then $\hbar=1$ set explicitly per-section.

---

## 8. Recommended priorities (if the goal is a high-school-accessible path)

1. Add a short "Prerequisites" note on the home page naming the real requirements (single-variable calculus, some linear algebra, complex numbers) — or, if the target truly is high-school math, add foundational pages for derivatives/integrals, complex numbers + Euler's formula, and basic matrix/vector algebra before `classical-mechanics.md`.
2. Define bra-ket notation once, near `first-quantization.md:5`, before it is used in the adjoint footnote.
3. State Noether's theorem (one line) where it is first invoked, or replace the invocation with an explicit one-page derivation of the conserved current.
4. Supply the phase-space measure formula and the spin/polarization sums so a Compton cross section can actually be completed.
5. Either derive or flag the g=2/Pauli-equation limit and the charge-conjugation algebra.
6. State Euler's formula and a one-line Fourier-transform gloss the first time each is used.
7. Define "group," "trace," "contour/residue," and "natural units" at first use (the last is now glossed nowhere).
8. Fill the four stub chapters, or soften the forward references that currently point to non-existent content.

---

## 9. Resolution status (updated 2026-09-08)

A "Math Refresher" appendix was added (5 pages: `appendix-math-{calculus,complex,linear-algebra,tensors,groups}.md`, wired into `config.js` nav + sidebar) plus targeted in-text fixes. The coverage knowledge base now lives in `memory/phyz-content-coverage.md` (per-page scope, term→first-definition map, conventions, open gaps) so new content can be cross-checked against it.

§5 logic gaps now **resolved**:
- #1 bra-ket — glossed at `first-quantization.md` §6, developed in `appendix-math-linear-algebra.md`.
- #2 Noether — stated at `qed.md:47` and `qft-action.md`.
- #3 phase-space measure — explicit $d\Pi_n$ + 2→2 CM formula in `lagrangian-to-experiment.md`.
- #4 spin/polarization sums — completeness relations + Casimir's trick + Klein–Nishina in `feynman-rules.md`.
- #5 g=2 — "Extra: the nonrelativistic limit and $g=2$" box in `dirac-equation.md`.
- #7 charge conjugation — "Extra: verifying the charge-conjugation map" box in `dirac-equation.md`.
- #8 Euler's formula — stated at `first-quantization.md`, developed in `appendix-math-complex.md`.
- #11 "group" — `appendix-math-groups.md`.
- #16 trace — `appendix-math-linear-algebra.md` §6.
- #17 natural units — glossed at `perturbation-theory.md:11`.
- #19 exterior derivative — removed from `special-relativity.md`.

§4 math-level audit: §4.1–4.5 now each have a corresponding appendix page (the "assumed" math is now taught at minimum depth). Exceptions still unaddressed: contour integration/residues (#10; `appendix-math-complex.md` deliberately omits them), Gaussian integrals, functional derivatives, and operator-valued distributions.

Still open:
- #6 minimal substitution "reproduces the Lorentz force" — asserted, not shown.
- #9 Fourier — in the appendix now, but the inline mentions in `first-quantization.md:133` / `field-quantization.md` are still bare names.
- #10 contour/residue, #12 symmetry factors, #13 S-matrix→probability, #14 Jacobi identity, #15 dimensional regularization, #18 $K_0$ derivation, #20 helicity-basis outline.
- The four stub chapters (`electroweak-unification`, `higgs-mechanism`, `qcd`, `standard-model`) — still the largest outstanding gap.

---

*Audit generated from a full read of `docs/*.md` and `docs/.vuepress/config.js` on 2026-09-08.*
