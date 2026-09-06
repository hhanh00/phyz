# Feynman Rules for QED

## The need for Feynman diagrams

The QED Lagrangian of the [previous page](qed.md) is

$$\mathcal{L}_\text{QED} = -\tfrac14 F_{\mu\nu}F^{\mu\nu} \;+\; \bar\psi\left(i\hbar\gamma^\mu\partial_\mu - m\right)\psi \;-\; q\,\bar\psi\gamma^\mu\psi\,A_\mu .$$

The first two pieces are free theories, one for the photon and one for the electron, and each is exactly solvable: they describe particles that travel forever without noticing anything else. The third piece, the interaction term $-q\bar\psi\gamma^\mu\psi\,A_\mu$, is the only part in which one particle acts on another, and every event beyond "free particles in straight lines" — scattering, emission, absorption, decay — lives inside it.

That term is also what makes the theory nonlinear. It couples the photon to the electron current, so the photon moves the electron, the electron's motion feeds the current, and the current feeds the photon back. A nonlinear field theory has no exact solution, so the way in is to treat the interaction as small and expand in the charge $q$: a process happens by the interaction acting once, twice, three times, each extra action worth one more power of $q$, and the scattering amplitude is a sum over all of these.

The obstacle is bookkeeping, not physics. Each time the interaction acts it contributes a factor of the three fields in $-q\bar\psi\gamma^\mu\psi A_\mu$, and a term with $n$ such factors has $n$ electron fields and $n$ photon fields to pair off among the particles that enter and leave. Listing every way the fields can pair, without missing one or counting one twice, is a combinatorial chore that grows quickly with $n$. The physics is straightforward; the accounting is where mistakes creep in.

A Feynman diagram is that accounting drawn as a picture. Draw a line for each particle, draw a point where lines meet for each application of the interaction, and agree on a fixed translation — the Feynman rules — that turns the picture back into the algebraic factor the term contributes.

```feynman
\feynmandiagram [horizontal=a to b] {
  a -- [fermion] b,
  b -- [photon] c,
};
```

One point where an electron line and a photon line meet is one application of the interaction term.

The picture adds no new physics; it adds organization, and that organization buys several things:

- **Enumeration.** All the ways a process can happen become pictures set side by side, so a contribution is far harder to miss than it is inside a string of contracted fields.
- **Reading off amplitudes.** The rules turn each picture into its algebraic factor in one step, replacing the pairing count.
- **Higher orders.** One more interaction is one more point in the picture, so a whole perturbative series is visible at a glance.
- **Relations between processes.** Processes whose pictures differ only by moving a line share the same algebra — a connection that is invisible until it is drawn.

The rest of this page turns the promise into procedure: the building blocks of a diagram, the rules that translate a picture into an amplitude, and the demonstration that a diagram produces in one step the result the raw algebra produces in many.

## QED and Physical Processes

## Building Blocks of Feynman Diagrams

```feynman
\feynmandiagram [horizontal=a to b] {
  i1 -- [fermion] a -- [fermion] i2,
  a -- [photon] b,
  f1 -- [fermion] b -- [fermion] f2,
};
```

## Feynman Rules and Amplitudes

## Tree-level and Loop Diagrams

## Infinities in Loop Diagrams
