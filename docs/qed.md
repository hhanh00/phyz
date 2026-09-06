# Quantum Electrodynamics

## Recap of the Lagrangians

QED is the theory of two species of quantum — the electron and the photon — so it starts from the two free Lagrangians the [Action and Lagrangians](qft-action.md) page read off the field table, one per species.

The **Dirac Lagrangian** describes the electron field. Its density,

$$\mathcal{L}_\text{Dirac} = \bar\psi\left(i\hbar\gamma^\mu\partial_\mu - m\right)\psi,$$

combines a kinetic term, $\bar\psi\,i\hbar\gamma^\mu\partial_\mu\,\psi$, with a mass term, $-m\bar\psi\psi$, and its Euler–Lagrange equation is the Dirac equation. The **Maxwell Lagrangian** describes the photon field, the vector $A_\mu$:

$$\mathcal{L}_\text{Maxwell} = -\tfrac14 F_{\mu\nu}F^{\mu\nu}, \qquad F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu.$$

Its Euler–Lagrange equation is Maxwell's equations in free space, $\partial_\mu F^{\mu\nu} = 0$.

Taken separately, these two Lagrangians describe a world in which electrons move freely and photons move freely, each unaware of the other. That is not the world we live in: electrons carry charge, and charge is what makes photons, so QED seeks a single Lagrangian that includes both species and the way each acts on the other. The claim, argued over the next two sections, is

$$\mathcal{L}_\text{QED} = -\tfrac14 F_{\mu\nu}F^{\mu\nu} \;+\; \bar\psi\left(i\hbar\gamma^\mu\partial_\mu - m\right)\psi \;-\; q\,\bar\psi\gamma^\mu\psi\,A_\mu .$$

The first two terms are the free Lagrangians above, and the third is the **interaction term**: it couples the photon $A_\mu$ to the electron current $\bar\psi\gamma^\mu\psi$, with the charge $q$ fixing the strength.

The interaction term is not added by hand — it follows from a single substitution. Replace the ordinary derivative in the Dirac Lagrangian by the covariant derivative,

$$\partial_\mu \;\to\; D_\mu = \partial_\mu + \frac{iq}{\hbar}A_\mu ,$$

and the kinetic term splits into the free kinetic term plus $-q\bar\psi\gamma^\mu\psi\,A_\mu$. This is the minimal coupling that [The Dirac Equation §1](dirac-equation.md#_1-spin) used to introduce charge in the first place. The next two sections justify why a gauge principle demands exactly this substitution, and the term above is what that principle forces.

## U(1) Global Symmetry

The electron's wave function carries a phase, but no experiment can detect it. [First Quantization](first-quantization.md) computes every probability from the squared amplitude,

$$P = |\psi|^2 = \psi^*\psi,$$

and squaring throws the phase away. Slide the phase by an angle $\alpha$ — multiply $\psi$ by $e^{i\alpha}$ — and every observable probability is left exactly as it was. The phase is present in the amplitude and invisible in the predictions.

That indifference is a **symmetry**, in the ordinary sense of the word: an operation you can perform on a system without changing its behavior. A circle looks the same after a rotation, and re-phasing the electron field is an operation of the same kind:

$$\psi \to e^{i\alpha}\psi, \qquad \bar\psi \to e^{-i\alpha}\bar\psi .$$

The Dirac Lagrangian cannot tell that it happened. Every term pairs a $\bar\psi$ with a $\psi$, so the two phases cancel — $\bar\psi\psi \to e^{-i\alpha}e^{i\alpha}\bar\psi\psi = \bar\psi\psi$, and the kinetic term $\bar\psi\gamma^\mu\partial_\mu\psi$ cancels the same way. Because the action is built from these bilinears alone, the equations of motion, and with them the physics, are unchanged. The invariance is **global**: $\alpha$ is one number, the same at every point of spacetime.

A continuous symmetry never sits idle. [Noether's theorem](qft-action.md) pairs every such symmetry with a conserved quantity, and this one is no exception: the re-phasing invariance guarantees a conserved current,

$$j^\mu = q\,\bar\psi\gamma^\mu\psi, \qquad \partial_\mu j^\mu = 0,$$

whose conserved charge is the electric charge. Phase symmetry is therefore charge conservation in disguise — the freedom to re-phase the field is what makes a conserved electric current exist at all.

The family of re-phasings has a shape worth naming. As $\alpha$ runs over all angles, the factors $e^{i\alpha}$ trace out a circle, and a circle of transformations is the group called **U(1)**: unitary because $|e^{i\alpha}| = 1$, with the $1$ because a single angle labels every member. This section's global symmetry is a U(1) symmetry.

That symmetry is also the seed of the next step. If the absolute phase is unobservable, singling out one common phase at every point is arbitrary — nothing in the physics prefers it. Promote $\alpha$ to a function $\alpha(x)$, letting each point choose its own phase, and the derivative no longer commutes past the phase: $\partial_\mu\big(e^{i\alpha(x)}\psi\big)$ leaves a $\partial_\mu\alpha(x)$ term behind, and the Lagrangian is no longer invariant. Restoring invariance forces a new field into the theory, the gauge field $A_\mu$, and with it a rule that trades the ordinary derivative for the covariant one. That demand is the local gauge symmetry of the next section, and it is exactly where the photon and the interaction term $-q\bar\psi\gamma^\mu\psi\,A_\mu$ come from.

## Local Gauge Symmetry U(1)

The last section's symmetry used one phase for all of spacetime, and that choice is arbitrary. If the absolute phase is unobservable at every point, then nothing in the physics prefers one point's phase over another's, so the natural next move is to let each point choose its own. Promote the constant angle to a function $\alpha(x)$, and ask that the theory remain unchanged under

$$\psi(x) \to e^{i\alpha(x)}\psi(x), \qquad \bar\psi(x) \to e^{-i\alpha(x)}\bar\psi(x).$$

Test the Lagrangian against this transformation. The mass term survives, because its two phases cancel at the same point:

$$-m\,\bar\psi\psi \;\to\; -m\,e^{-i\alpha(x)}e^{i\alpha(x)}\,\bar\psi\psi = -m\,\bar\psi\psi .$$

The kinetic term does not. Its derivative acts on the phase, and differentiating a point-dependent phase leaves a gradient behind:

$$\partial_\mu\Big(e^{i\alpha(x)}\psi\Big) = e^{i\alpha(x)}\Big(\partial_\mu\psi + i(\partial_\mu\alpha)\,\psi\Big).$$

Substituting into the kinetic term therefore adds an unwanted piece,

$$\bar\psi\,i\hbar\gamma^\mu\partial_\mu\psi \;\to\; \bar\psi\,i\hbar\gamma^\mu\partial_\mu\psi \;-\; \hbar\,(\partial_\mu\alpha)\,\bar\psi\gamma^\mu\psi ,$$

so the local transformation fails: the Lagrangian gains a term proportional to $\partial_\mu\alpha$ and is no longer invariant.

The failure points at the fix. The unwanted term is a gradient of the phase, so cancel it with a field that shifts by that same gradient. Introduce a vector field $A_\mu$ that transforms as

$$A_\mu \;\to\; A_\mu - \frac{\hbar}{q}\,\partial_\mu\alpha ,$$

and package it with the ordinary derivative into the **covariant derivative**,

$$D_\mu = \partial_\mu + \frac{iq}{\hbar}A_\mu .$$

Under the combined transformation, $D_\mu\psi$ picks up the same phase as $\psi$ and nothing else,

$$D_\mu\psi \;\to\; e^{i\alpha(x)}\,D_\mu\psi ,$$

so replacing $\partial_\mu$ by $D_\mu$ restores the symmetry: $\bar\psi\gamma^\mu D_\mu\psi$ is invariant term by term, exactly as the global version was. The compensating field $A_\mu$ is not a third field — it is the photon field of the recap. Expanding $D_\mu$,

$$\bar\psi\,i\hbar\gamma^\mu D_\mu\psi \;=\; \bar\psi\,i\hbar\gamma^\mu\partial_\mu\psi \;-\; q\,\bar\psi\gamma^\mu\psi\,A_\mu ,$$

and the extra term is precisely the interaction term of the recap: the photon field $A_\mu$ coupled to the electron current $\bar\psi\gamma^\mu\psi$, with the charge $q$ setting the strength. Local gauge invariance therefore explains why the photon couples to charge: the field the symmetry demands is the photon field $A_\mu$ already in the theory, not a new one. The photon still needs a kinetic term of its own — the Maxwell term, whose gauge invariance is the subject of the next section.

## QED Lagrangian

The photon field $A_\mu$ has been forced into the theory, but it still needs a kinetic term of its own so that it can propagate. The natural choice is the Maxwell term, and it is the only choice consistent with the gauge symmetry. Under the shift $A_\mu \to A_\mu - \tfrac{\hbar}{q}\,\partial_\mu\alpha$, the field strength

$$F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$$

is unchanged, because the gradient parts cancel — $\partial_\mu\partial_\nu\alpha - \partial_\nu\partial_\mu\alpha = 0$, since mixed partial derivatives commute. The Maxwell term $-\tfrac14 F_{\mu\nu}F^{\mu\nu}$ is therefore gauge invariant, and it always was: the free photon Lagrangian of the recap already carried the symmetry that the electron's kinetic term demanded.

Assembling the pieces gives the QED Lagrangian. Replace the ordinary derivative in the Dirac Lagrangian by the covariant one, and add the photon's kinetic term:

$$\mathcal{L}_\text{QED} = -\tfrac14 F_{\mu\nu}F^{\mu\nu} \;+\; \bar\psi\left(i\hbar\gamma^\mu D_\mu - m\right)\psi, \qquad D_\mu = \partial_\mu + \frac{iq}{\hbar}A_\mu .$$

Expanding the covariant derivative shows the three pieces of the recap side by side,

$$\mathcal{L}_\text{QED} = -\tfrac14 F_{\mu\nu}F^{\mu\nu} \;+\; \bar\psi\left(i\hbar\gamma^\mu\partial_\mu - m\right)\psi \;-\; q\,\bar\psi\gamma^\mu\psi\,A_\mu :$$

the photon's kinetic term, the free electron, and the interaction that couples the two.

Nothing in this Lagrangian was put in by trial and error. A single demand — invariance under a local U(1) phase rotation — produced all of it: it forced the photon field $A_\mu$ into the electron's derivative, fixed its coupling to the current as $-q\bar\psi\gamma^\mu\psi\,A_\mu$, and selected the Maxwell term as the photon's kinetic energy. The same demand also explains a familiar fact. A mass term for the photon, $m^2 A_\mu A^\mu$, is not gauge invariant, so the gauge principle forbids it: the photon is massless because the U(1) symmetry that gives QED its photon leaves no room for a photon mass.

That is QED as a Lagrangian theory. The [next page](lagrangian-to-experiment.md) says where such a Lagrangian leads an experiment, and the pages after, [Perturbation Theory](perturbation-theory.md) and [Feynman Rules for QED](feynman-rules.md), read the scattering amplitudes out of this Lagrangian.
