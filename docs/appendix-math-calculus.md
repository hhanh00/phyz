# Math Refresher: Calculus

These appendix pages collect the mathematical tools the rest of the site uses. Each tool gets a definition and one example, plus a pointer to where it first appears. A reader meeting calculus for the first time can follow from these pages; a reader who has seen it can skim.

## 1. Derivatives

A **derivative** measures how fast a quantity changes. For a function $q(t)$, the derivative

$$q'(t) = \frac{dq}{dt} = \lim_{h\to0}\frac{q(t+h)-q(t)}{h}$$

is the slope of its graph, or the rate at which $q$ changes per unit change in $t$. A dot abbreviates a time derivative, $\dot q = dq/dt$.

**Example.** For $q(t)=t^2$, the change over a small interval is $(t+h)^2-t^2=2th+h^2$. Dividing by $h$ and letting $h\to0$ leaves $2t$, so $\dot q=2t$. This is why [Classical Mechanics](classical-mechanics.md) describes a particle's velocity as $\dot q$ and its acceleration as $\ddot q$.

A derivative can be negative or zero. Zero means the quantity is momentarily not changing; this is the condition that marks a maximum or minimum of a function.

## 2. Partial derivatives

A quantity often depends on several variables at once, such as the Lagrangian $L(q,\dot q,t)$. A **partial derivative** differentiates with respect to one variable while holding the others fixed:

$$\frac{\partial L}{\partial \dot q} = \left.\frac{dL}{d\dot q}\right|_{q,t\ \text{fixed}}.$$

We use the curly $\partial$ to distinguish this from a full derivative $\frac{d}{dt}$, which tracks how a quantity changes when *everything* that depends on time changes.

**Example.** For $L=\tfrac12 m\dot q^2-V(q)$, treat $\dot q$ and $q$ as independent variables. Then

$$\frac{\partial L}{\partial \dot q}=m\dot q, \qquad \frac{\partial L}{\partial q}=-V'(q).$$

Both derivatives appear in the Euler–Lagrange equation on [Classical Mechanics](classical-mechanics.md#_2-lagrangian-and-the-euler-lagrange-derivation):

$$\frac{d}{dt}\left(\frac{\partial L}{\partial \dot q}\right) - \frac{\partial L}{\partial q} = 0.$$

The same partial-derivative operation acts on a *field* $\phi(t,\mathbf x)$ on the [Action page](qft-action.md), where the independent variables are $\phi$ and each derivative $\partial_\mu\phi$.

## 3. The chain rule

When one variable depends on another, their rates of change compose. For $f(q(t))$,

$$\frac{df}{dt}=\frac{df}{dq}\,\frac{dq}{dt}.$$

With several variables, the full time derivative collects one term per path of dependence:

$$\frac{df}{dt}=\frac{\partial f}{\partial q}\,\dot q+\frac{\partial f}{\partial t}.$$

**Example.** The [Lorentz time transformation](special-relativity.md) $t'=\gamma(t-vx/c^2)$ mixes $t$ and $x$, so time derivatives transform with both terms of the chain rule. The same rule converts between a frame's time derivative and the derivative along a particle's own clock when the [Lorentz factor](special-relativity.md) appears.

## 4. Integrals and integration by parts

An **integral** adds a quantity over a range. The definite integral $\int_a^b f(t)\,dt$ accumulates $f$ between $t=a$ and $t=b$; the indefinite integral is the reverse of differentiating.

The [action](classical-mechanics.md) is a definite integral, $S=\int L\,dt$. To find which path makes it stationary, we move a derivative off the variation using **integration by parts**. For two functions $u(t)$ and $v(t)$,

$$\int_a^b u\,\frac{dv}{dt}\,dt = \big[u v\big]_a^b - \int_a^b v\,\frac{du}{dt}\,dt,$$

where $[uv]_a^b = u(b)v(b)-u(a)v(a)$ is the **boundary term**.

**Example.** In the variation of the action, the velocity term is $\int \frac{\partial L}{\partial\dot q}\,\frac{d}{dt}(\delta q)\,dt$. Taking $u=\frac{\partial L}{\partial\dot q}$ and $v=\delta q$ moves the derivative onto $u$. The boundary term vanishes because the variation $\delta q$ is chosen to be zero at the endpoints. What remains is $\int\left(\frac{d}{dt}\frac{\partial L}{\partial\dot q}\right)\delta q\,dt$, which produces the Euler–Lagrange equation. The same step runs over every spacetime direction when deriving the [field equation](qft-action.md).

## 5. Taylor expansion

A smooth function near a point agrees with a polynomial built from its derivatives there:

$$f(x)\approx f(x_0)+f'(x_0)\,(x-x_0)+\tfrac12 f''(x_0)\,(x-x_0)^2+\cdots$$

Each added term fixes one more derivative at $x_0$.

**Example.** Near a minimum of a potential, $V'(x_0)=0$, so the linear term drops out and

$$V(x)\approx V(x_0)+\tfrac12 V''(x_0)(x-x_0)^2.$$

The [harmonic oscillator](harmonic-oscillator.md) is exactly this quadratic approximation. A second use appears in [Special Relativity](special-relativity.md): the Lorentz factor obeys $\gamma\approx 1+v^2/(2c^2)$ at small speed, which recovers the non-relativistic kinetic energy.

## 6. Vector calculus

Fields vary over space, so we need derivatives that act on all three directions at once. Write $\mathbf v=(v_x,v_y,v_z)$ and $\nabla=(\partial_x,\partial_y,\partial_z)$.

- **Gradient**, $\nabla f=(\partial_x f,\partial_y f,\partial_z f)$: the vector pointing in the direction $f$ increases most steeply.
- **Divergence**, $\nabla\cdot\mathbf v=\partial_x v_x+\partial_y v_y+\partial_z v_z$: the net outward flow of $\mathbf v$ per unit volume.
- **Curl**, $\nabla\times\mathbf v$: a vector measuring circulation of $\mathbf v$ around each axis.
- **Laplacian**, $\nabla^2 f=\nabla\cdot(\nabla f)=\partial_x^2 f+\partial_y^2 f+\partial_z^2 f$: the divergence of the gradient.

These appear in the [Maxwell equations](special-relativity.md#_8-maxwell-equations): $\nabla\cdot\mathbf E=\rho$, $\nabla\times\mathbf E=-\partial_t\mathbf B$, and so on. The relativistic wave operator combines a time derivative with the Laplacian,

$$\Box = \partial_t^2-\nabla^2,$$

called the **d'Alembertian**, which appears in the [Klein–Gordon equation](relativistic-qm.md).

---

Next: [Complex Numbers](appendix-math-complex.md)
