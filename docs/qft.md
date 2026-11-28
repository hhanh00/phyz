# Quantum Field Theory: Fields and Quanta

A single-particle wave function cannot describe pair creation or annihilation. To continue from [The Dirac Equation](dirac-equation.md), we therefore introduce **field operators**: operators assigned to spacetime points that act on states with different particle numbers.

For the electron field, these operators remove electrons and create positrons. This gives the negative-frequency solutions a precise role without a filled sea of negative-energy electrons.

## From a negative energy to a positron

[The Dirac Equation](dirac-equation.md) left four wave functions for a particle at rest. Two have the energy $+mc^2$ and two have $-mc^2$, and in each pair one is spin up and one is spin down. [Chapter 5](relativistic-qm.md) said what is wrong with a negative energy: an electron could drop into such a state and keep falling, with no lowest rung, and no atom would last. A way out has to do three things.

1. **Stop the fall.** There has to be a lowest state, with nothing below it.
2. **Account for what is seen.** Positrons exist, with a positive energy, and an electron and a positron can appear together out of a packet of light.
3. **Keep the equation**, because it gave the spin and the strength of the electron's magnet.

This section does a first part of that. It shows what kind of particle the negative-energy solutions are about. It doesn't stop the fall and it doesn't make pairs, and the rest of the chapter needs fields for both.

Here is where the section ends up, for a particle at rest:

| Entry of the column | Energy of its solution | Spin of the entry | What it describes |
| --- | --- | --- | --- |
| $\psi_1$ | $+mc^2$ | up | An electron, spin up |
| $\psi_2$ | $+mc^2$ | down | An electron, spin down |
| $\psi_3$ | $-mc^2$ | up | A positron, spin down |
| $\psi_4$ | $-mc^2$ | down | A positron, spin up |

In the last two rows the solution has a negative energy, and the positron it describes has a positive one. The positron's spin is the opposite of the entry's as well.

**Another reading of a negative-energy solution.** Two steps turn each negative-energy solution into a positive-energy solution for a particle of the opposite charge. No chance of finding the particle changes on the way. The steps can also be undone, so the new solution holds the same information as the old one.

**Step one: take the complex conjugate.** We want to change the sign of the energy without changing any chance. The complex conjugate does that. The [complex conjugate](appendix-math-complex.md#_1-complex-numbers) of a number, marked with a star, has $-i$ wherever the number has $i$. It keeps the number's length, and a chance is a squared length, so it changes no chance.

A wave with momentum $p$ along $z$ and energy $E$ is $e^{i(pz - Et)/\hbar}$. Give it the negative energy $-E$, where $E$ is positive, and it reads $e^{i(pz + Et)/\hbar}$. Conjugating puts a minus sign in front of the whole exponent:

$$\left(e^{i(pz + Et)/\hbar}\right)^* = e^{-i(pz + Et)/\hbar} = e^{i\left((-p)z - Et\right)/\hbar}.$$

Compare the last form with the wave we started from. It has $-p$ where $p$ stood, and its energy is $+E$. Conjugating has reversed the energy, and the momentum with it.

**Step two: reshuffle the column.** Step one isn't enough on its own. Take the particle at rest, with only the third entry filled. After conjugating, its wave turns in time like a wave of energy $+mc^2$. But the filled entry still sits in the lower pair, and the equation gives the lower pair the energy $-mc^2$. The wave and its place in the column disagree, so the conjugate isn't a solution yet.

The repair is to move the entries. A fixed matrix, the same one for every solution, swaps the upper pair with the lower pair. That fixes the particle at rest. For a particle moving in some directions, one more term comes out of the conjugate with the wrong sign, and swapping spin up with spin down inside each pair fixes that one (box). So the matrix does both, and this second swap is why the positron's spin comes out opposite. What was in $\psi_3$ ends up in the place of $\psi_2$. That doesn't make it an electron with spin down, because the new column obeys a different equation, as the next paragraph shows. The matrix only moves entries and changes some signs, so like the conjugate it changes no chance.

Call the result $\psi_c$, with $c$ for conjugate:

$$\psi_c = (\text{a fixed matrix}) \times \psi^*.$$

**The charge.** So far the particle was free, and a free particle's equation doesn't contain its charge at all. The charge $q$ appears only when a magnetic field is present, as in [chapter 6's section 5](dirac-equation.md#_5-the-strength-of-the-magnet). So to find the charge of $\psi_c$, put a field in. The field adds one piece to the equation, with $q$ in it. Do the two steps to the whole equation (box). Everything comes back as it started except that piece, whose sign has changed. That is the Dirac equation with $-q$ in place of $q$. The electron's charge is $q = -e$, so $\psi_c$ obeys the equation for a particle of charge $+e$.

**What changes.** Put the three together. A negative-energy solution of the electron's equation becomes a positive-energy solution of the equation for a particle of charge $+e$.

![Two cards side by side. On the left, a negative-energy solution of the electron's equation: energy minus E, momentum p shown as an arrow pointing up, spin up, charge minus e, mass m. On the right, the solution it becomes, a positron: energy plus E, momentum minus p shown as an arrow pointing down, spin down, charge plus e, mass m. Between them each row is marked as reversed, except the mass, which is marked as the same.](./manim/electron-positron-flip.png)

*The energy, the momentum, the spin and the charge are reversed. The mass is the same.*

A particle with the electron's mass, a positive energy and the charge $+e$ is the **positron** of chapter 5.

**The same signs as chapter 5's hole.** These four reversals are the ones chapter 5's hole had. Physicists have dropped the filled sea, but its rule is easy to remember: a hole is a missing electron, so whatever that electron had, the hole has minus it. Chapter 5 used the rule for the energy and the charge. It gives the momentum and the spin too. So the equation, with no sea, gives the same particle the hole gave.

That is the table above. At rest, the four entries describe two particles, each with two spins.

**What this doesn't do.** This is still one equation for one particle. It can relabel a negative-energy solution, but it can't make an electron and a positron appear out of a packet of light, as chapter 5 said happens. It doesn't stop chapter 5's fall either. We have renamed the negative-energy solutions, but the electron's equation still has them, and nothing here stops an electron from dropping into one. Both need the wave function to become a field, which is what the rest of this chapter starts on.

<details>
<summary>The calculation: checking the conjugate solution</summary>

**The two steps, written out.** They take the column $(\psi_1, \psi_2, \psi_3, \psi_4)$ to

$$\psi_c = \left(\psi_4^*,\ -\psi_3^*,\ -\psi_2^*,\ \psi_1^*\right).$$

The upper pair and the lower pair have changed places. Inside each pair, up and down have changed places, and the two middle entries have a minus sign. For the particle at rest with only $\psi_3$ filled, $\psi_c$ has only its second entry filled, which is a spin-down entry in the upper pair.

**What the fixed matrix has to repair.** If $\psi$ obeys the Dirac equation, conjugate the whole equation to see what $\psi^*$ obeys. The rate of change in time comes with an $i$, and so does each slope, so those terms change sign. The mass term, $\beta\,mc^2$, has no $i$ and stays as it was. The matrix $\alpha_y$ is built from $\hat Y$, which has an $i$ of its own, and that cancels the sign change of the slope along $y$. So two terms are left with the wrong sign against the others: the mass term and the term with the slope along $y$. The fixed matrix changes the sign of exactly those two.

- It swaps the upper pair with the lower pair. The matrix $\beta$ is $+1$ on the upper pair and $-1$ on the lower, so swapping the pairs does to the mass term what changing the sign of $\beta$ would.
- Inside each pair it swaps spin up with spin down, with a change of sign, and the two pairs get opposite signs. Together these leave $\alpha_x$ and $\alpha_z$ as they were and change the sign of $\alpha_y$. Multiplying the matrices out confirms it, and we leave that out.

**The charge, term by term.** A field enters the equation by replacing $\hat p_x$ with $\hat p_x - qA_x$, which is $-i\hbar\,\partial/\partial x - qA_x$, and likewise for $y$ and $z$. Here $\mathbf A$ is the field of arrows from the box in chapter 6's section 5. Its values are ordinary real numbers, so conjugation turns the $-i$ into $+i$ and leaves $qA_x$ alone:

$$-i\hbar\,\frac{\partial}{\partial x} - qA_x \quad\longrightarrow\quad +i\hbar\,\frac{\partial}{\partial x} - qA_x = -\left(-i\hbar\,\frac{\partial}{\partial x} + qA_x\right).$$

Follow the terms of the equation through both steps.

| Term | After conjugating | After the fixed matrix |
| --- | --- | --- |
| Rate of change in time, $i\hbar\,\partial/\partial t$ | Sign changed | Still changed |
| Momentum along $x$ or $z$, with the field | Sign changed, and $-qA$ has become $+qA$ | No further change |
| Momentum along $y$, with the field | Sign not changed, but $-qA_y$ has become $+qA_y$ | Sign changed |
| Mass, $\beta\,mc^2$ | Sign not changed | Sign changed |

After both steps every term carries the same minus sign. Multiply the whole equation by $-1$, and every sign is as it was at the start, except that $+q\mathbf A$ stands where $-q\mathbf A$ stood. That is the Dirac equation for the charge $-q$.

</details>

**Conjugating a negative-energy solution and reshuffling its entries gives a positive-energy solution for the opposite charge, with the same mass. At rest, the four entries describe the electron and the positron, each with two spins.**

## Spacetime, components, and value spaces

<details>
<summary>Expand the notation</summary>

Before discussing particular fields, it is useful to distinguish the point at
which a field is evaluated from the kind of object the field returns. A
spacetime point is

$$x=(x^0,x^1,x^2,x^3)=(t,\mathbf x)\in\mathbb R^{1,3}.$$

The superscripts on $x^\mu$ label spacetime components; they are not powers.
A classical field is a function of $x$ whose values transform in some
representation of the Lorentz group:

| Field | Mathematical type before quantization | Components at each $x$ | Spin |
| --- | --- | --- | --- |
| real scalar $\phi(x)$ | $\mathbb R^{1,3}\to\mathbb R$ | one real number | $0$ |
| complex scalar $\phi(x)$ | $\mathbb R^{1,3}\to\mathbb C$ | one complex number, or two real numbers | $0$ |
| vector $A^\mu(x)$ | $\mathbb R^{1,3}\to\mathbb R^{1,3}$ | four-vector | $1$ |
| Dirac spinor $\psi(x)$ | $\mathbb R^{1,3}\to\mathbb C^4$ | four spinor components | $\tfrac12$ |

In this text, $\phi$ and $\varphi$ denote scalar fields or scalar field configurations, while $\psi$ denotes a fermion (spinor) field. The change from $\phi$ to $\varphi$ is notation, not a change of field type; $\varphi(\mathbf x)$ specifically denotes a spatial configuration at fixed time in the canonical discussion below.

The four components of $\psi$ belong to **spinor space** $\mathbb C^4$;
they are not the four spacetime components labelled by $\mu=0,1,2,3$.
The matrices $\gamma^\mu$ act on those spinor components and carry a
spacetime index so that $\gamma^\mu\partial_\mu\psi$ transforms as a
spinor. Likewise, a vector's four entries are spacetime components, and
raising or lowering its index uses the Minkowski metric.

A **field value** is the value of a field at one point, such as $\phi(x)$.
A **field configuration** is an entire assignment of field values over a
region. In the canonical picture, a configuration on the time slice $t$ is
often written

$$\varphi(\mathbf x)=\phi(t,\mathbf x),$$

so $\varphi$ is one point in an infinite-dimensional configuration space:
each possible function $\mathbf x\mapsto\varphi(\mathbf x)$ is a different
configuration. A wave functional $\Psi[\varphi]$ assigns an amplitude to
such a whole configuration, just as an ordinary wave function assigns an
amplitude to a particle position. In a path integral, one instead sums over
whole spacetime configurations $x\mapsto\phi(x)$.

After quantization, the fields acquire hats when useful in the notation:
$\hat\phi(x)$, $\hat A^\mu(x)$, and $\hat\psi(x)$ are operator-valued
distributions acting on a Hilbert (usually Fock) space of states. Their
spacetime labels and component spaces remain the same, but their values are
operators rather than ordinary numbers. Quantum fields are formally written
at spacetime points, but mathematically they are operator-valued
distributions. To obtain well-defined operators, we average them over a
finite region using a smooth test function. For example,

$$\hat\phi(f)=\int d^4x\,f(x)\hat\phi(x).$$

Real detectors likewise have finite spatial and temporal resolution, so this
smearing reflects physical measurement rather than a limitation of the
theory.

</details>

## Recap of Dirac Equation

The free Dirac solution is a sum of plane waves. At each momentum and spin, $a_s(p)$ multiplies a positive-frequency $u$ solution and $b_s^*(p)$ a negative-frequency $v$ solution. These coefficients are still numbers: they specify a classical field and cannot yet remove or add a particle.

<details>
<summary>The classical mode expansion</summary>

Start with the general free solution from [the Dirac reference page §1](dirac-reference.md#_1-the-general-solution):

$$\psi(x) = \sum_{s=1}^{2} \int \frac{d^3p}{(2\pi\hbar)^3}\,\frac{1}{\sqrt{2E_p}}\left[a_s(p)\,u_s(p)\,e^{-ip\cdot x/\hbar} + b_s^*(p)\,v_s(p)\,e^{+ip\cdot x/\hbar}\right],$$

Here $p\cdot x = E_p t - \mathbf p\cdot\mathbf x$ and $E_p = \sqrt{\mathbf p^2 + m^2}$. The index $s$ labels the two spin states. The coefficients $a_s(p)$ and $b_s^*(p)$ are complex amplitudes fixed by the initial field.

The $u$-terms have positive frequency; the $v$-terms have negative frequency. [The first section](#from-a-negative-energy-to-a-positron) related the second family to antiparticles, and [Relativistic QM §9](relativistic-qm.md#_9-the-negative-energies-predict-antimatter) introduced the historical hole interpretation. We will now describe both families with operators.

</details>

### The promotion

To describe changing particle numbers, replace the numerical amplitudes by operators. This implements the step discussed in [Relativistic QM §10](relativistic-qm.md#_10-why-a-one-particle-equation-isn-t-enough) and proposed after the general solution in [the Dirac reference page §1](dirac-reference.md#_1-the-general-solution):

$$a_s(p) \to \hat a_s(p), \qquad b_s^*(p) \to \hat b_s^\dagger(p),$$

The operator $\hat a_s(p)$ removes an electron of momentum $\mathbf p$ and spin label $s$. The operator $\hat b_s^\dagger(p)$ creates a positron with those labels.

For operators, the counterpart of complex conjugation is the **adjoint**, denoted by $\dagger$. This explains the notation $b_s^*$ in [the Dirac reference page §1](dirac-reference.md#_1-the-general-solution): after quantization it becomes $\hat b_s^\dagger$. The expansion is now

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

The phases determine whether an operator creates or annihilates. The species labels follow the convention in [the Dirac reference page](dirac-reference.md#_1-the-general-solution): the $u$-family describes electrons and the $v$-family describes positrons.

Both the field and its adjoint contain creation and annihilation terms. We retain the negative-frequency solutions, but use them to create positive-energy antiparticles.

### Particles as field excitations

For a free field, decompose a spatial configuration into independent wave
modes. A mode is one wave pattern, labeled by momentum $\mathbf p$ in free
space. Each mode evolves like a harmonic oscillator. Quantization promotes the
mode amplitudes to operators, and the creation operator produces one quantum
of that mode:

$$|1_{\mathbf p}\rangle=\hat a^\dagger(\mathbf p)|0\rangle.$$

Here $|0\rangle$ is the vacuum, $\hat a^\dagger(\mathbf p)$ creates one
excitation with momentum $\mathbf p$, and $|1_{\mathbf p}\rangle$ is the
corresponding one-particle state. A particle is therefore not a term in the
Lagrangian or a field value at one point; it is a quantized excitation of a
field. The quadratic part of the Lagrangian determines the free modes and
their masses, while higher-order terms describe interactions among their
excitations.

### What the promotion does not yet have

Replacing the coefficients gives a useful candidate field operator. To make it a complete quantum description, we still have to specify three ingredients:

- **States with arbitrary particle number.** Start from a vacuum $|0\rangle$ that every $\hat a$ and $\hat b$ annihilates. This replaces the sea in [Relativistic QM §9](relativistic-qm.md#_9-the-negative-energies-predict-antimatter). Schematically, pair annihilation becomes $\hat a\,\hat b\,|e^-\,e^+\rangle = |0\rangle$, up to the ordering convention for fermion states.
- **An operator algebra.** Commutators or anticommutators determine how multiparticle states behave under exchange, addressing the statistics assumption in [Relativistic QM §10](relativistic-qm.md#_10-why-a-one-particle-equation-isn-t-enough).
- **A Hamiltonian bounded below.** A lowest-energy vacuum must exist despite the negative-frequency solutions of [Relativistic QM §4](relativistic-qm.md#_4-first-problem-negative-energies).

Before constructing these, we need to distinguish the field types and the quantum pictures.

## Fields

A classical field assigns a value to each spacetime point. We classify fields by how those values change under Lorentz transformations, as in [the Dirac reference page §2](dirac-reference.md#_2-the-notation-later-chapters-use). This transformation law also determines the spin content of the quantized field:

| field | transformation law | spin | quanta |
| --- | --- | --- | --- |
| scalar $\phi(x)$ | $\phi'(x') = \phi(x)$ — invariant | $0$ | Higgs, pion |
| vector $A^\mu(x)$ | $A'^\mu(x') = \Lambda^\mu{}_{\nu}\,A^\nu(x)$ | $1$ | photon |
| spinor $\psi(x)$ | $\psi'(x') = S(\Lambda)\,\psi(x)$ | $\tfrac{1}{2}$ | electron |

To write a relativistic equation, combine fields and derivatives so that every term transforms consistently ([tensor appendix](appendix-math-tensors.md#_4-covariant-and-contravariant-indices)). The familiar free equations follow from the simplest choices for these field types.

For the free fields considered here, we use Klein–Gordon for scalars, Dirac for spinors, and Maxwell for the electromagnetic field. These equations determine how the modes evolve; quantization will determine how many particles occupy them.

<details>
<summary>The free equations for the three field types</summary>

**Scalar field.** A derivative combination that transforms as a scalar is $\Box = \partial_\mu\partial^\mu = \partial_t^2 - \nabla^2$. Combining it with a mass term gives

$$\left(\Box + \frac{m^2}{\hbar^2}\right)\phi = 0,$$

This is the Klein–Gordon equation from [Relativistic QM §3](relativistic-qm.md#_3-the-klein–gordon-equation), with dispersion relation $E^2 = \mathbf p^2 + m^2$.

Its earlier difficulty concerned interpreting the conserved density as a single-particle probability density. A classical field $\phi$ is not a probability amplitude, so that interpretation is unnecessary here.

**Spinor field.** The spinor transformation $S(\Lambda)$ and the gamma matrices from [the Dirac reference page §2](dirac-reference.md#_2-the-notation-later-chapters-use) satisfy a compatibility relation. As a result, the derivative term $\gamma^\mu\partial_\mu\psi$ transforms as a spinor, just like $\psi$. We can combine them as

$$(i\hbar\,\gamma^\mu\partial_\mu - m)\psi = 0,$$

The Dirac equation is first order in both time and space. [Relativistic QM §6](relativistic-qm.md#_6-dirac-s-idea-an-energy-rule-that-isn-t-squared) introduced it to obtain a positive single-particle density. We now use the same equation for a field with spin and antiparticle modes.

**Vector field.** The electromagnetic potential $A^\mu$ enters the field tensor $F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu$ from [Special Relativity §7](special-relativity.md#maxwell-s-equations-in-four-vector-form). In empty space,

$$\partial_\mu F^{\mu\nu} = 0 \quad\Longleftrightarrow\quad \Box A^\nu - \partial^\nu(\partial_\mu A^\mu) = 0,$$

These are the source-free Maxwell equations. Their physical waves propagate at $c$, corresponding to massless photons. A massive vector field instead satisfies $\partial_\mu F^{\mu\nu} + \tfrac{m^2}{\hbar^2}A^\nu = 0$. The transformation law alone does not fix the mass.

</details>

### Free scalar modes and the vacuum

The harmonic-oscillator picture gives a concrete way to quantize a free
scalar field. Fourier-expand one spatial snapshot as

$$\phi(t,\mathbf x)=\int\frac{d^3k}{(2\pi)^3}\,q_{\mathbf k}(t)e^{i\mathbf k\cdot\mathbf x}.$$

The quadratic free-field Hamiltonian becomes a sum of oscillator Hamiltonians,
one for each independent Fourier mode:

$$H=\sum_{\mathbf k}\hbar\omega_{\mathbf k}
\left(\hat a^\dagger_{\mathbf k}\hat a_{\mathbf k}+\tfrac12\right),
\qquad \omega_{\mathbf k}=\sqrt{|\mathbf k|^2+m^2}/\hbar.$$

The vacuum is the state in which every mode occupies its oscillator ground
state:

$$\hat a_{\mathbf k}|0\rangle=0\qquad\text{for every }\mathbf k.$$

The modes are **independent oscillators only for a free quadratic theory**,
and “independent” refers to the diagonalization of the Hamiltonian, not to
separate physical fields. A real field also obeys
$q_{-\mathbf k}=q_{\mathbf k}^*$, so the $\mathbf k$ and $-\mathbf k$ terms
are not two independent real modes. Interactions couple modes together. For
example, a $\lambda\phi^4$ term produces products of four Fourier amplitudes
whose momenta satisfy an overall conservation condition.

Each oscillator has a formal zero-point contribution
$\tfrac12\hbar\omega_{\mathbf k}$. In nongravitational QFT we normally
normal-order the Hamiltonian and measure energy relative to the vacuum, so
the vacuum energy is set to zero. Its absolute value becomes important when
gravity is included.

![A spatial scalar-field profile decomposes into Fourier modes, with each free mode behaving like a harmonic oscillator.](./manim/field-modes.png)

*A spatial field profile is built from Fourier modes. The oscillator picture
applies to the modes of a free field; interactions can couple them.*

The same idea can be pictured in position space by putting one local field
coordinate at each point of a spatial lattice. This is a useful visualization
of a configuration, but the local oscillators are not independent: the
gradient term in the Hamiltonian couples neighboring values. The independent
oscillators of the free theory appear after changing to Fourier modes.

This also separates the classical and quantum meanings of “vacuum.” A
classical field might have the lowest-energy configuration
$\phi_{\mathrm{cl}}(x,y)=0$ everywhere. The quantum vacuum is instead a
state $|0\rangle$. It has zero mean field,
$\langle0|\hat\phi(x)|0\rangle=0$, but nonzero fluctuations,
$\langle0|\hat\phi(x)^2|0\rangle>0$. Thus it is not the statement that the
field has the definite value zero everywhere; it is the ground state of all
the coupled degrees of freedom, or equivalently of the independent Fourier
modes.

![A lattice visualization of a scalar-field configuration, with a tiny local oscillator at each spatial point and couplings between neighbors.](./manim/scalar-vacuum-configuration.png)

*Each lattice site carries a local field coordinate. The connecting lines
show why these local oscillators are coupled; Fourier transformation finds the
independent normal modes in the free theory.*

We have met these equations before: Klein–Gordon in [Relativistic QM §3](relativistic-qm.md#_3-the-klein–gordon-equation), Dirac in [The Dirac Equation](dirac-equation.md), and Maxwell in classical electromagnetism. Here all three describe fields whose quantized excitations are particles.

The relation between transformation law and spin is the one developed in [the Dirac reference page §2](dirac-reference.md#_2-the-notation-later-chapters-use). The Higgs is another scalar example; its full description involves interactions beyond the free equations considered here.

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

We can place time dependence in the states or in the operators. These are two equivalent descriptions of the same predictions. [the Dirac reference page §2](dirac-reference.md#_2-the-notation-later-chapters-use) already used the second description to derive $d\hat A/dt = \tfrac{i}{\hbar}[\hat H,\hat A]$.

In the **Schrödinger picture**, states evolve. Operators without explicit time dependence stay fixed:

$$|\Psi_S(t)\rangle = e^{-i\hat H t/\hbar}\,|\Psi_S(0)\rangle, \qquad \hat O_S \;\text{ fixed};$$

In the **Heisenberg picture**, states stay fixed in time and operators evolve:

$$|\Psi_H\rangle \;\text{ fixed}, \qquad \hat\phi(t, \mathbf x) = e^{i\hat H t/\hbar}\,\hat\phi(0, \mathbf x)\,e^{-i\hat H t/\hbar}.$$

<details>
<summary>Checking that the two pictures give the same expectation values</summary>

The plus sign on the left comes from taking the adjoint of the time-evolution operator in [First Quantization](first-quantization.md). The ket evolves with $e^{-i\hat Ht/\hbar}$, while the bra evolves with $e^{+i\hat Ht/\hbar}$.

Moving both factors onto the operator gives the Heisenberg expression differentiated in [the Dirac reference page §2](dirac-reference.md#_2-the-notation-later-chapters-use). The expectation values agree:

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

This does not invalidate Schrödinger evolution. It means that covariance involves transforming the slice as well as the state. The first-order Dirac equation from [Relativistic QM §7](relativistic-qm.md#_7-the-dirac-equation) does not remove this distinction.

In the Heisenberg picture, the field already carries a spacetime label. With a consistent convention, a scalar transforms as $\hat U(\Lambda)\hat\phi(x)\hat U^{-1}(\Lambda)=\hat\phi(\Lambda x)$; vector and spinor fields also acquire their component matrices. We can therefore express covariance directly through local field transformations. States remain fixed under time evolution in this picture, though they still transform when we change reference frame.

The free field operators obey the same wave equations as the classical fields: Klein–Gordon for $\hat\phi(x)$ ([Relativistic QM §3](relativistic-qm.md#_3-the-klein–gordon-equation)) and Dirac for $\hat\psi(x)$ ([The Dirac Equation](dirac-equation.md)). Quantization changes the amplitudes into operators; it preserves these free equations.

The field types differ in their operator algebra. Integer-spin fields use commutators, while half-integer-spin fields use anticommutators. The constructions ahead illustrate this spin–statistics connection; we give the general result without proof because its derivation requires a longer treatment of relativistic locality and positive-norm states.

We can now construct the operator algebra, the state space, and the Hamiltonian. In particular, we must check that energy has a lower bound, resolving the problem in [Relativistic QM §4](relativistic-qm.md#_4-first-problem-negative-energies).

The [next page](qft-action.md) starts with the scalar field and its action. The [Field Quantization page](field-quantization.md#the-spinor-field) develops the spinor algebra. The photon also has gauge redundancy, which we handle on the [QED page](qed.md#quantizing-the-gauge-fixed-field).
