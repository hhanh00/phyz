# Quantum Field Theory: Fields and Quanta

A single-particle wave function cannot describe pair creation or annihilation. To continue from [The Dirac Equation](dirac-equation.md), we therefore introduce **field operators**: operators assigned to spacetime points that act on states with different particle numbers.

For the electron field, these operators remove electrons and create positrons. This gives the negative-frequency solutions a precise role without a filled sea of negative-energy electrons.

## Recap of Dirac Equation

The free Dirac solution is a sum of plane waves. At each momentum and spin, $a_s(p)$ multiplies a positive-frequency $u$ solution and $b_s^*(p)$ a negative-frequency $v$ solution. These coefficients are still numbers: they specify a classical field and cannot yet remove or add a particle.

<details>
<summary>The classical mode expansion</summary>

Start with the general free solution from [The Dirac Equation §6](dirac-equation.md#_6-general-solution):

$$\psi(x) = \sum_{s=1}^{2} \int \frac{d^3p}{(2\pi\hbar)^3}\,\frac{1}{\sqrt{2E_p}}\left[a_s(p)\,u_s(p)\,e^{-ip\cdot x/\hbar} + b_s^*(p)\,v_s(p)\,e^{+ip\cdot x/\hbar}\right],$$

Here $p\cdot x = E_p t - \mathbf p\cdot\mathbf x$ and $E_p = \sqrt{\mathbf p^2 + m^2}$. The index $s$ labels the two spin states. The coefficients $a_s(p)$ and $b_s^*(p)$ are complex amplitudes fixed by the initial field.

The $u$-terms have positive frequency; the $v$-terms have negative frequency. [§3](dirac-equation.md#_3-antiparticles) related the second family to antiparticles, and [§4](dirac-equation.md#_4-negative-energy-solutions) introduced the historical hole interpretation. We will now describe both families with operators.

</details>

### The promotion

To describe changing particle numbers, replace the numerical amplitudes by operators. This implements the step discussed in [§4](dirac-equation.md#_4-negative-energy-solutions) and proposed after the general solution in [§6](dirac-equation.md#_6-general-solution):

$$a_s(p) \to \hat a_s(p), \qquad b_s^*(p) \to \hat b_s^\dagger(p),$$

The operator $\hat a_s(p)$ removes an electron of momentum $\mathbf p$ and spin label $s$. The operator $\hat b_s^\dagger(p)$ creates a positron with those labels.

For operators, the counterpart of complex conjugation is the **adjoint**, denoted by $\dagger$. This explains the notation $b_s^*$ in [§6](dirac-equation.md#_6-general-solution): after quantization it becomes $\hat b_s^\dagger$. The expansion is now

$$\hat\psi(x) = \sum_{s=1}^{2} \int \frac{d^3p}{(2\pi\hbar)^3}\,\frac{1}{\sqrt{2E_p}}\left[\hat a_s(p)\,u_s(p)\,e^{-ip\cdot x/\hbar} + \hat b_s^\dagger(p)\,v_s(p)\,e^{+ip\cdot x/\hbar}\right],$$

This is the **electron field operator**. Split it into its positive- and negative-frequency parts, $\hat\psi = \hat\psi^{(+)} + \hat\psi^{(-)}$. Taking the adjoint reverses the phases and exchanges creation with annihilation:

| field term | operator | plane wave | action |
| --- | --- | --- | --- |
| $\hat\psi^{(+)}$ (positive frequency) | $\hat a_s(p)$ | $e^{-ip\cdot x/\hbar}$ | annihilates an electron |
| $\hat\psi^{(-)}$ (negative frequency) | $\hat b_s^\dagger(p)$ | $e^{+ip\cdot x/\hbar}$ | creates a positron |
| $\hat\psi^{(+)\dagger}$ | $\hat a_s^\dagger(p)$ | $e^{+ip\cdot x/\hbar}$ | creates an electron |
| $\hat\psi^{(-)\dagger}$ | $\hat b_s(p)$ | $e^{-ip\cdot x/\hbar}$ | annihilates a positron |

**The phase determines the energy change.** A **matrix element** $\langle f|\hat\psi|i\rangle$ is the component of $\hat\psi|i\rangle$ along a chosen final state $|f\rangle$. It measures how the field connects the two states.

The factor $e^{-iE_pt/\hbar}$ accompanies a decrease in energy by $E_p$; the opposite factor accompanies an increase. Negative frequency therefore does not imply that the created particle has negative energy.

<details>
<summary>Relating the phase to the energy change</summary>

For energy eigenstates, Heisenberg evolution gives this matrix element a time factor $e^{i(E_f-E_i)t/\hbar}$. Compare that with the factor $e^{-iE_p t/\hbar}$ multiplying $\hat a_s(p)$. A nonzero contribution requires $E_f-E_i=-E_p$, so this operator lowers the energy by $E_p$. Matching the spatial phases likewise shows that it removes momentum $\mathbf p$.

The opposite phase, $e^{+ip\cdot x/\hbar}$, corresponds to adding energy $E_p$ and momentum $\mathbf p$. This is why its coefficient is a creation operator. To identify each added quantum as a particle, we still have to construct the Hamiltonian and its spectrum.

</details>

The phases determine whether an operator creates or annihilates. The species labels follow the convention in [The Dirac Equation](dirac-equation.md): the $u$-family describes electrons and the $v$-family describes positrons.

Both the field and its adjoint contain creation and annihilation terms. We retain the negative-frequency solutions, but use them to create positive-energy antiparticles.

### What the promotion does not yet have

Replacing the coefficients gives a useful candidate field operator. To make it a complete quantum description, we still have to specify three ingredients:

- **States with arbitrary particle number.** Start from a vacuum $|0\rangle$ that every $\hat a$ and $\hat b$ annihilates. This replaces the sea in [§4](dirac-equation.md#_4-negative-energy-solutions). Schematically, pair annihilation becomes $\hat a\,\hat b\,|e^-\,e^+\rangle = |0\rangle$, up to the ordering convention for fermion states.
- **An operator algebra.** Commutators or anticommutators determine how multiparticle states behave under exchange, addressing the statistics assumption in [§4](dirac-equation.md#_4-negative-energy-solutions).
- **A Hamiltonian bounded below.** A lowest-energy vacuum must exist despite the negative-frequency solutions of [Relativistic QM §3](relativistic-qm.md#_3-negative-energy-and-probability).

Before constructing these, we need to distinguish the field types and the quantum pictures.

## Fields

A classical field assigns a value to each spacetime point. We classify fields by how those values change under Lorentz transformations, as in [The Dirac Equation §5](dirac-equation.md#_5-spinors). This transformation law also determines the spin content of the quantized field:

| field | transformation law | spin | quanta |
| --- | --- | --- | --- |
| scalar $\phi(x)$ | $\phi'(x') = \phi(x)$ — invariant | $0$ | Higgs, pion |
| vector $A^\mu(x)$ | $A'^\mu(x') = \Lambda^\mu{}_{\nu}\,A^\nu(x)$ | $1$ | photon |
| spinor $\psi(x)$ | $\psi'(x') = S(\Lambda)\,\psi(x)$ | $\tfrac{1}{2}$ | electron |

To write a relativistic equation, combine fields and derivatives so that every term transforms consistently ([Special Relativity §6](special-relativity.md#_6-metric-tensor-covariance-and-contravariance)). The familiar free equations follow from the simplest choices for these field types.

For the free fields considered here, we use Klein–Gordon for scalars, Dirac for spinors, and Maxwell for the electromagnetic field. These equations determine how the modes evolve; quantization will determine how many particles occupy them.

<details>
<summary>The free equations for the three field types</summary>

**Scalar field.** A derivative combination that transforms as a scalar is $\Box = \partial_\mu\partial^\mu = \partial_t^2 - \nabla^2$. Combining it with a mass term gives

$$\left(\Box + \frac{m^2}{\hbar^2}\right)\phi = 0,$$

This is the Klein–Gordon equation from [Relativistic QM §2](relativistic-qm.md#_2-klein-gordon), with dispersion relation $E^2 = \mathbf p^2 + m^2$.

Its earlier difficulty concerned interpreting the conserved density as a single-particle probability density. A classical field $\phi$ is not a probability amplitude, so that interpretation is unnecessary here.

**Spinor field.** The spinor transformation $S(\Lambda)$ and the gamma matrices from [The Dirac Equation](dirac-equation.md) satisfy a compatibility relation. As a result, the derivative term $\gamma^\mu\partial_\mu\psi$ transforms as a spinor, just like $\psi$. We can combine them as

$$(i\hbar\,\gamma^\mu\partial_\mu - m)\psi = 0,$$

The Dirac equation is first order in both time and space. [Relativistic QM §4](relativistic-qm.md#_4-dirac-equation) introduced it to obtain a positive single-particle density. We now use the same equation for a field with spin and antiparticle modes.

**Vector field.** The electromagnetic potential $A^\mu$ enters the field tensor $F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu$ from [Special Relativity §8](special-relativity.md#_8-maxwell-equations). In empty space,

$$\partial_\mu F^{\mu\nu} = 0 \quad\Longleftrightarrow\quad \Box A^\nu - \partial^\nu(\partial_\mu A^\mu) = 0,$$

These are the source-free Maxwell equations. Their physical waves propagate at $c$, corresponding to massless photons. A massive vector field instead satisfies $\partial_\mu F^{\mu\nu} + \tfrac{m^2}{\hbar^2}A^\nu = 0$. The transformation law alone does not fix the mass.

</details>

We have met these equations before: Klein–Gordon in [Relativistic QM §2](relativistic-qm.md#_2-klein-gordon), Dirac in [The Dirac Equation](dirac-equation.md), and Maxwell in classical electromagnetism. Here all three describe fields whose quantized excitations are particles.

The relation between transformation law and spin is the one developed in [§5](dirac-equation.md#_5-spinors). The Higgs is another scalar example; its full description involves interactions beyond the free equations considered here.

![Scalar, vector, and spinor fields use different component transformation laws for the same Lorentz change of frame.](./manim/field-transformation-types.png)

*Scalar, vector, and spinor fields use different component transformation laws for the same Lorentz change of frame.*

### What the table does not cover

The table is not exhaustive. Higher-spin representations exist, and composite particles can have higher spins: the $\Delta$ baryon has spin $\tfrac32$, for example.

The pion is itself composite. Its scalar field is an effective description of a quark bound state, but it still transforms as a scalar under Lorentz transformations. A field's transformation law and whether its particle is elementary are separate questions.

### Second quantization

[First Quantization](first-quantization.md) promoted a particle's position and momentum to operators. **Second quantization** instead quantizes a classical field, replacing its mode amplitudes by operators. Despite the name, we do not quantize the same object twice.

The resulting fields $\hat\phi(x)$, $\hat A^\mu(x)$, and $\hat\psi(x)$ act on a space containing different particle numbers. For example, $\hat a_s^\dagger(\mathbf p)|0\rangle$ contains one electron of momentum $\mathbf p$ and spin $s$. The electron field also has positron operators; the electromagnetic field has photon operators.

Strictly, quantum fields are **operator-valued distributions**. To obtain well-defined operators and normalizable states, we integrate them against suitable smooth functions rather than evaluate them at an exact point.

### Choosing a picture

We can place time dependence in the states or in the operators. These are two equivalent descriptions of the same predictions. [The Dirac Equation §2](dirac-equation.md#_2-conservation-and-commutators) already used the second description to derive $d\hat A/dt = \tfrac{i}{\hbar}[\hat H,\hat A]$.

In the **Schrödinger picture**, states evolve. Operators without explicit time dependence stay fixed:

$$|\Psi_S(t)\rangle = e^{-i\hat H t/\hbar}\,|\Psi_S(0)\rangle, \qquad \hat O_S \;\text{ fixed};$$

In the **Heisenberg picture**, states stay fixed in time and operators evolve:

$$|\Psi_H\rangle \;\text{ fixed}, \qquad \hat\phi(t, \mathbf x) = e^{i\hat H t/\hbar}\,\hat\phi(0, \mathbf x)\,e^{-i\hat H t/\hbar}.$$

<details>
<summary>Checking that the two pictures give the same expectation values</summary>

The plus sign on the left comes from taking the adjoint of the time-evolution operator in [First Quantization](first-quantization.md). The ket evolves with $e^{-i\hat Ht/\hbar}$, while the bra evolves with $e^{+i\hat Ht/\hbar}$.

Moving both factors onto the operator gives the Heisenberg expression differentiated in [The Dirac Equation §2](dirac-equation.md#_2-conservation-and-commutators). The expectation values agree:

$$\langle\Psi_S(t)|\,\hat O_S\,|\Psi_S(t)\rangle = \langle\Psi_H|\,\hat O_H(t)\,|\Psi_H\rangle,$$

</details>

The pictures differ in where we write the time dependence. Heisenberg fields make Lorentz covariance easier to display, as discussed below.

![Schrödinger and Heisenberg pictures place the time dependence in different objects while preserving all expectation values.](./manim/quantum-pictures.png)

*Schrödinger and Heisenberg pictures place the time dependence in different objects while preserving all expectation values.*

### State versus field

In wave mechanics, $\psi(\mathbf x)$ is the position-space representation of a state. In field theory, $\hat\psi(x)$ is an operator acting on a state $|\Psi\rangle$; it is not that state's wave function.

The state can describe a vacuum, a momentum eigenstate, or a localized wave packet with many particles. It still contains spatial information, although we need not represent it as a function of a fixed list of particle positions. The coordinate $x$ on a field operator labels where the operator acts. Particle position is therefore no longer a universal canonical coordinate for the whole theory.

![A creation operator adds a quantum to a particular mode. A field operator combines creation and annihilation operators for many modes.](./manim/state-and-field.png)

*A creation operator adds a quantum to a particular mode. A field operator combines creation and annihilation operators for many modes.*

### Building one-particle states

Apply $\hat\psi^\dagger(x)$ to the vacuum. Its positron-annihilation terms vanish because $\hat b_s(p)|0\rangle=0$. The electron-creation terms remain:

$$\hat\psi^\dagger(x)\,|0\rangle \;=\; \sum_s\int \frac{d^3p}{(2\pi\hbar)^3}\,\frac{1}{\sqrt{2E_p}}\;u_s^\dagger(p)\,e^{+ip\cdot x/\hbar}\,\hat a_s^\dagger(p)\,|0\rangle.$$

Each surviving term contains one electron creation operator. Thus the result is a superposition of one-electron momentum states. Applying $\hat\psi(x)$ instead leaves the $\hat b_s^\dagger$ terms and creates a positron superposition.

The point label $x$ fixes the relative phases of the momentum components. A field at an exact point gives a formal distributional state; integrating it with a suitable spatial profile produces a wave packet. This is the precise sense in which fields build one-particle states.

### Why Heisenberg

The Schrödinger picture remains valid in relativistic field theory, but its covariance is less explicit. The equation $i\hbar\partial_t|\Psi_S(t)\rangle=\hat H|\Psi_S(t)\rangle$ refers to a chosen time coordinate and a spatial slice at that time.

The state representation also becomes more elaborate as we move from one particle to many particles and then to a field:

$$\psi(\mathbf x) \;\longrightarrow\; \psi(\mathbf x_1, \ldots, \mathbf x_N) \;\longrightarrow\; \Psi[\varphi(\mathbf x)],$$

The **wave functional** $\Psi[\varphi(\mathbf x)]$ assigns an amplitude to each whole field configuration on a spatial slice. A Lorentz boost changes that slice: events simultaneous in one frame are generally not simultaneous in another.

This does not invalidate Schrödinger evolution. It means that covariance involves transforming the slice as well as the state. The first-order Dirac equation from [Relativistic QM §4](relativistic-qm.md#_4-dirac-equation) does not remove this distinction.

In the Heisenberg picture, the field already carries a spacetime label. With a consistent convention, a scalar transforms as $\hat U(\Lambda)\hat\phi(x)\hat U^{-1}(\Lambda)=\hat\phi(\Lambda x)$; vector and spinor fields also acquire their component matrices. We can therefore express covariance directly through local field transformations. States remain fixed under time evolution in this picture, though they still transform when we change reference frame.

The free field operators obey the same wave equations as the classical fields: Klein–Gordon for $\hat\phi(x)$ ([Relativistic QM §2](relativistic-qm.md#_2-klein-gordon)) and Dirac for $\hat\psi(x)$ ([The Dirac Equation](dirac-equation.md)). Quantization changes the amplitudes into operators; it preserves these free equations.

The field types differ in their operator algebra. Integer-spin fields use commutators, while half-integer-spin fields use anticommutators. The constructions ahead illustrate this spin–statistics connection; we give the general result without proof because its derivation requires a longer treatment of relativistic locality and positive-norm states.

We can now construct the operator algebra, the state space, and the Hamiltonian. In particular, we must check that energy has a lower bound, resolving the problem in [Relativistic QM §3](relativistic-qm.md#_3-negative-energy-and-probability).

The [next page](qft-action.md) starts with the scalar field and its action. The [Field Quantization page](field-quantization.md#the-spinor-field) develops the spinor algebra. The photon also has gauge redundancy, which we handle on the [QED page](qed.md#quantizing-the-photon-field).
