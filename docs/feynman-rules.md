# Feynman Rules for QED

## The need for Feynman diagrams

The [From Lagrangian to Experiment page](lagrangian-to-experiment.md) connected the scattering amplitude $\mathcal{M}$ to a measurable cross section, and the [Perturbation Theory page](perturbation-theory.md) derived the rules by which a Lagrangian's interaction term generates amplitudes. We now apply those rules to the [QED Lagrangian](qed.md),

$$\mathcal{L}_\text{QED} = -\tfrac14 F_{\mu\nu}F^{\mu\nu} \;+\; \bar\psi\left(i\hbar\gamma^\mu\partial_\mu - m\right)\psi \;-\; q\,\bar\psi\gamma^\mu\psi\,A_\mu .$$

The first two pieces describe free photons and electrons. The interaction term $-q\bar\psi\gamma^\mu\psi\,A_\mu$ couples the photon field to the electron current. We expand the scattering amplitude in powers of the charge $q$, with each application of the interaction contributing one more power. This is a perturbative expansion: we approximate the amplitude by retaining the lowest orders, then include higher orders to refine the calculation.

Each application also contributes two fermion fields and one photon field. Computing a term in the expansion means accounting for how these fields connect to the incoming and outgoing particles and pair with one another. The number of possible pairings grows quickly with the order of the expansion.

A Feynman diagram organizes these contributions as a picture. Lines represent particles, and vertices represent applications of the interaction. The Feynman rules translate each diagram into its contribution to the amplitude.

## Compton Scattering Example

In Compton scattering, an electron and a photon enter, and an electron and a photon leave:

$$e^-(p) + \gamma(k) \;\longrightarrow\; e^-(p') + \gamma(k').$$

The labels denote four-momenta, with $p+k=p'+k'$. From here onward we use natural units, $\hbar=c=1$, and the metric $g_{\mu\nu}=\operatorname{diag}(1,-1,-1,-1)$.

The QED interaction contains one photon field, so a single vertex cannot accommodate both the incoming and outgoing photon. The lowest-order contribution needs two vertices joined by an electron line. There are two ways to attach the photons along that line.

```feynman
\begin{tikzpicture}
\begin{feynman}
\vertex (i) at (-2,-1) {$e^-(p)$};
\vertex (a) at (0,0);
\vertex (b) at (2,0);
\vertex (f) at (4,-1) {$e^-(p')$};
\vertex (ki) at (-2,1) {$\gamma(k)$};
\vertex (kf) at (4,1) {$\gamma(k')$};
\diagram* {
(i) -- [fermion] (a) -- [fermion, edge label={$p+k$}] (b) -- [fermion] (f),
(ki) -- [photon] (a),
(b) -- [photon] (kf),
};
\end{feynman}
\end{tikzpicture}
```

*s-channel[^mandelstam]: the incoming photon attaches at the first vertex, and the internal electron carries $p+k$.*

In the first diagram, the incoming photon attaches first when we follow the electron arrow. Momentum conservation gives the internal electron momentum $p+k$.

```feynman
\begin{tikzpicture}
\begin{feynman}
\vertex (i) at (-2,-1) {$e^-(p)$};
\vertex (a) at (0,0);
\vertex (b) at (2,0);
\vertex (f) at (4,-1) {$e^-(p')$};
\vertex (kf) at (-2,1) {$\gamma(k')$};
\vertex (ki) at (4,1) {$\gamma(k)$};
\diagram* {
(i) -- [fermion] (a) -- [fermion, edge label={$p-k'$}] (b) -- [fermion] (f),
(a) -- [photon] (kf),
(ki) -- [photon] (b),
};
\end{feynman}
\end{tikzpicture}
```

*u-channel: the incoming photon attaches at the second vertex, and the internal electron carries $p-k'$.*

In the second diagram, the outgoing photon attaches first, giving internal momentum $p-k'$. These are two contributions to the same transition amplitude, not two experimentally distinguishable histories. We add them before squaring.

## Building Blocks of Feynman Diagrams

A **fermion line** is a straight line with an arrow. It represents the Dirac field, which describes both electrons and positrons. The arrow follows fermion-number flow: it points along an electron's physical propagation and against a positron's. A **photon line** is wavy and has no fermion arrow.

A **vertex** joins two fermion-line ends and one photon line, matching the fields in $-q\bar\psi\gamma^\mu\psi A_\mu$. Charge and four-momentum are conserved at every vertex. QED has no elementary vertex joining photons alone.

An **external line** ends at an incoming or outgoing state. Its momentum satisfies the physical mass relation, $p^2=m^2$ for an electron or $k^2=0$ for a photon; we call this being **on shell**. An **internal line** connects vertices and contributes a propagator, the factor describing propagation between interactions. Its momentum need not satisfy the mass relation, so it can be **off shell**. Such internal contributions are often called virtual particles. They are not separately detected particles, and they do not violate energy conservation.

Both Compton diagrams have four external lines, two vertices, and one internal electron line. Their different photon attachments change the internal momentum and therefore the propagator.

## Feynman Rules and Amplitudes

Reading a diagram back into an amplitude runs on a fixed translation, the **Feynman rules**: the interaction term fixes the factor at each vertex, the free terms fix the factors on the internal lines, and the external lines carry the single-particle wave functions. Compton scattering needs only these four rules.

| Diagram element | Factor |
| --- | --- |
| Electron–photon vertex | $-iq\gamma^\mu$ |
| Internal electron with momentum $r$ | $\displaystyle \frac{i(\not r+m)}{r^2-m^2+i\epsilon}$ |
| Incoming / outgoing electron | $u(p)$ / $\bar u(p')$ |
| Incoming / outgoing photon | $\varepsilon_\mu(k)$ / $\varepsilon_\mu^*(k')$ |

The table abbreviates objects the site has met. The vertex factor $-iq\gamma^\mu$ is the interaction term $-q\bar\psi\gamma^\mu\psi A_\mu$ with its three fields stripped off, and $\gamma^\mu$ are the Dirac matrices of [The Dirac Equation page](dirac-equation.md); $\not r$ is shorthand for the contraction $\gamma^\mu r_\mu$. The internal-electron factor is the propagator of that Dirac field: promoting the field the way the [Field Quantization page](field-quantization.md) promotes the scalar yields the vertex at every interaction and this factor between them, which is why it carries the electron mass and its Dirac structure. The $+i\epsilon$ in the denominator handles the propagator's poles and stays inert until an internal momentum is integrated over, as in the loop diagrams below[^epsilon]. The spinor $u(p)$ on the electron's external lines is the momentum-dependent positive-energy solution of the Dirac equation that [The Dirac Equation page](dirac-equation.md) built, and $\bar u(p')=u(p')^\dagger\gamma^0$ is its adjoint. The photon's factor $\varepsilon_\mu(k)$ is its polarization four-vector, which this page is the first to need and defines in a footnote[^polarization]. The remaining QED rules — the photon propagator, positron lines, and the gauge choice behind them — do not enter these two diagrams, so we park them in a footnote[^rulebook].

To translate the first Compton diagram into an amplitude, read along the electron's arrow: put the outgoing electron's factor $\bar u(p')$ on the left, the vertex factors and the electron propagator in the order the arrow meets them, and close with the incoming electron's factor $u(p)$ on the right:

$$
i\mathcal{M}_s = \bar u(p')(-iq\gamma^\nu)
\frac{i(\not p+\not k+m)}{(p+k)^2-m^2+i\epsilon}
(-iq\gamma^\mu)u(p)\,
\varepsilon_\mu(k)\varepsilon_\nu^*(k').
$$

The second diagram reverses the photon attachments:

$$
i\mathcal{M}_u = \bar u(p')(-iq\gamma^\mu)
\frac{i(\not p-\not k'+m)}{(p-k')^2-m^2+i\epsilon}
(-iq\gamma^\nu)u(p)\,
\varepsilon_\mu(k)\varepsilon_\nu^*(k').
$$

The subscripts refer to the momentum combinations $s=(p+k)^2$ and $u=(p-k')^2$. Spin labels are suppressed. Gamma matrices do not generally commute, so their order matters. The diagram factors give $i\mathcal{M}$, matching the S-matrix convention of the [From Lagrangian to Experiment page](lagrangian-to-experiment.md).

The leading amplitude is $\mathcal{M}_{\mathrm{tree}}=\mathcal{M}_s+\mathcal{M}_u$. Its square contains interference:

$$|\mathcal{M}_{\mathrm{tree}}|^2
=|\mathcal{M}_s|^2+|\mathcal{M}_u|^2
+2\operatorname{Re}(\mathcal{M}_s\mathcal{M}_u^*).$$

For unpolarized beams, average this expression over the two initial electron spins and two initial photon polarizations, and sum over the unobserved final spins and polarizations. The result enters the phase-space integral for the cross section.

## Tree-level and Loop Diagrams

A **tree diagram** has no closed cycle of internal lines. Once the external momenta are specified, conservation at its vertices fixes every internal momentum. Both diagrams above are trees, and each has two vertices, so the Compton tree amplitude is of order $q^2$ and its squared amplitude is of order $q^4$.

At higher orders, an additional internal photon can connect two points on the electron line, forming a cycle together with the electron segment between them. Momentum conservation now leaves a four-momentum $\ell$ undetermined. We integrate over it, including a factor

$$\int\frac{d^4\ell}{(2\pi)^4}$$

for each independent loop. A loop need not consist of a closed fermion line; the electron–photon cycle just described is already a loop. A closed fermion line contributes an additional minus sign and a trace over its spinor indices.

For Compton scattering, one-loop contributions have four interaction vertices and are of order $q^4$ in the amplitude. Their interference with the tree amplitude gives a correction of order $q^6$ to the squared amplitude:

$$|\mathcal{M}|^2
=|\mathcal{M}_{\mathrm{tree}}|^2
+2\operatorname{Re}\!\left(\mathcal{M}_{\mathrm{tree}}^*
\mathcal{M}_{\mathrm{one\ loop}}\right)+\cdots.$$

We must include all diagrams and counterterms at the chosen order. Keeping one selected loop diagram generally does not give a complete physical correction.

## Infinities in Loop Diagrams

The loop integral ranges over arbitrarily large momenta. If the propagators and numerator do not suppress the integrand sufficiently, this region produces an **ultraviolet divergence**. For example, an integral with large-momentum behavior $\int d^4\ell/(\ell^2)^2$ diverges logarithmically. Not every loop integral diverges.

To calculate with such expressions, first introduce a **regulator**, a temporary modification that makes the divergence explicit. Dimensional regularization continues the integral to $d=4-2\delta$ dimensions, where ultraviolet divergences appear as poles in $1/\delta$.

Next, express the Lagrangian's parameters and field normalizations in terms of renormalized quantities plus **counterterms**. These additional terms cancel the regulated ultraviolet divergences order by order. Fix the renormalized mass and charge through specified measurement conditions, and remove the regulator from the resulting predictions. This procedure is **renormalization**. In QED, the required counterterms have the same forms as terms already present in the Lagrangian, so a finite set of parameter and field redefinitions suffices at every perturbative order. [Forshaw's QED and QCD lectures](https://users.hep.manchester.ac.uk/u/jforshaw/NorthWest/QED.pdf) introduce this construction.

Massless photons also produce **infrared divergences** when a loop photon's momentum approaches zero. Renormalization does not remove these. A detector cannot distinguish an event with no extra photon from one with an additional photon below its energy resolution. Including that unresolved real emission together with the virtual corrections cancels the soft divergences in the inclusive observable. Thus a correction to the measured Compton rate includes both loop diagrams and sufficiently soft additional-photon emission.

[^mandelstam]: The channel names come from the Mandelstam variables, the three Lorentz-invariant ways to pair the four external momenta of a $2\to2$ process: $s=(p+k)^2=(p'+k')^2$, $t=(p-p')^2$, and $u=(p-k')^2$. Each variable is the squared total momentum of the pair that fuses into the exchanged line, so the name of a channel records which momentum combination appears in its propagator. In both diagrams here the exchanged line is the electron. An incoming electron and the incoming photon fuse at a vertex into $p+k$, which names the **s-channel**; an incoming electron and an *outgoing* photon pair as $p-k'$, which names the **u-channel**. The third pairing, $t=(p-p')^2$, would put the two electrons at one vertex and the two photons at the other, and a QED vertex cannot host that, because each vertex couples one photon to two fermion lines and never two photons to each other. Compton scattering therefore has no t-channel diagram, and the Mandelstam variables are not independent: for massless external particles $s+t+u=0$.

[^epsilon]: The denominator $r^2-m^2$ of the electron propagator vanishes on the electron's mass shell, $r^2=m^2$. The infinitesimal $+i\epsilon$ shifts those poles slightly off the real axis and records which way a momentum integral is to pass them. When an internal momentum is fixed by the external momenta, as in both tree diagrams here, the propagator never sits exactly on a pole and the prescription stays inert; it becomes essential in the loop integrals of the last sections.

[^polarization]: The photon is massless and transverse, so its polarization has two independent states, the two transverse directions (equivalently the two helicities). The four-vector $\varepsilon_\mu(k)$ points along the oscillation direction of a photon with momentum $k$ and is transverse to it, $k^\mu\varepsilon_\mu(k)=0$; an outgoing photon carries the complex conjugate $\varepsilon_\mu^*(k')$.

[^rulebook]: The general QED menu adds two rules this page never needs. An internal photon line carries the propagator $-ig_{\mu\nu}/(r^2+i\epsilon)$, written here in Feynman gauge, and positron external lines carry $\bar v(p)$ and $v(p)$ instead of the electron spinors. Deriving the photon propagator requires quantizing the free photon field and fixing its gauge freedom, which this site does not attempt, so we adopt these rules as given; the conventions used throughout agree with [David Tong's QED notes](https://www.damtp.cam.ac.uk/user/tong/qft/qfthtml/S6.html).
