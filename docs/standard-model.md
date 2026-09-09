# The Standard Model

We developed the interactions separately because each answered a different physical question. QED described charged particles and light. The weak theory described transitions such as beta decay. Electroweak unification related their couplings, the Higgs field supplied masses, and QCD described the strong interaction of quarks and gluons.

The **Standard Model** combines these fields and interactions in one quantum field theory. Its gauge group is

$$SU(3)_C\times SU(2)_L\times U(1)_Y.$$

The three factors act on colour, weak isospin, and hypercharge. They do not represent three disjoint sets of matter: a quark carries all three kinds of charge and participates in all three interactions.

This final chapter collects the construction and distinguishes its inputs from its predictions. We keep $\hbar=c=1$, metric $(+,-,-,-)$, $Q=T^3+Y/2$, and the plus-sign covariant derivative. We first summarize the minimal theory with massless neutrinos used in the preceding chapters, then explain why neutrino observations require extending it.

## Gauge Fields and Self-Interactions

The gauge group specifies how many independent gauge fields we introduce. The physical electroweak combinations follow after the Higgs mechanism:

| Gauge symmetry | Original fields | Description after the Higgs mechanism |
| --- | --- | --- |
| $SU(3)_C$ | Eight gluons $G^a_\mu$ | Eight colour gauge fields |
| $SU(2)_L$ | $W^1_\mu,W^2_\mu,W^3_\mu$ | $W^1,W^2$ form $W^\pm$; $W^3$ mixes with $B$ |
| $U(1)_Y$ | $B_\mu$ | Together with $W^3$, forms photon $A$ and $Z$ |

The neutral-field rotation does not add particles. We use $W^3,B$ to display the original symmetry and $A,Z$ to display the electromagnetic and neutral weak interactions of particles with definite masses.

For any fermion multiplet $F$, all gauge interactions enter through

$$D_\mu F=\left(\partial_\mu
+ig_sT_C^aG^a_\mu
+igT_L^iW^i_\mu
+ig'\frac{Y_F}{2}B_\mu\right)F.$$

Each generator acts on the appropriate internal index. A colour singlet has $T_C^a=0$; a weak singlet has $T_L^i=0$. Thus the same expression applies to fields with different interactions. The constants $g_s,g,g'$ set the three coupling strengths; the generators and hypercharges specify how each field couples. Their numerical values require experimental input.

The gauge-field kinetic terms are

$$\mathcal L_{\mathrm{gauge}}=-\frac14G^a_{\mu\nu}G^{a\mu\nu}
-\frac14W^i_{\mu\nu}W^{i\mu\nu}
-\frac14B_{\mu\nu}B^{\mu\nu}.$$

The [Yang–Mills construction](yang-mills.md) supplies the nonlinear terms in $G_{\mu\nu}$ and $W_{\mu\nu}$. Squaring them gives three- and four-gauge-boson interactions. Gluons therefore interact with gluons, while the weak gauge fields interact with one another. After changing the electroweak basis, these terms include photon–$W^+$–$W^-$ and $Z$–$W^+$–$W^-$ vertices.

The Abelian $B$ field strength has no such nonlinear term. There is no elementary three-photon or four-photon vertex in this Lagrangian. Photons can nevertheless scatter through charged-particle loops, so absence of a direct vertex does not imply absence of every process involving several photons.

## Quarks and Gauge Interactions

An up quark is one particle species with colour, electric charge, and weak couplings. Its colour components are not three different flavours. Likewise, left- and right-chiral parts belong to the same massive quark field but have different electroweak assignments.

For the first quark family, the assignments are

| Fields | Colour | Weak isospin | Hypercharge $Y$ | Electric charge in units of $e$ |
| --- | --- | --- | --- | --- |
| $(u_L,d_L)$ | Triplet | Doublet | $1/3$ | $(2/3,-1/3)$ |
| $u_R$ | Triplet | Singlet | $4/3$ | $2/3$ |
| $d_R$ | Triplet | Singlet | $-2/3$ | $-1/3$ |

A colour triplet has three components. A weak doublet has two. These are independent indices, as shown in [QCD](qcd.md). Both chiralities couple to gluons and photons. The charged weak interaction selects the left-chiral fields, while the $Z$ couples to both chiralities with different coefficients.

The interaction determines which labels can change. At a quark–gluon vertex, colour can change while flavour and electric charge remain the same. A charged-$W$ vertex can connect an up-type quark to a down-type quark, with the $W$ carrying the electric-charge difference. The gluon cannot replace the $W$ in beta decay.

Quarks and gluons form hadrons through the QCD dynamics. Protons and neutrons are composite states of this theory, not additional elementary fields in the Standard Model Lagrangian. Much of their mass comes from strong-interaction energy, even though the quark mass parameters themselves arise through Higgs interactions.

## Leptons and Gauge Interactions

**Leptons** are the fermions with no colour charge: charged leptons and neutrinos. Their first-family assignments are

| Fields | Colour | Weak isospin | Hypercharge $Y$ | Electric charge in units of $e$ |
| --- | --- | --- | --- | --- |
| $(\nu_{eL},e_L)$ | Singlet | Doublet | $-1$ | $(0,-1)$ |
| $e_R$ | Singlet | Singlet | $-2$ | $-1$ |

Zero colour generators mean no direct gluon coupling. This distinguishes an electron from a quark without introducing a separate rule that switches the strong force off for leptons.

For the photon and $Z$, the neutral interaction of a chiral component $f$ is the expression derived in [EW](electroweak-unification.md):

$$\mathcal L_{\mathrm{neutral}}
=-eQ_f\bar f\gamma^\mu fA_\mu
-\frac{g}{c_W}(t_3-s_W^2Q_f)\bar f\gamma^\mu fZ_\mu,$$

where $s_W=\sin\theta_W$, $c_W=\cos\theta_W$, and $e=gs_W=g'c_W$.

The neutrino has $Q_f=0$ but $t_3=1/2$. It therefore has no photon coupling in this construction, yet does couple to the $Z$. Both electron chiralities have $Q_f=-1$ and hence the same electromagnetic coupling. Their different $t_3$ values give different $Z$ couplings. The charged weak interaction connects the left-chiral electron and neutrino fields.

These distinctions are consequences of the assigned representations and charges. The group name alone does not select the particle content or every charge assignment. We use assignments that reproduce observations and satisfy quantum consistency conditions; the general anomaly-cancellation checks are beyond this course's construction.

## Higgs Mechanism — Gauge Masses

A direct gauge-boson mass term would violate the original gauge symmetry. The Higgs construction instead starts from a gauge-invariant scalar kinetic term and a potential with a nonzero minimum. The Higgs is a colour singlet, a weak doublet, and has hypercharge $Y=1$.

In unitary gauge we wrote

$$\phi(x)=\frac1{\sqrt2}\begin{pmatrix}0\\v+h(x)\end{pmatrix}.$$

The vacuum value $v$ is present even when there are no Higgs particles. The field $h$ describes fluctuations above that vacuum; its quanta are Higgs bosons. Substituting the constant part into $(D_\mu\phi)^\dagger D^\mu\phi$ gives

$$m_W=\frac{gv}{2},\qquad
m_Z=\frac v2\sqrt{g^2+g'^2},\qquad m_A=0.$$

The photon remains massless because electric charge leaves the vacuum unchanged. Colour also remains unbroken because the Higgs is a colour singlet, so no gluon mass term appears. This statement about the Lagrangian is compatible with confinement: isolated gluons are not the observable long-distance particles of QCD.

The doublet's four real scalar degrees of freedom account for the particle spectrum. Three provide longitudinal polarizations for $W^+,W^-,Z$; one remains as $h$. The Higgs mechanism changes how the degrees of freedom appear, without discarding three physical modes.

The mass relation $m_W=m_Z\cos\theta_W$ follows at tree level. Knowing the coupling parameters and the vacuum value fixes both masses; precision predictions also require quantum corrections. The measured Fermi constant determines $v\approx246\ \mathrm{GeV}$, while the Higgs mass determines the potential coupling through $m_h^2=2\lambda v^2$.

## Fermion Masses and Yukawa Interactions

Fermions acquire mass through Yukawa interactions, not through their gauge kinetic terms. For the electron, the gauge-invariant interaction gives

$$-y_e\bar L\phi e_R+\text{Hermitian conjugate}
\quad\longrightarrow\quad
-m_e\bar e e-\frac{m_e}{v}h\bar e e,
\qquad m_e=\frac{y_ev}{\sqrt2}.$$

The same coupling produces a mass from the vacuum value and an interaction with the fluctuating Higgs field. This is why the Higgs coupling to a charged fermion is proportional to its mass. The numerical value of $y_e$ is an input, so the mechanism explains the form and origin of the mass term without predicting the electron's mass from the gauge couplings.

We can now collect the Lagrangian constructed throughout the course:

$$\boxed{\mathcal L_{\mathrm{SM}}
=\mathcal L_{\mathrm{gauge}}
+\sum_F i\bar F\gamma^\mu D_\mu F
+(D_\mu\phi)^\dagger D^\mu\phi
-V(\phi)+\mathcal L_{\mathrm{Yukawa}}.}$$

The sum is over left-chiral doublets and right-chiral singlets, including their colour and family labels. The five pieces describe gauge propagation and self-interactions, fermion propagation and gauge interactions, scalar propagation and gauge interactions, the scalar potential, and scalar–fermion interactions. There are no separate bare fermion masses in this expression: they appear when we expand the Yukawa terms about the vacuum.

We omit the possible strong-CP term discussed in QCD. Gauge fixing and the associated auxiliary terms are also needed for perturbative calculations, but are not additional physical particle interactions in this classical gauge-invariant expression.

<details>
<summary>Writing the Yukawa terms with family indices</summary>

For three families, the coupling can connect a left-chiral field of family $i$ to a right-chiral field of family $j$:

$$\mathcal L_{\mathrm{Yukawa}}=
-\bar Q_L^i(Y_d)_{ij}\phi d_R^j
-\bar Q_L^i(Y_u)_{ij}\widetilde\phi u_R^j
-\bar L_L^i(Y_e)_{ij}\phi e_R^j
+\text{Hermitian conjugate}.$$

Here $i,j=1,2,3$ are summed, and $\widetilde\phi=i\sigma^2\phi^*$ is the conjugate doublet introduced in the [Higgs chapter](higgs-mechanism.md). The capital matrices $Y_u,Y_d,Y_e$ are Yukawa couplings, not hypercharges. Substitution of the vacuum gives mass matrices $M_f=vY_f/\sqrt2$.

The non-diagonal entries join fields with different family labels. To describe particles of definite mass, choose left and right unitary transformations such that $U_{fL}^\dagger M_fU_{fR}$ is diagonal with nonnegative entries. Those entries are the masses. This is the singular-value decomposition from matrix algebra; we use the result here without a separate derivation. Its physical consequence for charged weak interactions is explained next.

</details>

## Fermion Generations and Flavor Mixing

A **generation**, or family, contains one up-type quark, one down-type quark, one charged lepton, and its neutrino. Three generations occur in the observed particle content:

| Generation | Up-type quark | Down-type quark | Charged lepton | Neutrino |
| --- | --- | --- | --- | --- |
| First | Up $u$ | Down $d$ | Electron $e$ | $\nu_e$ |
| Second | Charm $c$ | Strange $s$ | Muon $\mu$ | $\nu_\mu$ |
| Third | Top $t$ | Bottom $b$ | Tau $\tau$ | $\nu_\tau$ |

Corresponding entries repeat the gauge assignments above. Their different masses arise from different Yukawa parameters, not different colour or electric charges. Antiparticles are described by the same quantum fields; they are not extra generations.

A field basis convenient for writing weak doublets need not be the basis in which the mass terms are diagonal. As with the neutral gauge fields in EW, changing the basis can make one part of the theory easier to interpret. Here we choose quark fields with definite masses. The up-type and down-type mass matrices generally require different left-chiral rotations.

Their mismatch appears in the charged weak current:

$$\mathcal L_{\mathrm{CC}}^{\mathrm{quark}}
=-\frac g{\sqrt2}\bar u_{Li}\gamma^\mu V_{ij}d_{Lj}W^+_\mu
+\text{Hermitian conjugate}.$$

The indices label $u_i=(u,c,t)$ and $d_j=(d,s,b)$. The **Cabibbo–Kobayashi–Maskawa matrix**, or **CKM matrix**, is $V=U_{uL}^\dagger U_{dL}$. It records the mismatch of the two rotations. An up quark can therefore couple through a charged current to more than one down-type mass eigenstate. Beta decay uses the entry $V_{ud}$ introduced in WI.

<details>
<summary>Why the mismatch remains in the weak current</summary>

Let the original fields be $u'_L=U_{uL}u_L$ and $d'_L=U_{dL}d_L$. Then

$$\bar u'_L\gamma^\mu d'_L
=\bar u_L\gamma^\mu U_{uL}^\dagger U_{dL}d_L
=\bar u_L\gamma^\mu Vd_L.$$

The matrices act on family labels, so they commute with $\gamma^\mu$. For a neutral current with the same coefficient for all up-type families, the product is instead $U_{uL}^\dagger U_{uL}=I$. The same cancellation occurs within the down-type sector. Thus the basis change introduces the CKM matrix in charged currents, without introducing flavour-changing photon or gluon vertices.

</details>

CKM entries are experimental inputs. The matrix has a physical complex phase that permits differences between certain particle and antiparticle processes, called **CP violation**. Establishing its independent parameters and calculating such asymmetries requires additional analysis; the key point here is the origin of mixing as a mismatch between mass and weak-interaction bases.

Neutrinos expose a limitation of the minimal construction. In experiments, a neutrino produced with one flavour can later interact as another. **Neutrino oscillations** arise because flavour states contain different mass eigenstates whose relative phases change during propagation. The observations require neutrino mass differences, whereas the minimal theory used above has massless neutrinos. New interactions or fields are needed; neutrino masses are not a prediction of the massless model. The [PDG neutrino review](https://pdg.lbl.gov/2025/reviews/rpp2025-rev-neutrino-mixing.pdf) develops this extension and its evidence.

## Final Remarks

The Standard Model is more than a list of particles. Its field assignments and interaction terms relate observations that would otherwise require separate rules. The same weak coupling enters beta decay and gauge-boson interactions. The same electroweak parameters determine photon and $Z$ couplings. The same Yukawa interaction gives a fermion mass and its Higgs coupling.

Those relationships make the theory testable even though it contains measured parameters:

| Experimental inputs | Consequences once those inputs are fixed |
| --- | --- |
| Gauge couplings and charge assignments | Relative gauge-interaction strengths and allowed elementary vertices |
| Higgs vacuum value and scalar coupling | Gauge masses, Higgs mass, and scalar interactions at the specified approximation |
| Yukawa masses and mixing parameters | Higgs–fermion couplings and charged-current flavour amplitudes |

A Lagrangian is the starting point for a prediction, not the final measured rate. We still construct amplitudes, sum interfering contributions, account for the observed final states, and compare with data, as in [From Lagrangian to Experiment](lagrangian-to-experiment.md). QCD bound states also require methods beyond a short perturbation series.

The theory does not explain why there are three generations or why its parameters take their observed values. The minimal field content does not account for neutrino masses. It contains no quantum theory of gravity, and explaining the cosmological dark matter and the observed matter–antimatter imbalance requires physics beyond what we have constructed here. These limitations do not erase its predictions within the regimes where it has been tested; they identify questions for a more complete theory.

The course began with equations for particle trajectories and ended with quantum fields whose interactions can change particle number. The recurring method was to identify the physical requirements, choose fields and symmetries, construct consistent interactions, and calculate observable consequences. The optional [Path Integrals](path-integrals.md) sequence gives another way to formulate and calculate with these same quantum theories.
