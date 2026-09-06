# From Lagrangian to Experiment

The previous pages built Lagrangians for particles and fields. This page follows the calculation from a Lagrangian to a scattering cross section, the quantity we compare with experiment.

## The job of a Lagrangian

In classical mechanics a Lagrangian's job is to produce a trajectory. The [Classical Mechanics](classical-mechanics.md) page built the principle of least action, and the [Action and Lagrangians](qft-action.md) page turned it into the Euler–Lagrange equation: feed the Lagrangian $L(q, \dot q)$ through the variational principle, get an equation of motion, and solve it for $q(t)$ and $\dot q(t)$ — where the particle is and how fast, at every instant. The initial conditions select a particular trajectory.

## Why a trajectory is the wrong target

That output stops making sense at the quantum level. A quantum particle has no definite position to trace, and a quantum field can create and destroy particles, so there is no fixed list of "the particles" whose path we follow. [First Quantization](first-quantization.md) already traded the trajectory for the wave function $\psi$, an amplitude for *where* the particle is; [Field Quantization](field-quantization.md) went one level further, so the natural object is an amplitude for *which particles are present* in the final state. In place of a path, the Lagrangian must produce transition amplitudes.

## What a scattering experiment measures

A scattering experiment does the same thing in every subfield: it prepares a definite initial state — a beam of particles with chosen momenta and spins — and counts how often each possible final state appears. For Compton scattering the initial state is an electron and a photon with known momenta, and the detector counts scattered electrons and photons as a function of their angle and energy. But counts depend on the apparatus — how dense the target is, how many particles the beam delivers — so the prediction is stated in an apparatus-independent form called the cross section.

## The cross section

The cross section $\sigma$ is the effective area a target presents to the beam. If the beam delivers $\Phi$ particles per unit area per unit time — the flux — and the target presents $N$ particles, then the rate of scattering events is

$$\text{rate} = \Phi\,N\,\sigma.$$

The cross section has units of area, and the standard unit is the barn. Experimenters determine $\sigma$ from the measured event rate, flux, and target count. A particle that decays is measured by the analogous number, the decay rate $\Gamma$, built from the amplitude in the same way.

## The amplitude and the S-matrix

Between the Lagrangian and the cross section sits the scattering amplitude. When a state $\lvert i\rangle$ is prepared and later measured as $\lvert f\rangle$, the amplitude for that transition is the matrix element

$$\langle f | S | i \rangle,$$

where $S$ is the S-matrix, the operator that carries the incoming state to the outgoing one. If nothing happens — the particles pass through freely — the matrix element is just the overlap $\langle f | i \rangle$; the interesting part is what remains, conventionally written

$$\langle f | S | i \rangle = \langle f | i \rangle + (2\pi)^4\,\delta^4(P_f - P_i)\;i\mathcal{M}.$$

Here $P_i$ and $P_f$ are the total incoming and outgoing four-momenta. The delta function $\delta^4(P_f - P_i)$ enforces conservation of energy and momentum. $\mathcal{M}$ — the invariant amplitude — is the object that carries the dynamics. The name "invariant" means Lorentz invariant: $\mathcal{M}$ takes the same value in every frame, since observers may disagree on momenta but must agree on the outcome of the experiment. It is not a constant, however — it is a function of the momenta themselves, through combinations like the center-of-mass energy and scattering angle, so it varies from one final state to another.

## From amplitude to cross section

The cross section is built from the amplitude by squaring it and integrating over the allowed final states,

$$\sigma = \frac{1}{\Phi}\int |\mathcal{M}|^{2}\; d\Pi,$$

where $d\Pi$ is the phase space, the measure over the final particles' momenta that enforces energy and momentum conservation. The formula splits into two independent ingredients. $|\mathcal{M}|^2$ carries the physics — it is where the interaction term of the Lagrangian lives, and the square is the Born rule of [First Quantization](first-quantization.md), which reads probabilities off squared amplitudes. $d\Pi$ carries the kinematics — it is geometry, the space of final states the conservation law permits.

## The missing piece

The chain from a Lagrangian to a number an experiment can check is therefore

$$\mathcal{L} \;\longrightarrow\; \mathcal{M} \;\longrightarrow\; \sigma,$$

with the amplitude-to-cross-section step described above. What remains is to compute $\mathcal{M}$ from the interaction term of the Lagrangian. The next page, [Perturbation Theory](perturbation-theory.md), shows that the interaction term alone generates this computation, and the page after, [Feynman Rules for QED](feynman-rules.md), runs it for Compton scattering.
