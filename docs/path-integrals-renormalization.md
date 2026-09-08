# Renormalization at One Loop

**Optional sequence.** These five pages offer another perspective on quantum theory; they are not prerequisites for the later chapters. You can continue directly from Feynman Rules for QED to [Weak Interaction](weak-interaction.md).

The [Feynman Rules page](feynman-rules.md#infinities-in-loop-diagrams) introduced the problem: an internal loop momentum is not fixed by the external particles, so the calculation integrates over it. Large momenta can make that integral diverge.

**Renormalization connects the parameters in the calculation to measured quantities.** It works in the operator and path-integral formulations alike.

## What a loop changes

At tree level, the electron propagator contains a mass parameter $m$. At higher order, the electron can interact with an internal photon, producing a correction to its propagation. That correction changes the relation between the mass parameter in the Lagrangian and the pole identified with a physical particle's mass.

Other loops affect photon propagation and interaction vertices. A calculation that includes those loops must also update how its mass, charge, and field normalization are related to physical inputs.

## First make the integral well defined

A **regulator** temporarily makes the divergent expression manageable. A momentum cutoff, for example, excludes momenta above a scale $\Lambda$. Dimensional regularization instead evaluates the integral in a variable spacetime dimension and identifies divergences as poles when returning to four dimensions.

These are tools for defining intermediate calculations. A regulator should allow the symmetries needed by the calculation to be maintained or consistently restored. Dimensional regularization is particularly useful for perturbative gauge theories.

Regularization alone does not produce a physical prediction: the regulated result still contains unwanted dependence on the regulator.

## Example: fixing a mass

To isolate the logic, consider a schematic one-loop mass relation:

$$M^2=m_0^2(\Lambda)+\Delta m_{\mathrm{loop}}^2(\Lambda).$$

Here $M$ is the physical pole mass, $m_0$ is the original or **bare** mass parameter, and $\Delta m_{\mathrm{loop}}^2$ is the loop correction. The displayed relation is schematic; its detailed form depends on the theory and the order calculated.

The loop term may grow without bound as the cutoff increases. The bare parameter is not independently measured, however. We choose it so that their combination reproduces the physical input.

It is convenient to split the bare parameter into a renormalized parameter and a **counterterm**:

$$m_0^2(\Lambda)=m_R^2+\delta m^2(\Lambda).$$

Then

$$M^2=m_R^2+\left[\delta m^2(\Lambda)+\Delta m_{\mathrm{loop}}^2(\Lambda)\right].$$

The counterterm cancels the divergent part of the loop correction. A finite condition fixes the remaining freedom. For example, an on-shell mass convention chooses $m_R=M$, so the bracket vanishes at the physical pole to the order being calculated.

This does not predict the mass without input. It defines how the parameter must be chosen to reproduce that input, allowing the theory to make other predictions consistently.

## How fitting one quantity allows other predictions

The same idea applies to interaction strength. Suppose a regulated loop contribution to a vertex has a momentum-independent divergent part $D(\Lambda)$ and a finite momentum-dependent part $F(Q)$:

$$\text{vertex at }Q=\lambda_R+\delta\lambda(\Lambda)+D(\Lambda)+F(Q).$$

Here $Q$ labels a momentum configuration, and $\lambda_R$ is the chosen renormalized coupling. This is an illustrative structure, not a universal formula for every vertex.

Define the coupling by a condition at a reference configuration $Q_*$:

$$\delta\lambda(\Lambda)=-D(\Lambda)-F(Q_*).$$

The resulting vertex is

$$\text{vertex at }Q=\lambda_R+F(Q)-F(Q_*).$$

The regulator-dependent term has disappeared, and the reference value is $\lambda_R$. Once the coupling is fixed, the momentum dependence elsewhere is a prediction. A condition imposed on an off-shell vertex is a parameter convention; connecting it to a measured rate still requires the full scattering calculation.

This works because the divergent term has the form of an interaction already represented by the counterterm. In renormalizable QED, a finite set of mass, charge, and field-normalization counterterms suffices at every perturbative order. Their coefficients are fixed consistently, rather than adjusted separately for each scattering event.

## Why a renormalization scale appears

Many prescriptions introduce a reference scale $\mu$. The numerical values of the renormalized parameters then depend on that scale. Changing $\mu$ changes how the result is divided between those parameters and the explicit loop terms.

A physical prediction remains unchanged when both pieces are changed consistently, up to corrections beyond the calculated order. The equations describing this dependence are called **renormalization-group equations**.

This makes it useful to quote a coupling together with its scale and convention. It also helps organize calculations when the momenta in an experiment are very different from those used to specify the parameters.

## What a complete QED calculation requires

For a one-loop Compton prediction, one selected loop is insufficient. The calculation includes all contributions at that order, the required counterterms, and the normalization of the external particle states. Gauge symmetry relates these pieces and constrains the counterterms.

There is also a distinct low-momentum problem. Very soft photons can cause infrared divergences, which ultraviolet renormalization does not remove. A detector includes events with additional photons too soft to resolve. Combining this unresolved emission with virtual-loop corrections gives the corresponding infrared-finite inclusive rate.

The roles are therefore different: [fermionic integration](path-integrals-fermions.md) preserves exchange signs, [gauge fixing](path-integrals-gauge-fixing.md) handles redundant potentials, and renormalization relates regulated calculations to physical inputs. Together they make the path-integral formulation usable for precision predictions, while the Feynman diagrams continue to organize the terms.
