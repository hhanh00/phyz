# Weak Interaction

In [QED](qed.md), the photon couples to a current built from one charged fermion field. Weak interactions also connect different fermion species: a neutron can decay into a proton, an electron, and an antineutrino. We develop the charged weak interaction here, including its chiral coupling and its Yang–Mills gauge fields. We use natural units, $\hbar=c=1$.

## Beta Decay and Neutrinos

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

At the quark level, a neutron has **valence-quark content** $udd$ and a proton has $uud$. Valence content specifies the net quark numbers after subtracting antiquarks of each species; the full bound state also contains gluons and quark–antiquark contributions. The decay changes a down quark into an up quark:

$$d\longrightarrow u+e^-+\bar\nu_e.$$

The charges again balance, since $-\tfrac13=\tfrac23-1$. Photon exchange cannot produce this change of quark species. We need an interaction that couples an up-quark field to a down-quark field, and a neutrino field to an electron field.

## From Dirac to Weak Interaction

There is also a difference in spin dependence. **Parity** reverses spatial coordinates, $\mathbf x\to-\mathbf x$, and hence momentum, $\mathbf p\to-\mathbf p$. Orbital angular momentum stays unchanged because $(-\mathbf r)\times(-\mathbf p)=\mathbf r\times\mathbf p$. Intrinsic spin transforms in the same way as angular momentum under parity.

A **polarized** sample has a preferred spin orientation instead of randomly oriented nuclear spins. Experimenters can compare how often beta-decay electrons emerge along or against that orientation. Under parity,

$$\mathbf S\cdot\mathbf p_e\longrightarrow-\mathbf S\cdot\mathbf p_e.$$

Thus the reversed experiment exchanges emission along the spin with emission against it, while retaining the same spin orientation. If the interaction preserved parity, those two directions would have equal rates. Experiments find an asymmetry, so the weak interaction violates parity.

To express this distinction using Dirac fields, define

$$\gamma^5=i\gamma^0\gamma^1\gamma^2\gamma^3,\qquad
P_L=\frac{1-\gamma^5}{2},\qquad P_R=\frac{1+\gamma^5}{2}.$$

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

The matrices are therefore **projectors** onto the left- and right-handed **chiral components**:

$$\psi_L=P_L\psi,\qquad \psi_R=P_R\psi,\qquad
\psi=\psi_L+\psi_R.$$

Chirality labels these two parts of the spinor. It is different from spin up/down along a chosen axis. It is also different from the upper/lower pair used for the rest solutions in [The Dirac Equation](dirac-equation.md): in that standard basis, $\gamma^5$ mixes the upper and lower pairs. A change to a **chiral basis** makes $\gamma^5$ diagonal, so the left and right parts occupy separate pairs of entries. The projectors select the same physical chiral parts in either basis.

**Helicity** describes spin relative to the particle's own momentum: positive helicity means aligned, and negative helicity means opposed. For a massive particle, an observer who overtakes it can reverse its momentum without reversing its spin, changing the helicity label. Chirality instead labels the spinor's transformation under rotations and boosts. In the massless limit, a left-chiral field annihilates negative-helicity particles and creates positive-helicity antiparticles. For massive particles, a state of definite helicity generally contains both chiral components. We neglect neutrino masses in the processes discussed here.

**Given without proof:** the relation between chirality and particle/antiparticle helicity above. Proving it requires solving the Dirac equation in a helicity basis and identifying the particle and antiparticle modes, a longer calculation than the projector algebra here.

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

The factor $1-\gamma^5$ gives the name **vector minus axial vector**, or **V−A**: the current contains a vector term with $\gamma^\mu$ and an axial-vector term with $\gamma^\mu\gamma^5$.

Parity exchanges left and right chirality. Because the charged weak interaction has no corresponding right-handed current, it does not preserve parity. A left-handed neutrino field also creates right-helicity antineutrinos in the massless limit, so this coupling includes the antineutrino in beta decay.

The chiral choice comes from experiment. Extending gauge symmetry alone does not determine which chiral fields participate.

## Global and Local SU(2) Symmetry

To construct a coupling between the neutrino and electron fields, arrange their left-handed components into a **doublet**, a column with two entries:

$$L=\begin{pmatrix}\nu_{eL}\\e_L\end{pmatrix}.$$

Each entry is a spinor field. The doublet index distinguishes particle species; it is separate from the spinor index on which the gamma matrices act.

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

The electron and neutrino do have different physical masses and electric charges. We are constructing one sector of the theory, not asserting that the two observed particles are interchangeable. The full electroweak theory also contains a $U(1)$ factor; after Higgs symmetry breaking, a particular combination of generators defines electric charge. The Higgs couplings account for the electron mass. We develop those steps in the next chapters.

When we make this symmetry local, a gauge transformation changes the fermion and gauge fields together as an equivalent description. Applying that transformation is not an electron physically decaying into a neutrino. Actual transitions follow from the interaction terms and must conserve energy, momentum, and electric charge.

For a local transformation, $U=U(x)$, differentiation gives an extra term:

$$\partial_\mu(UL)=U\partial_\mu L+(\partial_\mu U)L.$$

As in QED, replace the ordinary derivative by a covariant derivative. Using the same plus-sign convention as the QED chapter, define

$$D_\mu=\partial_\mu+igW_\mu,\qquad W_\mu=W_\mu^aT^a.$$

Here $g$ is the weak gauge coupling. We introduce three gauge fields $W_\mu^1,W_\mu^2,W_\mu^3$, one for each generator. To find their transformation, expand both sides of $D'_\mu L'=U D_\mu L$:

$$\begin{aligned}
D'_\mu(UL)&=(\partial_\mu U)L+U\partial_\mu L+igW'_\mu UL,\\
UD_\mu L&=U\partial_\mu L+igUW_\mu L.
\end{aligned}$$

Cancel $U\partial_\mu L$. Equality for every doublet $L$ requires

$$\partial_\mu U+igW'_\mu U=igUW_\mu.$$

Multiply on the right by $U^{-1}$, then divide by $ig$. Since $-1/i=i$, this gives

$$W'_\mu=UW_\mu U^{-1}+\frac{i}{g}(\partial_\mu U)U^{-1}.$$

Substitution into the kinetic term produces the interaction:

$$i\bar L\gamma^\mu D_\mu L
=i\bar L\gamma^\mu\partial_\mu L
-g\bar L\gamma^\mu T^aL\,W_\mu^a.$$

This symmetry acts on left-handed doublets, hence the name $SU(2)_L$. Right-handed charged fermions are **singlets** under this group: $SU(2)_L$ leaves them unchanged, so they have no coupling to these gauge fields. Their electromagnetic interactions remain present in the full electroweak theory.

## Yang–Mills Fields and Self-Interactions

The gauge fields also need kinetic terms. In QED we used the electromagnetic field strength $F_{\mu\nu}$. For $SU(2)$, the commutator of covariant derivatives transforms as $[D'_\mu,D'_\nu]=U[D_\mu,D_\nu]U^{-1}$. We can therefore extract a field strength with the same transformation law and use it to construct an invariant kinetic term:

$$[D_\mu,D_\nu]=igW_{\mu\nu},$$

Apply the two derivatives to an arbitrary test doublet $f(x)$. The product rule is essential because $W_\nu$ also depends on position:

$$\begin{aligned}
D_\mu D_\nu f
={}&\partial_\mu\partial_\nu f
+ig(\partial_\mu W_\nu)f
+igW_\nu\partial_\mu f\\
&+igW_\mu\partial_\nu f-g^2W_\mu W_\nu f.
\end{aligned}$$

Exchange $\mu$ and $\nu$ and subtract. The second derivatives cancel, as do the terms with one derivative acting on $f$. What remains is

$$\begin{aligned}
[D_\mu,D_\nu]f
&=\left[ig(\partial_\mu W_\nu-\partial_\nu W_\mu)
-g^2(W_\mu W_\nu-W_\nu W_\mu)\right]f\\
&=ig\left[\partial_\mu W_\nu-\partial_\nu W_\mu
+ig[W_\mu,W_\nu]\right]f.
\end{aligned}$$

Comparing with the definition gives

$$W_{\mu\nu}=\partial_\mu W_\nu-\partial_\nu W_\mu+ig[W_\mu,W_\nu].$$

The last term differs from electromagnetism. The generators obey

$$[T^a,T^b]=i\epsilon^{abc}T^c,$$

where $\epsilon^{abc}$ is completely antisymmetric and $\epsilon^{123}=1$. Two transformations generally give different results when applied in the opposite order. We call such a group **non-Abelian**. A gauge theory built from this structure is a **Yang–Mills theory**.

To extract components, substitute $W_\mu=W_\mu^bT^b$ into the last term. The component fields commute as classical coefficients; the generator matrices do not:

$$\begin{aligned}
ig[W_\mu,W_\nu]
&=igW_\mu^bW_\nu^c[T^b,T^c]\\
&=igW_\mu^bW_\nu^c\,i\epsilon^{bca}T^a
=-g\epsilon^{abc}W_\mu^bW_\nu^cT^a.
\end{aligned}$$

We named the remaining generator index $a$ and used $\epsilon^{bca}=\epsilon^{abc}$: a cyclic permutation makes two exchanges and preserves the sign. The minus sign comes from $i^2=-1$. Comparing coefficients of $T^a$ in $W_{\mu\nu}=W_{\mu\nu}^aT^a$ gives

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

The off-diagonal entries couple the two members of the doublet. They are $W_\mu^+/\sqrt2$ and $W_\mu^-/\sqrt2$, using the charged combinations defined above. First multiply the matrix by $L$:

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

The second line is the neutral $SU(2)_L$ contribution, which will combine with the $U(1)$ contribution in Electroweak Unification. Keeping the charged terms here gives

$$\boxed{\mathcal L_{\mathrm{CC}}=-\frac{g}{\sqrt2}
\left(\bar\nu_{eL}\gamma^\mu e_LW_\mu^+
+\bar e_L\gamma^\mu\nu_{eL}W_\mu^-\right).}$$

The subscript CC means **charged current**: the current connects fermions whose electric charges differ by one unit. The factor $1/\sqrt2$ follows from the generator normalization and the definition of $W^\pm$. In the conventions used here, the $W^+\bar\nu_e e$ vertex has factor $-ig\gamma^\mu P_L/\sqrt2$.

The same pattern occurs in three **generations**, repeated sets of fermions with the same gauge-charge pattern but different masses:

| Generation | Quarks | Charged lepton | Neutrino flavour |
| --- | --- | --- | --- |
| First | up $u$, down $d$ | electron $e$ | $\nu_e$ |
| Second | charm $c$, strange $s$ | muon $\mu$ | $\nu_\mu$ |
| Third | top $t$, bottom $b$ | tau $\tau$ | $\nu_\tau$ |

Quarks have the same kind of charged weak coupling as leptons. Ignoring mixing between generations, arrange their left-handed fields into a doublet $Q_L=(u_L,d_L)^T$, just as we did for the neutrino and electron. In the full theory, a charged weak interaction can also connect quarks from different rows of the table. Including mixing gives the beta-decay term

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
