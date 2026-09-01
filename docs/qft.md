# Quantum Field Theory: Fields and Quanta

This page continues from [The Dirac Equation](dirac-equation.md) and crosses the bridge promised at its end. The single-particle equation cannot describe particles that are created and destroyed, so we change the object: the wave function is not the fundamental object of the theory but a coefficient. The fundamental objects are **field operators**, operator-valued functions of space and time that create and annihilate particles. On this reading the negative-energy solutions of the Dirac equation need no explaining away: creation and annihilation operators acting on the vacuum replace the hole picture of its §4, the antiparticle of its §3 becomes the electron field's partner, and the physics of the positron follows from the mathematics of the field.

## Recap of Dirac Equation

The point of departure is the general solution at the end of [The Dirac Equation §6](dirac-equation.md#_6-general-solution). For the free equation,

$$\psi(x) = \sum_{s=1}^{2} \int \frac{d^3p}{(2\pi\hbar)^3}\,\frac{1}{\sqrt{2E_p}}\left[a_s(p)\,u_s(p)\,e^{-ip\cdot x/\hbar} + b_s^*(p)\,v_s(p)\,e^{+ip\cdot x/\hbar}\right],$$

with $p\cdot x = E_p t - \mathbf p\cdot\mathbf x$ and $E_p = \sqrt{\mathbf p^2 + m^2}$. The formula holds two kinds of terms and two coefficients. The $u$-terms oscillate at positive frequency and describe the electron; the $v$-terms oscillate at negative frequency, and [§3](dirac-equation.md#_3-antiparticles) identified them as the antiparticle, while [§4](dirac-equation.md#_4-negative-energy-solutions) could only interpret them as holes in a sea. The coefficients $a_s(p)$ and $b_s^*(p)$ are complex numbers, the amplitudes fixed by the initial conditions. Everything on this page happens inside this formula.

### The promotion

A coefficient can multiply a term of the solution, but it cannot create or destroy a particle, and creation and destruction are exactly what the negative-frequency terms demand ([§4](dirac-equation.md#_4-negative-energy-solutions)). The way out, announced at the end of [§6](dirac-equation.md#_6-general-solution), is to promote the coefficients to operators,

$$a_s(p) \to \hat a_s(p), \qquad b_s^*(p) \to \hat b_s^\dagger(p),$$

where $\hat a_s(p)$ annihilates an electron of momentum $\mathbf p$ and spin $s$, and $\hat b_s^\dagger(p)$ creates a positron of the same momentum and spin. The star on $b_s^*$ was there for a reason. When numbers become operators, the complex conjugate becomes the adjoint, ${}^* \to {}^\dagger$, so [§6](dirac-equation.md#_6-general-solution) wrote the second coefficient conjugated because the notation was already the shape of the quantized field. After the promotion the same expansion reads

$$\hat\psi(x) = \sum_{s=1}^{2} \int \frac{d^3p}{(2\pi\hbar)^3}\,\frac{1}{\sqrt{2E_p}}\left[\hat a_s(p)\,u_s(p)\,e^{-ip\cdot x/\hbar} + \hat b_s^\dagger(p)\,v_s(p)\,e^{+ip\cdot x/\hbar}\right],$$

and the object has changed kind. It is no longer a wave function but the **electron field operator**. Grouped by frequency, $\hat\psi = \hat\psi^{(+)} + \hat\psi^{(-)}$, with the adjoint field $\hat\psi^\dagger$ carrying the reversed halves. The full dictionary:

| half | operator | plane wave | action |
| --- | --- | --- | --- |
| $\hat\psi^{(+)}$ (positive frequency) | $\hat a_s(p)$ | $e^{-ip\cdot x/\hbar}$ | annihilates an electron |
| $\hat\psi^{(-)}$ (negative frequency) | $\hat b_s^\dagger(p)$ | $e^{+ip\cdot x/\hbar}$ | creates a positron |
| $\hat\psi^{(+)\dagger}$ | $\hat a_s^\dagger(p)$ | $e^{+ip\cdot x/\hbar}$ | creates an electron |
| $\hat\psi^{(-)\dagger}$ | $\hat b_s(p)$ | $e^{-ip\cdot x/\hbar}$ | annihilates a positron |

The action column needs an argument. The symbols alone do not decide it, because each species stands on both signs of plane wave across the field and its adjoint; the sign of the plane wave does. A state with energy $E$ oscillates in time as $e^{-iEt/\hbar}$. The $\hat a_s(p)$ term's plane wave, $e^{-ip\cdot x/\hbar}$ with $p\cdot x = E_p t - \mathbf p\cdot\mathbf x$, splits into the time factor $e^{-iE_p t/\hbar}$ and the spatial factor $e^{+i\mathbf p\cdot\mathbf x/\hbar}$. Sandwich the field between an initial state of energy $E_i$ and a final state of energy $E_f$ and read off the time dependence of $\langle f|\hat\psi|i\rangle$, the number measuring how strongly the field connects the two states. The three factors line up, $e^{-iE_i t/\hbar}$ from the initial state, $e^{+iE_f t/\hbar}$ from the final one, and $e^{-iE_p t/\hbar}$ from the operator. The product is steady only when $E_f = E_i - E_p$; for any other pair of states the matrix element oscillates in time and its time average vanishes, so the term participates in no other transitions. The $\hat a_s(p)$ term therefore removes energy $E_p$. Acting on a state, it produces, where it produces anything, a component whose energy is lower by exactly $E_p$, and the same matching on the spatial factors removes momentum $\mathbf p$. Removing a quantum of energy and momentum is what "annihilates" means. Strictly, the matching has earned only the removal. Calling what is removed a particle adds the identification of a particle with one quantum of energy and momentum, a claim about the theory's spectrum that the construction to come confirms when the Hamiltonian arrives as a sum of terms $E_p\,\hat a^\dagger\hat a$. The $e^{+ip\cdot x/\hbar}$ terms match with the signs reversed, so they add energy and momentum instead, and their operators create.

The phase matching fixes the action but not the name. [The Dirac Equation](dirac-equation.md) identified the positive-frequency $u$-terms as the electron's solutions, and the operator standing on such a term inherits the name. The $v$-terms' operator takes the remaining label, positron. Choice enters only here, as continuity with the single-particle theory.

The field and its adjoint mirror each other: each carries one annihilation half and one creation half. Nothing removed the negative-frequency terms; they changed jobs, from states an electron might fall into to the operators that create antiparticles.

### What the promotion does not yet have

We have asserted the promotion but not constructed it, and three things remain to be built. The first is the space the operators act on: states of any particle number, built from a vacuum $|0\rangle$ annihilated by every $\hat a$ and $\hat b$. This vacuum replaces the filled sea of [§4](dirac-equation.md#_4-negative-energy-solutions), and pair annihilation becomes the operator statement $\hat a\,\hat b\,|e^-\,e^+\rangle = |0\rangle$. The second is the algebra the operators obey, commutators or anticommutators, because that choice separates bosons from fermions and answers the statistics caveat of [§4](dirac-equation.md#_4-negative-energy-solutions). The third is the Hamiltonian: rebuilt from the promoted operators, it must come out bounded below, so that the negative-energy solutions of [Relativistic QM §3](relativistic-qm.md#_3-negative-energy-and-probability) are finally accounted for. The sections that follow prepare for this construction, after one more piece of ground: what a field is, and in which picture it lives.

## Fields

Fields come in kinds, and the previous pages already used the classification: by how the objects transform under Lorentz transformations ([The Dirac Equation §5](dirac-equation.md#_5-spinors-transformations)). A classical field assigns a value to every point of spacetime, and the representation under which those values transform fixes both the field's kind and the spin of the particles it will carry:

| field | transformation law | spin | quanta |
| --- | --- | --- | --- |
| scalar $\phi(x)$ | $\phi'(x') = \phi(x)$ — invariant | $0$ | Higgs, pion |
| vector $A^\mu(x)$ | $A'^\mu(x') = \Lambda^\mu{}_{\nu}\,A^\nu(x)$ | $1$ | photon |
| spinor $\psi(x)$ | $\psi'(x') = S(\Lambda)\,\psi(x)$ | $\tfrac{1}{2}$ | electron |

Each row comes with its wave equation, and the correspondence is forced rather than memorized. Once a field transforms by a fixed representation, we can build a relativistic wave equation only from combinations that are themselves Lorentz-invariant, or that transform consistently with the field ([Special Relativity §6](special-relativity.md#_6-metric-tensor-covariance-and-contravariance)). For each row, the simplest such equation is essentially unique.

The scalar offers only $\phi$ itself, so its equation is built from the one Lorentz scalar a derivative can form, $\Box = \partial_\mu\partial^\mu = \partial_t^2 - \nabla^2$:

$$\left(\Box + \frac{m^2}{\hbar^2}\right)\phi = 0,$$

which is the Klein–Gordon equation of [Relativistic QM §2](relativistic-qm.md#_2-klein-gordon). That page derived it from the exact relation $E^2 = \mathbf p^2 + m^2$ and rejected it as a single-particle wave equation because its probability density came out negative. As a *classical field equation* the Klein–Gordon equation has no such flaw, so here the rejection dissolves rather than gets repaired: a classical $\phi$ carries energy and momentum, not probability, and no positivity condition applies to it.

The spinor transforms by $S(\Lambda)$, and the matrices $S(\Lambda)$ are built from the $\gamma^\mu$ of [The Dirac Equation](dirac-equation.md). The same matrices assemble its equation when we contract them with the derivative to make a Lorentz scalar:

$$(i\hbar\,\gamma^\mu\partial_\mu - m)\psi = 0,$$

which is the Dirac equation itself, first order in time and space together. [Relativistic QM §4](relativistic-qm.md#_4-dirac-equation) sought exactly this escape from the Klein–Gordon equation's negative density, with the twist, already familiar, that the first-order equation came with four components and antiparticles attached.

The vector row carries the electromagnetic four-potential, and the field it enters physics through is the tensor $F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu$ of [Special Relativity §8](special-relativity.md#_8-maxwell-equations). In empty space its equation is

$$\partial_\mu F^{\mu\nu} = 0 \quad\Longleftrightarrow\quad \Box A^\nu - \partial^\nu(\partial_\mu A^\mu) = 0,$$

which is Maxwell's equations in free space, the wave equation with $m = 0$, and disturbances propagate at exactly $c$ in every frame. The zero on the right-hand side is physical: the vector family also admits a massive equation, $\partial_\mu F^{\mu\nu} + \tfrac{m^2}{\hbar^2}A^\nu = 0$, and the photon's masslessness is read off which member of the family light obeys.

So the table is closed on the left as well as the right: one transformation law, one wave equation, one spin, one species of quantum. The sequence met all three equations before, but as candidates for a different job, wave equations of a single particle: the Klein–Gordon equation was tried and rejected ([Relativistic QM §2](relativistic-qm.md#_2-klein-gordon)), the Dirac equation tried and triumphant ([The Dirac Equation](dirac-equation.md)), and Maxwell was never a particle equation at all. In this table they return in their original role as equations of fields, and the single-particle readings of the previous pages were the borrowings. Spin comes from transformation, the lesson of [§5](dirac-equation.md#_5-spinors-transformations), and the table reads as a table of contents for particle physics, with one row per species of carrier. One example runs ahead of the story: the Higgs field has not been met in the sequence so far. It is a scalar field of the interacting theory, and its turn comes later on this page.

### What the table does not cover

The classification by Lorentz transformation continues beyond these three rows, into field types above spin $1$ that no confirmed particle fills. The rows the table does carry describe **elementary** fields only, and that restriction matters. Composite particles fill in other spins (the $\Delta$ baryon carries spin $\tfrac{3}{2}$, and nuclei and atoms higher still), but they take no independent row. The pion already sitting in the scalar row is the standing example, because its field is an effective description assembled from the quark fields beneath it, not a representation of the Lorentz group in its own right.

### Second quantization

The quantum step has a name, and the name counts the quantizations. [First Quantization](first-quantization.md) turned a particle's classical quantities, position and momentum and energy, into operators acting on a wave function. The promotion of the previous section quantizes once more, one level up: the wave function's own coefficients become operators. This is **second quantization**, and it applies to every row of the table. Each classical field becomes an operator-valued function of spacetime, $\hat\phi(x)$, $\hat A^\mu(x)$, $\hat\psi(x)$ (strictly, operator-valued distributions, since the momentum integrals are what make them well-defined), acting on the state space to create and annihilate the field's quanta. The name is slightly misleading, and the misleading part is instructive. Nothing is quantized twice; a different object, the classical field rather than the classical particle, is quantized once. Read that way, the outcome is concrete: there is one field per particle species, and a particle is what that field's creation operator produces from the vacuum, so $\hat a_s^\dagger(\mathbf p)\,|0\rangle$ is a state with one electron of momentum $\mathbf p$ and spin $s$. Electrons and positrons come from $\hat\psi$'s operators, photons from $\hat A^\mu$'s, and the Higgs from $\hat\phi$'s.

### Choosing a picture

A quantum field can live in either picture, and the choice decides which object carries the spacetime labels, the state or the operators. The previous pages never faced the choice squarely: [The Dirac Equation §2](dirac-equation.md#_2-conservation-and-commutators) established that conservation means commutation with the Hamiltonian, and proved it with the equation of motion $d\hat A/dt = \tfrac{i}{\hbar}[\hat H, \hat A]$, an equation that already carries the time on the operator without presenting that as a choice. Here the choice is explicit. In the **Schrödinger picture** the states evolve and the operators stand still,

$$|\Psi_S(t)\rangle = e^{-i\hat H t/\hbar}\,|\Psi_S(0)\rangle, \qquad \hat O_S \;\text{ fixed};$$

in the **Heisenberg picture** the states stand still and the operators evolve,

$$|\Psi_H\rangle \;\text{ fixed}, \qquad \hat\phi(t, \mathbf x) = e^{i\hat H t/\hbar}\,\hat\phi(0, \mathbf x)\,e^{-i\hat H t/\hbar}.$$

Note where the plus sign comes from. The Schrödinger equation evolves only the ket, using $e^{-i\hat H t/\hbar}$, the time-evolution operator of [First Quantization](first-quantization.md). Its adjoint evolves the bra, $\langle\Psi(t)| = \langle\Psi(0)|\,e^{+i\hat H t/\hbar}$, so the plus-signed factor was present all along, on the left of every expectation value. The Heisenberg formula moves both factors from the state onto the operator, forming the same sandwich that [The Dirac Equation §2](dirac-equation.md#_2-conservation-and-commutators) differentiated to get its equation of motion. Every prediction of the theory is an expectation value, and the two pictures agree on every one of them,

$$\langle\Psi_S(t)|\,\hat O_S\,|\Psi_S(t)\rangle = \langle\Psi_H|\,\hat O_H(t)\,|\Psi_H\rangle,$$

so the choice between pictures is bookkeeping rather than physics. Which bookkeeping to adopt is a question of convenience, and relativity has a strong preference, as the Why Heisenberg section explains.

### State versus field

The promotion moves the spacetime labels from the state to the operators. The notation hides this structural change, because $\hat\psi(x)$ still looks like the old $\psi(x)$. In wave mechanics the state carried the labels: $\psi(\mathbf x)$ was an amplitude at every point of space, and the operators $\hat{\mathbf x}$, $\hat{\mathbf p}$, and $\hat H$ acted on that function. After the promotion the direction reverses. The **state** $|\Psi\rangle$ is a vector with no spacetime label of its own; it records only what it contains, "the vacuum" or "one electron of momentum $\mathbf p$" or "two photons", never where or when. The **field** $\hat\psi(x)$ is the object spread over spacetime, with one operator attached to every point. And because the states are no longer functions of position, $\hat{\mathbf x}$, which multiplies by $\mathbf x$, has nothing left to act on: position survives only as the label $x$ carried by the fields.

### Building one-particle states

States get built by applying fields to the vacuum, so it is worth doing one application in full. Apply the adjoint field to $|0\rangle$ and substitute the promoted expansion above. The halves separate: the annihilation half dies on the vacuum, $\hat b_s(p)\,|0\rangle = 0$, and the creation half survives,

$$\hat\psi^\dagger(x)\,|0\rangle \;=\; \sum_s\int \frac{d^3p}{(2\pi\hbar)^3}\,\frac{1}{\sqrt{2E_p}}\;u_s^\dagger(p)\,e^{+ip\cdot x/\hbar}\,\hat a_s^\dagger(p)\,|0\rangle.$$

Every term carries exactly one $\hat a_s^\dagger(p)$, which creates an electron with momentum $\mathbf p$ and spin $s$. So $\hat\psi^\dagger(x)|0\rangle$ is a one-electron state, a superposition over all momenta, with the electron created at the point $x$. The same computation with $\hat\psi$ kills the $\hat a_s(p)$ half and keeps the $\hat b_s^\dagger$ half, so $\hat\psi(x)|0\rangle$ is a one-positron state. This is the basic vocabulary of QFT read literally: *a one-electron state* means $\hat a_s^\dagger(p)\,|0\rangle$, or a superposition of these. The left-hand side assembles such a superposition, and the state space of the construction below takes it as its building block.

### Why Heisenberg

Carried into a relativistic theory, the Schrödinger picture uses time in a way that Lorentz invariance cannot sanction. The trouble is visible in its evolution equation, $i\hbar\,\partial_t|\Psi_S(t)\rangle = \hat H|\Psi_S(t)\rangle$, which is first order in $t$ and elevates one observer's time coordinate to the parameter of all change; the state it defines is an object at a time. What such a state becomes in field theory makes the price concrete. Wave mechanics carried one amplitude per position of one particle, $\psi(\mathbf x)$; many-particle mechanics carried one amplitude per configuration, $\psi(\mathbf x_1, \ldots, \mathbf x_N)$; field theory escalates once more,

$$\psi(\mathbf x) \;\longrightarrow\; \psi(\mathbf x_1, \ldots, \mathbf x_N) \;\longrightarrow\; \Psi[\varphi(\mathbf x)],$$

one amplitude per whole configuration $\varphi(\mathbf x)$ of the field at one instant of time, an amplitude on the space of functions. The construction is legitimate, but "all of space at one instant" is not a Lorentz-invariant notion, and neither is a state defined that way, because a boost mixes space with time: what one observer calls all of space at the instant $t$ is, for another, a spread over earlier and later times. The sequence has met this obstruction before. [Relativistic QM §4](relativistic-qm.md#_4-dirac-equation) required that a first-order-in-time equation be first order in space as well, and the Dirac equation complied. But that compliance belongs to the equation, not to the picture, so a Schrödinger state of the Dirac field is still defined at one frame's times, however covariant the equation it obeys. The Heisenberg picture dissolves the problem by moving the coordinates to where transformations can reach them. The states are fixed, the operators carry the labels, and a Lorentz transformation acts on the label, $\hat U(\Lambda)\,\hat\phi(x)\,\hat U^{-1}(\Lambda) = \hat\phi(\Lambda x)$, which is the quantum version of the table's transformation laws, with the vector and spinor rows acquiring their $\Lambda$ and $S(\Lambda)$ alongside. The state never moves: in the Heisenberg view the wave function is fixed once and for all, and all of the dynamics rides on the fields. For the free theory nothing is lost by that stillness, because free evolution creates and destroys nothing.

One further fact belongs here, to be confirmed rather than assumed: the wave equations survive the promotion. The operator $\hat\phi(x)$ obeys the Klein–Gordon equation of [Relativistic QM §2](relativistic-qm.md#_2-klein-gordon), and the operator $\hat\psi(x)$ obeys the Dirac equation of [The Dirac Equation](dirac-equation.md). The equations of the previous pages were field equations all along.

The table even foreshadows the algebra choice that the previous section left open, because the rows quantize differently: integer-spin rows with commutators, half-integer rows with anticommutators. That correlation of spin and statistics arrives with what follows; here it stands as a promise.

Everything so far has been the promotion, the expansion's coefficients turned into operators with assigned duties. Two choices are still open, and fixing them turns the promoted expansion into a working theory. First, the algebra: will the operators obey commutators or anticommutators? Second, the Hamiltonian: when we build it from these operators, will the energy come out bounded below, so that the negative-energy solutions of [Relativistic QM §3](relativistic-qm.md#_3-negative-energy-and-probability) are finally accounted for? The [next page](qft-action.md) settles the algebra for the scalar field $\hat\phi$, the simplest case with no spin to keep track of, and extracts the Hamiltonian that the second question is about. The spinor and vector rows of the table get their answers the same way.
