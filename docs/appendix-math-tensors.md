# Math Refresher: Index Notation and Tensors

Relativity mixes time and space into a single object, a four-vector. To write equations that work in every frame, the site uses **index notation**: upper and lower indices, summed in pairs. This page builds that notation in the smallest form needed.

## 1. Why index notation

Group time and position into one object with four entries,

$$x^\mu=(ct,x,y,z),\qquad \mu=0,1,2,3.$$

The index $\mu$ selects which entry; $x^0=ct$ and $x^1=x$. A **four-vector** is any quantity whose four entries transform together under a [Lorentz transformation](special-relativity.md), the same way $x^\mu$ does. Four-momentum is one example, $p^\mu=(E/c,\mathbf p)$.

## 2. Einstein summation

When an index appears once as a superscript and once as a subscript in the same expression, sum it over its four values. This is **Einstein summation notation**:

$$A^\mu B_\mu=A^0B_0+A^1B_1+A^2B_2+A^3B_3.$$

The summed index is a **dummy index**; its name does not matter, so $A^\mu B_\mu=A^\nu B_\nu$. An index left unsummed is a **free index** and must match on both sides of any equation.

## 3. The metric

To form the [spacetime interval](special-relativity.md#_4-spacetime-and-the-invariant-interval), time and space enter with opposite signs. The **Minkowski metric** encodes those signs:

$$\eta_{\mu\nu}=\operatorname{diag}(+1,-1,-1,-1).$$

It has entries $\eta_{00}=+1$, $\eta_{11}=\eta_{22}=\eta_{33}=-1$, and zeros elsewhere. Contracting the position four-vector with itself through the metric gives

$$x^\mu x_\mu=\eta_{\mu\nu}x^\mu x^\nu=c^2t^2-x^2-y^2-z^2,$$

which is the invariant interval. The metric is the geometric price of mixing time and space: it replaces the ordinary dot product's all-plus signs.

## 4. Upper and lower indices

The metric converts between an upper index and a lower one:

$$A_\mu=\eta_{\mu\nu}A^\nu,\qquad A^\mu=\eta^{\mu\nu}A_\nu.$$

Lowering leaves the time component alone and flips the sign of the spatial ones: $x_\mu=(ct,-x,-y,-z)$. The inverse metric $\eta^{\mu\nu}$ has the same diagonal entries as $\eta_{\mu\nu}$.

Why keep two kinds of index? An upper-index vector $A^\mu$ transforms one way under a Lorentz transformation, and a lower-index vector $A_\mu$ transforms the opposite way, so that the sum $A^\mu B_\mu$ comes out the same in every frame. [Special Relativity §6](special-relativity.md#_6-metric-tensor-covariance-and-contravariance) states the two transformation rules.

## 5. Contraction and Lorentz scalars

Summing a matched upper and lower index is a **contraction**. Contracting two four-vectors gives

$$A^\mu B_\mu=A^0B_0-\mathbf A\cdot\mathbf B,$$

a single number. A fully contracted expression is a **Lorentz scalar**: it has the same value in every inertial frame. The invariant interval $s^2=x^\mu x_\mu$, the squared mass $m^2=p^\mu p_\mu$, and the plane-wave phase $\phi=k^\mu x_\mu$ are all scalars built this way.

A **tensor** generalizes the rule: it carries several indices, and each upper index transforms one way while each lower index transforms the other. The metric itself is a tensor with two lower indices. The rest of the site uses only four-vectors and contractions; the full tensor law returns only for the field transformations on [QFT](qft.md).

---

Previous: [Linear Algebra](appendix-math-linear-algebra.md)

Next: [Groups and Symmetry](appendix-math-groups.md)
