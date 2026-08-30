# The Dirac Equation

This page continues from Relativistic QM §4: the Dirac equation $(i\hbar\gamma^\mu\partial_\mu - m)\psi = 0$ with its four-component spinor. The questions that section had to defer — what the extra components are, and what the negative-energy branch means — are taken up here.

## 1. Spin

Relativistic QM §4 deferred the meaning of the spinor's extra components. The identification is now forced by the equation itself. Define the operator

$$\mathbf S = \frac{\hbar}{2}\boldsymbol\Sigma, \qquad \boldsymbol\Sigma = \begin{pmatrix} \boldsymbol\sigma & \mathbf 0 \\ \mathbf 0 & \boldsymbol\sigma \end{pmatrix},$$

the block-diagonal Pauli matrices. Because the $\sigma_i$ satisfy $[\sigma_i, \sigma_j] = 2i\varepsilon_{ijk}\sigma_k$, the components of $\mathbf S$ satisfy

$$[S_i, S_j] = i\hbar\,\varepsilon_{ijk} S_k,$$

the **angular-momentum algebra** — the defining commutation relations of angular momentum, with eigenvalues $\pm\hbar/2$. The extra components are spin, and the equation describes a spin-½ particle.

That the spin is genuinely conserved follows from a short computation: the free Hamiltonian $H = \boldsymbol\alpha\cdot\hat{\mathbf p} + \beta m$ satisfies $[H, \mathbf L] = -[H, \mathbf S]$, so the **total angular momentum**

$$\mathbf J = \mathbf L + \mathbf S$$

commutes with $H$. Neither orbital angular momentum nor spin is separately conserved — the equation's structure mixes them, exactly as a relativistic theory should — but their sum is. The two components of each pair are spin-up and spin-down.

The equation also fixes the magnetic moment. Coupling to an electromagnetic field (minimal substitution $\hat{\mathbf p} \to \hat{\mathbf p} + e\mathbf A$) gives, in the non-relativistic limit, the Pauli equation with

$$\boldsymbol\mu = -\frac{e}{m}\,\mathbf S, \qquad g = 2,$$

Dirac's famous prediction: the electron's gyromagnetic ratio is twice the classical value. This answers the first deferred question of Relativistic QM §4 — the extra components are the two spin states of a spin-½ particle, and their transformation properties are the subject of §4 below.

## 2. Antiparticles

The second deferred question: the negative-energy branch. The key new fact comes from a symmetry of the equation itself. Taking the complex conjugate of the Dirac equation and multiplying by a suitable matrix $\eta$ (in the standard representation $\eta = i\gamma^2$) gives a solution of the same form with opposite charge — the **charge-conjugated spinor**

$$\psi_c = \eta\,\psi^*.$$

If $\psi$ describes a particle of charge $e$, then $\psi_c$ describes one of charge $-e$: the Dirac equation is invariant under charge conjugation. The negative-frequency solutions are therefore not redundant — they are the wave functions of a particle with the same mass and opposite charge, the **antiparticle**. Together with the Stückelberg–Feynman reading of Relativistic QM §3 — negative-frequency waves propagating backward in time — this is the physics of the positron, predicted by the equation and discovered in 1932, six years later.

What cannot be done at this level: making this precise requires particles to be created and destroyed, which a single-particle wave function cannot describe. The statement that survives at this level is that the Dirac equation has room in its mathematics for both particles and antiparticles — the positive-frequency and negative-frequency parts of its solutions — and that both are physical.

## 3. Negative Energy Solutions

Look directly at the negative-energy branch. Plane waves of the Dirac equation come in two families,

$$\psi_+ = u_s(p)\,e^{-ip\cdot x/\hbar} \quad (E = +E_p), \qquad \psi_- = v_s(p)\,e^{+ip\cdot x/\hbar} \quad (E = -E_p),$$

with $E_p = +\sqrt{\mathbf p^2 + m^2}$; the $v$-spinors are the negative-energy solutions, written with a positive-frequency phase by convention.

The problem they pose is the sharpened one of Relativistic QM §4: both branches carry positive density $\psi^\dagger\psi$, so nothing marks a negative-energy state as unphysical, and the energy is unbounded below — an interacting electron could radiate energy forever, falling through negative levels. Dirac's resolution was the **hole theory**. The vacuum is not empty; every negative-energy state is occupied — a filled sea of electrons, which the Pauli exclusion principle protects from further occupancy. A missing electron in the sea then behaves as a positive-energy particle of positive charge: a **hole**, the positron. When an electron falls from a negative level into a hole, both disappear — the radiation emitted is pair annihilation; the reverse process is pair creation.

Two honest caveats, in the spirit of the previous pages: the sea picture leans on fermionic statistics (the exclusion principle), and on a many-particle vacuum — both belong to the quantized theory, where the hole picture is replaced by creation and annihilation operators acting on the vacuum. What the single-particle equation contributes is definitive: negative-energy solutions exist, they carry opposite charge (§2), and their interpretation is the doorway to field theory.

## 4. Spinors (Transformations)

The four-component object transforms differently from anything encountered so far. Under a Lorentz transformation $x' = \Lambda x$, the spinor transforms as

$$\psi'(x') = S(\Lambda)\,\psi(x), \qquad S(\Lambda) = \exp\!\left(-\frac{i}{4}\,\omega_{\mu\nu}\sigma^{\mu\nu}\right), \qquad \sigma^{\mu\nu} = \frac{i}{2}\,[\gamma^\mu, \gamma^\nu],$$

where $\omega_{\mu\nu}$ are the boost/rotation parameters. Three features set $S$ apart from the transformations of vectors and scalars:

1. **Finite-dimensional.** $S(\Lambda)$ is a $4 \times 4$ matrix — a finite-dimensional representation of the Lorentz group — whereas the familiar transformations on functions (rotations of $\psi(\mathbf x)$) are infinite-dimensional. The spinor representation is a genuinely new structure.
2. **Double-valued.** A rotation by $2\pi$ gives $S = -\mathbb{1}$: the spinor returns to itself only up to a sign. A $4\pi$ rotation is needed to return exactly. No scalar or vector does this; the minus sign is the signature of spin-½.
3. **Reducible.** The $4 \times 4$ representation splits into two $2 \times 2$ pieces, $(\tfrac{1}{2}, 0) \oplus (0, \tfrac{1}{2})$ — the two two-component pieces are the **Weyl spinors**, which transform under rotations identically (the $\boldsymbol\Sigma/2$ of §1) and under boosts oppositely. They are the left- and right-handed parts of the Dirac spinor.

For rotations alone, $S = \exp\!\left(-\tfrac{i}{2}\,\boldsymbol\theta\cdot\boldsymbol\Sigma\right)$ — the spin operator of §1 as the generator, confirming from the transformation side that the extra components carry angular momentum $\hbar/2$.

## 5. General Solution

The Dirac equation is linear, so the general free solution superposes the four independent solutions per momentum — two spins, two energy signs. In the standard normalization,

$$\psi(x) = \sum_{s=1}^{2} \int \frac{d^3p}{(2\pi\hbar)^3}\,\frac{1}{\sqrt{2E_p}}\left[a_s(p)\,u_s(p)\,e^{-ip\cdot x/\hbar} + b_s^*(p)\,v_s(p)\,e^{+ip\cdot x/\hbar}\right],$$

with $p\cdot x = E_p t - \mathbf p\cdot\mathbf x$. The spinors, for a spin direction $\chi_s$ ($\chi_\uparrow = (1, 0)^T$, $\chi_\downarrow = (0, 1)^T$),

$$u_s(p) = \begin{pmatrix} \sqrt{E_p + m}\;\chi_s \\ \dfrac{\boldsymbol\sigma\cdot\mathbf p}{\sqrt{E_p + m}}\;\chi_s \end{pmatrix}, \qquad v_s(p) = \begin{pmatrix} \dfrac{\boldsymbol\sigma\cdot\mathbf p}{\sqrt{E_p + m}}\;\chi_s \\ \sqrt{E_p + m}\;\chi_s \end{pmatrix},$$

reproduce the structure of Relativistic QM §4: for $u$ (positive energy) the upper pair is large at low momentum; for $v$ (negative energy) the roles reverse.

The general solution is where the whole page comes together. The $u$-part carries the particles, the $v$-part the antiparticles of §2 and §3; both are dressed with the spin structure of §1, and both transform as the spinors of §4. The coefficients $a_s(p)$ and $b_s^*(p)$ are complex numbers here — in the quantized theory they become the creation and annihilation operators of the electron and positron fields. That is the bridge to the next stage.
