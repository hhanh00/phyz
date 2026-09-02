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

The equation also fixes the magnetic moment. Coupling a particle of charge $q$ to an electromagnetic field is done by **minimal substitution**: wherever the equation carries a momentum or a derivative, replace it by itself minus $q$ times the potential — $\hat{\mathbf p} \to \hat{\mathbf p} - q\mathbf A$, covariantly $\partial_\mu \to \partial_\mu + \tfrac{iq}{\hbar}A_\mu$. This is the rule by which charge enters the equation at all — the quantum version of the classical $\mathbf p \to \mathbf p - q\mathbf A$ that reproduces the Lorentz force. For the electron, $q = -e$; the substitution gives, in the non-relativistic limit, the Pauli equation with

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

What can $E$ be? At rest $\beta$ is diagonal — $\beta = \mathrm{diag}(1, 1, -1, -1)$ in the representation of [Relativistic QM §4](relativistic-qm.md#_4-dirac-equation) — so the single equation is really four ordinary equations, one per component of $w = (w_1, w_2, w_3, w_4)$:

$$E\,w_1 = m\,w_1, \qquad E\,w_2 = m\,w_2, \qquad E\,w_3 = -m\,w_3, \qquad E\,w_4 = -m\,w_4.$$

Each rearranges to a product set equal to zero, and a product is zero only when one of its factors is zero. So the first two equations say: **either the upper component is zero, or $E = m$**; the last two: **either the lower component is zero, or $E = -m$**. Now $w$ is a solution, and the zero vector is not — so at least one component survives, and whichever survives forces its equation's value of $E$. Three cases exhaust everything:

1. **$E \ne \pm m$:** the first pair of equations forces the upper components to zero, the second pair the lower ones — all four vanish, and that is not a solution. The case is empty.
2. **$E = m$:** the last two equations read $m\,w_3 = -m\,w_3$, so $w_3 = w_4 = 0$, while $w_1, w_2$ stay free: $w = (w_1, w_2, 0, 0)$, anything in the upper pair. Two independent solutions.
3. **$E = -m$:** symmetrically, the upper pair is forced to zero and $w = (0, 0, w_3, w_4)$ — two more solutions.

So $E = \pm m$ — nothing else — and no solution mixes the two pairs. These are the two branches of the dispersion relation $E^2 = \mathbf p^2 + m^2$ of [Relativistic QM §2](relativistic-qm.md#_2-klein-gordon) seen at $\mathbf p = 0$ — a relation every solution obeys, since the anticommutation of the Dirac matrices collapses $(\boldsymbol\alpha\cdot\hat{\mathbf p} + \beta m)^2$ to $\mathbf p^2 + m^2$. Both signs are realized, one in each pair of components: each eigenspace of $\beta$ is two-dimensional, so there are exactly four independent solutions, the basis vectors of the four-component space — two with $E = +m$, supported on the upper pair, and two with $E = -m$, supported on the lower pair,

$$E = +m: \quad w = \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix}; \qquad E = -m: \quad w = \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \end{pmatrix}.$$

The four components are forced, not chosen: the equation needs four mutually anticommuting matrices, and in $2 \times 2$ the three Pauli matrices cannot be extended by a fourth — each anticommutes with the others but not with itself — so the matrices, and with them $\psi$, live in $4 \times 4$ ([Relativistic QM §4](relativistic-qm.md#_4-dirac-equation)): two pairs, the particle and antiparticle components of the previous page.

The two members of each pair are the two **spin states** along $z$ — the eigenstates of the spin projection $S_z = \tfrac{\hbar}{2}\Sigma_z$. Call the four rest solutions $w^{(1)}_+, w^{(2)}_+, w^{(1)}_-, w^{(2)}_-$. Since $\Sigma_z = \mathrm{diag}(1, -1, 1, -1)$,

$$S_z\,w^{(1)}_\pm = +\frac{\hbar}{2}\,w^{(1)}_\pm, \qquad S_z\,w^{(2)}_\pm = -\frac{\hbar}{2}\,w^{(2)}_\pm,$$

the two eigenvalues, each occurring once per pair: the first member of each pair is **spin up** ($+\hbar/2$), the second **spin down** ($-\hbar/2$). On each pair the operator acts as $\tfrac{\hbar}{2}\sigma_z$, the factor $\tfrac12$ being the spin quantum number of §1. (This was done independently of the choice of axis: any direction would have served in place of $z$ — it entered only through the basis we wrote down.) At rest the equation is therefore completely solved — four states, two energies, two spins each.

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

and on the plane-wave solutions it maps the particle branch onto the antiparticle branch, $\eta\,u_s(p)^* = v_{s'}(-p)$ up to a phase, with momentum reversed and the two spin states interchanged. Where does charge enter? The equation on this page is free — it contains no charge at all. Charge comes in exactly one way: the minimal substitution defined in [§1](#_1-spin), coupling a particle of charge $q$ to an electromagnetic potential $A_\mu$ by $\partial_\mu \to \partial_\mu + \tfrac{iq}{\hbar}A_\mu$. Conjugating that substitution flips the sign of its $A_\mu$ term, so $\psi_c = \eta\,\psi^*$ solves the coupled equation with charge $-q$: if $\psi$ describes a particle of charge $q$, then $\psi_c$ describes one of charge $-q$ — the Dirac equation is invariant under charge conjugation. The negative-frequency solutions are therefore not redundant — they are the wave functions of a particle with the same mass and opposite charge, the **antiparticle**. Together with the Stückelberg–Feynman reading of [Relativistic QM §3](relativistic-qm.md#_3-negative-energy-and-probability) — negative-frequency waves propagating backward in time — this is the physics of the positron, predicted by the equation and discovered in 1932, six years later.

What cannot be done at this level: making this precise requires particles to be created and destroyed, which a single-particle wave function cannot describe. The statement that survives at this level is that the Dirac equation has room in its mathematics for both particles and antiparticles — the positive-frequency and negative-frequency parts of its solutions — and that both are physical.

## 4. Negative Energy Solutions

The two families of [§3](#_3-antiparticles) — the positive-energy $u$-branch and the negative-energy $v$-branch — pose the problem that [Relativistic QM §4](relativistic-qm.md#_4-dirac-equation) sharpened: both carry positive density $\psi^\dagger\psi$, so nothing marks a negative-energy state as unphysical, and the energy is unbounded below — an interacting electron could radiate energy forever, falling through negative levels. A single-particle wave function has no way out: the branches are what the equation gives, and no reinterpretation of a fixed-number wave function can remove half of them. The way out is the change of object this whole sequence has been announcing.

**How the quantized formulation handles the branch.** The mechanism is worth stating, even ahead of its construction on the [QFT](qft.md) page. When the coefficients of the general solution of [§6](#_6-general-solution) are promoted to operators, the Hamiltonian rebuilt from them takes the form, per mode, $E_p\,(\hat a^\dagger\hat a - \hat b\,\hat b^\dagger)$ — the minus sign of the negative branch is still there, now multiplying the antiparticle operators. But reordering the second product — creation operators to the left, the two forms differing by a constant that is absorbed into the vacuum's zero of energy — turns it into $E_p\,(\hat a^\dagger\hat a + \hat b^\dagger\hat b)$: electrons contribute $+E_p$ each, and so do positrons. The operator $\hat b^\dagger$, which creates the equation's $E = -E_p$ solution, is thereby read as creating a *positron of positive energy* — the Stückelberg–Feynman reading of [Relativistic QM §3](relativistic-qm.md#_3-negative-energy-and-probability) made into bookkeeping. The minus sign does not disappear; it moves from the energy of a state to the interpretation of an operator. Nothing observable ever carries negative energy — the branch's danger was never a state anyone could occupy, but a reading no one could sustain.

The historical route to the same place was Dirac's **hole theory**, proposed before quantization. The vacuum is not empty: every negative-energy state is occupied — a filled sea of electrons, protected from further occupancy by the exclusion principle. A missing electron in the sea then behaves as a positive-energy particle of positive charge: a **hole**, the positron. An electron falling into a hole disappears with it — pair annihilation; lifting an electron out leaves a hole behind — pair creation. The picture predicted the positron and named the processes, but its two load-bearing props — fermionic statistics and a many-particle vacuum — are exactly what the quantized theory supplies properly: the sea is the vacuum, and the hole is what the positron's creation operator creates. When the [QFT](qft.md) page says the hole picture is *replaced* by operators, this is the face of the replacement.

## 5. Spinors

The four-component object transforms differently from anything encountered so far. Under a Lorentz transformation $x' = \Lambda x$, the spinor transforms as

$$\psi'(x') = S(\Lambda)\,\psi(x), \qquad S(\Lambda) = \exp\!\left(-\frac{i}{4}\,\omega_{\mu\nu}\sigma^{\mu\nu}\right), \qquad \sigma^{\mu\nu} = \frac{i}{2}\,[\gamma^\mu, \gamma^\nu],$$

where $\omega_{\mu\nu}$ are the boost/rotation parameters. Three features set $S$ apart from the transformations of vectors and scalars:

1. **Finite-dimensional.** $S(\Lambda)$ is a $4 \times 4$ matrix — a finite-dimensional representation of the Lorentz group — whereas the familiar transformations on functions (rotations of $\psi(\mathbf x)$) are infinite-dimensional. The spinor representation is a genuinely new structure.
2. **Double-valued.** A rotation by $2\pi$ gives $S = -\mathbb{1}$: the spinor returns to itself only up to a sign. A $4\pi$ rotation is needed to return exactly. No scalar or vector does this; the minus sign is the signature of spin-½.
3. **Reducible.** The $4 \times 4$ representation splits into two $2 \times 2$ pieces, $(\tfrac{1}{2}, 0) \oplus (0, \tfrac{1}{2})$ — the two two-component pieces are the **Weyl spinors**, which transform under rotations identically (the $\boldsymbol\Sigma/2$ of [§1](#_1-spin)) and under boosts oppositely. They are the left- and right-handed parts of the Dirac spinor.

For rotations alone, $S = \exp\!\left(-\tfrac{i}{2}\,\boldsymbol\theta\cdot\boldsymbol\Sigma\right)$ — the spin operator of [§1](#_1-spin) as the generator, confirming from the transformation side that the extra components carry angular momentum $\hbar/2$. The boost case, and the derivation of the general formula itself, are in the extra subsection below — heavy on calculation, and safe to skip.

### Extra: Deriving the Spinor Transformation

This subsection is extra material: it is nearly all calculation, and nothing later in the sequence depends on it. Skip it freely. The main text states the transformation formula; what follows derives it from the one requirement the Dirac equation imposes.

The requirement is covariance. Let $\psi(x)$ solve $(i\hbar\gamma^\mu\partial_\mu - m)\psi = 0$ in one frame, and ask that $\psi'(x') = S(\Lambda)\,\psi(x)$ solve the same equation in the frame $x' = \Lambda x$, where $\partial'_\mu = (\Lambda^{-1})^\nu{}_\mu\,\partial_\nu$. Substituting into the primed equation and multiplying by $S^{-1}$,

$$(i\hbar\,S^{-1}\gamma^\mu S\,(\Lambda^{-1})^\nu{}_\mu\,\partial_\nu - m)\,\psi = 0,$$

and this is the original equation for every solution $\psi$ exactly when

$$S^{-1}\gamma^\mu S = \Lambda^\mu{}_\nu\,\gamma^\nu.$$

Now specialize to transformations near the identity, $\Lambda^\mu{}_\nu = \delta^\mu_\nu + \omega^\mu{}_\nu$, where the antisymmetric parameters $\omega_{\mu\nu} = -\omega_{\nu\mu}$ carry the three rotation angles and three boost rapidities, and let $S = 1 + \Omega$ to the same order. Then $S^{-1}\gamma^\mu S = (1 - \Omega)\,\gamma^\mu\,(1 + \Omega) = \gamma^\mu - [\Omega, \gamma^\mu]$, and the condition becomes

$$-[\Omega, \gamma^\mu] = \omega^\mu{}_\nu\,\gamma^\nu.$$

The claim is $\Omega = -\frac{i}{4}\,\omega_{\rho\sigma}\,\sigma^{\rho\sigma}$ with $\sigma^{\rho\sigma} = \frac{i}{2}[\gamma^\rho, \gamma^\sigma]$, and its verification needs one commutator identity. For any three matrices, $[AB, C] = A\{B, C\} - \{A, C\}B$, as expanding both sides shows. With $A = \gamma^\rho$, $B = \gamma^\sigma$, $C = \gamma^\mu$, and the Clifford algebra $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$,

$$[\gamma^\rho\gamma^\sigma, \gamma^\mu] = \gamma^\rho\,\{\gamma^\sigma, \gamma^\mu\} - \{\gamma^\rho, \gamma^\mu\}\,\gamma^\sigma = 2\,(g^{\mu\sigma}\gamma^\rho - g^{\mu\rho}\gamma^\sigma).$$

The commutator inside $\sigma^{\rho\sigma}$ is this twice over, once for each ordering of the two $\gamma$'s,

$$[\sigma^{\rho\sigma}, \gamma^\mu] = \frac{i}{2}\,\big([\gamma^\rho\gamma^\sigma, \gamma^\mu] - [\gamma^\sigma\gamma^\rho, \gamma^\mu]\big) = 2i\,(g^{\mu\sigma}\gamma^\rho - g^{\mu\rho}\gamma^\sigma).$$

Substituting into the left side of the condition,

$$-[\Omega, \gamma^\mu] = \frac{i}{4}\,\omega_{\rho\sigma}\cdot 2i\,(g^{\mu\sigma}\gamma^\rho - g^{\mu\rho}\gamma^\sigma) = -\frac{1}{2}\,\omega_{\rho\sigma}\,(g^{\mu\sigma}\gamma^\rho - g^{\mu\rho}\gamma^\sigma) = -\omega^\mu{}_\nu\,\gamma^\nu,$$

where the last step raises an index, $g^{\mu\sigma}\omega_{\rho\sigma} = \omega_\rho{}^\mu = -\omega^\mu{}_\rho$, and uses antisymmetry: the two metric terms come out equal rather than opposite. This satisfies the condition exactly, so the exponential form of the main text works to first order in $\omega$, and since parameters of composed transformations add, exponentiation promotes first order to all orders.

### An even more detailed derivation

The derivation above stands on its own, so the following checks are optional even by this subsection's standards. But they serve a second purpose: anyone content to take the formula as given can watch it act in two explicit cases, a rotation and a boost. Two cases suffice, because any Lorentz transformation connected to the identity is a composition of a rotation and a boost, so a formula that reproduces both reproduces the general case.

Before either case, pause over what the formula asserts, since the rest of this subsection only unpacks it. The matrix $S$ is an exponential, $S = e^{\Omega}$ with $\Omega = -\frac{i}{4}\sum_{\mu,\nu}\omega_{\mu\nu}\sigma^{\mu\nu}$. The exponential of a matrix is defined by the same power series as the exponential of a number, $e^{M} = 1 + M + \frac{1}{2!}M^2 + \frac{1}{3!}M^3 + \cdots$, where $1$ now means the $4\times4$ identity matrix, $M^2$ means the matrix product $M\cdot M$, and so on. Two properties of this series do all the work below. Because the dagger (conjugate transpose) reverses the order of a product, $(AB)^\dagger = B^\dagger A^\dagger$, every power satisfies $(M^n)^\dagger = (M^\dagger)^n$, so taking the dagger of the whole series term by term gives $(e^M)^\dagger = e^{M^\dagger}$. And because a matrix commutes with every power of itself, the series obeys $e^M e^{-M} = e^{M-M} = 1$: the exponential of $-M$ is the inverse of the exponential of $M$. Both properties are used below.

The symbols $\omega$ and $\sigma$ are objects of different kinds, and telling them apart prevents most of the confusion. The $\omega_{\mu\nu}$ are numbers. They are the parameters of the transformation, the amounts by which it departs from doing nothing, and they are read off the Lorentz matrix. The indices $\mu,\nu$ run over the four coordinates, with $0$ standing for time and $1,2,3$ for space, and a Lorentz transformation $\Lambda$ relates the coordinates of an event in two frames by $x'^\mu = \sum_\nu \Lambda^\mu{}_\nu x^\nu$, so $\Lambda$ is a $4\times4$ table of numbers. Near the identity that table is nearly the identity table $\delta$, which has $1$'s on the diagonal and $0$'s elsewhere, and one writes $\Lambda^\mu{}_\nu = \delta^\mu{}_\nu + \omega^\mu{}_\nu$, with $\omega^\mu{}_\nu$ the small corrections. The $\omega_{\mu\nu}$ that appear in the formula are the same numbers with the first index lowered by the metric, $\omega_{\mu\nu} = g_{\mu\rho}\,\omega^\rho{}_\nu$; on this page $g_{00} = 1$ and $g_{11} = g_{22} = g_{33} = -1$, and the only lowering we will need has the first index equal to $0$, where the metric leaves the number alone. The parameters are antisymmetric, $\omega_{\nu\mu} = -\omega_{\mu\nu}$. This is not an extra assumption: a Lorentz transformation is defined by preserving the interval, which in matrix form is $\Lambda^T g\Lambda = g$, and expanding $\Lambda = 1 + \omega$ in that condition gives exactly $\omega_{\nu\mu} = -\omega_{\mu\nu}$ at first order. Antisymmetry makes the diagonal entries vanish (a number equal to its own negative is zero) and reduces the sixteen entries to six independent ones, one for each pair $\mu<\nu$. Those six split into two types: the pairs $(0,1), (0,2), (0,3)$ carry a time index and describe boosts, which mix time with one spatial direction, and the pairs $(1,2), (1,3), (2,3)$ are purely spatial and describe rotations.

The $\sigma^{\mu\nu}$ are matrices, not numbers: $4\times4$ matrices acting on the spinor. Their definition, $\sigma^{\mu\nu} = \frac{i}{2}\left(\gamma^\mu\gamma^\nu - \gamma^\nu\gamma^\mu\right)$, uses nothing but the Dirac matrices, the fixed matrices of the equation, so the $\sigma$'s are the same for every transformation, and they are the raw material out of which $S$ is built. Matrices used this way, one attached to each index pair, multiplied by the corresponding parameter and summed inside an exponential, are called the **generators** of the transformation: for very small parameters the exponential is approximately $1 + \Omega$, so $\Omega$ is the infinitesimal change the transformation produces, and iterating many tiny transformations multiplies those changes into the finite exponential. Because $\sigma^{\mu\nu}$ is $\frac{i}{2}$ times a commutator, and a commutator changes sign when its two entries are swapped, the generators are antisymmetric in their indices too, $\sigma^{\nu\mu} = -\sigma^{\mu\nu}$, so the sixteen of them reduce to the same six pairs as the parameters.

Both cases share one piece of bookkeeping, which is also where the factor $-\frac{i}{4}$ in the formula comes from. In the double sum over all $\mu$ and $\nu$, the term $(\mu,\nu)$ and the reversed term $(\nu,\mu)$ are equal, because each is the other's two minus signs multiplied out, and the diagonal terms vanish. Summing over all sixteen pairs therefore counts each unordered pair twice, so the sum halves to one term per pair with the coefficient doubled:

$$\Omega = -\frac{i}{4}\sum_{\mu,\nu}\omega_{\mu\nu}\sigma^{\mu\nu} = -\frac{i}{2}\sum_{\mu<\nu}\omega_{\mu\nu}\,\sigma^{\mu\nu}.$$

A rotation uses only the spatial pairs and a boost only one time–space pair, so each case evaluates its own few terms of this reduced sum. The recipe is the same in both: find which $\omega$ survive and what they are, compute the corresponding $\sigma$'s, multiply each generator by its parameter, and exponentiate.

**Rotation.** A rotation turns the spatial axes and leaves time alone: in the rotated frame an event still has $t' = t$, so the Lorentz matrix has zeros wherever it would mix time with space. Near the identity that means $\omega_{0i} = 0$ for $i = 1,2,3$: the three boost pairs drop out, and only the numbers $\omega_{12}, \omega_{13}, \omega_{23}$ and the matrices $\sigma^{12}, \sigma^{13}, \sigma^{23}$ survive. The reduced exponent is

$$\Omega_{\text{rot}} = -\frac{i}{2}\left(\omega_{12}\,\sigma^{12} + \omega_{13}\,\sigma^{13} + \omega_{23}\,\sigma^{23}\right).$$

The whole rotation case is the computation of these three generators, each a commutator of two spatial Dirac matrices, $\sigma^{ij} = \frac{i}{2}\left(\gamma^i\gamma^j - \gamma^j\gamma^i\right)$, followed by a reassembly of the three terms.

To compute the commutators one must multiply Dirac matrices, so we need their entries. In the standard representation of [Relativistic QM §4](relativistic-qm.md#_4-dirac-equation), $\gamma^0 = \beta$ and $\gamma^i = \beta\alpha_i$, where $\beta$ and $\alpha_i$ are known from [§1](#_1-spin). Written as $2\times2$ arrays of $2\times2$ blocks, with $0$ the zero block, $1$ the identity block, and $\sigma_i$ the Pauli matrices of [§1](#_1-spin),

$$\beta = \begin{pmatrix}1 & 0 \\ 0 & -1\end{pmatrix}, \qquad \alpha_i = \begin{pmatrix}0 & \sigma_i \\ \sigma_i & 0\end{pmatrix}.$$

Block multiplication works exactly like multiplication of ordinary $2\times2$ matrices, with the blocks playing the role of the entries: the block in row $a$, column $b$ of a product is the sum over $c$ of the block in row $a$, column $c$ of the first factor times the block in row $c$, column $b$ of the second. Applying the rule to $\beta\alpha_i$,

$$\gamma^i = \beta\alpha_i = \begin{pmatrix}1\cdot 0 + 0\cdot\sigma_i & 1\cdot\sigma_i + 0\cdot 0 \\ 0\cdot 0 + (-1)\cdot\sigma_i & 0\cdot\sigma_i + (-1)\cdot 0\end{pmatrix} = \begin{pmatrix}0 & \sigma_i \\ -\sigma_i & 0\end{pmatrix}.$$

Now multiply two of these matrices, $\gamma^i\gamma^j$ with $i\neq j$. The same rule gives four block products, of which the two off-diagonal ones vanish:

$$\gamma^i\gamma^j = \begin{pmatrix}0\cdot 0 + \sigma_i\cdot(-\sigma_j) & 0\cdot\sigma_j + \sigma_i\cdot 0 \\ (-\sigma_i)\cdot 0 + 0\cdot(-\sigma_j) & (-\sigma_i)\cdot\sigma_j + 0\cdot 0\end{pmatrix} = \begin{pmatrix}-\sigma_i\sigma_j & 0 \\ 0 & -\sigma_i\sigma_j\end{pmatrix}.$$

The result is block-diagonal, with both diagonal blocks equal to the Pauli product $-\sigma_i\sigma_j$. Swapping $i$ and $j$ and subtracting gives, in each diagonal block, $-\sigma_i\sigma_j - (-\sigma_j\sigma_i) = -[\sigma_i,\sigma_j]$, the negative of the Pauli commutator:

$$[\gamma^i,\gamma^j] = \begin{pmatrix}-[\sigma_i,\sigma_j] & 0 \\ 0 & -[\sigma_i,\sigma_j]\end{pmatrix}.$$

The Pauli commutators are known from [§1](#_1-spin): $[\sigma_i,\sigma_j] = 2i\varepsilon_{ijk}\sigma_k$, where $\varepsilon$ is the totally antisymmetric symbol — $\varepsilon_{123} = 1$, any exchange of two indices changes the sign, and the symbol is zero whenever two indices coincide. Substituting this and packing the two equal diagonal blocks into the block-diagonal matrix $\Sigma^k = \mathrm{diag}(\sigma_k,\sigma_k)$ of [§1](#_1-spin),

$$[\gamma^i,\gamma^j] = -2i\,\varepsilon_{ijk}\,\Sigma^k.$$

The generator multiplies this by $\frac{i}{2}$, and the numerical factor comes out real: $\frac{i}{2}\cdot(-2i) = -i^2 = 1$. Therefore

$$\sigma^{ij} = \frac{i}{2}\,[\gamma^i,\gamma^j] = \varepsilon_{ijk}\,\Sigma^k.$$

In particular $\sigma^{12} = \Sigma^3$, $\sigma^{13} = -\Sigma^2$, and $\sigma^{23} = \Sigma^1$: the generator of each pair points along the one axis not in the pair. Each $\Sigma^k$ is Hermitian, because its two diagonal blocks are the Hermitian matrices $\sigma_k$, and each $\sigma^{ij}$ is a $\Sigma^k$ up to a sign, so all three rotation generators are Hermitian.

Inserting them into the exponent,

$$\Omega_{\text{rot}} = -\frac{i}{2}\left(\omega_{12}\,\Sigma^3 - \omega_{13}\,\Sigma^2 + \omega_{23}\,\Sigma^1\right).$$

The parameters are real numbers, so the parentheses hold a real linear combination of Hermitian matrices, which is itself Hermitian. Multiplying a Hermitian matrix $H$ by $-i$ makes the product anti-Hermitian, because $(-iH)^\dagger = iH = -(-iH)$. And the exponential of an anti-Hermitian matrix is unitary, by the two series properties above: $S^\dagger = e^{\Omega_{\text{rot}}^\dagger} = e^{-\Omega_{\text{rot}}} = S^{-1}$. Rotations are therefore represented by unitary matrices.

One last step turns the three terms into the compact form quoted in the main text. The pair $(1,2)$ mixes the first two spatial coordinates, so it is a rotation about the third axis, and its generator is $\Sigma^3$; cyclically, the pair $(2,3)$ rotates about axis $1$ and the pair $(1,3)$ about axis $2$. Collecting the three parameters into the vector $\boldsymbol\theta = (\omega_{23}, -\omega_{13}, \omega_{12})$ — a rotation in the $xy$-plane, with only $\omega_{12}$ nonzero, has $\boldsymbol\theta = (0,0,\omega_{12})$ — turns the parentheses into the dot product $\boldsymbol\theta\cdot\boldsymbol\Sigma$, and

$$S = \exp\!\left(-\frac{i}{2}\,\boldsymbol\theta\cdot\boldsymbol\Sigma\right),$$

the unitary rotation matrix of the main text.

For a concrete instance, rotate about the $z$-axis through an angle $\theta$, so that $\omega_{12} = \theta$ and $\boldsymbol\theta = (0,0,\theta)$. The result is $S = \exp(-\frac{i\theta}{2}\Sigma^3)$. The matrix $\Sigma^3$ is diagonal — it is two copies of $\sigma_3 = \mathrm{diag}(1,-1)$, so $\Sigma^3 = \mathrm{diag}(1,-1,1,-1)$ — and the exponential of a diagonal matrix is the diagonal matrix of the exponentials of its entries:

$$S = \mathrm{diag}\!\left(e^{-i\theta/2},\, e^{i\theta/2},\, e^{-i\theta/2},\, e^{i\theta/2}\right).$$

Each component picks up a phase, the two spin states opposite phases, and the upper and lower pairs acquire the same phases. Rotating by a full turn, $\theta = 2\pi$, gives $e^{\mp i\pi} = -1$ on every diagonal entry: the spinor returns to itself only up to a sign, which is the double-valuedness announced in [§5](#_5-spinors-transformations). Two full turns are needed to return exactly.

**Boost along $x$.** A boost is a change into a frame that is moving, and it mixes time with the spatial direction of the motion. The boost case does the part the rotation case skipped, which is fixing the numerical value of the parameter, because that value is set by the velocity rather than chosen freely. For motion along $x$, only the pair $(0,1)$ survives: the transformation leaves $y$ and $z$ alone, so the other two boost parameters vanish, and no rotation is mixed in, so all $\omega_{ij}$ vanish too.

First the parameter. If the new frame moves along the $x$-axis with velocity $v$ (in the units of this page, where the speed of light is $1$), the coordinate relations of [Special Relativity](special-relativity.md) are $t' = \gamma(t-vx)$ and $x' = \gamma(x-vt)$, with $\gamma = (1-v^2)^{-1/2}$. It helps to replace $v$ by the rapidity $\varphi$ defined by $v = \tanh\varphi$; then $\gamma = \cosh\varphi$ and $\gamma v = \sinh\varphi$, and the two relations read

$$t' = t\cosh\varphi - x\sinh\varphi, \qquad x' = x\cosh\varphi - t\sinh\varphi.$$

For a slow boost, $\varphi$ is small, and since $\cosh\varphi \approx 1$ and $\sinh\varphi \approx \varphi$, these reduce to $t' \approx t - \varphi x$ and $x' \approx x - \varphi t$. The entries of the Lorentz matrix are the coefficients in these two equations. The entry $\Lambda^0{}_1$ is the coefficient of $x$ in $t'$, namely $-\varphi$; the entry $\Lambda^1{}_0$ is the coefficient of $t$ in $x'$, also $-\varphi$; the diagonal entries are $1$. First order in $\varphi$ is all we need: as noted above, the parameters of composed transformations add, so exponentiating this first-order piece will produce the exact finite boost. Because $\Lambda = \delta + \omega$ with $\delta$ the identity, subtracting the identity leaves the off-diagonal entries as the parameters,

$$\omega^0{}_1 = -\varphi, \qquad \omega^1{}_0 = -\varphi.$$

Lowering the first index by the metric uses only $g_{00} = 1$, since no spatial metric entry meets an index that is $0$, so

$$\omega_{01} = g_{00}\,\omega^0{}_1 = -\varphi.$$

The reduced exponent therefore contains exactly one term:

$$\Omega_{\text{boost}} = -\frac{i}{2}\,\omega_{01}\,\sigma^{01}.$$

Next comes the generator $\sigma^{01} = \frac{i}{2}[\gamma^0,\gamma^1]$, which needs the two products $\gamma^0\gamma^1$ and $\gamma^1\gamma^0$. In the standard representation, $\gamma^0 = \beta = \mathrm{diag}(1,1,-1,-1)$, the block matrix with the $2\times2$ identity and its negative on the diagonal, and $\gamma^1$ is the block matrix computed in the rotation case, $\begin{pmatrix}0 & \sigma_1 \\ -\sigma_1 & 0\end{pmatrix}$. Multiplying the two block by block,

$$\gamma^0\gamma^1 = \begin{pmatrix}1\cdot 0 + 0\cdot(-\sigma_1) & 1\cdot\sigma_1 + 0\cdot 0 \\ 0\cdot 0 + (-1)\cdot(-\sigma_1) & 0\cdot\sigma_1 + (-1)\cdot 0\end{pmatrix} = \begin{pmatrix}0 & \sigma_1 \\ \sigma_1 & 0\end{pmatrix}.$$

The product is exactly the matrix $\alpha_1$ of [§1](#_1-spin), written $\alpha^1$ when its index is up. Reversing the order of the factors gives a product with the off-diagonal blocks negated,

$$\gamma^1\gamma^0 = \begin{pmatrix}0\cdot 1 + \sigma_1\cdot 0 & 0\cdot 0 + \sigma_1\cdot(-1) \\ (-\sigma_1)\cdot 1 + 0\cdot 0 & (-\sigma_1)\cdot 0 + 0\cdot(-1)\end{pmatrix} = \begin{pmatrix}0 & -\sigma_1 \\ -\sigma_1 & 0\end{pmatrix} = -\alpha^1,$$

so the two products differ by a sign, $\gamma^0\gamma^1 = -\gamma^1\gamma^0$ (the matrices anticommute). Therefore

$$[\gamma^0,\gamma^1] = \gamma^0\gamma^1 - \gamma^1\gamma^0 = \alpha^1 - (-\alpha^1) = 2\alpha^1,$$

and feeding the commutator into the definition gives

$$\sigma^{01} = \frac{i}{2}\,[\gamma^0,\gamma^1] = i\,\alpha^1.$$

This generator is not Hermitian, unlike the rotation generators. The matrix $\alpha^1$ has real, symmetric entries — it carries two copies of $\sigma_1 = \begin{pmatrix}0&1\\1&0\end{pmatrix}$ — so $(\alpha^1)^\dagger = \alpha^1$, and the factor of $i$ in front flips the dagger:

$$(\sigma^{01})^\dagger = (i\alpha^1)^\dagger = -i\alpha^1 = -\sigma^{01}.$$

The boost generator is anti-Hermitian.

Now multiply out the exponent. Only the one term survives, and it is

$$\Omega_{\text{boost}} = -\frac{i}{2}\,\omega_{01}\,\sigma^{01} = -\frac{i}{2}\,(-\varphi)\,(i\alpha^1).$$

The operator content is the single matrix $\alpha^1$; everything in front of it is an ordinary complex number, and ordinary numbers commute, so we may multiply the three scalars in any order. Combine the first two first: $-\frac{i}{2}\cdot(-\varphi) = \frac{i\varphi}{2}$, the two minus signs canceling. Then multiply by the third, the $i$ that sits inside the generator: $\frac{i\varphi}{2}\cdot i = \frac{i^2\varphi}{2} = -\frac{\varphi}{2}$. This is where the generator's own factor of $i$ does its work: the $i$ in $\sigma^{01} = i\alpha^1$ multiplies the $i$ in the prefactor $-\frac{i}{2}$ to give $i^2 = -1$, and what looked like an imaginary coefficient turns into the real number $-\varphi/2$. The boost matrix is therefore

$$S = \exp\!\left(-\frac{\varphi}{2}\,\alpha^1\right).$$

Because $\varphi$ is real and $\alpha^1$ is Hermitian, the exponent is a Hermitian matrix, and $S^\dagger = e^{(\text{exponent})^\dagger} = e^{\text{exponent}} = S$: the boost is represented by a Hermitian matrix. It is not unitary, because $S^\dagger S = S^2 = e^{-\varphi\alpha^1}$, which differs from the identity.

Expand the exponential once, because later pages quote its matrix. Since $(\alpha^1)^2 = 1$, the even powers of $\alpha^1$ are the identity and the odd powers are $\alpha^1$ itself, so

$$e^{-\varphi\alpha^1/2} = \underbrace{\Big[1 + \tfrac{(\varphi/2)^2}{2!} + \cdots\Big]}_{\cosh(\varphi/2)} \;-\; \alpha^1\underbrace{\Big[\tfrac{\varphi}{2} + \tfrac{(\varphi/2)^3}{3!} + \cdots\Big]}_{\sinh(\varphi/2)},$$

the same even/odd split that makes $e^x = \cosh x + \sinh x$.

At small velocity the result connects back to [§3](#_3-antiparticles). Keeping only the first term of each series gives $S \approx 1 - \frac{\varphi}{2}\alpha^1$, whose off-diagonal blocks mix the upper and lower pairs of the spinor with relative size $\varphi/2 = v/2$. For a slow particle $|\mathbf p| \approx m|v|$, so this is $|\mathbf p|/2m$ — the size of the small components that [§3](#_3-antiparticles) found by a separate route.

The two cases differ in exactly one place, and the difference survives a change of axis. The rotation result is already axis-free, since $\boldsymbol\theta$ points along whatever axis the rotation uses. For a boost along any unit direction $\hat{\mathbf n}$, the parameters are $\omega_{0k} = -\varphi\,\hat n_k$, and the same block multiplication gives $\sigma^{0k} = i\alpha^k$, so the exponent collects into the real $-\frac{\varphi}{2}\,\boldsymbol\alpha\cdot\hat{\mathbf n}$: $\boldsymbol\alpha\cdot\hat{\mathbf n}$ is again Hermitian and squares to one. Rotations always produce unitary matrices, and boosts always produce Hermitian ones.

## 6. General Solution

The Dirac equation is linear, so the general free solution superposes the four independent solutions per momentum — two spins, two energy signs. In the standard normalization,

$$\psi(x) = \sum_{s=1}^{2} \int \frac{d^3p}{(2\pi\hbar)^3}\,\frac{1}{\sqrt{2E_p}}\left[a_s(p)\,u_s(p)\,e^{-ip\cdot x/\hbar} + b_s^*(p)\,v_s(p)\,e^{+ip\cdot x/\hbar}\right],$$

with $p\cdot x = E_p t - \mathbf p\cdot\mathbf x$. The coefficients $a_s(p)$ and $b_s^*(p)$ are complex numbers here — the amplitudes of the particle and antiparticle branches, fixed by the initial conditions. One note, left for later: in the quantized theory these coefficients are promoted to creation and annihilation operators — $a_s(p)$ annihilates an electron, $b_s^\dagger(p)$ creates a positron — and this expansion becomes the electron field operator. That promotion is the subject of [QFT](qft.md); on this page the coefficients remain numbers. The spinors derived in [§3](#_3-antiparticles), for a spin direction $\chi_s$ ($\chi_\uparrow = (1, 0)^T$, $\chi_\downarrow = (0, 1)^T$),

$$u_s(p) = \begin{pmatrix} \sqrt{E_p + m}\;\chi_s \\ \dfrac{\boldsymbol\sigma\cdot\mathbf p}{\sqrt{E_p + m}}\;\chi_s \end{pmatrix}, \qquad v_s(p) = \begin{pmatrix} -\dfrac{\boldsymbol\sigma\cdot\mathbf p}{\sqrt{E_p + m}}\;\chi_s \\ \sqrt{E_p + m}\;\chi_s \end{pmatrix},$$

reproduce the structure of [Relativistic QM §4](relativistic-qm.md#_4-dirac-equation): for $u$ (positive energy) the upper pair is large at low momentum; for $v$ (negative energy) the roles reverse.

The general solution is where the whole page comes together. The $u$-part carries the particles, the $v$-part the antiparticles of [§3](#_3-antiparticles) and [§4](#_4-negative-energy-solutions); both are dressed with the spin structure of [§1](#_1-spin), and both transform as the spinors of [§5](#_5-spinors-transformations). Why the second coefficient is written conjugated, $b_s^*(p)$: under that promotion a number's complex conjugate becomes an operator's adjoint, $b_s^* \to b_s^\dagger$, the positron creation operator — the notation above is already the shape of the quantized field. That is the bridge to the next stage, [QFT](qft.md).
