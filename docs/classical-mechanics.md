# Classical Mechanics

## 1. Newtonian Formulation

Newton's second law, $F = ma$, relates a particle's acceleration to the force on it. Given its initial position and velocity, we can solve for its later motion. For ordinary well-posed force laws, those initial conditions determine a unique trajectory.

The equation is second order in position. Integrating once gives the velocity; integrating again gives the position. For constrained motion, such as a bead on a wire, we must also account for the forces that keep the particle on its allowed path. Generalized coordinates make these constraints easier to handle.

![For constant force, acceleration is constant, velocity changes linearly, and position changes quadratically.](./manim/newton-motion.png)

*For constant force, acceleration is constant, velocity changes linearly, and position changes quadratically.*

## 2. Lagrangian and the Euler–Lagrange Derivation

For a pendulum, an angle describes the motion more directly than three Cartesian coordinates. The Lagrangian method works with such **generalized coordinates** $q$, which specify the allowed configurations of the system.

For the usual kinetic and potential energies, define $L = T - V$. The **action** is the integral of the Lagrangian along a proposed path:

$$S = \int L(q, \dot q, t)\, dt$$

The principle of **stationary action** states that the physical path makes the first-order change in $S$ vanish when we vary the path while keeping its endpoints fixed. Stationary does not necessarily mean a minimum.

To obtain an equation we can solve, perturb $q(t)$ by a small function that vanishes at the endpoints. Expand $S$ to first order, then integrate the term containing the velocity variation by parts. The boundary term vanishes. Requiring the remaining integral to vanish for every allowed variation gives the **Euler–Lagrange equation**,

$$\frac{d}{dt}\left(\frac{\partial L}{\partial \dot q}\right) - \frac{\partial L}{\partial q} = 0$$

with one equation for each generalized coordinate. For $L = \tfrac12m\dot q^2-V(q)$, it gives $m\ddot q=-\partial V/\partial q$, Newton's second law. The same procedure works for angular coordinates and, later, for fields.

![Vary a free-particle path while fixing its endpoints. The physical path makes the first-order action variation vanish.](./manim/stationary-action-paths.png)

*Vary a free-particle path while fixing its endpoints. The physical path makes the first-order action variation vanish.*

## 3. Hamiltonian and State Space

To describe the state using position and momentum, define the **conjugate momentum** $p = \partial L/\partial \dot q$. Then form the Hamiltonian $H(q,p) = p\dot q - L$, expressing $\dot q$ in terms of $q$ and $p$. This change of variables is a **Legendre transform**.

For a regular Lagrangian, the second-order Euler–Lagrange equation becomes two first-order **Hamilton equations**:

$$\dot q = \frac{\partial H}{\partial p}, \qquad \dot p = -\frac{\partial H}{\partial q}$$

For the usual kinetic energy and a velocity-independent potential, $H$ is the total energy $T+V$. Its independent variables are position and momentum.

The pair $(q,p)$ specifies a point in **phase space**, the space of classical states. Position alone specifies the configuration; momentum also specifies how it is moving. Hamilton's equations determine a trajectory through phase space, and uniqueness prevents distinct trajectories from crossing at the same time.

Quantum mechanics keeps the idea of a state evolving under a Hamiltonian. We will replace phase-space points with vectors in Hilbert space and replace the classical Hamiltonian with an operator.

![Two states can have the same position and opposite momenta. Phase space distinguishes them.](./manim/phase-space-states.png)

*Two states can have the same position and opposite momenta. Phase space distinguishes them.*

## 4. The Poisson Bracket

We can express Hamiltonian evolution in a form that carries over to quantum mechanics. For two quantities $f(q,p)$ and $g(q,p)$, define their **Poisson bracket**:

$$\{f, g\} = \frac{\partial f}{\partial q}\frac{\partial g}{\partial p} - \frac{\partial f}{\partial p}\frac{\partial g}{\partial q}$$

For several coordinates, sum this expression over each conjugate pair. The bracket is bilinear, meaning linear in either argument, and antisymmetric: exchanging $f$ and $g$ reverses its sign. It also satisfies the Jacobi identity, a consistency relation between nested brackets.

For a quantity with no explicit time dependence, Hamilton's equations give $\dot f = \{f,H\}$. Thus the bracket with the Hamiltonian determines its rate of change. In particular, $\{q,p\}=1$.

*Why it matters later*: canonical quantization uses $\{\cdot,\cdot\} \to \frac{1}{i\hbar}[\cdot,\cdot]$. The classical relation $\{q,p\}=1$ becomes the quantum relation $[\hat q,\hat p]=i\hbar$. This is a starting prescription; operator ordering can complicate the correspondence for more general quantities.

---

Next: [First Quantization](./first-quantization.md)
