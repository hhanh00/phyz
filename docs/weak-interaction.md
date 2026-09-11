# Weak Interaction

In [QED](qed.md), the photon couples to a current built from one charged fermion field. Weak interactions also connect different fermion species: a neutron can decay into a proton, an electron, and an antineutrino. We build an interaction that accounts for the particles and chiral preference seen in beta decay, then connect its strength to exchange of a heavy force carrier. We use natural units, $\hbar=c=1$.

<details>
<summary>Notation and mass dimensions</summary>

In this table, $[X]$ means the **mass dimension** of $X$: its power of
energy in natural units. In four spacetime dimensions the Lagrangian density
has dimension $[\mathcal L]=4$.

| Symbol | Meaning | Mathematical role | Mass dimension |
| --- | --- | --- | ---: |
| $x^\mu$ | spacetime point | $x\in\mathbb R^{1,3}$, $\mu=0,1,2,3$ | $-1$ |
| $\partial_\mu$ | spacetime derivative | $\partial_\mu=\partial/\partial x^\mu$ | $1$ |
| $p^\mu$, $k^\mu$, $q^\mu$ | particle, mode, or exchanged momentum | four-vectors | $1$ |
| $e(x),\nu_e(x),u(x),d(x)$ | fermion fields | four-component Dirac spinor fields | $\tfrac32$ |
| $\bar\psi$ | Dirac adjoint | $\bar\psi=\psi^\dagger\gamma^0$ | $\tfrac32$ |
| $\gamma^\mu$, $\gamma^5$ | spinor matrices | act on Dirac components | $0$ |
| $P_L$, $P_R$ | chiral projectors | $P_{L,R}=(1\mp\gamma^5)/2$ | $0$ |
| $L$, $Q_L$ | left-chiral doublets | $L=(\nu_{eL},e_L)^T$, $Q_L=(u_L,d_L)^T$ | $\tfrac32$ |
| $j^\mu$ | weak current | bilinear such as $\bar e_L\gamma^\mu\nu_{eL}$ | $3$ |
| $W_\mu^a$, $W_\mu^\pm$ | weak gauge fields | $a=1,2,3$ labels the three $SU(2)$ generators | $1$ |
| $T^a$ | $SU(2)$ generators | $T^a=\sigma^a/2$; act on doublet entries | $0$ |
| $g$ | weak gauge coupling | coefficient in $D_\mu=\partial_\mu+igW_\mu^aT^a$ | $0$ |
| $m_W$, $m_n$, $m_p$, $m_e$ | masses | parameters with dimensions of energy | $1$ |
| $G_F$ | Fermi constant | low-energy four-fermion coupling | $-2$ |

The $e$ in $e(x)$ denotes the **electron field**, while the $e$ in a charge
such as $-e$ denotes the positive elementary-charge magnitude. The symbols
$a,b,c$ label internal $SU(2)$ directions; $\mu,\nu$ label spacetime
components. They are different kinds of indices.

</details>

The steps connect as follows:

1. **Start with the observations.** Beta decay specifies the particles we must produce; parity and other weak-interaction measurements add a chiral preference.
2. **Write the required transitions.** Projectors select the left-chiral parts of the fields. Currents combine those fields to describe the down-to-up transition and creation of the electron–antineutrino pair.
3. **Connect the transitions.** Multiplying the currents gives a direct low-energy interaction. We then propose a heavy $W$ carrier connecting them through two vertices, and seek a broader theory for its couplings.
4. **Find a symmetry to organize those couplings.** Just as a phase change preserves the free QED Lagrangian, certain mixtures of each field pair preserve its free, massless Lagrangian. These include SU(2).
5. **Make that symmetry local.** Allowing the mixing to vary across spacetime requires compensating fields: one per SU(2) generator, giving three fields.
6. **Read the resulting interactions.** Expanding the modified Lagrangian identifies the charged $W^\pm$ couplings and the neutral $W^3$ couplings. The charged terms join to produce beta decay; kinetic terms let the carrier propagate between the vertices.
7. **Return to the low-energy experiment.** Heavy-$W$ exchange reduces to the direct interaction from step 3, relating its measured strength to the $W$ coupling and mass.

## Beta Decay and Neutrinos

Beta decay introduces several new particles at once, so it helps to name what they buy. Working through the decay forces three conclusions. First, the electron energy is not fixed, so a third, invisible particle carries off the difference — the neutrino. Second, the decay turns a down quark into an up quark, a change of species the photon cannot produce. Third, the decay pairs an electron with an antineutrino rather than a neutrino, a rule the gauge theory will have to reproduce. Each conclusion becomes a target the rest of the chapter aims at.

Protons and neutrons are the particles that make up atomic nuclei; together we call them **nucleons**. Both are composite particles built from quarks. Electrons and neutrinos are **leptons**, elementary spin-½ particles that do not participate in the strong interaction that binds quarks.

The particles needed for beta decay are:

| Particle | Symbol | Electric charge |
| --- | --- | --- |
| Neutron | $n$ | $0$ |
| Proton | $p$ | $+e$ |
| Electron | $e^-$ | $-e$ |
| Electron neutrino / antineutrino | $\nu_e$ / $\bar\nu_e$ | $0$ |
| Up quark | $u$ | $+2e/3$ |
| Down quark | $d$ | $-e/3$ |

The subscript $e$ identifies the neutrino **flavour** associated with an electron in a charged weak interaction. Flavour means particle species here; an electron neutrino is not an electron with its charge removed.

A free neutron undergoes **beta decay**:

$$n\longrightarrow p+e^-+\bar\nu_e.$$

Here $\bar\nu_e$ is the electron antineutrino. Electric charge balances: the neutral neutron produces a proton of charge $+e$, an electron of charge $-e$, and a neutral antineutrino.

```feynman
\begin{tikzpicture}
\begin{feynman}
\vertex (n) at (-2,0) {$n$};
\vertex [blob] (a) at (0,0) {};
\vertex (p) at (2,1.5) {$p$};
\vertex (e) at (2,0) {$e^-$};
\vertex (nu) at (2,-1.5) {$\bar\nu_e$};
\diagram* {
(n) -- [fermion] (a) -- [fermion] (p),
(a) -- [fermion] (e),
(nu) -- [fermion] (a),
};
\end{feynman}
\end{tikzpicture}
```

*Neutron beta decay, with the incoming neutron on the left and the three outgoing particles on the right. The shaded vertex summarizes the low-energy interaction of these composite nucleons; we resolve the quark transition and $W$ exchange later in this chapter. The antineutrino arrow points inward because arrows indicate fermion flow, not motion.*

If the final state contained only a proton and an electron, momentum conservation in the neutron rest frame would give $\mathbf p_p=-\mathbf p_e$. Writing their common momentum magnitude as $k$, energy conservation would then require

$$m_n=\sqrt{m_p^2+k^2}+\sqrt{m_e^2+k^2}.$$

Both terms increase with $k$, so this fixes one momentum magnitude and hence one electron energy. Instead, experiments show a continuous range of electron energies. With a third particle, the proton and electron momenta need not be opposite: the antineutrino carries the remaining momentum and energy. Different three-particle configurations give different electron energies. The neutrino hypothesis accounted for this missing energy; experiments later detected neutrinos directly.

Charge conservation cannot distinguish a neutrino from an antineutrino because both are neutral. For these reactions, assign **lepton number** $+1$ to leptons, $-1$ to antileptons, and $0$ to quarks and nucleons. Beta decay preserves the total: the electron contributes $+1$ and the antineutrino $-1$, matching the neutron's zero. The charged weak coupling we derive below produces precisely this pair. This bookkeeping concerns the processes here; it does not settle whether neutrinos are fundamentally distinct from their antiparticles when their masses are included.

Neutrinos have no electric charge, so they have no direct photon coupling of the kind used in QED. They participate in weak interactions, which makes them difficult to detect. The electron and antineutrino are created in the decay; they are not constituents stored inside the neutron.

At the quark level, the decay changes a down quark into an up quark:[^valence]

$$d\longrightarrow u+e^-+\bar\nu_e.$$

The charges again balance, since $-\tfrac13=\tfrac23-1$. Photon exchange cannot produce this change of quark species. We need an interaction that couples an up-quark field to a down-quark field, and a neutrino field to an electron field.

## Parity adds a requirement from experiment

There is also a difference in spin dependence. **Parity** reverses spatial coordinates, $\mathbf x\to-\mathbf x$, and hence momentum, $\mathbf p\to-\mathbf p$. Orbital angular momentum stays unchanged because $(-\mathbf r)\times(-\mathbf p)=\mathbf r\times\mathbf p$. Intrinsic spin transforms in the same way as angular momentum under parity.

A **polarized** sample has a preferred spin orientation instead of randomly oriented nuclear spins. Experimenters can compare how often beta-decay electrons emerge along or against that orientation. Under parity,

$$\mathbf S\cdot\mathbf p_e\longrightarrow-\mathbf S\cdot\mathbf p_e.$$

Thus the reversed experiment exchanges emission along the spin with emission against it, while retaining the same spin orientation.[^mirror] If the interaction preserved parity, those two directions would have equal rates. Wu and her collaborators observed this asymmetry in polarized cobalt-60 beta decay, in work published in 1957. The weak interaction therefore violates parity. This evidence comes from another beta-decay experiment, now measuring emission directions as well as energies. See the [NIST account of the experiment](https://www.nist.gov/pml/fall-parity/reversal-parity-law-nuclear-physics).

Parity violation tells us that the interaction distinguishes left from right. A Dirac field has two parts, called left- and right-chiral, which parity exchanges; we will define how to select them below. It does not, by itself, prove that only one chirality couples. The left-chiral charged current is a further empirical input, supported by weak-decay and neutrino measurements. We will build that choice into the theory.

The requirements and the tools we will use now fit together as follows:

| Physical requirement | How we will represent it |
| --- | --- |
| A third particle shares the decay energy and momentum | Include a neutrino field and a three-particle final state |
| A down quark becomes an up quark | Couple different species through a charged weak current |
| The electron accompanies an antineutrino | Use a lepton current whose fields create that pair |
| Charged weak interactions distinguish chirality | Select the left-chiral parts of the fermion fields |

Here a **current** is a combination of two fermion fields that we can couple to a force-carrying field. Its field content specifies which particles can meet at an interaction. First we construct those combinations. Then we introduce the force-carrying field that connects the quark interaction to the lepton interaction. Beta decay motivates this construction, but does not uniquely determine the full gauge theory.

## Selecting the chiral part of a field

A Dirac field represents a spin-½ particle and its antiparticle using four components at each point in spacetime. It contains left- and right-chiral parts. To put only the left part into an interaction, we need a mathematical operation that keeps it and removes the right part. That operation is the projector $P_L$. Define

$$\gamma^5=i\gamma^0\gamma^1\gamma^2\gamma^3,\qquad
P_L=\frac{1-\gamma^5}{2},\qquad P_R=\frac{1+\gamma^5}{2}.$$

The four spacetime gamma matrices $\gamma^0\dots\gamma^3$ carry a spacetime index; $\gamma^5$ is their product, and its "5" is a conventional label, not a fifth direction — which is why there is no $\gamma^4$.

It is useful to view $\gamma^5$ as a linear operator on the four-dimensional
spinor space $\mathbb C^4$. It has two eigenvalues, $-1$ and $+1$. Each occurs
twice: if their multiplicities are $n_-$ and $n_+$, then $n_-+n_+=4$, while
$\operatorname{tr}(\gamma^5)=0$ gives $n_+-n_-=0$. The trace vanishes because
$\gamma^0\gamma^5\gamma^0=-\gamma^5$ and the cyclic property of the trace
leaves $\operatorname{tr}(\gamma^5)=-\operatorname{tr}(\gamma^5)$. Thus
$n_-=n_+=2$. In a chiral basis,

$$
\gamma^5=\begin{pmatrix}
-1&0&0&0\\
0&-1&0&0\\
0&0&+1&0\\
0&0&0&+1
\end{pmatrix},
\qquad
\mathbb C^4=\mathbb C^2_L\oplus\mathbb C^2_R.
$$

A general spinor is usually not an eigenvector of $\gamma^5$; it is a sum
of a vector from each eigenspace. The projectors $P_L$ and $P_R$ extract
those two components. This is an operation in spinor space, not a quantum
field operator acting on a state.

The useful properties are $(\gamma^5)^2=1$ and $(\gamma^5)^\dagger=\gamma^5$. Its eigenvalues are therefore $-1$ and $+1$. On the $-1$ part, $P_L=(1-(-1))/2=1$; on the $+1$ part, $P_L=(1-1)/2=0$. It keeps exactly the part we call left-chiral. $P_R$ does the reverse.

<details>
<summary>Checking the gamma-matrix and projector algebra</summary>

To check these definitions, use $\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}$ from the Dirac chapter. Distinct gamma matrices anticommute, while $(\gamma^0)^2=1$ and $(\gamma^i)^2=-1$ for spatial indices. Bringing equal matrices together in the squared four-matrix product takes six exchanges, so

$$\begin{aligned}
(\gamma^5)^2
&=i^2(\gamma^0\gamma^1\gamma^2\gamma^3)^2\\
&=-(-1)^6(\gamma^0)^2(\gamma^1)^2(\gamma^2)^2(\gamma^3)^2
=-1\cdot1\cdot(-1)^3=1.
\end{aligned}$$

Moving any $\gamma^\mu$ through the other three distinct matrices gives three minus signs, hence $\gamma^\mu\gamma^5=-\gamma^5\gamma^\mu$. Also, $(\gamma^0)^\dagger=\gamma^0$ and $(\gamma^i)^\dagger=-\gamma^i$ give

$$ (\gamma^5)^\dagger
=(-i)(-1)^3\gamma^3\gamma^2\gamma^1\gamma^0
=i\gamma^0\gamma^1\gamma^2\gamma^3=\gamma^5,$$

where reversing the four matrices again takes six exchanges. Thus $\gamma^5$ is Hermitian and has eigenvalues $\pm1$. On a $-1$ eigenvector, $P_L$ acts as $1$ and $P_R$ as $0$; on a $+1$ eigenvector, the roles reverse. Direct multiplication gives

$$P_L^2=\frac{1-2\gamma^5+(\gamma^5)^2}{4}=P_L,\qquad
P_R^2=P_R,\qquad P_LP_R=0,\qquad P_L+P_R=1.$$

</details>

The matrices are therefore **projectors** onto the left- and right-handed **chiral components**:

$$\psi_L=P_L\psi,\qquad \psi_R=P_R\psi,\qquad
\psi=\psi_L+\psi_R.$$

Chirality labels these two parts of the spinor. Each part is a two-component spinor, and the two transform oppositely under a boost; left and right name that distinction. Chirality is different from spin up/down along a chosen axis. It is also different from the upper/lower pair used for the rest solutions in [The Dirac Equation](dirac-equation.md): in that standard basis, $\gamma^5$ mixes the upper and lower pairs. A change to a **chiral basis** makes $\gamma^5$ diagonal, so the left and right parts occupy separate pairs of entries. The projectors select the same physical chiral parts in either basis.

**Helicity** describes spin relative to the particle's own momentum: positive helicity means aligned, and negative helicity means opposed. For a massive particle, an observer who overtakes it can reverse its momentum without reversing its spin, changing the helicity label. Chirality instead labels the spinor's transformation under rotations and boosts. In the massless limit, a left-chiral field annihilates negative-helicity particles and creates positive-helicity antiparticles. For massive particles, a state of definite helicity generally contains both chiral components. We neglect neutrino masses in the processes discussed here.

<details>
<summary>Helicity versus chirality</summary>

Helicity compares a particle's spin with its direction of motion:

$$h\propto\frac{\mathbf S\cdot\mathbf p}{|\mathbf p|}.$$

Spin aligned with momentum gives positive helicity; spin opposed to momentum gives negative helicity. For a massive particle, helicity depends on the observer. An observer moving faster than the particle can see its momentum reverse while its spin orientation remains unchanged, so the particle's helicity changes sign.

Chirality is instead an intrinsic property of a spinor. The operators

$$P_L=\frac{1-\gamma^5}{2},\qquad P_R=\frac{1+\gamma^5}{2}$$

extract its left- and right-chiral components. These components transform differently under Lorentz transformations; chirality is therefore not simply spin up or spin down along a chosen axis.

For a massless particle, chirality and helicity coincide for particles:

$$\text{left-chiral particle}\leftrightarrow\text{negative helicity},\qquad
\text{right-chiral particle}\leftrightarrow\text{positive helicity}.$$

The relationship is reversed for antiparticles. Consequently, a left-chiral field annihilates negative-helicity particles and creates positive-helicity antiparticles. This is why the left-chiral weak interaction produces left-helicity neutrinos and right-helicity antineutrinos when neutrino masses are neglected.

For a massive fermion, a definite-helicity state generally contains both chiral components. In the ultra-relativistic limit, the unwanted component is suppressed by roughly $m/E$, so helicity is a good approximation to chirality, but they are not exactly the same. In this chapter we neglect neutrino masses, so the massless correspondence is sufficient.

</details>

**Given without proof:** the relation between chirality and particle/antiparticle helicity above. Proving it requires solving the Dirac equation in a helicity basis and identifying the particle and antiparticle modes, a longer calculation than the projector algebra here.

## Building a current that connects two species

The projector selects part of a field; it does not yet specify which particle species interact or what carries the interaction between them. In the [QED recap](qed.md#recap-of-the-lagrangians), the current is written as $j^\mu=q\bar\psi\gamma^\mu\psi$. Here we call the electron field $e$ instead of $\psi$ and keep the charge factor separate: $\bar e\gamma^\mu e$ contains the electron field on both sides, so the photon couples an electron to an electron. For the weak interaction, put different species on the two sides and retain their left-chiral parts:

$$j_\ell^\mu=\bar e_L\gamma^\mu\nu_{eL}
=\bar e\gamma^\mu P_L\nu_e
=\frac12\bar e\gamma^\mu(1-\gamma^5)\nu_e.$$

This expression combines two choices. The fields $e$ and $\nu_e$ specify which species participate; $P_L$ specifies which chiral parts participate. Its conjugate current is $\bar\nu_{eL}\gamma^\mu e_L$. For the quark transition, the corresponding current is $j_q^\mu=\bar u_L\gamma^\mu d_L$.

The lepton current has a term that creates an electron and an antineutrino: $\bar e_L$ can create the electron, and $\nu_{eL}$ can create the antineutrino. This uses the particle-creation and antiparticle-creation content of Dirac fields from Field Quantization. It explains how a neutrino *field* supplies the outgoing *antineutrino*. The quark current similarly has a term that destroys a down quark and creates an up quark.

<details>
<summary>Checking the chiral currents and comparing with QED</summary>

To form currents, first move a projector through a gamma matrix:

$$P_L\gamma^\mu=\frac{1-\gamma^5}{2}\gamma^\mu
=\gamma^\mu\frac{1+\gamma^5}{2}=\gamma^\mu P_R.$$

Interchanging $L$ and $R$ gives $P_R\gamma^\mu=\gamma^\mu P_L$. Since $P_L^\dagger=P_L$, taking the Dirac adjoint gives

$$\bar\psi_L\equiv\overline{P_L\psi}
=(P_L\psi)^\dagger\gamma^0
=\psi^\dagger P_L\gamma^0
=\psi^\dagger\gamma^0P_R=\bar\psi P_R.$$

Consequently, the mixed current vanishes:

$$\bar\psi_L\gamma^\mu\psi_R
=\bar\psi P_R\gamma^\mu P_R\psi
=\bar\psi\gamma^\mu P_LP_R\psi=0.$$

The other mixed current vanishes in the same way. Expanding $\psi=\psi_L+\psi_R$ therefore leaves the two electromagnetic contributions with equal coupling:

$$\bar\psi\gamma^\mu\psi
=\bar\psi_L\gamma^\mu\psi_L+\bar\psi_R\gamma^\mu\psi_R.$$

The charged weak interaction instead couples the left-handed fermion fields. For electrons and electron neutrinos, the relevant current is

$$\begin{aligned}
\bar\nu_{eL}\gamma^\mu e_L
&=\bar\nu_e P_R\gamma^\mu P_L e
=\bar\nu_e\gamma^\mu P_L^2e\\
&=\bar\nu_e\gamma^\mu P_L e
=\frac12\bar\nu_e\gamma^\mu(1-\gamma^5)e.
\end{aligned}$$

</details>

Parity exchanges left and right chirality. Because the charged weak interaction has no corresponding right-handed current, it does not preserve parity. A left-handed neutrino field also creates right-helicity antineutrinos in the massless limit, so this coupling includes the antineutrino in beta decay.

The chiral choice comes from experiment. Extending gauge symmetry alone does not determine which chiral fields participate.

## Connecting the two currents

We now have expressions for the two parts of beta decay: a down quark becomes an up quark, and an electron–antineutrino pair appears. To describe the whole decay, we need an interaction that connects those currents.

We can multiply them directly:

$$\mathcal L_{\mathrm{interaction}}\propto
(\bar u_L\gamma^\mu d_L)(\bar e_L\gamma_\mu\nu_{eL})
+\text{Hermitian conjugate}.$$

The coefficient sets the interaction strength; the conjugate term includes the reverse transitions. This is a **four-fermion interaction** because it contains four fermion fields. It treats the two parts of the decay as a single interaction at one spacetime point. With a strength determined from measurements, this gives Fermi's low-energy description of beta decay. We have introduced no new force carrier at this step.

To go beyond this direct description, we now hypothesize that **a force-carrying field connects the two currents**, much as the photon connects currents in QED. One current couples to the carrier at one vertex, and the other current couples to it at another. An exchanged particle joins the vertices. We will denote this proposed weak force carrier by $W$; its field content, couplings, and mass will be derived below.

The four-fermion vertex is not wrong or merely a diagrammatic shortcut: it is the appropriate low-energy description. The $W$-exchange picture is a hypothesis about the more fundamental, shorter-distance interaction. At energies much smaller than $m_W$, the internal $W$ propagator is approximately constant, so its two vertices reduce to the same effective four-fermion interaction.

Charge conservation tells us which charge it must carry in beta decay. The quark changes from charge $-e/3$ to $+2e/3$, so the exchanged carrier takes charge $-e$: it is a $W^-$. At the other vertex, that charge goes into the electron, while the antineutrino is neutral.

If the carrier is very massive compared with the energies involved, the exchange reduces approximately to the direct four-fermion interaction above. We will check this later by calculating its low-energy limit. This gives us a way to recover the successful decay description while proposing a mechanism behind it.

We could stop here and write a model with a charged $W$ field and its couplings to the two currents. That field describes both $W^-$ and its antiparticle $W^+$. For low-energy beta decay, this is enough to describe the exchange. To describe higher-energy processes too, we need to examine the limits of this model.

We want the theory to work when there is enough energy to produce the carriers themselves. A massive spin-1 particle has an additional polarization, called longitudinal, that the photon does not have. In a model with only the massive $W$ and the fermion couplings written above, some calculated scattering amplitudes involving this polarization grow too rapidly with energy. Eventually, the lowest-order calculations exceed the bounds required for consistent probabilities. This signals a breakdown of the approximation: we need additional physics or a different treatment at those energies.

<details>
<summary>Why a massive vector has a longitudinal polarization</summary>

The distinction comes from the polarization constraints. For a massive vector,

$$k^2=m^2,qquad k\cdot\varepsilon=0.$$

In the particle's rest frame, $k^\mu=(m,0,0,0)$, so the second condition sets $\varepsilon^0=0$ but leaves three independent spatial directions. These are the two transverse polarizations and one longitudinal polarization. For motion along the $z$-axis, a convenient longitudinal choice is

$$\varepsilon_L^\mu=\left(\frac{|\mathbf k|}{m},0,0,\frac{E}{m}\right),$$

which still satisfies $k\cdot\varepsilon_L=0$.

For comparison, the [earlier massless photon treatment](qed.md#counting-a-free-photons-polarizations) has $k^2=0$ and also imposes $k\cdot\varepsilon=0$. The massless gauge redundancy $\varepsilon^\mu\sim\varepsilon^\mu+\alpha k^\mu$ removes the remaining non-transverse direction, leaving only two physical polarizations. A massive $W$ has no such removable longitudinal mode, so its third polarization is physical.

</details>

**This is a theoretical consistency check, not a report that the model failed a beta-decay experiment.** We find the limitation by calculating consequences of the proposed model. Experiments have a separate role: they determine which extension describes nature. The high-energy argument alone does not uniquely select SU(2).

In the full electroweak theory, the additional gauge interactions and Higgs contributions cancel the troublesome growth in the relevant amplitudes. SU(2) is part of that construction; it does not solve the whole problem by itself. We will introduce the neutral electroweak sector and the Higgs mechanism in the next chapters. For the scattering argument, see this [CERN lecture on longitudinal vector-boson scattering](https://indico.cern.ch/event/520953/attachments/1311404/1962512/GHM_Lecture_1.pdf).

We therefore look for a common rule relating the couplings, rather than choosing every interaction strength independently. QED offers a precedent: a local symmetry supplies both a force-carrying field and its coupling. To try that approach here, we first look for a symmetry of the paired fermion fields.

## Finding a global symmetry of the pair

The motivation follows the same observation as in [QED's global phase symmetry](qed.md#u-1-global-symmetry). For a complex quantity $x$, changing its phase preserves its squared magnitude:

$$x\to e^{i\alpha}x,\qquad
x^*x\to x^*e^{-i\alpha}e^{i\alpha}x=x^*x.$$

For two complex quantities, we can preserve their combined squared magnitude while mixing them. Write $X=(x,y)^T$ and let $U$ be a **unitary** two-by-two matrix, meaning $U^\dagger U=1$. Then

$$X\to UX,\qquad
X^\dagger X=|x|^2+|y|^2
\to X^\dagger U^\dagger UX=X^\dagger X.$$

The individual entries can change, but their combined squared magnitude stays the same. All such matrices form the group U(2); the subset with determinant one forms SU(2). We will use this subset to organize the weak interaction.

To apply this observation to the fermion fields, temporarily leave out masses and interactions. The left-chiral electron and neutrino then have exactly the same free kinetic form. A constant unitary matrix can mix them without changing their combined free Lagrangian: the matrix passes through the derivative and cancels against its adjoint, just as the constant phase does in QED. The two-number example above illustrates the cancellation; the fields also carry spinor components, on which this mixing matrix does not act.

This gives us a symmetry to investigate before adding any new gauge fields. It is promising because it mixes the same species that the weak interaction connects. We then try the next step used in QED: allow the transformation to vary from point to point, and find which additional fields and couplings make that possible.

A **gauge symmetry** is a freedom to change the mathematical description without changing physical predictions. Making that freedom **local** means allowing a different change at each point in spacetime. Choosing to make SU(2) local, and choosing the left-chiral pairs it acts on, are inputs to the model. The free symmetry motivates this choice but does not prove that nature uses it. Once we make the choice, local symmetry fixes the pattern of gauge couplings, whose consequences we can test experimentally.

To let a matrix act on the two species together, arrange their left-handed components into a **doublet**, a column with two entries:

$$L=\begin{pmatrix}\nu_{eL}\\e_L\end{pmatrix}.$$

This grouping introduces no new particle. $L$ names the pair of fields; $\mathcal L$ names the Lagrangian. Each entry in $L$ is a left-chiral spinor with two independent complex components, so the pair has four independent complex components at each point. In our Dirac notation each spinor occupies four slots, but the projection leaves only two independent. The two-by-two mixing matrix acts on the species entries, while gamma matrices act on their spinor components.

<details>
<summary>The matrices that mix the doublet and preserve its free kinetic term</summary>

An $SU(2)$ transformation acts on this doublet as

$$L\to UL,\qquad U=\exp(i\alpha^aT^a),\qquad T^a=\frac{\sigma^a}{2}.$$

The $\sigma^a$ are the three Pauli matrices, now acting on the doublet rather than spatial spin. An $SU(2)$ matrix is a unitary two-by-two matrix with determinant one. Its three **generators** $T^a$ specify the infinitesimal transformations. For example, using $T^1=\tfrac12\begin{pmatrix}0&1\\1&0\end{pmatrix}$ and a small angle $\alpha$ gives

$$U\simeq1+i\alpha T^1,\qquad
\begin{pmatrix}\nu_{eL}\\e_L\end{pmatrix}
\longrightarrow
\begin{pmatrix}\nu_{eL}+\tfrac{i\alpha}{2}e_L\\e_L+\tfrac{i\alpha}{2}\nu_{eL}\end{pmatrix}.$$

Unlike a common phase, this transformation mixes the two field entries. We call it an **internal** transformation because it acts on species components at a fixed spacetime point, without rotating or moving that point. The corresponding generators are called **weak isospin** generators; they do not describe spatial spin.

We use three different kinds of indices. Gamma matrices act on spinor components, the two-by-two matrices $T^a$ act on doublet components, and $a=1,2,3$ labels which generator we use. Repeated $a,b,c$ indices are summed with the internal Euclidean metric $\delta^{ab}$, so we often write both upstairs. The spacetime indices $\mu,\nu$ still use the Minkowski metric and the upper/lower convention from Special Relativity.

For a constant $U$, the massless kinetic term

$$\mathcal L_0=i\bar L\gamma^\mu\partial_\mu L$$

is unchanged: $U$ passes through the derivative and cancels against $U^\dagger$. This is global $SU(2)$ symmetry of the massless kinetic term. Both entries have the same kinetic form, so mixing them preserves their sum.

</details>

The two massless fields have the same free kinetic form, so these matrices can mix them without changing their total free Lagrangian. This supplies the global symmetry, meaning the same change of description everywhere.

The electron and neutrino do have different physical masses and electric charges. We are constructing one sector of the theory, not asserting that the two observed particles are interchangeable. The full electroweak theory also contains a $U(1)$ factor; after Higgs symmetry breaking, a particular combination of generators defines electric charge. The Higgs couplings account for the electron mass. We develop those steps in the next chapters.

## Making the symmetry local introduces three fields

So far, the same mixing matrix acts everywhere, and we have introduced no new force fields. We now require the Lagrangian to remain invariant when the matrix varies across spacetime, $U=U(x)$. A derivative then acts on both the field and the changing matrix:

$$\partial_\mu(UL)=U\partial_\mu L+(\partial_\mu U)L.$$

The extra term spoils the invariance. As in QED, we introduce compensating fields and include them in a modified derivative, called the **covariant derivative**, so that changes in our description do not alter the physics.

Conceptually, this is similar to working in a rotating or otherwise non-inertial frame. When the frame changes from place to place, differentiating a quantity produces extra terms, and a connection term keeps track of how to compare descriptions at neighboring points. In mechanics those terms appear as inertial forces; here the compensating connection is the gauge field. The analogy concerns the method of introducing a connection, not the underlying physics: the gauge field can have a physical field strength and propagating particles.

The number of fields comes from the symmetry. SU(2) has three **generators**, three independent matrix directions for infinitesimal transformations. Each needs its own compensating field:

| Symmetry | Independent generators | Gauge fields |
| --- | --- | --- |
| U(1), used in QED | One | $A_\mu$ |
| SU(2), used here | Three | $W_\mu^1,W_\mu^2,W_\mu^3$ |

Each gauge field has four spacetime components indexed by $\mu$. The superscripts $1,2,3$ distinguish fields; they are not powers or spatial directions. Writing the added term explicitly makes the origin of all three fields visible:

$$D_\mu=\partial_\mu+ig\left(W_\mu^1T^1+W_\mu^2T^2+W_\mu^3T^3\right).$$

Here $T^1,T^2,T^3$ are the generator matrices and $g$ sets the coupling strength. We have not added $W^3$ separately to fix a decay diagram: it enters with the other two because we chose local SU(2).

<details>
<summary>Expanding the matrix-valued four-vector</summary>

The notation $W_\mu$ combines two kinds of information. The index $\mu$ tells us which spacetime component we are using, while the matrix structure acts on the two entries of the weak doublet. For each fixed $\mu$,

$$
W_\mu=W_\mu^aT^a
=\frac12
\begin{pmatrix}
W_\mu^3 & W_\mu^1-iW_\mu^2\\
W_\mu^1+iW_\mu^2 & -W_\mu^3
\end{pmatrix}.
$$

Thus $W_\mu$ means four separate $2\times2$ matrices:

$$
W_0,\qquad W_1,\qquad W_2,\qquad W_3.
$$

They act on the doublet

$$
L=\begin{pmatrix}\nu_{eL}\\ e_L\end{pmatrix}
$$

one spacetime component at a time. For example,

$$
D_\mu L
=\begin{pmatrix}
\partial_\mu\nu_{eL}\\
\partial_\mu e_L
\end{pmatrix}
+\frac{ig}{2}
\begin{pmatrix}
W_\mu^3\nu_{eL}+(W_\mu^1-iW_\mu^2)e_L\\
(W_\mu^1+iW_\mu^2)\nu_{eL}-W_\mu^3e_L
\end{pmatrix}.
$$

The fields $\nu_{eL}$ and $e_L$ are still spinors; the displayed matrix multiplication concerns only which weak species are mixed.

</details>

A gauge transformation changes the fermion and gauge fields together as an equivalent description. Actual particle transitions follow from the interaction terms we obtain next, and conserve energy, momentum, and electric charge.

<details>
<summary>How the derivative introduces the gauge fields</summary>

For a local transformation, $U=U(x)$, differentiation gives an extra term:

$$\partial_\mu(UL)=U\partial_\mu L+(\partial_\mu U)L.$$

As in QED, replace the ordinary derivative by a covariant derivative. Using the same plus-sign convention as the QED chapter, define

$$D_\mu=\partial_\mu+igW_\mu,\qquad W_\mu=W_\mu^aT^a.$$

Here $g$ is the weak gauge coupling. We introduce three gauge fields $W_\mu^1,W_\mu^2,W_\mu^3$, one for each generator. The new fields compensate for the extra derivative term, just as $A_\mu$ does in QED.

<details>
<summary>Deriving the gauge-field transformation</summary>

To find their transformation, expand both sides of $D'_\mu L'=U D_\mu L$:

$$\begin{aligned}
D'_\mu(UL)&=(\partial_\mu U)L+U\partial_\mu L+igW'_\mu UL,\\
UD_\mu L&=U\partial_\mu L+igUW_\mu L.
\end{aligned}$$

Cancel $U\partial_\mu L$. Equality for every doublet $L$ requires

$$\partial_\mu U+igW'_\mu U=igUW_\mu.$$

Multiply on the right by $U^{-1}$, then divide by $ig$. Since $-1/i=i$, this gives

$$W'_\mu=UW_\mu U^{-1}+\frac{i}{g}(\partial_\mu U)U^{-1}.$$

</details>

Substitution into the kinetic term produces the interaction:

$$i\bar L\gamma^\mu D_\mu L
=i\bar L\gamma^\mu\partial_\mu L
-g\bar L\gamma^\mu T^aL\,W_\mu^a.$$

</details>

The result is a coupling between the new fields and the fermion currents. Its strength is set by a parameter $g$. We have chosen the symmetry and which fermion parts it acts on; the derivative construction then supplies the interaction terms.

This symmetry acts on left-handed doublets, hence the name $SU(2)_L$. Right-handed charged fermions are **singlets** under this group: $SU(2)_L$ leaves them unchanged, so they have no coupling to these gauge fields. Their electromagnetic interactions remain present in the full electroweak theory.

## Reading the interaction as W exchange

We now put the modified derivative into the fermion Lagrangian and expand the matrices. This produces new interaction terms. To read each term physically, look at which fields appear together: they specify the particles that can meet at a vertex. The coefficient sets the coupling strength, and the gamma matrices and projectors specify its spin and chirality dependence.

The terms containing $W^1$ and $W^2$ connect the two species. We rewrite those two fields as the charged combinations

$$W_\mu^\pm=\frac{W_\mu^1\mp iW_\mu^2}{\sqrt2}.$$

These combinations describe $W^+$ and $W^-$. The third field, $W^3$, remains and couples without changing species. We still have the same three gauge fields, written in a form that makes their interactions easier to identify. In the full electroweak theory the charged bosons have charges $\pm e$, consistent with the transitions below.

<details>
<summary>Expanding the two-by-two matrix to find the charged couplings</summary>

To identify the interactions that change a neutrino into an electron, write the gauge-field matrix explicitly:

$$W_\mu^aT^a=\frac12
\begin{pmatrix}
W_\mu^3&W_\mu^1-iW_\mu^2\\
W_\mu^1+iW_\mu^2&-W_\mu^3
\end{pmatrix}.$$

The off-diagonal entries couple the two members of the doublet. They are $W_\mu^+/\sqrt2$ and $W_\mu^-/\sqrt2$, using these charged combinations. First multiply the matrix by $L$:

$$W_\mu L=
\begin{pmatrix}
\tfrac12W_\mu^3\nu_{eL}+\tfrac{1}{\sqrt2}W_\mu^+e_L\\
\tfrac{1}{\sqrt2}W_\mu^-\nu_{eL}-\tfrac12W_\mu^3e_L
\end{pmatrix}.$$

Now multiply by $-g\bar L\gamma^\mu$. The gamma matrix acts on each spinor entry, while $\bar L=(\bar\nu_{eL},\bar e_L)$ contracts the doublet index:

$$\begin{aligned}
-g\bar L\gamma^\mu W_\mu L
={}&-\frac{g}{\sqrt2}\left(
\bar\nu_{eL}\gamma^\mu e_LW_\mu^+
+\bar e_L\gamma^\mu\nu_{eL}W_\mu^-\right)\\
&-\frac g2\left(
\bar\nu_{eL}\gamma^\mu\nu_{eL}
-\bar e_L\gamma^\mu e_L\right)W_\mu^3.
\end{aligned}$$

The second line is the neutral $SU(2)_L$ contribution, which will combine with the $U(1)$ contribution in Electroweak Unification.

</details>

The expansion gives two terms that exchange the species, plus neutral terms that keep each species unchanged. Keeping the charged terms gives

$$\boxed{\mathcal L_{\mathrm{CC}}=-\frac{g}{\sqrt2}
\left(\bar\nu_{eL}\gamma^\mu e_LW_\mu^+
+\bar e_L\gamma^\mu\nu_{eL}W_\mu^-\right).}$$

For example, $\bar\nu_{eL}\gamma^\mu e_LW_\mu^+$ contains two different species and a charged field: it connects the electron and neutrino through a $W$ interaction. A neutral term such as $\bar e_L\gamma^\mu e_LW_\mu^3$ contains the electron on both sides, so it leaves the species unchanged. The matrix expansion tells us which of these couplings appear and fixes their relative coefficients.

The subscript CC means **charged current**: the current connects fermions whose electric charges differ by one unit. The factor $1/\sqrt2$ follows from the generator normalization and the definition of $W^\pm$. In the conventions used here, the $W^+\bar\nu_e e$ vertex has factor $-ig\gamma^\mu P_L/\sqrt2$.

<details>
<summary>Other particle generations</summary>

The same pattern occurs in three **generations**, repeated sets of fermions with the same gauge-charge pattern but different masses:

| Generation | Quarks | Charged lepton | Neutrino flavour |
| --- | --- | --- | --- |
| First | up $u$, down $d$ | electron $e$ | $\nu_e$ |
| Second | charm $c$, strange $s$ | muon $\mu$ | $\nu_\mu$ |
| Third | top $t$, bottom $b$ | tau $\tau$ | $\nu_\tau$ |

</details>

For beta decay, we need to connect the down-to-up transition to the electron–antineutrino pair. The quarks form a second doublet, and couple to the same charged boson fields as the leptons. An exchanged $W$ can therefore join the two interactions.

<details>
<summary>The quark coupling and the particle created by a charged field</summary>

Quarks have the same kind of charged weak coupling as leptons. Ignoring mixing between generations, arrange their left-handed fields into a doublet $Q_L=(u_L,d_L)^T$, just as we did for the neutrino and electron. In the full theory, a charged weak interaction can also connect quarks from different rows of the table. Including mixing gives the beta-decay term

$$\mathcal L_{\mathrm{CC}}^{ud}
=-\frac{g}{\sqrt2}V_{ud}\bar u_L\gamma^\mu d_LW_\mu^+
+\text{Hermitian conjugate}.$$

The Hermitian conjugate contains $V_{ud}^*\bar d_L\gamma^\mu u_LW_\mu^-$. The coefficient $V_{ud}$ is an entry of the **Cabibbo–Kobayashi–Maskawa (CKM) matrix**, which describes how charged weak interactions mix quark species. We keep just the up–down transition here.

The $W^+$ field annihilates a $W^+$ boson or creates its antiparticle, a $W^-$. Thus the displayed $\bar u_L\gamma^\mu d_LW_\mu^+$ term annihilates a down quark and creates an up quark while emitting a $W^-$. The field label and the emitted particle charge need not match.

</details>

Charge conservation helps us read the result. Changing a down quark of charge $-e/3$ into an up quark of charge $+2e/3$ leaves charge $-e$ for the exchanged boson. That is the $W^-$. At the other end, the electron and antineutrino together have this same charge. The two vertices combine into the beta-decay process:

$$d\longrightarrow u+W^{-*},\qquad W^{-*}\longrightarrow e^-+\bar\nu_e.$$

The asterisk marks a virtual $W$: an internal line in the amplitude, not an independently produced particle. Beta decay does not have enough energy to produce a real $W$. Energy and momentum still balance at each vertex; the internal momentum need not obey the real-particle condition $q^2=m_W^2$.

```feynman
\begin{tikzpicture}
\begin{feynman}
\vertex (d) at (-2,1.2) {$d$};
\vertex (a) at (0,1.2);
\vertex (u) at (3,2.4) {$u$};
\vertex (b) at (1,-0.5);
\vertex (e) at (3,0.2) {$e^-$};
\vertex (n) at (3,-1.5) {$\bar\nu_e$};
\diagram* {
(d) -- [fermion] (a) -- [fermion] (u),
(a) -- [boson, edge label={$W^-$}] (b),
(b) -- [fermion] (e),
(n) -- [fermion] (b),
};
\end{feynman}
\end{tikzpicture}
```

*Beta decay at the quark level, with the incoming down quark on the left and the three outgoing particles on the right. The antineutrino arrow points toward the vertex because arrows track fermion flow, not the direction of motion. The other two valence quarks of the neutron do not participate in this weak vertex and are omitted.*

The two vertices now account for the opening particle requirements: one changes $d$ to $u$, and the other creates $e^-+\bar\nu_e$, giving a three-particle final state that can share energy continuously. Both vertices contain $P_L$, so they also implement the measured chiral preference. To predict an energy spectrum, angular asymmetry, or lifetime, we still need to turn these vertices into an amplitude and integrate over the allowed final states. For a neutron, we also need the current between the composite nucleon states.

## Yang–Mills Fields and Self-Interactions

The fermion interaction terms tell us where a $W$ can couple, but an exchange calculation also needs a rule for how the field propagates between the vertices. We add gauge-field kinetic terms for that purpose, just as we added the Maxwell term for the photon. Requiring local SU(2) invariance also gives interactions among the gauge fields themselves. This type of gauge theory is called a **Yang–Mills theory**. Those self-interactions do not enter the leading beta-decay diagram; the [optional Yang–Mills page](yang-mills.md) develops their derivation.

## Connecting W exchange to the decay strength

The decay rate depends on the two vertex couplings and on propagation between them. This is why the $W$ mass matters: at beta-decay energies, exchanging such a heavy boson strongly suppresses the amplitude.

We now use the physical $W$ mass $m_W$ as an input; the Higgs chapter explains its origin. At momentum transfers with $|q^2|\ll m_W^2$, the propagator denominator becomes

$$\frac{1}{q^2-m_W^2}\simeq-\frac{1}{m_W^2}.$$

The **propagator**, the factor representing the internal boson line in an amplitude, is therefore approximately proportional to $1/m_W^2$. Each end of the line contributes a coupling proportional to $g$, so the whole exchange has strength proportional to $g^2/m_W^2$. At these energies, we can replace the two vertices and their connecting line by one interaction involving all four fermion fields. The measured coefficient of this effective interaction is conventionally expressed using the **Fermi constant** $G_F$.

At leading order, the relation is

$$\frac{G_F}{\sqrt2}=\frac{g^2}{8m_W^2}.$$

This connects the strength of the direct interaction we started with to the coupling and mass of the proposed carrier. A larger $W$ mass makes the low-energy interaction weaker. The numerical factors follow from how we normalized the currents; the calculation below checks them.

<details>
<summary>Calculating the coefficient and its normalization</summary>

**Given without proof:** the massive-vector propagator below. Its derivation requires a longer treatment of the massive gauge field and its constraints. Here we use the result and work out its low-energy limit. In **unitary gauge**, a choice in which the physical massive vector field appears explicitly, it is

$$D_{\mu\nu}(q)=\frac{-i}{q^2-m_W^2+i\epsilon}
\left(g_{\mu\nu}-\frac{q_\mu q_\nu}{m_W^2}\right).$$

Compared with the photon propagator, this has a massive denominator and an additional momentum-dependent numerator. At energies and momentum transfers small compared with $m_W$, the second numerator term is suppressed, and the denominator has the expansion above. Thus $D_{\mu\nu}(q)\simeq ig_{\mu\nu}/m_W^2$. We can use this limit without deriving massive-vector quantization. Define the external-state currents

$$J_q^\mu=\bar u_u\gamma^\mu P_Lu_d,\qquad
J_\ell^\nu=\bar u_e\gamma^\nu P_Lv_{\bar\nu_e}.$$

Here $u_f$ denotes a particle spinor of species $f$, and $v_{\bar\nu_e}$ is the outgoing antineutrino spinor. Multiplying the two vertex factors and the propagator gives

$$i\mathcal M\simeq
\left(-\frac{igV_{ud}}{\sqrt2}\right)J_q^\mu
\frac{ig_{\mu\nu}}{m_W^2}
\left(-\frac{ig}{\sqrt2}\right)J_\ell^\nu
=-\frac{ig^2V_{ud}}{2m_W^2}J_q^\mu J_{\ell\mu}.$$

The metric contracts the two current indices. With no momentum dependence left in the propagator at this order, a local four-fermion interaction gives the same amplitude. Replacing each $P_L$ by $(1-\gamma^5)/2$ supplies another factor of $1/4$, so its coefficient is $g^2/(8m_W^2)$. For beta decay at the quark level, write this as

$$\mathcal L_{\mathrm{eff}}
=-\frac{G_FV_{ud}}{\sqrt2}
\big[\bar u\gamma^\mu(1-\gamma^5)d\big]
\big[\bar e\gamma_\mu(1-\gamma^5)\nu_e\big]
+\text{Hermitian conjugate},$$

This is the tree-level relation quoted above; loop corrections refine it.

The **Fermi constant** $G_F$ measures the strength of this low-energy interaction. The two factors of $1/2$ in the chiral projectors account for the normalization when we write the currents with $1-\gamma^5$. This approximation connects massive-boson exchange to Fermi's four-fermion description; see [Tong, *Electroweak Interactions*, §5.3.4](https://davidtong.org/pdfs/teaching/standard-model/standardmodel5.pdf).

</details>

```feynman
\begin{tikzpicture}
\begin{feynman}
\vertex (d) at (-2,0) {$d$};
\vertex [dot] (a) at (0,0) {};
\vertex (u) at (2,1.5) {$u$};
\vertex (e) at (2,0) {$e^-$};
\vertex (n) at (2,-1.5) {$\bar\nu_e$};
\diagram* {
(d) -- [fermion] (a) -- [fermion] (u),
(a) -- [fermion] (e),
(n) -- [fermion] (a),
};
\end{feynman}
\end{tikzpicture}
```

*The same external particles in the Fermi approximation. The filled dot represents the effective four-fermion interaction obtained by replacing the short-distance $W$ exchange. It is valid for $|q^2|\ll m_W^2$.*

The large $W$ mass suppresses low-energy amplitudes through $1/m_W^2$. The weak gauge coupling itself is not exceptionally small. To calculate neutron decay, we must also evaluate the quark current between neutron and proton states; their internal strong-interaction structure affects the result.

We have recovered the direct low-energy interaction from an exchange theory, while retaining the particle content and chiral preference that motivated it. Computing the neutron lifetime or the detailed spectrum still requires the nucleon structure and final-state phase space; we have not calculated those observables here.

The same charged-current coupling produces muon decay, $\mu^-\to\nu_\mu+e^-+\bar\nu_e$, with a muon–neutrino current in place of the quark current. Weak interactions also include neutral-current processes mediated by the $Z$. The next chapter develops the neutral sector and its relation to electromagnetism; the [Higgs chapter](higgs-mechanism.md) explains the origin of the gauge-boson masses used here.

[^mirror]: The “mirror experiment” is a transformed comparison, not necessarily a second apparatus physically reflected in a laboratory. The experiment measures the parity-sensitive correlation $\mathbf S\cdot\mathbf p_e$: parity changes its sign, so parity conservation would require equal rates for emission along and opposite to the nuclear spin. Wu’s 1957 cobalt-60 experiment observed the asymmetry. The 1958 Goldhaber experiment measured the helicity of neutrinos produced in electron capture, and later beta-decay, muon-decay, and neutrino-scattering experiments reinforced the left-chiral structure of the charged weak interaction. Electrons with either spin or helicity can still be observed through other interactions; the asymmetry concerns how the weak interaction couples to the corresponding chiral components.

[^valence]: A neutron has **valence-quark content** $udd$ and a proton $uud$: the net quark numbers after subtracting antiquarks of each species. The full bound state also contains gluons and quark–antiquark contributions, which belong to the discussion of [Quantum Chromodynamics](qcd.md).
