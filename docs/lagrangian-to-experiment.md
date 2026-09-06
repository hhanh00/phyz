# From Lagrangian to Experiment

The previous pages built Lagrangians — first for classical particles, then for fields, culminating in the QED Lagrangian. But none of them said what a Lagrangian is *for* in a way that reaches an experiment. This page closes that gap: given a Lagrangian, what do we compute, and how does the result meet a measurement? The short answer is that a Lagrangian's job changes as the theory goes from classical mechanics to quantum field theory, and this page follows that change to the one number an experiment actually reads off.

## The job of a Lagrangian

In classical mechanics a Lagrangian's job is to produce a trajectory. The [Classical Mechanics](classical-mechanics.md) page built the principle of least action, and the [Action and Lagrangians](qft-action.md) page turned it into the Euler–Lagrange equation: feed the Lagrangian $L(q, \dot q)$ through the variational principle, get an equation of motion, and solve it for $q(t)$ and $\dot q(t)$ — where the particle is and how fast, at every instant. The trajectory is the entire output. A Lagrangian is worth having because one function $L$ generates every trajectory of the system, and an experiment picks one initial condition, not a new $L$.

## Why a trajectory is the wrong target

That output stops making sense at the quantum level. A quantum particle has no definite position to trace, and a quantum field can create and destroy particles, so there is no fixed list of "the particles" whose path we follow. [First Quantization](first-quantization.md) already traded the trajectory for the wave function $\psi$, an amplitude for *where* the particle is; [Field Quantization](field-quantization.md) went one level further, so the natural object is an amplitude for *which particles are present* in the final state. In place of a path, the Lagrangian must produce transition amplitudes.

## What a scattering experiment measures

A scattering experiment does the same thing in every subfield: it prepares a definite initial state — a beam of particles with chosen momenta and spins — and counts how often each possible final state appears. For Compton scattering the initial state is an electron and a photon with known momenta, and the detector counts scattered electrons and photons as a function of their angle and energy. The theory's job is to predict those counts. But counts depend on the apparatus — how dense the target is, how many particles the beam delivers — so the prediction is stated in an apparatus-independent form called the cross section.

## The cross section

The cross section $\sigma$ is the effective area a target presents to the beam. If the beam delivers $\Phi$ particles per unit area per unit time — the flux — and the target presents $N$ particles, then the rate of scattering events is

$$\text{rate} = \Phi\,N\,\sigma.$$

The cross section absorbs all the physics; the flux and the target count are experimental details that factor out. It has units of area, and the standard unit is the barn. Measuring a cross section means counting events for a known flux and target and solving for $\sigma$; predicting a cross section means computing $\sigma$ from the Lagrangian. Everything the theory has to say about an experiment is packaged in $\sigma$. A particle that decays is measured by the analogous number, the decay rate $\Gamma$, built from the amplitude in the same way.

## The amplitude and the S-matrix

Between the Lagrangian and the cross section sits the scattering amplitude. When a state $\lvert i\rangle$ is prepared and later measured as $\lvert f\rangle$, the amplitude for that transition is the matrix element

$$\langle f | S | i \rangle,$$

where $S$ is the S-matrix, the operator that carries the incoming state to the outgoing one. If nothing happens — the particles pass through freely — the matrix element is just the overlap $\langle f | i \rangle$; the interesting part is what remains, conventionally written

$$\langle f | S | i \rangle = \langle f | i \rangle + (2\pi)^4\,\delta^4(P_f - P_i)\;i\mathcal{M}.$$

The labels $P_i$ and $P_f$ name the total four-momentum each state carries, the sum of the four-momenta of the particles it contains: for Compton scattering the initial state holds one electron and one photon, so $P_i$ is their two four-momenta added, and $P_f$ is the sum for the scattered pair. The delta $\delta^4(P_f - P_i)$ vanishes unless the two totals agree, and the conservation law it states is that the incoming and outgoing particles carry the same total energy and the same total momentum. $\mathcal{M}$ — the invariant amplitude — is the object that carries the dynamics. The name "invariant" means Lorentz invariant: $\mathcal{M}$ takes the same value in every frame, since observers may disagree on momenta but must agree on the outcome of the experiment. It is not a constant, however — it is a function of the momenta themselves, through combinations like the center-of-mass energy and scattering angle, so it varies from one final state to another. The Lagrangian determines $\mathcal{M}$, and the Feynman rules compute it.

## From amplitude to cross section

The cross section is built from the amplitude by squaring it and integrating over the allowed final states,

$$\sigma = \frac{1}{\Phi}\int |\mathcal{M}|^{2}\; d\Pi,$$

where $d\Pi$ is the phase space, the measure over the final particles' momenta that enforces energy and momentum conservation. The formula splits into two independent ingredients. $|\mathcal{M}|^2$ carries the physics — it is where the interaction term of the Lagrangian lives, and the square is the Born rule of [First Quantization](first-quantization.md), which reads probabilities off squared amplitudes. $d\Pi$ carries the kinematics — it is geometry, the space of final states the conservation law permits. The kinematics can be handled once and for all; the physics is the part that changes from process to process.

## The missing piece

The chain from a Lagrangian to a number an experiment can check is therefore

$$\mathcal{L} \;\longrightarrow\; \mathcal{M} \;\longrightarrow\; \sigma,$$

and every step except the first is mechanical. Squaring and integrating an amplitude is straightforward, given the amplitude. The one genuinely hard step is the first: turning the Lagrangian into the amplitude $\mathcal{M}$. For QED the interaction term $-q\bar\psi\gamma^\mu\psi\,A_\mu$ makes the theory nonlinear, so $\mathcal{M}$ must be assembled as a series in the charge $q$, and that series is the combinatorial bookkeeping the [Feynman Rules for QED](feynman-rules.md) page is about. This page has located $\mathcal{M}$; the next page describes how to get it.
