# Relativistic QM

## 1. Plane Wave

Before changing the Schrödinger equation, we will solve it for a free particle with definite energy and momentum. These plane-wave solutions make it easy to compare non-relativistic and relativistic energy relations.

**Specify a definite energy.** The Hamiltonian $\hat H$ is the energy operator. A state with a definite energy $E$ satisfies its eigenvalue equation,

$$\hat H \psi = E \psi .$$

Measuring energy in this state gives $E$ with certainty. For a time-independent Hamiltonian, time evolution changes only its overall phase. Its probability distribution and the expectation values of observables with no explicit time dependence stay constant.

**Find the time dependence.** Start with the time-dependent Schrödinger equation,

$$i\hbar \frac{\partial \psi}{\partial t} = \hat H \psi$$

using $c=1$ and keeping $\hbar$ explicit, as in Special Relativity §9.

For a definite-energy solution, factor the wave function as $\psi(x,t)=\phi(x)\tau(t)$. Substitute this into the equation and divide by the product:

$$i\hbar \frac{\dot\tau(t)}{\tau(t)} = \frac{\hat H \phi(x)}{\phi(x)} = E,$$

The left side depends only on time and the right side only on position. Both must therefore equal a constant, which we identify as the energy $E$. Integrating the time equation gives

$$\tau(t) = e^{-iEt/\hbar},$$

up to a constant factor. The spatial equation is the **time-independent Schrödinger equation**,

$$\hat H \phi = E \phi .$$

**Find the spatial dependence.** For a free particle, $\hat H=\hat{\mathbf p}^2/2m$ and $\hat{\mathbf p}=-i\hbar\nabla$, so

$$-\frac{\hbar^2}{2m}\nabla^2 \phi = E \phi,$$

A momentum eigenfunction $\phi(\mathbf x)=e^{i\mathbf p\cdot\mathbf x/\hbar}$ satisfies this equation when $E=\mathbf p^2/2m$. Multiplying by the time factor gives

$$\psi(x, t) = e^{i(\mathbf p\cdot\mathbf x - Et)/\hbar},$$

a **plane wave** with definite momentum $\mathbf p$ and energy $E=\mathbf p^2/2m$. Its squared magnitude is constant across space, so it has no localized position distribution. An exact plane wave is an idealized generalized eigenstate; a normalizable particle state uses a superposition, or wave packet.

The plane-wave form will also solve relativistic equations. What changes is the dispersion relation connecting $E$ and $\mathbf p$. We next derive an equation with the exact relativistic relation.

## 2. Klein Gordon

The non-relativistic equation uses an approximation to the energy. To retain Lorentz covariance, start instead with the exact energy–momentum relation.

**Start with relativistic energy.** In units $c=1$, Special Relativity §7 gives

$$E^2 = \mathbf p^2 + m^2$$

This is the invariant four-momentum norm $p^\mu p_\mu=m^2$. At low momentum, the positive energy is approximately $m+\mathbf p^2/2m$. Subtracting the rest energy $m$ gives the non-relativistic kinetic energy.

**Replace energy and momentum by operators.** Use the same prescription as before:

$$E \to i\hbar\,\frac{\partial}{\partial t}, \qquad \mathbf p \to -i\hbar\nabla .$$

Apply these operators to the squared relation, without making a low-speed approximation.

**Collect the derivatives.** Acting on $\psi$ gives the following steps:

$$\left(i\hbar\,\frac{\partial}{\partial t}\right)^2 \psi = \left(m^2 - \hbar^2\nabla^2\right)\psi,$$

$$-\hbar^2\,\partial_t^2\psi = m^2\psi - \hbar^2\nabla^2\psi,$$

$$\partial_t^2\psi - \nabla^2\psi + \frac{m^2}{\hbar^2}\psi = 0,$$

Define $\Box$, the d'Alembertian, to write the result compactly:

$$\left(\Box + \frac{m^2}{\hbar^2}\right)\psi = 0, \qquad \Box \equiv \partial_\mu\partial^\mu = \partial_t^2 - \nabla^2,$$

This is the **Klein–Gordon equation**. For a scalar field $\psi$, each term transforms as a Lorentz scalar: $\Box$ contracts the derivative indices, and $m$ is invariant. The equation therefore has the same form in every inertial frame.

Substituting the plane wave $\psi=e^{i(\mathbf p\cdot\mathbf x-Et)/\hbar}$ gives

$$E^2 = \mathbf p^2 + m^2,$$

Both $E=+\sqrt{\mathbf p^2+m^2}$ and $E=-\sqrt{\mathbf p^2+m^2}$ satisfy the equation. We must explain the negative-energy solutions and determine whether the wave function still has a single-particle probability interpretation.

## 3. Negative Energy and Probability

The Klein–Gordon equation has the correct relativistic energy relation. The difficulty is interpreting all of its solutions as states of one particle.

**Negative energies.** The plane-wave energies have both signs:

$$E = \pm\sqrt{\mathbf p^2 + m^2},$$

For every momentum, there is a solution with $E\leq-m$. If these represented accessible particle energies, there would be no lowest energy: the negative values decrease without bound as momentum increases. Interactions coupling positive- and negative-energy states could then destabilize a one-particle description.

In field theory, we interpret negative-frequency modes through **antiparticles**, with positive energy and the opposite charge. The **Stückelberg–Feynman interpretation** expresses the same relation by reversing the direction of a charged particle line in time. A negative-energy contribution with momentum $\mathbf p$ corresponds to an antiparticle contribution with positive energy and reversed momentum. Emission and absorption exchange roles under this reinterpretation.

This does not mean that observed antiparticles travel backward on laboratory clocks. The full description uses particle creation and annihilation, which a fixed single-particle wave function cannot represent.

**Find a conserved probability.** For comparison, consider the Schrödinger equation with a real local potential $V$:

$$i\hbar\,\partial_t \psi = \left(-\frac{\hbar^2}{2m}\nabla^2 + V\right)\psi,$$

Differentiate the candidate density: $\partial_t|\psi|^2=\psi^*\partial_t\psi+\psi\,\partial_t\psi^*$. Substitute the Schrödinger equation and its complex conjugate:

$$\partial_t|\psi|^2 = \frac{1}{i\hbar}\left[\psi^*\left(-\frac{\hbar^2}{2m}\nabla^2 + V\right)\psi - \psi\left(-\frac{\hbar^2}{2m}\nabla^2 + V\right)\psi^*\right].$$

The terms containing the real potential cancel. The derivative terms form a divergence because $\nabla\cdot(\psi^*\nabla\psi-\psi\nabla\psi^*)=\psi^*\nabla^2\psi-\psi\nabla^2\psi^*$. Therefore,

$$\partial_t |\psi|^2 = -\nabla\cdot\mathbf j, \qquad \mathbf j = \frac{\hbar}{2mi}\left(\psi^*\nabla\psi - \psi\,\nabla\psi^*\right).$$

This is a **continuity equation**: a change in probability inside a region equals the net flow through its boundary. With no probability flux at infinity, $\int|\psi|^2\,d^3x$ stays constant. The density is also nonnegative, so we can normalize it as a probability.

The derivation used the Schrödinger equation to determine $\partial_t\psi$ from $\psi$. The Klein–Gordon equation instead determines the second time derivative. We must specify both $\psi$ and $\partial_t\psi$ initially, and $|\psi|^2$ generally does not obey this conservation law.

To find a conserved quantity, multiply the Klein–Gordon equation by $\psi^*$ and subtract its complex conjugate multiplied by $\psi$. Rearranging gives the **Klein–Gordon current**,

$$j^\mu = i\left(\psi^*\partial^\mu\psi - \psi\,\partial^\mu\psi^*\right), \qquad \partial_\mu j^\mu = 0,$$

with time component

$$\rho = j^0 = i\left(\psi^*\partial_t\psi - \psi\,\partial_t\psi^*\right).$$

For a plane wave, substitute $\partial_t\psi=-iE\psi/\hbar$ to obtain

$$\rho = \frac{2E}{\hbar}\,|\psi|^2,$$

The sign of this density follows the sign of $E$. It can therefore be negative, so we cannot use it as an ordinary probability density for all Klein–Gordon solutions.

A charge density can have either sign. In the quantized complex field, this current describes charge, and the two signs correspond to the charges of particles and antiparticles.

The difference is:

| Schrödinger (first order) | Klein–Gordon (second order) |
| --- | --- |
| Specify $\psi$ initially; the equation fixes $\partial_t\psi$. | Specify both $\psi$ and $\partial_t\psi$ initially. |
| $\lvert\psi\rvert^2$ is nonnegative and obeys a continuity equation. | $\lvert\psi\rvert^2$ is generally not the conserved density. |
| Normalize $\int\lvert\psi\rvert^2\,d^3x$ as total probability. | The conserved density is $\rho=\frac{2E}{\hbar}\lvert\psi\rvert^2$ for a plane wave and can have either sign. |

**Move beyond one particle.** In **second quantization**, the field becomes an operator with terms that create and annihilate particles. Negative-frequency terms then describe antiparticles, while physical excitations have positive energies. For a complex field, the conserved Klein–Gordon quantity becomes charge.

Historically, Dirac first sought a relativistic equation with a positive density $\rho=\psi^\dagger\psi$. His equation achieves that by using a multicomponent wave function and a first time derivative. It still has negative-energy solutions, which he later interpreted using a filled sea and holes. Field quantization provides the modern interpretation.

## 4. Dirac Equation

In 1928, Dirac sought an equation that combined Lorentz covariance with a positive conserved density. We can reconstruct it by requiring a first-order equation that reproduces the relativistic energy relation when squared.

**Set the conditions.** A first time derivative determines $\partial_t\psi$ from the state. With a suitable Hermitian Hamiltonian, this gives a continuity equation for $\psi^\dagger\psi$.

For a local Lorentz-covariant equation linear in derivatives, time and spatial derivatives must enter together. We therefore try first derivatives in space as well. Finally, plane waves must satisfy $E^2=\mathbf p^2+m^2$.

**Try a linear Hamiltonian.** Write

$$i\hbar\,\partial_t\psi = \left(-i\hbar\,\boldsymbol\alpha\cdot\nabla + \beta m\right)\psi,$$

where the coefficients $\boldsymbol\alpha=(\alpha_1,\alpha_2,\alpha_3)$ and $\beta$ are constant objects we must determine.

**Square the equation.** Applying the time-evolution operator again must reproduce the Klein–Gordon equation:

$$(i\hbar\,\partial_t)^2\psi = \left(-i\hbar\,\boldsymbol\alpha\cdot\nabla + \beta m\right)^2\psi = \left(m^2 - \hbar^2\nabla^2\right)\psi.$$

Expanding the Hamiltonian square makes the required conditions explicit:

$$-\hbar^2\sum_{ij}\alpha_i\alpha_j\,\partial_i\partial_j\,\psi + m^2\beta^2\,\psi - i\hbar m\sum_i\left(\alpha_i\beta + \beta\alpha_i\right)\partial_i\psi = m^2\psi - \hbar^2\nabla^2\psi.$$

Matching the mass term gives $\beta^2=\mathbb1$. Removing mixed mass–derivative terms gives $\alpha_i\beta+\beta\alpha_i=0$. Matching the Laplacian gives $\alpha_i\alpha_j+\alpha_j\alpha_i=2\delta_{ij}$.

These are **anticommutation relations**: the sum of two operator orderings vanishes when the indices differ. Ordinary numbers cannot satisfy all these conditions. Matrices can, so $\psi$ must have multiple components.

**Choose the matrices.** The three Pauli matrices anticommute with one another. To include a fourth independent matrix that anticommutes with all three and has square one, the smallest complex representation has size $4\times4$. A standard choice is

$$\alpha_i = \begin{pmatrix} 0 & \sigma_i \\ \sigma_i & 0 \end{pmatrix}, \qquad \beta = \begin{pmatrix} \mathbb{1} & 0 \\ 0 & -\mathbb{1} \end{pmatrix},$$

where each displayed block is $2\times2$. The wave function is then a **four-component spinor**, which we write as two pairs, $\psi=\begin{pmatrix}u\\v\end{pmatrix}$. Substituting a plane wave, so that $i\hbar\partial_t\to E$, gives

$$(E - m)\,u = \boldsymbol\sigma\cdot\mathbf p\,v, \qquad (E + m)\,v = \boldsymbol\sigma\cdot\mathbf p\,u,$$

These equations couple the upper and lower pairs. For a positive-energy state at low momentum, $E\approx m$. Solving the second equation gives

$$v = \frac{\boldsymbol\sigma\cdot\mathbf p}{E + m}\,u \approx \frac{\boldsymbol\sigma\cdot\mathbf p}{2m}\,u,$$

The lower pair is smaller than the upper pair by a factor of order speed divided by $c$. These are the **small components**. At low speed, the positive-energy solution therefore reduces mainly to the upper two components.

For a negative-energy solution near $E=-m$, use the first coupled equation instead. The upper pair is then small compared with the lower pair. At general momentum, both pairs contribute; they do not separately represent particle and antiparticle states.

The two components within each pair are associated with the two spin states of a spin-½ particle. We did not insert those spin states into a scalar equation: they follow from the matrix structure needed for Dirac's construction. [The Dirac Equation](dirac-equation.md) develops their transformation and physical meaning.

**Check the density.** Use the Dirac equation and its adjoint to differentiate $\psi^\dagger\psi$. The result is

$$\partial_t\left(\psi^\dagger\psi\right) = -\nabla\cdot\left(\psi^\dagger\boldsymbol\alpha\,\psi\right),$$

The density $\rho=\psi^\dagger\psi$ is nonnegative, and the equation conserves its integral when there is no boundary flux. This resolves the density problem for the Dirac wave equation.

Define $\gamma^0=\beta$ and $\gamma^i=\beta\alpha_i$. Multiplying the equation by $\beta$ gives the covariant form

$$\left(i\hbar\,\gamma^\mu\partial_\mu - m\right)\psi = 0,$$

The conserved current is $j^\mu=\bar\psi\gamma^\mu\psi$, where $\bar\psi=\psi^\dagger\gamma^0$ is the **Dirac adjoint**. Its time component is the positive density above.

**Interpret the remaining energies.** Squaring the Dirac equation reproduces Klein–Gordon, so $E=\pm\sqrt{\mathbf p^2+m^2}$ remains. Both signs now have nonnegative probability density. Positivity alone therefore does not resolve the negative energies.

Dirac's filled-sea interpretation and the Stückelberg–Feynman interpretation both introduce antiparticles. The [Dirac Equation](dirac-equation.md) page develops these ideas. A full account of creation and annihilation still requires field quantization.

**Connect to observations.** Coupling the Dirac equation to electromagnetism predicts $g=2$ for the electron at this level of approximation. Its antiparticle interpretation predicts an oppositely charged particle, the positron, discovered in 1932, four years after the equation.

We now have a relativistic wave equation with a positive probability density. The next page, [The Dirac Equation](dirac-equation.md), explains the spinor components and the negative-energy solutions in more detail.

## 5. Summary

The derivation used four steps:

**1. Start with the exact energy relation.** Special relativity gives $E^2=\mathbf p^2+m^2$. At low momentum, subtracting the rest energy from its positive solution gives $E_{\mathrm{kin}}\approx\mathbf p^2/2m$. The Schrödinger equation uses this approximation.

**2. Substitute operators.** Replace $E\to i\hbar\,\partial_t$ and $\mathbf p\to-i\hbar\nabla$. The kinetic-energy approximation gives Schrödinger; the exact squared relation gives Klein–Gordon.

**3. Check the Klein–Gordon interpretation.** The equation $(\Box+m^2/\hbar^2)\psi=0$ is Lorentz-covariant. It has both energy signs, and its conserved density can be negative. We therefore cannot interpret that density as a single-particle probability for all solutions.

**4. Construct the Dirac equation.** A first-order equation whose square gives the same dispersion relation requires anticommuting matrices and a four-component spinor. Its density $\psi^\dagger\psi$ is nonnegative, but negative-energy solutions remain.

Field quantization completes the interpretation by describing particles and antiparticles with positive excitation energies, including processes that change their numbers.
