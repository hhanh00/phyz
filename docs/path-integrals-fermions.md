# Fermionic Path Integrals

**Optional extra.** These five pages follow [The Standard Model](standard-model.md) and offer another perspective on quantum theory. They complement the main sequence and are not prerequisites for it.

The [field path integral](path-integrals-fields.md) recovers propagators through free-field pairings. For electrons, those pairings must also reproduce the minus signs associated with exchanging fermions.

**The physical requirement is already familiar: fermionic quantities anticommute.** The path-integral method needs integration variables that preserve this property.

## Why ordinary numbers are insufficient

Ordinary numbers commute: $ab=ba$. Fermionic operators instead obey anticommutation rules, and exchanging two identical fermions reverses the sign of their joint state.

If we represented the electron field using ordinary commuting integration variables, the pairings would carry the wrong exchange signs. The solution is to use **Grassmann variables**, defined by

$$\theta_1\theta_2=-\theta_2\theta_1.$$

In particular, $\theta^2=0$, since it must equal its own negative. This is a mathematical device for keeping track of fermionic signs. It does not introduce a new physical particle or an additional interaction.

## What “integration” means here

A Grassmann variable is not a number that ranges along a real axis. Its integration is an algebraic rule. Since $\theta^2=0$, a function of one variable has the form $a+b\theta$, and the rule is

$$\int d\theta\,(a+b\theta)=b.$$

It extracts the coefficient of $\theta$. With several variables, their order matters because exchanging them changes a sign. The field version uses this rule for the components of the fermion field throughout spacetime.

The important consequence is that the resulting pairings have the same exchange signs as fermionic operator contractions. Detailed integration conventions are needed to perform the calculation, but the physical reason for using this algebra is the anticommutation rule.

## The same electron propagator

The free Dirac action contains the operator $i\gamma^\mu\partial_\mu-m$. In momentum space, this becomes $\not p-m$, where $\not p=\gamma^\mu p_\mu$.

The propagator reverses the action of this free operator, with the appropriate time-ordering prescription. The Dirac matrix identity

$$(\not p-m)(\not p+m)=p^2-m^2$$

explains its structure:

$$\frac{i(\not p+m)}{p^2-m^2+i\epsilon}.$$

The numerator handles the spinor structure; the denominator gives the mass-shell poles. The Grassmann field integral produces this same propagator used in [Feynman Rules for QED](feynman-rules.md#feynman-rules-and-amplitudes).

The interaction remains $-q\bar\psi\gamma^\mu\psi A_\mu$, so its vertex factor remains $-iq\gamma^\mu$. No new force has appeared: we have changed how the existing theory is calculated.

## Why closed fermion loops have a minus sign

When evaluating several fermion fields, putting them into the order needed for a particular pairing can require exchanges. Each exchange of odd fermionic factors contributes a minus sign.

For a closed fermion chain, the resulting bookkeeping gives the extra minus sign associated with a closed fermion loop. The sum over the internal spinor index also produces the trace mentioned on the [loop-diagram page](feynman-rules.md#tree-level-and-loop-diagrams).

A loop made from an electron segment and a photon line is not a closed fermion chain, so it does not acquire this particular extra minus sign. The distinction comes from how fermionic fields are contracted, not simply from whether the drawing contains a closed shape.

In more advanced treatments, integrating out the fermions packages closed fermion loops into a determinant. This is a compact way to organize the same signs and contractions; the determinant is not an additional physical contribution on top of those loops.

## What this adds to the diagram rules

For a Compton tree diagram, the electron chain begins and ends on external states. Grassmann integration yields the same ordered spinor expression obtained with operators. For processes containing closed fermion loops, it also supplies the required loop signs automatically.

Thus fermionic path integrals preserve both ingredients needed for electrons: the Dirac propagator and the exchange signs. The photon field presents a different issue: several potentials describe the same physical electromagnetic field. [Gauge Fixing](path-integrals-gauge-fixing.md) explains how the integral handles that redundancy.
