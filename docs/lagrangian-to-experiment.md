# From Lagrangian to Experiment

We have built Lagrangians for particles and fields. Now we will use them to predict a **scattering cross section**, the quantity that connects a scattering calculation to measured event rates.

## The job of a Lagrangian

**Start with the classical calculation.** The [Classical Mechanics](classical-mechanics.md) page introduced stationary action, and [Action and Lagrangians](qft-action.md) derived the Euler–Lagrange equation. Insert $L(q, \dot q)$ into that equation, then solve for the trajectory $q(t)$. Initial conditions specify which trajectory occurs, and differentiating it gives the velocity $\dot q(t)$.

## Why a trajectory is the wrong target

In quantum mechanics we predict probabilities for measurement outcomes. [First Quantization](first-quantization.md) introduced the wave function $\psi$, whose squared magnitude gives a position probability density.

[Field Quantization](field-quantization.md) also permits particle creation and annihilation. We therefore calculate an amplitude for each possible final collection of particles. The quantum calculation takes us from the Lagrangian to **transition amplitudes**.

## What a scattering experiment measures

A scattering experiment prepares incoming particles with specified beam properties, such as momenta and polarizations, and counts the outgoing particles. In Compton scattering, an electron and a photon enter. Detectors record the energies and directions of the scattered electron and photon.

The count also depends on beam intensity and the amount of target material. To compare the interaction across experiments, divide out those effects and report a cross section.

## The cross section

The **cross section** $\sigma$ measures the strength of scattering in units of area. Let $\Phi$ be the incident flux, the number of beam particles crossing unit area per unit time, and let $N$ be the number of exposed target particles. For a thin target with independent scattering, the event rate is

$$\text{rate} = \Phi\,N\,\sigma.$$

Experimenters infer $\sigma$ from the event rate, flux, and target count. A standard unit is the barn. For an unstable particle, the corresponding observable is its **decay rate** $\Gamma$, which we also calculate from a transition amplitude.

## The amplitude and the S-matrix

**First calculate the amplitude.** Write the incoming state as $\lvert i\rangle$ and the outgoing state as $\lvert f\rangle$. Their transition amplitude is the matrix element

$$\langle f | S | i \rangle,$$

A **matrix element** is the number obtained by applying an operator to one state and taking its overlap with another. Here $S$, the **S-matrix**, maps incoming free-particle states to outgoing ones.

The overlap $\langle f|i\rangle$ is the contribution from free passage without scattering. Separate it from the interaction contribution using the convention

$$\langle f | S | i \rangle = \langle f | i \rangle + (2\pi)^4\,\delta^4(P_f - P_i)\;i\mathcal{M}.$$

Here $P_i$ and $P_f$ are the total incoming and outgoing four-momenta. The delta function enforces energy and momentum conservation. After factoring it out, the remaining quantity $\mathcal M$ is the **invariant amplitude**.

The amplitude depends on the interaction and on the external momenta and spin states. Lorentz-invariant combinations of momenta describe its kinematic dependence. Changing the physical collision energy or scattering angle changes the amplitude; describing the same process in another frame preserves the corresponding physical prediction.

## From amplitude to cross section

**Square the amplitude and sum over allowed outcomes.** Schematically, the cross section has the form

$$\sigma = \frac{1}{\Phi}\int |\mathcal{M}|^{2}\; d\Pi,$$

Here $d\Pi$ is the **phase-space measure**, which integrates over final momenta and includes energy and momentum conservation. The denominator represents the incident-flux normalization appropriate to the scattering states; its precise form depends on their normalization and is not the laboratory particle flux used above.

The factor $|\mathcal M|^2$ depends on the dynamics through the interaction Lagrangian. Squaring follows the Born rule introduced in [First Quantization](first-quantization.md). The phase-space measure supplies the kinematics: which final momenta are possible and how to count them. Sum over unobserved final spins and average over an unpolarized initial ensemble when needed.

## The missing piece

We can now separate the calculation into two steps:

$$\mathcal{L} \;\longrightarrow\; \mathcal{M} \;\longrightarrow\; \sigma,$$

We have described the second step, from amplitude to cross section. [Perturbation Theory](perturbation-theory.md) derives the amplitude from the interaction Lagrangian. [Feynman Rules for QED](feynman-rules.md) then applies that method to Compton scattering.
