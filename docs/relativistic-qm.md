# Relativistic QM

## 1. Plane Wave

Start from the non-relativistic Schrödinger equation (Special Relativity §10) and ask what its simplest solutions are: the states of definite energy.

**A state of definite energy.** In quantum mechanics an observable takes a sharp, predictable value only when the system is in an eigenstate of the corresponding operator. The energy observable is the **Hamiltonian** $\hat H$, so a state of definite energy $E$ satisfies

$$\hat H \psi = E \psi .$$

Measurement of the energy on such a state returns $E$ with certainty, and the state is stationary in distribution: under time evolution the wave function changes, but every expectation value — in particular $|\psi|^2$ — does not.

**Solve the Schrödinger equation.** The time-dependent Schrödinger equation is

$$i\hbar \frac{\partial \psi}{\partial t} = \hat H \psi$$

(restoring $\hbar$, still $c = 1$, as in Special Relativity §10). We want its definite-energy solutions.

**Separation of variables.** Assume the wave function factors into spatial and temporal parts, $\psi(x, t) = \phi(x)\,\tau(t)$. Substituting into the Schrödinger equation and dividing by $\psi$,

$$i\hbar \frac{\dot\tau(t)}{\tau(t)} = \frac{\hat H \phi(x)}{\phi(x)} = E,$$

where the two sides depend on $t$ and $x$ separately, so both must equal the same constant — call it $E$. The temporal equation integrates immediately,

$$\tau(t) = e^{-iEt/\hbar},$$

and the spatial equation is the **time-independent Schrödinger equation**

$$\hat H \phi = E \phi .$$

**The spatial part, $\phi = \ldots$.** For a free particle the Hamiltonian is the kinetic operator $\hat H = \hat{\mathbf p}^2/2m$ with $\hat{\mathbf p} = -i\hbar\nabla$, so

$$-\frac{\hbar^2}{2m}\nabla^2 \phi = E \phi,$$

whose solutions (up to normalization) are the plane waves $\phi(\mathbf x) = e^{i\mathbf p\cdot\mathbf x/\hbar}$ with $E = \mathbf p^2/2m$. Assembling the two factors gives the full solution

$$\psi(x, t) = e^{i(\mathbf p\cdot\mathbf x - Et)/\hbar},$$

the **plane wave**: a state of definite momentum $\mathbf p$ and definite energy $E = \mathbf p^2/2m$. Note the price of definiteness: $|\psi|^2 = 1$ everywhere — a state with sharp momentum carries no position information at all, the extreme limit of the Heisenberg uncertainty relation.

The plane wave is the natural eigen-solution of the non-relativistic theory, but its dispersion relation $E = \mathbf p^2/2m$ is precisely the one Special Relativity §10 showed to be incompatible with Lorentz covariance. The next step is to replace the Schrödinger operator with the relativistic wave equation — the Klein–Gordon equation — and see what a definite-energy plane wave looks like there.

## 2. Klein Gordon

The Schrödinger equation failed the Lorentz test (Special Relativity §10) because it quantized the *approximate* energy relation. The Klein–Gordon equation is what you get by quantizing the exact one.

**Take the definition of $E$ in special relativity.** The exact relation between energy and momentum (Special Relativity §8) is

$$E^2 = \mathbf p^2 + m^2$$

($c = 1$): the Lorentz-invariant norm $p^\mu p_\mu = m^2$ of the four-momentum. The non-relativistic relation $E = \mathbf p^2/2m$ of §1 is only its low-velocity limit, valid when $|\mathbf p| \ll m$.

**Promote to operators.** Apply the same quantization prescription used in Special Relativity §8 and in §1 — replace the classical energy and momentum by operators:

$$E \to i\hbar\,\frac{\partial}{\partial t}, \qquad \mathbf p \to -i\hbar\nabla .$$

The difference from §1 is that the exact, Lorentz-invariant relation is quantized — no small-velocity approximation was made.

**Derive the Klein–Gordon equation.** Acting on the wave function,

$$\left(i\hbar\,\frac{\partial}{\partial t}\right)^2 \psi = \left(m^2 - \hbar^2\nabla^2\right)\psi,$$

$$-\hbar^2\,\partial_t^2\psi = m^2\psi - \hbar^2\nabla^2\psi,$$

$$\partial_t^2\psi - \nabla^2\psi + \frac{m^2}{\hbar^2}\psi = 0,$$

or, in covariant notation,

$$\left(\Box + \frac{m^2}{\hbar^2}\right)\psi = 0, \qquad \Box \equiv \partial_\mu\partial^\mu = \partial_t^2 - \nabla^2,$$

the **Klein–Gordon equation**. It is manifestly Lorentz-invariant: $\Box$ is the Lorentz scalar built from derivatives (Special Relativity §10), $m$ is a scalar, and the equation is a scalar equation — a boost cannot change its form. This is the fix §10 promised.

Plane-wave solutions $\psi = e^{i(\mathbf p\cdot\mathbf x - Et)/\hbar}$ reproduce the dispersion relation

$$E^2 = \mathbf p^2 + m^2,$$

so $E = \pm\sqrt{\mathbf p^2 + m^2}$: the equation admits **negative-energy solutions**, and because it is second order in *time* it no longer supports the probability interpretation of §1 — the conserved density is not positive. The equation restored covariance but paid for it in two new problems, taken up in the next section: negative energies, and a probability that can go negative.

## 3. Negative Energy and Probability

The Klein–Gordon equation restored Lorentz covariance at the price of two pathologies, both already visible in its plane-wave solutions $\psi = e^{i(\mathbf p\cdot\mathbf x - Et)/\hbar}$.

**Negative energy.** The dispersion relation admits both signs,

$$E = \pm\sqrt{\mathbf p^2 + m^2},$$

so for every momentum there is a negative-energy solution with $E \leq -m$. Three consequences follow. First, the energy is *unbounded below*: there is no ground state, and any interaction would let the system radiate energy indefinitely, falling through negative levels forever — a theory with no stable matter. Second, this is not what is observed: a real electron always carries $E \geq m$, never the negative branch. Third — and this is the clue — a negative-energy plane wave with momentum $\mathbf p$ is mathematically the same as a positive-energy state with momentum $-\mathbf p$ and *opposite charge* propagating backward in time. That is the **Stückelberg–Feynman interpretation**: negative-frequency solutions are antiparticles moving backward in time, and the emission of a negative-energy particle is the absorption of an antiparticle. The catch is that interpreting them this way requires particle number to change — creation and annihilation — which a single-particle wave function cannot describe. Negative energies are the first sign that one-particle relativistic wave mechanics is incomplete.

**The probability crisis.** The same two-branch structure shows up on the other side of the theory, in the conserved quantity. In §1 the interpretation of $|\psi|^2$ as a probability density rested on a conservation law, and the conservation law rested on the equation being first order in time. Writing the Schrödinger equation as

$$i\hbar\,\partial_t \psi = \left(-\frac{\hbar^2}{2m}\nabla^2 + V\right)\psi,$$

the density's time derivative is $\partial_t|\psi|^2 = \psi^*\partial_t\psi + \psi\,\partial_t\psi^*$. Substituting the equation for $\partial_t\psi$ and its complex conjugate for $\partial_t\psi^*$,

$$\partial_t|\psi|^2 = \frac{1}{i\hbar}\left[\psi^*\left(-\frac{\hbar^2}{2m}\nabla^2 + V\right)\psi - \psi\left(-\frac{\hbar^2}{2m}\nabla^2 + V\right)\psi^*\right].$$

The potential terms cancel — the same operator acts on both sides of the bilinear, so a Hermitian potential cannot change the density — and the remainder is a pure divergence, since $\nabla\cdot(\psi^*\nabla\psi - \psi\nabla\psi^*) = \psi^*\nabla^2\psi - \psi\nabla^2\psi^*$. Hence

$$\partial_t |\psi|^2 = -\nabla\cdot\mathbf j, \qquad \mathbf j = \frac{\hbar}{2mi}\left(\psi^*\nabla\psi - \psi\,\nabla\psi^*\right).$$

Probability obeys a *local* conservation law: it can flow from place to place but never appear or vanish, and $\int |\psi|^2\, d^3x$ is constant and positive — the total probability. All of this worked only because $\partial_t\psi$ is fixed by the equation itself. That is the derivation's whole point: it exhibits the mechanism — first order in time, so the equation owns $\partial_t\psi$, so it owns $\partial_t|\psi|^2$ — which the second-order equation will lack. The Klein–Gordon equation is second order in time: $\psi$ and $\partial_t\psi$ are independent initial data, and $|\psi|^2$ obeys no such conservation law. The quantity that *is* conserved is different. Multiplying the equation by $\psi^*$, subtracting the complex conjugate, and rearranging the derivatives gives the **Klein–Gordon current**,

$$j^\mu = i\left(\psi^*\partial^\mu\psi - \psi\,\partial^\mu\psi^*\right), \qquad \partial_\mu j^\mu = 0,$$

whose time component is

$$\rho = j^0 = i\left(\psi^*\partial_t\psi - \psi\,\partial_t\psi^*\right).$$

For a plane wave, $\partial_t\psi = -iE\psi/\hbar$, and the expression collapses to

$$\rho = \frac{2E}{\hbar}\,|\psi|^2,$$

whose sign is the sign of the *energy* — the very sign that produced the negative-energy solutions above, and for the same structural reason: the density is forced to involve $\partial_t\psi$, and for a plane wave $\partial_t\psi$ *is* proportional to $E$. A negative-energy wave therefore carries negative density: the theory demands negative probabilities, which no observer could interpret. Read instead as a charge density, the sign flip is exactly the opposite charge of the antiparticle — the same Stückelberg–Feynman picture from above.

The contrast, in one table:

| Schrödinger (first order) | Klein–Gordon (second order) |
| --- | --- |
| $\partial_t\psi$ fixed by the equation $\Rightarrow$ $\partial_t\lvert\psi\rvert^2 = -\nabla\cdot\mathbf j$ $\Rightarrow$ $\int\lvert\psi\rvert^2\,d^3x$ conserved — positive, a probability | $\partial_t\psi$ NOT fixed: $\psi$ and $\partial_t\psi$ are independent initial data $\Rightarrow$ no conservation law for $\lvert\psi\rvert^2$ $\Rightarrow$ the conserved density must borrow $\partial_t\psi$ $\Rightarrow$ $\rho = \frac{2E}{\hbar}\lvert\psi\rvert^2$ — the sign of $E$ |

**The end of the single-particle picture.** The two pathologies are the same disease. Negative energies say that states can be created and destroyed; negative densities say that the conserved quantity is a charge, not a count of one particle. Both force the same conclusion: the wave function of §1 is not a probability amplitude for a fixed number of particles, and the probability interpretation must give way to **second quantization** — promoting the field $\psi$ itself to an operator that creates and annihilates particles, with the negative-frequency modes creating antiparticles. That is the modern resolution, and where this page is heading. Historically the first step was Dirac's: factor the Klein–Gordon operator so the equation becomes first order in time with a manifestly positive density, $\rho = \psi^\dagger\psi$ — the Dirac equation — which postpones but does not remove the negative energies, reinterpreted there as holes in a sea: antiparticles.

## 4. Dirac Equation

Dirac's 1928 move was to solve the probability problem by construction: write down an equation that is first order in time, so that §3's machinery runs and the density is positive — while remaining Lorentz-covariant, so that the dispersion relation of §2 is untouched.

**The requirements.** First, the equation must be first order in time: then $\partial_t\psi$ is fixed by the equation, and the density $\psi^\dagger\psi$ obeys a continuity equation with positive total probability, exactly as in the Schrödinger case of §3. Second, it must be Lorentz-covariant — and a first-order-in-time equation can only be covariant if space enters at the same order (otherwise the equation singles out the time direction, the §10 asymmetry argument all over again). Third, plane waves must still satisfy $E^2 = \mathbf p^2 + m^2$, so that iterating the equation reproduces the Klein–Gordon result.

**The guess.** The most general first-order equation with these properties is

$$i\hbar\,\partial_t\psi = \left(-i\hbar\,\boldsymbol\alpha\cdot\nabla + \beta m\right)\psi,$$

with three objects $\boldsymbol\alpha = (\alpha_1, \alpha_2, \alpha_3)$ and $\beta$ to be determined.

**Squaring reproduces the Klein–Gordon equation.** Iterating the operator must reproduce the squared energy relation,

$$(i\hbar\,\partial_t)^2\psi = \left(-i\hbar\,\boldsymbol\alpha\cdot\nabla + \beta m\right)^2\psi = \left(m^2 - \hbar^2\nabla^2\right)\psi.$$

Expanding the square,

$$-\hbar^2\sum_{ij}\alpha_i\alpha_j\,\partial_i\partial_j\,\psi + m^2\beta^2\,\psi - i\hbar m\sum_i\left(\alpha_i\beta + \beta\alpha_i\right)\partial_i\psi = m^2\psi - \hbar^2\nabla^2\psi.$$

For this to hold identically: $\beta^2 = \mathbb{1}$; the cross terms must vanish, $\alpha_i\beta + \beta\alpha_i = 0$; and the diagonal derivative terms must reassemble into $\nabla^2$, which requires $\alpha_i\alpha_j + \alpha_j\alpha_i = 2\delta_{ij}$. No ordinary numbers satisfy anticommutation — the $\alpha$'s and $\beta$ must be **matrices**, and $\psi$ must therefore be a multicomponent object.

**The matrices and the spinor.** Three anticommuting objects already exist — the Pauli matrices — but a fourth that anticommutes with all of them forces the size up to $4 \times 4$. In the standard representation,

$$\alpha_i = \begin{pmatrix} 0 & \sigma_i \\ \sigma_i & 0 \end{pmatrix}, \qquad \beta = \begin{pmatrix} \mathbb{1} & 0 \\ 0 & -\mathbb{1} \end{pmatrix},$$

so $\psi$ is a **four-component spinor**, written as two two-component pairs, $\psi = \begin{pmatrix} u \\ v \end{pmatrix}$. The block form of the equation shows what the pairs do. For a plane wave ($i\hbar\partial_t \to E$),

$$(E - m)\,u = \boldsymbol\sigma\cdot\mathbf p\,v, \qquad (E + m)\,v = \boldsymbol\sigma\cdot\mathbf p\,u,$$

so the pairs are coupled, not independent. For a positive-energy state, $E \approx m$, and the second equation gives

$$v = \frac{\boldsymbol\sigma\cdot\mathbf p}{E + m}\,u \approx \frac{\boldsymbol\sigma\cdot\mathbf p}{2m}\,u,$$

of order $v/c$ compared with $u$: the **small components**. In the non-relativistic limit the lower pair is suppressed, which is why at low velocity the equation effectively acts on the upper pair alone. For a negative-energy state, $E \approx -m$, the denominator is small and the roles reverse — the lower pair becomes the large one. The two pairs are the particle and antiparticle components.

Spin is not added by hand — the matrices in the equation contain the Pauli matrices, so a scalar wave function cannot satisfy the equation at all; the wave function is forced to carry its components in pairs. What those extra components *are* — they are the spin states of a spin-½ particle — cannot be made precise yet: spin has not been introduced at this point in the notes, and its full significance only emerges in the quantized theory. For now the content is structural: the Dirac equation cannot live on a scalar wave function, and the mathematics forces the four-component form used above.

**Probability restored.** Because the equation is first order in time, §3's argument runs unimpeded:

$$\partial_t\left(\psi^\dagger\psi\right) = -\nabla\cdot\left(\psi^\dagger\boldsymbol\alpha\,\psi\right),$$

so $\rho = \psi^\dagger\psi$ is positive and conserved — the probability problem of §3 is gone by construction. Writing $\gamma^0 = \beta$, $\gamma^i = \beta\alpha_i$, the equation takes the covariant form

$$\left(i\hbar\,\gamma^\mu\partial_\mu - m\right)\psi = 0,$$

with conserved current $j^\mu = \bar\psi\gamma^\mu\psi$, $\bar\psi = \psi^\dagger\gamma^0$.

**Negative energies remain.** Iterating the Dirac equation reproduces the Klein–Gordon equation, so plane waves still give $E = \pm\sqrt{\mathbf p^2 + m^2}$: the equation did not remove the negative-energy branch, and in one way it makes the situation *sharper* — both branches now carry positive density, so nothing in the wave function marks a negative-energy state as unphysical. Interpreting the branch is not possible at this point: the pictures on offer (Dirac's filled sea; §3's Feynman–Stückelberg reading) both require particles to be created and destroyed, which single-particle wave mechanics cannot provide. The negative-energy question — like the spin question above — is answered only by second quantization, and is deferred until then.

**The new physics.** The Dirac equation is not a repaired version of an old theory; it is the equation of a new object. Two of its famous results are settled even at this level: the prediction of the electron's magnetic moment, $g = 2$, and the existence of a particle of opposite charge — the positron, discovered in 1932, six years after the equation. The relativistic wave mechanics of §1–§3 is now complete: the single-particle equation with a sane probability interpretation is the Dirac equation, and its unresolved parts — the meaning of the extra components, the meaning of the negative-energy solutions — are precisely the questions that force the next step: second quantization.

## 5. Summary

The page's argument in four moves:

**1. Relativistic energy.** The exact energy–momentum relation is $E^2 = \mathbf p^2 + m^2$ — the Lorentz-invariant norm $p^\mu p_\mu = m^2$. The non-relativistic relation $E = \mathbf p^2/2m$ is its low-velocity limit; quantizing that limit produced the Schrödinger equation, which Special Relativity §10 showed is not Lorentz-covariant.

**2. The quantization rule.** Replace energy and momentum by operators, $E \to i\hbar\,\partial_t$ and $\mathbf p \to -i\hbar\nabla$. Applied to the non-relativistic relation this gives the Schrödinger equation of §1; applied to the exact relation it gives the relativistic equation.

**3. The Klein–Gordon attempt.** Quantizing $E^2 = \mathbf p^2 + m^2$ yields $(\Box + m^2/\hbar^2)\psi = 0$: manifestly Lorentz-covariant, but second order in time. The price (§3): the conserved density must involve $\partial_t\psi$, its sign follows $E$, and negative-energy solutions appear — two pathologies from one disease: a single-particle probability interpretation cannot survive.

**4. The Dirac equation.** To restore probability, demand first order in time — and covariance then forces first order in space. Consistency with the squared relation forces anticommuting matrices and a four-component spinor; the density $\psi^\dagger\psi$ is positive again, at the cost of questions — the extra components, the negative-energy branch — that single-particle mechanics cannot answer.

**The arc.** Each step is forced by the failure of the previous one: the Schrödinger equation fails covariance $\Rightarrow$ the Klein–Gordon equation restores it but loses probability $\Rightarrow$ the Dirac equation restores probability but raises questions that only second quantization can answer.
