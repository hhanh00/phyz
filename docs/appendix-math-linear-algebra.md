# Math Refresher: Linear Algebra

Quantum states live in a vector space, and observables act on them as matrices. This page defines the pieces: vectors, matrix multiplication, the adjoint, eigenvalues, and the bra-ket notation that carries them.

## 1. Vectors

A **vector** is an ordered list of numbers. A column vector with two entries is

$$\mathbf v=\begin{pmatrix}v_1\\v_2\end{pmatrix}.$$

The entries are its **components** in some basis. Adding two vectors adds component by component, and multiplying by a number scales every component. These two operations are what "vector space" means, so a quantum state — a vector in [Hilbert space](first-quantization.md) — can be added to another and scaled, exactly like an arrow.

## 2. Matrices and multiplication

A **matrix** is a rectangular array that turns one vector into another. Multiplying a matrix by a column vector produces a new column vector:

$$\begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}v_1\\v_2\end{pmatrix}=\begin{pmatrix}av_1+bv_2\\cv_1+dv_2\end{pmatrix}.$$

Each output entry is a row of the matrix dotted against the vector. Multiplying two matrices composes their two transformations, and it matters which order they act: $AB$ and $BA$ generally differ. This failure to commute is exactly what the [commutator](first-quantization.md#_8-commutators) $[\hat A,\hat B]=\hat A\hat B-\hat B\hat A$ measures.

## 3. Transpose, conjugate transpose, and the adjoint

The **transpose** $A^T$ flips rows and columns. The **conjugate transpose** also conjugates every entry:

$$A^\dagger=(A^*)^T.$$

The dagger $^\dagger$ reads "adjoint." For a column vector, $\mathbf v^\dagger$ is the corresponding row with conjugated entries.

The adjoint matters because it tells us how an operator acts on the *other* side of an inner product. It is the operator version of complex conjugation, as [Complex Numbers](appendix-math-complex.md#_5-conjugation-and-the-adjoint) notes.

## 4. Eigenvalues and eigenvectors

When a matrix acts on a vector and only rescales it,

$$\hat A\mathbf v=\lambda\mathbf v,$$

the vector $\mathbf v$ is an **eigenvector** and the number $\lambda$ is its **eigenvalue**. Solving this equation for a matrix $\hat A$ finds its special directions. In quantum mechanics the eigenvalues of an observable are the possible measurement outcomes, as [First Quantization](first-quantization.md#_7-eigenvectors-and-eigenvalues) explains.

**Example.** The matrix $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ has eigenvectors $\begin{pmatrix}1\\1\end{pmatrix}$ and $\begin{pmatrix}1\\-1\end{pmatrix}$ with eigenvalues $+1$ and $-1$.

## 5. Inner products and bra-ket notation

An **inner product** assigns a number to two vectors, measuring how much they overlap. For column vectors, it is the dot product with a conjugate:

$$\langle\mathbf u|\mathbf v\rangle=u_1^*v_1+u_2^*v_2.$$

Its value is $\lVert\mathbf v\rVert^2=\langle\mathbf v|\mathbf v\rangle$, the squared length, which is never negative.

Quantum mechanics abbreviates this with **bra-ket notation**. A **ket** $|\psi\rangle$ is a state vector; the matching **bra** $\langle\phi|$ is the conjugate-transpose of a state vector, ready to form an inner product. The bracket $\langle\phi|\psi\rangle$ is therefore the overlap of the two states. Inserting an operator between them,

$$\langle\phi|\hat A|\psi\rangle,$$

means the overlap of $\phi$ with the vector $\hat A|\psi\rangle$. The adjoint is defined so that moving an operator from one side to the other conjugates it:

$$\langle\phi|\hat A^\dagger\psi\rangle=\langle\hat A\phi|\psi\rangle.$$

This notation first appears on [First Quantization](first-quantization.md) and is used from then on. A ket written as $|0\rangle$ is a named state (the ground state or the vacuum), not the number zero.

## 6. Hermitian and unitary operators; trace

Two kinds of operator do most of the work:

- A **Hermitian** operator satisfies $\hat A=\hat A^\dagger$. Its eigenvalues are real, which is why observables are Hermitian. Eigenvectors with distinct eigenvalues are orthogonal.
- A **unitary** operator satisfies $\hat U^\dagger\hat U=\hat U\hat U^\dagger=1$. It preserves every inner product, so it maps normalized states to normalized states and describes time evolution and symmetry transformations.

For a Hermitian matrix we can always find a complete set of orthogonal eigenvectors. This is the **spectral theorem**: a state can be expanded in the eigenbasis of an observable, and the squared magnitudes of the expansion coefficients give outcome probabilities ([First Quantization](first-quantization.md#_7-eigenvectors-and-eigenvalues)).

The **trace** of a square matrix is the sum of its diagonal entries, $\operatorname{tr}A=\sum_i A_{ii}$. It appears when a [closed fermion loop](feynman-rules.md#tree-level-and-loop-diagrams) is evaluated, where the sum over the spinor index of a closed chain is a trace.

---

Previous: [Complex Numbers](appendix-math-complex.md)

Next: [Index Notation and Tensors](appendix-math-tensors.md)
