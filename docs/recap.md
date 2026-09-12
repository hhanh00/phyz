# Final Recap

We use **natural units** $c=\hbar=1$ throughout.

## Classical System
- Given the force laws and suitable initial position and velocity, the equations determine future and past motion wherever a unique solution exists.
- **Newtonian Formulation**
  - For a constant-mass particle in an inertial frame, $\mathbf F = m\mathbf a$.
  - Tracking forces and constraints can become cumbersome in complicated systems.
  - The vector law does not depend on a particular choice of Cartesian axes; its component expressions depend on the coordinates used.
- **Lagrangian Formulation**
  - For ordinary particles with standard kinetic energy and a velocity-independent potential, $L = K - V$. More general systems can require other forms of $L$.
  - **Action**: $S = \int_{t_i}^{t_f} L(q,\dot q,t)\,dt$.
  - Physical trajectories make the **action stationary**: $\delta S = 0$. A stationary point need not be a minimum or maximum.
  - Stationary action gives the **Euler–Lagrange equations**: $\dfrac{d}{dt}\dfrac{\partial L}{\partial \dot q_i}-\dfrac{\partial L}{\partial q_i}=0$.
  - The usual variational derivation fixes the endpoint positions. These are boundary conditions for the variation, not initial conditions for predicting motion; we normally solve the resulting equations using initial positions and velocities.
  - We choose **generalized coordinates** and encode the dynamics in $L$, often avoiding explicit constraint forces.
- **Hamiltonian Formulation**
  - Define the **canonical momenta** $p_i = \partial L / \partial \dot q_i$. When these relations can be inverted for the velocities, use $(q_i,p_i)$ as phase-space coordinates.
  - The Hamiltonian is $H(q,p,t) = \sum_i p_i\dot q_i - L$, with the velocities expressed in terms of $q,p,t$. For standard kinetic energy and a velocity-independent potential in time-independent coordinates, $H = K + V$; this equality is not universal.
  - For each degree of freedom, replace a second-order ordinary differential equation with two first-order ordinary differential equations: $\dot q_i = \partial H / \partial p_i$ and $\dot p_i = -\partial H / \partial q_i$.
  - The system follows a trajectory in $(q,p)$ **phase space**. Along that trajectory, $dH/dt = \partial H/\partial t$, so $H$ stays constant when it has no explicit time dependence.
## Quantum System
- A quantum state generally predicts a distribution of measurement outcomes. Position and momentum cannot both have arbitrarily sharp distributions. An isolated state's evolution under the Schrödinger equation is deterministic, even though individual measurement outcomes are generally probabilistic.
- A **pure state** is represented by a normalized vector $|\phi\rangle$, up to an overall phase. A single measurement does not reveal that entire vector; mixed states require density operators.
- Observables are **self-adjoint linear operators** (Hermitian matrices in finite dimensions), so their possible measured values are real.
- A linear operator maps vectors in its domain to vectors. Its output need not be normalized and can be zero, so it is not automatically another physical state.
- An **eigenvector** satisfies $\hat A|a_n\rangle = a_n|a_n\rangle$: the operator maps the nonzero vector to a scalar multiple of itself, and $a_n$ is its **eigenvalue**. General operators can have complex eigenvalues, but self-adjoint observables have real ones.
- For an observable with a discrete orthonormal eigenbasis, expand the state itself as $|\phi\rangle = \sum_n c_n|a_n\rangle$, where $c_n = \langle a_n|\phi\rangle$.
- For a nondegenerate eigenvalue $a_n$, the probability of measuring it is $|c_n|^2$. The coefficient $c_n$ is a **probability amplitude**. For a degenerate eigenvalue, sum $|c_n|^2$ over an orthonormal basis of its eigenspace.
- Applying $\hat A$ to a state is not a model of performing a measurement. In an **ideal projective measurement**, the observed outcome selects an eigenspace, and projection followed by normalization gives the conditional state after measurement.
- Useful examples of observables:
  - **Position:** possible outcomes are positions in space. In the position representation, $(\hat x\phi)(x) = x\phi(x)$.
  - **Momentum:** possible outcomes are momenta. In the position representation for a particle on a line, $(\hat p\phi)(x) = -i\,\partial_x\phi(x)$.
- The **wavefunction** $\phi(x) = \langle x|\phi\rangle$ expresses the state in the position basis. It is not the result of applying $\hat x$ to the state.
- The **momentum-space wavefunction** $\tilde\phi(p) = \langle p|\phi\rangle$ expresses the same state in a different basis. A **Fourier transform** relates these two wavefunctions.
- Position and momentum on an infinite line have continuous spectra and use generalized eigenstates. Here $|\phi(x)|^2$ is a **probability density**: the probability of finding the particle in a region $R$ is $\int_R |\phi(x)|^2\,dx$.
- **Evolution of a quantum system**
  - The initial state determines how an isolated system evolves, so we usually study its time dependence.
  - The **Schrödinger equation** governs the time evolution of the state: $i\partial_t|\phi(t)\rangle=\hat H|\phi(t)\rangle$.
- **Harmonic Oscillator**
  - Important model system and the basis for **ladder-operator quantization**
  - Restoring force proportional to displacement: $F=-kx$
  - Potential energy is quadratic about equilibrium: $V(x)=\tfrac12kx^2$
  - Hamiltonian: $H(x,p)=\dfrac{p^2}{2m}+\dfrac12m\omega^2x^2$, where $k=m\omega^2$
  - Constant-energy trajectories are ellipses in ordinary $(x,p)$ phase space and circles after rescaling the axes
  - Quantization promotes $x$ and $p$ to operators satisfying $[\hat x,\hat p]=i$. Define

    $$
    \hat a=\sqrt{\frac{m\omega}{2}}\,\hat x
    +\frac{i}{\sqrt{2m\omega}}\,\hat p,
    \qquad
    \hat a^\dagger=\sqrt{\frac{m\omega}{2}}\,\hat x
    -\frac{i}{\sqrt{2m\omega}}\,\hat p,
    $$

    which obey $[\hat a,\hat a^\dagger]=1$.
  - With the **number operator** $\hat N=\hat a^\dagger\hat a$,

    $$
    \hat H=\omega\left(\hat N+\frac12\right).
    $$

    The ground state satisfies $\hat a|0\rangle=0$, and the normalized number states are $|n\rangle=(\hat a^\dagger)^n|0\rangle/\sqrt{n!}$.
  - The ladder operators act as

    $$
    \hat a|n\rangle=\sqrt n\,|n-1\rangle,
    \qquad
    \hat a^\dagger|n\rangle=\sqrt{n+1}\,|n+1\rangle,
    $$

    giving the discrete spectrum $E_n=\omega(n+\tfrac12)$. The ground state therefore has nonzero **zero-point energy** $E_0=\omega/2$.
- **First Quantization**
  - In **canonical quantization**, promote position and momentum to operators satisfying $[\hat x,\hat p]=i$, then construct the Hamiltonian operator $\hat H$ from them.
  - Products involving noncommuting variables can introduce **operator-ordering ambiguities**.
- **Special Relativity**
  - Particle physics often involves particles moving near the speed of light, so relativistic effects must be included.
  - **Lorentz transformations** relate spacetime coordinates in different inertial frames with a common origin.
  - For a boost with relative velocity $v$ along the $x$ direction,

    $$
    t'=\gamma(t-vx),
    \qquad
    x'=\gamma(x-vt),
    \qquad
    y'=y,
    \qquad
    z'=z,
    \qquad
    \gamma=\frac{1}{\sqrt{1-v^2}}.
    $$

    The inverse boost is obtained by replacing $v\to-v$. Unlike a Galilean transformation, a Lorentz boost mixes space and time and preserves the speed of light.
  - The **Minkowski metric** with signature $(+,-,-,-)$ gives the **invariant spacetime interval squared**: $\Delta s^2 = (\Delta t)^2 - |\Delta \mathbf{x}|^2$.
  - Energy and three-momentum form the **four-momentum** $p^\mu = (E,\mathbf p)$, which transforms as a four-vector under Lorentz transformations.
  - Under the same boost,

    $$
    E'=\gamma(E-vp_x),
    \qquad
    p_x'=\gamma(p_x-vE),
    \qquad
    p_y'=p_y,
    \qquad
    p_z'=p_z.
    $$

  - Its invariant squared norm is $p^\mu p_\mu = E^2 - |\mathbf p|^2 = m^2$, where $m$ is the **rest mass**.
- **Klein–Gordon Equation**
  - The Klein–Gordon equation follows from the relativistic **energy–momentum relation** $E^2=|\mathbf p|^2+m^2$ by substituting $E\to i\partial_t$ and $\mathbf p\to-i\nabla$, giving $(\partial_t^2-\nabla^2+m^2)\phi=0$.
  - Has positive- and negative-frequency plane-wave solutions, with $E=\pm\sqrt{|\mathbf p|^2+m^2}$. In quantum field theory, these are interpreted through particle and antiparticle modes with positive physical energies. For a real scalar field, the particle is its own antiparticle.
  - Is **second order in time**, so specifying a solution requires both $\phi$ and $\partial_t\phi$ initially.
  - Its conserved density is **not positive definite**, so it cannot serve as an ordinary position probability density. For a complex field, it is interpreted as a **charge density**.
  - Describes spin-0 fields; particles with other spins require different field equations.
- **Plane-Wave Solutions**
  - A free particle with definite momentum has a plane wave $\psi(t,\mathbf x)=A e^{i(\mathbf p\cdot\mathbf x-Et)}=A e^{i(\mathbf k\cdot\mathbf x-\omega t)}$, where $\mathbf p=\mathbf k$ and $E=\omega$ in natural units.
  - **Nonrelativistic:** this solves the free Schrödinger equation $i\partial_t\psi=-\frac{1}{2m}\nabla^2\psi$ when the kinetic energy is $E=|\mathbf p|^2/(2m)$. The corresponding relativistic total energy has the low-momentum expansion $E_{\mathrm{rel}}\approx m+|\mathbf p|^2/(2m)$.
  - **Relativistic:** a free scalar field has plane-wave solutions $\phi(x)=A e^{-ip_\mu x^\mu}$, where $x^\mu=(t,\mathbf x)$ and $p_\mu x^\mu=Et-\mathbf p\cdot\mathbf x$ is Lorentz invariant. These solve the Klein–Gordon equation when $E^2=|\mathbf p|^2+m^2$.
  - A single plane wave extends throughout space and is not square-normalizable on infinite space; superpositions can form localized, normalizable **wave packets**.
- **Free Dirac Equation**
  - The Dirac equation factorizes the Klein–Gordon operator using **gamma matrices**, which satisfy the Clifford algebra $\{\gamma^\mu,\gamma^\nu\}=2\eta^{\mu\nu}I$.
  - Is **first order in time and space**: $(i\gamma^\mu\partial_\mu-m)\psi=0$.
  - Applying $(i\gamma^\mu\partial_\mu+m)$ shows that the free Dirac equation implies $(\Box+m^2)\psi=0$, where $\Box=\partial_t^2-\nabla^2$. Thus each spinor component satisfies the Klein–Gordon equation, and plane-wave solutions satisfy $E^2=|\mathbf p|^2+m^2$. The Klein–Gordon equation alone does not imply the Dirac equation.
  - Has a **nonnegative conserved probability density** $\rho=\psi^\dagger\psi$ in the single-particle interpretation.
  - Describes spin-$\tfrac12$ particles.
  - Still has positive- and negative-energy solutions; quantum field theory interprets these through particles and antiparticles with positive physical energies.
  - **General solution**
    - Because the free Dirac equation is linear, its general solution is a superposition of all momentum, spin, and frequency modes:

      $$
      \psi(x)=\sum_{s=1}^{2}\int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}
      \left[a_s(\mathbf p)u_s(\mathbf p)e^{-ip\cdot x}
      +b_s^*(\mathbf p)v_s(\mathbf p)e^{+ip\cdot x}\right],
      \qquad E_{\mathbf p}=\sqrt{|\mathbf p|^2+m^2}.
      $$

    - Here $p\cdot x=E_{\mathbf p}t-\mathbf p\cdot\mathbf x$. The $u_s$ terms are positive-frequency modes and the $v_s$ terms are negative-frequency modes, with two spin labels $s=1,2$ for each momentum.
    - For a classical Dirac field, $a_s(\mathbf p)$ and $b_s^*(\mathbf p)$ are numerical amplitudes fixed by the initial field. In quantum field theory they become electron-annihilation and positron-creation operators, respectively.
    - The field is therefore a superposition of independent momentum–spin modes. After quantization, each mode behaves as a **fermionic oscillator**, governed by anticommutation relations rather than the commutation relations of an ordinary bosonic harmonic oscillator.
  - **Spin**
    - Spin is **intrinsic angular momentum** associated with how the Dirac spinor transforms under rotations; it is not literal rotation of a particle. Angular momentum conservation reveals why orbital angular momentum alone is insufficient.
    - For the free Dirac Hamiltonian $H=\boldsymbol\alpha\cdot\mathbf p+\beta m$, with $\alpha^i=\gamma^0\gamma^i$ and $\beta=\gamma^0$, orbital angular momentum $\mathbf L=\mathbf x\times\mathbf p$ is not separately conserved: $[H,L_i]\ne0$ in general.
    - **Spin operator**: $\mathbf S=\tfrac12\boldsymbol\Sigma$, where in the Dirac representation $\Sigma_i=\begin{pmatrix}\sigma_i&0\\0&\sigma_i\end{pmatrix}$ and $\sigma_i$ are the **Pauli matrices**. It obeys $[S_i,S_j]=i\epsilon_{ijk}S_k$ and $\mathbf S^2=\tfrac34 I$, corresponding to spin $s=\tfrac12$.
    - **Total angular momentum** $\mathbf J=\mathbf L+\mathbf S$ is conserved: $[H,J_i]=0$. More precisely, the two commutators cancel, $[H,L_i]+[H,S_i]=0$, although neither $\mathbf L$ nor $\mathbf S$ is separately conserved in general.
    - Along the $z$ axis, the two-component spin basis is $\chi_+=\begin{pmatrix}1\\0\end{pmatrix}$ and $\chi_-=\begin{pmatrix}0\\1\end{pmatrix}$, with $(\sigma_z/2)\chi_\pm=\pm\tfrac12\chi_\pm$.
    - **Positive-frequency spinor solutions** have the form $\psi_s(x)=u_s(\mathbf p)e^{-ip_\mu x^\mu}$, where $E=\sqrt{|\mathbf p|^2+m^2}$ and $(\gamma^\mu p_\mu-m)u_s=0$.
    - For $m>0$, in the Dirac representation one choice is $u_s(\mathbf p)=\sqrt{E+m}\begin{pmatrix}\chi_s\\\dfrac{\boldsymbol\sigma\cdot\mathbf p}{E+m}\chi_s\end{pmatrix}$, normalized so that $u_s^\dagger u_s=2E$. The label $s=\pm$ specifies the rest-frame spin projection; a moving spinor need not be an eigenvector of $S_z$.
    - **Negative-frequency solutions** are $\psi_s(x)=v_s(\mathbf p)e^{+ip_\mu x^\mu}$ with $E>0$ and $(\gamma^\mu p_\mu+m)v_s=0$. In quantum field theory, these modes enter the antiparticle part of the field.
    - A Dirac spinor has four components, but the free equation leaves **two independent spin states** for each energy branch. Under a $2\pi$ spatial rotation, a spinor changes sign; it returns to itself after $4\pi$.

## Classical Field to Quantum Field

- A **classical field** assigns a number, vector, or spinor to every spacetime point. Examples include a scalar field $\phi(x)$, the electromagnetic field $A^\mu(x)$, and a Dirac spinor $\psi(x)$.
- Its dynamics follow from an action $S=\int d^4x\,\mathcal L$. Stationary action gives the field Euler–Lagrange equation

  $$
  \partial_\mu\!\left(\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\right)
  -\frac{\partial\mathcal L}{\partial\phi}=0.
  $$

- A free field obeys a linear equation, so it can be decomposed into independent **Fourier modes**. For a free scalar field, each momentum mode satisfies

  $$
  \ddot\phi_{\mathbf p}(t)+E_{\mathbf p}^2\phi_{\mathbf p}(t)=0,
  \qquad E_{\mathbf p}=\sqrt{|\mathbf p|^2+m^2},
  $$

  which has the same form as a harmonic oscillator with frequency $E_{\mathbf p}$.
- **Canonical field quantization** promotes the classical field $\phi(t,\mathbf x)$ and its conjugate momentum $\pi(t,\mathbf x)=\partial\mathcal L/\partial\dot\phi$ to operators with the equal-time relation

  $$
  [\hat\phi(t,\mathbf x),\hat\pi(t,\mathbf y)]=i\delta^3(\mathbf x-\mathbf y).
  $$

- Equivalently, promote each mode amplitude to creation and annihilation operators. A free real scalar field becomes

  $$
  \hat\phi(x)=\int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}
  \left(\hat a_{\mathbf p}e^{-ip\cdot x}+\hat a_{\mathbf p}^\dagger e^{+ip\cdot x}\right),
  $$

  with $[\hat a_{\mathbf p},\hat a_{\mathbf q}^\dagger]=(2\pi)^3\delta^3(\mathbf p-\mathbf q)$.
- The **vacuum** $|0\rangle$ satisfies $\hat a_{\mathbf p}|0\rangle=0$. Acting with $\hat a_{\mathbf p}^\dagger$ creates one particle of momentum $\mathbf p$ and energy $E_{\mathbf p}$; repeated creation operators build multiparticle **Fock states**.
- The free-field Hamiltonian is a sum of oscillator Hamiltonians. In a finite box with discrete momenta, it has the schematic form $\hat H=\sum_{\mathbf p}E_{\mathbf p}(\hat N_{\mathbf p}+\tfrac12)$. The $\tfrac12E_{\mathbf p}$ terms make up the vacuum energy, and each excitation above the vacuum is one particle quantum of a field mode.
- Bosonic fields use **commutators** and permit any occupation number. Dirac fields use **anticommutators**, so each momentum–spin particle or antiparticle mode can have occupation number only $0$ or $1$.
- In a free theory the momentum modes evolve independently. **Interactions** couple the fields and allow quanta to be created, destroyed, or scattered while conserving the symmetries' associated quantities.

### Free Lagrangian Densities

- **Real scalar field — Klein–Gordon**

  $$
  \mathcal L_{\mathrm{KG}}
  =\frac12\partial_\mu\phi\,\partial^\mu\phi-\frac12m^2\phi^2.
  $$

  The Euler–Lagrange equation is $(\Box+m^2)\phi=0$. After quantization, the field describes neutral spin-$0$ bosons; a real scalar particle is its own antiparticle. A complex scalar field instead uses $\mathcal L=\partial_\mu\phi^*\partial^\mu\phi-m^2\phi^*\phi$ and can carry a conserved charge.

- **Dirac field**

  $$
  \mathcal L_{\mathrm D}=\bar\psi(i\gamma^\mu\partial_\mu-m)\psi,
  \qquad \bar\psi=\psi^\dagger\gamma^0.
  $$

  Varying $\bar\psi$ gives $(i\gamma^\mu\partial_\mu-m)\psi=0$; varying $\psi$ gives the adjoint Dirac equation. After quantization, $\psi$ describes spin-$\tfrac12$ fermions and $\bar\psi$ is its Dirac adjoint. Particle and antiparticle modes obey anticommutation relations.

- **Electromagnetic field — Maxwell**

  $$
  \mathcal L_{\mathrm M}=-\frac14F_{\mu\nu}F^{\mu\nu},
  \qquad F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu.
  $$

  The Euler–Lagrange equation is the source-free Maxwell equation $\partial_\mu F^{\mu\nu}=0$. The Lagrangian is invariant under the **gauge transformation** $A_\mu\to A_\mu+\partial_\mu\Lambda$. After quantization, the field describes massless spin-$1$ photons with two physical transverse polarizations.

- Adding an external conserved current gives the interaction term $\mathcal L_{\mathrm{int}}=-j_\mu A^\mu$ and changes Maxwell's equation to $\partial_\mu F^{\mu\nu}=j^\nu$.
- Each free Lagrangian is **quadratic in its field**, so its equation of motion is linear and its momentum modes evolve independently. Interaction terms contain products of fields and couple those modes.

### Fermion and Photon Quantization

- Quantizing the Dirac field promotes its mode amplitudes to operators:

  $$
  \hat\psi(x)=\sum_{s=1}^{2}\int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}
  \left[
  \hat a_s(\mathbf p)u_s(\mathbf p)e^{-ip\cdot x}
  +\hat b_s^\dagger(\mathbf p)v_s(\mathbf p)e^{+ip\cdot x}
  \right].
  $$

  Here $\hat a_s$ annihilates a fermion and $\hat b_s^\dagger$ creates its antifermion.
- Fermionic modes obey **canonical anticommutation relations**:

  $$
  \{\hat a_s(\mathbf p),\hat a_{s'}^\dagger(\mathbf q)\}
  =(2\pi)^3\delta_{ss'}\delta^3(\mathbf p-\mathbf q),
  $$

  $$
  \{\hat b_s(\mathbf p),\hat b_{s'}^\dagger(\mathbf q)\}
  =(2\pi)^3\delta_{ss'}\delta^3(\mathbf p-\mathbf q),
  $$

  with all other anticommutators zero. Consequently, $(\hat a_s^\dagger)^2=(\hat b_s^\dagger)^2=0$ for a fixed mode, implementing the Pauli exclusion principle and restricting each mode's occupation to $0$ or $1$.
- The vacuum satisfies $\hat a_s(\mathbf p)|0\rangle=\hat b_s(\mathbf p)|0\rangle=0$. The operators $\hat a_s^\dagger$ and $\hat b_s^\dagger$ create particle and antiparticle states. After normal ordering, the free Hamiltonian is a sum of positive-energy particle and antiparticle number operators.
- The Maxwell field has gauge redundancy, so its four potential components do not represent four physical photon polarizations. For external physical photons, one may use the transverse-mode expansion

  $$
  \hat A_\mu(x)=\sum_{\lambda=1}^{2}\int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2|\mathbf p|}}
  \left[
  \hat a_\lambda(\mathbf p)\epsilon_\mu^{(\lambda)}(\mathbf p)e^{-ip\cdot x}
  +\hat a_\lambda^\dagger(\mathbf p)\epsilon_\mu^{(\lambda)*}(\mathbf p)e^{+ip\cdot x}
  \right],
  $$

  where $p^0=|\mathbf p|$ and $\lambda=1,2$ labels the two physical polarizations.
- Photon operators obey bosonic commutation relations,

  $$
  [\hat a_\lambda(\mathbf p),\hat a_{\lambda'}^\dagger(\mathbf q)]
  =(2\pi)^3\delta_{\lambda\lambda'}\delta^3(\mathbf p-\mathbf q),
  $$

  so any number of photons may occupy the same mode.
- Covariant perturbation theory adds the gauge-fixing term

  $$
  \mathcal L_{\mathrm{gf}}=-\frac{1}{2\xi}(\partial_\mu A^\mu)^2.
  $$

  In Feynman gauge, $\xi=1$, the internal photon propagator is $-ig_{\mu\nu}/(p^2+i\epsilon)$. Four formal components appear internally, but gauge invariance ensures that only the two physical transverse polarizations contribute to observable external photon states.

- The rest of the recap builds the **Standard Model Lagrangian** from matter- and gauge-field kinetic terms, gauge interactions, the Higgs sector, and Yukawa interactions. After electroweak symmetry breaking, the Higgs and Yukawa terms generate masses for the massive gauge bosons and fermions.

## Electromagnetic Field and QED

- The free Dirac and Maxwell Lagrangians describe electrons and photons propagating independently. **Quantum electrodynamics (QED)** adds the interaction between them.
- **Global $U(1)$ symmetry:** the free Dirac Lagrangian is invariant under a constant phase rotation

  $$
  \psi\to e^{i\alpha}\psi,
  \qquad \bar\psi\to e^{-i\alpha}\bar\psi.
  $$

  Noether's theorem associates this symmetry with the conserved electric current $j^\mu=q\bar\psi\gamma^\mu\psi$, satisfying $\partial_\mu j^\mu=0$. Its conserved charge is $Q=\int d^3x\,j^0$.
- **Local $U(1)$ symmetry:** if the phase becomes position dependent, $\alpha\to\alpha(x)$, differentiating $e^{i\alpha(x)}\psi$ produces an extra term, so the ordinary derivative does not transform covariantly.
- Introduce the electromagnetic **gauge field** $A_\mu$ and the **covariant derivative**

  $$
  D_\mu=\partial_\mu+iqA_\mu.
  $$

  Under

  $$
  \psi\to e^{i\alpha(x)}\psi,
  \qquad A_\mu\to A_\mu-\frac1q\partial_\mu\alpha,
  $$

  the covariant derivative transforms as $D_\mu\psi\to e^{i\alpha(x)}D_\mu\psi$. The gauge field compensates for the position-dependent phase.
- The **field strength**

  $$
  F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu
  $$

  is gauge invariant. The term $-\tfrac14F_{\mu\nu}F^{\mu\nu}$ supplies the gauge field's dynamics and gives Maxwell's equations.
- The complete QED Lagrangian is

  $$
  \mathcal L_{\mathrm{QED}}
  =-\frac14F_{\mu\nu}F^{\mu\nu}
  +\bar\psi(i\gamma^\mu D_\mu-m)\psi.
  $$

  Expanding $D_\mu$ separates it into

  $$
  \mathcal L_{\mathrm{QED}}
  =\underbrace{-\frac14F_{\mu\nu}F^{\mu\nu}}_{\text{free photon}}
  +\underbrace{\bar\psi(i\gamma^\mu\partial_\mu-m)\psi}_{\text{free electron/positron}}
  \underbrace{-q\bar\psi\gamma^\mu\psi A_\mu}_{\text{interaction}}.
  $$

- The interaction is $\mathcal L_{\mathrm{int}}=-j^\mu A_\mu$. It allows a charged fermion to emit or absorb a photon and gives the QED vertex factor $-iq\gamma^\mu$. Charge and four-momentum are conserved at each vertex.
- Because $U(1)$ is Abelian, $F_{\mu\nu}$ contains no terms quadratic in $A_\mu$; therefore QED has no elementary photon-only interaction vertex. Photons can still scatter indirectly through charged-particle loops.
- A photon mass term $m_\gamma^2A_\mu A^\mu/2$ is not gauge invariant, so unbroken electromagnetic $U(1)$ requires the photon to be massless. Quantizing $A_\mu$ leaves two physical transverse photon polarizations.

## Weak Interaction

- Experiments such as beta decay show that the weak interaction violates **parity**, which reverses spatial coordinates and momenta: $\mathbf x\to-\mathbf x$ and $\mathbf p\to-\mathbf p$. Spin is unchanged under parity, so the correlation $\mathbf S\cdot\mathbf p$ changes sign. The observed asymmetry means the weak interaction distinguishes left from right.
- Define

  $$
  \gamma^5=i\gamma^0\gamma^1\gamma^2\gamma^3,
  \qquad
  P_L=\frac{1-\gamma^5}{2},
  \qquad
  P_R=\frac{1+\gamma^5}{2}.
  $$

  These **chiral projectors** satisfy $P_L^2=P_L$, $P_R^2=P_R$, $P_LP_R=0$, and $P_L+P_R=1$. They split a Dirac field into $\psi_L=P_L\psi$ and $\psi_R=P_R\psi$.
- **Chirality** is a Lorentz-transformation property of a spinor and is distinct from spin projection. For massless particles it agrees with helicity; for massive particles, a state of definite helicity generally contains both chiralities.
- The charged weak interaction couples only to **left-chiral fermion fields**. A left-chiral neutrino field annihilates negative-helicity neutrinos and creates positive-helicity antineutrinos in the massless limit. There is no corresponding right-chiral charged current.
- For the electron and electron neutrino, the left-chiral current and its conjugate are

  $$
  j_\ell^\mu=\bar e_L\gamma^\mu\nu_{eL}
  =\bar e\gamma^\mu P_L\nu_e,
  \qquad
  (j_\ell^\mu)^\dagger=\bar\nu_{eL}\gamma^\mu e_L.
  $$

  The analogous quark current $\bar u_L\gamma^\mu d_L$ changes a down quark into an up quark. These currents account for the species changes in beta decay.
- Group the left-chiral fields into **weak-isospin doublets**

  $$
  L=\begin{pmatrix}\nu_{eL}\\e_L\end{pmatrix},
  \qquad
  Q=\begin{pmatrix}u_L\\d_L\end{pmatrix}.
  $$

  A global $SU(2)$ transformation acts as $L\to UL$, where $U=\exp(i\alpha^aT^a)$ and $T^a=\sigma^a/2$. The Pauli matrices here mix the two species in a doublet; they do not act on spin.
- Making the symmetry local, $U\to U(x)$, requires one gauge field for each of the three $SU(2)$ generators. Define

  $$
  D_\mu=\partial_\mu+igW_\mu^aT^a,
  $$

  where $g$ is the weak coupling and $W_\mu^1,W_\mu^2,W_\mu^3$ are the three gauge fields. Because this symmetry acts on left-chiral doublets, it is called $SU(2)_L$; right-chiral charged fermions are $SU(2)_L$ singlets.
- The combinations

  $$
  W_\mu^\pm=\frac{W_\mu^1\mp iW_\mu^2}{\sqrt2}
  $$

  are the charged weak fields. The third field $W_\mu^3$ is neutral. Before electroweak mixing, $W^3$ is not yet the physical $Z$ boson or photon.
- Expanding the covariant derivative gives the lepton interaction

  $$
  \begin{aligned}
  \mathcal L_{\mathrm{int}}={}&-\frac{g}{\sqrt2}
  \left(\bar\nu_{eL}\gamma^\mu e_LW_\mu^+
  +\bar e_L\gamma^\mu\nu_{eL}W_\mu^-\right)\\
  &-\frac g2\left(
  \bar\nu_{eL}\gamma^\mu\nu_{eL}
  -\bar e_L\gamma^\mu e_L\right)W_\mu^3.
  \end{aligned}
  $$

  The first line contains the **charged-current interactions**, which exchange an electron and neutrino through $W^\pm$. The second line is the neutral $SU(2)_L$ interaction; electroweak mixing later turns the neutral gauge fields into the physical $Z$ and photon.
- The $SU(2)$ field strength and gauge-field kinetic term are

  $$
  W_{\mu\nu}^a=\partial_\mu W_\nu^a-\partial_\nu W_\mu^a
  -g\epsilon^{abc}W_\mu^bW_\nu^c,
  \qquad
  \mathcal L_{\mathrm{YM}}=-\frac14W_{\mu\nu}^aW^{a\mu\nu}.
  $$

  The extra product of gauge fields appears because $SU(2)$ is **non-Abelian**. It produces direct three- and four-gauge-boson interactions, unlike the Abelian photon field in QED.
- Local $SU(2)_L$ symmetry forbids an explicit mass term for the gauge fields. In the full electroweak theory, the Higgs mechanism gives masses to $W^\pm$ and $Z$ while leaving the photon massless.

### Electromagnetic and Weak Terms So Far

- Collect the first-generation fermions as $f\in\{\nu_e,e,u,d\}$ and the left-chiral doublets as

  $$
  L=\begin{pmatrix}\nu_{eL}\\e_L\end{pmatrix},
  \qquad
  Q=\begin{pmatrix}u_L\\d_L\end{pmatrix}.
  $$

  The electromagnetic current is

  $$
  J_{\mathrm{EM}}^\mu=\sum_f q_f\bar f\gamma^\mu f,
  $$

  where $q_f$ is the electric charge of each field.
- A compact bookkeeping summary of the free gauge fields, free fermions, and interactions introduced so far is

  $$
  \boxed{
  \begin{aligned}
  \mathcal L_{\mathrm{so\ far}}={}&
  -\frac14F_{\mu\nu}F^{\mu\nu}
  -\frac14W_{\mu\nu}^aW^{a\mu\nu}
  +\sum_f\bar f(i\gamma^\mu\partial_\mu-m_f)f\\
  &-J_{\mathrm{EM}}^\mu A_\mu
  -g\bar L\gamma^\mu T^aL\,W_\mu^a
  -g\bar Q\gamma^\mu T^aQ\,W_\mu^a.
  \end{aligned}}
  $$

- The terms have the following roles:
  - $-\tfrac14F_{\mu\nu}F^{\mu\nu}$: photon propagation.
  - $-\tfrac14W_{\mu\nu}^aW^{a\mu\nu}$: weak gauge-boson propagation and self-interactions.
  - $\sum_f\bar f(i\gamma^\mu\partial_\mu-m_f)f$: free fermion propagation in the broken-phase, low-energy description.
  - $-J_{\mathrm{EM}}^\mu A_\mu$: photon coupling to every electrically charged fermion.
  - $-g\bar L\gamma^\mu T^aL\,W_\mu^a-g\bar Q\gamma^\mu T^aQ\,W_\mu^a$: weak couplings to left-chiral lepton and quark doublets.
- Rewriting $W^1$ and $W^2$ as $W^\pm$ exposes the charged-current part

  $$
  \mathcal L_{\mathrm{CC}}=-\frac g{\sqrt2}\left(
  \bar\nu_{eL}\gamma^\mu e_LW_\mu^+
  +\bar e_L\gamma^\mu\nu_{eL}W_\mu^-
  +\bar u_L\gamma^\mu d_LW_\mu^+
  +\bar d_L\gamma^\mu u_LW_\mu^-
  \right).
  $$

- This is an **intermediate bookkeeping expression**, rather than the final gauge-invariant electroweak Lagrangian. In particular, the displayed fermion masses belong to the broken-phase, low-energy description. Before symmetry breaking, electromagnetism and the weak interaction are organized as $SU(2)_L\times U(1)_Y$, with a hypercharge field $B_\mu$ instead of a separate photon field and with fermion masses replaced by Yukawa couplings to the Higgs. The Higgs mechanism later mixes $W^3_\mu$ and $B_\mu$ into the physical photon $A_\mu$ and $Z_\mu$, and generates the fermion and massive gauge-boson mass terms.

## Electroweak Unification

- The neutral $SU(2)_L$ field $W_\mu^3$ **cannot be the photon** because its couplings have the wrong pattern:

  | Fermion component | $t_3$ | Coupling to $W^3$ | Required photon coupling |
  | --- | ---: | ---: | ---: |
  | $\nu_{eL}$ | $+\tfrac12$ | nonzero | $0$ |
  | $e_L$ | $-\tfrac12$ | nonzero | $-e$ |
  | $e_R$ | $0$ | $0$ | $-e$ |

  The photon must couple equally to $e_L$ and $e_R$ because they are two chiral components of the same charged electron, while it must not couple to the neutrino. The $W^3$ field instead couples only according to weak isospin $t_3$.
- Add a second symmetry, **weak hypercharge** $U(1)_Y$, with generator $Y/2$. Electric charge is then

  $$
  \boxed{Q=T^3+\frac Y2}.
  $$

  Hypercharge supplies the common offset that $T^3$ alone lacks. In the convention $Q=T^3+Y/2$, the minimal Standard Model assignments for each generation and the Higgs are

  | Multiplet | $SU(3)_C$ | $SU(2)_L$ | $t_3$ | $Y$ | $Q$ |
  | --- | ---: | ---: | ---: | ---: | ---: |
  | $L=(\nu_L,e_L)$ | $\mathbf1$ | $\mathbf2$ | $(+\tfrac12,-\tfrac12)$ | $-1$ | $(0,-1)$ |
  | $e_R$ | $\mathbf1$ | $\mathbf1$ | $0$ | $-2$ | $-1$ |
  | $Q_L=(u_L,d_L)$ | $\mathbf3$ | $\mathbf2$ | $(+\tfrac12,-\tfrac12)$ | $+\tfrac13$ | $(+\tfrac23,-\tfrac13)$ |
  | $u_R$ | $\mathbf3$ | $\mathbf1$ | $0$ | $+\tfrac43$ | $+\tfrac23$ |
  | $d_R$ | $\mathbf3$ | $\mathbf1$ | $0$ | $-\tfrac23$ | $-\tfrac13$ |
  | $\Phi=(\phi^+,\phi^0)$ | $\mathbf1$ | $\mathbf2$ | $(+\tfrac12,-\tfrac12)$ | $+1$ | $(+1,0)$ |

  The same gauge assignments repeat for all three generations. The minimal model contains no right-chiral neutrino; adding $\nu_R$ for a Dirac neutrino mass would make it a complete gauge singlet with $Y=Q=0$.

- Making $U(1)_Y$ local introduces the **hypercharge gauge field** $B_\mu$ with coupling $g'$. For a field $F$ with weak isospin generators $T^a$ and hypercharge $Y_F$,

  $$
  D_\mu F=\left(\partial_\mu+igT^aW_\mu^a
  +ig'\frac{Y_F}{2}B_\mu\right)F.
  $$

  The electroweak gauge group is therefore $SU(2)_L\times U(1)_Y$.
- Neither $W_\mu^3$ nor $B_\mu$ alone has the correct photon coupling. Define the **weak mixing angle** $\theta_W$, with $s_W=\sin\theta_W$ and $c_W=\cos\theta_W$, and rotate the two neutral fields:

  $$
  A_\mu=s_WW_\mu^3+c_WB_\mu,
  \qquad
  Z_\mu=c_WW_\mu^3-s_WB_\mu.
  $$

  The couplings obey

  $$
  e=gs_W=g'c_W,
  $$

  so the $A_\mu$ coefficient becomes $e(t_3+Y/2)=eQ$. Thus $A_\mu$ couples to electric charge with the universal interaction $-eQ_f\bar f\gamma^\mu fA_\mu$.
- The orthogonal field $Z_\mu$ couples to the **neutral weak current**:

  $$
  \mathcal L_Z=-\frac g{c_W}
  \left(t_3-s_W^2Q_f\right)\bar f\gamma^\mu fZ_\mu
  $$

  for a chiral component with quantum numbers $t_3$ and $Q_f$. Unlike the photon, the $Z$ generally couples differently to left- and right-chiral fermions.
- Electroweak unification reorganizes four gauge fields without changing their number:

  $$
  W^1,W^2,W^3,B
  \quad\longrightarrow\quad
  W^+,W^-,Z,A.
  $$

  The Higgs mechanism later makes $W^\pm$ and $Z$ massive while leaving the photon $A$ massless.

### Electroweak Lagrangian So Far

- Before adding the Higgs field, the gauge-invariant electroweak theory contains the $SU(2)_L$ fields $W_\mu^a$, the hypercharge field $B_\mu$, and the chiral fermion multiplets. For one generation,

  $$
  F\in\{L,Q,e_R,u_R,d_R\},
  \qquad
  L=\begin{pmatrix}\nu_{eL}\\e_L\end{pmatrix},
  \qquad
  Q=\begin{pmatrix}u_L\\d_L\end{pmatrix}.
  $$

- The electroweak gauge and fermion Lagrangian is

  $$
  \boxed{
  \mathcal L_{\mathrm{EW}}^{\mathrm{gauge+fermion}}
  =-\frac14W_{\mu\nu}^aW^{a\mu\nu}
  -\frac14B_{\mu\nu}B^{\mu\nu}
  +\sum_F i\bar F\gamma^\mu D_\mu F
  }
  $$

  with

  $$
  D_\mu F=\left(\partial_\mu+igT^aW_\mu^a
  +ig'\frac{Y_F}{2}B_\mu\right)F,
  $$

  $$
  W_{\mu\nu}^a=\partial_\mu W_\nu^a-\partial_\nu W_\mu^a
  -g\epsilon^{abc}W_\mu^bW_\nu^c,
  \qquad
  B_{\mu\nu}=\partial_\mu B_\nu-\partial_\nu B_\mu.
  $$

  For right-chiral singlets, $T^a=0$, so only the hypercharge part of $D_\mu$ acts.
- After defining $W^\pm$ and rotating $W^3,B$ into $A,Z$, the fermion interactions can be collected as

  $$
  \boxed{
  \mathcal L_{\mathrm{int}}
  =-eJ_{\mathrm{EM}}^\mu A_\mu
  -\frac g{\sqrt2}\left(J_+^\mu W_\mu^+ + J_-^\mu W_\mu^-\right)
  -\frac g{c_W}J_Z^\mu Z_\mu
  }
  $$

  where, for the first generation,

  $$
  J_{\mathrm{EM}}^\mu=\sum_fQ_f\bar f\gamma^\mu f,
  $$

  $$
  J_+^\mu=\bar\nu_{eL}\gamma^\mu e_L+\bar u_L\gamma^\mu d_L,
  \qquad
  J_-^\mu=\bar e_L\gamma^\mu\nu_{eL}+\bar d_L\gamma^\mu u_L,
  $$

  $$
  J_Z^\mu=\sum_f
  \left(t_{3f}-s_W^2Q_f\right)\bar f\gamma^\mu f.
  $$

  The sum in $J_Z^\mu$ runs over chiral fermion components; $t_{3f}=0$ for right-chiral singlets.
- The three interaction terms describe:
  - **Electromagnetism:** the photon couples universally to electric charge $Q_f$.
  - **Charged weak interaction:** $W^\pm$ couples only to left-chiral doublets and changes one doublet member into the other.
  - **Neutral weak interaction:** $Z$ couples to both electric charge and weak isospin, so its left- and right-chiral couplings differ.
- The gauge kinetic term $-\tfrac14W_{\mu\nu}^aW^{a\mu\nu}$ also produces $WW\gamma$, $WWZ$, and four-gauge-boson interactions after the field rotation. These follow from the non-Abelian $SU(2)_L$ field strength.
- This is the electroweak Lagrangian **before the Higgs and Yukawa sectors**. Explicit fermion, $W$, and $Z$ mass terms are absent because they would violate $SU(2)_L\times U(1)_Y$ gauge invariance. The Higgs field supplies those masses through spontaneous symmetry breaking while preserving a massless photon.

## Higgs Mechanism

- The Higgs mechanism allows gauge bosons and fermions to acquire mass while the underlying Lagrangian remains gauge invariant.

### Spontaneous Symmetry Breaking: Global $U(1)$ Example

- Begin with a complex scalar field and a symmetric potential

  $$
  \mathcal L=\partial_\mu\phi^*\partial^\mu\phi-V(\phi),
  \qquad
  V(\phi)=-\mu^2\phi^*\phi+\lambda(\phi^*\phi)^2,
  \qquad \mu^2,\lambda>0.
  $$

  The Lagrangian is invariant under the global transformation $\phi\to e^{i\alpha}\phi$.
- The origin is unstable. Minimizing the potential gives a circle of degenerate vacua,

  $$
  \phi^*\phi=\frac{\mu^2}{2\lambda}=\frac{v^2}{2},
  \qquad v^2=\frac{\mu^2}{\lambda}.
  $$

  Choose one vacuum, for example $\langle\phi\rangle=v/\sqrt2$. The laws retain the $U(1)$ symmetry, but the chosen vacuum does not. This is **spontaneous symmetry breaking**.
- Expand around the chosen vacuum:

  $$
  \phi(x)=\frac1{\sqrt2}\left(v+h(x)+i\chi(x)\right).
  $$

  The radial fluctuation $h$ is massive, while the angular fluctuation $\chi$ is a massless **Goldstone boson**:

  $$
  m_h^2=2\lambda v^2,
  \qquad m_\chi^2=0.
  $$

  A broken continuous global generator produces a massless Goldstone mode.

### Local $U(1)$ Higgs Mechanism

- Now make the symmetry local by introducing a gauge field $A_\mu$:

  $$
  D_\mu=\partial_\mu+iqA_\mu,
  \qquad
  \mathcal L=(D_\mu\phi)^*(D^\mu\phi)-V(\phi)
  -\frac14F_{\mu\nu}F^{\mu\nu}.
  $$

  This is a toy $U(1)$ gauge field used to demonstrate the mechanism; it is not the physical photon of the electroweak theory.

- Write the scalar in polar form,

  $$
  \phi(x)=\frac{v+h(x)}{\sqrt2}e^{i\theta(x)/v}.
  $$

  A local gauge transformation can set $\theta(x)=0$. In **unitary gauge**,

  $$
  \phi(x)=\frac{v+h(x)}{\sqrt2}.
  $$

  Gauge fixing removes the redundant phase from the scalar-field description; it does not discard a physical degree of freedom.
- Substitution into the scalar kinetic term gives

  $$
  (D_\mu\phi)^*(D^\mu\phi)
  =\frac12(\partial_\mu h)^2
  +\frac12q^2(v+h)^2A_\mu A^\mu.
  $$

  The term $\tfrac12q^2v^2A_\mu A^\mu$ is a vector mass term, so

  $$
  m_A=qv.
  $$

  The Goldstone degree of freedom becomes the longitudinal polarization of the massive vector. The counting is preserved: a massless vector has two polarizations and the complex scalar has two real modes; afterward, the massive vector has three polarizations and one real scalar $h$ remains.

### Standard Model Higgs Field

- The electroweak Higgs field is a complex $SU(2)_L$ doublet with hypercharge $Y=1$:

  $$
  \Phi=\begin{pmatrix}\phi^+\\\phi^0\end{pmatrix},
  \qquad
  V(\Phi)=-\mu^2\Phi^\dagger\Phi
  +\lambda(\Phi^\dagger\Phi)^2.
  $$

- Choose the vacuum and unitary-gauge field as

  $$
  \langle\Phi\rangle=\frac1{\sqrt2}\begin{pmatrix}0\\v\end{pmatrix},
  \qquad
  \Phi(x)=\frac1{\sqrt2}\begin{pmatrix}0\\v+h(x)\end{pmatrix}.
  $$

  The vacuum is electrically neutral because $Q\langle\Phi\rangle=(T^3+Y/2)\langle\Phi\rangle=0$. Thus $SU(2)_L\times U(1)_Y$ is reduced to the unbroken electromagnetic $U(1)_{\mathrm{EM}}$.
- The doublet contains four real degrees of freedom. Three Goldstone modes supply the longitudinal polarizations of $W^+$, $W^-$, and $Z$. The remaining radial excitation $h$ is the physical **Higgs boson**, with

  $$
  m_h^2=2\lambda v^2.
  $$

### Gauge-Boson Masses

- The Higgs kinetic term uses

  $$
  (D_\mu\Phi)^\dagger D^\mu\Phi,
  \qquad
  D_\mu=\partial_\mu+igT^aW_\mu^a+i\frac{g'}2B_\mu.
  $$

  Evaluated at the vacuum, it produces

  $$
  \mathcal L_{\mathrm{mass}}
  =\frac{v^2}{8}\left[
  g^2\left(W_\mu^1W^{1\mu}+W_\mu^2W^{2\mu}\right)
  +(gW_\mu^3-g'B_\mu)(gW^{3\mu}-g'B^\mu)
  \right].
  $$

- In the $W^\pm,Z,A$ basis,

  $$
  \boxed{m_W=\frac{gv}{2}},
  \qquad
  \boxed{m_Z=\frac v2\sqrt{g^2+g'^2}},
  \qquad
  \boxed{m_A=0}.
  $$

  Consequently, at tree level,

  $$
  \frac{m_W}{m_Z}=\cos\theta_W.
  $$

  The vacuum gives mass to the three gauge fields associated with broken generators. The photon corresponds to the unbroken charge generator and remains massless.

### Fermion Masses

- A direct fermion mass term is not electroweak gauge invariant because $f_L$ and $f_R$ transform differently. Instead, introduce gauge-invariant **Yukawa interactions**. For the electron,

  $$
  \mathcal L_{\mathrm{Yukawa}}
  =-y_e\bar L\Phi e_R+\mathrm{h.c.}
  $$

- Substituting the Higgs vacuum gives

  $$
  \mathcal L_{\mathrm{Yukawa}}
  =-\frac{y_ev}{\sqrt2}\bar e e
  -\frac{y_e}{\sqrt2}h\bar e e,
  $$

  so

  $$
  \boxed{m_e=\frac{y_ev}{\sqrt2}},
  \qquad
  \mathcal L_{hee}=-\frac{m_e}{v}h\bar e e.
  $$

  Other charged fermions acquire masses in the same way. The Higgs mechanism relates each Higgs–fermion coupling to $m_f/v$, but the Yukawa constants $y_f$ remain independent measured parameters. Neutrino masses require an extension of the minimal massless-neutrino model used here.

### Electroweak Lagrangian Including the Higgs

- Combining the gauge, fermion, Higgs, and Yukawa terms gives the electroweak Lagrangian developed so far. For one fermion generation,

  $$
  \boxed{
  \begin{aligned}
  \mathcal L_{\mathrm{EW}}={}&
  -\frac14W_{\mu\nu}^aW^{a\mu\nu}
  -\frac14B_{\mu\nu}B^{\mu\nu}
  +\sum_{F\in\{L,Q,e_R,u_R,d_R\}}
  i\bar F\gamma^\mu D_\mu F\\
  &+(D_\mu\Phi)^\dagger D^\mu\Phi
  -V(\Phi)\\
  &-\left(
  y_e\bar L\Phi e_R
  +y_d\bar Q\Phi d_R
  +y_u\bar Q\widetilde\Phi u_R
  +\mathrm{h.c.}\right),
  \end{aligned}}
  $$

  where

  $$
  V(\Phi)=-\mu^2\Phi^\dagger\Phi
  +\lambda(\Phi^\dagger\Phi)^2,
  \qquad
  \widetilde\Phi=i\sigma^2\Phi^*,
  $$

  and $D_\mu$ contains the $SU(2)_L$ and $U(1)_Y$ gauge fields with the generators and hypercharge appropriate to each multiplet.
- This single expression contains:
  - free propagation and self-interactions of the electroweak gauge fields;
  - electroweak interactions of leptons and quarks;
  - Higgs propagation, its potential, and its gauge interactions;
  - Yukawa interactions that become charged-fermion masses and Higgs–fermion couplings after symmetry breaking.
- For all three generations, each fermion multiplet acquires a generation index and the Yukawa couplings become matrices. Diagonalizing those matrices produces the observed fermion masses and quark mixing in the charged weak current.
- **Is only QCD missing?** For the minimal, gauge-invariant classical Standard Model Lagrangian, QCD is the remaining force sector. It adds the $SU(3)_C$ gluon kinetic term and the colour part of the quark covariant derivative. Once those terms and all three generations are included, the core Standard Model Lagrangian is complete.
- Some additions depend on what is being calculated:
  - Gauge-fixing and ghost terms are required for perturbative quantization but are not part of the compact gauge-invariant classical expression.
  - The minimal Standard Model written here has massless neutrinos. Observed neutrino masses require an extension, such as right-chiral neutrinos or an effective higher-dimensional operator.
  - Gravity is not part of the Standard Model.

## Quantum Chromodynamics

- **Quantum chromodynamics (QCD)** is the gauge theory of quarks, gluons, and the strong interaction.

### Quarks, Flavours, and Colours

- Quarks are spin-$\tfrac12$ fermions. There are six **flavours**, arranged by their electric charges:

  | Type | Flavours | Electric charge |
  | --- | --- | ---: |
  | Up-type | $u,c,t$ | $+\tfrac23e$ |
  | Down-type | $d,s,b$ | $-\tfrac13e$ |

  Flavour identifies the quark species. The strong interaction preserves flavour at a quark–gluon vertex; weak charged currents can change an up-type flavour into a down-type flavour.
- Every flavour has three **colour components**, conventionally labelled red, green, and blue:

  $$
  q=\begin{pmatrix}q_r\\q_g\\q_b\end{pmatrix}.
  $$

  These labels have no connection to visible colour. A colour transformation acts on this three-component internal index while leaving the quark's flavour, spinor index, and electric charge unchanged.
- Observable hadrons are colour singlets. Mesons contain quark–antiquark colour combinations, while baryons contain an antisymmetric combination of three colours. Isolated quarks and gluons are not observed at long distances; this is **confinement**.

### Local $SU(3)_C$ Symmetry

- The three colour components have the same free kinetic form, so the free quark Lagrangian is invariant under global colour rotations

  $$
  q\to Uq,
  \qquad
  U=\exp(i\alpha^aT_C^a)\in SU(3)_C.
  $$

- The group $SU(3)$ has eight Hermitian, traceless generators $T_C^a$, normalized by

  $$
  \operatorname{tr}(T_C^aT_C^b)=\frac12\delta^{ab},
  \qquad
  [T_C^a,T_C^b]=if^{abc}T_C^c.
  $$

  The nonzero structure constants $f^{abc}$ show that $SU(3)_C$ is **non-Abelian**.
- Making the colour transformation local introduces eight gluon gauge fields $G_\mu^a$ and the strong coupling $g_s$:

  $$
  D_\mu q=\left(\partial_\mu+ig_sT_C^aG_\mu^a\right)q.
  $$

  Expanding the covariant derivative gives the quark–gluon interaction

  $$
  \mathcal L_{qg}=-g_s\bar q\gamma^\mu T_C^aq\,G_\mu^a,
  $$

  with vertex factor $-ig_s\gamma^\mu T_C^a$. A gluon interaction can change a quark's colour but not its flavour or electric charge.

### Gluons and the QCD Lagrangian

- Define the gluon field strength by

  $$
  G_{\mu\nu}^a=\partial_\mu G_\nu^a-\partial_\nu G_\mu^a
  -g_sf^{abc}G_\mu^bG_\nu^c.
  $$

  The last term occurs because $SU(3)_C$ is non-Abelian. Squaring the field strength produces both three-gluon and four-gluon vertices, so gluons interact directly with one another.
- The QCD Lagrangian is

  $$
  \boxed{
  \mathcal L_{\mathrm{QCD}}
  =-\frac14G_{\mu\nu}^aG^{a\mu\nu}
  +\sum_{f=1}^{6}\bar q_f(i\gamma^\mu D_\mu-m_f)q_f
  }.
  $$

  The masses $m_f$ arise from the Higgs Yukawa couplings. Both left- and right-chiral quarks carry colour and therefore couple to gluons.
- The Higgs is a colour singlet, so its vacuum does not break $SU(3)_C$ and the gluons have no mass term. They remain massless in the Lagrangian even though confinement prevents isolated gluons from appearing as asymptotic particles.
- The effective strong coupling $\alpha_s=g_s^2/(4\pi)$ decreases at high energies or short distances: **asymptotic freedom**. It grows at hadronic distances, where perturbation theory fails and nonperturbative methods such as lattice QCD are needed.

### Minimal Gauge-Invariant Standard Model

- The complete Standard Model gauge group is

  $$
  \boxed{SU(3)_C\times SU(2)_L\times U(1)_Y}.
  $$

  Colour, weak isospin, and hypercharge act on different internal indices. Quarks carry all three types of charge; leptons and the Higgs are colour singlets.
- All gauge interactions can be written in one covariant derivative:

  $$
  D_\mu F=\left(
  \partial_\mu
  +ig_sT_C^aG_\mu^a
  +igT_L^iW_\mu^i
  +ig'\frac{Y_F}{2}B_\mu
  \right)F.
  $$

  A generator is zero when the field is a singlet under that group.
- Combining QCD with the electroweak and Higgs sectors gives

  $$
  \boxed{
  \begin{aligned}
  \mathcal L_{\mathrm{SM}}={}&
  -\frac14G_{\mu\nu}^aG^{a\mu\nu}
  -\frac14W_{\mu\nu}^iW^{i\mu\nu}
  -\frac14B_{\mu\nu}B^{\mu\nu}\\
  &+\sum_F i\bar F\gamma^\mu D_\mu F
  +(D_\mu\Phi)^\dagger D^\mu\Phi
  -V(\Phi)
  +\mathcal L_{\mathrm{Yukawa}}.
  \end{aligned}}
  $$

  The sum runs over the left-chiral doublets and right-chiral singlets of all three generations, including the three colour components of each quark field.
- For three generations, the Yukawa sector is

  $$
  \mathcal L_{\mathrm{Yukawa}}=
  -\bar Q^i(Y_d)_{ij}\Phi d_R^j
  -\bar Q^i(Y_u)_{ij}\widetilde\Phi u_R^j
  -\bar L^i(Y_e)_{ij}\Phi e_R^j
  +\mathrm{h.c.},
  $$

  where $i,j=1,2,3$ are generation indices. After symmetry breaking, these matrices produce fermion masses and the CKM quark-mixing matrix.
- This is the compact **minimal gauge-invariant classical Standard Model Lagrangian**. It omits gauge-fixing and ghost terms used in perturbative calculations, the optional strong-CP term, gravity, and any extension required to generate neutrino masses.

## Using the Lagrangian

- The Lagrangian specifies the fields, their free propagation, and their interactions. To predict an experiment, follow the chain

  $$
  \boxed{
  \mathcal L
  \longrightarrow S
  \longrightarrow \mathcal M
  \longrightarrow |\mathcal M|^2
  \longrightarrow \sigma
  \longrightarrow \text{event rate}
  }.
  $$

### From the Lagrangian to the $S$-Matrix

- Split the Lagrangian into free and interaction parts,

  $$
  \mathcal L=\mathcal L_0+\mathcal L_{\mathrm{int}}.
  $$

  The quadratic part $\mathcal L_0$ determines particle states and propagators. The interaction terms determine which particles can meet at a vertex and the strength and tensor structure of that interaction.
- The **$S$-matrix** maps an incoming free-particle state in the distant past to an outgoing free-particle state in the distant future. The transition amplitude is $\langle f|S|i\rangle$.
- Probability conservation requires the $S$-matrix to be unitary, $S^\dagger S=I$. This relates different scattering contributions and ensures that the probabilities of all possible outcomes sum consistently.
- In the interaction picture,

  $$
  S=T\exp\!\left[i\int d^4x\,\mathcal L_{\mathrm{int}}(x)\right],
  $$

  where $T$ denotes time ordering. Expanding the exponential gives the **Dyson series**:

  $$
  S=\sum_{n=0}^{\infty}\frac{i^n}{n!}
  \int d^4x_1\cdots d^4x_n\,
  T\!\left[\mathcal L_{\mathrm{int}}(x_1)\cdots
  \mathcal L_{\mathrm{int}}(x_n)\right].
  $$

  If an interaction carries coupling $g$, a term with $n$ insertions is generally of order $g^n$.
- **Wick's theorem** rewrites time-ordered products as normal-ordered products plus contractions. The contractions are free-field propagators, and the remaining fields attach to the external particle states. Feynman diagrams organize these contributions:
  - external lines represent specified incoming and outgoing particles;
  - internal lines represent propagators and need not satisfy the on-shell relation;
  - vertices come from $\mathcal L_{\mathrm{int}}$;
  - loops represent integrations over undetermined internal momenta.
- The Feynman rules convert each allowed diagram into an algebraic expression. Add the amplitudes of all diagrams leading to the same final state before taking the absolute square, so interference is retained.

### Invariant Amplitude

- Separate free passage from the interacting part using

  $$
  \langle f|S|i\rangle
  =\langle f|i\rangle
  +(2\pi)^4\delta^4(P_f-P_i)\,i\mathcal M.
  $$

  The four-dimensional delta function enforces total energy–momentum conservation. The remaining quantity $\mathcal M$ is the **invariant amplitude**.
- The probability is built from $|\mathcal M|^2$. For unobserved quantum numbers, sum over final spins, colours, and polarizations and average over the corresponding initial ones:

  $$
  \overline{|\mathcal M|^2}
  =\frac{1}{N_{\mathrm{initial}}}
  \sum_{\mathrm{initial,final}}|\mathcal M|^2.
  $$

  Identical final-state particles also require the appropriate symmetry factor to avoid overcounting equivalent configurations.

### Scattering Cross Section

- The **cross section** measures the probability of scattering after dividing out the incoming beam flux. For a process $1+2\to n$ particles,

  $$
  d\sigma=
  \frac{\overline{|\mathcal M|^2}}
  {4\sqrt{(p_1\cdot p_2)^2-m_1^2m_2^2}}\,d\Phi_n.
  $$

- For a $2\to2$ process in the centre-of-momentum frame,

  $$
  \frac{d\sigma}{d\Omega}
  =\frac{1}{64\pi^2s}
  \frac{|\mathbf p_f|}{|\mathbf p_i|}
  \overline{|\mathcal M|^2},
  \qquad s=(p_1+p_2)^2.
  $$

  Integrating over the allowed solid angle gives the total cross section. Experimental event counts satisfy $N_{\mathrm{events}}=\mathscr L_{\mathrm{int}}\sigma$, where $\mathscr L_{\mathrm{int}}$ is the integrated luminosity, up to detector efficiency and acceptance.

### Perturbative Accuracy

- Keeping only the lowest nonzero power of a coupling gives the **leading-order** or tree-level prediction. Loop diagrams give higher-order quantum corrections and generally require regularization and renormalization.
- A perturbative expansion is useful only when the relevant running coupling is sufficiently small. This works well for QED and many high-energy electroweak or QCD processes, but long-distance QCD requires nonperturbative methods.
- Gauge theories also require gauge fixing to define propagators. Ghost fields appear in non-Abelian perturbation theory and cancel unphysical gauge contributions; only gauge-independent observables such as cross sections are physical.
