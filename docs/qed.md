# Quantum Electrodynamics

Two electrons that pass near each other come out moving in new directions. In quantum electrodynamics (QED) they scatter by exchanging a photon: one electron emits it and the other absorbs it, and neither the emission nor the absorption is seen directly. QED is the theory of the electron field, the photon field, and this coupling between them.

```feynman
\begin{tikzpicture}
\begin{feynman}
\vertex (i1) at (-2.4,1.4) {$e^-$};
\vertex (a) at (0,1.4);
\vertex (f1) at (2.4,1.4) {$e^-$};
\vertex (i2) at (-2.4,-1.4) {$e^-$};
\vertex (b) at (0,-1.4);
\vertex (f2) at (2.4,-1.4) {$e^-$};
\diagram* {
(i1) -- [fermion] (a) -- [fermion] (f1),
(i2) -- [fermion] (b) -- [fermion] (f2),
(a) -- [photon, edge label={$\gamma$}] (b),
};
\end{feynman}
\end{tikzpicture}
```

*Two electrons scatter by exchanging a photon. The exchanged photon is internal: it is created and absorbed inside the process and never reaches a detector. Predicting how often the electrons deflect through a given angle needs a numerical factor for each vertex where the photon meets an electron line, and a factor for the internal photon line.*

To turn a diagram like this into a number, we need a factor for each vertex and a factor for the internal photon line. This chapter derives the QED interaction and quantizes the photon field; [Perturbation Theory](perturbation-theory.md) extracts the propagator and assembles the diagram factors.

1. **The vertex factor** comes from an interaction term in the QED Lagrangian. Most of the chapter works out where that term comes from and why it has only one possible form.
2. **The photon field** supplies the internal-line factor. Quantizing it carries a complication the electron field did not: four potential components describe only two physical photons. The propagator is extracted later, after time ordering and contractions have been introduced.

A third QED building block, the propagator for an internal *electron* line, already came out of [Field Quantization](field-quantization.md#the-spinor-field). It appears in processes such as Compton scattering rather than the exchange drawn above. The [Perturbation Theory](perturbation-theory.md) and [Feynman Rules](feynman-rules.md) pages assemble all three factors into amplitudes.

We use natural units, $\hbar=c=1$, and metric $g_{\mu\nu}=\operatorname{diag}(1,-1,-1,-1)$, so $k^2 = E_k^2 - |\mathbf k|^2$.

The foundational distinction between spacetime labels and field-value spaces
appears in [Quantum Field Theory: Fields and Quanta §Spacetime, components,
and value spaces](qft.md#spacetime-components-and-value-spaces). QED brings
several of those objects together, so the following recap collects the
notation used most often in this chapter.

<details>
<summary>Expand the QED notation</summary>

| Symbol | Meaning | Mathematical role |
| --- | --- | --- |
| $x^\mu$ | spacetime point | $x\in\mathbb R^{1,3}$, with $\mu=0,1,2,3$ |
| $\psi(x)$ | electron field | four-component Dirac spinor, valued in $\mathbb C^4$ |
| $\bar\psi=\psi^\dagger\gamma^0$ | Dirac adjoint | makes combinations such as $\bar\psi\psi$ Lorentz covariant |
| $\gamma^\mu$ | gamma matrices | act on spinor components and carry a Lorentz index |
| $A_\mu(x)$ | electromagnetic potential | Lorentz covector field; its four components are not four photons |
| $F_{\mu\nu}$ | electromagnetic field strength | antisymmetric tensor, $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$ |
| $D_\mu$ | covariant derivative | $D_\mu=\partial_\mu+iqA_\mu$ |
| $j^\mu$ | electric current | four-vector, $j^\mu=q\bar\psi\gamma^\mu\psi$ |
| $\alpha(x)$, $\chi(x)$ | gauge functions | real-valued functions on spacetime |
| $q$, $m$ | charge and mass | constants; $q$ sets the interaction strength |

Repeated Lorentz indices are summed, so

$$\bar\psi\gamma^\mu D_\mu\psi
 =\sum_{\mu=0}^{3}\bar\psi\gamma^\mu D_\mu\psi.$$

The position-space variable $x$ labels where a field is evaluated. The
momentum-space variable $k^\mu$ labels a Fourier mode or an internal-line
momentum, and $\varepsilon^\mu$ labels a polarization four-vector. A Lorentz
index such as $\mu$ is different from a spinor component index: $\gamma^\mu$
is a $4\times4$ matrix for each value of $\mu$.

After quantization, hats distinguish operators when needed, for example
$\hat\psi(x)$ and $\hat A_\mu(x)$. The fields remain operator-valued
distributions; the indices still refer to the same Lorentz and spinor spaces.

</details>

The route to the interaction term runs through symmetry:

1. **Assemble the free pieces.** The Dirac and Maxwell Lagrangians describe the electron and photon fields propagating on their own.
2. **Find the interaction.** Requiring the theory to be unchanged by a local phase convention for the electron field forces a coupling to the photon potential.
3. **Quantize the photon.** The canonical construction needs a gauge-fixing step and a condition that picks out the physical states.
4. **Extract the propagator.** The quantized field supplies the factor for an internal photon line.

## Recap of the Lagrangians

We begin with the two free Lagrangians from [Action and Lagrangians](qft-action.md).

The Dirac Lagrangian describes the free electron field:

$$\mathcal{L}_\text{Dirac} = \bar\psi\left(i\gamma^\mu\partial_\mu - m\right)\psi.$$

Here $\psi$ is the electron's spinor field and $\bar\psi=\psi^\dagger\gamma^0$ is its Dirac adjoint. The derivative term describes propagation, and $-m\bar\psi\psi$ is the mass term. Applying the Euler–Lagrange equation gives the Dirac equation.

The Maxwell Lagrangian describes the free photon field. The potential $A_\mu$ has four components, and its derivatives form the electromagnetic field strength:

$$\mathcal{L}_\text{Maxwell} = -\tfrac14 F_{\mu\nu}F^{\mu\nu}, \qquad F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu.$$

Varying $A_\mu$ gives Maxwell's equations in free space, $\partial_\mu F^{\mu\nu}=0$.

Adding these two Lagrangians describes fields that propagate independently, with nothing passing between them. Electromagnetic scattering needs an interaction term as well. The next two sections show that requiring the electron Lagrangian to respect a local phase symmetry forces that term into one particular shape, the **minimal coupling** used in [The Dirac Equation §1](dirac-equation.md#_1-spin).

## U(1) Global Symmetry

Multiplying the electron field by a constant phase changes no prediction. Take

$$\psi \to e^{i\alpha}\psi, \qquad \bar\psi \to e^{-i\alpha}\bar\psi,$$

with the same constant $\alpha$ everywhere. The probability density from [First Quantization](first-quantization.md), $P = \psi^*\psi$, is unchanged because the phase and its conjugate cancel. Relative phases between parts of a superposition still matter for interference; the transformation here rotates the whole field by one angle.

Every term in the free Dirac Lagrangian contains one $\psi$ and one $\bar\psi$. In the mass term the two phases cancel directly, $e^{-i\alpha}e^{i\alpha}=1$. In the kinetic term the constant phase passes through the derivative and then cancels the same way. The Lagrangian is therefore unchanged. A transformation that leaves the action unchanged is a **symmetry**, and this one is **global** because a single $\alpha$ applies across all of spacetime.

The symmetry also implies charge conservation. Noether's theorem attaches a conserved current to each continuous symmetry of the action, and for the phase transformation that current is

$$j^\mu = q\,\bar\psi\gamma^\mu\psi, \qquad \partial_\mu j^\mu = 0.$$

Its time component is the charge density and its spatial components describe charge flow. Integrating the density over all space gives the total electric charge, and the continuity equation says that charge moving between regions is never created or destroyed.

The phases $e^{i\alpha}$ form the group **U(1)**. Each is a unitary $1\times1$ matrix, equivalently a complex number of unit magnitude, and as $\alpha$ varies these numbers trace out the unit circle.

## Local Gauge Symmetry U(1)

The phase of the electron field is not measurable on its own, so it is natural to ask that the theory not depend on this convention even when it is chosen separately at each point rather than once for all of spacetime. Replace the constant $\alpha$ by a function $\alpha(x)$:

$$\psi(x) \to e^{i\alpha(x)}\psi(x), \qquad \bar\psi(x) \to e^{-i\alpha(x)}\bar\psi(x).$$

The free Dirac Lagrangian does not survive this stronger demand. The mass term still cancels, because its two phase factors sit at the same point:

$$-m\,\bar\psi\psi \;\to\; -m\,e^{-i\alpha(x)}e^{i\alpha(x)}\,\bar\psi\psi = -m\,\bar\psi\psi .$$

The kinetic term does not. The derivative now acts on the phase as well as on $\psi$, and the product rule leaves an extra term proportional to $(\partial_\mu\alpha)\,\bar\psi\gamma^\mu\psi$, which does not vanish for a general $\alpha(x)$.

<details>
<summary>How the derivative breaks local invariance</summary>

Apply the product rule to the phase-transformed field:

$$\partial_\mu\Big(e^{i\alpha(x)}\psi\Big) = e^{i\alpha(x)}\Big(\partial_\mu\psi + i(\partial_\mu\alpha)\,\psi\Big).$$

Substituting into the kinetic term gives

$$\bar\psi\,i\gamma^\mu\partial_\mu\psi \;\to\; \bar\psi\,i\gamma^\mu\partial_\mu\psi \;-\; (\partial_\mu\alpha)\,\bar\psi\gamma^\mu\psi .$$

The last term does not vanish for a general $\alpha(x)$, so the free Dirac Lagrangian is not invariant under local phase changes.

</details>

To cancel the extra term, introduce a field that shifts under the same transformation. Give the vector potential the rule

$$A_\mu \;\to\; A_\mu - \frac1q\,\partial_\mu\alpha,$$

and fold it into the derivative:

$$D_\mu = \partial_\mu + iq\,A_\mu .$$

The shift in $A_\mu$ places $-i\partial_\mu\alpha$ inside $D_\mu$, which cancels the $+i\partial_\mu\alpha$ from differentiating the phase. What remains is

$$D_\mu\psi \;\to\; e^{i\alpha(x)}\,D_\mu\psi ,$$

so $D_\mu\psi$ carries the same phase as $\psi$ itself. That is why $D_\mu$ is called the **covariant derivative**. Multiplying by $\bar\psi$ removes the phase, and the kinetic term built from $D_\mu$ is locally invariant.

Expanding it,

$$\bar\psi\,i\gamma^\mu D_\mu\psi \;=\; \bar\psi\,i\gamma^\mu\partial_\mu\psi \;-\; q\,\bar\psi\gamma^\mu\psi\,A_\mu ,$$

produces exactly one interaction term, coupling the electron current $j^\mu = q\bar\psi\gamma^\mu\psi$ to the potential $A_\mu$. Local U(1) invariance fixes its form. The charge $q$ sets its strength, and the symmetry argument does not predict the numerical value.

The photon potential now appears in the electron's dynamics. The next section adds a kinetic term for $A_\mu$ so that electromagnetic disturbances can propagate on their own.

![A global phase rotation uses one angle everywhere. A local rotation has a position-dependent angle, whose derivative requires a compensating transformation of the gauge potential.](./manim/global-local-phase.png)

*A global phase rotation uses one angle everywhere. A local rotation has a position-dependent angle, whose derivative requires a compensating transformation of the gauge potential.*

## QED Lagrangian

The potential $A_\mu$ now belongs to the same locally gauge-invariant theory as the electron field. Its kinetic term must therefore be the **same kinetic term** for two gauge-equivalent potentials. We do **not** modify the kinetic term itself: we transform $A_\mu$, then check that the existing Maxwell term is unchanged. The field strength here is the **same** $F_{\mu\nu}$ introduced in the free Maxwell theory. Write

$$A'_\mu=A_\mu-\frac1q\partial_\mu\alpha.$$

Substitute this transformed potential into the same definition:

$$F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$$

$$\begin{aligned}
F'_{\mu\nu}
&=\partial_\mu A'_\nu-\partial_\nu A'_\mu\\
&=F_{\mu\nu}-\frac1q\left(\partial_\mu\partial_\nu\alpha-\partial_\nu\partial_\mu\alpha\right)\\
&=F_{\mu\nu}.
\end{aligned}$$

The added piece vanishes because mixed partial derivatives commute. Thus the transformation changes the potential's description but not the electromagnetic field strength.

<details>
<summary>Zero field strength does not require a constant potential</summary>

Locally, $F_{\mu\nu}=0$ means that the potential can be a pure gradient,
$A_\mu=\partial_\mu\chi$, not necessarily a constant. For example,
$\chi=t^2$ gives $A_\mu=(2t,0,0,0)$ while

$$F_{\mu\nu}=\partial_\mu\partial_\nu\chi-
\partial_\nu\partial_\mu\chi=0.$$

</details>

The Maxwell term $-\tfrac14F_{\mu\nu}F^{\mu\nu}$ is therefore gauge invariant. It is the standard Lorentz-invariant term quadratic in the field strength. Gauge symmetry permits additional higher-order terms in an effective theory, so it constrains the Lagrangian rather than fixing it uniquely.

Combining the photon term with the covariant Dirac term,

$$\mathcal{L}_\text{QED} = -\tfrac14 F_{\mu\nu}F^{\mu\nu} \;+\; \bar\psi\left(i\gamma^\mu D_\mu - m\right)\psi, \qquad D_\mu = \partial_\mu + iq\,A_\mu .$$

Expanding the covariant derivative separates the three contributions:

$$\mathcal{L}_\text{QED} = -\tfrac14 F_{\mu\nu}F^{\mu\nu} \;+\; \bar\psi\left(i\gamma^\mu\partial_\mu - m\right)\psi \;-\; q\,\bar\psi\gamma^\mu\psi\,A_\mu .$$

They describe photon propagation, free electron propagation, and the electron–photon interaction.

The interaction term is the source of the vertex factor promised in the introduction. Stripping the three fields off $-q\bar\psi\gamma^\mu\psi A_\mu$ and keeping the factor of $i$ from the S-matrix expansion leaves

$$-iq\gamma^\mu,$$

the number attached to each point where a photon line meets an electron line. The [Feynman Rules page](feynman-rules.md) derives this in full.

A direct photon mass term proportional to $m_\gamma^2 A_\mu A^\mu$ is not gauge invariant, because $A_\mu A^\mu$ changes under the gradient shift. An unbroken U(1) gauge symmetry therefore forbids it, and the photon we quantize next is massless.

## Quantizing the Photon Field

The photon propagator is the factor for an internal photon line. The [Field Quantization page](field-quantization.md) built propagators by expanding a free field into modes and treating each mode as an oscillator. The photon follows the same route with one extra step: the four components of $A_\mu$ carry only two physical polarizations, and the construction has to remove the other two.

On a first read, take two results from this section and move on. The photon has two physical polarizations, and its propagator in Feynman gauge is

$$D_{\mu\nu}(k)=\frac{-ig_{\mu\nu}}{k^2+i\epsilon}.$$

The rest of the section works through the steps needed to reach it.

The plan is to make all four components easy to quantize, then restrict the quantum states so that only the two physical polarizations survive. We first see where the two come from, then why the direct canonical construction stalls.

### Counting a free photon's polarizations

Write the potential as a single plane wave,

$$A^\mu(x) = \varepsilon^\mu e^{-ik\cdot x},$$

where $k^\mu = (E_k, \mathbf k)$ sets the energy and momentum and the polarization vector $\varepsilon^\mu$ sets the amplitude of each component of the potential. A complex wave keeps the algebra short; its real part is the physical classical field.

Putting this wave into the free Maxwell equation $\partial_\mu F^{\mu\nu}=0$ leaves one condition on the momentum and polarization,

$$k^2\varepsilon^\nu=k^\nu(k\cdot\varepsilon). \tag{1}$$

It has two consequences. First, a wave that carries a nonzero electromagnetic field must have $k^2=0$, the massless energy–momentum relation $E_k = |\mathbf k|$, because a polarization proportional to $k$ produces a vanishing field strength. Such a potential oscillates without any $\mathbf E$ or $\mathbf B$ and is called **pure gauge**. Second, with $k^2=0$ the condition becomes $k\cdot\varepsilon=0$, which ties the four amplitude components together and removes one of them.

<details>
<summary>Deriving the condition, and the pure-gauge case</summary>

Differentiating the exponential brings down $-ik_\mu$, so the field strength is

$$F^{\mu\nu} = -i\left(k^\mu\varepsilon^\nu-k^\nu\varepsilon^\mu\right)e^{-ik\cdot x}.$$

Now apply the free Maxwell equation, $\partial_\mu F^{\mu\nu}=0$. Another derivative brings down another momentum factor. After removing the common exponential and numerical factors, we get

$$k^2\varepsilon^\nu=k^\nu(k\cdot\varepsilon). \tag{1}$$

This equation specifies which polarizations and momenta can describe a free electromagnetic wave.

Suppose instead that $k^2\ne0$. Dividing equation (1) by $k^2$ gives

$$\varepsilon^\nu=Ck^\nu, \qquad C=\frac{k\cdot\varepsilon}{k^2}.$$

But a polarization proportional to $k$ makes the field strength vanish:

$$F^{\mu\nu}\propto C\left(k^\mu k^\nu-k^\nu k^\mu\right)=0. \tag{2}$$

The components of $k$ are ordinary numbers, so the two products are equal. The potential can oscillate while producing no $\mathbf E$ or $\mathbf B$. We call such a potential **pure gauge**.

For a wave with a nonzero electromagnetic field, we therefore need

$$k^2=0 \quad\Longrightarrow\quad E_k=|\mathbf k|.$$

This is the massless energy–momentum relation. A zero Minkowski square does not mean zero momentum: $k^\mu=(E_k,0,0,E_k)$ has $k^2=E_k^2-E_k^2=0$ even when $E_k$ is nonzero.

Substituting $k^2=0$ into equation (1) leaves

$$0=k^\nu(k\cdot\varepsilon). \tag{3}$$

For nonzero $k$, this requires $k\cdot\varepsilon=0$. One equation on four components leaves three independent amplitudes.

</details>

Gauge freedom removes one more amplitude. A gauge transformation shifts the potential by a gradient,

$$A_\mu\longrightarrow A_\mu+\partial_\mu\chi,$$

which leaves $F_{\mu\nu}$ unchanged because the extra term is $\partial_\mu\partial_\nu\chi-\partial_\nu\partial_\mu\chi=0$. For a gauge function with the same plane-wave dependence, the gradient is proportional to $k_\mu$, so the polarization shifts as $\varepsilon^\mu\to\varepsilon^\mu+\alpha k^\mu$. Choosing $\alpha$ appropriately removes the remaining non-transverse amplitude. Only the two directions perpendicular to the motion remain as independent physical polarizations:

$$\varepsilon^{(1)}=(0,1,0,0), \qquad \varepsilon^{(2)}=(0,0,1,0).$$

For a free photon, the count is therefore **four potential components, minus one Maxwell constraint, minus one gauge freedom, leaving two physical polarizations**.

<details>
<summary>Removing the non-transverse amplitudes</summary>

For a wave travelling along $z$, take $k^\mu=(E_k,0,0,E_k)$. The constraint $k\cdot\varepsilon=0$ reads

$$k\cdot\varepsilon=E_k(\varepsilon^0-\varepsilon^3)=0,$$

so the polarization has the form

$$\varepsilon^\mu=(a,\varepsilon^1,\varepsilon^2,a).$$

This is four-dimensional **transversality**. At this stage it ties the time and $z$ components together; it does not require them to vanish.

For a plane-wave gauge function, the polarization changes as

$$\varepsilon^\mu\longrightarrow\varepsilon^\mu+\alpha k^\mu. \tag{4}$$

Choose $\alpha=-a/E_k$. This removes the time and $z$ components together:

$$(a,\varepsilon^1,\varepsilon^2,a)\longrightarrow(0,\varepsilon^1,\varepsilon^2,0).$$

The electromagnetic field stays the same. Only the two transverse directions remain.

</details>

![A photon moving along z: the Maxwell constraint ties the time and z components together, and a gauge transformation removes that shared component, leaving two transverse polarizations.](./manim/photon-polarizations.png)

*A photon moving along z: the Maxwell constraint ties the time and z components together, and a gauge transformation removes that shared component, leaving two transverse polarizations.*

### Why the canonical construction stalls

Canonical quantization pairs each field with a conjugate momentum. For each component of the potential, calculate

$$\pi^\mu=\frac{\partial\mathcal L}{\partial(\partial_0 A_\mu)} = -F^{0\mu}.$$

The spatial components come out as $\pi^i=E^i$. The time component does not: antisymmetry forces $F^{00}=0$, so

$$\pi^0=0.$$

The same gap shows up directly in the Lagrangian, where $\dot A_0$ never appears, because the time derivatives in $F_{\mu\nu}$ act only on the spatial components of the potential.

A vanishing conjugate momentum blocks the usual canonical commutator. The standard relation for $A_0$ would set the right-hand delta function equal to zero, which cannot hold. The vanishing momentum instead marks $A_0$ as a constrained variable. Its Maxwell equation is Gauss's law, $\nabla\cdot\mathbf E=0$, a condition on the electric field at one instant with no time derivative to carry it to the next. In the Hamiltonian description, $A_0$ enforces that constraint.

Constrained systems can still be quantized. We use a method that keeps Lorentz covariance visible: add a gauge-fixing term that gives all four components a nonzero conjugate momentum, quantize, then select the physical states afterward.

### Fixing the gauge

The gauge freedom lets many potentials describe the same $\mathbf E$ and $\mathbf B$. A useful choice is the **Lorenz condition**,[^lorenz]

$$\partial_\mu A^\mu=0.$$

The contraction makes this condition Lorentz covariant: it has the same form in every Lorentz frame.

To see how we can reach it, apply a gauge transformation. The divergence changes as

$$\partial\cdot A\longrightarrow\partial\cdot A+\Box\chi, \qquad \Box=\partial_t^2-\nabla^2.$$

Choosing $\chi$ to solve

$$\Box\chi=-\partial\cdot A$$

therefore gives a potential satisfying the Lorenz condition, with suitable boundary conditions in the flat spacetime setting used here. Some freedom remains: a further transformation with $\Box\chi=0$ preserves the condition. For plane waves, this includes the shift along $k$ that we used to remove the amplitude $a$.

![Equivalent potentials belong to one gauge orbit and produce the same electromagnetic field. The Lorenz condition still permits residual gauge transformations.](./manim/gauge-descriptions.png)

*Equivalent potentials belong to one gauge orbit and produce the same electromagnetic field. The Lorenz condition still permits residual gauge transformations.*

In the quantum theory, this cannot become an exact identity between independent canonical field operators. The divergence contains $\dot{\hat A}^0$, which will be related to the momentum of $\hat A_0$. Setting that divergence identically to zero conflicts with the canonical commutator.[^operator-lorenz] We will instead impose a weaker condition on physical states.

The gauge-fixing term is not unique. A Lorentz-covariant family is

$$\mathcal L_\text{gf}=-\frac{1}{2\xi}(\partial_\mu A^\mu)^2.$$

Different values of $\xi$ give different intermediate propagators and
different treatments of the unphysical gauge directions. We choose
$\xi=1$, called **Feynman gauge**, because it makes the four components
decouple and gives the simplest canonical quantization. This is a choice of
formalism, not a new physical interaction.

For this choice, to make the canonical construction possible, add

$$\mathcal L_\text{gf}=-\frac12(\partial_\mu A^\mu)^2.$$

Since

$$\partial\cdot A=\dot A^0+\nabla\cdot\mathbf A,$$

the added term contains $-\tfrac12(\dot A^0)^2$. The missing velocity now appears, and the momentum becomes

$$\pi^0=-\partial\cdot A.$$

We have made all four components dynamical. This enlarges the space of solutions we quantize, so **adding the term and selecting physical states must go together**. The fact that the term vanishes on Lorenz-obeying fields is not, by itself, a proof that the quantum predictions stay the same. The Gupta–Bleuler condition below removes the extra gauge-sector states; equivalently, in other quantization formalisms, Ward identities or BRST symmetry ensure that gauge-invariant observables do not depend on $\xi$.

An arbitrary extra term would change the physical equations and could change
the predictions. Gauge fixing is special because the original Maxwell action
is constant along gauge orbits: all potentials $A_\mu+\partial_\mu\chi$ in
one orbit describe the same physical field. The gauge-fixing term changes
which representative is selected and adds motion in the redundant directions,
but it does not remove the physical gauge-equivalence class. In a path
integral, it changes the weighting of descriptions within each orbit; the
physical-state restriction (or, in another formalism, the corresponding
gauge-fixing determinant/BRST construction) removes that artificial change
from gauge-invariant predictions.

The added term also decouples the components: inside the action, the component-mixing part of the Maxwell term cancels against the gauge-fixing term after two integrations by parts. The equivalent Lagrangian is

$$\boxed{\mathcal L=-\frac12(\partial_\mu A_\nu)(\partial^\mu A^\nu).}$$

For this form of the Lagrangian, the canonical momenta are

$$\pi^\nu=-\partial^0 A^\nu, \qquad \pi^0=-\dot A^0.$$

The last expression differs from the momentum before integration by parts because changing the boundary terms can change the canonical momenta. Both Lagrangians give the same bulk equations of motion.

Each component now obeys a massless wave equation,

$$\Box A_\nu=0.$$

This choice gives four decoupled wave equations, which we can quantize using the oscillator construction. We still need to recover the two-polarization physical state space.

<details>
<summary>Decoupling the components</summary>

Expand the Maxwell term:

$$\mathcal L_\text{Maxwell}=-\frac12(\partial_\mu A_\nu)(\partial^\mu A^\nu)+\frac12(\partial_\mu A_\nu)(\partial^\nu A^\mu).$$

The second term mixes components. Inside the action, integrate it by parts twice:

$$\int d^4x\,(\partial_\mu A_\nu)(\partial^\nu A^\mu)
=-\int d^4x\,A_\nu\partial^\nu(\partial\cdot A)
=\int d^4x\,(\partial\cdot A)^2,$$

where we have dropped boundary terms under the usual boundary assumptions. The gauge-fixing term cancels this contribution, leaving the Lagrangian stated above.

</details>

### Quantizing the gauge-fixed field

With the components decoupled, expand the field into four families of modes. For momentum along $z$, choose the polarization basis

$$\varepsilon^{(0)}=(1,0,0,0), \qquad \varepsilon^{(1)}=(0,1,0,0),$$

$$\varepsilon^{(2)}=(0,0,1,0), \qquad \varepsilon^{(3)}=(0,0,0,1).$$

The labels $1$ and $2$ are the transverse directions. The label $0$ is timelike, and $3$ is longitudinal, pointing along the spatial momentum. Promote each mode amplitude to an annihilation operator and its complex conjugate to a creation operator:

<details>
<summary>Example of the extra formal modes</summary>

For momentum along $z$, the gauge-fixed equation $\Box A^\mu=0$ allows, as
formal plane-wave solutions,

$$A^\mu_{(0)}(x)=(1,0,0,0)e^{-ik\cdot x},\qquad
A^\mu_{(3)}(x)=(0,0,0,1)e^{-ik\cdot x}.$$

They lead to formal one-quantum states

$$\hat c_0^\dagger(k)|0\rangle,\qquad
\hat c_3^\dagger(k)|0\rangle.$$

These are not physical photon states. The time-like and longitudinal modes
are included so the four-component field can be quantized; the
Gupta–Bleuler condition below removes their gauge-dependent combinations.
The transverse states $\hat c_1^\dagger(k)|0\rangle$ and
$\hat c_2^\dagger(k)|0\rangle$ satisfy the physical condition and remain.

</details>

$$\hat A_\mu(x)=\int\frac{d^3k}{(2\pi)^3}\frac{1}{\sqrt{2E_k}}\sum_{\lambda=0}^3
\left[\hat c_\lambda(k)\varepsilon_\mu^{(\lambda)}(k)e^{-ik\cdot x}
+\hat c_\lambda^\dagger(k)\varepsilon_\mu^{(\lambda)*}(k)e^{+ik\cdot x}\right], \qquad E_k=|\mathbf k|.$$

This has the same structure as the scalar field expansion. The extra sum accounts for the four polarization directions. Each $\hat c_\lambda$ removes a quantum in its mode, and each $\hat c_\lambda^\dagger$ adds one.

Two of these four modes are unphysical, and the construction has to remove them. The timelike mode is the awkward one. The metric gives the time component a kinetic term of the opposite sign from the three spatial components, that sign carries through into the ladder algebra, and a single timelike quantum comes out with negative norm. A state space that contains negative-norm states cannot be read directly as a space of physical photons.

The **Gupta–Bleuler condition** selects the physical states. It imposes the Lorenz condition on states, but only through its annihilation part:

$$\boxed{\big(\partial_\mu\hat A^\mu\big)^{(+)}\lvert\mathrm{phys}\rangle=0,}$$

where the superscript $(+)$ keeps the positive-frequency terms, those containing $\hat c_\lambda e^{-ik\cdot x}$. This restricts which states we accept while leaving the canonical operator algebra intact. For momentum along $z$ it forces $\hat c_0$ and $\hat c_3$ to act identically on a physical state, so their contributions to observable quantities cancel. A final identification then drops states that differ only by a zero-norm gauge mode. What remains are the two transverse polarizations found from Maxwell's equation.

<details>
<summary>Negative norm, the physical-state condition, and the null states</summary>

**The timelike commutator.** The metric makes the kinetic term

$$\mathcal L=-\frac12(\partial_\mu A^0)(\partial^\mu A^0)
+\frac12\sum_{i=1}^3(\partial_\mu A^i)(\partial^\mu A^i).$$

The three spatial components have the usual scalar kinetic sign. The time component has the opposite sign.

Write $\eta_\lambda=\varepsilon^{(\lambda)*}\cdot\varepsilon^{(\lambda)}$, so $\eta_0=+1$ and $\eta_{1,2,3}=-1$. The canonical commutators give

$$[\hat c_\lambda(k),\hat c_{\lambda'}^\dagger(k')]
=-\eta_\lambda\,\delta_{\lambda\lambda'}(2\pi)^3\delta^3(\mathbf k-\mathbf k').$$

The factor $(2\pi)^3$ matches the integration measure in the expansion. If we suppress the momentum normalization, the spatial modes have $[\hat c_i,\hat c_i^\dagger]=1$, while the timelike mode has $[\hat c_0,\hat c_0^\dagger]=-1$. That minus sign means a timelike one-quantum state has negative norm.

**The condition on physical states.** For momentum along $z$, the transverse modes contribute nothing to the divergence. The timelike and longitudinal modes contribute with opposite signs, giving

$$\big(\hat c_0(k)-\hat c_3(k)\big)\lvert\mathrm{phys}\rangle=0.$$

Thus $\hat c_0$ and $\hat c_3$ act identically on a physical state. One consequence shows up in the Hamiltonian:

$$\hat H=\int\frac{d^3k}{(2\pi)^3}E_k
\left(\hat c_1^\dagger\hat c_1+\hat c_2^\dagger\hat c_2
+\hat c_3^\dagger\hat c_3-\hat c_0^\dagger\hat c_0\right)+\text{const.}$$

On physical states, the last two terms have equal and opposite expectation values. The transverse modes supply the physical excitation energy.

**The null states.** Physical states that differ only by a zero-norm gauge state represent the same physical state. These null states have no effect on physical matrix elements. After this identification, the photon has the two transverse polarizations found from Maxwell's equation.

</details>

An external photon in a scattering calculation therefore carries one of these two polarizations, or a superposition of them such as circular polarization.

![Gauge fixing gives four quantizable modes. The physical-state condition and identification of null gauge states recover the two physical photon polarizations.](./manim/photon-quantization-route.png)

*Gauge fixing gives four quantizable modes. The physical-state condition and identification of null gauge states recover the two physical photon polarizations.*

### Handoff to perturbation theory

The photon field is now quantized, including its gauge fixing and physical-state
restriction. The next step is to introduce time ordering and contractions, then
extract the photon propagator from this field. [Perturbation Theory](perturbation-theory.md)
performs that extraction and assembles the QED factors into amplitudes. The
[Feynman Rules page](feynman-rules.md) then uses those factors in scattering
calculations, and [From Lagrangian to Experiment](lagrangian-to-experiment.md)
connects the resulting amplitude to measured rates.

[^lorenz]: The Lorenz condition is named for Ludvig Lorenz. The spelling distinguishes his name from Hendrik Lorentz, whose name appears in Lorentz transformations.

[^operator-lorenz]: Using the simplified gauge-fixed Lagrangian, $\hat\pi^0=-\dot{\hat A}^0$, so $\partial\cdot\hat A=-\hat\pi^0+\partial_i\hat A^i$. The equal-time canonical algebra then gives $[\partial\cdot\hat A(t,\mathbf x),\hat A_0(t,\mathbf y)]=i\delta^3(\mathbf x-\mathbf y)$, since the field components commute with each other at equal times. If the divergence were the zero operator, this commutator would have to vanish. The Gupta–Bleuler condition avoids that contradiction by constraining states with only the annihilation part of the divergence.
