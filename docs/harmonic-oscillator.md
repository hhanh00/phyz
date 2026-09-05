# The Harmonic Oscillator

## 1. Why the harmonic oscillator

A harmonic oscillator is a system whose potential energy grows as the square of its displacement from equilibrium. It is the most common system in physics, not a special one, because near any stable minimum a smooth potential is quadratic to first order: the linear term vanishes at a minimum, and the constant term only shifts the zero of energy. Write

$$V(x) \approx V(x_0) + \tfrac12 V''(x_0)\,(x - x_0)^2.$$

So a pendulum at small angles, an atom rattling inside a molecule, and the atoms of a crystal lattice all behave as oscillators when disturbed gently. This is why the oscillator, rather than any more complicated system, is the standard first worked example in quantum mechanics — and why it returns in field theory, where each momentum mode of a free field turns out to be exactly such a system.

## 2. The classical oscillator

Take a mass $m$ on a spring of stiffness $k$. Its energy is

$$H = \frac{p^2}{2m} + \tfrac12 m\omega^2 x^2, \qquad \omega = \sqrt{k/m},$$

with $\omega$ the natural frequency. The two terms are the kinetic and elastic energies. The frequency is fixed by the system; the energy is set by how hard you drive it. Drive gently and the mass oscillates with a small amplitude, drive hard and the amplitude grows, always at the same frequency.

In phase space the state is a point $(x, p)$, and a fixed-energy orbit is an ellipse: as the spring stores and releases energy, $x$ and $p$ trade places around that ellipse. The [Field Quantization](field-quantization.md) page reuses this picture, one momentum mode at a time.

## 3. Quantization

[First Quantization](first-quantization.md) supplies the method: promote the coordinate and momentum to operators and impose the canonical commutator,

$$[\hat x, \hat p] = i\hbar,$$

so the Hamiltonian becomes the operator

$$\hat H = \frac{\hat p^2}{2m} + \tfrac12 m\omega^2 \hat x^2.$$

The problem is now the eigenvalue equation $\hat H\psi = E\psi$. Solving it directly means facing a second-order differential equation, but the commutator offers a route that never writes $\psi$ down.

## 4. Ladder operators

The commutator $[\hat x, \hat p] = i\hbar$ alone determines the spectrum, and the fastest way to see it is to combine $\hat x$ and $\hat p$ into a pair of operators that step between energy levels. Define

$$\hat a = \sqrt{\frac{m\omega}{2\hbar}}\,\hat x + \frac{i}{\sqrt{2m\hbar\omega}}\,\hat p, \qquad \hat a^\dagger = \sqrt{\frac{m\omega}{2\hbar}}\,\hat x - \frac{i}{\sqrt{2m\hbar\omega}}\,\hat p.$$

The two are each other's adjoint, and their commutator follows directly from $[\hat x, \hat p] = i\hbar$:

$$[\hat a, \hat a^\dagger] = 1.$$

Inverting the definitions expresses $\hat x$ and $\hat p$ in terms of $\hat a$ and $\hat a^\dagger$, and substituting into $\hat H$ turns the Hamiltonian into

$$\hat H = \hbar\omega\left(\hat a^\dagger\hat a + \tfrac12\right).$$

The frequency now appears as a fixed unit, $\hbar\omega$, multiplying a single counting operator plus a constant. Everything about the spectrum lives in that operator.

## 5. The number operator and the spectrum

Name the counting operator $\hat N = \hat a^\dagger\hat a$. From $[\hat a, \hat a^\dagger] = 1$ follow the two relations

$$[\hat N, \hat a] = -\hat a, \qquad [\hat N, \hat a^\dagger] = \hat a^\dagger,$$

which say that $\hat a$ lowers the count by one and $\hat a^\dagger$ raises it by one. Lowering cannot continue forever, because $\hat N$ has nonnegative eigenvalues: for any state, $\langle\psi|\hat N|\psi\rangle = \lVert \hat a|\psi\rangle\rVert^2 \ge 0$. There is therefore a lowest state $\lvert 0\rangle$ that lowering annihilates, $\hat a\lvert 0\rangle = 0$, with $\hat N = 0$.

Raising from the floor generates the whole spectrum. The state $\lvert n\rangle \propto (\hat a^\dagger)^n\lvert 0\rangle$ has $\hat N\lvert n\rangle = n\lvert n\rangle$ for every nonnegative integer $n$, and energy

$$E_n = \hbar\omega\left(n + \tfrac12\right).$$

The levels form an evenly spaced ladder with spacing $\hbar\omega$: $\hat a^\dagger$ adds one quantum and $\hat a$ removes one, which is why they are called creation and annihilation operators. Their explicit action on a state of $n$ quanta is

$$\hat a\,\lvert n\rangle = \sqrt{n}\;\lvert n-1\rangle, \qquad \hat a^\dagger\,\lvert n\rangle = \sqrt{n+1}\;\lvert n+1\rangle,$$

with $\hat a\lvert 0\rangle = 0$, since nothing sits below the floor. The $\sqrt{\,}$ factors normalize the states: because $\lvert n\rangle = \frac{(\hat a^\dagger)^n}{\sqrt{n!}}\lvert 0\rangle$, each application of $\hat a$ or $\hat a^\dagger$ must multiply by the constant that keeps $\langle n\lvert n\rangle = 1$.

## 6. Zero-point energy

The floor itself is nonzero. The lowest state carries energy $\tfrac12\hbar\omega$, so the oscillator never rests. This follows from $[\hat x, \hat p] = i\hbar$: a state at rest would have $\hat x$ and $\hat p$ both fixed, and no state can fix two noncommuting observables at once. The $\tfrac12\hbar\omega$ is the price of position and momentum failing to commute.

## 7. Why it matters later

The [Field Quantization](field-quantization.md) page uses everything in this page without redoing it. There the free scalar field is expanded in spatial Fourier modes, and each momentum $\mathbf p$ decouples into an independent copy of the oscillator solved here, with frequency $E_p/\hbar$ set by the particle's energy. Because the oscillator's spectrum is already known, the field's spectrum follows by reading the levels once per momentum. That page absorbs the mass into a rescaled coordinate, so its Hamiltonian reads $\hat H = \tfrac12\hat p^2 + \tfrac12\omega^2\hat q^2$ and its ladder operators drop the $m$; it is the same oscillator with the same algebra, only relabeled.

---

Previous: [First Quantization](./first-quantization.md)

Next: [Special Relativity](./special-relativity.md)
