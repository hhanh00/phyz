# Exercises

## Classical Mechanics

<details>
<summary>What is the Newtonian formulation of classical mechanics?</summary>

Newton's formulation describes motion through forces. For a particle of constant mass, Newton's second law gives

$$\mathbf F_{\mathrm{net}}=m\mathbf a=m\frac{d^2\mathbf x}{dt^2}.$$

Once we know the force law and the particle's initial position and velocity, we solve this second-order differential equation to find its trajectory $\mathbf x(t)$. Integrating the acceleration once gives the velocity, and integrating it again gives the position.

</details>

<details>
<summary>What is the principle of stationary action?</summary>

The **Lagrangian** is a function of the system's generalized coordinates, velocities, and time:

$$L(q_i,\dot q_i,t)=T-V,$$

for an ordinary mechanical system with kinetic energy $T$ and potential energy $V$.

The **action** assigns a number to each possible path between two fixed times:

$$S[q]=\int_{t_i}^{t_f}L(q_i,\dot q_i,t)\,dt.$$

The physical path makes the action **stationary**. For every small variation of the path that leaves its endpoints fixed, the first-order change in the action vanishes:

$$\delta S=0.$$

Stationary does not always mean smallest; the action can also have a maximum or another stationary value. Applying $\delta S=0$ gives the Euler–Lagrange equations,

$$\frac{d}{dt}\left(\frac{\partial L}{\partial\dot q_i}\right)-\frac{\partial L}{\partial q_i}=0,$$

which determine the system's motion.

</details>

<details>
<summary>How do we derive the Euler–Lagrange equations from stationary action?</summary>

We want to derive

$$\frac{d}{dt}\left(\frac{\partial L}{\partial\dot q_i}\right)-\frac{\partial L}{\partial q_i}=0.$$

Consider a small variation of the physical path,

$$q_i(t)\rightarrow q_i(t)+\epsilon\eta_i(t),$$

where $\epsilon$ is small and $\eta_i(t_i)=\eta_i(t_f)=0$, so the endpoints remain fixed. The corresponding variation of the velocity is

$$\delta\dot q_i=\frac{d}{dt}(\delta q_i).$$

The action is

$$S[q]=\int_{t_i}^{t_f}L(q_i,\dot q_i,t)\,dt.$$

Its first-order variation is

$$\delta S=\int_{t_i}^{t_f}\left(
\frac{\partial L}{\partial q_i}\delta q_i
+\frac{\partial L}{\partial\dot q_i}\delta\dot q_i
\right)dt,$$

where repeated $i$ indices are summed. Substitute $\delta\dot q_i=d(\delta q_i)/dt$ and integrate the second term by parts:

$$\delta S=
\left[\frac{\partial L}{\partial\dot q_i}\delta q_i\right]_{t_i}^{t_f}
+\int_{t_i}^{t_f}\left[
\frac{\partial L}{\partial q_i}
-\frac{d}{dt}\left(\frac{\partial L}{\partial\dot q_i}\right)
\right]\delta q_i\,dt.$$

The boundary term vanishes because $\delta q_i(t_i)=\delta q_i(t_f)=0$. Stationary action requires $\delta S=0$, so

$$\int_{t_i}^{t_f}\left[
\frac{\partial L}{\partial q_i}
-\frac{d}{dt}\left(\frac{\partial L}{\partial\dot q_i}\right)
\right]\delta q_i\,dt=0.$$

The variations $\delta q_i(t)$ are arbitrary between the endpoints. Therefore, their coefficient must vanish at every time:

$$\frac{d}{dt}\left(\frac{\partial L}{\partial\dot q_i}\right)-\frac{\partial L}{\partial q_i}=0.$$

These are the Euler–Lagrange equations.

</details>

<details>
<summary>What are generalized coordinates and canonical momenta?</summary>

**Generalized coordinates** $q_i$ are independent variables that specify a system's configuration. They need not be Cartesian positions. For example, a pendulum can be described by one generalized coordinate, its angle $q=\theta$, rather than by the bob's Cartesian coordinates subject to a length constraint. Their time derivatives $\dot q_i$ are the generalized velocities.

The **canonical momentum** conjugate to $q_i$ is defined from the Lagrangian by

$$p_i=\frac{\partial L}{\partial\dot q_i}.$$

Canonical momentum does not always equal mechanical momentum $m\dot q_i$. The two agree for a Cartesian coordinate with the Lagrangian $L=\tfrac12m\dot q_i^2-V(q)$, but constraints or velocity-dependent interactions can change the relation.
</details>

<details>
<summary>What is the Hamiltonian?</summary>
The **Hamiltonian** replaces the generalized velocities $\dot q_i$ with the canonical momenta $p_i$. It is the Legendre transform of the Lagrangian:

$$H(q_i,p_i,t)=\sum_i p_i\dot q_i-L(q_i,\dot q_i,t),$$

where the velocities on the right must be expressed in terms of $q_i$, $p_i$, and $t$.
</details>

<details>
<summary>What are the time evolution equations of the Hamiltonian?</summary>

The Hamiltonian generates time evolution through Hamilton's equations,

$$\dot q_i=\frac{\partial H}{\partial p_i},
\qquad
\dot p_i=-\frac{\partial H}{\partial q_i}.$$

For the common Lagrangian $L=T-V$ with Cartesian coordinates and a velocity-independent potential,

$$H=T+V,$$

so the Hamiltonian equals the system's total energy. This equality does not hold for every possible Lagrangian.
</details>

## Quantum Mechanics

<details>
<summary>What is a quantum state, and how do we represent it?</summary>

A quantum state contains all the information that quantum mechanics can use to predict the outcomes of measurements. We represent a pure state by a normalized vector $|\psi\rangle$ in a complex Hilbert space:

$$\langle\psi|\psi\rangle=1.$$

Two vectors that differ only by an overall phase, $|\psi\rangle$ and $e^{i\alpha}|\psi\rangle$, represent the same physical state. In the position basis, the state is represented by the wave function

$$\psi(x,t)=\langle x|\psi(t)\rangle.$$
</details>

<details>
<summary>What is an observable?</summary>

An observable is a measurable physical quantity, such as position, momentum, energy, or spin. Quantum mechanics represents observables by **self-adjoint linear operators** (Hermitian matrices in finite-dimensional Hilbert spaces). Self-adjoint operators have real eigenvalues, so their possible measured values are real.

</details>

<details>
<summary>What are eigenvalues and eigenstates?</summary>

An **eigenstate** of an observable $\hat A$ is a state whose direction does not change when the operator acts on it:

$$\hat A|a_n\rangle=a_n|a_n\rangle.$$

Here, $|a_n\rangle$ is the eigenstate and $a_n$ is its eigenvalue. If the system is in $|a_n\rangle$, measuring $A$ gives $a_n$ with certainty. For example, an energy eigenstate satisfies

$$\hat H|E_n\rangle=E_n|E_n\rangle.$$

</details>

<details>
<summary>How can a quantum state be expanded in an observable’s eigenbasis?</summary>

If an observable has orthonormal eigenstates $|a_n\rangle$, we can expand the state as

$$|\psi\rangle=\sum_n c_n|a_n\rangle.$$

</details>

<details>
<summary>What is the Born rule?</summary>
The Born rule assigns probability

$$P(a_n)=|c_n|^2=|\langle a_n|\psi\rangle|^2$$

to obtaining the value $a_n$ in a measurement.

</details>

<details>
<summary>How does a quantum state evolve between measurements?</summary>

Between measurements, the state evolves according to the Schrödinger equation,

$$i\hbar\frac{d}{dt}|\psi(t)\rangle=\hat H|\psi(t)\rangle.$$
</details>

<details>
<summary>What are the position and momentum operators?</summary>

In the position representation, the **position operator** multiplies the wave function by $x$:

$$\hat x\,\psi(x)=x\psi(x).$$

The **momentum operator** differentiates the wave function:

$$\hat p\,\psi(x)=-i\hbar\frac{d\psi(x)}{dx}.$$

In three dimensions,

$$\hat{\mathbf x}=\mathbf x,
\qquad
\hat{\mathbf p}=-i\hbar\nabla.$$

They satisfy the canonical commutation relation

$$[\hat x,\hat p]=i\hbar,$$

which leads to the position–momentum uncertainty relation

$$\Delta x\,\Delta p\geq\frac{\hbar}{2}.$$

</details>

## Harmonic Oscillator

<details>
<summary>What force defines a harmonic oscillator?</summary>

A **harmonic oscillator** is a system whose restoring force is proportional to its displacement from equilibrium and points back toward equilibrium:

$$F=-kx.$$

</details>

<details>
<summary>What is the classical equation of motion and angular frequency of a harmonic oscillator?</summary>

Its classical equation of motion is

$$m\ddot x+kx=0,$$

so it oscillates sinusoidally with angular frequency

$$\omega=\sqrt{\frac{k}{m}}.$$

</details>

<details>
<summary>What is the Hamiltonian of a harmonic oscillator?</summary>
The Hamiltonian is

$$H=\frac{p^2}{2m}+\frac12m\omega^2x^2.$$

</details>

<details>
<summary>What are the energy levels of the quantum harmonic oscillator?</summary>
In quantum mechanics, the oscillator has discrete energy levels:

$$E_n=\hbar\omega\left(n+\frac12\right),
\qquad n=0,1,2,\ldots.$$

</details>

<details>
<summary>What is zero-point energy, and why does the harmonic oscillator appear throughout physics?</summary>

Its lowest state has the nonzero zero-point energy $E_0=\tfrac12\hbar\omega$. The harmonic oscillator appears throughout physics because a smooth potential near a stable equilibrium is approximately quadratic.

</details>

<details>
<summary>What potential defines the quantum harmonic oscillator?</summary>

The **quantum harmonic oscillator** is the quantum description of a particle moving in the quadratic potential

$$V(x)=\frac12m\omega^2x^2.$$

</details>

<details>
<summary>What is the Hamiltonian operator of the quantum harmonic oscillator?</summary>
Its Hamiltonian is

$$\hat H=\frac{\hat p^2}{2m}+\frac12m\omega^2\hat x^2.$$

</details>

<details>
<summary>What energy eigenvalue equation and spectrum does the quantum harmonic oscillator have?</summary>
Solving the time-independent Schrödinger equation,

$$\hat H|n\rangle=E_n|n\rangle,$$

gives discrete, equally spaced energy levels:

$$E_n=\hbar\omega\left(n+\frac12\right),
\qquad n=0,1,2,\ldots.$$

</details>

<details>
<summary>What are the quantum harmonic oscillator's ground-state energy and ladder operators, and why is the model important?</summary>

The ground state has energy $E_0=\tfrac12\hbar\omega$, so the oscillator never has zero energy. Ladder operators move between adjacent energy states:

$$\hat a^\dagger|n\rangle=\sqrt{n+1}\,|n+1\rangle,
\qquad
\hat a|n\rangle=\sqrt n\,|n-1\rangle.$$

The model matters because many systems behave approximately like harmonic oscillators near stable equilibria. Each mode of a free quantum field also behaves like a quantum harmonic oscillator.

</details>

<details>
<summary>If ω can have any value, how is the quantum harmonic oscillator's energy quantized?</summary>

The frequency $\omega$ can be any positive value because it is a parameter that defines the particular oscillator:

$$\omega=\sqrt{\frac{k}{m}}.$$

Once $m$, $k$, and therefore $\omega$ are fixed, that oscillator can have only the discrete energies

$$E_n=\hbar\omega\left(n+\frac12\right),
\qquad n=0,1,2,\ldots.$$

Across different oscillators, the energy scale can vary continuously with $\omega$. For one fixed oscillator, however, the allowed energies remain discrete and adjacent levels differ by $\hbar\omega$. Quantization restricts the level number $n$, not the externally specified parameter $\omega$.

</details>

## Special Relativity

<details>
<summary>What are the two postulates of special relativity?</summary>

The **principle of relativity** states that the laws of physics have the same form in every inertial frame. The **invariance of the speed of light** states that every inertial observer measures the same vacuum light speed $c$, regardless of the source's motion.

</details>

<details>
<summary>Why do Lorentz transformations replace Galilean transformations?</summary>

Galilean transformations preserve absolute time and use ordinary velocity addition, which would make different observers measure different light speeds. Lorentz transformations preserve $c$ by mixing space and time:

$$t'=\gamma\left(t-\frac{vx}{c^2}\right),
\qquad
x'=\gamma(x-vt),
\qquad
\gamma=\frac{1}{\sqrt{1-v^2/c^2}}.$$

</details>

<details>
<summary>What is the invariant spacetime interval?</summary>

Observers can disagree about simultaneity, elapsed time, and spatial distance, but they agree on the spacetime interval

$$s^2=c^2\Delta t^2-\Delta x^2-\Delta y^2-\Delta z^2.$$

The sign of $s^2$ classifies event separations as timelike, lightlike, or spacelike and determines whether one event can causally influence another.

</details>

<details>
<summary>What are four-vectors and Lorentz scalars?</summary>

Four-vectors combine time and space components into objects that transform consistently between inertial frames. With the Minkowski metric $\eta_{\mu\nu}=\operatorname{diag}(+1,-1,-1,-1)$, contracting an upper and lower index produces a **Lorentz scalar**, whose value every inertial observer agrees on.

</details>

<details>
<summary>What is the relativistic energy–momentum relation?</summary>

The four-momentum is

$$p^\mu=\left(\frac{E}{c},\mathbf p\right)$$

and has the invariant norm $p^\mu p_\mu=m^2c^2$. Therefore,

$$E^2=(mc^2)^2+(pc)^2.$$

This relation reduces to $E=mc^2$ for a massive particle at rest and to $E=pc$ for a massless particle.

</details>

<details>
<summary>Why are Maxwell's equations compatible with special relativity?</summary>

Relativistic equations must retain their form under Lorentz transformations. Maxwell's equations meet this requirement when written using the four-current $J^\mu$ and electromagnetic field tensor $F^{\mu\nu}$:

$$\partial_\mu F^{\mu\nu}=J^\nu.$$

Electric and magnetic fields form parts of one relativistic field and can mix under a boost.

</details>

<details>
<summary>Why is the Schrödinger equation not Lorentz covariant?</summary>

The Schrödinger equation treats time and space derivatives differently, so its form changes when a Lorentz boost mixes space and time. It also uses the non-relativistic relation $E=\mathbf p^2/(2m)$. Starting instead from the exact relativistic energy–momentum relation leads toward the Klein–Gordon and Dirac equations.

</details>

## Relativistic QM

<details>
<summary>What's the plane wave solution for a free particle of momentum p and energy E?</summary>

A free particle with definite momentum $\mathbf p$ and energy $E$ has the plane-wave form

$$\psi(\mathbf x,t)=e^{i(\mathbf p\cdot\mathbf x-Et)/\hbar}.$$

Substituting this form into a wave equation determines the equation's relation between energy and momentum, called its **dispersion relation**. An exact plane wave extends across all space, so a localized particle requires a wave packet built from many momenta.

</details>

<details>
<summary>Why does relativistic quantum mechanics require a new wave equation?</summary>

The Schrödinger equation uses the non-relativistic kinetic energy $E=\mathbf p^2/(2m)$. Special relativity instead gives the exact relation

$$E^2=\mathbf p^2+m^2$$

in units where $c=1$. A relativistic wave equation must reproduce this relation and retain the same form under Lorentz transformations.

</details>

<details>
<summary>How do we obtain the Klein–Gordon equation?</summary>

Replace energy and momentum in the relativistic relation with their quantum operators:

$$E\rightarrow i\hbar\partial_t,
\qquad
\mathbf p\rightarrow-i\hbar\nabla.$$

This gives

$$\left(\Box+\frac{m^2}{\hbar^2}\right)\psi=0,
\qquad
\Box=\partial_t^2-\nabla^2.$$

The d'Alembertian $\Box=\partial_\mu\partial^\mu$ is a Lorentz scalar, so the Klein–Gordon equation has the same form in every inertial frame.

</details>

<details>
<summary>What difficulties arise from the Klein–Gordon equation?</summary>

A plane wave satisfies

$$E=\pm\sqrt{\mathbf p^2+m^2}.$$

If the negative branch described ordinary one-particle energies, the spectrum would have no lower bound. The equation is also second order in time, so an initial state requires both $\psi$ and $\partial_t\psi$. In contrast, the first-order Schrödinger equation determines the future state from $\psi$ alone.

</details>

<details>
<summary>Why is the Klein–Gordon conserved density not an ordinary probability density?</summary>

The conserved Klein–Gordon current is

$$j^\mu=i\left(\psi^*\partial^\mu\psi-\psi\partial^\mu\psi^*\right),
\qquad
\partial_\mu j^\mu=0.$$

For a plane wave, its time component is

$$j^0=\frac{2E}{\hbar}|\psi|^2.$$

This density changes sign with $E$, so it cannot represent a nonnegative probability for all solutions. In quantum field theory, the conserved quantity instead becomes charge, which can have either sign.

</details>

<details>
<summary>How is the Dirac equation constructed from the relativistic energy relation?</summary>

Dirac sought an equation that is first order in both time and space:

$$i\hbar\partial_t\psi=\left(-i\hbar\boldsymbol\alpha\cdot\nabla+\beta m\right)\psi.$$

Requiring its square to reproduce $E^2=\mathbf p^2+m^2$ gives

$$\beta^2=1,
\qquad
\{\alpha_i,\beta\}=0,
\qquad
\{\alpha_i,\alpha_j\}=2\delta_{ij}.$$

Ordinary numbers cannot satisfy these relations. The coefficients must be matrices, and in three spatial dimensions the wave function becomes a four-component spinor. Defining $\gamma^0=\beta$ and $\gamma^i=\beta\alpha_i$ gives the covariant equation

$$(i\hbar\gamma^\mu\partial_\mu-m)\psi=0.$$

</details>

<details>
<summary>What does the Dirac equation resolve, and what still requires quantum field theory?</summary>

The Dirac equation has the conserved current

$$j^\mu=\bar\psi\gamma^\mu\psi,$$

whose time component is

$$j^0=\psi^\dagger\psi\geq0.$$

It therefore provides a nonnegative single-particle density and naturally introduces spin-$\tfrac12$. However, it still has positive- and negative-energy solutions. Quantum field theory completes the interpretation by treating negative-frequency modes as antiparticles with positive excitation energy and by allowing particles to be created and destroyed.

</details>

## Dirac Equation

<details>
<summary>What is the Dirac equation?</summary>

The Dirac equation is a relativistic wave equation for spin-$\tfrac12$ particles:

$$(i\hbar\gamma^\mu\partial_\mu-m)\psi=0.$$

The wave function $\psi$ is a four-component spinor, and the gamma matrices satisfy

$$\{\gamma^\mu,\gamma^\nu\}=2\eta^{\mu\nu}\mathbb 1.$$

This algebra ensures that solutions obey the relativistic energy–momentum relation $E^2=\mathbf p^2+m^2$ in units where $c=1$.

</details>

<details>
<summary>How does spin arise from the Dirac equation?</summary>

For the free Dirac Hamiltonian

$$H=\boldsymbol\alpha\cdot\hat{\mathbf p}+\beta m,$$

orbital angular momentum $\mathbf L$ is not conserved by itself. The Dirac components carry intrinsic angular momentum described by

$$\mathbf S=\frac{\hbar}{2}\boldsymbol\Sigma,
\qquad
\Sigma_i=\operatorname{diag}(\sigma_i,\sigma_i).$$

The total angular momentum $\mathbf J=\mathbf L+\mathbf S$ is conserved because $[H,\mathbf J]=0$. Since $S_z$ has eigenvalues $\pm\hbar/2$, the Dirac equation describes spin-$\tfrac12$ particles.

</details>

<details>
<summary>How do commutators identify conserved observables?</summary>

For an operator $A$ with no explicit time dependence, the Heisenberg equation gives

$$\frac{dA}{dt}=\frac{i}{\hbar}[H,A].$$

An observable is conserved in every state when it commutes with the Hamiltonian. In the Dirac theory, $[H,\mathbf L]\ne0$, but $[H,\mathbf L+\mathbf S]=0$, so spin and orbital angular momentum can change separately while their sum remains constant.

</details>

<details>
<summary>How does the Dirac equation predict the electron's magnetic moment?</summary>

Minimal coupling replaces momentum by

$$\hat{\mathbf p}\rightarrow\hat{\mathbf p}-q\mathbf A.$$

Taking the non-relativistic limit then produces the Pauli equation and the magnetic moment

$$\boldsymbol\mu=\frac{q}{m}\mathbf S.$$

Comparing this with $\boldsymbol\mu=g\,q\mathbf S/(2m)$ gives $g=2$. For an electron, $q=-e$, so $\boldsymbol\mu=-(e/m)\mathbf S$.

</details>

<details>
<summary>What positive- and negative-energy solutions does the Dirac equation have?</summary>

For each momentum, the free Dirac equation has energies

$$E=\pm E_p,
\qquad
E_p=\sqrt{\mathbf p^2+m^2}.$$

Each energy sign has two independent spin states. At rest in the standard representation, the positive-energy solutions occupy the upper pair of spinor components, while the negative-energy solutions occupy the lower pair. Motion mixes the upper and lower components. We denote the positive-energy spinors by $u_s(p)$ and the negative-energy spinors by $v_s(p)$.

</details>

<details>
<summary>How are negative-energy solutions related to antiparticles?</summary>

Charge conjugation maps a particle solution to an antiparticle solution:

$$\psi_c=i\gamma^2\psi^*.$$

Complex conjugation reverses the sign of the electromagnetic charge, so the transformed solution has the same mass and opposite charge. For the electron, this antiparticle is the positron.

A one-particle theory cannot consistently treat negative-energy solutions as ordinary electron states because the energy would have no lower bound. Quantum field theory instead interprets the negative-frequency terms as operators that create positive-energy antiparticles.

</details>

<details>
<summary>How do Dirac spinors transform under Lorentz transformations?</summary>

When coordinates transform as $x'=\Lambda x$, a Dirac spinor transforms as

$$\psi'(x')=S(\Lambda)\psi(x),
\qquad
S(\Lambda)=\exp\left(-\frac{i}{4}\omega_{\mu\nu}\sigma^{\mu\nu}\right),$$

where

$$\sigma^{\mu\nu}=\frac{i}{2}[\gamma^\mu,\gamma^\nu].$$

A $2\pi$ rotation changes the sign of a spinor, while a $4\pi$ rotation returns it to its original value. The four-component Dirac spinor can also be separated into left- and right-handed Weyl spinors, which transform alike under rotations and oppositely under boosts.

</details>

<details>
<summary>What is the general free solution of the Dirac equation?</summary>

The general solution superposes every momentum, both spin states, and both frequency signs:

$$\psi(x)=\sum_{s=1}^{2}\int\frac{d^3p}{(2\pi\hbar)^3}\frac{1}{\sqrt{2E_p}}
\left[a_s(p)u_s(p)e^{-ip\cdot x/\hbar}+b_s^*(p)v_s(p)e^{+ip\cdot x/\hbar}\right].$$

In one-particle quantum mechanics, $a_s$ and $b_s^*$ are numerical amplitudes fixed by the initial state. Quantum field theory promotes them to operators: $a_s$ annihilates a particle, while $b_s^*\rightarrow\hat b_s^\dagger$ creates an antiparticle.

</details>

## Fields and Quanta

<details>
<summary>What is a classical field?</summary>

A **classical field** assigns a physical value to every point in spacetime:

$$\phi:x^\mu\mapsto\phi(x).$$

A temperature field assigns a number to each point, while the electromagnetic field assigns electric and magnetic vectors. A classical field has a definite configuration, follows classical field equations, and is not an operator.

</details>

<details>
<summary>What is a quantum field?</summary>

A **quantum field** is an operator-valued field defined throughout spacetime:

$$x^\mu\mapsto\hat\phi(x).$$

Unlike a classical field, it does not assign one definite physical value to each point. Instead, it acts on quantum states.
</details>

<details>
<summary>Is a quantum field an operator?</summary>

Informally, a quantum field is an operator-valued field. More precisely, it is an **operator-valued distribution**, not an ordinary operator assigned independently to each exact point.

The notation $\hat\phi(x)$ treats the field at $x$ like an operator, but it can be singular at an exact spacetime point. Averaging, or **smearing**, it with a smooth function $f(x)$ gives a well-defined operator:

$$\hat\phi(f)=\int d^4x\,f(x)\hat\phi(x).$$

This smeared field acts on states in Fock space.

</details>

<details>
<summary>In QM, a state belongs to a Hilbert space. What about in QFT?</summary>

In QFT, a state also belongs to a **Hilbert space**. For free fields and perturbative particle descriptions, this is usually a **Fock space**:

$$|\Psi\rangle\in\mathcal F,
\qquad
\mathcal F=\mathcal H_0\oplus\mathcal H_1\oplus\mathcal H_2\oplus\cdots.$$

Here, $\mathcal H_0$ contains the vacuum, $\mathcal H_1$ contains one-particle states, and $\mathcal H_2$ contains two-particle states. Creation and annihilation operators move states between these sectors:

$$a^\dagger:\mathcal H_n\rightarrow\mathcal H_{n+1},
\qquad
a:\mathcal H_n\rightarrow\mathcal H_{n-1}.$$

Thus, QM and QFT both use Hilbert spaces, but QFT needs a state space that allows particle number to change. A general interacting QFT still uses a Hilbert space, although it may not decompose cleanly into free-particle sectors.

</details>

<details>
<summary>How does quantum field theory describe particles?</summary>

Quantum field theory assigns a field to every point in spacetime. A field can be a scalar, vector, or spinor depending on how its values transform. After quantization, each momentum mode behaves like a quantum oscillator, and applying creation operators produces particle excitations. Particles are therefore discrete quanta of fields, while the field remains the fundamental object.

</details>

<details>
<summary>How do scalar, vector, and spinor fields differ?</summary>

They differ in the type of value assigned to each spacetime point and in how that value transforms. A scalar has one Lorentz-invariant component, a vector has components that mix like spacetime coordinates, and a spinor follows the spin-$\tfrac12$ transformation law. These properties determine which Lorentz-invariant terms can appear in a field theory.

</details>

<details>
<summary>How do spacetime and value spaces play different roles?</summary>

Spacetime labels where a field is evaluated; the value space specifies what lives at that point. A Lorentz transformation changes spacetime coordinates and also acts on vector or spinor components through the appropriate representation. Keeping these actions distinct prevents confusion between moving a point and transforming a field value.

</details>

<details>
<summary>What is the Heisenberg picture?</summary>

In the **Heisenberg picture**, quantum states stay fixed while operators evolve with time:

$$|\psi_H\rangle=\text{constant},
\qquad
\hat A_H(t)=e^{i\hat Ht/\hbar}\hat A_H(0)e^{-i\hat Ht/\hbar}.$$

Their evolution obeys

$$\frac{d\hat A_H}{dt}=\frac{i}{\hbar}[\hat H,\hat A_H]+\frac{\partial\hat A_H}{\partial t}.$$

In QFT, the field operator $\hat\phi(x)$ evolves and obeys the field equation while the state remains fixed. In the Schrödinger picture, operators are usually fixed and states obey $i\hbar\,d|\psi_S\rangle/dt=\hat H|\psi_S\rangle$. Both pictures give the same measurement predictions.

</details>

## Action and Lagrangians

<details>
<summary>How do the action and Euler–Lagrange equations work for fields?</summary>

A field theory uses a Lagrangian density $\mathcal L(\phi,\partial_\mu\phi)$ and action

$$S=\int d^4x\,\mathcal L.$$

Requiring stationary action gives the field Euler–Lagrange equation

$$\partial_\mu\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}-\frac{\partial\mathcal L}{\partial\phi}=0.$$

Choosing a Lorentz-scalar density makes the resulting equations covariant.

</details>

<details>
<summary>What Lagrangian density gives the Klein–Gordon equation?</summary>

For a real scalar field,

$$\mathcal L=\frac12\partial_\mu\phi\,\partial^\mu\phi-\frac12m^2\phi^2.$$

The field Euler–Lagrange equation gives $(\Box+m^2)\phi=0$. The derivative term governs propagation, while the quadratic term sets the particle mass.

</details>

<details>
<summary>How does a field variation differ from a particle-path variation?</summary>

For a particle, the unknown is a path such as $q(t)$. Test the path by changing it slightly:

$$q(t)\rightarrow q(t)+\delta q(t).$$

For a field, the unknown is a value at every spacetime point, $\phi(x)$. Change the entire field slightly:

$$\phi(x)\rightarrow\phi(x)+\delta\phi(x).$$

Keep $\delta\phi=0$ at the boundary because the starting and ending configurations are fixed. Requiring the action to be stationary for every allowed change gives

$$\partial_\mu\left(\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\right)-\frac{\partial\mathcal L}{\partial\phi}=0.$$

The main difference is that we vary an entire function $\phi(x)$ rather than a finite list of coordinates.

</details>

<details>
<summary>What is the difference between a Lagrangian and a Lagrangian density?</summary>

The density $\mathcal L$ is local in spacetime. Integrating it over space gives the Lagrangian, $L=\int d^3x\,\mathcal L$, and integrating that over time gives the action, $S=\int d^4x\,\mathcal L$.

</details>

<details>
<summary>Why should the Lagrangian density be a Lorentz scalar?</summary>

If $\mathcal L$ is a Lorentz scalar, every inertial observer assigns the same value to the action. Its stationary configurations then obey field equations with the same form in every inertial frame.

</details>

<details>
<summary>How are the conjugate momentum and Hamiltonian defined for a field?</summary>

Define

$$\pi=\frac{\partial\mathcal L}{\partial\dot\phi},
\qquad
\mathcal H=\pi\dot\phi-\mathcal L,
\qquad
H=\int d^3x\,\mathcal H.$$

After quantization, $\hat H$ generates time evolution.

</details>

<details>
<summary>What is the state space of a classical field?</summary>

A state on one time slice is the pair of functions $(\phi(\mathbf x),\pi(\mathbf x))$. Because it contains one conjugate pair at every spatial point, the state space is infinite-dimensional.

</details>

<details>
<summary>What two roles does the field Hamiltonian play?</summary>

It assigns energy to a field configuration and generates its time evolution. When the action has time-translation symmetry, Noether's theorem connects these roles by making the energy conserved.

</details>

<details>
<summary>What Lagrangian density gives the source-free Maxwell equations?</summary>

For the electromagnetic potential,

$$\mathcal L=-\frac14F_{\mu\nu}F^{\mu\nu}.$$

Varying $A_\nu$ gives $\partial_\mu F^{\mu\nu}=0$. The absence of an $A_\mu A^\mu$ term keeps the photon massless.

</details>

<details>
<summary>Why does the Dirac Lagrangian use the Dirac adjoint?</summary>

The density $\psi^\dagger\psi$ is the time component of a current, not a Lorentz scalar. Defining $\bar\psi=\psi^\dagger\gamma^0$ makes $\bar\psi\psi$ invariant, so

$$\mathcal L=\bar\psi(i\hbar\gamma^\mu\partial_\mu-m)\psi$$

is a Lorentz scalar.

</details>

<details>
<summary>How does varying the Dirac action produce its equations?</summary>

Treat $\psi$ and $\bar\psi$ as independent variables. Varying $\bar\psi$ gives the Dirac equation, while varying $\psi$ gives the adjoint Dirac equation. The derivative is first order, so specifying $\psi$ on one time slice is sufficient initial data.

</details>

## Field Quantization

<details>
<summary>How is a classical field promoted to a quantum field?</summary>

Canonical quantization starts with a classical field $\phi(\mathbf x,t)$ and its conjugate momentum

$$\pi(\mathbf x,t)=\frac{\partial\mathcal L}{\partial\dot\phi(\mathbf x,t)}.$$

Replace them with operators,

$$\phi\rightarrow\hat\phi,
\qquad
\pi\rightarrow\hat\pi,$$

and impose the equal-time commutator

$$[\hat\phi(\mathbf x,t),\hat\pi(\mathbf y,t)]=i\hbar\delta^3(\mathbf x-\mathbf y).$$

Expanding a free field into momentum modes turns the mode coefficients into creation and annihilation operators:

$$\hat\phi(x)\sim\int d^3p\left(\hat a_{\mathbf p}e^{-ip\cdot x}+\hat a_{\mathbf p}^\dagger e^{ip\cdot x}\right).$$

Each mode behaves like a quantum harmonic oscillator. The operator $\hat a_{\mathbf p}^\dagger$ creates a particle, while $\hat a_{\mathbf p}$ removes one. Fermion fields use anticommutation relations instead of commutation relations. Path-integral quantization provides another route to the quantum theory.

</details>

<details>
<summary>Why is a classical field promoted this way?</summary>

A classical field behaves like an infinite collection of coupled classical coordinates, with roughly one coordinate $\phi(\mathbf x)$ at every point in space. Ordinary canonical quantization replaces a coordinate and its conjugate momentum with operators satisfying

$$[\hat q,\hat p]=i\hbar.$$

The field version applies the same rule at every spatial point:

$$[\hat\phi(\mathbf x),\hat\pi(\mathbf y)]=i\hbar\delta^3(\mathbf x-\mathbf y).$$

The delta function says that $\hat\phi(\mathbf x)$ is conjugate to $\hat\pi(\mathbf x)$, while variables at different points are independent at equal times. This prescription reproduces quantum mechanics for each field mode, gives the correct Heisenberg equations and particle spectrum, and produces bosonic statistics.

Canonical quantization is a construction rule, not something derived from classical physics alone. We test the resulting theory for mathematical consistency and agreement with experiment. Fermionic fields require anticommutators, while constrained and gauge theories need additional care.

</details>

<details>
<summary>Why does QFT replace a fixed-particle wave function with a field?</summary>

Relativistic interactions can create and destroy particles, so a state with a fixed particle number is insufficient. A quantum field contains creation and annihilation operators and can connect sectors with different particle numbers while preserving relativistic locality.

</details>

<details>
<summary>How do we quantize a free field?</summary>

Expand the classical field into momentum modes and promote each mode's amplitudes to creation and annihilation operators. For a scalar field, canonical quantization imposes equal-time commutators such as

$$[\hat\phi(t,\mathbf x),\hat\pi(t,\mathbf y)]=i\hbar\delta^3(\mathbf x-\mathbf y).$$

The resulting ladder operators create and remove particles of definite momentum. Fermion fields use anticommutators, which enforce the exclusion principle.

</details>

<details>
<summary>What is a field mode?</summary>

A **mode** is one independent pattern in which a field can oscillate. A Fourier transform decomposes a free field into plane-wave modes labeled by momentum $\mathbf p$:

$$\phi(x)=\int d^3p\left[a(\mathbf p)e^{-ip\cdot x}+a^*(\mathbf p)e^{ip\cdot x}\right].$$

Each mode has a definite momentum, frequency $\omega_{\mathbf p}=E_{\mathbf p}/\hbar$, and amplitude. The full field is the sum of all its modes, like a vibrating string built from musical harmonics. In a free quantum field, a mode's occupation number counts particles with that momentum. Interactions can couple different modes.

</details>

<details>
<summary>What are the free solutions for a spin-0 field?</summary>

A free spin-0 field obeys the Klein–Gordon equation:

$$\left(\Box+\frac{m^2}{\hbar^2}\right)\phi(x)=0.$$

Its basic solutions are $e^{-ip\cdot x/\hbar}$ and $e^{+ip\cdot x/\hbar}$, with on-shell momentum

$$p^2=m^2,
\qquad
E_{\mathbf p}=\sqrt{\mathbf p^2+m^2}.$$

For a real scalar field, the general classical solution is

$$\phi(x)=\int\frac{d^3p}{(2\pi\hbar)^3}\frac{\hbar}{\sqrt{2E_{\mathbf p}}}
\left[a(\mathbf p)e^{-ip\cdot x/\hbar}+a^*(\mathbf p)e^{+ip\cdot x/\hbar}\right].$$

The two terms are complex conjugates, which keeps $\phi$ real. After quantization, $a\to\hat a$ and $a^*\to\hat a^\dagger$. The negative-frequency term then creates a positive-energy particle rather than describing a physical negative-energy particle.

</details>

<details>
<summary>What are the free solutions for a spin-½ field?</summary>

A free spin-$\tfrac12$ field obeys the Dirac equation:

$$(i\hbar\gamma^\mu\partial_\mu-m)\psi(x)=0.$$

Its plane-wave spinors satisfy

$$(\gamma^\mu p_\mu-m)u_s(p)=0,
\qquad
(\gamma^\mu p_\mu+m)v_s(p)=0,$$

with $p^2=m^2$ and $E_{\mathbf p}=\sqrt{\mathbf p^2+m^2}$. The general quantized free field is

$$\hat\psi(x)=\sum_{s=1}^{2}\int\frac{d^3p}{(2\pi\hbar)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}
\left[\hat a_s(p)u_s(p)e^{-ip\cdot x/\hbar}+\hat b_s^\dagger(p)v_s(p)e^{+ip\cdot x/\hbar}\right].$$

The operator $\hat a_s$ annihilates a particle, while $\hat b_s^\dagger$ creates its antiparticle. The label $s=1,2$ identifies the two spin states.

</details>

<details>
<summary>Why does each free-field mode behave like a harmonic oscillator?</summary>

Fourier expansion separates a free field into independent momentum modes. Each mode has a quadratic Hamiltonian with the same form as a harmonic oscillator. The operator $\hat a_{\mathbf p}^\dagger$ adds one quantum of momentum $\mathbf p$ and energy $E_{\mathbf p}$, while $\hat a_{\mathbf p}$ removes one.

</details>

<details>
<summary>What is the conjugate momentum of a scalar field?</summary>

For a Lagrangian density $\mathcal L$, the conjugate momentum is

$$\pi(x)=\frac{\partial\mathcal L}{\partial\dot\phi(x)}.$$

For the free real scalar field, $\pi=\dot\phi$. It is the field analogue of $p=\partial L/\partial\dot q$.

</details>

<details>
<summary>What commutators do scalar-field ladder operators satisfy?</summary>

Canonical commutation implies

$$[a_{\mathbf p},a_{\mathbf q}^\dagger]=(2\pi)^3\delta^3(\mathbf p-\mathbf q),$$

up to the normalization convention, while two creation operators or two annihilation operators commute. Different momentum modes are independent oscillators.

</details>

<details>
<summary>What is the scalar-field vacuum and a one-particle state?</summary>

The vacuum obeys $a_{\mathbf p}|0\rangle=0$ for every momentum. Acting once with a creation operator gives $|\mathbf p\rangle=a_{\mathbf p}^\dagger|0\rangle$, a one-particle momentum eigenstate. Repeated action builds multiparticle bosonic states.

</details>

<details>
<summary>How does the free-field Hamiltonian count particles?</summary>

After mode expansion, the Hamiltonian is a sum of oscillator energies. Normal ordering removes the formal vacuum constant and leaves

$$H=\int d^3p\,E_{\mathbf p}\,a_{\mathbf p}^\dagger a_{\mathbf p},$$

so each occupied mode contributes its relativistic energy.

</details>

<details>
<summary>How is a Dirac field quantized differently from a scalar field?</summary>

Its particle and antiparticle amplitudes become operators $a_s$ and $b_s$ that obey anticommutation relations. The field contains $a_su_s e^{-ipx}$ and $b_s^\dagger v_s e^{ipx}$ terms. Anticommutation restricts each fermionic mode to occupation zero or one and makes both particle and antiparticle excitation energies positive.

</details>

## Quantum Electrodynamics

<details>
<summary>What is the electromagnetic field strength?</summary>

The electromagnetic field strength is the antisymmetric tensor

$$F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu,$$

built from the gauge potential $A_\mu$. Its components contain the electric and magnetic fields. With the convention $\eta_{\mu\nu}=\operatorname{diag}(+1,-1,-1,-1)$ used here, the raised tensor is

$$F^{\mu\nu}=
\begin{pmatrix}
0 & -E_x & -E_y & -E_z \\
E_x & 0 & -B_z & B_y \\
E_y & B_z & 0 & -B_x \\
E_z & -B_y & B_x & 0
\end{pmatrix}.$$

The time–space components contain $\mathbf E$, while the space–space components contain $\mathbf B$. Antisymmetry, $F^{\mu\nu}=-F^{\nu\mu}$, leaves six independent components: three electric and three magnetic.

</details>

<details>
<summary>How is the field strength computed from the electromagnetic potential?</summary>

Write the four-potential as $A^\mu=(\varphi,\mathbf A)$ in units where $c=1$. Take its antisymmetrized derivative:

$$F^{\mu\nu}=\partial^\mu A^\nu-\partial^\nu A^\mu.$$

The same calculation in three-vector notation gives

$$\mathbf E=-\nabla\varphi-\partial_t\mathbf A,
\qquad
\mathbf B=\nabla\times\mathbf A.$$

Thus,

$$F^{0i}=-E_i,
\qquad
F^{ij}=-\varepsilon^{ijk}B_k.$$

For example, $F^{01}=\partial_tA_x+\partial_x\varphi=-E_x$ and $F^{12}=\partial_yA_x-\partial_xA_y=-B_z$. Computing the other index pairs fills the field-strength matrix.

</details>

<details>
<summary>Is the choice of electromagnetic potential unique?</summary>

No. The gauge transformation

$$A_\mu\rightarrow A_\mu-\partial_\mu\alpha$$

leaves the field strength unchanged because the extra second derivatives cancel:

$$F'_{\mu\nu}=F_{\mu\nu}.$$

Different potentials related this way describe the same electric and magnetic fields. An arbitrary change $A_\mu\to A_\mu+B_\mu$ generally changes the physics; it is locally a pure gauge only when $\partial_\mu B_\nu-\partial_\nu B_\mu=0$.

</details>

<details>
<summary>How is the electromagnetic potential A computed?</summary>

The potential $A_\mu$ is a dynamical field. Given a four-current $J^\nu$, solve Maxwell's equation

$$\partial_\mu F^{\mu\nu}=J^\nu,
\qquad
F^{\mu\nu}=\partial^\mu A^\nu-\partial^\nu A^\mu.$$

Substitution gives

$$\Box A^\nu-\partial^\nu(\partial_\mu A^\mu)=J^\nu.$$

Because the solution is not unique, choose a gauge. In Lorenz gauge, $\partial_\mu A^\mu=0$, the equation becomes

$$\Box A^\nu=J^\nu.$$

The sources, boundary or initial conditions, and gauge choice then determine a representative $A_\mu$. The function $\alpha(x)$ does not generate the physical field; it only changes which gauge-equivalent representative describes the same field.

</details>

<details>
<summary>How do Maxwell's equations follow from the field strength?</summary>

Maxwell's four equations combine into two tensor equations:

$$\partial_\mu F^{\mu\nu}=J^\nu,$$

$$\partial_\lambda F_{\mu\nu}+\partial_\mu F_{\nu\lambda}+\partial_\nu F_{\lambda\mu}=0.$$

In the first equation, choosing $\nu=0$ gives Gauss's electric law,

$$\nabla\cdot\mathbf E=\rho,$$

while $\nu=1,2,3$ gives the Ampère–Maxwell law,

$$\nabla\times\mathbf B=\partial_t\mathbf E+\mathbf j.$$

In the second equation, choosing three spatial indices gives $\nabla\cdot\mathbf B=0$. Choosing one time index gives Faraday's law,

$$\nabla\times\mathbf E=-\partial_t\mathbf B.$$

The second tensor equation follows automatically from $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$ because partial derivatives commute. The first follows from varying the electromagnetic action, including its coupling to the four-current $J^\mu$.

</details>

<details>
<summary>What is a global symmetry?</summary>

A **global symmetry** is a transformation applied in the same way at every point in spacetime. For example, the Dirac field has the global U(1) phase symmetry

$$\psi(x)\rightarrow e^{i\alpha}\psi(x),$$

where $\alpha$ is the same constant everywhere. This changes the field's mathematical phase but leaves the Lagrangian and physical predictions unchanged. By Noether's theorem, every continuous global symmetry has a conserved quantity. For this U(1) symmetry, that quantity is electric charge.

</details>

<details>
<summary>How does local U(1) symmetry produce QED?</summary>

A spacetime-dependent phase transformation of the Dirac field breaks invariance of the free derivative. Introducing the gauge field $A_\mu$ and covariant derivative

$$D_\mu=\partial_\mu+ieA_\mu$$

restores local U(1) symmetry. The QED Lagrangian is

$$\mathcal L_{\rm QED}=\bar\psi(i\gamma^\mu D_\mu-m)\psi-\frac14F_{\mu\nu}F^{\mu\nu}.$$

Its interaction term couples charged fermions to photons.

</details>

<details>
<summary>Why is the U(1) gauge field A the electromagnetic potential?</summary>

Making the charged field's U(1) phase symmetry local requires a connection $A_\mu$ with the transformation

$$A_\mu\rightarrow A_\mu-\partial_\mu\alpha.$$

This is exactly the gauge freedom of the electromagnetic four-potential. Its gauge-invariant curvature

$$F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$$

contains the electric and magnetic fields. Giving $A_\mu$ the kinetic term $-F_{\mu\nu}F^{\mu\nu}/4$ produces Maxwell's equations, while the covariant derivative produces the coupling $-e\bar\psi\gamma^\mu A_\mu\psi$ to electric current.

Thus the new U(1) gauge field has the transformation law, dynamics, and coupling of electromagnetism. Experiment confirms this identification, and its quantum excitations are photons.

</details>

<details>
<summary>How does the photon field transform under a gauge transformation?</summary>

If $\psi(x)\to e^{ie\alpha(x)}\psi(x)$, covariance requires

$$A_\mu\to A_\mu-\partial_\mu\alpha.$$

This cancels the derivative of the local phase in $D_\mu\psi$. The field strength $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$ remains unchanged, so the electric and magnetic fields are gauge invariant.

</details>

<details>
<summary>Which terms make up the QED Lagrangian?</summary>

It contains the Dirac kinetic and mass terms, the photon kinetic term $-F_{\mu\nu}F^{\mu\nu}/4$, and the interaction $-e\bar\psi\gamma^\mu A_\mu\psi$. The interaction describes one photon meeting an incoming and outgoing charged-fermion line.

</details>

<details>
<summary>How is the photon field quantized?</summary>

Expand $A_\mu$ into momentum and polarization modes and promote their coefficients to ladder operators. Gauge freedom removes unphysical redundancies, leaving two transverse polarizations for an on-shell photon. Creation operators add photon quanta to the Fock state.

</details>

<details>
<summary>Why does a photon have only two physical polarizations?</summary>

A plane wave $A^\mu=\varepsilon^\mu e^{-ik\cdot x}$ starts with four polarization components. Maxwell's equation imposes $k\cdot\varepsilon=0$, removing one. Gauge freedom $\varepsilon^\mu\to\varepsilon^\mu+\alpha k^\mu$ removes another, leaving two directions transverse to the momentum.

</details>

<details>
<summary>What is a pure-gauge photon mode?</summary>

A polarization proportional to its momentum, $\varepsilon^\mu=Ck^\mu$, gives

$$F^{\mu\nu}\propto k^\mu k^\nu-k^\nu k^\mu=0.$$

The potential oscillates, but it produces no electric or magnetic field, so it is not a physical photon.

</details>

<details>
<summary>Why does direct canonical quantization of A fail?</summary>

The Maxwell Lagrangian contains no time derivative of $A_0$. Its conjugate momentum is therefore

$$\pi^0=-F^{00}=0.$$

This prevents imposing an ordinary canonical commutator for $A_0$. The component $A_0$ instead enforces Gauss's-law constraint.

</details>

<details>
<summary>What is a gauge-fixing term?</summary>

A gauge-fixing term is an extra term added to the QED Lagrangian to control
the redundant descriptions related by gauge transformations. It is not added
to the gauge potential $A_\mu$. A common choice is

$$\mathcal L_{\rm QED}\longrightarrow
\mathcal L_{\rm QED}+\mathcal L_{\rm gf},\qquad
\mathcal L_{\rm gf}=-\frac{1}{2\xi}(\partial_\mu A^\mu)^2.$$

It changes the equations for the redundant components used during
quantization without changing gauge-invariant physical predictions.

</details>

<details>
<summary>Why add a gauge-fixing term?</summary>

The Feynman-gauge term

$$\mathcal L_{\rm gf}=-\frac12(\partial_\mu A^\mu)^2$$

supplies the missing time derivative of $A_0$ and makes all four components obey $\Box A_\mu=0$. We can then quantize them uniformly, but we must remove the extra unphysical states afterward.

</details>

<details>
<summary>Which photon modes are unphysical after gauge fixing?</summary>

Quantizing all four components introduces two transverse modes, one longitudinal mode, and one timelike mode. The timelike mode has negative norm because the Minkowski metric gives its oscillator the opposite sign. Longitudinal and timelike excitations cannot represent physical photons.

</details>

<details>
<summary>What is the photon propagator in Feynman gauge?</summary>

After adding the Feynman-gauge term, the four components decouple. The momentum-space propagator is

$$D_{\mu\nu}(k)=\frac{-ig_{\mu\nu}}{k^2+i\epsilon}.$$

Unphysical components may appear on internal lines, but the physical-state conditions and gauge symmetry remove them from observable predictions.

</details>


## From Lagrangian to Experiment

<details>
<summary>How does a Lagrangian lead to a measurable cross section?</summary>

The interaction Lagrangian determines the transition amplitude $\mathcal M$ through the S-matrix. To predict a scattering rate, calculate $|\mathcal M|^2$, sum and average over unobserved quantum states, integrate over final-state phase space, and divide by the incoming flux. The resulting cross section can be compared directly with event counts in an experiment.

</details>

<details>
<summary>What ingredients convert an amplitude into a cross section?</summary>

Square the amplitude, average over unobserved initial states, sum over final states, impose four-momentum conservation, and integrate over Lorentz-invariant phase space. Dividing by the incoming flux gives $d\sigma$. This separates the dynamics in $\mathcal M$ from the kinematics of the initial and final particles.

</details>

<details>
<summary>What does a scattering experiment specify and measure?</summary>

It prepares incoming beams with known momenta and quantum numbers, then counts specified outgoing particles in detector bins. Luminosity measures the opportunity for collisions, and $N=\mathcal L_{\rm int}\sigma$ relates an event count to the cross section, before efficiencies and backgrounds are included.

</details>

<details>
<summary>What is Lorentz-invariant phase space?</summary>

For each final particle it supplies $d^3p/[(2\pi)^3 2E]$, and a delta function enforces total four-momentum conservation. Integrating this measure sums over all final configurations accepted by the measurement.

</details>

<details>
<summary>Why is calculating the amplitude the central dynamical step?</summary>

Flux and phase space follow from kinematics once the external particles are specified. The theory-dependent information lies in $\mathcal M$, which encodes couplings, exchanged particles, spin, and interference. Perturbation theory and Feynman rules provide a systematic way to compute it.

</details>

## Perturbation Theory

<details>
<summary>What are we trying to calculate in perturbation theory?</summary>

We want the transition amplitude between chosen initial and final states,
$\langle f|S|i\rangle$. Its interacting part defines the invariant amplitude
$\mathcal M$:

$$\langle f|iT|i\rangle
=(2\pi)^4\delta^4(P_f-P_i)\,i\mathcal M.$$

Perturbation theory approximates $\mathcal M$ by expanding the S-matrix in
powers of the interaction strength. We then use $|\mathcal M|^2$ to calculate
measurable cross sections and decay rates.

</details>

<details>
<summary>How do we split the full Lagrangian?</summary>

Write

$$\mathcal L=\mathcal L_0+\mathcal L_{\rm int}.$$

The quadratic terms form the exactly solvable free Lagrangian $\mathcal L_0$.
The remaining terms couple fields and form $\mathcal L_{\rm int}$. We quantize
$\mathcal L_0$ exactly and expand the S-matrix in powers of
$\mathcal L_{\rm int}$ and its coupling constants. We split the Lagrangian;
we do not expand the Lagrangian itself.

</details>

<details>
<summary>What is the interaction Lagrangian for a cubic scalar theory?</summary>

For a real scalar field $\phi$,

$$\mathcal L_{\rm int}=-\frac{g}{3!}\phi^3.$$

The coupling $g$ sets the interaction strength. The factor $3!$ compensates
for the equivalent ways of attaching three identical scalar lines to a
vertex. Each insertion of $\mathcal L_{\rm int}$ in the Dyson series produces
one three-legged vertex with factor $-ig$.

</details>

<details>
<summary>Is the interaction Lagrangian different for QED?</summary>

Yes. Cubic scalar theory has

$$\mathcal L_{\rm int}=-\frac{g}{3!}\phi^3,$$

which couples three identical scalar fields. QED instead has

$$\mathcal L_{\rm int}=-q\bar\psi\gamma^\mu\psi A_\mu,$$

which joins two fermion lines and one photon line and gives the vertex factor
$-iq\gamma^\mu$. The perturbative method is the same, but the fields,
propagators, spinor structure, and fermionic signs differ.

</details>

<details>
<summary>What is the S-matrix?</summary>

The S-matrix maps an incoming free-particle state in the distant past to an
outgoing free-particle state in the distant future. After splitting

$$\mathcal L=\mathcal L_0+\mathcal L_{\rm int},$$

$\mathcal L_0$ defines the free fields and asymptotic particle states, while
$\mathcal L_{\rm int}$ generates transitions between them. In the interaction
picture,

$$S=\mathcal T\exp\left(i\int d^4x\,\mathcal L_{\rm int}(x)\right),$$

where $\mathcal T$ orders later interactions to the left. Expanding the
exponential gives

$$\begin{aligned}
S={}&1+i\int d^4x\,\mathcal L_{\rm int}(x)\\
&+\frac{i^2}{2!}\int d^4x\,d^4y\,
\mathcal T[\mathcal L_{\rm int}(x)\mathcal L_{\rm int}(y)]+\cdots.
\end{aligned}$$

Each insertion of $\mathcal L_{\rm int}$ adds one interaction vertex. Writing
$S=1+iT$ separates free passage from scattering, and matrix elements of $T$
define the invariant amplitude $\mathcal M$.

</details>

<details>
<summary>How do we calculate the transition operator T?</summary>

Start from the interaction Lagrangian and expand the S-matrix:

$$S=\mathcal T\exp\left(i\int d^4x\,\mathcal L_{\rm int}(x)\right)=1+iT.$$

The Dyson expansion therefore determines $iT=S-1$. In practice, we usually
calculate only the matrix element needed for a chosen process:

$$\langle f|iT|i\rangle=(2\pi)^4\delta^4(P_f-P_i)\,i\mathcal M.$$

Choose the initial and final states, expand to the required order in the
coupling, and evaluate the result with Wick's theorem or the equivalent
Feynman rules. Here $T$ is the transition operator, while $\mathcal T$ is the
time-ordering operator.

</details>

<details>
<summary>How does perturbation theory generate Feynman rules?</summary>

Expand the interaction-picture S-matrix,

$$S=T\exp\left[-\frac{i}{\hbar}\int d^4x\,\mathcal H_I(x)\right],$$

in powers of the coupling. Wick's theorem rewrites time-ordered products as normal-ordered fields plus contractions. Contractions become propagators, interaction terms become vertices, and the remaining external fields become external lines. This dictionary turns each term in the series into a Feynman diagram and amplitude.

</details>

<details>
<summary>What do propagators and vertices represent in the perturbative expansion?</summary>

A contraction of two free fields gives a propagator, which connects two spacetime points or carries momentum internally. Each factor from the interaction Lagrangian gives a vertex and coupling constant. The expansion order counts vertices, so higher powers of a small coupling usually give smaller corrections.

</details>

<details>
<summary>How is the S-matrix organized by powers of the coupling?</summary>

Expanding the time-ordered exponential gives terms with zero, one, two, and more insertions of the interaction Hamiltonian. A process begins at the lowest order capable of connecting its external states; higher orders add vertices and loop corrections.

</details>

<details>
<summary>What is Wick's theorem?</summary>

Wick's theorem rewrites a time-ordered product of free fields as its
normal-ordered product plus every possible contraction. For two fields,

$$\mathcal T[\phi(x)\phi(y)]
=:\!\phi(x)\phi(y)\!:
+\langle0|\mathcal T[\phi(x)\phi(y)]|0\rangle.$$

Each contraction is a propagator. In a vacuum expectation value, terms with
unpaired field operators vanish, so the surviving contractions map directly
to Feynman diagrams.

</details>

<details>
<summary>What is a propagator mathematically?</summary>

A propagator is a time-ordered two-point function. In momentum space, the
scalar propagator $i/(p^2-m^2+i\epsilon)$ is $i$ times the inverse of the free
quadratic operator. Its pole structure encodes free-particle propagation, and
the $i\epsilon$ specifies the time-ordering prescription.

</details>

<details>
<summary>How do symmetry factors arise?</summary>

Different contractions can produce the same diagram. Factorials from the exponential and interaction Lagrangian cancel many duplicated contractions; any remaining multiplicity becomes the diagram's symmetry factor. It prevents identical configurations from being overcounted.

</details>

<details>
<summary>How does the scalar-field dictionary extend to QED?</summary>

The logic is unchanged, but contractions use Dirac and photon propagators, external fermions carry spinors, and each interaction insertion supplies $-ie\gamma^\mu$. Anticommuting fermion fields also introduce signs when their order changes.

</details>

## Feynman Rules for QED

<details>
<summary>How do QED Feynman diagrams encode scattering amplitudes?</summary>

Attach a spinor or polarization factor to each external line, a propagator to each internal line, and a factor $-ie\gamma^\mu$ to each electron–photon vertex. Conserve four-momentum at every vertex and integrate over independent loop momenta. Tree diagrams give the leading approximation; loops supply quantum corrections and can contain divergences that require renormalization.

</details>

<details>
<summary>Why can one process require several Feynman diagrams?</summary>

Every distinct allowed contraction or internal routing contributes an amplitude. Add these amplitudes before taking the absolute square, so their cross terms produce quantum interference. Compton scattering, for example, has two tree-level electron-exchange diagrams with different vertex orderings.

</details>

<details>
<summary>What are the external and internal building blocks of a QED diagram?</summary>

External fermions contribute $u,\bar u,v,$ or $\bar v$ spinors, external photons contribute polarization vectors, internal lines contribute propagators, and each vertex contributes $-ie\gamma^\mu$ with four-momentum conserved.

</details>

<details>
<summary>How is the Compton-scattering amplitude assembled?</summary>

Electron–photon scattering has two tree diagrams because the photons can attach in two orders. Add both amplitudes before squaring; the internal electron momentum and propagator differ between the two terms.

</details>

<details>
<summary>How is a QED amplitude converted into an unpolarized result?</summary>

Square the summed amplitude, average over initial spins and polarizations, and sum over final ones. Completeness relations turn spin sums into gamma-matrix traces and polarization sums into tensor contractions.

</details>

<details>
<summary>What distinguishes tree and loop diagrams?</summary>

Tree diagrams contain no closed momentum cycles and usually give the leading result. Each loop introduces an unconstrained four-momentum integral, an additional coupling order, and a genuine quantum correction.

</details>

<details>
<summary>Why do loop diagrams become infinite?</summary>

Their integrals include arbitrarily large virtual momenta and can diverge. Regularization exposes the divergence, and renormalization absorbs it into measured parameters so finite predictions remain.

</details>

## Weak Interaction

<details>
<summary>How does the weak interaction arise from SU(2) gauge symmetry?</summary>

The weak interaction acts on left-handed fermion doublets and violates parity. Making their SU(2) symmetry local introduces three gauge fields $W_\mu^a$ with self-interactions. The combinations $W^\pm$ mediate charged-current processes such as beta decay, while $W^3$ contributes to the neutral interaction. At low energy, massive-W exchange reduces to Fermi's effective four-fermion interaction.

</details>

<details>
<summary>Why does the weak interaction distinguish left from right?</summary>

Experiments show maximal parity violation: charged weak currents couple to left-handed fermions and right-handed antifermions. The projector $P_L=(1-\gamma^5)/2$ selects this chiral component. Left-handed leptons form SU(2) doublets, while their right-handed charged partners are SU(2) singlets.

</details>

<details>
<summary>How does beta decay reveal the weak interaction?</summary>

At quark level, a down quark becomes an up quark while emitting a virtual $W^-$, which produces an electron and electron antineutrino. The neutrino carries missing energy, momentum, and angular momentum.

</details>

<details>
<summary>How are weak charged currents constructed?</summary>

Left-handed partners form doublets such as $(\nu_e,e)_L$. Off-diagonal SU(2) generators convert one member into the other, producing currents coupled to $W^+$ and $W^-$.

</details>

<details>
<summary>Why does local SU(2) introduce three weak gauge fields?</summary>

SU(2) has three generators, so its covariant derivative needs three fields $W_\mu^a$. Their charged combinations are $W^\pm=(W^1\mp iW^2)/\sqrt2$, while $W^3$ is neutral.

</details>

<details>
<summary>How is the weak coupling related to Fermi's constant?</summary>

At momenta far below $m_W$, the W propagator reduces to a contact interaction. Matching coefficients gives $G_F/\sqrt2=g^2/(8m_W^2)$ at tree level.

</details>

## Yang–Mills Fields

<details>
<summary>Why do non-Abelian gauge fields interact with themselves?</summary>

For a non-Abelian group, the generators do not commute. The field strength therefore contains a term quadratic in the gauge fields:

$$F^a_{\mu\nu}=\partial_\mu A^a_\nu-\partial_\nu A^a_\mu+g f^{abc}A^b_\mu A^c_\nu.$$

Substituting this into $-F^a_{\mu\nu}F^{a\mu\nu}/4$ produces three- and four-gauge-boson vertices. Abelian U(1) has vanishing structure constants, so photons have no corresponding tree-level self-coupling.

</details>

<details>
<summary>How does the Yang–Mills covariant derivative produce the field strength?</summary>

With $D_\mu=\partial_\mu-igA_\mu^aT^a$, the commutator defines

$$[D_\mu,D_\nu]=-igF_{\mu\nu}^aT^a.$$

The commutator of generators supplies the nonlinear $gf^{abc}A_\mu^bA_\nu^c$ term. This construction makes the field strength transform covariantly under local gauge transformations.

</details>

## Electroweak Unification

<details>
<summary>How do SU(2)L and U(1)Y combine electromagnetism with the weak interaction?</summary>

The electroweak theory uses the gauge group $SU(2)_L\times U(1)_Y$ and charge relation

$$Q=T_3+\frac{Y}{2}.$$

The neutral fields $W^3_\mu$ and $B_\mu$ mix to form the photon $A_\mu$ and the $Z_\mu$ boson. This structure gives the same electromagnetic charge to the appropriate left- and right-handed fields while allowing only left-handed fermions to carry weak isospin.

</details>

<details>
<summary>How are the photon and Z boson formed?</summary>

The neutral gauge fields mix through the weak angle $\theta_W$:

$$A_\mu=B_\mu\cos\theta_W+W_\mu^3\sin\theta_W,
\qquad Z_\mu=-B_\mu\sin\theta_W+W_\mu^3\cos\theta_W.$$

The photon combination couples to electric charge and remains massless; the orthogonal Z combination mediates the neutral weak current.

</details>

<details>
<summary>Why can the neutral weak field not be the photon?</summary>

$W^3$ couples to weak isospin and only to left-handed doublets, whereas the photon couples to electric charge for both chiralities. A second neutral U(1) hypercharge field is required.

</details>

<details>
<summary>What is hypercharge?</summary>

Hypercharge $Y$ is the U(1)Y charge chosen so $Q=T_3+Y/2$. Different left- and right-handed multiplets carry different hypercharges, which reproduces their observed electric charges after mixing.

</details>

<details>
<summary>How does the Z boson couple to matter?</summary>

The Z couples to a neutral current involving both weak isospin and electric charge. Its left- and right-handed couplings differ because only the left-handed fields carry $T_3$.

</details>

<details>
<summary>Why does the electroweak theory need the Higgs field?</summary>

Explicit masses for W and Z would violate gauge consistency. The Higgs covariant-derivative term generates their masses from a gauge-invariant Lagrangian after the vacuum acquires a nonzero value.

</details>

## Higgs Mechanism

<details>
<summary>How does the Higgs field give particles mass without breaking gauge consistency?</summary>

The Higgs potential has minima at a nonzero field magnitude, so the vacuum selects a direction in field space. Expanding the Higgs doublet around this vacuum converts three Goldstone modes into longitudinal polarizations of $W^\pm$ and $Z$, making them massive while leaving the photon massless. The remaining fluctuation is the Higgs boson. Yukawa couplings to the Higgs vacuum generate fermion masses.

</details>

<details>
<summary>What does spontaneous symmetry breaking mean?</summary>

The equations can respect a symmetry even when the lowest-energy state does not. For the Higgs potential, all vacuum orientations have the same energy, but choosing one hides part of the gauge symmetry in the vacuum. The gauge symmetry remains a redundancy of the description; reorganizing the fields around the chosen vacuum reveals massive gauge bosons.

</details>

<details>
<summary>How does the Abelian Higgs mechanism make a gauge boson massive?</summary>

For a complex scalar with nonzero vacuum magnitude, write the phase fluctuation into the gauge field by a gauge choice. The scalar kinetic term then contains a gauge-boson mass term, while the radial fluctuation remains as a physical Higgs particle.

</details>

<details>
<summary>Which electroweak gauge bosons gain mass?</summary>

The Higgs doublet supplies three Goldstone modes to $W^+$, $W^-$, and $Z$. Their masses are $m_W=gv/2$ and $m_Z=v\sqrt{g^2+g'^2}/2$. The photon corresponds to the unbroken charge generator and stays massless.

</details>

<details>
<summary>How do Yukawa interactions generate fermion masses?</summary>

A gauge-invariant Yukawa term couples left-handed doublets, right-handed singlets, and the Higgs. Replacing the Higgs by its vacuum value gives $m_f=y_fv/\sqrt2$, while the remaining Higgs fluctuation couples in proportion to the fermion mass.

</details>

## Quantum Chromodynamics

<details>
<summary>How does QCD describe quarks and gluons?</summary>

QCD is an $SU(3)_C$ gauge theory. Quarks carry three color states, and local color symmetry introduces eight gluons. Because SU(3) is non-Abelian, gluons carry color charge and interact with one another. The coupling weakens at high energy, producing asymptotic freedom, but grows at long distance, so isolated colored particles are confined inside color-neutral hadrons.

</details>

<details>
<summary>Why are there eight gluons rather than three?</summary>

Gluons correspond to the generators of SU(3). A traceless Hermitian $3\times3$ generator has eight independent components, so the theory has eight gauge fields. These gluons carry combinations of color and anticolor, but physical particles must combine into color singlets.

</details>

<details>
<summary>Why was color introduced?</summary>

Color provides three otherwise identical internal quark states. It makes baryon wave functions compatible with Fermi statistics and explains observed multiplicities while requiring physical hadrons to be color neutral.

</details>

<details>
<summary>How does local SU(3) symmetry determine the QCD Lagrangian?</summary>

The covariant derivative $D_\mu=\partial_\mu-ig_sG_\mu^aT^a$ couples quarks to gluons. The non-Abelian field strength supplies gluon kinetic terms plus three- and four-gluon self-interactions.

</details>

<details>
<summary>How do asymptotic freedom and confinement describe different distance scales?</summary>

Quantum corrections make the strong coupling decrease at high momentum transfer, so quarks behave nearly free at short distances. At long distances the coupling grows, and separating color charges produces hadrons rather than isolated quarks.

</details>

## Standard Model

<details>
<summary>What fields and interactions make up the Standard Model?</summary>

The Standard Model is based on

$$SU(3)_C\times SU(2)_L\times U(1)_Y.$$

Its matter fields are quarks and leptons in three generations; its gauge fields produce the strong, weak, and electromagnetic interactions. The Higgs field breaks electroweak symmetry and supplies gauge-boson and fermion masses. Yukawa matrices also produce flavor mixing, while gravity and several observed phenomena remain outside the model.

</details>

<details>
<summary>What does the Standard Model not explain?</summary>

It does not include quantum gravity and does not identify the dark matter or dark energy. In its minimal form it also leaves neutrino masses unexplained. Its many measured parameters, fermion generations, mass hierarchy, matter–antimatter asymmetry, and strong-CP puzzle point to questions beyond the theory.

</details>

<details>
<summary>How do gauge fields interact with quarks and leptons?</summary>

Covariant derivatives encode every gauge coupling. Quarks carry color, weak isospin according to chirality, and hypercharge; leptons carry no color. Their representation assignments determine all photon, W, Z, and gluon vertices.

</details>

<details>
<summary>How does the Higgs sector complete the gauge theory?</summary>

Its vacuum breaks the electroweak symmetry to electromagnetic U(1), gives masses to W and Z, and leaves the photon massless. The physical radial excitation is the Higgs boson.

</details>

<details>
<summary>What are Yukawa matrices and flavor mixing?</summary>

Yukawa matrices couple fermion generations to the Higgs. Diagonalizing the resulting mass matrices misaligns the weak and mass bases, producing the CKM matrix for quarks and the analogous PMNS mixing for massive neutrinos.

</details>

<details>
<summary>Why are there three fermion generations?</summary>

The Standard Model contains three copies of the same gauge representations with different masses. It describes their couplings and mixing but does not explain why there are three generations or why their masses span such different scales.

</details>
