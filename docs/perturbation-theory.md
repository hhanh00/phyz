# Perturbation Theory: From the Lagrangian to the Feynman Rules

The [Feynman Rules page](feynman-rules.md) states a rulebook — a vertex factor, propagators, external-line wave functions — and translates diagrams with it. This page is the reconciliation the rules are owed: it derives that rulebook from the Lagrangian. The argument runs entirely on machinery the site has already built. The [Field Quantization page](field-quantization.md) showed that a free field is a stack of harmonic oscillators whose quanta are particles, which gives the free-theory part of the story. What remains is the interacting part: the Lagrangian contains a term that couples fields, and the S-matrix of [From Lagrangian to Experiment](lagrangian-to-experiment.md) must be expanded in that coupling. Two tools carry the expansion, the Dyson series and Wick's theorem, and both are bookkeeping — one organizes the orders, the other organizes the field pairings. We run them on the simplest interacting field theory, a real scalar with a three-field interaction, where no spin structure or gauge symmetry can hide the logic, and we read the rules off what the expansion computes. The final section carries the same dictionary to QED.

We work in natural units, $\hbar = c = 1$, and use the metric $g_{\mu\nu} = \operatorname{diag}(1,-1,-1,-1)$, so $p^2 = p^\mu p_\mu = E^2 - \mathbf p^2$ and an on-shell particle of mass $m$ obeys $p^2 = m^2$. This matches the convention the route to cross sections has already adopted.

## Outline of the argument

The derivation runs in six steps, and each section of this page carries out one of them.

1. **Define the theory.** Add the interaction $-g\phi^3/3!$ to the free scalar Lagrangian, so that quanta can meet and scatter.
2. **Write the S-matrix.** In the interaction picture, the Schrödinger equation with the interaction as its generator solves, by time-slicing, to the time-ordered exponential $S = T\exp[i\int d^4x\,\mathcal{L}_{\mathrm{int}}]$.
3. **Expand it.** The Taylor series of that exponential is the Dyson series, a sum over how many times the interaction acts, and the time ordering is the only part of it that still needs to be dealt with.
4. **Sort the operators.** Wick's theorem rewrites each time-ordered product as normal-ordered fields plus pairings, and each pairing contributes a number called a contraction.
5. **Compute the contraction.** The free-field mode expansion turns the contraction into the propagator $i/(p^2 - m^2 + i\epsilon)$, the inverse of the free kinetic operator.
6. **Assemble amplitudes.** Uncontracted fields become external lines, contractions become internal lines, the position integrals become momentum-conserving deltas, and the pairing counts fix the combinatorial factors.

The final section carries the finished dictionary to QED by changing only the free-field input.

In layman's terms:
- The S matrix sums over every number of interaction events, every position for each event, and every way of assigning the fields' creation and annihilation parts. We sum over everything because during the interaction we do not know what is happening, and only the terms that connect the initial state to the final state survive the evaluation.
- Operators at different times do not commute, and evolution composes in sequence, so each product carries a canonical order: later times to the left. That is what the $T$ symbol imposes.
- Separately, evaluating against the states has its own rules: an annihilation part that finds no particle gives zero, and a creation part facing the vacuum bra gives zero. These rules select which terms survive.
- Time-ordered products are hard to evaluate, so Wick's theorem trades them for normal-ordered products plus leftover numbers. Those numbers are the contractions.
- A contraction is not the commutator itself. It is the vacuum expectation value of the reordering residue, a plain number that depends only on the separation of the two points.
- After the trade, we evaluate the normal-ordered products directly against the states and add the contractions as numbers.
- In the diagrams, uncontracted fields are the external lines, contractions are the internal lines, and the interaction factors together with their position integrals are the vertices.


## The setup: an interacting scalar

The [Field Quantization page](field-quantization.md) solved a free real scalar field $\phi$, with Lagrangian density

$$\mathcal{L}_0 = \tfrac12 (\partial_\mu\phi)(\partial^\mu\phi) - \tfrac{m^2}{2}\phi^2.$$

Free fields cannot scatter, because their quanta never meet. To let them interact we add a term built from three fields,

$$\mathcal{L} = \mathcal{L}_0 - \frac{g}{3!}\,\phi^3.$$

The coupling $g$ sets the strength of the interaction, and the factor $3!$ is a combinatorial convenience whose purpose appears when the field pairings are counted. The theory this defines contains exactly one field, a real scalar of spin 0, and every vertex joins three quanta of that one field. It is not QED. QED contains two fields, the spinor $\psi$ and the vector $A_\mu$, and its interaction $-q\bar\psi\gamma^\mu\psi A_\mu$ joins two quanta of the electron field to one quantum of the photon field at each vertex. The two interactions are nonetheless analogues, because both join three fields at a point and so produce the same kind of diagrammatic vertex. We derive the rules for the scalar theory because it is the simplest interacting field theory: its single field carries no spin indices and no gauge freedom, so fewer structures appear alongside the derivation itself, and the same derivation then transfers to QED. The interaction makes the theory nonlinear, exactly as in [QED](qed.md), so we treat $g$ as small and expand.

## The S-matrix as a series

The interaction picture does the bookkeeping for time. States evolve freely, and the operators carry the interaction, so the S-matrix — the operator that maps a free initial state at $t \to -\infty$ to a free final state at $t \to +\infty$ — is the time evolution generated by the interaction alone. For a time-independent interaction that evolution is an exponential,

$$S = T \exp\!\left[i \int d^4x\; \mathcal{L}_{\mathrm{int}}(x)\right],$$

where $T$ is the time-ordering symbol, which arranges the operators in each product by their time arguments, later times to the left[^time]. On two fields it reads $T[\phi(x)\phi(y)] = \phi(x)\phi(y)$ when $x^0 > y^0$ and $\phi(y)\phi(x)$ when $y^0 > x^0$, and on a product of any length it applies the same rule field by field. Here $\mathcal{L}_{\mathrm{int}} = -g\phi^3/3!$. The time ordering matters because field operators at different times do not commute, so the order of a product changes its value and $T$ fixes one canonical order, and the exponential is shorthand for its Taylor series,

$$S = \sum_{n=0}^\infty \frac{i^n}{n!} \int d^4x_1 \cdots d^4x_n\; T\big[\mathcal{L}_{\mathrm{int}}(x_1) \cdots \mathcal{L}_{\mathrm{int}}(x_n)\big].$$

Each factor of $\mathcal{L}_{\mathrm{int}}$ carries one power of the coupling, so the $n$ th term of the series is the contribution of $n$ interactions. A scattering amplitude computed from $S$ is therefore a sum over the number of times the interaction acts, which is the perturbative expansion in $g$ that the [Feynman Rules page](feynman-rules.md) promised the diagrams would organize. Each term integrates over $n$ positions $x_i$, one per interaction, and the time-ordering symbol is the only subtlety left in the expression; Wick's theorem removes it.

## Wick's theorem

The time-ordered product in the series is a product of field operators at different points, and fields split into creation and annihilation parts, $\phi = \phi^+ + \phi^-$, where $\phi^-$ creates a particle and $\phi^+$ destroys one, each with a plane-wave factor from the mode expansion of the [Field Quantization page](field-quantization.md). Acting on a state, a creation operator adds a particle; acting on the vacuum, an annihilation operator gives zero. The **normal-ordered product** $:\!\phi_1\cdots\phi_n\!:$ moves every creation operator to the left of every annihilation operator, so that it annihilates a vacuum on the right. Consider a matrix element built from a normal-ordered product, $\langle 0|\,:\!\phi_1\cdots\phi_n\!:\,|\text{particles}\rangle$, with the vacuum bra on the left and a state of particles on the right. The annihilation parts sit on the right, next to the particle state, and the creation parts sit on the left. You can then check every operator one by one. An annihilation part either removes one particle and leaves a plane-wave factor, or it finds no particle left and gives zero, which makes the whole term zero. A creation part adjacent to the vacuum bra also gives zero, because a creation operator annihilates the vacuum bra from the left. A term survives only when every operator succeeds, and a surviving term is a product of plane-wave factors. A time-ordered product cannot be checked this way, because it is sorted by time rather than by operator type. It can contain an annihilation part standing to the left of a creation part, and moving such a pair toward the states forces an annihilation part past a creation part; their commutator is a nonzero number. That number does not come from any external particle. It is a leftover of the ordering itself, and the next paragraph accounts for it.

**Wick's theorem** rewrites the one as the other. Its elementary form for two fields states the pattern:

$$T\big[\phi(x)\phi(y)\big] = \;:\!\phi(x)\phi(y)\!: \;+\; \langle 0\lvert T\big[\phi(x)\phi(y)\big]\rvert 0\rangle.$$

The last term is a number, the vacuum expectation of the time-ordered product, and it is called the **contraction** of the two fields. As an operation, contracting a pair means deleting those two fields from the product and multiplying everything else by this number, which depends only on the separation $x - y$. Physically, the contraction is the amplitude for one quantum to be created at one of the two points and destroyed at the other, and the vacuum states on the two sides are what forbid anything else from entering the process.

For $n$ fields the theorem says: a time-ordered product equals the normal-ordered product of all the fields, plus the sum over every way of replacing some pairs of fields by their contractions, with the uncontracted fields left in normal order. Every term in that sum is a possible way the product could resolve, and the external states decide which terms survive. An uncontracted field has exactly one way to contribute: it must act on a real particle supplied by the initial or final state. A term that leaves uncontracted fields with no particle to act on gives zero, because a normal-ordered product annihilates the vacuum on its right. So the surviving terms are fixed by counting. At order $n$ the series supplies $3n$ fields; if the process has $k$ external particles, a surviving term contracts exactly $3n - k$ fields among themselves — in pairs, so $3n - k$ must be even — and lets the remaining $k$ fields meet the particles. Two checks from the theory at hand: first-order decay $\phi \to \phi\phi$ has three fields and three particles, so no contraction appears and the amplitude is the single vertex factor; second-order scattering $\phi\phi \to \phi\phi$ has six fields and four particles, so two fields must contract with each other, and that contraction is the internal line between the two interaction points.

## The propagator from the free field

The contraction is computable because the free field is known. Evaluate $\langle 0\lvert T\phi(x)\phi(y)\rvert 0\rangle$ with the mode expansion. When $x^0 > y^0$ the time-ordering puts $\phi(x)$ first, and only the annihilation half of $\phi(x)$ followed by the creation half of $\phi(y)$ survives between vacua, leaving the phase $e^{-ip\cdot(x-y)}$ and the weight $1/\sqrt{2E_p}$ from the expansion's normalization:

$$\langle 0\lvert T\phi(x)\phi(y)\rvert 0\rangle = \int \frac{d^3p}{(2\pi)^3}\,\frac{1}{2E_p}\left[\theta(x^0-y^0)\,e^{-ip\cdot(x-y)} + \theta(y^0-x^0)\,e^{+ip\cdot(x-y)}\right].$$

When $y^0 > x^0$ the roles reverse, which is the second term. The two orderings are both contained in one four-momentum integral once the contour is chosen correctly:

$$\langle 0\lvert T\phi(x)\phi(y)\rvert 0\rangle = \int \frac{d^4p}{(2\pi)^4}\,\frac{i}{p^2 - m^2 + i\epsilon}\,e^{-ip\cdot(x-y)}.$$

The integrand has poles where $p^2 = m^2$, the mass shell. A wave with $e^{-ip\cdot(x-y)}$ is a positive-frequency wave propagating forward in time when the integral closes in the lower half of the $p^0$ plane, and the $+i\epsilon$ shifts the pole at $E_p$ up and the pole at $-E_p$ down so that closing the contour picks up exactly the pole that belongs to the ordering $\theta(x^0-y^0)$[^contour]. Time ordering, not a convention, chooses which side of each pole the integral passes, and that choice is the origin of the $i\epsilon$ that appears in every propagator. In momentum space the result is strikingly simple: the contraction is the Fourier transform of

$$\frac{i}{p^2 - m^2 + i\epsilon},$$

which is the inverse of the Klein–Gordon operator $p^2 - m^2$ times $i$. The free term of the Lagrangian determines the propagator because the propagator undoes the free equation of motion; a particle that travels between two interactions obeys the free dynamics, so the factor that carries it between points is the inverse of the free kinetic operator. This is the first entry of the rulebook, and it came from the free theory alone.

## Building amplitudes: the dictionary

Now assemble a transition amplitude. Insert the Dyson series between a final state and an initial state, apply Wick's theorem term by term, and collect the pieces. Three kinds of object appear.

**External lines.** An uncontracted field meets a particle in the initial or final state. A field's creation half acting on an initial state adds the particle with phase $e^{+ip\cdot x}$; its annihilation half removes a particle from a final state with phase $e^{-ip\cdot x}$ (by Hermitian conjugation of the creation amplitude). For the real scalar there is nothing else: a one-particle state is fully specified by its momentum, so the external-line factor carries no spinor or polarization index.

**Contractions.** A pair of fields contracted with each other contributes the propagator computed above, evaluated at the momentum that flows between their positions.

**Vertex integrals.** Each factor of $\mathcal{L}_{\mathrm{int}}$ integrates over its position and contributes its three fields. Writing $P$ for the total of the momenta meeting at the vertex, integrating the position $x$ against the plane-wave phases of those fields produces $\int d^4x\, e^{-ix\cdot P} = (2\pi)^4\delta^4(P)$, a momentum-conserving delta for each vertex.

Counting the fields decides which pairings survive. At a vertex of $\phi^3$ the three fields are identical, and the $3!$ ways of assigning them to the three legs cancel the $3!$ in the denominator of the interaction — the combinatorial factor exists so that permuting the legs does not multiply the answer. Reading a diagram is then mechanical: multiply $-ig$ for each vertex, $i/(p^2-m^2+i\epsilon)$ for each internal line, and integrate over any momentum not fixed by conservation.

The simplest process shows the dictionary at work. A scalar of momentum $p$ decays into two scalars of momenta $p_1, p_2$, $\phi(p) \to \phi(p_1)\phi(p_2)$. First order in the series has one vertex, and Wick's theorem leaves the three fields to create the two daughters and destroy the parent:

$$i\mathcal{M} = -ig,$$

with the momenta constrained by $\delta^4(p - p_1 - p_2)$, energy and momentum conserved at the single vertex. A vertex contributes the coupling; that is all a vertex is.

A second example exercises the internal line. For two-to-two scattering $\phi(p_1)\phi(p_2) \to \phi(p_3)\phi(p_4)$ at second order, two vertices appear, each supplying three fields. Six fields must pair against four external particles, so two fields contract with each other and form the propagator that connects the vertices. One routing has the incoming pair fuse at the first vertex, an internal line of momentum $q = p_1 + p_2$ carry the result to the second vertex, and the pair split there; that routing contributes

$$i\mathcal{M}_s = (-ig)^2\, \frac{i}{q^2 - m^2 + i\epsilon}, \qquad q^2 = (p_1+p_2)^2.$$

Because the scattered particles are identical bosons, the other two routings — pairing the momenta in the alternative ways — contribute the same expression with $q$ replaced by the other momentum combinations, and the full amplitude is their sum[^identical]. The diagram rules reproduce the algebra term by term, which is the reconciliation this page promised: a diagram is not a picture of a process, it is the drawn residue of the expansion, and the rules are the translation back.

The scalar rulebook that has now been derived, not asserted, is:

| Diagram element | Factor |
| --- | --- |
| Vertex | $-ig$ |
| Internal line, momentum $r$ | $\displaystyle \frac{i}{r^2 - m^2 + i\epsilon}$ |
| External line | $1$ |

An amplitude $\mathcal{M}$ is the product of these factors, with momentum conservation enforced at each vertex and the overall delta $\delta^4(P_f - P_i)$ factored out to define $\mathcal{M}$, exactly as the S-matrix split of [From Lagrangian to Experiment](lagrangian-to-experiment.md) requires[^lsz].

## QED's rules are the same dictionary

Nothing in the derivation used a property specific to the real scalar except the free-field results. The machinery — Dyson series, Wick's theorem, propagator as inverse of the free kinetic operator, delta at each vertex — runs unchanged for the fields of QED. The interaction there is $-q\bar\psi\gamma^\mu\psi A_\mu$, and expanding the S-matrix in $q$ organizes the same way, because that interaction also joins three fields at a point. What changes is only the free-theory input, the propagators of the individual fields.

The electron's free Lagrangian gives its propagator as the inverse of its kinetic operator, $i(\not r + m)/(r^2 - m^2 + i\epsilon)$, and the photon's gives $-ig_{\mu\nu}/(r^2 + i\epsilon)$; each carries the indices and spinor structure its field carries. The vertex factor falls out of the interaction: the contraction structure of $\bar\psi\gamma^\mu\psi A_\mu$ produces $-iq\gamma^\mu$, the object the [Feynman Rules page](feynman-rules.md) reads off diagrams. External lines differ only because the fields differ: a one-electron state is not fully specified by momentum, so the electron field's uncontracted factor carries the spinor $u(p)$ or $\bar u(p')$, and a photon's carries its polarization $\varepsilon_\mu(k)$. Wick's theorem supplies the same pairings, the vertex delta functions enforce momentum conservation, and the resulting diagram rules are precisely those stated on the Feynman Rules page.

The electron and photon propagators quoted above are not derived on this page. They are the results of the two remaining free-field quantizations: the spinor construction, which runs on the [Field Quantization page](field-quantization.md#the-spinor-field), and the photon construction with its gauge fixing, which runs on the [QED page](qed.md#quantizing-the-photon-field). Given those free-field results, the perturbative expansion produces the QED rulebook by the argument of this page. The [next page](feynman-rules.md) applies that rulebook to Compton scattering and then extends it to loop diagrams and renormalization, where the divergences of the higher-order terms are handled.

[^contour]: The detail of which pole belongs to which ordering is a residue computation. In the $p^0$ plane the propagator has poles at $p^0 = \pm E_p$. Closing the contour below the real axis for $x^0 - y^0 > 0$ and above it for $x^0 - y^0 < 0$ selects the pole whose exponential decays in the right half of spacetime; the $+i\epsilon$ is precisely the shift that makes those two closure choices land on the correct poles. The sign of $\epsilon$ is fixed by demanding that positive-energy states propagate forward in time, which is causality.

[^identical]: For two identical final scalars the alternative routings are the t- and u-channels, named after the Mandelstam variables of the channel discussion on the Feynman Rules page. The same bookkeeping that produced the one routing produces the others, and they are added because the field that creates the final particles cannot tell which particle is which.

[^lsz]: This page computes $S$-matrix elements between normalized free-particle states, whose mode expansions carry factors of $1/\sqrt{2E_p}$. Conventional amplitudes $\mathcal{M}$ absorb those factors together with the wave-function residues into the definition of $\mathcal{M}$, which is why the amplitude written for the decay above has no such factors. The precise statement that a scattering amplitude is obtained from fully amputated, on-shell Feynman diagrams is the **LSZ reduction formula**; it is standard quantum field theory and is not derived here.

[^time]: The symbol $T$ for time ordering is standard notation across quantum field theory, QED included. Dyson introduced it in 1949 in the course of deriving the series below, which is why the expansion of $S$ is called the **Dyson series**. One refinement appears when the theory contains fermion fields, as QED does: fermion operators anticommute, so there $T$ also multiplies by $-1$ for each pair of fermionic operators swapped in the reordering. The scalar field of this page is bosonic, so no signs arise, and the final section transfers the machinery to QED with that single amendment.
