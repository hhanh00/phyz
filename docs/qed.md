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

## Quantizing the Photon Field

The Feynman machinery of the pages ahead needs the photon's propagator, and propagators come from quantizing the free field, which the [Field Quantization page](field-quantization.md) did for the scalar and then for the spinor. The photon field cannot be quantized that way directly, because it is a gauge field: its components overcount the physics, and the overcounting must be removed before the field can be split into independent oscillators. The section does this in five steps. It works out what a free electromagnetic wave contains, shows why the canonical construction stalls on the photon, removes the redundancy by fixing the gauge, quantizes what remains, and computes the propagator from the result.

### What a free photon holds

What must a plane wave satisfy to represent a real, freely propagating electromagnetic field? Write the potential as

$$A^\mu(x) = \varepsilon^\mu e^{-ik\cdot x/\hbar}.$$

Here $k^\mu = (E_k, \mathbf k)$ describes its energy and momentum, while $\varepsilon^\mu$ gives the amplitudes of the four components of the potential. The exponential describes how the wave oscillates in space and time.

First, Maxwell's equation becomes an algebraic constraint. Differentiating the exponential multiplies it by $-ik_\mu/\hbar$, so the field strength is

$$F^{\mu\nu} = \frac{-i}{\hbar}\left(k^\mu \varepsilon^\nu - k^\nu \varepsilon^\mu\right)e^{-ik\cdot x/\hbar}.$$

Taking one more derivative and applying the free Maxwell equation, $\partial_\mu F^{\mu\nu} = 0$, gives

$$0 = -\frac{1}{\hbar^2}\left[k^2\varepsilon^\nu - k^\nu(k\cdot\varepsilon)\right]e^{-ik\cdot x/\hbar}.$$

Removing the common factors leaves

$$k^2\varepsilon^\nu = k^\nu(k\cdot\varepsilon),$$

where $k^2 = E_k^2 - |\mathbf k|^2$, using $c = 1$.

Second, if $k^2 \neq 0$, the potential produces no electromagnetic field. Dividing by $k^2$ gives

$$\varepsilon^\nu = Ck^\nu, \qquad C = \frac{k\cdot\varepsilon}{k^2}.$$

Substituting this back into the field strength gives[^commuting-components]

$$F^{\mu\nu} = \frac{-iC}{\hbar}(k^\mu k^\nu - k^\nu k^\mu)e^{-ik\cdot x/\hbar} = 0.$$

The potential may oscillate, but both $\mathbf E$ and $\mathbf B$ vanish. This is what *pure gauge* means here: a nonzero potential describing zero physical field.[^longitudinal] Consequently, a plane wave with a nonzero electromagnetic field must have

$$k^2 = 0 \quad\Longrightarrow\quad E_k = |\mathbf k|.$$

That is the energy–momentum relation for a massless particle.[^null-momentum]

Third, when $k^2 = 0$, Maxwell's equation also requires $k\cdot\varepsilon = 0$. The constraint becomes

$$0 = k^\nu(k\cdot\varepsilon).$$

For a nonzero wave momentum, at least one component of $k^\nu$ is nonzero, so the scalar $k\cdot\varepsilon$ must vanish. This is one constraint on the four components of $\varepsilon^\mu$, leaving three. It is called transversality, but at this stage it means four-dimensional orthogonality: it does not yet say that the spatial potential points sideways. For a wave travelling along $z$, it requires $\varepsilon^0 = \varepsilon^3$, rather than requiring both components to vanish. The gauge freedom will let us remove that remaining pair together.

The gauge freedom removes one more. A gauge transformation shifts $A_\mu$ by a gradient, and the gradient of the same plane wave is proportional to $k_\mu$, so the transformation acts on the polarization as

$$\varepsilon_\mu \;\to\; \varepsilon_\mu + \alpha\, k_\mu,$$

which changes nothing physical: $F_{\mu\nu}$ is unchanged by construction, and transversality survives because $k\cdot k = 0$. Two polarizations that differ by a multiple of $k_\mu$ describe the same photon in two descriptions.

The counting becomes concrete for a wave moving along the $z$ axis, $k^\mu \propto (1,0,0,1)$. Transversality reads $k\cdot\varepsilon = \varepsilon^0 - \varepsilon^3 = 0$[^transverse], so a transverse polarization has the form $(a, \varepsilon^1, \varepsilon^2, a)$: the two directions $(0,1,0,0)$ and $(0,0,1,0)$, plus the diagonal direction $(1,0,0,1)$ with any weight $a$. The diagonal direction is $k$ itself, which the paragraph above identified as pure gauge. Of the three transverse directions, one is gauge and two are physical:

$$\varepsilon^{(1)} = (0,1,0,0), \qquad \varepsilon^{(2)} = (0,0,1,0).$$

So the four components of $A_\mu$, minus one for the equation of motion and one for the gauge redundancy, leave two polarization states. Light has two polarizations because the photon's equation and its gauge symmetry each remove a component.

### Why the canonical construction stalls

The [Field Quantization construction](field-quantization.md#the-canonical-commutator) begins by pairing each field component with a conjugate momentum and imposing $[\hat\phi, \hat\pi] = i\hbar\,\delta^3$. For the photon the pairing fails at the first step. The conjugate momentum of $A_\mu$ follows from the Maxwell Lagrangian,

$$\pi^\mu = \frac{\partial\mathcal{L}}{\partial(\partial_0 A_\mu)} = -F^{0\mu},$$

and for the time component this is identically zero, $\pi^0 = -F^{00} = 0$, because $F$ is antisymmetric. The zero is structural, not small. Imposing the canonical commutator on $A_0$ would read $[\hat A_0,\, 0] = i\hbar\,\delta^3$, a contradiction. The physical content of the zero is that $A_0$ is not independent data: the $\nu = 0$ component of the free equation is Gauss's law, $\nabla\cdot\mathbf E = 0$, a constraint that ties $A_0$ to the other components instead of evolving it. A field whose components overcount the physics cannot be split into independent oscillators, and that split is the foundation the scalar construction stands on.

### Fixing the gauge

The repair is to spend the gauge freedom before quantizing, removing the overcounting at the classical level. The Lorenz condition[^lorenz] $\partial_\mu A^\mu = 0$ can always be imposed: under $A_\mu \to A_\mu + \partial_\mu\chi$ the divergence changes as $\partial\cdot A \to \partial\cdot A + \Box\chi$, so choosing $\chi$ to solve $\Box\chi = -\,\partial\cdot A$ reaches the condition. Some freedom survives, because any further $\chi$ with $\Box\chi = 0$ keeps it; that residue is precisely the plane-wave shift $\varepsilon \to \varepsilon + \alpha k$ of the first subsection.

Imposing the condition directly on the operators fails again, because the operator identity $\partial\cdot\hat A = 0$ is as incompatible with the canonical algebra as $\pi^0 = 0$ was. The working method enforces the condition through the Lagrangian instead, by adding a **gauge-fixing term**

$$\mathcal{L}_\text{gf} = -\tfrac{1}{2}\,(\partial_\mu A^\mu)^2 .$$

The term costs nothing physical, since gauge-invariant quantities — everything built from $F_{\mu\nu}$ — do not depend on it, and it vanishes for fields that obey the Lorenz condition. What it buys is decoupling. Expand the Maxwell term,

$$-\tfrac{1}{4}F_{\mu\nu}F^{\mu\nu} \;=\; -\tfrac{1}{2}(\partial_\mu A_\nu)(\partial^\mu A^\nu) \;+\; \tfrac{1}{2}(\partial_\mu A_\nu)(\partial^\nu A^\mu),$$

and integrate the last piece by parts. One pass writes $(\partial_\mu A_\nu)(\partial^\nu A^\mu) = \partial_\mu\big[A_\nu\,\partial^\nu A^\mu\big] - A_\nu\,\partial^\nu(\partial\cdot A)$, and a second pass moves the remaining derivative onto the divergence, $A_\nu\,\partial^\nu(\partial\cdot A) = \partial^\nu\big[A_\nu\,(\partial\cdot A)\big] - (\partial\cdot A)^2$. Up to the two boundary terms the result is

$$(\partial_\mu A_\nu)(\partial^\nu A^\mu) \;=\; (\partial\cdot A)^2 \quad \text{(up to total derivatives)},$$

so the gauge-fixing term cancels the second piece of the Maxwell term and the total Lagrangian collapses to

$$\mathcal{L}_\text{Maxwell} + \mathcal{L}_\text{gf} \;=\; -\tfrac{1}{2}\,(\partial_\mu A_\nu)(\partial^\mu A^\nu) \quad \text{(up to total derivatives)}.$$

Each component $A_\nu$ now enters as an independent massless scalar field: no mass term, because the gauge principle forbids one, and no coupling between components. The Euler–Lagrange equation of each component is the wave equation, $\Box A_\nu = 0$. This particular combination of Maxwell term plus gauge-fixing term is called **Feynman gauge**.

### Quantizing the gauge-fixed field

With the redundancy fixed away, the [Field Quantization](field-quantization.md) construction runs without obstruction. Expand the field on a basis of four polarization vectors per momentum: the two transverse polarizations $\varepsilon^{(1)}$, $\varepsilon^{(2)}$ of the first subsection, a timelike vector $\varepsilon^{(0)}$ with $\varepsilon^{(0)}\cdot\varepsilon^{(0)} = +1$ (for $k$ along $z$: $(1,0,0,0)$), and a longitudinal vector $\varepsilon^{(3)}$ (for $k$ along $z$: $(0,0,0,1)$). The promoted field reads

$$\hat A_\mu(x) = \int \frac{d^3k}{(2\pi\hbar)^3}\,\frac{1}{\sqrt{2E_k}} \sum_{\lambda=0}^{3}\left[\hat c_\lambda(k)\,\varepsilon_\mu^{(\lambda)}(k)\,e^{-ik\cdot x/\hbar} \;+\; \hat c_\lambda^\dagger(k)\,\varepsilon_\mu^{(\lambda)*}(k)\,e^{+ik\cdot x/\hbar}\right], \qquad E_k = |\mathbf k|.$$

The ladder algebra comes out as four copies of the scalar algebra, one per polarization, but with the metric signature attached. Write $\eta_\lambda$ for the polarization's scalar product with itself, $\eta_0 = +1$ for the timelike vector and $\eta_{1,2,3} = -1$ for the spacelike ones; then

$$[\hat c_\lambda(k), \hat c_{\lambda'}^\dagger(k')] = -\eta_\lambda\;\delta_{\lambda\lambda'}\;\delta^3(k-k'),$$

so the three spacelike families carry the standard $[\hat a, \hat a^\dagger] = 1$ algebra and the timelike family carries it with a minus sign. The sign is inherited from the kinetic term: for the time component the combination $-\tfrac12(\partial_\mu A_\nu)(\partial^\mu A^\nu)$ gives $-\tfrac12(\partial A_0)^2$, the negative of a scalar's kinetic term, because $g^{00} = +1$ while $g^{ii} = -1$, and that sign flows through the construction into the algebra. Substituting the expansion into the Hamiltonian, by the same orthogonality steps as the scalar case, gives per momentum

$$\hat H = \int \frac{d^3k}{(2\pi\hbar)^3}\;E_k\left(\hat c_1^\dagger \hat c_1 + \hat c_2^\dagger \hat c_2 + \hat c_3^\dagger \hat c_3 - \hat c_0^\dagger \hat c_0\right) + \text{const.}$$

Two families are healthy oscillators, and they are the transverse photons. The timelike and longitudinal families enter with opposite signs, and they are the modes the gauge freedom was supposed to remove: quantizing all four components has reintroduced them as bookkeeping. The definition of a physical state locks the pair together so that their contributions cancel in every observable[^gupta], and on the physical states the energy comes from the two transverse families alone. A photon state is therefore specified by a momentum $\mathbf k$ and a choice of $\varepsilon^{(1)}$ or $\varepsilon^{(2)}$, which matches the two-polarization count of the first subsection, and an external photon line in a diagram carries one of those two polarization vectors.

### The propagator

The contraction $\langle 0\rvert T\hat A_\mu(x)\hat A_\nu(y)\lvert 0\rangle$ computes mode by mode, exactly as the scalar contraction did. Each spacelike mode is a massless scalar and contributes the scalar propagator with $m = 0$; the timelike mode contributes the same expression with its minus sign. In momentum space the mode-by-mode sum reads

$$\sum_{\lambda=0}^{3}\left(-\eta_\lambda\right)\,\varepsilon_\mu^{(\lambda)}\,\varepsilon_\nu^{(\lambda)}\;\frac{i}{k^2 + i\epsilon},$$

and the polarization part of the sum is the completeness relation of the basis. The four vectors $\varepsilon^{(\lambda)}$ span the component space, and summing their outer products with the weights $\eta_\lambda$ reconstructs the metric,

$$\sum_{\lambda=0}^{3}\eta_\lambda\;\varepsilon_\mu^{(\lambda)}\,\varepsilon_\nu^{(\lambda)} = g_{\mu\nu},$$

which can be checked component by component in the $k$-along-$z$ basis. The contraction is therefore

$$\frac{-i\,g_{\mu\nu}}{k^2 + i\epsilon}$$

in momentum space, and this is the photon propagator. No mass term appears in the denominator because the photon is massless, so the only pole sits at $k^2 = 0$. The tensor $g_{\mu\nu}$ carries the vector structure, one index for each end of the line, and its sign pattern records the same timelike bookkeeping: an internal photon line effectively sums over all four polarization modes, with the unphysical pair canceling in every gauge-invariant result, which is why diagram calculations may use $-g_{\mu\nu}$ as the polarization sum on internal lines. This is the rule the [Feynman Rules page](feynman-rules.md) needs, and with it the free-field input of the QED rulebook is complete: the electron propagator from the spinor construction, the photon propagator from this one, and the interaction term supplying the vertex.

That is QED as a Lagrangian theory, with both of its fields quantized. The [next page](lagrangian-to-experiment.md) says where such a Lagrangian leads an experiment, and the pages after, [Perturbation Theory](perturbation-theory.md) and [Feynman Rules for QED](feynman-rules.md), read the scattering amplitudes out of this Lagrangian.

[^gupta]: The covariant statement is the **Gupta–Bleuler condition**: the Lorenz condition is imposed on physical states, using only the annihilation half of the operator, as $\big(\partial_\mu\hat A^\mu\big)^{(+)}\,\lvert\text{phys}\rangle = 0$. For $k$ along $z$ it pairs the timelike and longitudinal modes as $\big(\hat c_0 - \hat c_3\big)\lvert\text{phys}\rangle = 0$, so the two operators act identically on every physical state, and their Hamiltonian terms $\hat c_3^\dagger\hat c_3 - \hat c_0^\dagger\hat c_0$ have equal and opposite expectation values there. The construction is standard quantum field theory; this site uses only its conclusion, that the unphysical pair cancels in every observable, because the diagram rules build that cancellation into the $-g_{\mu\nu}$ polarization sum of internal lines.

[^lorenz]: The condition is named for Ludvig Lorenz, who wrote it down in 1867, before Hendrik Lorentz's work on the coordinate transformations; the spelling with a "z" keeps the two physicists apart.

[^longitudinal]: The vanishing is index bookkeeping, not dynamics. $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ is antisymmetric by construction, so it only picks up the antisymmetric part of anything it meets. When $\varepsilon_\mu \propto k_\mu$ the only tensor available is $k_\mu k_\nu$, which is symmetric under $\mu \leftrightarrow \nu$, and the antisymmetric part of a symmetric tensor is zero. Since $F_{\mu\nu}$ holds the physical $\mathbf E$ and $\mathbf B$, a polarization along $k$ has $\mathbf E = \mathbf B = 0$. Such a potential is a pure gradient, $A_\mu = \partial_\mu\chi$ with $\chi \propto e^{-ik\cdot x/\hbar}$, and $F_{\mu\nu}$ annihilates a gradient because $\partial_\mu\partial_\nu\chi - \partial_\nu\partial_\mu\chi = 0$.

[^transverse]: The condition $k\cdot\varepsilon = 0$ is the covariant statement of transversality, written for the 4-potential $A^\mu = (\phi, \mathbf A)$, and it involves the scalar potential's component $\varepsilon^0$. The familiar 3D form, $\mathbf k\cdot\mathbf E = 0$ giving $E_z = 0$, is a statement about the fields $\mathbf E$ and $\mathbf B$, which have no time component — which is why the two versions look different. For the lightlike $k = (1,0,0,1)$ the dot product $k\cdot\varepsilon = k^0\varepsilon^0 - k^3\varepsilon^3$ reduces to $\varepsilon^0 = \varepsilon^3$, and the direction that satisfies it — the diagonal $(1,0,0,1)$ — is exactly the pure-gauge mode with $F_{\mu\nu} = 0$. The two statements agree: the physical polarizations $(0,1,0,0)$ and $(0,0,1,0)$ have zero $z$-component in the potential and in the field alike.

[^null-momentum]: $k^2 = 0$ does not mean $k^\mu = 0$: this is a Minkowski square, $k^2 = E_k^2 - |\mathbf k|^2$, whose time and space contributions can cancel. For example, a photon travelling along $z$ has $k^\mu = (E_k,0,0,E_k)$, so $k^2 = E_k^2 - E_k^2 = 0$ even for nonzero energy. Unlike a Euclidean squared length, a zero Minkowski square does not force the vector to vanish. A nonzero vector with zero Minkowski square is called **null** or **lightlike**.

[^commuting-components]: Each component $k^\mu$ is an ordinary number, so multiplication commutes: $k^\mu k^\nu = k^\nu k^\mu$. Their difference is therefore zero for every choice of $\mu$ and $\nu$; the indices only select components.
