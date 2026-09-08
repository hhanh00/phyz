# Weak Interaction

In [QED](qed.md), the photon couples to a current built from one charged fermion field. Weak interactions also connect different fermion species: a neutron can decay into a proton, an electron, and an antineutrino. We develop the charged weak interaction here, including its chiral coupling and its Yang–Mills gauge fields. We use natural units, $\hbar=c=1$.

## Beta Decay and Neutrinos

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

If the final state contained only a proton and an electron, conservation of energy and momentum would fix the electron energy in the neutron rest frame. Instead, experiments show a continuous range of electron energies. A third particle can carry different amounts of energy and momentum in different decays. The neutrino hypothesis accounted for this missing energy; experiments later detected neutrinos directly.

Neutrinos have no electric charge, so they have no direct photon coupling of the kind used in QED. They participate in weak interactions, which makes them difficult to detect. The electron and antineutrino are created in the decay; they are not constituents stored inside the neutron.

At the quark level, a neutron has valence-quark content $udd$ and a proton has $uud$. The decay changes a down quark into an up quark:

$$d\longrightarrow u+e^-+\bar\nu_e.$$

The charges again balance, since $-\tfrac13=\tfrac23-1$. Photon exchange cannot produce this change of quark species. We need an interaction that couples an up-quark field to a down-quark field, and a neutrino field to an electron field.

## From Dirac to Weak Interaction

There is also a difference in spin dependence. **Parity** reverses spatial coordinates, $\mathbf x\to-\mathbf x$. Momentum reverses under parity, while angular momentum does not. In polarized beta-decay experiments, electrons emerge preferentially in one direction relative to the nuclear spin. The parity-reversed process would have the opposite preference. The weak interaction therefore violates parity.

To express this distinction using Dirac fields, define

$$\gamma^5=i\gamma^0\gamma^1\gamma^2\gamma^3,\qquad
P_L=\frac{1-\gamma^5}{2},\qquad P_R=\frac{1+\gamma^5}{2}.$$

Because $(\gamma^5)^2=1$, its eigenvalues are $-1$ and $+1$. The matrices $P_L$ and $P_R$ select these respective eigenspaces. They are **projectors**: applying either twice has the same effect as applying it once. They separate a field into its left- and right-handed **chiral components**:

$$\psi_L=P_L\psi,\qquad \psi_R=P_R\psi,\qquad
\psi=\psi_L+\psi_R.$$

Chirality labels these two spinor components. **Helicity** describes whether a particle's spin points along or against its momentum. In the massless limit, a left-chiral field annihilates negative-helicity particles and creates positive-helicity antiparticles. For massive particles, a state of definite helicity generally contains both chiral components. We neglect neutrino masses in the processes discussed here.

The identity $\{\gamma^5,\gamma^\mu\}=0$ means that $\gamma^5$ anticommutes with each gamma matrix, so $P_R\gamma^\mu=\gamma^\mu P_L$. Together with $\bar\psi_L=\bar\psi P_R$, this gives the current identities below. The electromagnetic current contains both components with equal coupling:

$$\bar\psi\gamma^\mu\psi
=\bar\psi_L\gamma^\mu\psi_L+\bar\psi_R\gamma^\mu\psi_R.$$

The charged weak interaction instead couples the left-handed fermion fields. For electrons and electron neutrinos, the relevant current is

$$\bar\nu_{eL}\gamma^\mu e_L
=\bar\nu_e\gamma^\mu P_L e
=\frac12\bar\nu_e\gamma^\mu(1-\gamma^5)e.$$

The factor $1-\gamma^5$ gives the name **vector minus axial vector**, or **V−A**: the current contains a vector term with $\gamma^\mu$ and an axial-vector term with $\gamma^\mu\gamma^5$.

Parity exchanges left and right chirality. Because the charged weak interaction has no corresponding right-handed current, it does not preserve parity. A left-handed neutrino field also creates right-helicity antineutrinos in the massless limit, so this coupling includes the antineutrino in beta decay.

The chiral choice comes from experiment. Extending gauge symmetry alone does not determine which chiral fields participate.

## Global and Local SU(2) Symmetry

To construct a coupling between the neutrino and electron fields, arrange their left-handed components into a **doublet**, a column with two entries:

$$L=\begin{pmatrix}\nu_{eL}\\e_L\end{pmatrix}.$$

Each entry is a spinor field. The doublet index distinguishes particle species; it is separate from the spinor index on which the gamma matrices act.

An $SU(2)$ transformation acts on this doublet as

$$L\to UL,\qquad U=\exp(i\alpha^aT^a),\qquad T^a=\frac{\sigma^a}{2}.$$

The $\sigma^a$ are the three Pauli matrices, now acting on the doublet rather than spatial spin. An $SU(2)$ matrix is a unitary two-by-two matrix with determinant one. Its three **generators** $T^a$ specify the infinitesimal transformations. Repeated indices $a=1,2,3$ are summed.

For a constant $U$, the massless kinetic term

$$\mathcal L_0=i\bar L\gamma^\mu\partial_\mu L$$

is unchanged: $U$ passes through the derivative and cancels against $U^\dagger$. This is global $SU(2)$ symmetry. We start with the kinetic term because the physical electron mass needs additional structure, developed in [Higgs Mechanism](higgs-mechanism.md).

For a local transformation, $U=U(x)$, differentiation gives an extra term:

$$\partial_\mu(UL)=U\partial_\mu L+(\partial_\mu U)L.$$

As in QED, replace the ordinary derivative by a covariant derivative. Using the same plus-sign convention as the QED chapter, define

$$D_\mu=\partial_\mu+igW_\mu,\qquad W_\mu=W_\mu^aT^a.$$

Here $g$ is the weak gauge coupling. We introduce three gauge fields $W_\mu^1,W_\mu^2,W_\mu^3$, one for each generator. Requiring $D'_\mu L'=U D_\mu L$ gives

$$W'_\mu=UW_\mu U^{-1}+\frac{i}{g}(\partial_\mu U)U^{-1}.$$

Substitution into the kinetic term produces the interaction:

$$i\bar L\gamma^\mu D_\mu L
=i\bar L\gamma^\mu\partial_\mu L
-g\bar L\gamma^\mu T^aL\,W_\mu^a.$$

This symmetry acts on left-handed doublets, hence the name $SU(2)_L$. Right-handed charged fermions are **singlets** under this group: $SU(2)_L$ leaves them unchanged, so they have no coupling to these gauge fields. Their electromagnetic interactions remain present in the full electroweak theory.

## Yang–Mills Fields and Self-Interactions

The gauge fields also need kinetic terms. In QED we used the electromagnetic field strength $F_{\mu\nu}$. For $SU(2)$, the commutator of covariant derivatives transforms as $[D'_\mu,D'_\nu]=U[D_\mu,D_\nu]U^{-1}$. We can therefore extract a field strength with the same transformation law and use it to construct an invariant kinetic term:

$$[D_\mu,D_\nu]=igW_{\mu\nu},$$

$$W_{\mu\nu}=\partial_\mu W_\nu-\partial_\nu W_\mu+ig[W_\mu,W_\nu].$$

The last term differs from electromagnetism. The generators obey

$$[T^a,T^b]=i\epsilon^{abc}T^c,$$

where $\epsilon^{abc}$ is completely antisymmetric and $\epsilon^{123}=1$. Two transformations generally give different results when applied in the opposite order. We call such a group **non-Abelian**. A gauge theory built from this structure is a **Yang–Mills theory**.

Writing $W_{\mu\nu}=W_{\mu\nu}^aT^a$ gives

$$\boxed{W_{\mu\nu}^a=\partial_\mu W_\nu^a-\partial_\nu W_\mu^a
-g\epsilon^{abc}W_\mu^bW_\nu^c.}$$

The minus sign follows from our convention $D_\mu=\partial_\mu+igW_\mu$. With $D_\mu=\partial_\mu-igW_\mu$, the corresponding component formula has a plus sign.

Under a gauge transformation, $W_{\mu\nu}\to UW_{\mu\nu}U^{-1}$. The trace of its square is therefore invariant. With $\operatorname{tr}(T^aT^b)=\delta^{ab}/2$, the gauge-field Lagrangian is

$$\mathcal L_{\mathrm{YM}}=-\frac12\operatorname{tr}(W_{\mu\nu}W^{\mu\nu})
=-\frac14W_{\mu\nu}^aW^{a\mu\nu}.$$

The field strength contains a derivative term linear in $W$ and a term quadratic in $W$. Squaring it produces three kinds of terms:

| Terms in the Lagrangian | Role in perturbation theory |
| --- | --- |
| Quadratic in $W$ | Free gauge-field propagation |
| Cubic in $W$, proportional to $g$ | Three-gauge-boson vertices |
| Quartic in $W$, proportional to $g^2$ | Four-gauge-boson vertices |

Thus the gauge bosons interact directly with one another. The Maxwell Lagrangian is quadratic in the photon field and has no such vertices. Photon scattering through charged-particle loops is a separate effect. For a more general derivation of the Yang–Mills kinetic term and these vertices, see [Tong, *Symmetries*, §1.3.3](https://davidtong.org/pdfs/teaching/standard-model/standardmodel1.pdf).

So far, these are the $SU(2)_L$ gauge fields. The neutral field $W^3$ is not yet the physical $Z$ boson. Its relation to the $Z$ and photon belongs to [Electroweak Unification](electroweak-unification.md).

For the diagrams, use the charged combinations

$$W_\mu^\pm=\frac{W_\mu^1\mp iW_\mu^2}{\sqrt2}.$$

They describe bosons with electric charges $\pm e$. The next section shows how these combinations enter the fermion interaction.

```feynman
\begin{tikzpicture}
\begin{feynman}
\vertex (a) at (0,0);
\vertex (p) at (-1.5,1.2) {$W^+$};
\vertex (m) at (-1.5,-1.2) {$W^-$};
\vertex (n) at (1.5,0) {$W^3$};
\vertex (b) at (5,0);
\vertex (p2) at (3.5,1.2) {$W^+$};
\vertex (m2) at (3.5,-1.2) {$W^-$};
\vertex (n2) at (6.5,1.2) {$W^3$};
\vertex (n3) at (6.5,-1.2) {$W^3$};
\diagram* {
(p) -- [boson] (a) -- [boson] (m),
(a) -- [boson] (n),
(p2) -- [boson] (b) -- [boson] (m2),
(n2) -- [boson] (b) -- [boson] (n3),
};
\end{feynman}
\end{tikzpicture}
```

*Examples of the three- and four-gauge-boson vertices, drawn with all legs outgoing. These represent interaction terms, not decays of an isolated on-shell boson. Wavy lines here denote weak gauge fields; they do not necessarily denote photons.*

## Charged Weak Interaction

To identify the interactions that change a neutrino into an electron, write the gauge-field matrix explicitly:

$$W_\mu^aT^a=\frac12
\begin{pmatrix}
W_\mu^3&W_\mu^1-iW_\mu^2\\
W_\mu^1+iW_\mu^2&-W_\mu^3
\end{pmatrix}.$$

The off-diagonal entries couple the two members of the doublet. They are $W_\mu^+/\sqrt2$ and $W_\mu^-/\sqrt2$, using the charged combinations defined above. Expanding the fermion interaction gives

$$\boxed{\mathcal L_{\mathrm{CC}}=-\frac{g}{\sqrt2}
\left(\bar\nu_{eL}\gamma^\mu e_LW_\mu^+
+\bar e_L\gamma^\mu\nu_{eL}W_\mu^-\right).}$$

The subscript CC means **charged current**: the current connects fermions whose electric charges differ by one unit. The factor $1/\sqrt2$ follows from the generator normalization and the definition of $W^\pm$. In the conventions used here, the $W^+\bar\nu_e e$ vertex has factor $-ig\gamma^\mu P_L/\sqrt2$.

Quarks have the same kind of coupling. Ignoring mixing between generations, arrange their left-handed fields into a doublet $Q_L=(u_L,d_L)^T$, just as we did for the neutrino and electron. Including mixing gives the beta-decay term

$$\mathcal L_{\mathrm{CC}}^{ud}
=-\frac{g}{\sqrt2}V_{ud}\bar u_L\gamma^\mu d_LW_\mu^+
+\text{Hermitian conjugate}.$$

The Hermitian conjugate contains $V_{ud}^*\bar d_L\gamma^\mu u_LW_\mu^-$. The coefficient $V_{ud}$ is an entry of the **Cabibbo–Kobayashi–Maskawa (CKM) matrix**, which describes how charged weak interactions mix quark species. We keep just the up–down transition here.

The $W^+$ field annihilates a $W^+$ boson or creates its antiparticle, a $W^-$. Thus the displayed $\bar u_L\gamma^\mu d_LW_\mu^+$ term annihilates a down quark and creates an up quark while emitting a $W^-$. The field label and the emitted particle charge need not match.

The two vertices combine into the beta-decay process:

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

### The low-energy limit

We now use the physical $W$ mass $m_W$ as an input; the Higgs chapter explains its origin. At momentum transfers with $|q^2|\ll m_W^2$, the propagator denominator becomes

$$\frac{1}{q^2-m_W^2}\simeq-\frac{1}{m_W^2}.$$

At leading order in external momenta divided by $m_W$, the massive-vector propagator reduces to $D_{\mu\nu}(q)\simeq ig_{\mu\nu}/m_W^2$. Define the external-state currents

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

$$\boxed{\frac{G_F}{\sqrt2}=\frac{g^2}{8m_W^2}}\qquad\text{at tree level}.$$

The **Fermi constant** $G_F$ measures the strength of this low-energy interaction. The two factors of $1/2$ in the chiral projectors account for the normalization when we write the currents with $1-\gamma^5$. This approximation connects massive-boson exchange to Fermi's four-fermion description; see [Tong, *Electroweak Interactions*, §5.3.4](https://davidtong.org/pdfs/teaching/standard-model/standardmodel5.pdf).

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

The same charged-current coupling produces muon decay, $\mu^-\to\nu_\mu+e^-+\bar\nu_e$, with a muon–neutrino current in place of the quark current. Weak interactions also include neutral-current processes mediated by the $Z$. The next chapter develops the neutral sector and its relation to electromagnetism; the [Higgs chapter](higgs-mechanism.md) explains the origin of the gauge-boson masses used here.
