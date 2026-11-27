# Solutions of the Dirac Equation

The last chapter found the electron's spin inside Dirac's equation, with the electron at rest throughout. This chapter gives the electron some momentum and finishes the account of the four wave functions. A moving electron's solution fills both pairs of the column. Each negative-energy solution turns out to describe a positron. And the sum of all the solutions is the formula the next chapter starts from.

**What chapter 6a found.** Three facts carry over.

- The state is a column of four wave functions, an upper pair $(\psi_1, \psi_2)$ and a lower pair $(\psi_3, \psi_4)$.
- For a particle at rest, the upper pair has energy $+mc^2$ and the lower pair has $-mc^2$.
- In each pair the first entry is spin up and the second is spin down, and the spin is $\hbar/2$ in size.

Here is where we end up, for a particle at rest:

| Entry of the column | Energy | Spin | What it describes (section 2) |
| --- | --- | --- | --- |
| $\psi_1$ | $+mc^2$ | up | An electron, spin up |
| $\psi_2$ | $+mc^2$ | down | An electron, spin down |
| $\psi_3$ | $-mc^2$ | up | A positron, spin down |
| $\psi_4$ | $-mc^2$ | down | A positron, spin up |

In the last two rows the positron's spin is the opposite of the entry's. Section 2 explains the flip.

## 1. A moving electron

So far the electron has been at rest. Now give it some momentum.

**The entries mix.** At rest, a positive-energy solution fills only the upper pair. [Chapter 6a's section 2](dirac-equation.md#_2-four-wave-functions-and-one-question) noted that each $\alpha$ sends the upper pair to the lower pair. With a momentum, the $\alpha$ terms in $\hat H$ are no longer zero, so the lower pair can't stay empty.

Take an electron moving up, along $z$, with momentum $p$ and positive energy $E = \sqrt{(pc)^2 + (mc^2)^2}$, and start from the first solution at rest, with only the first entry filled. The momentum term is now $c\,\alpha_z\,p$, and $\alpha_z$ sends the first entry to the third. For a wave of energy $E$ the equation reads $E\psi = (c\,\alpha_z\,p + \beta\,mc^2)\psi$. Its third row is $E\psi_3 = pc\,\psi_1 - mc^2\psi_3$, with the $-mc^2$ from $\beta$ on the lower pair. Move that term across:

$$(E + mc^2)\,\psi_3 = pc\,\psi_1.$$

The solution is therefore (box)

$$\psi = \begin{pmatrix} 1 \\ 0 \\ r \\ 0 \end{pmatrix} e^{i(pz - Et)/\hbar}, \qquad r = \frac{pc}{E + mc^2}.$$

At rest, $p = 0$ and $r = 0$, which is the solution at rest. In motion the third entry fills in.

**How much.** Chapter 4's box gave $p = \gamma mv$ and $E = \gamma mc^2$. Put them in, and the mass cancels: $r = \gamma\,(v/c)/(\gamma + 1)$. So $r$ depends only on the speed:

| Speed | $r$, the size of the lower entry | Share of the chance in the lower pair |
| --- | --- | --- |
| $0.01\,c$ | 0.005 | 0.0025% |
| $0.1\,c$ | 0.05 | 0.25% |
| $0.5\,c$ | 0.27 | 6.7% |
| $0.9\,c$ | 0.63 | 28% |
| $0.99\,c$ | 0.87 | 43% |

The share is $r^2/(1 + r^2)$, because chapter 5 made the chance the sum of the entries' squared lengths. For a slow electron $r$ is about half its speed divided by $c$, so the lower pair is tiny. That's why Schrödinger's single wave function, with spin added as two amplitudes, works so well for slow electrons. Near the speed of light the two pairs are almost equal.

So "the upper pair has positive energy" is true only at rest. A moving positive-energy electron can have all four entries filled, with the upper pair the larger. For a negative-energy solution it's the other way round: the lower pair is the larger and the upper pair fills in, to the same size $r$.

**Names for the solutions.** For each momentum there are four solutions, as at rest. Physicists write the two positive-energy columns as $u_1(p)$ and $u_2(p)$, and the two negative-energy columns as $v_1(p)$ and $v_2(p)$. The number says which entry of the larger pair is filled: 1 for its spin-up entry and 2 for its spin-down entry. The example above is $u_1$. Chapter 5's last section used the same two letters for the upper and lower pairs. From here on they mean whole solutions.

**Spin in motion.** In the example the motion is along $z$. The matrix $\alpha_z$ is built from $\hat Z$, which keeps up as up, so only the spin-up entries are filled and the spin along $z$ is exactly up. Chapter 6a's section 3 agrees: its leftover, $\alpha_x\hat p_y - \alpha_y\hat p_x$, is zero when the momentum has no $x$ or $y$ part. Spin along the direction of motion is the one case where the spin is kept.

If the electron moves sideways instead, along $x$, the momentum term has $\alpha_x$, which is built from $\hat S$, and $\hat S$ swaps up and down. The solution $u_1$ is then $(1, 0, 0, r)$, with a spin-up entry and a spin-down entry. A measurement of its spin along the vertical can give either result. That is [chapter 6a's section 3](dirac-equation.md#_3-angular-momentum-that-isn-t-kept) again: for sideways motion the spin doesn't commute with $\hat H$, so a state with a definite energy needn't have a definite spin.

<details>
<summary>The calculation: solving for a moving particle</summary>

This box sets $c = 1$, as later chapters do. The main text's ratio $r = pc/(E + mc^2)$ is then $p/(E + m)$. Chapter 5's last section wrote the two pairs as $u$ and $v$. Here they are $\phi$ and $\chi$, because $u$ and $v$ are the usual names for the whole solutions. The columns $\xi_\uparrow = (1, 0)$ and $\xi_\downarrow = (0, 1)$ are spin up and spin down for one pair. The three spin matrices together are written $\boldsymbol\sigma$, and $E_p = \sqrt{\mathbf p^2 + m^2}$ is the positive energy.

**Moving ($\mathbf p\ne0$).** Substituting a plane wave $\psi=w(p)e^{-ip\cdot x/\hbar}$ turns the differential equation into

$$(E - \boldsymbol\alpha\cdot\mathbf p - \beta m)\,w = 0,$$

Write $w=(\phi,\chi)$ for the upper and lower pairs. Then

$$(E - m)\,\phi = \boldsymbol\sigma\cdot\mathbf p\,\chi, \qquad (E + m)\,\chi = \boldsymbol\sigma\cdot\mathbf p\,\phi.$$

For $E=E_p=\sqrt{\mathbf p^2+m^2}$, the second equation gives $\chi=\frac{\boldsymbol\sigma\cdot\mathbf p}{E_p+m}\phi$. Choose either spin state for the upper pair, $\xi_\uparrow$ or $\xi_\downarrow$. With standard normalization, the two positive-energy spinors are

$$u_s(p) = \begin{pmatrix} \sqrt{E_p + m}\;\xi_s \\ \dfrac{\boldsymbol\sigma\cdot\mathbf p}{\sqrt{E_p + m}}\;\xi_s \end{pmatrix} \qquad (E = +E_p),$$

At $\mathbf p=0$, these reduce to the positive-energy rest states up to normalization. For $E=-E_p$, the first equation instead gives $\phi=-\frac{\boldsymbol\sigma\cdot\mathbf p}{E_p+m}\chi$. At this same spatial momentum, the negative-energy spinors are

$$v_s(p) = \begin{pmatrix} -\dfrac{\boldsymbol\sigma\cdot\mathbf p}{\sqrt{E_p + m}}\;\xi_s \\ \sqrt{E_p + m}\;\xi_s \end{pmatrix} \qquad (E = -E_p),$$

Their lower blocks dominate at low momentum, as in [Relativistic QM §11](relativistic-qm.md#_11-the-notation-later-chapters-use).

**The main text's example.** For $\mathbf p$ along $z$, $\boldsymbol\sigma\cdot\mathbf p = p\hat Z$. With spin up, $\xi_\uparrow = (1, 0)$, the lower pair is $p/(E_p + m)$ times $(1, 0)$. Dividing the whole column by $\sqrt{E_p + m}$ gives $(1, 0, r, 0)$. For $\mathbf p$ along $x$, $\boldsymbol\sigma\cdot\mathbf p = p\hat S$, which swaps the two amplitudes, and the column is $(1, 0, 0, r)$.

</details>

**A moving electron's solution fills all four entries. The lower pair grows with speed, from almost nothing for a slow electron to nearly half the chance near the speed of light.**

## 2. Electron and positron

That leaves the negative-energy solutions. Chapter 5 ended by saying that they describe antiparticles. The equation itself shows part of this: each negative-energy solution can be turned into a positive-energy solution for a particle of the opposite charge, with the same chances at every point.

**Step one: take the complex conjugate.** The [complex conjugate](appendix-math-complex.md#_1-complex-numbers) of a number, marked with a star, has $-i$ wherever the number has $i$. It keeps the number's length, so it changes no chance. Take a negative-energy wave, with momentum $p$ and energy $-E$, where $E$ is positive. Conjugating it gives

$$\left(e^{i(px + Et)/\hbar}\right)^* = e^{i\left((-p)x - Et\right)/\hbar},$$

a wave with momentum $-p$ and energy $+E$. Conjugating has reversed both.

**Step two: reshuffle the column.** If $\psi$ obeys the Dirac equation, conjugate the whole equation to see what $\psi^*$ obeys. The rate of change in time comes with an $i$, and so does each slope, so those terms change sign. The mass term, $\beta\,mc^2$, has no $i$ and stays as it was. So the mass term now has the wrong sign compared with the others. One of the matrices, $\hat Y$, also has an $i$ of its own. A fixed matrix repairs both (box), and it does two things:

- It swaps the upper pair with the lower pair. The matrix $\beta$ is $+1$ on the upper pair and $-1$ on the lower, so the swap changes the sign of the mass term.
- Inside each pair it swaps spin up with spin down, with a change of sign, and the two pairs get opposite signs. Together these leave $\alpha_x$ and $\alpha_z$ as they were and change the sign of $\alpha_y$, which cancels the sign $\alpha_y$ picked up from the $i$ in $\hat Y$.

The fixed matrix only moves entries about and changes signs, so like the conjugate it changes no chance.

Call the result $\psi_c$:

$$\psi_c = (\text{a fixed matrix}) \times \psi^*.$$

**The charge flips.** [Chapter 6a's section 5](dirac-equation.md#_5-the-strength-of-the-magnet) put the field in by replacing $\hat p_x$ with $\hat p_x - qA_x$, which is $-i\hbar\,\partial/\partial x - qA_x$. The arrows of $\mathbf A$ are ordinary real numbers, so conjugation turns the $-i$ into $+i$ and leaves $qA_x$ alone:

$$-i\hbar\,\frac{\partial}{\partial x} - qA_x \quad\longrightarrow\quad +i\hbar\,\frac{\partial}{\partial x} - qA_x = -\left(-i\hbar\,\frac{\partial}{\partial x} + qA_x\right).$$

Follow the three terms of the equation through both steps.

| Term | After conjugating | After the fixed matrix |
| --- | --- | --- |
| Rate of change in time, $i\hbar\,\partial/\partial t$ | Sign flipped | Still flipped |
| Momentum with the field, $-i\hbar\,\partial/\partial x - qA_x$ | Sign flipped, and $-qA_x$ has become $+qA_x$ | The same |
| Mass, $\beta\,mc^2$ | Unchanged | Sign flipped |

After both steps every term carries the same minus sign. Multiply the whole equation by $-1$ and the signs are gone. What remains is the Dirac equation with $+qA_x$ where $-qA_x$ stood. So $\psi_c$ obeys the Dirac equation for a particle of charge $-q$.

**The pairs.** Put the conjugation, the reshuffle and the change of charge together. A negative-energy solution of the electron's equation becomes a positive-energy solution of the equation for a particle of charge $+e$:

| | A negative-energy solution for the electron | The solution it becomes |
| --- | --- | --- |
| Energy | $-E$ | $+E$ |
| Momentum | $p$ | $-p$ |
| Spin | up | down |
| Charge in the equation | $-e$ | $+e$ |
| Mass | $m$ | $m$ |

The new solution is for a particle with the electron's mass, positive energy and a positive charge. That's the **positron** of chapter 5. Every item except the mass is reversed. Chapter 5's hole had the opposite charge and a positive energy, and the same reasoning covers the rest: a hole is a missing electron, so it has minus that electron's energy, momentum, spin and charge.

So the four entries of the Dirac column describe two particles, each with two spins: the electron and the positron. That's the table at the top of this chapter.

**What this doesn't do.** This is still one equation for one particle. It can relabel a negative-energy solution, but it can't make an electron and a positron appear out of a packet of light, as chapter 5 said happens. For that, the wave function has to become a field.

<details>
<summary>The calculation: checking the conjugate solution</summary>

The main text starts from a negative-energy solution. This box runs the same map the other way, from a positive-energy solution to a negative-energy one. Applying the map twice gives back the start, so the two directions say the same thing.

This box sets $c = 1$ and uses the short form of the equation from [chapter 5's last section](relativistic-qm.md#_11-the-notation-later-chapters-use), with $\gamma^0 = \beta$ and $\gamma^i = \beta\alpha_i$. The spin matrices are written $\sigma_1, \sigma_2, \sigma_3$ for $\hat S, \hat Y, \hat Z$. The fixed matrix is $\eta = i\gamma^2$, and the operation $\psi_c = \eta\,\psi^*$ is called **charge conjugation**.

To see the map in coordinates, use the two-component form. A momentum-space plane wave $w=(\phi,\chi)$ solves the coupled equations

$$(E-m)\,\phi = \boldsymbol\sigma\cdot\mathbf p\,\chi, \qquad (E+m)\,\chi = \boldsymbol\sigma\cdot\mathbf p\,\phi.$$

For a positive-energy solution, $\phi$ is the large upper pair and $\chi$ the small lower pair. Now conjugate both equations. The Pauli matrices obey $\sigma_1^*=\sigma_1$, $\sigma_3^*=\sigma_3$, and $\sigma_2^*=-\sigma_2$, so $\boldsymbol\sigma^*=(\sigma_1,-\sigma_2,\sigma_3)$, and

$$(E-m)\,\phi^* = \boldsymbol\sigma^*\cdot\mathbf p\,\chi^*, \qquad (E+m)\,\chi^* = \boldsymbol\sigma^*\cdot\mathbf p\,\phi^*.$$

The matrix $i\sigma^2=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ satisfies $(i\sigma^2)\,\boldsymbol\sigma^*\,(i\sigma^2)^{-1}=-\boldsymbol\sigma$, the property that will flip the frequency sign. In the standard representation $\eta=i\gamma^2$ has the block form $\eta=\begin{pmatrix}0&i\sigma^2\\-i\sigma^2&0\end{pmatrix}$, so applying it to $w^*$ gives

$$\psi_c=\eta\,w^*=\begin{pmatrix}i\sigma^2\,\chi^*\\-i\sigma^2\,\phi^*\end{pmatrix}\equiv\begin{pmatrix}\phi_c\\\chi_c\end{pmatrix}.$$

Multiply the conjugated equations by $i\sigma^2$. Because $(i\sigma^2)(\boldsymbol\sigma^*\cdot\mathbf p)=-(\boldsymbol\sigma\cdot\mathbf p)(i\sigma^2)$, they become

$$(E+m)\,\phi_c = \boldsymbol\sigma\cdot\mathbf p\,\chi_c, \qquad (E-m)\,\chi_c = \boldsymbol\sigma\cdot\mathbf p\,\phi_c.$$

Multiplying both equations by $-1$ puts them in the original form with energy $-E$ and momentum $-\mathbf p$. Complex conjugation reverses both signs in the plane-wave phase as well. Thus the transformed spinor is proportional to $v_{s'}(-p)$ in the fixed-momentum convention of [section 1](#_1-a-moving-electron), with the spin label interchanged. The reversal of momentum is essential to this identification.

To restore charge, reinsert the replacement from chapter 6a's section 5, $\hat{\mathbf p}\to\hat{\mathbf p}-q\mathbf A$, which in index form is $\partial_\mu\to\partial_\mu+\tfrac{iq}{\hbar}A_\mu$. Conjugation reverses the sign of every $i$, so $\psi_c$ obeys the equation with $q\to-q$: the antiparticle, with opposite charge and the same mass.

In the full theory of electrons and light, charge conjugation also reverses the sign of the potential itself.

</details>

**Conjugating a negative-energy solution and reshuffling its entries gives a positive-energy solution for the opposite charge, with the same mass. The four entries describe the electron and the positron, each with two spins.**

## 3. The general solution

The next chapter starts from one formula, which collects the solutions of sections 1 and 2.

**Adding solutions.** The Dirac equation is linear: if two columns each obey it, so does their sum. Start with two waves. Section 1's electron, with one momentum and spin up, is a solution. Add a second with a different momentum, each multiplied by a number that says how much of it there is, and the sum is still a solution. The general state of a free particle does this for every momentum, both spins and both signs of the energy. From here on we measure speeds as fractions of the speed of light, so that $c = 1$ and drops out of the formulas, as in later chapters:

$$\psi(x) = \sum_{s=1}^{2} \int \frac{d^3p}{(2\pi\hbar)^3}\,\frac{1}{\sqrt{2E_p}}\left[a_s(p)\,u_s(p)\,e^{-ip\cdot x/\hbar} + b_s^*(p)\,v_s(p)\,e^{+ip\cdot x/\hbar}\right].$$

The $x$ in $\psi(x)$ now stands for the time and the position together. Here is what each piece is:

| Piece | What it is |
| --- | --- |
| $\int d^3p$ | The sum over all momenta $\mathbf p$, with its three parts $p_x$, $p_y$, $p_z$ |
| $\sum_s$ | The sum over the two spins |
| $E_p$ | The positive energy $\sqrt{\mathbf p^2 + m^2}$ |
| $\mathbf p\cdot\mathbf x$ | Short for $p_xx + p_yy + p_zz$ |
| $p\cdot x$ | Short for $E_pt - \mathbf p\cdot\mathbf x$, which is chapter 4's summing rule $A^\mu B_\mu$ applied to $p$ and $x$ |
| $u_s(p)$ | Section 1's positive-energy column, multiplied by $\sqrt{E_p + m}$ by convention |
| $v_s(p)$ | Section 1's negative-energy column for momentum $-\mathbf p$, with the same factor (first box) |
| $u_s(p)\,e^{-ip\cdot x/\hbar}$ | Section 1's positive-energy solution |
| $v_s(p)\,e^{+ip\cdot x/\hbar}$ | A negative-energy solution, with its phase turning the other way |
| $a_s(p)$ and $b_s^*(p)$ | Numbers that say how much of each wave the state contains |

The factor $1/\sqrt{2E_p}$ and the $(2\pi\hbar)^3$ are conventions that shorten later formulas. For example, if only $a_1(p)$ is different from zero, and only for one momentum, the state is section 1's moving electron.

**The second term.** Its wave is $e^{+ip\cdot x/\hbar}$, with both signs reversed. Read on its own, it has energy $-E_p$ and momentum $-\mathbf p$. By section 2, a negative-energy wave with momentum $-\mathbf p$ becomes a positron with energy $+E_p$ and momentum $+\mathbf p$. So the $\mathbf p$ in $v_s(p)$ names the positron's momentum. The sum runs over every momentum, so naming the waves this way leaves none out. The $s$ doesn't get the same treatment. It still names which entry of the larger pair is filled, 1 for the spin-up entry and 2 for the spin-down entry, so the positron's spin is the opposite of the one $s$ names. $v_1$ goes with a spin-down positron.

**Why a star on the $b$.** The coefficients $a_s(p)$ and $b_s^*(p)$ are ordinary numbers here, fixed by how the state starts out, and for now $b_s^*$ is only a name for one of them. The next chapter turns them into operators, as chapter 3 turned the spring's position and momentum into operators that step up and down the rungs. There $a_s(p)$ removes an electron, and $b_s^*(p)$ becomes $\hat b_s^\dagger(p)$, which creates a positron, as chapter 5's section 10 promised for the negative-energy waves. We write the star now so that the formula keeps its shape then.

<details>
<summary>The calculation: the columns in the sum, and the sign of the momentum</summary>

For the negative-frequency phase written here, the spatial wave is $e^{-i\mathbf p\cdot\mathbf x/\hbar}$. Its classical momentum is therefore $-\mathbf p$. Replace $\mathbf p$ by $-\mathbf p$ in the negative-energy spinor of [section 1](#_1-a-moving-electron). With $\xi_\uparrow=(1,0)$ and $\xi_\downarrow=(0,1)$, the spinors in this expansion are

$$u_s(p) = \begin{pmatrix} \sqrt{E_p + m}\;\xi_s \\ \dfrac{\boldsymbol\sigma\cdot\mathbf p}{\sqrt{E_p + m}}\;\xi_s \end{pmatrix}, \qquad v_s(p) = \begin{pmatrix} \dfrac{\boldsymbol\sigma\cdot\mathbf p}{\sqrt{E_p + m}}\;\xi_s \\ \sqrt{E_p + m}\;\xi_s \end{pmatrix},$$

The relabeling changes the sign of the upper block of $v$. The low-momentum structure remains the one found in [Relativistic QM §11](relativistic-qm.md#_11-the-notation-later-chapters-use): $u$ has a large upper block, while $v$ has a large lower block.

</details>

<details>
<summary>Preview: positive energies once the coefficients are operators</summary>

This preview uses the next chapter's terms. Skip it now and come back after that chapter.

**Quantize the amplitudes.** The [QFT page](qft.md) replaces the coefficients of [section 3](#_3-the-general-solution) by operators. Before reordering, one mode contributes $E_p(\hat a^\dagger\hat a-\hat b\hat b^\dagger)$ to the Hamiltonian.

Fermion operators obey $\hat b\hat b^\dagger=1-\hat b^\dagger\hat b$. Substitution gives $E_p(\hat a^\dagger\hat a+\hat b^\dagger\hat b)$ plus a vacuum constant. After subtracting that constant, electrons and positrons both contribute positive energy $E_p$.

Thus $\hat b^\dagger$ multiplies a negative-frequency solution but creates a positive-energy positron. This implements the reinterpretation in [Relativistic QM §10](relativistic-qm.md#_10-why-a-one-particle-equation-isn-t-enough).

</details>

**The general free solution is a sum over momenta and spins of the $u$ waves and the $v$ waves. Its coefficients become the operators of the next chapter.**

## 4. The notation later chapters use

Later chapters use the standard names for the things chapters 6a and 6b built, and they need the exact rule for how a spinor changes between observers. You don't need either to follow this chapter, so both are collected here.

| Chapters 6a and 6b | Later chapters |
| --- | --- |
| The spin matrices $\hat S$, $\hat Y$, $\hat Z$ | The **Pauli matrices** $\sigma_1, \sigma_2, \sigma_3$, together $\boldsymbol\sigma$ |
| Two copies of them, $\Sigma_x, \Sigma_y, \Sigma_z$ | $\boldsymbol\Sigma$ |
| The spin, $\tfrac{\hbar}{2}\boldsymbol\Sigma$ | $\mathbf S$ (not chapter 2b's sideways matrix $\hat S$) |
| The angular momentum of the motion, and the total | $\mathbf L = \mathbf r\times\mathbf p$ and $\mathbf J = \mathbf L + \mathbf S$ |
| The magnet strength, twice a spinning charge's | The **magnetic moment** $\boldsymbol\mu$, with gyromagnetic factor $g = 2$ |
| The column of four wave functions | A **spinor**, or Dirac spinor |
| Conjugate and reshuffle | **Charge conjugation**, $\psi_c = \eta\,\psi^*$ |
| "Kept" | **Conserved** |

<details>
<summary>Reference: the rule for operators, called the Heisenberg equation</summary>

Later chapters use this box. Nothing in this chapter depends on it.

[Chapter 6a's section 3](dirac-equation.md#_3-angular-momentum-that-isn-t-kept) used chapter 2b's rule for how an average changes in time. Later chapters use the same rule for the operator itself, written $d\hat A/dt = \tfrac{i}{\hbar}[\hat H, \hat A]$. Swapping the order in the commutator changes its sign, and $1/i = -i$, so this is the same rule.

Take an energy operator $\hat H$ that doesn't change in time. A state changes in time by the factor $e^{-i\hat Ht/\hbar}$, as in chapter 2b. Move that factor and its conjugate from the state onto the operator:

$$\hat A_H(t) = e^{i\hat Ht/\hbar}\,\hat A\,e^{-i\hat Ht/\hbar}.$$

At $t=0$, $\hat A_H(0)=\hat A$. Take the rate of change of each factor, using $\frac{d}{dt}e^{\pm i\hat Ht/\hbar}=\pm\frac{i}{\hbar}\hat He^{\pm i\hat Ht/\hbar}$:

$$\frac{d\hat A_H}{dt} = \frac{i}{\hbar}\left(\hat H e^{i\hat Ht/\hbar}\hat A e^{-i\hat Ht/\hbar} - e^{i\hat Ht/\hbar}\hat A e^{-i\hat Ht/\hbar} \hat H\right) = \frac{i}{\hbar}[\hat H, \hat A_H].$$

Taking the average of both sides gives chapter 2b's rule. A zero commutator means the quantity is kept in every state. An average can also stay constant in one particular state while the commutator isn't zero.

</details>

The spin obeys $[S_i, S_j] = i\hbar\,\varepsilon_{ijk}S_k$, the **angular-momentum commutation relations**. For example $[S_x, S_y] = i\hbar S_z$. The symbol $\varepsilon_{ijk}$ is $+1$ for the order $(1, 2, 3)$, changes sign when two indices swap, and is zero when two are equal.

<details>
<summary>The notation: how a spinor changes between observers</summary>

This box and the two after it set $c = 1$ and use the short form of the equation, $(i\hbar\gamma^\mu\partial_\mu - m)\psi = 0$, from [chapter 5's last section](relativistic-qm.md#_11-the-notation-later-chapters-use).

Chapter 6a's section 6 turned a spinor about one axis. Chapter 4's observers can also move past each other. When the coordinates change by a Lorentz transformation $x' = \Lambda x$, which may be a turn, a change of speed (a **boost**) or both, the four components change through a matrix $S(\Lambda)$:

$$\psi'(x') = S(\Lambda)\,\psi(x), \qquad S(\Lambda) = \exp\!\left(-\frac{i}{4}\,\omega_{\mu\nu}\sigma^{\mu\nu}\right), \qquad \sigma^{\mu\nu} = \frac{i}{2}\,[\gamma^\mu, \gamma^\nu].$$

The real antisymmetric numbers $\omega_{\mu\nu}$ say which turn and which boost. The matrices $\sigma^{\mu\nu}$ act on the components. Three properties set this rule apart:

1. **It acts on the components at each point.** $S$ is a four-by-four matrix. It is separate from the change of the function over space.
2. **It is double-valued.** A turn of $2\pi$ gives $S = -\mathbb 1$, and a turn of $4\pi$ gives back the spinor exactly. This is the sign of [chapter 6a's section 6](dirac-equation.md#_6-one-full-turn-flips-the-sign). The last box of this section turns the spin the other way round from that section, so its two phases are swapped; which way is a matter of which way the field points.
3. **It splits in two.** A change of basis for the components separates the rule into two rules for two components each. The corresponding **Weyl spinors** are the left- and right-handed parts. They change in the same way under turns and in opposite ways under boosts. [Symmetries](symmetries.md) gives the reason there are two kinds.

For a turn, $S = \exp(-\tfrac i2\boldsymbol\theta\cdot\boldsymbol\Sigma)$, which contains the spin $\mathbf S/\hbar$ of [chapter 6a's section 3](dirac-equation.md#_3-angular-momentum-that-isn-t-kept). The splitting into left and right parts is stated here without proof. [Weak Interaction](weak-interaction.md) introduces the projectors that separate them, where the difference starts to matter.

</details>

<details>
<summary>Deriving the covariant spinor transformation</summary>

This optional derivation checks that the spinor transformation preserves the Dirac equation. Later chapters use the result without requiring these calculations.

**Impose covariance.** If $\psi$ solves $(i\hbar\gamma^\mu\partial_\mu-m)\psi=0$, require $\psi'(x')=S(\Lambda)\psi(x)$ to solve the primed equation. The derivative transforms as $\partial'_\mu=(\Lambda^{-1})^\nu{}_\mu\partial_\nu$. Substitute and multiply on the left by $S^{-1}$:

$$(i\hbar\,S^{-1}\gamma^\mu S\,(\Lambda^{-1})^\nu{}_\mu\,\partial_\nu - m)\,\psi = 0,$$

To recover the original equation, require

$$S^{-1}\gamma^\mu S = \Lambda^\mu{}_\nu\,\gamma^\nu.$$

First consider a small transformation, $\Lambda^\mu{}_\nu=\delta^\mu_\nu+\omega^\mu{}_\nu$, with $\omega_{\mu\nu}=-\omega_{\nu\mu}$. Write $S=1+\Omega$ and keep first-order terms. Since $S^{-1}\gamma^\mu S=\gamma^\mu-[\Omega,\gamma^\mu]$, covariance becomes

$$-[\Omega, \gamma^\mu] = \omega^\mu{}_\nu\,\gamma^\nu.$$

Test $\Omega=-\tfrac i4\omega_{\rho\sigma}\sigma^{\rho\sigma}$. Use the matrix identity $[AB,C]=A\{B,C\}-\{A,C\}B$ and the gamma-matrix anticommutator $\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}$:

$$[\gamma^\rho\gamma^\sigma, \gamma^\mu] = \gamma^\rho\,\{\gamma^\sigma, \gamma^\mu\} - \{\gamma^\rho, \gamma^\mu\}\,\gamma^\sigma = 2\,(g^{\mu\sigma}\gamma^\rho - g^{\mu\rho}\gamma^\sigma).$$

The definition $\sigma^{\rho\sigma}=\tfrac i2[\gamma^\rho,\gamma^\sigma]$ contains both orderings. Subtract them to obtain

$$[\sigma^{\rho\sigma}, \gamma^\mu] = \frac{i}{2}\,\big([\gamma^\rho\gamma^\sigma, \gamma^\mu] - [\gamma^\sigma\gamma^\rho, \gamma^\mu]\big) = 2i\,(g^{\mu\sigma}\gamma^\rho - g^{\mu\rho}\gamma^\sigma).$$

Insert this into the covariance condition:

$$-[\Omega, \gamma^\mu] = \frac{i}{4}\,\omega_{\rho\sigma}\cdot 2i\,(g^{\mu\sigma}\gamma^\rho - g^{\mu\rho}\gamma^\sigma) = -\frac{1}{2}\,\omega_{\rho\sigma}\,(g^{\mu\sigma}\gamma^\rho - g^{\mu\rho}\gamma^\sigma) = \omega^\mu{}_\nu\,\gamma^\nu,$$

In the last step, use $g^{\mu\sigma}\omega_{\rho\sigma}=-\omega^\mu{}_\rho$. The two contributions add, giving the required sign.

This verifies the infinitesimal transformation. Repeating a transformation along a fixed generator gives its finite exponential. Different generators generally do not commute, so composing arbitrary rotations and boosts requires matrix multiplication rather than adding their parameters.

</details>

<details>
<summary>Working out rotations and boosts explicitly</summary>

The following calculations apply the formula to a rotation and a boost. These transformations generate the Lorentz transformations connected to the identity.

**Matrix exponentials.** Write $S=e^\Omega$, where $\Omega=-\tfrac i4\sum_{\mu,\nu}\omega_{\mu\nu}\sigma^{\mu\nu}$. Define the exponential by $e^M=1+M+M^2/2!+\cdots$, with $1$ the identity matrix.

We will use two properties. Taking an adjoint gives $(e^M)^\dagger=e^{M^\dagger}$ because $(M^n)^\dagger=(M^\dagger)^n$. Also, $e^Me^{-M}=1$, so $e^{-M}$ is the inverse.

**Parameters and generators.** The $\omega_{\mu\nu}$ are numbers specifying the transformation. Near the identity, $\Lambda=1+\omega$. Lower the first index using $\omega_{\mu\nu}=g_{\mu\rho}\omega^\rho{}_\nu$, with metric $g=\mathrm{diag}(1,-1,-1,-1)$.

Expanding the Lorentz condition $\Lambda^Tg\Lambda=g$ to first order gives $\omega_{\mu\nu}=-\omega_{\nu\mu}$. There are six independent parameters. The pairs $(0,1),(0,2),(0,3)$ mix time and space and describe boosts. The spatial pairs $(1,2),(1,3),(2,3)$ describe rotations.

The $\sigma^{\mu\nu}=\tfrac i2[\gamma^\mu,\gamma^\nu]$ are fixed $4\times4$ matrices, called **generators** because they determine the infinitesimal change of the spinor. Multiplying them by the parameters and exponentiating gives a finite transformation.

They are also antisymmetric in their indices, so only six are independent. Their values do not depend on which transformation we choose.

In the double sum, reversing $(\mu,\nu)$ changes both signs, so each pair contributes twice. The diagonal terms vanish. Therefore

$$\Omega = -\frac{i}{4}\sum_{\mu,\nu}\omega_{\mu\nu}\sigma^{\mu\nu} = -\frac{i}{2}\sum_{\mu<\nu}\omega_{\mu\nu}\,\sigma^{\mu\nu}.$$

For each example, find the nonzero parameters, compute their generators, and exponentiate the resulting matrix.

**Rotation.** A spatial rotation leaves time unchanged, so $\omega_{0i}=0$. Only the three spatial pairs remain:

$$\Omega_{\text{rot}} = -\frac{i}{2}\left(\omega_{12}\,\sigma^{12} + \omega_{13}\,\sigma^{13} + \omega_{23}\,\sigma^{23}\right).$$

We need the generators $\sigma^{ij}=\tfrac i2(\gamma^i\gamma^j-\gamma^j\gamma^i)$. Compute the gamma-matrix products first.

Use the standard representation from [Relativistic QM §11](relativistic-qm.md#_11-the-notation-later-chapters-use): $\gamma^0=\beta$ and $\gamma^i=\beta\alpha_i$. The matrices from [chapter 6a's section 2](dirac-equation.md#_2-four-wave-functions-and-one-question) have the following block form, with each entry a $2\times2$ block and $\sigma_i$ the [Pauli matrices](#_4-the-notation-later-chapters-use):

$$\beta = \begin{pmatrix}1 & 0 \\ 0 & -1\end{pmatrix}, \qquad \alpha_i = \begin{pmatrix}0 & \sigma_i \\ \sigma_i & 0\end{pmatrix}.$$

Multiply the blocks in row-by-column order, keeping their order within each product:

$$\gamma^i = \beta\alpha_i = \begin{pmatrix}1\cdot 0 + 0\cdot\sigma_i & 1\cdot\sigma_i + 0\cdot 0 \\ 0\cdot 0 + (-1)\cdot\sigma_i & 0\cdot\sigma_i + (-1)\cdot 0\end{pmatrix} = \begin{pmatrix}0 & \sigma_i \\ -\sigma_i & 0\end{pmatrix}.$$

For $i\ne j$, multiply two spatial gamma matrices. The off-diagonal blocks vanish:

$$\gamma^i\gamma^j = \begin{pmatrix}0\cdot 0 + \sigma_i\cdot(-\sigma_j) & 0\cdot\sigma_j + \sigma_i\cdot 0 \\ (-\sigma_i)\cdot 0 + 0\cdot(-\sigma_j) & (-\sigma_i)\cdot\sigma_j + 0\cdot 0\end{pmatrix} = \begin{pmatrix}-\sigma_i\sigma_j & 0 \\ 0 & -\sigma_i\sigma_j\end{pmatrix}.$$

Subtract the reverse product. Each diagonal block becomes the negative Pauli commutator:

$$[\gamma^i,\gamma^j] = \begin{pmatrix}-[\sigma_i,\sigma_j] & 0 \\ 0 & -[\sigma_i,\sigma_j]\end{pmatrix}.$$

The box in chapter 6a's section 3 worked out two cases of the general rule $[\sigma_i,\sigma_j]=2i\varepsilon_{ijk}\sigma_k$. The symbol $\varepsilon_{ijk}$ is $+1$ for $(1,2,3)$, changes sign under an index exchange, and vanishes when indices repeat. Grouping the repeated blocks into [the spin matrix](dirac-equation.md#_3-angular-momentum-that-isn-t-kept) $\Sigma^k=\mathrm{diag}(\sigma_k,\sigma_k)$ gives

$$[\gamma^i,\gamma^j] = -2i\,\varepsilon_{ijk}\,\Sigma^k.$$

Multiply by $i/2$ to obtain the generator. Since $(i/2)(-2i)=1$,

$$\sigma^{ij} = \frac{i}{2}\,[\gamma^i,\gamma^j] = \varepsilon_{ijk}\,\Sigma^k.$$

Thus $\sigma^{12}=\Sigma^3$, $\sigma^{13}=-\Sigma^2$, and $\sigma^{23}=\Sigma^1$. Each generator corresponds to rotation about the axis perpendicular to its coordinate plane. All three are Hermitian because the Pauli matrices are Hermitian.

Substitute these generators into the exponent:

$$\Omega_{\text{rot}} = -\frac{i}{2}\left(\omega_{12}\,\Sigma^3 - \omega_{13}\,\Sigma^2 + \omega_{23}\,\Sigma^1\right).$$

The parameters are real, so the matrix in parentheses is Hermitian. Multiplication by $-i$ makes $\Omega_{\rm rot}$ **anti-Hermitian**, meaning $\Omega_{\rm rot}^\dagger=-\Omega_{\rm rot}$.

Consequently $S^\dagger=e^{-\Omega_{\rm rot}}=S^{-1}$. The rotation matrix is **unitary**.

Collect the angles into $\boldsymbol\theta=(\omega_{23},-\omega_{13},\omega_{12})$. Each entry specifies rotation about the corresponding axis. The exponent becomes a dot product:

$$S = \exp\!\left(-\frac{i}{2}\,\boldsymbol\theta\cdot\boldsymbol\Sigma\right),$$

This is the rotation formula used above.

For a rotation about $z$, set $\omega_{12}=\theta$ and the other angles to zero. Since $\Sigma^3=\mathrm{diag}(1,-1,1,-1)$, exponentiate each diagonal entry:

$$S = \mathrm{diag}\!\left(e^{-i\theta/2},\, e^{i\theta/2},\, e^{-i\theta/2},\, e^{i\theta/2}\right).$$

Spin up and spin down acquire opposite phases. At $\theta=2\pi$, every entry is $-1$, so the spinor changes sign. At $4\pi$ it returns exactly, confirming the property described in [chapter 6a's section 6](dirac-equation.md#_6-one-full-turn-flips-the-sign).

**Boost along $x$.** A boost mixes time with one spatial coordinate. For motion along $x$, only the pair $(0,1)$ contributes. We first express its parameter in terms of the frame's velocity.

The coordinate transformation from [Special Relativity](special-relativity.md) is $t'=\gamma(t-vx)$ and $x'=\gamma(x-vt)$, using $c=1$. Define **rapidity** $\varphi$ by $v=\tanh\varphi$. Then $\gamma=\cosh\varphi$ and $\gamma v=\sinh\varphi$, giving

$$t' = t\cosh\varphi - x\sinh\varphi, \qquad x' = x\cosh\varphi - t\sinh\varphi.$$

For small $\varphi$, these become $t'\approx t-\varphi x$ and $x'\approx x-\varphi t$. Read the off-diagonal entries of $\Lambda=1+\omega$ from those coefficients:

$$\omega^0{}_1 = -\varphi, \qquad \omega^1{}_0 = -\varphi.$$

Lowering the first index uses $g_{00}=1$, so

$$\omega_{01} = g_{00}\,\omega^0{}_1 = -\varphi.$$

Only one pair remains in the reduced exponent:

$$\Omega_{\text{boost}} = -\frac{i}{2}\,\omega_{01}\,\sigma^{01}.$$

Compute $\sigma^{01}=\tfrac i2[\gamma^0,\gamma^1]$. Use $\gamma^0=\beta$ and the block form of $\gamma^1$ found above:

$$\gamma^0\gamma^1 = \begin{pmatrix}1\cdot 0 + 0\cdot(-\sigma_1) & 1\cdot\sigma_1 + 0\cdot 0 \\ 0\cdot 0 + (-1)\cdot(-\sigma_1) & 0\cdot\sigma_1 + (-1)\cdot 0\end{pmatrix} = \begin{pmatrix}0 & \sigma_1 \\ \sigma_1 & 0\end{pmatrix}.$$

This is $\alpha_1$ from [chapter 6a's section 2](dirac-equation.md#_2-four-wave-functions-and-one-question), also written $\alpha^1$ here. Reversing the multiplication gives

$$\gamma^1\gamma^0 = \begin{pmatrix}0\cdot 1 + \sigma_1\cdot 0 & 0\cdot 0 + \sigma_1\cdot(-1) \\ (-\sigma_1)\cdot 1 + 0\cdot 0 & (-\sigma_1)\cdot 0 + 0\cdot(-1)\end{pmatrix} = \begin{pmatrix}0 & -\sigma_1 \\ -\sigma_1 & 0\end{pmatrix} = -\alpha^1,$$

The two gamma matrices anticommute, so

$$[\gamma^0,\gamma^1] = \gamma^0\gamma^1 - \gamma^1\gamma^0 = \alpha^1 - (-\alpha^1) = 2\alpha^1,$$

Substituting into the generator definition gives

$$\sigma^{01} = \frac{i}{2}\,[\gamma^0,\gamma^1] = i\,\alpha^1.$$

The matrix $\alpha^1$ is Hermitian. The factor $i$ therefore makes $\sigma^{01}$ anti-Hermitian:

$$(\sigma^{01})^\dagger = (i\alpha^1)^\dagger = -i\alpha^1 = -\sigma^{01}.$$

This differs from the Hermitian rotation generators.

Now insert the parameter and generator into the exponent:

$$\Omega_{\text{boost}} = -\frac{i}{2}\,\omega_{01}\,\sigma^{01} = -\frac{i}{2}\,(-\varphi)\,(i\alpha^1).$$

The scalar coefficient is $(-i/2)(-\varphi)i=-\varphi/2$. The two factors of $i$ produce a real exponent:

$$S = \exp\!\left(-\frac{\varphi}{2}\,\alpha^1\right).$$

Here the exponent is Hermitian, so $S^\dagger=S$. A nonzero boost is not unitary as a matrix acting on these four components: $S^\dagger S=e^{-\varphi\alpha^1}\ne1$. This does not imply that Lorentz transformations fail to preserve the physical Hilbert-space norm.

To evaluate the exponential, use $(\alpha^1)^2=1$. Even powers contribute the identity and odd powers contribute $\alpha^1$:

$$e^{-\varphi\alpha^1/2} = \underbrace{\Big[1 + \tfrac{(\varphi/2)^2}{2!} + \cdots\Big]}_{\cosh(\varphi/2)} \;-\; \alpha^1\underbrace{\Big[\tfrac{\varphi}{2} + \tfrac{(\varphi/2)^3}{3!} + \cdots\Big]}_{\sinh(\varphi/2)},$$

Thus $S=\cosh(\varphi/2)-\alpha^1\sinh(\varphi/2)$.

At small velocity, $S\approx1-\tfrac\varphi2\alpha^1$. Its off-diagonal blocks mix the upper and lower spinor components with relative size $\varphi/2\approx v/2$. Since $|\mathbf p|\approx m|v|$, this gives the small-component size $|\mathbf p|/(2m)$ obtained in [section 1](#_1-a-moving-electron). It provides an independent check of [those moving solutions](#_1-a-moving-electron).

For a boost along a unit vector $\hat{\mathbf n}$, use $\omega_{0k}=-\varphi\hat n_k$ and $\sigma^{0k}=i\alpha^k$. Then $S=\exp[-\tfrac\varphi2\boldsymbol\alpha\cdot\hat{\mathbf n}]$.

In this representation, pure rotations give unitary component matrices and pure boosts give Hermitian component matrices. Their different factors of $i$ account for the different exponential forms.

</details>

## Where this comes back

- **[Fields and Quanta](./qft.md)**, the next chapter, starts from section 3's general solution and turns its coefficients into operators that create and remove electrons and positrons.
- **[Action and Lagrangians](./qft-action.md)** uses section 4's rule for how a spinor changes between observers to build the electron's Lagrangian.

---

Previous: [The Dirac Equation](./dirac-equation.md)

Next: [Fields and Quanta](./qft.md)
