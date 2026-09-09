---
name: phyz-content-coverage
description: "What the Phyz docs already cover — per-page scope, term→first-definition map, conventions, and open gaps. Source this before adding new content to avoid duplicate explanations."
metadata:
  node_type: memory
  type: reference
---

A knowledge base of what the Phyz docs (`docs/*.md`) already explain, so new content can link to existing explanations instead of repeating them. The full line-by-line analysis (math-level audit, silent logic gaps) lives in `SITE-AUDIT.md` at the repo root; this file is the quick-reference source of truth.

## Reading order and per-page scope

Reading order is set by the `sidebar` array in `docs/.vuepress/config.js`.

1. `classical-mechanics.md` — Newton's 2nd law, generalized coordinates, Lagrangian, action + stationary action, Euler–Lagrange equation, conjugate momentum / Legendre transform, Hamilton's equations, phase space, Poisson bracket, canonical-quantization preview.
2. `first-quantization.md` — Hilbert space, first quantization, Schrödinger equation, Born rule, Copenhagen interpretation, operators/observables, eigenvectors/eigenvalues, commutators, superposition, uncertainty principle. Footnotes define Hermitian/unitary/adjoint, position/momentum representation, Bell's theorem. Bra-ket notation is glossed in main text at §6.
3. `harmonic-oscillator.md` — quadratic approximation, classical oscillator, ladder operators, number operator, spectrum $E_n=\hbar\omega(n+1/2)$, zero-point energy.
4. `special-relativity.md` — postulates, Galilean vs Lorentz transforms, simultaneity, spacetime interval, four-vectors, Minkowski metric, covariant/contravariant indices, tensors/contraction, energy–momentum relation, Maxwell equations in tensor form, Schrödinger non-invariance.
5. `relativistic-qm.md` — plane waves, Klein–Gordon equation, negative energies, Klein–Gordon current, Dirac equation construction (α/β/γ matrices, anticommutation relations, small components).
6. `dirac-equation.md` — spin (orbital + intrinsic), Heisenberg equation, antiparticles + rest/moving spinors, charge conjugation, spinor Lorentz transformations (two detailed "Extra" boxes). Added "Extra" boxes: nonrelativistic limit → $g=2$, and charge-conjugation verification.
7. `qft.md` — field operators, promotion of amplitudes to operators, field classification (scalar/vector/spinor), second quantization, Schrödinger/Heisenberg pictures, state-vs-field, wave functional.
8. `qft-action.md` — field action, Lagrangian density, field Euler–Lagrange equation, Hamiltonian/state space, functional derivative, Noether's theorem (stated), KG/Maxwell/Dirac Lagrangians.
9. `field-quantization.md` — scalar mode expansion, equal-time canonical commutator, ladder commutators, one oscillator per momentum, particle creation, spinor field (anticommutators), Pauli exclusion, spin-statistics preview, propagator preview.
10. `qed.md` — QED Lagrangian, U(1) global vs local symmetry, covariant derivative, minimal coupling, Noether → charge conservation, photon quantization (polarizations, Lorenz gauge, Gupta–Bleuler, Feynman gauge), photon propagator.
11. `lagrangian-to-experiment.md` — cross section, decay rate, S-matrix, invariant amplitude, explicit phase-space measure + 2→2 CM cross-section formula.
12. `perturbation-theory.md` — interacting scalar ($\phi^3$), Dyson series, time ordering, Wick's theorem, propagator, vertex factor, QED rule dictionary. Natural units first glossed here (§1).
13. `feynman-rules.md` — Feynman diagrams, Compton s/u-channels, QED Feynman rules, full algebraic derivation, loops, UV/IR divergences, renormalization preview. Added: spin/polarization completeness relations, Casimir's trick, Klein–Nishina formula.
14. `weak-interaction.md` — beta decay, neutrinos, parity violation, $\gamma^5$/chiral projectors, helicity vs chirality, SU(2) gauge symmetry, Yang–Mills field strength + self-interactions, charged current, CKM matrix, Fermi (low-energy) limit.
15. `electroweak-unification.md` — why W³ cannot be the photon; chiral charge assignments; hypercharge and Q=T³+Y/2; local SU(2)L × U(1)Y and Bμ; photon/Z mixing and e=g sin θW=g′ cos θW; neutral-current couplings; νμ–electron scattering diagram and amplitude; gauge+fermion Lagrangian; gauge/fermion mass obstruction leading to Higgs. Short algebra in expandable sections. Higgs selection of mass eigenstates and masses deferred to the next chapter.
16. `higgs-mechanism.md` — **STUB**.
17. `qcd.md` — **STUB**.
18. `standard-model.md` — **STUB**.
19–23. `path-integrals*.md` — optional sequence (paths, fields, fermions, gauge fixing, renormalization).
24–28. `appendix-math-*.md` — **Math Refresher** appendix (calculus, complex numbers, linear algebra, index notation/tensors, groups/symmetry).

## Math Refresher appendix (do NOT re-teach this inline)

Five pages under `docs/appendix-math-*.md`, each teaching from zero (definition + worked example + pointer to where it's used). When new content needs a tool, link to the appendix; don't re-derive.

- `appendix-math-calculus.md` — derivative, partial derivative, chain rule, integration by parts, Taylor expansion, vector calculus ($\nabla$, $\nabla\cdot$, $\nabla\times$, Laplacian, d'Alembertian).
- `appendix-math-complex.md` — complex numbers, Euler's formula, phases/interference, waves + Fourier transform, conjugation↔adjoint.
- `appendix-math-linear-algebra.md` — matrices, transpose/conjugate-transpose/adjoint, eigenvalues, bra-ket notation, Hermitian/unitary, trace, spectral theorem.
- `appendix-math-tensors.md` — Einstein summation, metric, upper/lower indices, contraction, Lorentz scalars.
- `appendix-math-groups.md` — group, U(1), generators, SU(2)/Pauli matrices, non-Abelian + structure constants.

Unusual notation is still glossed inline at first use in the main text (e.g. bra-ket in `first-quantization.md` §6, Euler's formula in `first-quantization.md`, "natural units" in `perturbation-theory.md:11`). The appendix is the deep version; the inline gloss is the one-liner.

## Conventions (keep consistent)

- Metric signature $(+,-,-,-)$, $\eta_{\mu\nu}=\operatorname{diag}(1,-1,-1,-1)$.
- Covariant derivative: QED $D_\mu=\partial_\mu+\frac{iq}{\hbar}A_\mu$; weak $D_\mu=\partial_\mu+igW_\mu$ (plus-sign convention, stated at `weak-interaction.md`).
- Units: pages 1–9 keep $\hbar$ explicit (and often $c=1$); from `perturbation-theory.md` onward, natural units $\hbar=c=1$. Each page states its convention at the top.
- Photon propagator in Feynman gauge: $-ig_{\mu\nu}/(k^2+i\epsilon)$.
- Electroweak hypercharge: $Q=T^3+Y/2$, $D_\mu=\partial_\mu+igT^aW_\mu^a+ig'(Y/2)B_\mu$. Lepton doublet $Y=-1$, right electron $Y=-2$. Neutral mixing: $A=s_WW^3+c_WB$, $Z=c_WW^3-s_WB$; $e=gs_W=g'c_W$.
- Spacetime diagrams: **x vertical, t horizontal** (see [[phyz-manim-setup]]).
- Terminology: use "term"/"negative-energy solutions", not "branch" for the u/v solution parts (see [[phyz-terminology]]).

## Term → first-definition map (most-consulted entries)

| Term | First defined at |
| --- | --- |
| action / stationary action | `classical-mechanics.md` §2 |
| Lagrangian (density) | `classical-mechanics.md` / `qft-action.md` |
| phase space / conjugate momentum | `classical-mechanics.md` §3 |
| Poisson bracket | `classical-mechanics.md` §4 |
| Hilbert space / bra-ket | `first-quantization.md` §1 / §6 (+ `appendix-math-linear-algebra.md`) |
| operator / adjoint / Hermitian / unitary | `first-quantization.md` footnotes |
| eigenvalue / eigenstate | `first-quantization.md` §7 |
| commutator / anticommutator | `first-quantization.md` §8 / `relativistic-qm.md` §4 |
| Born rule / wave function | `first-quantization.md` §3 |
| uncertainty relation | `first-quantization.md` §10 |
| ladder / creation / annihilation | `harmonic-oscillator.md` §4–5 |
| zero-point energy / vacuum | `harmonic-oscillator.md` §6 / `field-quantization.md` |
| Lorentz factor / interval / four-vector | `special-relativity.md` §3–5 |
| metric / covariant / contravariant / Einstein sum | `special-relativity.md` §6 |
| d'Alembertian | `special-relativity.md` §9 |
| field tensor | `special-relativity.md` §8 |
| plane wave | `relativistic-qm.md` §1 |
| Klein–Gordon / Dirac equation | `relativistic-qm.md` §2 / §4 |
| antiparticle / Stückelberg–Feynman / hole theory | `relativistic-qm.md` §3 / `dirac-equation.md` §3–4 |
| spin / spinor / small components | `dirac-equation.md` §1 |
| gyromagnetic factor $g=2$ | `dirac-equation.md` §1 (+ "Extra" box) |
| charge conjugation | `dirac-equation.md` §3 (+ "Extra" box) |
| helicity / chirality | `weak-interaction.md` §2 |
| second quantization / field operator | `qft.md` |
| operator-valued distribution | `qft.md` |
| Schrödinger/Heisenberg picture | `qft.md` |
| matrix element | `qft.md` |
| on shell / mass shell | `field-quantization.md` footnote |
| Dirac delta function | `field-quantization.md` |
| boson / fermion / Pauli exclusion | `field-quantization.md` |
| propagator | `perturbation-theory.md` §5 |
| U(1) / gauge symmetry / covariant derivative / minimal coupling | `qed.md` |
| Lorenz condition / Feynman gauge / Gupta–Bleuler | `qed.md` |
| cross section / S-matrix / invariant amplitude | `lagrangian-to-experiment.md` |
| phase-space measure / 2→2 CM formula | `lagrangian-to-experiment.md` |
| Dyson series / Wick's theorem / contraction | `perturbation-theory.md` |
| symmetry factor | `perturbation-theory.md` (named, not computed) |
| Feynman diagram / virtual particle / off-shell | `feynman-rules.md` |
| Mandelstam variables | `feynman-rules.md` footnote |
| spin/polarization sums / Casimir's trick / Klein–Nishina | `feynman-rules.md` |
| UV/IR divergence / regulator / renormalization | `feynman-rules.md` / `path-integrals-renormalization.md` |
| $\gamma^5$ / chiral projectors / V−A | `weak-interaction.md` |
| SU(2) / generator / doublet / non-Abelian / Yang–Mills | `weak-interaction.md` |
| CKM matrix / Fermi constant | `weak-interaction.md` |
| hypercharge / Bμ / weak mixing angle / photon–Z mixing | `electroweak-unification.md` |
| neutral-current chiral coefficients / νμ–electron scattering | `electroweak-unification.md` |

## Open gaps (know before writing new content)

- **Stub chapters**: `higgs-mechanism.md`, `qcd.md`, `standard-model.md` contain only planned headings. Earlier pages forward-reference them (gauge-boson masses, confinement, Yukawa couplings) — these are the highest-value missing content. Electroweak now derives the photon/Z coupling combinations; the Higgs derivation of their masses and selection as mass eigenstates remains open.
- **Explicitly "given without proof"** (deferred by design): massive-vector propagator (`weak-interaction.md`), helicity↔chirality statement (`weak-interaction.md`), LSZ reduction (`perturbation-theory.md` footnote), general spin–statistics theorem (`qft.md`/`field-quantization.md`).
- **Named but not computed**: symmetry factors (`perturbation-theory.md`).

## How to apply

Before adding any new page or section: (1) check the term map above and link to the existing definition instead of re-defining; (2) reuse the conventions listed; (3) put any needed math background in the Math Refresher appendix rather than teaching it inline; (4) if a "given without proof" item is now being filled, update both the page and this file. Also see [[phyz-prose-style]] for voice and [[phyz-vuepress-quirks]] for build/verify steps (`pnpm docs:build`, grep `docs/.vuepress/dist/`).
