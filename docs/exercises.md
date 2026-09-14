# Exercises

## Classical Mechanics

<details>
<summary>
What's the Newton Formulation of Classical Mechanics?
</summary>

Newton's formulation describes motion through forces. For a particle of constant mass, Newton's second law gives

$$\mathbf F_{\mathrm{net}}=m\mathbf a=m\frac{d^2\mathbf x}{dt^2}.$$

Once we know the force law and the particle's initial position and velocity, we solve this second-order differential equation to find its trajectory $\mathbf x(t)$. Integrating the acceleration once gives the velocity, and integrating it again gives the position.

</details>

<details>
<summary>
What's the Principle of Least Action?
</summary>

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
<summary>
Derive the Euler–Lagrange equations from the Principle of Least Action

$$\frac{d}{dt}\left(\frac{\partial L}{\partial\dot q_i}\right)-\frac{\partial L}{\partial q_i}=0,$$
</summary>

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
<summary>
What are generalized coordinates, canonical momenta, and the Hamiltonian?
</summary>

**Generalized coordinates** $q_i$ are independent variables that specify a system's configuration. They need not be Cartesian positions. For example, a pendulum can be described by one generalized coordinate, its angle $q=\theta$, rather than by the bob's Cartesian coordinates subject to a length constraint. Their time derivatives $\dot q_i$ are the generalized velocities.

The **canonical momentum** conjugate to $q_i$ is defined from the Lagrangian by

$$p_i=\frac{\partial L}{\partial\dot q_i}.$$

Canonical momentum does not always equal mechanical momentum $m\dot q_i$. The two agree for a Cartesian coordinate with the Lagrangian $L=\tfrac12m\dot q_i^2-V(q)$, but constraints or velocity-dependent interactions can change the relation.
</details>

<details>
<summary>
What's the Hamiltonian?
</summary>
The **Hamiltonian** replaces the generalized velocities $\dot q_i$ with the canonical momenta $p_i$. It is the Legendre transform of the Lagrangian:

$$H(q_i,p_i,t)=\sum_i p_i\dot q_i-L(q_i,\dot q_i,t),$$

where the velocities on the right must be expressed in terms of $q_i$, $p_i$, and $t$.
</details>


<details>
<summary>
What are the time evolution equations of the Hamiltonian?
</summary>

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
<summary>
What is the state of a quantum system?
When do two state vectors represent the same physical state?
How is a quantum state represented in the position basis?
</summary>

A quantum state contains all the information that quantum mechanics can use to predict the outcomes of measurements. We represent a pure state by a normalized vector $|\psi\rangle$ in a complex Hilbert space:

$$\langle\psi|\psi\rangle=1.$$

Two vectors that differ only by an overall phase, $|\psi\rangle$ and $e^{i\alpha}|\psi\rangle$, represent the same physical state. In the position basis, the state is represented by the wave function

$$\psi(x,t)=\langle x|\psi(t)\rangle.$$
</details>

<details>
<summary>
What's an observable?
</summary>

An observable is a measurable physical quantity, such as position, momentum, energy, or spin. Quantum mechanics represents observables by **self-adjoint linear operators** (Hermitian matrices in finite-dimensional Hilbert spaces). Self-adjoint operators have real eigenvalues, so their possible measured values are real.

</details>

<details>
<summary>
What's an eigenvalue / eigenstate?
</summary>

An **eigenstate** of an observable $\hat A$ is a state whose direction does not change when the operator acts on it:

$$\hat A|a_n\rangle=a_n|a_n\rangle.$$

Here, $|a_n\rangle$ is the eigenstate and $a_n$ is its eigenvalue. If the system is in $|a_n\rangle$, measuring $A$ gives $a_n$ with certainty. For example, an energy eigenstate satisfies

$$\hat H|E_n\rangle=E_n|E_n\rangle.$$

</details>

<details>
<summary>
How can a quantum state be expanded in an observable’s eigenbasis?
</summary>

If an observable has orthonormal eigenstates $|a_n\rangle$, we can expand the state as

$$|\psi\rangle=\sum_n c_n|a_n\rangle.$$

</details>

<details>
<summary>
What is the Born rule?
</summary>
The Born rule assigns probability

$$P(a_n)=|c_n|^2=|\langle a_n|\psi\rangle|^2$$

to obtaining the value $a_n$ in a measurement.

</details>

<details>
<summary>
How does a quantum state evolve between measurements?
</summary>

Between measurements, the state evolves according to the Schrödinger equation,

$$i\hbar\frac{d}{dt}|\psi(t)\rangle=\hat H|\psi(t)\rangle.$$
</details>

<details>
<summary>
What are the position and momentum operators?
</summary>

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
<summary>
</summary>
</details>

<details>
<summary>
What force defines a harmonic oscillator?
</summary>

A **harmonic oscillator** is a system whose restoring force is proportional to its displacement from equilibrium and points back toward equilibrium:

$$F=-kx.$$

</details>

<details>
<summary>
What is the classical equation of motion and angular frequency of a harmonic oscillator?
</summary>

Its classical equation of motion is

$$m\ddot x+kx=0,$$

so it oscillates sinusoidally with angular frequency

$$\omega=\sqrt{\frac{k}{m}}.$$

</details>

<details>
<summary>
What is the Hamiltonian of a harmonic oscillator?
</summary>
The Hamiltonian is

$$H=\frac{p^2}{2m}+\frac12m\omega^2x^2.$$

</details>

<details>
<summary>
What are the energy levels of the quantum harmonic oscillator?
</summary>
In quantum mechanics, the oscillator has discrete energy levels:

$$E_n=\hbar\omega\left(n+\frac12\right),
\qquad n=0,1,2,\ldots.$$

</details>

<details>
<summary>
What is zero-point energy, and why does the harmonic oscillator appear throughout physics?
</summary>

Its lowest state has the nonzero zero-point energy $E_0=\tfrac12\hbar\omega$. The harmonic oscillator appears throughout physics because a smooth potential near a stable equilibrium is approximately quadratic.

</details>

<details>
<summary>
What potential defines the quantum harmonic oscillator?
</summary>

The **quantum harmonic oscillator** is the quantum description of a particle moving in the quadratic potential

$$V(x)=\frac12m\omega^2x^2.$$

</details>

<details>
<summary>
What is the Hamiltonian operator of the quantum harmonic oscillator?
</summary>
Its Hamiltonian is

$$\hat H=\frac{\hat p^2}{2m}+\frac12m\omega^2\hat x^2.$$

</details>

<details>
<summary>
What energy eigenvalue equation and spectrum does the quantum harmonic oscillator have?
</summary>
Solving the time-independent Schrödinger equation,

$$\hat H|n\rangle=E_n|n\rangle,$$

gives discrete, equally spaced energy levels:

$$E_n=\hbar\omega\left(n+\frac12\right),
\qquad n=0,1,2,\ldots.$$

</details>

<details>
<summary>
What are the quantum harmonic oscillator's ground-state energy and ladder operators, and why is the model important?
</summary>

The ground state has energy $E_0=\tfrac12\hbar\omega$, so the oscillator never has zero energy. Ladder operators move between adjacent energy states:

$$\hat a^\dagger|n\rangle=\sqrt{n+1}\,|n+1\rangle,
\qquad
\hat a|n\rangle=\sqrt n\,|n-1\rangle.$$

The model matters because many systems behave approximately like harmonic oscillators near stable equilibria. Each mode of a free quantum field also behaves like a quantum harmonic oscillator.

</details>

<details>
<summary>
If ω can have any value, how is the quantum harmonic oscillator's energy quantized?
</summary>

The frequency $\omega$ can be any positive value because it is a parameter that defines the particular oscillator:

$$\omega=\sqrt{\frac{k}{m}}.$$

Once $m$, $k$, and therefore $\omega$ are fixed, that oscillator can have only the discrete energies

$$E_n=\hbar\omega\left(n+\frac12\right),
\qquad n=0,1,2,\ldots.$$

Across different oscillators, the energy scale can vary continuously with $\omega$. For one fixed oscillator, however, the allowed energies remain discrete and adjacent levels differ by $\hbar\omega$. Quantization restricts the level number $n$, not the externally specified parameter $\omega$.

</details>

## Special Relativity

<details>
<summary>
What are the two postulates of special relativity?
</summary>

The **principle of relativity** states that the laws of physics have the same form in every inertial frame. The **invariance of the speed of light** states that every inertial observer measures the same vacuum light speed $c$, regardless of the source's motion.

</details>

<details>
<summary>
Why do Lorentz transformations replace Galilean transformations?
</summary>

Galilean transformations preserve absolute time and use ordinary velocity addition, which would make different observers measure different light speeds. Lorentz transformations preserve $c$ by mixing space and time:

$$t'=\gamma\left(t-\frac{vx}{c^2}\right),
\qquad
x'=\gamma(x-vt),
\qquad
\gamma=\frac{1}{\sqrt{1-v^2/c^2}}.$$

</details>

<details>
<summary>
What is the invariant spacetime interval?
</summary>

Observers can disagree about simultaneity, elapsed time, and spatial distance, but they agree on the spacetime interval

$$s^2=c^2\Delta t^2-\Delta x^2-\Delta y^2-\Delta z^2.$$

The sign of $s^2$ classifies event separations as timelike, lightlike, or spacelike and determines whether one event can causally influence another.

</details>

<details>
<summary>
What are four-vectors and Lorentz scalars?
</summary>

Four-vectors combine time and space components into objects that transform consistently between inertial frames. With the Minkowski metric $\eta_{\mu\nu}=\operatorname{diag}(+1,-1,-1,-1)$, contracting an upper and lower index produces a **Lorentz scalar**, whose value every inertial observer agrees on.

</details>

<details>
<summary>
What is the relativistic energy–momentum relation?
</summary>

The four-momentum is

$$p^\mu=\left(\frac{E}{c},\mathbf p\right)$$

and has the invariant norm $p^\mu p_\mu=m^2c^2$. Therefore,

$$E^2=(mc^2)^2+(pc)^2.$$

This relation reduces to $E=mc^2$ for a massive particle at rest and to $E=pc$ for a massless particle.

</details>

<details>
<summary>
Why are Maxwell's equations compatible with special relativity?
</summary>

Relativistic equations must retain their form under Lorentz transformations. Maxwell's equations meet this requirement when written using the four-current $J^\mu$ and electromagnetic field tensor $F^{\mu\nu}$:

$$\partial_\mu F^{\mu\nu}=J^\nu.$$

Electric and magnetic fields form parts of one relativistic field and can mix under a boost.

</details>

<details>
<summary>
Why is the Schrödinger equation not Lorentz covariant?
</summary>

The Schrödinger equation treats time and space derivatives differently, so its form changes when a Lorentz boost mixes space and time. It also uses the non-relativistic relation $E=\mathbf p^2/(2m)$. Starting instead from the exact relativistic energy–momentum relation leads toward the Klein–Gordon and Dirac equations.

</details>
