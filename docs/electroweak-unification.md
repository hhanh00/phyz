# Electroweak Unification

In [Weak Interaction](weak-interaction.md), local $SU(2)_L$ symmetry introduced three gauge fields. Two charged combinations, $W^\pm$, connect the currents in beta decay. The neutral field $W^3$ remains. We now ask how this construction fits with the photon and the electromagnetic interactions we already know.

The physical requirements constrain the extension. The photon couples to both chiral parts of an electron with the same electric charge, while a neutrino has no direct photon coupling. The weak interaction also includes neutral processes in which a neutrino scatters without becoming a charged lepton. We will construct couplings that account for all three features.

The steps are:

1. **Compare the neutral weak coupling with electromagnetism.** Their different action on neutrinos and right-handed electrons rules out identifying $W^3$ with the photon.
2. **Introduce a second charge and gauge field.** Hypercharge supplies the additional coupling needed to reproduce electric charges.
3. **Combine the neutral fields.** One combination has the photon coupling; the other has the $Z$ coupling.
4. **Read the physical interactions.** The photon preserves the electromagnetic coupling, while the $Z$ permits neutral weak scattering.
5. **Identify the remaining mass problem.** The next chapter explains why the photon is massless while the $W$ and $Z$ are massive.

We use $\hbar=c=1$, metric $(+,-,-,-)$, and the plus-sign convention for the covariant derivative used in QED and WI. Throughout, $e>0$ denotes the elementary charge; an electron has charge $-e$.

## The neutral weak field cannot be the photon

The [matrix expansion in WI](weak-interaction.md#reading-the-interaction-as-w-exchange) gave the neutral interaction

$$\mathcal L_{W^3}
=-\frac g2\left(\bar\nu_{eL}\gamma^\mu\nu_{eL}
-\bar e_L\gamma^\mu e_L\right)W_\mu^3.$$

This couples $W^3$ to the neutrino and the left-chiral electron. There is no right-chiral electron term because $e_R$ is an $SU(2)_L$ singlet. Compare those properties with the photon:

| Fermion component | Coupling to $W^3$ | Electric charge |
| --- | --- | --- |
| $\nu_{eL}$ | Nonzero | $0$ |
| $e_L$ | Nonzero | $-e$ |
| $e_R$ | Zero | $-e$ |

Changing the strength $g$ cannot fix this pattern. We need an additional neutral coupling that can cancel the neutrino's contribution in the electromagnetic combination and also reach the right-chiral electron.

This is a motivation for extending the model, not a proof that there is only one possible extension. We will use the $SU(2)_L\times U(1)_Y$ structure of the **Glashow–Salam–Weinberg electroweak theory**. Its charge assignments and predictions must agree with experiment.

## Left and right parts need different weak charges

The [chiral projectors](weak-interaction.md#selecting-the-chiral-part-of-a-field) split the electron field into $e_L=P_Le$ and $e_R=P_Re$. These are parts of the same electron field, not separate electron species. The charged weak interaction treats them differently, even though both have electric charge $-e$.

The left-chiral neutrino and electron form the doublet

$$L=\begin{pmatrix}\nu_{eL}\\e_L\end{pmatrix},\qquad
T^3=\frac12\begin{pmatrix}1&0\\0&-1\end{pmatrix}.$$

The upper entry has $T^3$ eigenvalue $+1/2$ and the lower entry $-1/2$. We write an individual component's eigenvalue as $t_3$. For a right-chiral singlet, all three $SU(2)_L$ generators act as zero, so $t_3=0$.

These values do not equal the electric charges. For the doublet, the desired charges in units of $e$ are $(0,-1)$, whereas the $t_3$ values are $(1/2,-1/2)$. Both entries need the same offset, $-1/2$. This suggests adding a generator that acts equally on both entries.

## Hypercharge supplies the additional charge

Introduce a $U(1)$ phase symmetry with charge **weak hypercharge**, denoted $Y$. We use the convention

$$\boxed{Q=T^3+\frac Y2.}$$

Here $Q$ is the dimensionless electric-charge operator; a component with eigenvalue $Q_f$ has charge $eQ_f$. Within a doublet, $Y$ multiplies the identity matrix. It therefore adds the same offset to both entries without mixing them.

For the lepton doublet, choose $Y_L=-1$. The upper and lower charges become $1/2-1/2=0$ and $-1/2-1/2=-1$. For the right-chiral electron, $t_3=0$, so $Y_{e_R}=-2$ gives the required charge $-1$.

We can make the same assignments for the first-generation quarks:

| Fields | $SU(2)_L$ type | $t_3$ for each entry | $Y$ | $Q_f=t_3+Y/2$ |
| --- | --- | --- | --- | --- |
| $(\nu_{eL},e_L)$ | Doublet | $(+1/2,-1/2)$ | $-1$ | $(0,-1)$ |
| $e_R$ | Singlet | $0$ | $-2$ | $-1$ |
| $(u_L,d_L)$ | Doublet | $(+1/2,-1/2)$ | $+1/3$ | $(+2/3,-1/3)$ |
| $u_R$ | Singlet | $0$ | $+4/3$ | $+2/3$ |
| $d_R$ | Singlet | $0$ | $-2/3$ | $-1/3$ |

The other generations repeat this charge pattern. As in WI, we neglect neutrino masses and use the minimal fermion content without a right-chiral neutrino field. A singlet $\nu_R$ with $Y=0$, if added, would have no coupling to either electroweak gauge group.

These assignments reproduce the known charges once we choose $Q=T^3+Y/2$. The gauge-group name alone does not determine them. Full quantum consistency also constrains the assignments across quarks and leptons; those checks are beyond this construction.[^charges]

**Hypercharge is not electric charge.** In particular, a neutrino can have nonzero $Y$ while $Q_f=0$. The cancellation between $t_3$ and $Y/2$ will also cancel its photon coupling.

<details>
<summary>Checking the charge operator on a doublet</summary>

For any doublet with common hypercharge $Y$, the charge matrix is

$$Q=\begin{pmatrix}(1+Y)/2&0\\0&(Y-1)/2\end{pmatrix}.$$

The two charges differ by one. Their average is $Y/2$. For $(u_L,d_L)$, the required average is $(2/3-1/3)/2=1/6$, hence $Y=1/3$. For $(\nu_{eL},e_L)$, the average is $-1/2$, hence $Y=-1$.

For a singlet the matrix $T^3$ is zero, so $Y=2Q_f$. This gives the three right-chiral assignments in the table.

</details>

## Making both symmetries local

The product symbol in $SU(2)_L\times U(1)_Y$ means that we permit both types of transformation: an $SU(2)$ mixing and a hypercharge phase. They commute because the hypercharge is the same for both entries of a doublet. A field multiplet $F$ transforms as

$$F(x)\longrightarrow
e^{i\beta(x)Y_F/2}U(x)F(x).$$

Here $F$ can be a doublet or a singlet; for a singlet, $U$ acts as the identity. This is the same local-symmetry construction used in WI, now with one additional phase.

Local $SU(2)_L$ already supplied $W_\mu^1,W_\mu^2,W_\mu^3$. The extra $U(1)_Y$ supplies one more gauge field, called $B_\mu$, with coupling $g'$. This $B_\mu$ is a four-potential, not the magnetic field $\mathbf B$ from electromagnetism. The covariant derivative is

$$\boxed{D_\mu F=
\left(\partial_\mu+igT^aW_\mu^a
+ig'\frac{Y_F}{2}B_\mu\right)F.}$$

Substitution into $i\bar F\gamma^\mu D_\mu F$ gives the interaction terms. The charged $W^\pm$ terms stay as in WI. For a component of definite $t_3$ and $Y$, the neutral part is

$$\mathcal L_{\mathrm{neutral}}
=-\bar f\gamma^\mu f
\left(gt_3W_\mu^3+g'\frac Y2 B_\mu\right),$$

where $f$ denotes that chiral component. The two neutral fields couple to different charges. Neither, by itself, has the photon coupling for every fermion.

<details>
<summary>Checking the new phase compensation</summary>

Consider the hypercharge transformation alone, $F'=e^{i\beta Y_F/2}F$. Differentiating the phase produces $i(Y_F/2)(\partial_\mu\beta)F$. Choose

$$B'_\mu=B_\mu-\frac{1}{g'}\partial_\mu\beta.$$

Then the added term in the derivative contributes the opposite quantity:

$$\begin{aligned}
D'_\mu F'
&=e^{i\beta Y_F/2}\left[
D_\mu F+i\frac{Y_F}{2}(\partial_\mu\beta)F
-i\frac{Y_F}{2}(\partial_\mu\beta)F\right]\\
&=e^{i\beta Y_F/2}D_\mu F.
\end{aligned}$$

The $SU(2)$ contribution commutes with the phase. Under $SU(2)$ transformations, the $W$ fields transform as derived in WI, and $B_\mu$ is unchanged. Together, these rules make the kinetic term invariant under both local transformations.

</details>

## Identifying the photon combination

We need one neutral field whose coefficient is $eQ_f$ for every fermion. Try a rotation of the two neutral fields:

$$\begin{aligned}
A_\mu&=s_WW_\mu^3+c_WB_\mu,\\
Z_\mu&=c_WW_\mu^3-s_WB_\mu,
\end{aligned}\qquad
s_W=\sin\theta_W,\quad c_W=\cos\theta_W.$$

The angle $\theta_W$ is the **weak mixing angle**. This change of basis retains two independent neutral fields. We identify $A_\mu$ by demanding the electromagnetic coupling; the orthogonal combination is $Z_\mu$.

The coefficient of $A_\mu$ is $gs_Wt_3+g'c_WY/2$. To make it equal $e(t_3+Y/2)$, choose

$$\boxed{e=gs_W=g'c_W,\qquad \tan\theta_W=\frac{g'}g.}$$

With that choice, the interaction is exactly $-eQ_f\bar f\gamma^\mu f A_\mu$. Both electron chiralities have $Q_f=-1$, so both couple with the same electric charge. The neutrino has $Q_f=0$, so its two contributions cancel.

This establishes the electromagnetic coupling pattern. **It does not yet prove that $A$ is massless or that $Z$ is massive.** We use the physical names in anticipation of the Higgs mechanism, which selects these combinations as the neutral mass eigenstates: fields with definite particle masses. The next chapter derives that selection. A field rotation alone cannot generate a mass.

<details>
<summary>Rotating the neutral interaction and checking the cancellation</summary>

Invert the rotation:

$$W_\mu^3=s_WA_\mu+c_WZ_\mu,\qquad
B_\mu=c_WA_\mu-s_WZ_\mu.$$

Substitution gives

$$\begin{aligned}
gt_3W_\mu^3+g'\frac Y2B_\mu
={}&\left(gs_Wt_3+g'c_W\frac Y2\right)A_\mu\\
&+\left(gc_Wt_3-g's_W\frac Y2\right)Z_\mu.
\end{aligned}$$

For $\nu_{eL}$, $t_3=1/2$ and $Y=-1$, so the photon coefficient is

$$\frac{gs_W}{2}-\frac{g'c_W}{2}=\frac e2-\frac e2=0.$$

For $e_L$, it is $-gs_W/2-g'c_W/2=-e$. For $e_R$, it is $-g'c_W=-e$. A single relation between couplings therefore reproduces all three entries in the opening table.

To simplify the $Z$ coefficient, use $Y/2=Q_f-t_3$ and $g'=gs_W/c_W$:

$$\begin{aligned}
gc_Wt_3-g's_W\frac Y2
&=gc_Wt_3-\frac{gs_W^2}{c_W}(Q_f-t_3)\\
&=\frac g{c_W}\left[(c_W^2+s_W^2)t_3-s_W^2Q_f\right]\\
&=\frac g{c_W}(t_3-s_W^2Q_f).
\end{aligned}$$

</details>

## The Z couples to neutral weak currents

After the rotation, each chiral component has the neutral interaction

$$\mathcal L_{\mathrm{neutral}}
=-eQ_f\bar f\gamma^\mu fA_\mu
-\frac g{c_W}(t_3-s_W^2Q_f)\bar f\gamma^\mu fZ_\mu.$$

The photon coefficient depends only on electric charge. The $Z$ coefficient also depends on $t_3$, so left and right components generally couple differently. A **neutral current** connects a fermion to the same species at a vertex; it need not be a current of electrically neutral particles.

For the electron and neutrino, remove the common $g/c_W$ factor to compare the remaining $Z$ coefficients:

| Component | $t_3$ | $Q_f$ | $t_3-s_W^2Q_f$ |
| --- | --- | --- | --- |
| $\nu_{eL}$ | $+1/2$ | $0$ | $+1/2$ |
| $e_L$ | $-1/2$ | $-1$ | $-1/2+s_W^2$ |
| $e_R$ | $0$ | $-1$ | $s_W^2$ |

The neutrino couples to $Z$ even though it does not couple directly to the photon. The right-chiral electron also couples to $Z$, through its hypercharge contribution. The statement that charged weak interactions select left-chiral fermion fields does not mean that every weak interaction excludes right-chiral charged fermions.

For a charged fermion represented by a full Dirac field, collect the two chiral terms as

$$\mathcal L_Z=-\frac g{c_W}
\bar f\gamma^\mu\left(g_L^fP_L+g_R^fP_R\right)fZ_\mu,$$

$$g_L^f=t_{3L}^f-s_W^2Q_f,\qquad
g_R^f=-s_W^2Q_f.$$

The symbols $g_L^f,g_R^f$ are dimensionless coefficients; they are not new independent gauge couplings. Once $g$ and $g'$ are fixed, the charge assignments determine them. This is a testable consequence of electroweak unification: photon, charged weak, and neutral weak couplings follow from the same two parameters.[^neutral]

## A neutrino can scatter without changing species

Consider

$$\nu_\mu+e^-\longrightarrow\nu_\mu+e^-.$$

The muon-flavour neutrino remains a neutrino, and the electron remains an electron. A photon cannot connect the two currents because it has no direct coupling to the neutrino. The $Z$ has both required couplings:

```feynman
\begin{tikzpicture}
\begin{feynman}
\vertex (ni) at (-2,1.3) {$\nu_\mu$};
\vertex (a) at (0,1.3);
\vertex (nf) at (2,1.3) {$\nu_\mu$};
\vertex (ei) at (-2,-1.3) {$e^-$};
\vertex (b) at (0,-1.3);
\vertex (ef) at (2,-1.3) {$e^-$};
\diagram* {
(ni) -- [fermion] (a) -- [fermion] (nf),
(ei) -- [fermion] (b) -- [fermion] (ef),
(a) -- [boson, edge label={$Z$}] (b),
};
\end{feynman}
\end{tikzpicture}
```

*Neutral-current neutrino–electron scattering at tree level, with incoming particles on the left. Each fermion keeps its species, while the internal $Z$ transfers energy and momentum between the currents. The arrows indicate fermion flow.*

We chose $\nu_\mu$ to separate this example from electron-neutrino elastic scattering, which also has a charged-$W$ contribution at tree level. The charged current pairs $\nu_\mu$ with a muon, so it does not supply that extra diagram for the external particles shown here.

Experiments can observe the recoiling electron even when the outgoing neutrino escapes detection. In 1973, the Gargamelle collaboration announced evidence for weak neutral currents. That evidence supported the neutral interactions predicted by electroweak theory; it was not a direct observation of an on-shell $Z$. See [CERN's account of the discovery](https://timeline.web.cern.ch/discovery-weak-neutral-currents).

The diagram establishes which coupling contributes. Predicting an event rate still requires an amplitude, spin sums, and the final-state phase space from [From Lagrangian to Experiment](lagrangian-to-experiment.md).

<details>
<summary>Writing the amplitude with the new neutral-current factors</summary>

Let the incoming momenta be $k$ for the neutrino and $p$ for the electron, with outgoing momenta $k'$ and $p'$. The internal momentum is $q=k-k'=p'-p$. In the massless-neutrino approximation, the neutrino vertex is $-ig\gamma^\mu P_L/(2c_W)$. The electron vertex is $-ig\gamma^\nu(g_L^eP_L+g_R^eP_R)/c_W$.

Using external spinors and the massive-vector propagator as in WI gives

$$\begin{aligned}
i\mathcal M={}&
\left[\bar u_{\nu_\mu}(k')\left(-\frac{ig}{2c_W}\gamma^\mu P_L\right)u_{\nu_\mu}(k)\right]
D^Z_{\mu\nu}(q)\\
&\times\left[\bar u_e(p')\left(-\frac{ig}{c_W}\gamma^\nu(g_L^eP_L+g_R^eP_R)\right)u_e(p)\right].
\end{aligned}$$

At energies and momentum transfers small compared with $m_Z$, the supplied propagator result reduces to $D^Z_{\mu\nu}\simeq ig_{\mu\nu}/m_Z^2$. Thus

$$i\mathcal M\simeq-\frac{ig^2}{2c_W^2m_Z^2}
\left[\bar u_{\nu_\mu}(k')\gamma^\mu P_Lu_{\nu_\mu}(k)\right]
\left[\bar u_e(p')\gamma_\mu(g_L^eP_L+g_R^eP_R)u_e(p)\right].$$

This has the same current–current structure as the Fermi approximation in WI. The different chiral coefficients affect the angular distribution and rate. The mass $m_Z$ remains an input here; its origin and relation to $m_W$ come from the Higgs mechanism.

</details>

## Assembling the electroweak Lagrangian

We can now collect the gauge and fermion terms used above. Before symmetry breaking, they have the form

$$\boxed{\mathcal L_{\mathrm{gauge+fermion}}
=-\frac14W_{\mu\nu}^aW^{a\mu\nu}
-\frac14B_{\mu\nu}B^{\mu\nu}
+\sum_F i\bar F\gamma^\mu D_\mu F.}$$

The sum runs over the left-chiral doublets and right-chiral singlets in all three generations. For quarks, it also includes their three colour components, whose strong interactions we defer to QCD. The derivative acts with the generators and hypercharge appropriate to each $F$; its $SU(2)$ term vanishes on a singlet.

The first two terms describe the gauge fields. The $SU(2)$ field strength includes gauge-boson self-interactions, as developed on the [Yang–Mills page](yang-mills.md). The Abelian field strength is $B_{\mu\nu}=\partial_\mu B_\nu-\partial_\nu B_\mu$, with the same derivative structure as Maxwell's. The fermion term includes both propagation and the couplings obtained by expanding $D_\mu$.

The full electroweak Lagrangian also contains a Higgs field, its potential, and its couplings to fermions. We have not supplied those terms yet. The expression above completes the gauge and fermion construction; it does not by itself describe the observed particle masses.

Unification here means a common gauge theory whose fields combine into the photon, $W^\pm$, and $Z$, with related couplings. It does not mean that $g$ and $g'$ are equal or that low-energy electromagnetic and weak processes have equal strengths.

## The mass problem leads to the Higgs field

The physical photon is massless, while the $W$ and $Z$ have masses. A direct mass term quadratic in the original gauge potentials changes under their local gauge transformations. Adding such terms by hand would abandon the gauge invariance we used to relate the interactions.

Fermion masses present a related problem. The ordinary electron mass term joins its two chiral parts:

$$-m_e\bar e e=-m_e\left(\bar e_Le_R+\bar e_Re_L\right).$$

But $e_L$ belongs to an $SU(2)_L$ doublet with $Y=-1$, whereas $e_R$ is a singlet with $Y=-2$. Their transformation factors do not cancel. The ordinary mass term is not invariant under the full electroweak group, even though it respects electromagnetic gauge symmetry.

<details>
<summary>Checking why the electron mass term fails the hypercharge transformation</summary>

Under a hypercharge transformation alone,

$$e_L\to e^{-i\beta/2}e_L,\qquad
\bar e_L\to\bar e_Le^{+i\beta/2},\qquad
e_R\to e^{-i\beta}e_R.$$

Therefore

$$\bar e_Le_R\longrightarrow e^{-i\beta/2}\bar e_Le_R,$$

which differs from the original term for a general $\beta(x)$. The conjugate term acquires the opposite phase, so their sum is not generally unchanged. An $SU(2)$ transformation also mixes $e_L$ with the neutrino component while leaving $e_R$ a singlet. An additional field with appropriate transformation properties is needed to build an invariant coupling between them.

</details>

The [Higgs mechanism](higgs-mechanism.md) supplies that field. Its vacuum configuration leaves electromagnetic charge unbroken while giving masses to the $W$ and $Z$; its fermion couplings produce charged-fermion masses. That chapter will derive these statements. Here we have established the coupling structure and shown how it permits neutral weak scattering while preserving the photon interactions from QED.

[^charges]: These are the usual electroweak assignments in the convention $Q=T^3+Y/2$. Some texts absorb the factor $1/2$ into the definition of hypercharge. For example, [Tong's electroweak notes, §5.1](https://davidtong.org/pdfs/teaching/standard-model/standardmodel5.pdf) use hypercharges half as large with the corresponding change in the covariant derivative. The physical products of coupling and charge are unchanged. A **gauge anomaly** is a quantum failure of the classical gauge symmetry; cancellation across the fermion content is an additional consistency check, not derived here.

[^neutral]: The [Particle Data Group's electroweak review, §10.1](https://pdg.lbl.gov/2025/reviews/rpp2025-rev-standard-model.pdf) gives the neutral-current couplings and weak mixing relations. It also discusses the radiative corrections needed for precision comparisons. Our formulas describe the tree-level structure.
