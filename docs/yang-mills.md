---
sidebar: false
prev: false
next: false
---

# Yang–Mills Fields and Self-Interactions

This optional derivation extends [Weak Interaction](weak-interaction.md#yang–mills-fields-and-self-interactions). The main page explains how local SU(2) introduces three gauge fields and their couplings to fermions. Here we construct the terms that let those fields propagate and show why the gauge fields also interact with one another. These self-interactions do not enter the leading beta-decay diagram.

We use the same conventions: $D_\mu=\partial_\mu+igW_\mu$, $W_\mu=W_\mu^aT^a$, and $T^a=\sigma^a/2$. The matrices act on the two species in a doublet, and repeated generator indices run over $1,2,3$. The charged combinations are $W_\mu^\pm=(W_\mu^1\mp iW_\mu^2)/\sqrt2$. We use $\hbar=c=1$.

## Constructing the field strength

In QED we used the electromagnetic field strength $F_{\mu\nu}$. For $SU(2)$, the commutator of covariant derivatives transforms as $[D'_\mu,D'_\nu]=U[D_\mu,D_\nu]U^{-1}$. We can therefore extract a field strength with the same transformation law and use it to construct an invariant kinetic term:

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

Unlike the photon field strength, the weak field strength includes products of gauge fields. The field strength contains a derivative term linear in $W$ and a term quadratic in $W$. Squaring it produces three kinds of terms:

| Terms in the Lagrangian | Role in perturbation theory |
| --- | --- |
| Quadratic in $W$ | Free gauge-field propagation |
| Cubic in $W$, proportional to $g$ | Three-gauge-boson vertices |
| Quartic in $W$, proportional to $g^2$ | Four-gauge-boson vertices |

Thus the gauge bosons interact directly with one another. The Maxwell Lagrangian is quadratic in the photon field and has no such vertices. Photon scattering through charged-particle loops is a separate effect. For a more general derivation of the Yang–Mills kinetic term and these vertices, see [Tong, *Symmetries*, §1.3.3](https://davidtong.org/pdfs/teaching/standard-model/standardmodel1.pdf).

These are the $SU(2)_L$ gauge fields before electroweak mixing. The neutral field $W^3$ is not yet the physical $Z$ boson. Its relation to the $Z$ and photon belongs to [Electroweak Unification](electroweak-unification.md).

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

Return to [the low-energy beta-decay calculation](weak-interaction.md#connecting-w-exchange-to-the-decay-strength).
