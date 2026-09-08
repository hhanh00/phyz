# Gauge Fixing

**Optional extra.** These five pages follow [The Standard Model](standard-model.md) and offer another perspective on quantum theory. They complement the main sequence and are not prerequisites for it.

The [QED page](qed.md) introduced gauge freedom: different potentials can describe the same electromagnetic field. A path integral over potentials must account for that freedom when calculating photon propagation.

**Gauge fixing chooses how to represent the electromagnetic field during a calculation.** It does not change the measured electric and magnetic fields.

## Different descriptions of the same field

The electromagnetic potential changes under

$$A_\mu\longrightarrow A_\mu+\partial_\mu\alpha,$$

where $\alpha$ is a function of spacetime. The field strength

$$F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$$

stays unchanged, because the two extra second-derivative terms cancel. Potentials related by such transformations describe the same field. Their collection is called a **gauge orbit**.

Integrating independently over every potential includes repeated descriptions of the same physics. It also makes the free photon operator impossible to invert on the full space of potentials: changing the potential in a pure-gauge direction produces no change in the field strength.

This is why obtaining a photon propagator requires one more step than obtaining a scalar propagator.

## Choose a gauge condition

One useful choice is the **Lorenz gauge condition**

$$\partial_\mu A^\mu=0.$$

Together with suitable boundary conditions and treatment of any remaining gauge freedom, this restricts the redundant descriptions used in the calculation.

The selection must preserve the relative weights of physically different fields. A simple analogy is changing coordinates in an ordinary integral: changing from Cartesian to polar coordinates requires the factor $r$ in $dx\,dy=r\,dr\,d\theta$. Restricting a gauge integral likewise requires a correction to its measure.

The corresponding correction is called the **Faddeev–Popov determinant**. Its detailed formula belongs to the machinery of performing the calculation; its purpose is to account correctly for the change from redundant potentials to a chosen gauge description. [Adel Bilal's advanced QFT notes](https://www.personal.soton.ac.uk/ab1u06/teaching/qft/qft3/lit/aqft.pdf) give the full construction.

## The practical result: a photon propagator

A convenient family of covariant gauges adds the term

$$\mathcal L_{\mathrm{gf}}=-\frac1{2\xi}(\partial_\mu A^\mu)^2$$

to the Lagrangian used in the calculation. The parameter $\xi$ labels the gauge choice. This term makes the free operator invertible after its boundary conditions are specified.

In **Feynman gauge**, $\xi=1$, the photon propagator has the simple form

$$\frac{-ig_{\mu\nu}}{k^2+i\epsilon}.$$

This is the rule already quoted in [Feynman Rules for QED](feynman-rules.md). A different gauge changes intermediate propagator expressions. It does not add physical photon polarizations or change a measured scattering rate.

## Why physical predictions agree

The gauge-dependent part of a covariant photon propagator is proportional to $k_\mu k_\nu$. When the photon connects conserved currents, those factors give zero because

$$k_\mu J^\mu=0.$$

Thus the gauge-dependent contribution drops out of the current-to-current amplitude. Current conservation connects the redundancy of the description to the independence of the prediction.

For an external photon, adding a multiple of its momentum to its polarization vector likewise must not change the physical amplitude. In Compton scattering, this property holds for the sum of the s- and u-channel diagrams. Keeping only one generally fails the check.

These cancellations explain why the complete set of contributions at a chosen order matters. Gauge independence is a property of the physical result, even when individual terms depend on the gauge choice.

## What ghosts are doing

The Faddeev–Popov correction can be represented using auxiliary fields called **ghosts**. They use the Grassmann algebra described on the [fermion page](path-integrals-fermions.md), but they are not physical electron-like particles. They encode the gauge-fixing correction and do not appear as detected external particles.

In QED with the linear covariant gauges used here, this correction is independent of the photon field. The ghosts do not interact with electrons or photons and cancel out of normalized physical calculations.

In QCD, gauge transformations involve the gluon field itself. The correction then depends on that field, so ghosts interact and contribute to loop calculations. Their role is still to preserve correct gauge bookkeeping.

This discussion describes the usual perturbative construction. Choosing a gauge globally in more general settings can be more complicated, but that issue is separate from using the QED propagator above.

Gauge fixing handles redundant descriptions. It does not remove large-momentum divergences from loop integrals. The next page explains [Renormalization at One Loop](path-integrals-renormalization.md).
