# The Dirac Equation

This page continues from [Relativistic QM §4](relativistic-qm.md#_4-dirac-equation): the Dirac equation $(i\hbar\gamma^\mu\partial_\mu - m)\psi = 0$ with its four-component spinor. The questions that section had to defer — what the extra components are, and what the negative-energy branch means — are taken up here.

## 1. Spin

[Relativistic QM §4](relativistic-qm.md#_4-dirac-equation) deferred the meaning of the spinor's extra components. The identification is now forced by the equation itself. Begin with the standard definition: the total angular momentum of a particle is the sum of its orbital and intrinsic parts,

$$\mathbf J = \mathbf L + \mathbf S, \qquad \mathbf L = \mathbf r \times \mathbf p,$$

where $\mathbf L$ is the orbital angular momentum of the motion and $\mathbf S$ the intrinsic angular momentum. The Dirac equation shows that the intrinsic part is not optional. With the free Hamiltonian $H = \boldsymbol\alpha\cdot\hat{\mathbf p} + \beta m$,

$$[H, L_i] = -i\hbar\,(\boldsymbol\alpha \times \hat{\mathbf p})_i \neq 0,$$

so orbital angular momentum alone is not conserved. Conservation is a commutator statement: an observable $\mathbf A$ with no explicit time dependence evolves by the Heisenberg equation of motion ([§2](#_2-conservation-and-commutators))

$$\frac{d\mathbf A}{dt} = \frac{i}{\hbar}[H, \mathbf A],$$

so it is a constant of the motion exactly when $[H, \mathbf A] = 0$ — the commutator measures how fast the observable changes. That is the criterion used throughout this section: $[H, \mathbf L] \neq 0$ rules out $\mathbf L$ as a conserved quantity, and the intrinsic term must restore $[H, \mathbf J] = 0$.

The $\boldsymbol\alpha$ matrices act on the spinor's internal components, coupling the motion to degrees of freedom that $\mathbf L$ — a purely spatial operator — cannot see. What must the intrinsic term be? Two requirements constrain it: it must cancel the deficit, and it must be an angular momentum — its components must obey the angular-momentum commutation table, a property to be checked once the candidate is found. The first requirement fixes the size:

$$[H, S_i] = -[H, L_i] = i\hbar\,(\boldsymbol\alpha \times \hat{\mathbf p})_i.$$

Where does the candidate come from? It is already inside the equation. From [Relativistic QM §4](relativistic-qm.md#_4-dirac-equation), the Dirac matrices are built from Pauli matrices, $\alpha_j = \begin{pmatrix} 0 & \sigma_j \\ \sigma_j & 0 \end{pmatrix}$, so a product of two of them is block-diagonal: $\alpha_j\alpha_k = \mathrm{diag}(\sigma_j\sigma_k, \sigma_j\sigma_k)$. Antisymmetrizing the product, the Pauli commutator $[\sigma_j, \sigma_k] = 2i\varepsilon_{jkl}\sigma_l$ reappears in each block,

$$[\alpha_j, \alpha_k] = 2i\varepsilon_{jkl}\begin{pmatrix} \sigma_l & \mathbf 0 \\ \mathbf 0 & \sigma_l \end{pmatrix},$$

so the commutators of the equation's own matrices generate the block-diagonal Pauli matrix — the spin structure latent in the equation:

$$\boldsymbol\Sigma = \begin{pmatrix} \boldsymbol\sigma & \mathbf 0 \\ \mathbf 0 & \boldsymbol\sigma \end{pmatrix}.$$

Its commutator with the Hamiltonian follows from $[\alpha_j, \Sigma_i] = -2i\varepsilon_{ijk}\alpha_k$:

$$[H, \Sigma_i] = 2i\,(\boldsymbol\alpha \times \hat{\mathbf p})_i.$$

This is twice the needed deficit — the factor 2 is the one already sitting in the Pauli commutator $[\sigma_i, \sigma_j] = 2i\varepsilon_{ijk}\sigma_k$. Scaling down by exactly that factor produces the operator whose commutator cancels the deficit:

$$\mathbf S = \frac{\hbar}{2}\boldsymbol\Sigma.$$

The coefficient is fixed, not chosen: $\hbar/2$ is the ratio of the deficit $i\hbar(\boldsymbol\alpha\times\hat{\mathbf p})$ to what $\boldsymbol\Sigma$ provides, $2i(\boldsymbol\alpha\times\hat{\mathbf p})$ — the $\hbar$ from the canonical commutator $[x_j, p_k] = i\hbar\,\delta_{jk}$ inside $[H, \mathbf L]$, the 2 from the Pauli matrices. The check:

$$[H, S_i] = \frac{\hbar}{2}\,[H, \Sigma_i] = \frac{\hbar}{2}\cdot 2i\,(\boldsymbol\alpha \times \hat{\mathbf p})_i = i\hbar\,(\boldsymbol\alpha \times \hat{\mathbf p})_i = -[H, L_i],$$

so the **total angular momentum** $\mathbf J = \mathbf L + \mathbf S$ commutes with $H$. Neither orbital angular momentum nor spin is separately conserved — the equation's structure mixes them, exactly as a relativistic theory should — but their sum is.

What kind of operator is this $\mathbf S$? Because the $\sigma_i$ satisfy $[\sigma_i, \sigma_j] = 2i\varepsilon_{ijk}\sigma_k$, the components of $\mathbf S$ satisfy

$$[S_i, S_j] = i\hbar\,\varepsilon_{ijk} S_k,$$

the **angular-momentum algebra** — the defining commutation relations of angular momentum. "Algebra" in the sense of a set closed under the commutator: the commutator of any two components is again a component ($[S_x, S_y] = i\hbar S_z$, cyclically), so the three operators form a self-contained structure. The identification carries the physics: any three operators satisfying this table are angular momentum — orbital $\mathbf L$ obeys the same relations, and the Pauli matrices are one particular realization of it, the smallest, not its source — and the table is the infinitesimal statement that rotations about different axes do not commute. The eigenvalues follow at once: $\Sigma_z$ has eigenvalues $\pm 1$, so $S_z$ has eigenvalues $\pm\hbar/2$. The extra components are spin, and the equation describes a spin-½ particle; the two components of each pair are spin-up and spin-down.

The equation also fixes the magnetic moment. Coupling to an electromagnetic field (minimal substitution $\hat{\mathbf p} \to \hat{\mathbf p} + e\mathbf A$) gives, in the non-relativistic limit, the Pauli equation with

$$\boldsymbol\mu = -\frac{e}{m}\,\mathbf S, \qquad g = 2,$$

Dirac's famous prediction: the electron's gyromagnetic ratio is twice the classical value. This answers the first deferred question of [Relativistic QM §4](relativistic-qm.md#_4-dirac-equation) — the extra components are the two spin states of a spin-½ particle, and their transformation properties are the subject of [§5](#_5-spinors-transformations) below.

## 2. Conservation and Commutators

The criterion used in [§1](#_1-spin) — an observable is conserved exactly when it commutes with the Hamiltonian — deserves a proof. An observable $\mathbf A$ with no explicit time dependence evolves by the **Heisenberg equation of motion**,

$$\frac{d\mathbf A}{dt} = \frac{i}{\hbar}[H, \mathbf A],$$

so it is a constant of the motion exactly when $[H, \mathbf A] = 0$: the commutator measures how fast the observable changes. The equation is proved by carrying the time evolution in the operator itself. In the **Heisenberg picture**,

$$\mathbf A_H(t) = e^{iHt/\hbar}\,\mathbf A\,e^{-iHt/\hbar},$$

with $\mathbf A_H(0) = \mathbf A$. Differentiating — using $\frac{d}{dt}e^{\pm iHt/\hbar} = \pm\frac{i}{\hbar}H\,e^{\pm iHt/\hbar}$, valid because $H$ is time-independent and so commutes with its own exponential —

$$\frac{d\mathbf A_H}{dt} = \frac{i}{\hbar}\left(H e^{iHt/\hbar}\mathbf A e^{-iHt/\hbar} - e^{iHt/\hbar}\mathbf A e^{-iHt/\hbar} H\right) = \frac{i}{\hbar}[H, \mathbf A_H].$$

Taking expectation values in any state gives $d\langle\mathbf A\rangle/dt = \frac{i}{\hbar}\langle[H, \mathbf A]\rangle$: the expectation value is constant exactly when the commutator vanishes. An explicit time dependence in $\mathbf A$ would add a term $\langle\partial\mathbf A/\partial t\rangle$; none of the operators on this page has one.

This is the criterion applied in [§1](#_1-spin): orbital angular momentum fails it — $[H, \mathbf L] \neq 0$ — and the intrinsic term $\mathbf S$ is exactly the correction that restores it, $[H, \mathbf J] = 0$. The same criterion is used, without further proof, on the pages that follow.

## 3. Antiparticles

The second deferred question: the negative-energy branch. The fastest way in is to solve the equation: plane waves separate into two cases, rest and moving, and the solutions at rest are the whole structure in embryo.

**At rest ($\mathbf p = 0$).** The Hamiltonian is simply $H = \beta m$, so a plane wave $\psi = w\,e^{-iEt/\hbar}$ with constant four-vector $w$ satisfies

$$E\,w = \beta m\,w.$$

Where do these two values come from? The equation is an eigenvalue problem: $\beta$ has eigenvalues $+1$ (twice) and $-1$ (twice) — the content of its diagonal form — so multiplying by $m$ fixes $E$ to exactly the two values $E = +m$ and $E = -m$, the two roots of $E^2 = m^2$. These are the two branches of the dispersion relation of [Relativistic QM §2](relativistic-qm.md#_2-klein-gordon) seen at $\mathbf p = 0$: iterating the Dirac equation reproduces $E^2 = \mathbf p^2 + m^2$, and at rest that is simply the rest energy with either sign, $E = \pm m$. The equation does not choose between them — both are realized, one in each pair of components. Each eigenspace of $\beta$ being two-dimensional, there are exactly four independent solutions, the basis vectors of the four-component space: two with $E = +m$, supported on the upper pair, and two with $E = -m$, supported on the lower pair,

$$E = +m: \quad w = \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix}; \qquad E = -m: \quad w = \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \end{pmatrix}.$$

The four components are forced, not chosen: the equation needs four mutually anticommuting matrices, and in $2 \times 2$ the three Pauli matrices cannot be extended by a fourth — each anticommutes with the others but not with itself — so the matrices, and with them $\psi$, live in $4 \times 4$ ([Relativistic QM §4](relativistic-qm.md#_4-dirac-equation)): two pairs, the particle and antiparticle components of the previous page.

The two members of each pair are the two **spin states** along $z$ — the eigenstates of the spin projection $S_z = \tfrac{\hbar}{2}\Sigma_z$. Call the four rest solutions $w^{(1)}_+, w^{(2)}_+, w^{(1)}_-, w^{(2)}_-$. Since $\Sigma_z = \mathrm{diag}(1, -1, 1, -1)$,

$$S_z\,w^{(1)}_\pm = +\frac{\hbar}{2}\,w^{(1)}_\pm, \qquad S_z\,w^{(2)}_\pm = -\frac{\hbar}{2}\,w^{(2)}_\pm,$$

the two eigenvalues, each occurring once per pair: the first member of each pair is **spin up** ($+\hbar/2$), the second **spin down** ($-\hbar/2$). On each pair the operator acts as $\tfrac{\hbar}{2}\sigma_z$, the factor $\tfrac12$ being the spin quantum number of §1 — not a consequence of the block structure — and the total spin is $\mathbf S^2 = \tfrac{\hbar^2}{4}\boldsymbol\Sigma^2 = \tfrac{3\hbar^2}{4}$, computed directly from the matrices ($\boldsymbol\Sigma^2 = 3$, since each $\sigma_i^2 = 1$): a magnitude $\tfrac{\sqrt3}{2}\hbar$, larger than the largest projection $\tfrac{\hbar}{2}$ — the spin vector never lies along a single axis.

The axis is a choice: for any direction $\mathbf n$ the operator $\mathbf n\cdot\mathbf S = \tfrac{\hbar}{2}\,\mathbf n\cdot\boldsymbol\Sigma$ has the same two eigenvalues $\pm\hbar/2$ (the Pauli matrices have eigenvalues $\pm 1$ along every axis), so every direction defines spin states of its own, the eigenstates of $\mathbf n\cdot\mathbf S$; the $z$-axis is singled out here only by the basis we wrote down. At rest the equation is therefore completely solved — four states, two energies, two spins each.

**Moving ($\mathbf p \neq 0$).** For a plane wave $\psi = w(p)\,e^{-ip\cdot x/\hbar}$, the equation becomes algebraic,

$$(E - \boldsymbol\alpha\cdot\mathbf p - \beta m)\,w = 0,$$

and writing $w = (\phi, \chi)$ for the upper and lower pairs of [Relativistic QM §4](relativistic-qm.md#_4-dirac-equation) recovers the coupled equations found there,

$$(E - m)\,\phi = \boldsymbol\sigma\cdot\mathbf p\,\chi, \qquad (E + m)\,\chi = \boldsymbol\sigma\cdot\mathbf p\,\phi.$$

For $E = +E_p$ (with $E_p = +\sqrt{\mathbf p^2 + m^2}$) the lower pair is determined by the upper, $\chi = \frac{\boldsymbol\sigma\cdot\mathbf p}{E_p + m}\,\phi$, so there are again two independent solutions, fixed by the choice of spin state in the upper pair. This is where the **spinors** enter — the momentum-dependent four-vectors, in the standard normalization, with $\chi_\uparrow = (1, 0)^T$ and $\chi_\downarrow = (0, 1)^T$:

$$u_s(p) = \begin{pmatrix} \sqrt{E_p + m}\;\chi_s \\ \dfrac{\boldsymbol\sigma\cdot\mathbf p}{\sqrt{E_p + m}}\;\chi_s \end{pmatrix} \qquad (E = +E_p),$$

which reduce to the two positive rest solutions at $\mathbf p = 0$. For $E = -E_p$ the roles reverse — the upper pair is now determined by the lower, $\phi = -\frac{\boldsymbol\sigma\cdot\mathbf p}{E_p + m}\,\chi$, the minus sign forced by the coupled equations — giving the two negative-energy spinors

$$v_s(p) = \begin{pmatrix} -\dfrac{\boldsymbol\sigma\cdot\mathbf p}{\sqrt{E_p + m}}\;\chi_s \\ \sqrt{E_p + m}\;\chi_s \end{pmatrix} \qquad (E = -E_p),$$

with the lower pair large, exactly as [Relativistic QM §4](relativistic-qm.md#_4-dirac-equation) found.

The two branches are not independent: they are each other's charge conjugates. Taking the complex conjugate of the Dirac equation and multiplying by a suitable matrix $\eta$ (in the standard representation $\eta = i\gamma^2$) gives a solution of the same form with opposite charge — the **charge-conjugated spinor**

$$\psi_c = \eta\,\psi^*,$$

and on the plane-wave solutions it maps the particle branch onto the antiparticle branch, $\eta\,u_s(p)^* = v_{s'}(-p)$ up to a phase, with momentum reversed and the two spin states interchanged. If $\psi$ describes a particle of charge $e$, then $\psi_c$ describes one of charge $-e$: the Dirac equation is invariant under charge conjugation. The negative-frequency solutions are therefore not redundant — they are the wave functions of a particle with the same mass and opposite charge, the **antiparticle**. Together with the Stückelberg–Feynman reading of [Relativistic QM §3](relativistic-qm.md#_3-negative-energy-and-probability) — negative-frequency waves propagating backward in time — this is the physics of the positron, predicted by the equation and discovered in 1932, six years later.

What cannot be done at this level: making this precise requires particles to be created and destroyed, which a single-particle wave function cannot describe. The statement that survives at this level is that the Dirac equation has room in its mathematics for both particles and antiparticles — the positive-frequency and negative-frequency parts of its solutions — and that both are physical.

## 4. Negative Energy Solutions

The two families of [§3](#_3-antiparticles) — the positive-energy $u$-branch and the negative-energy $v$-branch — pose the problem that [Relativistic QM §4](relativistic-qm.md#_4-dirac-equation) sharpened: both carry positive density $\psi^\dagger\psi$, so nothing marks a negative-energy state as unphysical, and the energy is unbounded below — an interacting electron could radiate energy forever, falling through negative levels. Dirac's resolution was the **hole theory**. The vacuum is not empty; every negative-energy state is occupied — a filled sea of electrons, which the Pauli exclusion principle protects from further occupancy. A missing electron in the sea then behaves as a positive-energy particle of positive charge: a **hole**, the positron. When a positive-energy electron falls into a hole, both disappear — the energy released is radiated away: pair annihilation; the reverse process, lifting an electron out of the sea into a positive level and leaving a hole behind, is pair creation.

Two honest caveats, in the spirit of the previous pages: the sea picture leans on fermionic statistics (the exclusion principle), and on a many-particle vacuum — both belong to the quantized theory, where the hole picture is replaced by creation and annihilation operators acting on the vacuum. What the single-particle equation contributes is definitive: negative-energy solutions exist, they carry opposite charge ([§3](#_3-antiparticles)), and their interpretation is the doorway to field theory.

## 5. Spinors (Transformations)

The four-component object transforms differently from anything encountered so far. Under a Lorentz transformation $x' = \Lambda x$, the spinor transforms as

$$\psi'(x') = S(\Lambda)\,\psi(x), \qquad S(\Lambda) = \exp\!\left(-\frac{i}{4}\,\omega_{\mu\nu}\sigma^{\mu\nu}\right), \qquad \sigma^{\mu\nu} = \frac{i}{2}\,[\gamma^\mu, \gamma^\nu],$$

where $\omega_{\mu\nu}$ are the boost/rotation parameters. Three features set $S$ apart from the transformations of vectors and scalars:

1. **Finite-dimensional.** $S(\Lambda)$ is a $4 \times 4$ matrix — a finite-dimensional representation of the Lorentz group — whereas the familiar transformations on functions (rotations of $\psi(\mathbf x)$) are infinite-dimensional. The spinor representation is a genuinely new structure.
2. **Double-valued.** A rotation by $2\pi$ gives $S = -\mathbb{1}$: the spinor returns to itself only up to a sign. A $4\pi$ rotation is needed to return exactly. No scalar or vector does this; the minus sign is the signature of spin-½.
3. **Reducible.** The $4 \times 4$ representation splits into two $2 \times 2$ pieces, $(\tfrac{1}{2}, 0) \oplus (0, \tfrac{1}{2})$ — the two two-component pieces are the **Weyl spinors**, which transform under rotations identically (the $\boldsymbol\Sigma/2$ of [§1](#_1-spin)) and under boosts oppositely. They are the left- and right-handed parts of the Dirac spinor.

For rotations alone, $S = \exp\!\left(-\tfrac{i}{2}\,\boldsymbol\theta\cdot\boldsymbol\Sigma\right)$ — the spin operator of [§1](#_1-spin) as the generator, confirming from the transformation side that the extra components carry angular momentum $\hbar/2$.

## 6. General Solution

The Dirac equation is linear, so the general free solution superposes the four independent solutions per momentum — two spins, two energy signs. In the standard normalization,

$$\psi(x) = \sum_{s=1}^{2} \int \frac{d^3p}{(2\pi\hbar)^3}\,\frac{1}{\sqrt{2E_p}}\left[a_s(p)\,u_s(p)\,e^{-ip\cdot x/\hbar} + b_s^*(p)\,v_s(p)\,e^{+ip\cdot x/\hbar}\right],$$

with $p\cdot x = E_p t - \mathbf p\cdot\mathbf x$. The spinors derived in [§3](#_3-antiparticles), for a spin direction $\chi_s$ ($\chi_\uparrow = (1, 0)^T$, $\chi_\downarrow = (0, 1)^T$),

$$u_s(p) = \begin{pmatrix} \sqrt{E_p + m}\;\chi_s \\ \dfrac{\boldsymbol\sigma\cdot\mathbf p}{\sqrt{E_p + m}}\;\chi_s \end{pmatrix}, \qquad v_s(p) = \begin{pmatrix} -\dfrac{\boldsymbol\sigma\cdot\mathbf p}{\sqrt{E_p + m}}\;\chi_s \\ \sqrt{E_p + m}\;\chi_s \end{pmatrix},$$

reproduce the structure of [Relativistic QM §4](relativistic-qm.md#_4-dirac-equation): for $u$ (positive energy) the upper pair is large at low momentum; for $v$ (negative energy) the roles reverse.

The general solution is where the whole page comes together. The $u$-part carries the particles, the $v$-part the antiparticles of [§3](#_3-antiparticles) and [§4](#_4-negative-energy-solutions); both are dressed with the spin structure of [§1](#_1-spin), and both transform as the spinors of [§5](#_5-spinors-transformations). The coefficients $a_s(p)$ and $b_s^*(p)$ are complex numbers here — in the quantized theory they become the creation and annihilation operators of the electron and positron fields. That is the bridge to the next stage.
