# First Quantization

[Quantum Ideas](./quantum-ideas.md) showed, from experiments, that a state is a list of amplitudes, and that measurements give random results with chances set by those amplitudes. This chapter turns those ideas into maths. It also keeps the two promises chapter 1 ended with: the Hamiltonian keeps its job of moving the state forward in time, and the Poisson bracket of position with momentum gets a quantum version.

Here's where we end up. Each idea from chapter 1 gets a quantum counterpart:

| | Classical (chapter 1) | Quantum (this chapter) |
| --- | --- | --- |
| The state | A point: position and momentum | A list of complex numbers called **amplitudes**, one for each possible outcome |
| A measurable quantity | A number worked out from the state | An **operator** (section 1) |
| A measurement gives | The value, exactly | One of the possible results, at random |
| What moves the state | Hamilton's equations, from $H$ | The **Schrödinger equation**, from the same $H$ |
| Position with momentum | Their bracket is 1 | Their **commutator** is $i\hbar$, with $\hbar$ a tiny constant (section 2) |

Turning classical quantities into operators like this is called **first quantization**. It's "first" because it quantizes the motion of particles; [Field Quantization](./field-quantization.md) later does the same to fields.

## 1. Measured quantities become operators

A measurable quantity now needs two things: its possible values, and for each value the state that gives it for certain. That's because of how chapter 2a's chances work. The amplitude a state $\psi$ has for a result $a$ is called its **overlap** with that result's certain state, written $\langle a\vert\psi\rangle$, and the chance of the result is its squared length. The overlap multiplies the two states' amplitudes pair by pair and adds, after conjugating the first, $\langle a\vert\psi\rangle = \sum_k a_k^*\psi_k$ (see [conjugation](appendix-math-complex.md#_5-conjugation-and-the-adjoint) and [bra-ket notation](appendix-math-linear-algebra.md#_5-inner-products-and-bra-ket-notation)). An **operator** is a rule that takes a state and returns another state, and it packages both. Applied to one of its certain states, it just multiplies the state by its value:

$$\hat A\lvert a\rangle = a\lvert a\rangle.$$

Any other state is a mix of these certain states, the way the tilted spin was a mix of up and down. And an operator is **linear**: it acts on each part of a mix separately and adds the results. So on a mix it multiplies each part by that part's own value,

$$\hat A\big(c_1\lvert a_1\rangle + c_2\lvert a_2\rangle\big) = c_1 a_1\lvert a_1\rangle + c_2 a_2\lvert a_2\rangle.$$

The certain states are called **eigenstates**, and the values **eigenvalues** (see the [Math Refresher](appendix-math-linear-algebra.md#_4-eigenvalues-and-eigenvectors)). For the spin, the vertical magnet's operator has the eigenstates up and down, which we give the values $+1$ and $-1$. The sideways magnet's operator has the eigenstates right and left, also with the values $+1$ and $-1$.

Not every operator will do: measured values are real, and a state that gives one value for certain can never give another, so different certain states can't overlap. Operators with both properties are called **Hermitian** (the box has the details), and the quantities they describe are **observables**. (Applying an operator isn't the same as measuring; chapter 2a covers what a measurement does to the state.)

**The average.** Repeat a measurement on many identically prepared atoms, and the results have an average, called the **expectation value** $\langle A\rangle$, and a spread around it, $\Delta A$ (which section 4 uses). Take atoms tilted 60° to the right, whose amplitudes are $\sqrt3/2$ and $1/2$ (chapter 2a's section 4 box gives the rule). Measured sideways, they give $+1$ 93.3% of the time and $-1$ 6.7% of the time, so the average is about 0.87. The operator gives the same number directly. Since it multiplies each certain-state part by its value, the overlap of the state with the operator applied to the state, written $\langle\psi\vert\hat A\vert\psi\rangle$, adds up each value times its chance. The mixed terms drop out, because different certain states don't overlap.

**Order matters.** With ordinary numbers, $ab = ba$. With operators, the order you apply them in can change the answer. The **commutator** measures by how much:

$$[\hat A, \hat B] = \hat A\hat B - \hat B\hat A.$$

If two operators shared all their certain states, the order wouldn't matter, and their commutator would be zero. So when the commutator isn't zero, there are states that are sharp for one quantity and spread out for the other. The magnets in a row showed exactly that: up-and-down and right-and-left don't commute, and atoms that were certainly "right" came out up and down half and half.

<details>
<summary>The calculation: the spin's operators</summary>

Write a spin state as the column of its two amplitudes (see [matrices](appendix-math-linear-algebra.md#_2-operators-and-matrix-multiplication) in the Math Refresher). The vertical operator $\hat Z$ and the sideways operator $\hat S$ are

$$\hat Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}, \qquad \hat S = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}.$$

$\hat Z$ leaves "up", $(1, 0)$, unchanged and turns "down", $(0, 1)$, into its negative.

$\hat S$ swaps the two amplitudes. It leaves "right", $(1, 1)/\sqrt2$, unchanged, so its value is $+1$, and turns "left", $(1, -1)/\sqrt2$, into its negative, so its value is $-1$.

**The average and the spread.** For the right-tilted atoms, $\langle S\rangle = (+1)(0.933) + (-1)(0.067) = 0.866$. From the operator, $\hat S$ swaps $(\sqrt3/2,\ 1/2)$ to $(1/2,\ \sqrt3/2)$, and the overlap with the state is $\sqrt3/4 + \sqrt3/4 \approx 0.866$. Every result squared is 1, so $\langle S^2\rangle = 1$, and the spread is $\Delta S = \sqrt{\langle S^2\rangle - \langle S\rangle^2} = \sqrt{1 - 0.75} = 0.5$.

**The commutator.**

$$[\hat Z, \hat S] = \begin{pmatrix} 0 & 2 \\ -2 & 0 \end{pmatrix},$$

which isn't zero.

</details>

<details>
<summary>Reference: Hermitian operators</summary>

A **Hermitian** operator satisfies $\hat A = \hat A^\dagger$, where the **adjoint** $\hat A^\dagger$ is defined by $\langle\phi\vert\hat A^\dagger\psi\rangle = \langle\hat A\phi\vert\psi\rangle$. For matrices, $\hat A^\dagger = (\hat A^*)^T$: conjugate the entries, then transpose. Both $\hat Z$ and $\hat S$ above are Hermitian.

Its eigenvalues are real. If $\hat A\psi = \lambda\psi$, then $\lambda = \langle\psi\vert\hat A\psi\rangle/\langle\psi\vert\psi\rangle$, and Hermiticity makes the numerator equal its own conjugate. Eigenvectors with different eigenvalues are orthogonal: computing $\langle\psi_2\vert\hat A\psi_1\rangle$ two ways gives $\lambda_1\langle\psi_2\vert\psi_1\rangle = \lambda_2\langle\psi_2\vert\psi_1\rangle$. The spectral theorem says a Hermitian operator has enough eigenvectors to write any state in them; written that way, the squared amplitudes are the chances of each value, and $\langle\psi\vert\hat A\vert\psi\rangle$ adds up each value times its chance. Position and momentum can take any value, so their sums become integrals, and their certain states, a spike at one point or an endless wave, can't be scaled to length one.

</details>

**Each measurable quantity is an operator, and the order of two operators can matter.**

## 2. Position and momentum operators

**Position.** The certain states of position are wave functions squeezed onto a single point. On a state squeezed onto the point $a$, multiplying by $x$ is the same as multiplying by $a$, its value. So the position operator, $\hat x$, just multiplies the wave function by $x$.

**What momentum does in chapter 1.** For momentum, start from classical mechanics. Chapter 1's Poisson bracket tells us what momentum's job is. Take any quantity $f$ that depends only on position, and bracket it with momentum:

$$\{f, p\} = \frac{\partial f}{\partial q}\,\frac{\partial p}{\partial p} - \frac{\partial f}{\partial p}\,\frac{\partial p}{\partial q} = \frac{\partial f}{\partial q}\cdot 1 - 0\cdot 0 = \frac{\partial f}{\partial q}.$$

So, classically, bracketing with momentum takes slopes along position. For $f = q$, it's the familiar $\{q, p\} = 1$.

**The quantum rule.** Chapter 1 promised the bracket a quantum version. The commutator is the natural stand-in: like the bracket, it flips sign when you swap the two quantities, it follows the same product rule, and it's zero for ordinary numbers, just as a bracket is zero for constants. So replace each Poisson bracket by a commutator divided by $i\hbar$:

$$\{f, g\} \;\to\; \frac{1}{i\hbar}\,[\hat f, \hat g].$$

The constant $\hbar$, read "h-bar", is $h/2\pi = 1.055\times10^{-34}$ J s, built from chapter 2a's Planck constant $h$. It supplies the units, and the $i$ makes the result a real quantity, like a bracket (the box shows why). This rule is the heart of first quantization. It's a guess, and experiment has to test it, which we'll do in a moment.

**The momentum operator.** Writing the position as $x$ from here on, the rule says the commutator of any $f(x)$ with $\hat p$, divided by $i\hbar$, must be the slope of $f$. (Like $\hat x$, $f$ just multiplies the wave function.) One operator does exactly that: $-i\hbar$ times the slope, as the box shows using the product rule. So

$$\hat p = -i\hbar\,\frac{d}{dx}, \qquad [\hat x, \hat p] = i\hbar.$$

The second is the case $f = x$: chapter 1's $\{q, p\} = 1$, times $i\hbar$. Position and momentum don't commute.

**The check: de Broglie's waves.** Which states have a definite momentum under this operator? Ones whose slope is just the state times a fixed number. Those are exponentials:

$$\psi_p(x) = e^{ipx/\hbar}, \qquad \hat p\,\psi_p = p\,\psi_p.$$

This wave has size 1 everywhere, and its phase turns steadily as you move along (see [Euler's formula](appendix-math-complex.md#_2-the-complex-plane-and-euler-s-formula) in the Math Refresher), making a full turn every $2\pi\hbar/p = h/p$. That's de Broglie's wavelength, from chapter 2a. The constant $h$ was measured with light, in the photoelectric effect. So, with nothing adjusted, the operator built from chapter 1's bracket predicts that an electron with momentum $p$ behaves like a wave of wavelength $h/p$, and Davisson and Germer's electrons confirmed it. (Like the state squeezed onto one point for position, this wave is an idealization: it spreads over all space, so its total area isn't one. Real states are sums of such waves.)

<details>
<summary>The calculation: the commutator, and why the i and the ħ</summary>

**The commutator.** Apply both orders to a wave function $\psi(x)$, using the product rule:

$$[f, \hat p]\psi = f\,(-i\hbar\,\psi') + i\hbar\,(f\psi)' = -i\hbar\,f\psi' + i\hbar\,(f'\psi + f\psi') = i\hbar\,f'\psi.$$

The terms with $\psi'$ cancel, and what survives comes from the slope of $f$. So $[f, \hat p]/i\hbar = f'$, the quantum version of $\{f, p\} = \partial f/\partial q$. With $f = x$, $[\hat x,\hat p] = i\hbar$. For example, with $\psi = x^2$: $\hat x\hat p\,x^2 = -2i\hbar\,x^2$ and $\hat p\hat x\,x^2 = -3i\hbar\,x^2$, a difference of $i\hbar\,x^2$.

**Why $i$.** The commutator of two Hermitian operators is minus its own adjoint, because $(\hat A\hat B)^\dagger = \hat B\hat A$. Dividing it by $i$ makes it Hermitian, so its values are real, like a Poisson bracket's.

**Why $\hbar$.** $[\hat x, \hat p]$ has units of position times momentum, the units of $\hbar$, while $\{q, p\} = 1$ has none. The $\hbar$ supplies the units. Its size, $h/2\pi$, takes $h$ from experiments on light; the electron wavelength $h/p$ is then a prediction.

**Representations.** A state doesn't depend on a choice of basis. In the position representation used here, the amplitudes are $\psi(x)$, $\hat x$ multiplies by $x$ and $\hat p$ acts as $-i\hbar\,d/dx$. In the momentum representation, $\hat p$ multiplies by $p$ and $\hat x$ acts as $i\hbar\,d/dp$. A [Fourier transform](appendix-math-complex.md#_4-waves-and-the-fourier-transform) relates the two.

</details>

**Position multiplies by $x$, momentum takes the slope, as chapter 1's bracket demands, and the two don't commute: $[\hat x, \hat p] = i\hbar$.**

## 3. The energy moves the state: the Schrödinger equation

**The energy operator.** In chapter 1, the Hamiltonian $H = p^2/2m + V(x)$ moved the state forward. Quantum mechanics keeps the same function and puts the momentum operator into it. Taking the slope twice brings two factors of $-i\hbar$, which multiply to $-\hbar^2$, so

$$\hat H = -\frac{\hbar^2}{2m}\frac{d^2}{dx^2} + V(x).$$

Its certain states are the **states of definite energy**, and any state can be written as a mix of them. So to move a state forward in time, it's enough to know how each of those moves.

**A definite energy turns the phase.** De Broglie read chapter 2a's $E = hf$ for light the other way too: a particle with energy $E$ oscillates at the frequency $f = E/h$. So its phase turns steadily, a full turn every $h/E$ seconds, which after a time $t$ is an angle of $2\pi Et/h = Et/\hbar$. As a complex factor, the state has picked up

$$e^{-iEt/\hbar}.$$

That's the time version of the momentum wave $e^{ipx/\hbar}$; the minus sign makes waves move the way their momentum points (the unitary box shows why). De Broglie proposed the rule for free particles; taking it for every system is an assumption, and experiment has confirmed it ever since. Every amplitude of the state picks up the same factor, so the whole state turns together and no relative phase changes. So no chance changes, and a state of definite energy looks exactly the same at every moment. These are called **stationary states**.

**The Schrödinger equation.** Now put the two together. The rate of change of $e^{-iEt/\hbar}$ in time brings down $-iE/\hbar$, so $i\hbar$ times the rate of change of a state of definite energy is $E$ times the state. And $\hat H$ applied to that state also gives $E$ times the state, since it's one of $\hat H$'s certain states. Writing $\Psi(x, t)$ for the wave function as it changes in time, with $\partial$ for a rate of change in one variable while the other is held fixed, every state of definite energy obeys

$$i\hbar\,\frac{\partial\Psi}{\partial t} = \hat H\,\Psi.$$

Any state is a mix of states of definite energy, and both sides are linear, so every state obeys it. This is the **Schrödinger equation**. Like Hamilton's equations, it has one rate of change in time, so the state now fixes its future. Notice the parallel: a rate of change in time, times $i\hbar$, stands for the energy, just as a slope times $-i\hbar$ stands for the momentum.

**What the equation does.** Two more things follow:

1. **It keeps the total chance at one.** Each piece only turns its phase, so none of the energy amplitudes grows or shrinks. The step that moves the state forward is called **unitary**: it keeps the total chance, and every overlap, the same.
2. **Averages follow chapter 1's rule.** The average of any quantity changes at a rate set by its commutator with $\hat H$, divided by $i\hbar$. That's chapter 1's rule, rate of change equals the bracket with $H$, with the bracket replaced by the commutator. For position and momentum it gives Hamilton's equations for the averages, with the force averaged over the state.

<details>
<summary>The calculation: why the averages follow chapter 1</summary>

Write $\langle A\rangle = \langle\Psi\vert\hat A\vert\Psi\rangle$ and differentiate both copies of $\Psi$. The Schrödinger equation gives $\partial_t\lvert\Psi\rangle = \tfrac{1}{i\hbar}\hat H\lvert\Psi\rangle$, and its adjoint gives $\partial_t\langle\Psi\rvert = -\tfrac{1}{i\hbar}\langle\Psi\rvert\hat H$, because $\hat H$ is Hermitian. So

$$\frac{d\langle A\rangle}{dt} = \frac{1}{i\hbar}\langle[\hat A,\hat H]\rangle.$$

For position, $[\hat x,\hat p^2] = 2i\hbar\,\hat p$, so $d\langle x\rangle/dt = \langle p\rangle/m$. For momentum, $[\hat p, V]\psi = -i\hbar\,V'\psi$, so $d\langle p\rangle/dt = -\langle V'\rangle$: the force averaged over the state. That equals the force at the average position when the force barely changes across the state, and exactly for a spring or a constant force.

</details>

<details>
<summary>Reference: unitary operators and generators</summary>

Collect the phase factors into one operator $\hat U(t)$, which multiplies each state of definite energy $E$ by $e^{-iEt/\hbar}$, so that $\lvert\Psi(t)\rangle = \hat U(t)\lvert\Psi(0)\rangle$. It's written $e^{-i\hat Ht/\hbar}$, because on those states $\hat H$ acts as the number $E$.

A **unitary** operator satisfies $\hat U^\dagger\hat U = \hat U\hat U^\dagger = \hat I$, so it preserves overlaps: $\langle\hat U\phi\vert\hat U\psi\rangle = \langle\phi\vert\psi\rangle$. For Hermitian $\hat G$, $e^{-i\theta\hat G}$ is unitary. Conversely, a smooth family of unitary transformations with $\hat U(a)\hat U(b) = \hat U(a + b)$ can be written $\hat U(\theta) = e^{-i\theta\hat G}$ with $\hat G$ Hermitian, called its **generator**. The Hamiltonian divided by $\hbar$ is the generator of time evolution.

A crest of $e^{i(px - Et)/\hbar}$, where $px - Et$ is fixed, moves at $x = (E/p)\,t + \text{const}$, toward $+x$ when $p > 0$. That's why the time factor is $e^{-iEt/\hbar}$ with a minus sign, opposite to the plus in $e^{ipx/\hbar}$.

</details>

**The Hamiltonian keeps its job: it now moves a list of amplitudes instead of a point.**

## 4. Why position and momentum cannot both be sharp

<!-- TODO (Hanh, 2026-11-25): uncertainty was taken out of chapter 2a and belongs here. Plan: open this section from what
the reader sees (narrow a slit and the electrons spread wider), give the intuition with an everyday analogy (a long steady
note has one pitch, a short click is a jumble of many pitches), and keep the Fourier picture in a box with the WaveSum
figure (scene WaveSum in docs/manim/page_diagrams.py, drafted, not yet registered; its one-wavelength row is too crowded).
Bring back the electron-versus-ball paragraph and its numbers box from the old chapter 2 (git show
fff1299:docs/first-quantization.md, "An electron and a ball"). The figure fourier-uncertainty.png (scene
FourierUncertainty) is unused but kept for this section. Say "the length of the arrow" rather
than "size" for a momentum wave. -->

Squeezing a particle's position spreads its momentum. The commutator gives the reason in a few lines. Suppose some state had a sharp position and a sharp momentum at once. Each operator would just multiply it by a number, and numbers don't care about order, so their commutator would give zero. But the commutator gives $i\hbar$ times the state, which isn't zero. So no such state exists. The best a state can do is keep both spreads small, and the commutator sets how small. This is the **Heisenberg uncertainty relation**:

$$\Delta x\,\Delta p \ \ge\ \frac{\hbar}{2}.$$

For other pairs of quantities the bound is half the average of their commutator, so it can depend on the state (box).

<details>
<summary>The calculation: the general bound</summary>

**Any two observables.** The product of their spreads is at least half the size of the average of their commutator, $\Delta A\,\Delta B \ge \tfrac12\lvert\langle[\hat A,\hat B]\rangle\rvert$. To show it, define $\lvert u\rangle = (\hat A - \langle A\rangle)\lvert\psi\rangle$ and $\lvert v\rangle = (\hat B - \langle B\rangle)\lvert\psi\rangle$, whose squared lengths are the squared spreads. The Cauchy–Schwarz inequality gives $(\Delta A)^2(\Delta B)^2 \ge \lvert\langle u\vert v\rangle\rvert^2 \ge (\operatorname{Im}\langle u\vert v\rangle)^2$, and $2i\operatorname{Im}\langle u\vert v\rangle = \langle u\vert v\rangle - \langle v\vert u\rangle = \langle[\hat A,\hat B]\rangle$. With $[\hat x,\hat p] = i\hbar$ this gives $\Delta x\,\Delta p \ge \hbar/2$. The bound is about the spreads within one state, not about disturbance by a measuring device.

</details>

**The commutator $[\hat x, \hat p] = i\hbar$ is why position and momentum can't both be sharp.**

## Where this comes back

The next chapter, [The Harmonic Oscillator](./harmonic-oscillator.md), runs these rules on chapter 1's spring, from start to finish. It finds the spring's energies from the commutator $[\hat x, \hat p] = i\hbar$ alone, and they come in evenly spaced steps.

Further on, [Field Quantization](./field-quantization.md) applies the same bracket-to-commutator rule to a field, with a pair of operators at every point of space. And the unitary step that moves a state forward in time returns in [Symmetries](./symmetries.md) and [Quantum Field Theory](./qft.md).

---

Previous: [Quantum Ideas](./quantum-ideas.md)

Next: [The Harmonic Oscillator](./harmonic-oscillator.md)
