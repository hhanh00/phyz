# Quantum Field Theory

This page continues from [The Dirac Equation](dirac-equation.md): the bridge promised at its end is crossed here. What the single-particle equation could not do — describing particles that are created and destroyed — requires a change of object: the wave function is not the fundamental object of the theory, it is a coefficient. The fundamental objects are **field operators** — operator-valued functions of space and time that create and annihilate particles. The negative-energy branch of the Dirac equation is then not a problem to be explained away: the hole picture of its §4 is replaced by creation and annihilation operators acting on the vacuum, the antiparticle of its §3 is the electron field's partner, and the physics of the positron follows from the mathematics of the field.

## Recap of Dirac Equation

The point of departure is the general solution at the end of [The Dirac Equation §6](dirac-equation.md#_6-general-solution). For the free equation,

$$\psi(x) = \sum_{s=1}^{2} \int \frac{d^3p}{(2\pi\hbar)^3}\,\frac{1}{\sqrt{2E_p}}\left[a_s(p)\,u_s(p)\,e^{-ip\cdot x/\hbar} + b_s^*(p)\,v_s(p)\,e^{+ip\cdot x/\hbar}\right],$$

with $p\cdot x = E_p t - \mathbf p\cdot\mathbf x$ and $E_p = \sqrt{\mathbf p^2 + m^2}$. The formula holds two branches — the $u$-terms at positive frequency, the electron; the $v$-terms at negative frequency, the branch [§3](dirac-equation.md#_3-antiparticles) identified as the antiparticle and [§4](dirac-equation.md#_4-negative-energy-solutions) could only interpret as holes in a sea — and two coefficients, $a_s(p)$ and $b_s^*(p)$: complex numbers, the amplitudes fixed by the initial conditions. Everything on this page happens inside this formula.

### The promotion

A number can weight a branch; it cannot create or destroy a particle — and creation and destruction are exactly what the negative-frequency branch demands ([§4](dirac-equation.md#_4-negative-energy-solutions)). The way out was announced at the end of [§6](dirac-equation.md#_6-general-solution): promote the coefficients to operators,

$$a_s(p) \to \hat a_s(p), \qquad b_s^*(p) \to \hat b_s^\dagger(p),$$

where $\hat a_s(p)$ annihilates an electron of momentum $\mathbf p$ and spin $s$, and $\hat b_s^\dagger(p)$ creates a positron of the same momentum and spin. The star on $b_s^*$ was no decoration: when numbers become operators, the complex conjugate becomes the adjoint, ${}^* \to {}^\dagger$ — [§6](dirac-equation.md#_6-general-solution) wrote the second coefficient conjugated because the notation was already the shape of the quantized field. After the promotion the same expansion reads

$$\hat\psi(x) = \sum_{s=1}^{2} \int \frac{d^3p}{(2\pi\hbar)^3}\,\frac{1}{\sqrt{2E_p}}\left[\hat a_s(p)\,u_s(p)\,e^{-ip\cdot x/\hbar} + \hat b_s^\dagger(p)\,v_s(p)\,e^{+ip\cdot x/\hbar}\right],$$

and the object has changed kind: not a wave function but the **electron field operator**. Grouped by frequency, $\hat\psi = \hat\psi^{(+)} + \hat\psi^{(-)}$, with the adjoint field $\hat\psi^\dagger$ carrying the reversed halves — the full dictionary:

| half | operator | plane wave | action |
| --- | --- | --- | --- |
| $\hat\psi^{(+)}$ (positive frequency) | $\hat a_s(p)$ | $e^{-ip\cdot x/\hbar}$ | annihilates an electron |
| $\hat\psi^{(-)}$ (negative frequency) | $\hat b_s^\dagger(p)$ | $e^{+ip\cdot x/\hbar}$ | creates a positron |
| $\hat\psi^{(+)\dagger}$ | $\hat a_s^\dagger(p)$ | $e^{+ip\cdot x/\hbar}$ | creates an electron |
| $\hat\psi^{(-)\dagger}$ | $\hat b_s(p)$ | $e^{-ip\cdot x/\hbar}$ | annihilates a positron |

The field and its adjoint are each other's mirror: each carries one annihilation half and one creation half. The negative-frequency terms have not been removed — they have been reassigned, from states an electron might fall into to the operators that create antiparticles.

Stated once without the spinor dressing — the construction below builds it that way, for the scalar field $\hat\phi$ (normalization suppressed, $k\cdot x = E_k t - \mathbf k\cdot\mathbf x$, $E_k = \sqrt{\mathbf k^2 + m^2}$):

$$\hat\phi(x) = \int \frac{d^3k}{(2\pi\hbar)^3}\left[\hat a(\mathbf k)\,e^{-ik\cdot x/\hbar} + \hat b^\dagger(\mathbf k)\,e^{+ik\cdot x/\hbar}\right], \qquad \hat\phi^\dagger(x) = \int \frac{d^3k}{(2\pi\hbar)^3}\left[\hat a^\dagger(\mathbf k)\,e^{+ik\cdot x/\hbar} + \hat b(\mathbf k)\,e^{-ik\cdot x/\hbar}\right],$$

so $\hat a$ annihilates a particle and $\hat b^\dagger$ creates an antiparticle inside the field, while $\hat a^\dagger$ creates a particle and $\hat b$ annihilates an antiparticle inside its adjoint. The doubling of coefficients is charge made visible: a field equal to its own adjoint — a real field, $\hat\phi^\dagger = \hat\phi$ — has no $\hat b$'s at all and describes a particle that is its own antiparticle; only when particle and antiparticle are distinct, opposite charges, does the field need both pairs.

### What the promotion does not yet have

The promotion has been asserted, not constructed. Three things remain to be built. The space the operators act on: states of any particle number, built from a vacuum $|0\rangle$ annihilated by every $\hat a$ and $\hat b$ — the object that replaces the filled sea of [§4](dirac-equation.md#_4-negative-energy-solutions), on which pair annihilation is simply the operator statement $\hat a\,\hat b\,|e^-\,e^+\rangle = |0\rangle$. The algebra the operators obey: commutators or anticommutators, the choice that separates bosons from fermions, and the answer to the statistics caveat of [§4](dirac-equation.md#_4-negative-energy-solutions). And the Hamiltonian: rebuilt from the promoted operators, it must come out bounded below, the negative-energy branch of [Relativistic QM §3](relativistic-qm.md#_3-negative-energy-and-probability) finally accounted for. That construction is the work of the sections below, after one more piece of ground: what a field is, and in which picture it lives.

## Fields

What kind of object is being built? Fields come in kinds, classified the way the wave functions of the previous pages were — by how they transform under Lorentz transformations ([The Dirac Equation §5](dirac-equation.md#_5-spinors-transformations)). A classical field assigns a value to every point of spacetime, and the representation under which those values transform fixes both the field's kind and the spin of the particles it will carry:

| field | transformation law | spin | quanta |
| --- | --- | --- | --- |
| scalar $\phi(x)$ | $\phi'(x') = \phi(x)$ — invariant | $0$ | Higgs, pion |
| vector $A^\mu(x)$ | $A'^\mu(x') = \Lambda^\mu{}_{\nu}\,A^\nu(x)$ | $1$ | photon |
| spinor $\psi(x)$ | $\psi'(x') = S(\Lambda)\,\psi(x)$ | $\tfrac{1}{2}$ | electron |

Each row comes with its wave equation, and the correspondence is not an inventory to memorize — it is forced. Once a field transforms by a fixed representation, a relativistic wave equation must be built from that field in combinations that are themselves Lorentz-invariant (or transform consistently with it, [Special Relativity §7](special-relativity.md#_7-metric-tensor-covariance-and-contravariance)), and for each row the simplest such equation is essentially unique.

The scalar offers only $\phi$ itself, so its equation is built from the one Lorentz scalar a derivative can form, $\Box = \partial_t^2 - \nabla^2$:

$$\left(\Box + \frac{m^2}{\hbar^2}\right)\phi = 0,$$

the Klein–Gordon equation of [Relativistic QM §2](relativistic-qm.md#_2-klein-gordon) — derived there from the exact relation $E^2 = \mathbf p^2 + m^2$ and rejected as a single-particle wave equation because its probability density came out negative. Here the rejection dissolves rather than gets repaired: as a *classical field equation* the Klein–Gordon equation has no flaw — a classical $\phi$ carries energy and momentum, not probability, and nothing in the theory asked it to be positive.

The spinor transforms by $S(\Lambda)$, and the matrices $S(\Lambda)$ are built from the $\gamma^\mu$ of [The Dirac Equation](dirac-equation.md) — the same matrices assemble its equation, contracted with the derivative to make a Lorentz scalar:

$$(i\hbar\,\gamma^\mu\partial_\mu - m)\psi = 0,$$

the Dirac equation itself: first order in time and space together, the escape from the Klein–Gordon equation's negative density that [Relativistic QM §4](relativistic-qm.md#_4-dirac-equation) sought — with the twist, already familiar, that the first-order equation came with four components and antiparticles attached.

The vector row carries the electromagnetic four-potential, and the field it enters physics through is the tensor $F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu$ of [Special Relativity §9](special-relativity.md#_9-maxwell-equations). In empty space its equation is

$$\partial_\mu F^{\mu\nu} = 0 \quad\Longleftrightarrow\quad \Box A^\nu - \partial^\nu(\partial_\mu A^\mu) = 0,$$

Maxwell's equations in free space — the wave equation with $m = 0$, disturbances propagating at exactly $c$ in every frame. The zero is physical: the vector family also admits a massive equation, $\partial_\mu F^{\mu\nu} + \tfrac{m^2}{\hbar^2}A^\nu = 0$, and the photon's masslessness is read off which member of the family light obeys.

So the table is closed on the left as well as the right: one transformation law, one wave equation, one spin, one species of quantum. The sequence met all three equations already — but as candidates for a different job, wave equations of a single particle: the Klein–Gordon tried and rejected ([Relativistic QM §2](relativistic-qm.md#_2-klein-gordon)), the Dirac tried and triumphant ([The Dirac Equation](dirac-equation.md)), Maxwell never a particle equation at all. In this table they return in their original role — equations of fields — and the single-particle readings of the previous pages were the borrowings. Spin comes from transformation: the lesson of [§5](dirac-equation.md#_5-spinors-transformations), read as a table of contents for particle physics — one row per species of carrier. One example runs ahead of the story: the Higgs field has not been met in the sequence so far — it is a scalar field of the interacting theory, and its turn comes later on this page.

### How much does the table cover?

Not everything — the classification by Lorentz transformation continues beyond these three rows, into field types above spin $1$ that no confirmed particle fills. What the table does carry, it carries as **elementary** fields, and that restriction matters: composite particles fill in other spins — the $\Delta$ baryon carries spin $\tfrac{3}{2}$, nuclei and atoms higher still — but they take no independent row. The pion already sitting in the scalar row is the standing example: its field is an effective description assembled from the quark fields beneath it, not its own representation of the Lorentz group.

### Second quantization

The quantum step has a name, and the name counts the quantizations. [First Quantization](first-quantization.md) turned a particle's classical quantities — position, momentum, energy — into operators acting on a wave function. The promotion of the previous section quantizes once more, one level up: the wave function's own coefficients become operators. This is **second quantization**, and it applies to every row of the table: each classical field becomes an operator-valued function of spacetime, $\hat\phi(x)$, $\hat A^\mu(x)$, $\hat\psi(x)$ (strictly, operator-valued distributions — the momentum integrals are what make them well-defined), acting on the state space to create and annihilate the field's quanta. The name is slightly misleading, and the misleading part is instructive: nothing is quantized twice — it is a different object, the classical field rather than the classical particle, quantized once. Read that way, the outcome is concrete: one field per particle species, and a particle is what that field's creation operator produces from the vacuum — $\hat a_s^\dagger(\mathbf p)\,|0\rangle$ is a state with one electron of momentum $\mathbf p$ and spin $s$. Electrons and positrons come from $\hat\psi$'s operators, photons from $\hat A^\mu$'s, the Higgs from $\hat\phi$'s.

### Heisenberg or Schrödinger

In which picture does a quantum field live? The previous pages never faced the question squarely. [The Dirac Equation §2](dirac-equation.md#_2-conservation-and-commutators) established that conservation means commutation with the Hamiltonian, proving it with the equation of motion $d\hat A/dt = \tfrac{i}{\hbar}[\hat H, \hat A]$ — an equation that already carries the time on the operator, without presenting that as a choice. Here the choice is made explicit, and in field theory it decides which object carries the spacetime labels: the state, or the operators. In the **Schrödinger picture** the states evolve and the operators stand still,

$$|\Psi_S(t)\rangle = e^{-i\hat H t/\hbar}\,|\Psi_S(0)\rangle, \qquad \hat O_S \;\text{ fixed};$$

in the **Heisenberg picture** the states stand still and the operators evolve,

$$|\Psi_H\rangle \;\text{ fixed}, \qquad \hat\phi(t, \mathbf x) = e^{i\hat H t/\hbar}\,\hat\phi(0, \mathbf x)\,e^{-i\hat H t/\hbar}.$$

Note where the plus sign comes from. The Schrödinger equation itself evolves only the ket, with $e^{-i\hat H t/\hbar}$ — the time-evolution operator of [First Quantization](first-quantization.md). Its adjoint evolves the bra, $\langle\Psi(t)| = \langle\Psi(0)|\,e^{+i\hat H t/\hbar}$, so the plus-signed factor was present all along, on the left of every expectation value; the Heisenberg formula moves both factors from the state onto the operator — the same sandwich [The Dirac Equation §2](dirac-equation.md#_2-conservation-and-commutators) differentiated to get its equation of motion. Every prediction of the theory is an expectation value, and the two pictures agree on every one of them,

$$\langle\Psi_S(t)|\,\hat O_S\,|\Psi_S(t)\rangle = \langle\Psi_H|\,\hat O_H(t)\,|\Psi_H\rangle,$$

so the split is bookkeeping, not physics. Which bookkeeping to adopt is a question of convenience — and relativity has a strong preference.

### State versus field

The promotion moves the spacetime labels from the state to the operators — a structural change the notation hides, because $\hat\psi(x)$ still looks like the old $\psi(x)$. In wave mechanics the state carried the labels: $\psi(\mathbf x)$ was an amplitude at every point of space, and the operators — $\hat{\mathbf x}$, $\hat{\mathbf p}$, $\hat H$ — acted on that function. After the promotion the direction reverses. The **state** $|\Psi\rangle$ is a vector with no spacetime label of its own: it records only what it contains — "the vacuum", "one electron of momentum $\mathbf p$", "two photons" — never where or when. The **field** $\hat\psi(x)$ is the object spread over spacetime: one operator attached to every point. And once the states are no longer functions of position, $\hat{\mathbf x}$ — multiplication by $\mathbf x$ — has nothing left to act on: position survives only as the label $x$ carried by the fields.

### The basic operation

States get built by applying fields to the vacuum, so the application deserves doing once, in full. Apply the adjoint field to $|0\rangle$ and substitute the promoted expansion above: the halves separate — the annihilation half dies on the vacuum, $\hat b_s(p)\,|0\rangle = 0$, the creation half survives,

$$\hat\psi^\dagger(x)\,|0\rangle \;=\; \sum_s\int \frac{d^3p}{(2\pi\hbar)^3}\,\frac{1}{\sqrt{2E_p}}\;u_s^\dagger(p)\,e^{+ip\cdot x/\hbar}\,\hat a_s^\dagger(p)\,|0\rangle.$$

Every term carries exactly one $\hat a_s^\dagger(p)$ — the creation of an electron with momentum $\mathbf p$ and spin $s$ — so $\hat\psi^\dagger(x)|0\rangle$ is a one-electron state: a superposition over all momenta, an electron created at the point $x$. The same computation with $\hat\psi$ kills the $\hat a_s(p)$ half and keeps the $\hat b_s^\dagger$ half: $\hat\psi(x)|0\rangle$ is a one-positron state. This is the basic vocabulary of QFT, read literally: *a one-electron state* means $\hat a_s^\dagger(p)\,|0\rangle$, or a superposition of these — which is what the left-hand side assembles, and what the state space of the construction below takes as its building block.

### Why Heisenberg

Carried into a relativistic theory, the Schrödinger picture uses time in a way that Lorentz invariance cannot sanction. The trouble is visible in its evolution equation, $i\hbar\,\partial_t|\Psi_S(t)\rangle = \hat H|\Psi_S(t)\rangle$: first order in $t$, with $t$ — one observer's time coordinate — elevated to the parameter of all change, and the state it defines is an object *at a time*. What such a state is, in field theory, makes the price concrete: wave mechanics carried one amplitude per position of one particle, $\psi(\mathbf x)$; many-particle mechanics one amplitude per configuration, $\psi(\mathbf x_1, \ldots, \mathbf x_N)$; field theory escalates once more,

$$\psi(\mathbf x) \;\longrightarrow\; \psi(\mathbf x_1, \ldots, \mathbf x_N) \;\longrightarrow\; \Psi[\varphi(\mathbf x)],$$

one amplitude per whole configuration $\varphi(\mathbf x)$ of the field at one instant of time — an amplitude on the space of functions. The construction is legitimate, but "all of space at one instant" is not a Lorentz-invariant notion, and neither is a state defined that way: a boost mixes space with time, so what one observer calls all of space at the instant $t$ is, for another, a spread over earlier and later times. The sequence has met this obstruction before — [Relativistic QM §4](relativistic-qm.md#_4-dirac-equation) required that a first-order-in-time equation be first order in space as well, and the Dirac equation complied. But that compliance belongs to the equation, not to the picture: a Schrödinger state of the Dirac field is still defined at one frame's times, however covariant the equation it obeys. The Heisenberg picture dissolves the problem by moving the coordinates to where transformations can reach them: the states are fixed, the operators carry the labels, and a Lorentz transformation acts on the label, $\hat U(\Lambda)\,\hat\phi(x)\,\hat U^{-1}(\Lambda) = \hat\phi(\Lambda x)$ — the quantum version of the table's transformation laws, with the vector and spinor rows acquiring their $\Lambda$ and $S(\Lambda)$ alongside. The state never moves: in the Heisenberg view the wave function is fixed once and for all, and all of the dynamics rides on the fields. For the free theory nothing is lost by that stillness, since free evolution creates and destroys nothing.

One further fact belongs here, to be confirmed rather than assumed: the wave equations survive the promotion. The operator $\hat\phi(x)$ obeys the Klein–Gordon equation of [Relativistic QM §2](relativistic-qm.md#_2-klein-gordon), and the operator $\hat\psi(x)$ the Dirac equation of [The Dirac Equation](dirac-equation.md) — the equations of the previous pages were field equations all along.

The table even foreshadows the algebra choice the previous section left open: the rows quantize differently — integer-spin rows with commutators, half-integer rows with anticommutators. That correlation of spin and statistics arrives with what follows; here it stands as a promise.

Everything so far has been the promotion — the expansion's coefficients turned into operators with assigned duties. Two choices are still open, and fixing them turns the promoted expansion into a working theory. First, the algebra: do the operators obey commutators or anticommutators — $[\hat a(\mathbf k), \hat a^\dagger(\mathbf k')]$ or $\{\hat a(\mathbf k), \hat a^\dagger(\mathbf k')\}$? Second, the Hamiltonian: built from these operators, does the energy come out bounded below — the negative-energy branch of [Relativistic QM §3](relativistic-qm.md#_3-negative-energy-and-probability) finally accounted for? The next section settles both for the scalar field $\hat\phi$ — the simplest case, no spin to keep track of — and the answers carry over to the spinor and vector rows of the table.

## Principle of Least Action

One more piece of classical machinery, and the previous pages never needed it. [Classical Mechanics §2](classical-mechanics.md#_2-lagrangian-and-the-euler-lagrange-derivation) reframed dynamics as optimization: to every path $q(t)$ between fixed endpoints in time attach the **action**

$$S[q] = \int_{t_1}^{t_2} L(q, \dot q)\,dt, \qquad L = T - V,$$

and demand the true path leave $S$ stationary against every variation that leaves the endpoints fixed. The variation itself was two lines: perturb the path by a small function vanishing at the endpoints, expand to first order, integrate the velocity term by parts — the boundary term dies because the perturbation dies at the endpoints — and demand the remainder vanish for every perturbation. What survives is the Euler–Lagrange equation,

$$\frac{d}{dt}\,\frac{\partial L}{\partial \dot q} - \frac{\partial L}{\partial q} = 0,$$

Newton's law in disguise. And the disguise is the point. The Newtonian formulation names a force and a coordinate; the Lagrangian formulation names only a scalar $L$, and the equation of motion follows mechanically. Nothing in the input knows about vectors, forces, or geometry — a formulation that thin is a formulation relativity can take over whole, and that is exactly what this page needs it for: the promoted theory must get its Hamiltonian — the generator whose commutators defined conservation back in [The Dirac Equation §2](dirac-equation.md#_2-conservation-and-commutators), the thing the negative-energy crisis of [Relativistic QM §3](relativistic-qm.md#_3-negative-energy-and-probability) is about — and the Hamiltonian comes from $L$.

### From particles to fields

The upgrade to a field is one change of integration variable. Mechanics solved for $q(t)$ — a function of time only, the position of the one unknown. A field solves for the *value at every point*: in $\phi(t, \mathbf x)$ the $\mathbf x$ is not an unknown but a fixed address — one degree of freedom per point of space — and as $\mathbf x$ ranges over space its values form a continuum of coordinates, the configuration at one instant being the whole function. So what gets integrated is not a function of time but a **Lagrangian density** $\mathcal{L}(\phi, \partial_\mu\phi)$ over all of spacetime,

$$S[\phi] = \int d^4x\;\mathcal{L}(\phi, \partial_\mu\phi),$$

and the same two-line variation, one more index, returns the Euler–Lagrange equation for the field,

$$\partial_\mu\left(\frac{\partial\mathcal{L}}{\partial(\partial_\mu\phi)}\right) - \frac{\partial\mathcal{L}}{\partial\phi} = 0.$$

What the principle buys in return is precisely what the table above was after. Let $\mathcal{L}$ be a Lorentz scalar built from the field and its derivatives: the action is then a single number every observer agrees on, the stationary configuration cannot depend on a frame, and the equation that comes out is automatically covariant — Lorentz invariance not checked afterward but built into the derivation. Each row of the table's wave equations is the Euler–Lagrange equation of the simplest invariant density its field admits: the scalar's $\mathcal{L} = \tfrac{1}{2}\,(\partial_\mu\phi)(\partial^\mu\phi) - \tfrac{m^2}{2\hbar^2}\,\phi^2$ gives the Klein–Gordon equation, the spinor's $\mathcal{L} = \bar\psi\,(i\hbar\gamma^\mu\partial_\mu - m)\,\psi$ gives the Dirac equation, the vector's $\mathcal{L} = -\tfrac{1}{4}F^{\mu\nu}F_{\mu\nu}$ gives Maxwell with the massless term. The "essentially unique" of the previous section here becomes a computation: write down the simplest scalar density the representation allows, and the wave equation of that row falls out.

The Hamiltonian is extracted the same way as in [Classical Mechanics §3](classical-mechanics.md#_3-hamiltonian-and-state-space), one conjugate momentum per field — $\pi(t, \mathbf x) = \partial\mathcal{L}/\partial\dot\phi$ — and the density

$$\mathcal{H} = \pi\,\dot\phi - \mathcal{L}, \qquad \hat H = \int d^3x\;\mathcal{H},$$

the total energy that the quantum theory will inherit as its operator. Here the tension the Fields section exposed comes to a head, and the honesty is due at once: the asymmetry between $t$ and $\mathbf x$ is real, and the Hamiltonian framework commits to it on purpose. A state is "the condition of the whole system at an instant," and an initial-value problem needs a *now* — a notion no Lorentz-invariant object supplies, since a boost tilts every slicing of spacetime into a different one. The covariant statement of the theory survives intact: the field equation stays symmetric in $t$ and $\mathbf x$ — one operator $\Box$, no distinguished time — and the action is a Lorentz scalar, $t$ and $\mathbf x$ living inside a single $d^4x$. The Hamiltonian is what that statement yields after one slicing is chosen — the definition $\pi = \partial\mathcal{L}/\partial\dot\phi$ already picks out a frame's time derivative. Each inertial observer slices the same solution differently and reads off a different pair $(\phi, \pi)$. A change of frame is a rotation of axes in spacetime — different photographs, one scene — and covariance is the statement that the physics lives in the scene, not in any photograph. The split is a matter of bookkeeping, exactly like the pictures — and both readings come from the same $\mathcal{L}$.

### The geometry of H

[Classical Mechanics §3](classical-mechanics.md#_3-hamiltonian-and-state-space) named the arena **state space**: a system's entire condition at one instant is one point of it, and dynamics is the path that point traces. For a field the point is heavier. The mechanical pair $(q, p)$ becomes the pair of functions $(\phi, \pi)$ — one $q$ and one $p$ per point of space, with $\pi = \partial\mathcal{L}/\partial\dot\phi$ the field version of $p = \partial L/\partial\dot q$. Freeze $t$ and both become functions of $\mathbf x$ alone; that pair $(\phi(\mathbf x), \pi(\mathbf x))$ is one state — the whole configuration at that instant. The space of all such pairs is infinite-dimensional, and a classical history of the field is a curve in it. What moves the point along the curve is $H$. A single scalar on state space, $H = \int d^3x\,\mathcal{H}$ — a number attached to every state, the energy — and at every point it plants a direction: the direction the state must next flow. Hamilton's equations are that direction written coordinate by coordinate, $\dot\phi = \delta H/\delta\pi$, $\dot\pi = -\delta H/\delta\phi$ — functional derivatives in place of partial ones, the mechanical equations unchanged in form. Nothing else is supplied: no force, no law beyond *flow along the arrows H plants*. The physical histories of the field are the flow lines, and determinism is geometric — one point, one arrow, one curve.

![Hamiltonian flow in the $(\phi,\pi)$ plane of one oscillator mode: circles are the states of constant energy, the gray arrows are the directions $H$ assigns, and the orbits close because $H$ is conserved](./manim/hamiltonian-flow.png)

Two readings of $H$ fall out of the flow, and the quantum theory will inherit both. $H$ is the **energy**: a density with no explicit time dependence makes $H$ constant along its own flow — the curve never changes the value of the function that steers it — which is conservation stated as geometry. And $H$ is the **generator of time translations**: flowing along the arrows *is* what moving forward in time means on state space, the Noether statement that the symmetry "shift $t$" is carried by the charge $\int d^3x\,\mathcal{H}$. The operator version of the second reading is already on the page: $\hat\phi(t) = e^{i\hat H t/\hbar}\,\hat\phi(0)\,e^{-i\hat H t/\hbar}$, the Heisenberg formula of the Fields section, is conjugation by the generator — the quantum version of flowing along the classical arrows, on a state space no one draws.

The flow has an algebra, and the algebra is the hinge to the quantum theory. [Classical Mechanics §4](classical-mechanics.md#_4-the-poisson-bracket) paired any two observables on state space with a bracket $\{\cdot, \cdot\}$ — measuring how the flow generated by one displaces the other — and compressed the dynamics to a single line, $\dot F = \{F, H\}$; [First Quantization](first-quantization.md) then fixed the bracket's quantum fate, $\{\cdot, \cdot\} \to \tfrac{1}{i\hbar}[\hat{\cdot}, \hat{\cdot}]$, the rule whose one known case was $\{x, p\} = 1 \to [\hat x, \hat p] = i\hbar$. Run the rule on the field — $\phi$ and $\pi$ are conjugate at every point of space — and the algebra question the page opened with is produced, not posed: $[\hat\phi(t, \mathbf x), \hat\pi(t, \mathbf x')] = i\hbar\,\delta^3(\mathbf x - \mathbf x')$, and mode by mode, each momentum $\mathbf k$ of the free field an oscillator on its own, the oscillator algebra $[\hat a(\mathbf k), \hat a^\dagger(\mathbf k')] \propto \delta^3(\mathbf k - \mathbf k')$ — the commutators the promotion's operators will turn out to obey. The construction below does not choose this algebra; it confirms it. (The half-integer rows will rerun the passage with the bracket's graded replacement — the point where the choice reopens, and the spin-statistics promise comes due.)
