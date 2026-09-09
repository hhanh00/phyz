# Higgs Mechanism

In [Electroweak Unification](electroweak-unification.md), we identified the photon, $W^\pm$, and $Z$ and related their interactions. Their masses remained unexplained. Direct gauge-boson mass terms would violate the electroweak gauge symmetry, while an electron mass term joins left- and right-chiral fields with different electroweak charges.

We now introduce a scalar field whose lowest-energy value is nonzero. Interactions with that vacuum value produce mass terms when we expand around the ground state, even though the original Lagrangian respects the full gauge symmetry. Fluctuations about the vacuum describe an additional particle, the Higgs boson. The field's vacuum value and the particle excitation play different roles; we will distinguish them throughout.

We use natural units, $\hbar=c=1$, the metric $(+,-,-,-)$, and the covariant-derivative conventions of the previous two chapters. The mass formulas below are at tree level, before quantum corrections.

The steps connect as follows:

1. **Separate the symmetry of the laws from the symmetry of the ground state.** A potential can respect a symmetry while its lowest-energy configurations do not. Selecting one of those configurations is spontaneous symmetry breaking.
2. **Gauge the broken symmetry in the simplest case.** A charged scalar with a nonzero vacuum value gives a $U(1)$ gauge field a mass. This simpler example shows how the scalar phase becomes the additional polarization of a massive vector.
3. **Apply the construction to $SU(2)_L\times U(1)_Y$.** A scalar doublet with a suitable potential acquires a vacuum value that leaves electric charge unbroken.
4. **Read off the fermion masses.** Coupling that doublet to the fermions gives each charged fermion a mass set by its coupling strength.
5. **Read off the gauge-boson masses.** Expanding the doublet's kinetic term gives masses to the $W$ and $Z$ while leaving the photon massless.

## Spontaneous Symmetry Breaking

A symmetric law can have a ground state that does not share its symmetry. Consider an idealized magnet whose spin interactions have no preferred direction. Below its critical temperature, its magnetization points in one direction, although other orientations have the same energy. We will construct a field with an analogous set of lowest-energy configurations, then study small disturbances around one of them.

Take a single complex scalar field $\phi(x)$ with a global $U(1)$ symmetry, $\phi\to e^{i\alpha}\phi$ (see [the appendix on groups](appendix-math-groups.md) for $U(1)$). Its Lagrangian is

$$\mathcal L=\partial_\mu\phi^*\partial^\mu\phi-V(\phi),\qquad
V(\phi)=-\mu^2\phi^*\phi+\lambda(\phi^*\phi)^2,$$

with $\mu^2>0$ and $\lambda>0$. The phase rotation leaves $\phi^*\phi$ unchanged, so $\mathcal L$ is invariant. The unusual part is the sign of the quadratic term. A positive $\mu^2$ in front of $-\phi^*\phi$ means the field configuration $\phi=0$ sits at a local maximum of $V$, not a minimum.

The **vacuum** is the lowest-energy state. For a static, spatially uniform scalar field, derivative contributions to the energy vanish, so we find its classical vacuum by minimizing $V$. To find the minima, write $\phi^*\phi=\rho^2$ and minimize $V=-\mu^2\rho^2+\lambda\rho^4$. Treating $r=\rho^2$ as the variable gives $dV/dr=-\mu^2+2\lambda r=0$, hence

$$\phi^*\phi=\frac{\mu^2}{2\lambda}\equiv\frac{v^2}{2}.$$

The minimum is not a point but a circle in the complex plane: every $\phi$ with $|\phi|=v/\sqrt2$ has the same lowest energy. We use $v$ to parameterize the **vacuum expectation value**, the value of the field in the ground state; with our normalization, its magnitude is $v/\sqrt2$. We describe particles as excitations above that ground state. Choose the real point on the circle,

$$\langle\phi\rangle=\frac{v}{\sqrt2},$$

taking the vacuum value real. The Lagrangian's $U(1)$ symmetry still holds, but this vacuum is not invariant under it: a phase rotation moves it to a different point on the circle. A symmetry of the Lagrangian that the chosen vacuum does not share is **spontaneously broken**. The potential still has the symmetry. The nonzero vacuum value specifies which member of the equal-energy, or **degenerate**, set we expand around.

![The Mexican-hat potential V(φ) plotted over the complex φ plane. The centre φ=0 is a local maximum; the lowest energy lies on a circle of radius v/√2, the degenerate minima. One point on that circle is the chosen vacuum. Moving around the trough (the flat direction) costs no energy and gives the massless Goldstone mode χ; moving radially up the wall costs energy and gives the massive mode h.](./manim/mexican-hat-potential.png)

The two independent excitations above this vacuum behave differently. Write the field as a fluctuation about the chosen point,

$$\phi(x)=\frac{1}{\sqrt2}\bigl(v+h(x)+i\,\chi(x)\bigr),$$

The real fields $h$ and $\chi$ describe small displacements in the radial and tangential directions at the chosen vacuum. At first order, $\chi$ changes the phase; a finite displacement around the circle is more accurately described with polar coordinates below.

The terms quadratic in these fluctuations determine their free propagation:

$$\mathcal L_{\mathrm{quadratic}}=\frac12\partial_\mu h\partial^\mu h+\frac12\partial_\mu\chi\partial^\mu\chi-\frac12m_h^2h^2,
\qquad m_h^2=2\lambda v^2,\quad m_\chi^2=0.$$

For a canonically normalized scalar, $\tfrac12(\partial f)^2-\tfrac12m^2f^2$ gives $(\Box+m^2)f=0$, hence $E^2=\mathbf p^2+m^2$. This is why the quadratic coefficient identifies a particle mass. Higher powers describe interactions between the excitations.

<details>
<summary>Expanding the potential around the chosen vacuum</summary>

Using $\phi^*\phi=\tfrac12\bigl((v+h)^2+\chi^2\bigr)$ and $v^2=\mu^2/\lambda$,

$$V=-\frac{\mu^2}{2}\bigl((v+h)^2+\chi^2\bigr)
+\frac{\lambda}{4}\bigl((v+h)^2+\chi^2\bigr)^2.$$

Expanding to second order in $h$ and $\chi$, the terms linear in $h$ cancel because $v$ sits at the minimum, and the quadratic terms are

$$V=\text{const}+\frac12\bigl(2\mu^2\bigr)h^2+0\cdot\chi^2+\dots$$

A quadratic term $\tfrac12 m^2 f^2$ identifies the mass of a scalar field $f$, in the same way the quadratic term in the [harmonic oscillator](harmonic-oscillator.md) fixes its frequency. So

$$m_h^2=2\mu^2=2\lambda v^2,\qquad m_\chi^2=0.$$

The radial field $h$ is massive; the angular field $\chi$ is massless.

</details>

The massless field $\chi$ is a **Goldstone boson**. Its absence of mass is not a coincidence of this potential: moving along the circle of minima costs no energy, because every point on the circle is a degenerate vacuum, and a field excitation that costs no energy at long wavelength has no mass. For relativistic scalar theories of this kind, Goldstone's theorem gives one massless mode per broken continuous global generator. We state the general theorem without proof because its derivation requires a longer discussion of conserved currents; the expansion above proves the result for this example. Spatially varying phase disturbances still carry gradient energy; masslessness means zero rest energy, not zero energy for every wave. The massive field $h$ measures excursions in the direction that does cost energy, out of the trough and up the wall of the potential.

![The two excitations of the chosen vacuum. Left: in the complex-φ plane, the radial direction h points up the wall of the potential, while the angular direction θ runs along the circle of minima. Right: the energy cost of each. Displacing along h is a parabola, so h has mass m_h²=2λv²; displacing along θ stays at the minimum, a flat direction, so θ is the massless Goldstone mode.](./manim/goldstone-modes.png)

The electroweak symmetry is local, so the global-symmetry result is not yet our final particle spectrum. The next step shows why the phase does not remain an independent massless particle when a gauge field is present.

## Higgs Mechanism U(1)

Now make the $U(1)$ local, exactly as [QED](qed.md) makes the electron's phase symmetry local. Promoting $\phi\to e^{i\alpha(x)}\phi$ to a spacetime-dependent phase requires a gauge field $A_\mu$ and the covariant derivative $D_\mu=\partial_\mu+iqA_\mu$, with $q$ the scalar's gauge coupling, taken positive here. This $A_\mu$ belongs to a toy model; it is not the physical photon of the electroweak theory. The Lagrangian becomes

$$\mathcal L=(D_\mu\phi)^*(D^\mu\phi)-V(\phi)-\frac14F_{\mu\nu}F^{\mu\nu},$$

with the same potential as before and the same circle of minima. The field strength $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$ describes the free gauge field, which is massless on its own, as a photon-like mass term would break the gauge symmetry.

Unlike a global phase change, a gauge transformation changes both $\phi$ and $A_\mu$ as two parts of the same description. Near the nonzero vacuum, we can choose the scalar to be real at each point, provided we transform the gauge field at the same time. This choice is **unitary gauge**:

$$\phi(x)=\frac{1}{\sqrt2}\bigl(v+h(x)\bigr).$$

The phase no longer appears as a separate scalar field. Its dynamical degree of freedom remains in the gauge field, which will now have three physical polarizations rather than two. Gauge fixing does not discard a physical mode.

<details>
<summary>Why fixing the phase removes the Goldstone field</summary>

Write the field in magnitude-and-phase form rather than real and imaginary parts,

$$\phi(x)=\frac{1}{\sqrt2}\bigl(v+h(x)\bigr)e^{i\theta(x)/v}.$$

Here $\theta/v$ is the phase angle, and $\theta$ agrees with $\chi$ to first order in small fluctuations. The radial variable $h$ in this polar expression likewise agrees with the earlier Cartesian $h$ only to first order. A gauge transformation multiplies $\phi$ by $e^{i\alpha(x)}$, which shifts $\theta(x)/v\to\theta(x)/v+\alpha(x)$. Choosing $\alpha(x)=-\theta(x)/v$ at every point cancels the phase and leaves $\phi$ real, which sets $\theta$ to zero everywhere. Zeroing the phase and removing the Goldstone field are the same operation because the Goldstone field is that phase. This needs $\alpha$ to be a free function of spacetime; a global symmetry supplies only one constant $\alpha$ and cannot cancel a varying $\theta(x)$. With our derivative convention, $A'_\mu=A_\mu-\partial_\mu\alpha/q$, so this choice gives

$$A'_\mu=A_\mu+\frac{\partial_\mu\theta}{qv},\qquad
\frac{\partial_\mu\theta}{v}+qA_\mu=qA'_\mu.$$

The combination on the left appears in the scalar kinetic term and is gauge invariant. In unitary gauge we write it using $A'_\mu$ alone, then drop the prime. This explains where the phase contribution goes. The construction applies to fluctuations near the nonzero vacuum; it need not define a single smooth gauge through zeros of the scalar field.

</details>

<details>
<summary>Substituting the unitary-gauge field into the kinetic term</summary>

With $\phi$ real, $D_\mu\phi=\tfrac{1}{\sqrt2}\bigl(\partial_\mu h+iq(v+h)A_\mu\bigr)$, so

$$(D_\mu\phi)^*(D^\mu\phi)
=\frac12(\partial_\mu h)^2+\frac12q^2(v+h)^2A_\mu A^\mu.$$

Expanding $(v+h)^2=v^2+2vh+h^2$ isolates a term with no factor of $h$:

$$\frac12q^2v^2A_\mu A^\mu.$$

A term $\tfrac12 m^2 A_\mu A^\mu$ is the mass term for a vector field, so the gauge field has acquired

$$m_A=qv.$$

The remaining pieces, proportional to $vh$ and $h^2$, are couplings between the gauge field and the surviving scalar $h$.

</details>

The key term in the main Lagrangian is therefore

$$\mathcal L\supset-\frac14F_{\mu\nu}F^{\mu\nu}+\frac12q^2v^2A_\mu A^\mu.$$

Its vector equation has the form $\partial_\mu F^{\mu\nu}+m_A^2A^\nu=0$, with $m_A=qv$. The mass comes from the original gauge-invariant scalar kinetic term, evaluated around a nonzero vacuum. The Goldstone field did not simply vanish when we chose the gauge. A massless vector field has two polarizations, while a massive one has three, and the extra, longitudinal polarization is the mode that would otherwise have been the Goldstone boson. Counting the independent fields confirms this bookkeeping:

| Before breaking | Degrees of freedom | After breaking | Degrees of freedom |
| --- | --- | --- | --- |
| Complex scalar $\phi$ | 2 | Real scalar $h$ | 1 |
| Massless vector $A_\mu$ | 2 | Massive vector $A_\mu$ | 3 |
| **Total** | **4** | **Total** | **4** |

<details>
<summary>Why a massive vector has one more polarization than a massless one</summary>

A vector field $A_\mu$ has four components, and the number of physical polarizations is what remains after the constraints. The massive field equation, $\partial_\mu F^{\mu\nu}+m^2A^\nu=0$ (the massive vector introduced with the [field classification in QFT](qft.md#fields)), forces one constraint automatically: taking its divergence kills the antisymmetric field-strength term and leaves $m^2\partial_\mu A^\mu=0$, so $\partial_\mu A^\mu=0$. For a plane wave $A_\mu\propto\varepsilon_\mu e^{-ip\cdot x}$ this reads $p^\mu\varepsilon_\mu=0$: the polarization must be orthogonal to the momentum, one condition on the four components, leaving three.

To see what those three are, go to the particle's rest frame, $p^\mu=(m,\mathbf 0)$. The condition becomes $\varepsilon_0=0$, so the polarization is a purely spatial 3-vector with three independent directions. A spatial vector under rotations is exactly the spin-1 object with $2s+1=3$ states, all on equal footing. The transverse-versus-longitudinal distinction appears only once the particle moves: boosting along its direction of motion leaves the two polarizations perpendicular to that direction unchanged (transverse) and singles out the third along it (longitudinal).

A massless particle has no rest frame, and the count drops to two. With no mass term the equation of motion is unchanged by a gauge transformation $A_\mu\to A_\mu+\partial_\mu\lambda$, which shifts the polarization by $\varepsilon_\mu\to\varepsilon_\mu+\alpha\,k_\mu$ and removes the longitudinal mode, leaving only the two transverse polarizations. This is the same $4\to2$ reduction worked out for the photon in [QED](qed.md). A standalone vector mass term removes that gauge freedom. In the Higgs construction, the full scalar–vector theory retains gauge invariance, but unitary gauge has already used the phase freedom. The massive vector therefore retains its third physical polarization.

So giving the gauge field a mass requires exactly one extra polarization it did not have when massless. The spontaneously broken scalar supplies exactly one degree of freedom, which fills that longitudinal slot. With a global symmetry that scalar would be a physical massless Goldstone particle; with the symmetry gauged, the same degree of freedom becomes the vector's longitudinal polarization instead.

</details>

This is the **Higgs mechanism**: a nonzero scalar vacuum value gives the gauge field a mass, with the scalar phase providing its longitudinal polarization. We often call this spontaneous gauge-symmetry breaking. Unlike the global example, gauge-related vacuum orientations describe the same physical state; the local gauge symmetry remains a redundancy of the full description.

The surviving scalar $h$ has physical, massive excitations. It plays the same role in this simplified model that the Higgs boson plays in the full theory. We now apply the mechanism to the electroweak symmetry from the [previous chapter](electroweak-unification.md), using a scalar doublet.

In the electroweak theory, the Higgs interactions also address the consistency problem raised in [Weak Interaction](weak-interaction.md#connecting-the-two-currents): the longitudinal polarization of a massive vector, which made some scattering amplitudes grow too fast when added by hand, here comes from a scalar field with couplings fixed by the same symmetry, and the resulting Higgs contributions cancel the problematic leading growth. We state this scattering result without proof; checking it requires combining several amplitudes and is beyond the mass calculation here.

## Standard Model Higgs SU(2)L × U(1)Y

The $U(1)$ example gave a mass to one gauge field. For electroweak theory, we need three massive fields, $W^+,W^-,Z$, and one massless field, the photon. We must choose a scalar whose vacuum value produces that pattern.

A scalar can have a constant vacuum value without selecting a spatial direction or preferred inertial frame. To give the $W$ fields masses, it must also carry weak isospin: an $SU(2)_L$ singlet has zero generators and therefore no $W$ coupling in its covariant derivative. The smallest nontrivial choice is a **doublet**, two complex scalar components that transform together under $SU(2)_L$.

We want the component with a vacuum value to have electric charge zero. Choose it to be the lower entry, where $t_3=-1/2$. The charge formula from EW gives

$$Q_f=t_3+Y/2=-\frac12+\frac Y2=0,
\qquad\text{so}\qquad Y=+1.$$

The upper entry then has charge $+1$. We write

$$\phi=\begin{pmatrix}\phi^+\\\phi^0\end{pmatrix}.$$

The superscripts label electric charge. Both entries are scalar fields, not fermions: “doublet” describes their internal weak-isospin transformation, not spatial spin. This is the minimal suitable scalar content; larger scalar sectors are possible. A doublet with $Y=-1$ and a neutral upper entry would be the conjugate description.

To obtain a nonzero vacuum value, use the same potential as in the earlier example, replacing $\phi^*\phi$ by the sum of the two component magnitudes:

$$V=-\mu^2\phi^\dagger\phi+\lambda(\phi^\dagger\phi)^2,
\qquad \phi^\dagger\phi=|\phi^+|^2+|\phi^0|^2,
\qquad \mu^2,\lambda>0.$$

The potential is gauge invariant because these transformations preserve $\phi^\dagger\phi$. Its minimum fixes $\phi^\dagger\phi=\mu^2/(2\lambda)=v^2/2$. We choose a gauge in which the vacuum is real and lies in the lower component:

$$\langle\phi\rangle=\frac1{\sqrt2}\begin{pmatrix}0\\v\end{pmatrix}.$$

This orientation is a choice of description. Rotating the scalar and gauge fields together does not change the masses. In this basis, the electromagnetic transformation leaves the vacuum unchanged because its nonzero component has charge zero. The other three independent electroweak transformation directions change the vacuum's component values.

<details>
<summary>Checking which transformation leaves the vacuum unchanged</summary>

A generator $G$ preserves the vacuum under every transformation $e^{i\alpha G}$ when $G\langle\phi\rangle=0$. For $Y=1$,

$$Q=T^3+\frac Y2 I=\begin{pmatrix}1&0\\0&0\end{pmatrix},
\qquad Q\langle\phi\rangle=0.$$

The two diagonal contributions cancel on the lower entry. By contrast, $T^1$ and $T^2$ generate an upper component, while $T^3-YI/2=\operatorname{diag}(0,-1)$ changes the lower component. There are therefore three independent broken directions and one unbroken direction, generated by electric charge.

</details>

The doublet contains four real scalar degrees of freedom. Three supply the longitudinal polarizations of $W^+,W^-,Z$, just as one scalar phase supplied the longitudinal polarization in the $U(1)$ example. One scalar excitation remains. In unitary gauge,

$$\phi(x)=\frac1{\sqrt2}\begin{pmatrix}0\\v+h(x)\end{pmatrix}.$$

The constant $v$ specifies the vacuum; quanta of the fluctuating field $h$ are **Higgs bosons**. Expanding the potential gives $m_h^2=2\lambda v^2$, by the same calculation as in the first section. We will now use this one expression for $\phi$ twice: in its coupling to the electron, then in its own kinetic term.

## Fermion Masses

An electron mass term connects its left- and right-chiral parts:

$$-m_e\bar e e=-m_e(\bar e_Le_R+\bar e_Re_L).$$

EW showed why we cannot insert this term directly: $e_L$ belongs to $L=(\nu_{eL},e_L)^T$ with hypercharge $-1$, while $e_R$ is a singlet with hypercharge $-2$. Their transformation factors do not cancel. The Higgs doublet can provide the missing factor.

Consider the interaction

$$\mathcal L_{\mathrm{Yukawa}}=-y_e\bar L\phi e_R+\text{Hermitian conjugate}.$$

A coupling of a scalar to two fermion fields is called a **Yukawa coupling**. Here $y_e$ is its dimensionless strength. For this one-electron example, we choose field phases so that $y_e$ is real and positive. The Hermitian conjugate adds $-y_e\bar e_R\phi^\dagger L$.

This interaction respects the electroweak symmetry. The hypercharges add to zero, $+1+1-2=0$, so their phase factors cancel. Under $SU(2)_L$, $\bar L\to\bar L U^\dagger$ and $\phi\to U\phi$, so the matrices cancel in $\bar L\phi$ as well.

Substitute the unitary-gauge Higgs field. Multiplying the row and column selects the electron component:

$$\bar L\phi=(\bar\nu_{eL},\bar e_L)
\frac1{\sqrt2}\begin{pmatrix}0\\v+h\end{pmatrix}
=\frac{v+h}{\sqrt2}\bar e_L.$$

The interaction separates into two terms:

$$\mathcal L_{\mathrm{Yukawa}}
=-\underbrace{\frac{y_ev}{\sqrt2}}_{m_e}\bar e e
-\frac{y_e}{\sqrt2}h\bar e e.$$

The first is the electron mass term. The second describes an interaction with a Higgs boson. Thus

$$m_e=\frac{y_ev}{\sqrt2},\qquad
\mathcal L_{hee}=-\frac{m_e}{v}h\bar e e.$$

The vacuum value produces the mass even when there are no Higgs particles present. Exciting $h$ gives a particle whose coupling to the electron is fixed by that same mass. The mass term arose from an invariant interaction; we did not insert a term that violates the original gauge symmetry.

Other charged fermions have analogous Yukawa interactions. Their masses depend on independent coupling parameters, so the mechanism does not predict their numerical masses. It predicts a relation: the Higgs coupling to a charged fermion is proportional to $m_f/v$. We retain the earlier massless-neutrino approximation; explaining neutrino masses requires extending this construction.

<details>
<summary>The corresponding construction for quarks</summary>

For $Q_L=(u_L,d_L)^T$, the Higgs doublet selects $d_L$ just as it selected $e_L$. To select $u_L$, use the conjugate doublet

$$\widetilde\phi=i\sigma^2\phi^*
=\begin{pmatrix}\phi^{0*}\\-\phi^-\end{pmatrix},
\qquad \phi^-=(\phi^+)^*.$$

It has hypercharge $-1$ and vacuum value $(v,0)^T/\sqrt2$. The interactions

$$-y_d\bar Q_L\phi d_R-y_u\bar Q_L\widetilde\phi u_R+\text{Hermitian conjugate}$$

give $m_d=y_dv/\sqrt2$ and $m_u=y_uv/\sqrt2$. With several generations, Yukawa couplings become matrices connecting the fermion families. After choosing fields with definite masses, the charged-current interactions contain the quark mixing described in WI. That additional matrix calculation is not needed for the electron example above.

</details>

## Gauge Boson Masses

The electron mass came from its Yukawa interaction. The gauge-boson masses come from a different term, the Higgs field's kinetic term:

$$(D_\mu\phi)^\dagger D^\mu\phi,
\qquad D_\mu=\partial_\mu+igT^aW_\mu^a+i\frac{g'}2B_\mu.$$

The hypercharge is $Y=1$. As in EW, $g$ and $g'$ are the shared gauge coupling strengths, while $T^a$ and $Y/2$ specify how this particular scalar couples.

At the constant vacuum, $\partial_\mu\langle\phi\rangle=0$. But the gauge-field terms in $D_\mu\langle\phi\rangle$ remain. Squaring them produces terms quadratic in gauge fields, with no derivatives: precisely the form of vector mass terms. The result is

$$\mathcal L_{\mathrm{mass}}=\frac{v^2}{8}\left[
g^2(W^1_\mu W^{1\mu}+W^2_\mu W^{2\mu})
+(gW^3_\mu-g'B_\mu)(gW^{3\mu}-g'B^\mu)\right].$$

<details>
<summary>Multiplying the covariant derivative by the vacuum doublet</summary>

Using $T^a=\sigma^a/2$, the gauge part of the derivative is $i$ times

$$\frac12\begin{pmatrix}
gW^3_\mu+g'B_\mu & g(W^1_\mu-iW^2_\mu)\\
g(W^1_\mu+iW^2_\mu)&-gW^3_\mu+g'B_\mu
\end{pmatrix}.$$

Only its second column contributes when acting on the vacuum:

$$D_\mu\langle\phi\rangle=\frac{iv}{2\sqrt2}
\begin{pmatrix}g(W^1_\mu-iW^2_\mu)\\-gW^3_\mu+g'B_\mu\end{pmatrix}.$$

Multiply its adjoint by $D^\mu\langle\phi\rangle$. The factor is $v^2/8$, and the upper-component product gives $g^2(W^1_\mu W^{1\mu}+W^2_\mu W^{2\mu})$. The lower-component product gives the neutral term above. All spacetime indices are contracted with the Minkowski metric.

</details>

For the charged fields, use the combinations already defined in WI,

$$W^\pm_\mu=\frac{W^1_\mu\mp iW^2_\mu}{\sqrt2}.$$

Since $W^1_\mu W^{1\mu}+W^2_\mu W^{2\mu}=2W^+_\mu W^{-\mu}$, the charged part becomes

$$\mathcal L_{\mathrm{mass}}^{\mathrm{charged}}
=\frac{g^2v^2}{4}W^+_\mu W^{-\mu}.
\qquad\boxed{m_W=\frac{gv}{2}.}$$

We matched its coefficient to $m_W^2W^+_\mu W^{-\mu}$. A real vector instead has the mass term $\tfrac12m^2V_\mu V^\mu$, as in the $U(1)$ example. The charged expression combines two real fields, accounting for the different factor.

For the neutral fields, the squared combination contains both $W^3$ and $B$, including a mixed product. We need fields with separate mass terms. This is another use of the **change of field basis** from EW, now to identify fields of definite mass:

$$Z_\mu=\frac{gW^3_\mu-g'B_\mu}{\sqrt{g^2+g'^2}},
\qquad A_\mu=\frac{g'W^3_\mu+gB_\mu}{\sqrt{g^2+g'^2}}.$$

These are exactly the photon and $Z$ combinations previously selected by their couplings, because $\tan\theta_W=g'/g$. Substitute $gW^3-g'B=\sqrt{g^2+g'^2}\,Z$ into the neutral mass term:

$$\mathcal L_{\mathrm{mass}}^{\mathrm{neutral}}
=\frac{(g^2+g'^2)v^2}{8}Z_\mu Z^\mu
=\frac12m_Z^2Z_\mu Z^\mu.$$

There is no $A_\mu A^\mu$ term. Therefore

$$\boxed{m_Z=\frac v2\sqrt{g^2+g'^2},\qquad m_A=0.}$$

This completes the step left open in EW: the combinations with photon and $Z$ interactions also have definite masses, and the photon is massless. Its absence from the mass term agrees with the earlier symmetry check, $Q\langle\phi\rangle=0$.

The same vacuum value appears in both masses. Dividing cancels it:

$$\frac{m_W}{m_Z}=\frac{g}{\sqrt{g^2+g'^2}}=\cos\theta_W.$$

This is a tree-level relation between measurable quantities, not a numerical prediction without experimental input. Quantum corrections must be included for precision comparisons. The Higgs vacuum value itself follows from the measured Fermi constant in WI:

$$\frac{G_F}{\sqrt2}=\frac{g^2}{8m_W^2}
=\frac{1}{2v^2},
\qquad v=(\sqrt2G_F)^{-1/2}\approx246\ \text{GeV}.$$

Once $v$ is known, the measured Higgs mass fixes $\lambda$ through $m_h^2=2\lambda v^2$. Neither the scalar potential parameters nor the Yukawa couplings receive numerical values from the mechanism alone.

We now have massive $W^\pm$ and $Z$, a massless photon, and a massive electron, all from interactions that respect the original electroweak gauge symmetry. Three scalar degrees of freedom supply the massive vectors' longitudinal polarizations; the fourth is the physical Higgs field $h$. The vacuum value generates masses, while fluctuations about it describe Higgs particles. The next [Standard Model](standard-model.md) chapter places these results alongside the remaining particles and interactions.
