# Path Integrals for Fields

**Optional sequence.** These five pages offer another perspective on quantum theory; they are not prerequisites for the later chapters. You can continue directly from Feynman Rules for QED to [Weak Interaction](weak-interaction.md).

The [particle path integral](path-integrals.md) adds contributions from possible position histories. Quantum field theory extends this idea to **histories of fields throughout spacetime**.

The destination is familiar: the same propagators, vertices, and amplitudes obtained in [Perturbation Theory](perturbation-theory.md). We use $\hbar=c=1$ on this and the following pages.

## What is being summed over?

A scalar field assigns a value $\phi(t,\mathbf x)$ to every spacetime point. One field history specifies all those values. A different history might have a larger field in one region, a different time dependence, or both.

To picture the integral, imagine sampling spacetime on a grid. Assign a field value to each grid point, calculate the action for that configuration, and integrate over the possible values at every point. Refining the grid leads to the continuum notation

$$\int\mathcal D\phi\,e^{iS[\phi]}.$$

The phase comes from the field action, just as it came from the particle action. Boundary conditions specify the states under discussion, and normalization removes common factors that do not affect the result. The bare expression above is not yet a particular scattering amplitude.

## Ask how fields at two points are related

A useful quantity is the **two-point correlation function**: insert field factors at two points and evaluate their normalized, time-ordered vacuum average. In the operator notation already used in these notes, this is

$$\langle0|T\phi(x)\phi(y)|0\rangle.$$

The path-integral method computes the same object by including $\phi(x)\phi(y)$ inside the integral. Its weighting is complex, so this is a quantum correlation rather than an ordinary statistical average over a positive probability distribution.

For a free scalar field, the result is the propagator. In momentum space it supplies the familiar factor

$$\frac{i}{p^2-m^2+i\epsilon}.$$

The free part of the action determines this result. The $+i\epsilon$ implements the vacuum time-ordering prescription explained in [Perturbation Theory](perturbation-theory.md). Changing the calculation method has not changed what propagates or the pole prescription.

## Free fields produce pairings

Free-field actions contain terms quadratic in the fields. Their integrals belong to the same family as ordinary Gaussian integrals. A useful property is that correlations involving several fields reduce to sums of two-field pairings.

For four scalar-field insertions, the possible complete pairings are

$$ (1,2)(3,4),\qquad (1,3)(2,4),\qquad (1,4)(2,3).$$

Each pair supplies a propagator; each complete pairing supplies a product of propagators. Adding these products reproduces Wick's theorem from the operator calculation. Here the numbers label insertion points, not individual detected particles.

## Interactions generate vertices

Separate the action into free and interaction parts:

$$S=S_0+S_{\mathrm{int}},\qquad
 e^{iS}=e^{iS_0}\left(1+iS_{\mathrm{int}}+\frac{(iS_{\mathrm{int}})^2}{2!}+\cdots\right).$$

The free-field integral evaluates each term using pairings. Each interaction insertion supplies fields that can attach to external states or pair with fields from other insertions. This is the same expansion structure as the Dyson series.

In QED, an interaction insertion contains two fermion fields and one photon field. It therefore produces an electron–photon vertex. Pairings between insertions produce internal propagators, and integrating over the interaction positions imposes momentum conservation.

| Part of the calculation | Diagram notation |
| --- | --- |
| Attachment to an external state | External line |
| Pairing of free fields | Propagator line |
| Insertion of the interaction | Vertex |
| Equivalent pairings and expansion factorials | Symmetry factor |
| Internal momentum not fixed by conservation | Loop integration |

## Back to Compton scattering

Compton scattering needs two photon attachments, so its leading connected contribution uses two QED interaction insertions. There are two ways to attach those photons along the electron line. The free fermion pairing supplies an electron propagator with momentum $p+k$ or $p-k'$.

These are precisely the s- and u-channel contributions in the [manual Compton derivation](feynman-rules.md#the-same-amplitude-without-diagrams). The path integral produces the same sum $\mathcal M_s+\mathcal M_u$.

To extract a scattering amplitude from field correlations, one must account for the external particle states and remove the external propagator factors. That step supplies the spinors and polarization vectors already present in the Feynman rules.

**A diagram records a group of terms in the expansion.** It is not a single field configuration or a drawing of a particle trajectory. The operator and path-integral methods provide two derivations of the same bookkeeping.

There is one extra ingredient for electrons: exchanging fermions changes signs. [Fermionic Path Integrals](path-integrals-fermions.md) explains how the field integral preserves that rule.
