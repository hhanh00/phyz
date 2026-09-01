# First Quantization

## 1. From Classical to Quantum State Space
First quantization is the procedure of promoting a classical system to a quantum one while keeping its basic structure intact. Phase space $(q, p)$ is replaced by a Hilbert space of state vectors, dynamical quantities become linear operators acting on that space, and the Poisson bracket is replaced by the commutator via $\{\cdot,\cdot\} \to \frac{1}{i\hbar}[\cdot,\cdot]$. The immediate consequence is that a system's state is no longer a single point specifying definite values for every quantity at once — it is a vector that, in general, does not have a definite value for every observable simultaneously. Everything that follows is really an unpacking of what that shift entails.

## 2. The Schrödinger Equation
Time evolution of a quantum state is governed by the Schrödinger equation, $i\hbar\, \partial \Psi/\partial t = \hat H \Psi$, the direct quantum analogue of Hamilton's equations: given the state now and the Hamiltonian operator, the equation determines the state at every later time, deterministically and unitarily. For a Hamiltonian with no explicit time dependence this separates into a time-independent form, $\hat H \Psi = E\Psi$, an eigenvalue equation whose solutions are the stationary states and allowed energies of the system.

$$i\hbar \frac{\partial \Psi(x,t)}{\partial t} = \left[-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V(x)\right]\Psi(x,t)$$

## 3. Wave Amplitude
The solution $\Psi(x,t)$ to the Schrödinger equation is a complex-valued function called the wave amplitude, or wavefunction. On its own it is not directly observable — what is physical is $|\Psi(x,t)|^2$, the probability density for finding the particle at position $x$ at time $t$. Because it is a probability density, $\Psi$ must be normalized so that $\int |\Psi|^2\, dx = 1$ over all space, and its phase, though unobservable in isolation, is exactly what produces interference when amplitudes are added.

## 4. Bohr Interpretation
The interpretation most often taught alongside this formalism — usually credited to Bohr and collaborators and known as the Copenhagen interpretation — treats $|\Psi|^2$ as a genuine probability rather than a description of hidden, already-determined values. Before a measurement, a system does not possess a definite value for an observable unless it happens to be in an eigenstate of that observable; measurement is taken to force the state to "collapse" onto one eigenstate, with outcome probabilities set by the Born rule. Bohr paired this with the principle of complementarity: quantities such as position and momentum, or wave and particle behavior, are both valid descriptions but can never be jointly and precisely observed in a single experiment.

## 5. Operators
Every classical dynamical variable is promoted to a linear operator acting on the Hilbert space of states. Position becomes the operator $\hat x$ (multiplication by $x$ in the position representation[^pos-rep]), and momentum becomes $\hat p = -i\hbar\, \partial/\partial x$. Operators act on state vectors to produce new state vectors, and the order in which two operators are applied can matter — a departure from classical variables, which are just numbers and always commute.

## 6. Observables
Not every operator corresponds to something measurable. Physical observables — energy, position, momentum, spin — are represented by Hermitian operators[^linalg] specifically, because Hermiticity guarantees real eigenvalues, and a measurement can only ever return a real number. The Hamiltonian $\hat H$ is itself an observable: it represents total energy, and its eigenvalues are the energies the system can actually be measured to have.

## 7. Eigenvectors and Eigenvalues
For an observable $\hat A$, a state satisfying $\hat A \psi = a\psi$ is an eigenstate, and $a$ is its eigenvalue. Physically, eigenstates are exactly the states with a definite value for that observable: measuring $\hat A$ on the state $\psi$ is guaranteed to return $a$. Because $\hat A$ is Hermitian, its eigenvectors form a complete orthonormal basis for the Hilbert space — every possible state can be written as a combination of them, which is what makes superposition meaningful.

## 8. Commutators
The commutator of two operators, $[\hat A, \hat B] = \hat A \hat B - \hat B \hat A$, measures the extent to which order of operation matters, and is the quantum inheritor of the classical Poisson bracket. Position and momentum satisfy the canonical commutation relation $[\hat x, \hat p] = i\hbar$ — never zero — and this single nonzero result is the algebraic root of most distinctly quantum behavior, including the uncertainty principle. Two observables that do commute share a common set of eigenstates and can, in principle, be known simultaneously with arbitrary precision.

## 9. Superposition
Because the Schrödinger equation is linear, any combination $\psi = c_1\psi_1 + c_2\psi_2 + \dots$ of valid states is itself a valid state. When the $\psi_i$ are eigenstates of some observable with distinct eigenvalues $a_i$, a system in the superposition $\psi$ does not have a definite value of that observable at all — measurement returns $a_i$ with probability $|c_i|^2$, and only after the measurement is the state left in the corresponding eigenstate. Superposition is the formal statement of what it means for a quantum state to be genuinely indefinite, rather than merely unknown to the observer.

## 10. Uncertainty Principle
Because position and momentum operators do not commute, no state can be a simultaneous eigenstate of both — there is no state with an exactly definite position and an exactly definite momentum at once. This is formalized by the Heisenberg uncertainty relation,

$$\Delta x \, \Delta p \geq \frac{\hbar}{2}$$

where $\Delta x$ and $\Delta p$ are the standard deviations of position and momentum in a given state. The result generalizes to any pair of non-commuting observables, $\Delta A\, \Delta B \geq \tfrac{1}{2}\left|\langle[\hat A, \hat B]\rangle\right|$, making the uncertainty principle a direct algebraic consequence of the commutator structure introduced above, not an added postulate.

---

Previous: [Lesson 01a — Classical Mechanics](./classical-mechanics.md)

[^linalg]: The linear algebra underlying quantum mechanics has two workhorse classes of operator, each chosen because it preserves something physically essential.

    A **Hermitian** (or self-adjoint) operator $\hat A$ satisfies $\hat A = \hat A^\dagger$, where the adjoint $\hat A^\dagger$ is defined by demanding $\langle \phi \vert \hat A^\dagger \psi \rangle = \langle \hat A \phi \vert \psi \rangle$ for all states. In matrix language this means $\hat A^\dagger = (\hat A^*)^T$ — conjugate every entry, then transpose. Two consequences follow immediately from this definition. First, all eigenvalues are real: if $\hat A \psi = \lambda \psi$ then $\lambda = \langle \psi \vert \hat A \psi \rangle / \langle \psi \vert \psi \rangle$, and Hermiticity forces that ratio to equal its own complex conjugate, so $\lambda \in \mathbb{R}$. Since every measurement outcome must be a real number, observables must be Hermitian — there is no other choice consistent with the formalism. Second, eigenvectors belonging to distinct eigenvalues are orthogonal: if $\hat A \psi_1 = \lambda_1 \psi_1$ and $\hat A \psi_2 = \lambda_2 \psi_2$ with $\lambda_1 \neq \lambda_2$, then $(\lambda_1 - \lambda_2)\langle \psi_2 \vert \psi_1 \rangle = 0$, forcing $\langle \psi_2 \vert \psi_1 \rangle = 0$. Taken together these two facts mean a Hermitian operator always supplies a complete orthonormal basis of eigenstates for the Hilbert space — the spectral theorem — which is exactly what is needed to expand an arbitrary state as a superposition and read off measurement probabilities as squared coefficients.

    A **unitary** operator $\hat U$ satisfies $\hat U^\dagger \hat U = \hat U \hat U^\dagger = \hat I$, the identity. Equivalently, $\hat U^\dagger = \hat U^{-1}$. In matrix language every column (and every row) of a unitary matrix forms an orthonormal set. Unitarity is the condition that preserves the inner product: $\langle \hat U \phi \vert \hat U \psi \rangle = \langle \phi \vert \hat U^\dagger \hat U \psi \rangle = \langle \phi \vert \psi \rangle$. Because the norm $\lVert \psi \rVert^2 = \langle \psi \vert \psi \rangle$ is the total probability, a norm-preserving map is one that keeps total probability equal to one. Time evolution must therefore be unitary: if $\hat H$ is Hermitian, the time-evolution operator $\hat U(t) = e^{-i\hat H t/\hbar}$ is unitary, and the Schrödinger equation is precisely the statement that states evolve by unitary maps. Measurement, by contrast, is not unitary — it collapses the state onto an eigenspace, which does not preserve the inner product with the pre-measurement state, and this non-unitarity is the formal expression of the irreversibility of measurement.

    The two classes are related by a simple correspondence: if $\hat A$ is Hermitian then $e^{i\hat A}$ is unitary, and conversely every unitary operator near the identity can be written in this exponential form with a Hermitian generator. In physics this connection runs everywhere — the Hamiltonian generates time translations, the momentum operator generates spatial translations, angular momentum generates rotations — and in each case the generator is Hermitian (an observable) while the finite transformation it produces is unitary (a symmetry operation that preserves probability).

## 11. Personal Notes

The biggest takeaway for me is the introduction of the system state as something different from the positions and velocities of the parts. In mechanics, classical or not, we are interested in the evolution of a system: where "things" are at some later point in the future. So we naturally take the positions (and velocities) as the state. That works as long as the equations directly involve positions, and Newton's law gives us exactly that. But in quantum mechanics, position is no longer certain.

Not *uniformly* uncertain, though. In most cases we can make educated guesses about where the particle is; we just cannot be 100% sure it is at a given spot. The best tool for capturing this situation is the wave function, and it is already very odd. It looks like a cop-out: "you say we MUST use a probability, but really it's because you do not know your system fully. Git gud bro." The rebuttal is Bell's inequality[^bell]. The debate about interpretations continues; what is undeniable is that *mathematically*, we can solve problems without hidden variables. IMO this is like thermodynamics: we know temperature comes from the agitation of molecules, but we don't care, since we get results by using the macroscopic view. I am sure some people will say it is not the same in QM: in QM there is *no* hidden variable, etc. It's philosophical and I don't want to get into it. But, as a result, QM is rejected by many as non-sensical, obviously wrong, stupid, and so on. I don't particularly care. I take it as a different set of rules. Our intuition does not apply here: it is a new "game". Learn the rules and play by them.

Speaking of games, back to the system state. In QM, position (and many other quantities) is no longer deterministic, but that's not the whole truth either: we can know with great precision, but there will always be *some* uncertainty left over. In theory, we could know the position exactly but then we would know nothing about the momentum (which could even be faster than light).

Our best tool is the mathematics of probabilities.
If you played Poker, you know what I mean.

Usually, when we don't know something for sure, we replace it with a probability, but that turns out to be useless here, because probabilities don't add the way QM needs. Instead, QM tracks the **probability amplitude** (the wave function), which relates to the position probability by

$$P(x, t) = |\Psi(x, t)|^2 = \Psi^*(x, t)\,\Psi(x, t).$$

The amplitude is an intermediate value that greatly simplifies the math: it is complex, and its phase is exactly what produces interference ([§3](#_3-wave-amplitude)), something no plain probability can do.

Imagine you make a video game. You have sprites. You need to animate them according to the game logic: in a platform game, sprites move, jump, but don't go through platforms. To track all of this, you keep the sprite coordinates, so the logic can check collisions. But the player does not see any of that: he sees the sprites drawn on the screen.

In QM, we track the wave function because we have tools that work on it: the Schrödinger equation for the evolution of the system, the momentum operator for momenta, and so on. The logic runs on the state; the observable outcomes are "rendered" at the end.

These calculations preserve the character of the state: inputs are probability-like (more precisely, vectors), outputs are probability-like too, and the maps between them are *linear*: the mathematical statement that a superposition of states evolves into the superposition of their evolutions. It doesn't have to be this way, but it is what makes a theory usable: you can decompose a complicated situation into manageable pieces, evolve the pieces, and recombine.

We have to be careful about what the state is *made of*, though. If we represented states by ordinary real numbers (0, 1, 1.3, etc.), the theory's predictions would not match experiments. With complex numbers (numbers with two parts, a real and an imaginary part), we can predict the experimental results; in particular, we get interference. So even though complex numbers are impossible to visualize, we must use them if we want the theory to work. Relativity asks for the same leap: spacetime is impossible to visualize, but it is an invaluable tool. The mathematics there gets harder because distance in spacetime is not the usual one, but there is a branch of mathematics (differential geometry) that deals with exactly that.

I think the bottom line is that the theory is much easier to work with when we don't try to interpret the equations along the way. Like the video game: do the logic and calculations with the state, then "render", i.e. calculate the probabilities that can be observed.

[^pos-rep]: A state vector $\psi$ is an abstract object in Hilbert space — it does not inherently "live" anywhere. A **representation** is a choice of basis that turns that abstract vector into a concrete function. In the **position representation** you project onto eigenstates of $\hat x$, giving the wavefunction $\psi(x)$: a complex amplitude at each point in space. In that basis $\hat x$ acts by multiplying by $x$ and $\hat p$ acts by $-i\hbar\,\partial/\partial x$. In the **momentum representation** the roles swap — $\hat p$ multiplies by $p$ and $\hat x$ acts by $i\hbar\,d/dp$ — and the two pictures are related by a Fourier transform. The form $\hat p = -i\hbar\,\partial/\partial x$ is therefore not a fundamental definition; it is what the abstract momentum operator looks like once you have committed to describing states as functions of position.

[^bell]: The "you just don't know the system fully" program is called a **hidden-variable** theory, and Bell's theorem (J. S. Bell, *On the Einstein–Podolsky–Rosen paradox*, Physics 1, 195 (1964)) shows that any such theory obeys an inequality that quantum mechanics violates. The violation is not a matter of taste: it was measured, first by Clauser and Freedman (1972), more sharply by Aspect (1982), and in loophole-free form by the experiments recognized with the 2022 Nobel Prize (Aspect, Clauser, Zeilinger). So the "Git gud" reading, restoring certainty by finding the hidden layer, is not merely unfinished; it is experimentally excluded for the whole class of theories Bell's argument covers. What survives the theorem are escapes of a subtler kind (superdeterminism, many worlds, and other reinterpretations), which is why the debate the text mentions is philosophical rather than empirical.

