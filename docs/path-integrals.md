# Path Integrals in Quantum Mechanics

**Optional extra.** These five pages follow [The Standard Model](standard-model.md) and offer another perspective on quantum theory. They complement the main sequence and are not prerequisites for it.

The [Feynman Rules page](feynman-rules.md) calculated amplitudes by expanding the S-matrix and pairing fields. **Path integrals provide another way to calculate the same amplitudes**, using the action introduced in [Classical Mechanics](classical-mechanics.md).

This five-page sequence explains the ideas behind particle paths, field histories, fermions, gauge fixing, and renormalization. It complements the operator approach already developed in these notes. We keep $\hbar$ explicit on this page.

## Add amplitudes for the alternatives

Suppose a particle starts at position $x_i$ and is detected later at $x_f$. Quantum mechanics gives an amplitude for this transition. Its squared magnitude, with the appropriate treatment of the initial and final states, determines a probability.

If several unobserved alternatives lead to the same final state, their amplitudes add before we calculate a probability. This is the interference principle used for the two Compton diagrams.

Apply that principle to an intermediate time. The particle could pass through different intermediate positions. For each position, multiply the amplitude for reaching it by the amplitude for continuing to the endpoint. Then add over the possible positions:

$$\text{total amplitude}=\sum_{\text{intermediate positions}}
(\text{amplitude for the first part})(\text{amplitude for the second part}).$$

Position is continuous, so the sum is an integral. Introducing more intermediate times means integrating over more intermediate positions. Each choice of positions describes a possible history. In the limit of arbitrarily small time steps, this becomes a **sum over paths**.

These intermediate positions are not measured. Measuring them would change the experiment and generally change the interference.

## The action determines the phase

For a particle moving in a potential $V(x)$, the classical action is

$$S[x]=\int_{t_i}^{t_f}dt\left(\frac12m\dot x^2-V(x)\right).$$

The notation $S[x]$ means “evaluate the action for the history $x(t)$.” Different histories generally have different actions.

The short-time quantum evolution gives each history a phase factor

$$e^{iS[x]/\hbar}.$$

The action has the same units as $\hbar$, so the exponent is dimensionless. Just as complex amplitudes can be drawn as arrows in a plane, this factor has an angle $S[x]/\hbar$. Histories with similar phases reinforce one another; histories with opposing phases cancel.

The compact expression is

$$\boxed{K(x_f,t_f;x_i,t_i)=\int\mathcal D x\,e^{iS[x]/\hbar}}.$$

Here $K$ is the propagation amplitude, and $\mathcal D x$ means integrating over the intermediate positions while keeping the endpoints fixed. It also includes the normalization needed to reproduce quantum time evolution. The formula is shorthand for the time-slicing procedure above.

**The phase factor is not a probability for a particular path.** The measurable prediction comes from adding the contributions and then forming a probability. The formula does not assign a secretly selected classical trajectory to the particle.

## Why classical motion appears

Classical mechanics selects paths for which the action is stationary: a small change of path produces no first-order change in the action. This is the principle $\delta S=0$ used to obtain the equations of motion.

The path integral explains why that principle appears. When action differences are large compared with $\hbar$, the phases change rapidly as we move between nearby histories. Many contributions cancel. Near a stationary-action path, phases vary more slowly, allowing nearby contributions to reinforce one another.

For a free particle with fixed endpoints, the classical path is straight motion at constant velocity. The quantum calculation still includes other histories. In the appropriate classical limit, stationary paths organize the dominant contributions.

Stationary does not always mean minimum, and more than one stationary path can contribute. Classical motion is an approximation to the quantum result, not an extra restriction imposed on the sum.

## Example: a free particle

Let $T=t_f-t_i>0$. Evaluating the free-particle path integral gives

$$K_0=\sqrt{\frac{m}{2\pi i\hbar T}}
\exp\!\left[\frac{im(x_f-x_i)^2}{2\hbar T}\right].$$

Two features of this result have a direct interpretation. The action of the straight classical path is $m(x_f-x_i)^2/(2T)$, which appears in the exponential. The square-root prefactor comes from summing the fluctuations around that path and supplies the normalization.

The phase alone is therefore insufficient. As the elapsed time shrinks to zero, propagation must leave the initial wavefunction unchanged. The full expression has this property when used to evolve a wavefunction; keeping only its exponential would fail it.

This example shows how classical action can appear inside an exact quantum answer without excluding nonclassical histories.

## From particle paths to field histories

For a particle, a history specifies its position at every time. For a field, a history specifies the field's value throughout space at every time. The same action-based idea extends to these field histories.

A Feynman diagram is not one of the paths or field histories being summed over. It records a term in an expansion of the resulting integral. The next page, [Path Integrals for Fields](path-integrals-fields.md), connects that expansion to the propagators and vertices already used in these notes.
