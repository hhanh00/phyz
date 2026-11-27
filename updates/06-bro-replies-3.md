# Chapter 6 (dirac-equation.md), bro test, round 3

Main text only, intro and sections 1 to 9. Reader has chapters 1, 2a, 2b, 3, 4, 5.

## Intro

**Bro version.** Ok so last chapter left us with a column of four wave functions, two with energy plus and two with energy minus, and nobody said what separates the two of each sign. Basically the answer is spin, and the wild part is that nobody put spin into the equation. You also get two freebies: the equation tells you how strong the electron's magnet is, and it says that turning an electron once round doesn't give you the same state back. After that the chapter gets the electron moving, matches each negative-energy solution with a positron, and writes the big sum of waves the next chapter needs. The table is the cheat sheet: ψ1 and ψ2 are the electron up and down, ψ3 and ψ4 are the positron, with its spin the opposite of the entry's.

**Added:** nothing.

**Dropped:** nothing.

**Why? with no answer:** nothing. "Section 8 explains the flip" is an honest pointer.

**Flags:** nothing.

## 1. A puzzle: a magnet twice too strong

**Bro version.** Ok so charge going in a circle is a current loop, and a current loop is a magnet, so anything charged that spins is a magnet. It also has angular momentum, and since both double when you spin it twice as fast, their ratio is fixed: magnet strength = q/2m times angular momentum. Stern and Gerlach's plate tells you two things. The gap between the spots gives the magnet's strength, eħ/2m. The number of spots gives the angular momentum: results come in steps of ħ, they sit evenly either side of zero, and two of them one step apart can only be +ħ/2 and −ħ/2. Now plug ħ/2 into the rule and you get eħ/4m, half of what's measured. If you instead want the measured strength from the rule you need a whole ħ, but that gives three spots, not two. So the count says ħ/2 and the gap says ħ, and people just bolted on a factor of two until Dirac.

**Added:** nothing I couldn't get from the page or chapter 2a. The step "results come in steps of ħ" is on trust from the box, and the page says so.

**Dropped:** nothing.

**Why? with no answer:**
- "Here $m$ is the mass of the electron, because the silver atom's magnet is that of one of its electrons." Why only one electron, when silver has 47? One clause would do (the others pair off and cancel), or say plainly it is taken on trust. Chapter 2a states it the same bare way, so this is a small one.

**Flags:**
- "The rule for a spinning charge can't produce both." The rule was stated only for a body "with the charge spread through it the same way as the mass". A reader can ask: what if the charge sits further out than the mass? The spinning-ball box answers a different objection (the speed). Small.

## 2. Four wave functions and one question

**Bro version.** Basically this is a recap with the matrices shown. The Dirac equation is the Schrödinger pattern, iħ times the rate of change equals Ĥψ, with Ĥ = c(α_x p_x + α_y p_y + α_z p_z) + βmc². The four matrices are four-by-four, made of two-by-two blocks, and the blocks are the three spin matrices. β keeps the upper pair (ψ1, ψ2) and the lower pair (ψ3, ψ4) apart, and each α swaps the pairs. For a particle at rest all the slopes are zero, so only βmc² is left, and it gives +mc² to the upper pair and −mc² to the lower pair. So ψ1 and ψ2 have the same energy and the same momentum, and the question is what measurement tells them apart, the way a vertical magnet tells up from down.

**Added:**
- "A particle at rest has a wave function that is the same at every point". I had to recall from chapter 2a that momentum is how fast the phase turns per metre, so zero momentum means no turning at all. The page jumps straight to "so every slope is zero".

**Dropped:** nothing.

**Why? with no answer:** nothing.

**Flags:**
- "These four meet chapter 5's conditions, each squaring to 1 and every pair anticommuting, because the spin matrices inside them do." That covers the three α's with each other. β anticommutes with each α for a different reason (β has opposite signs on the two pairs and each α swaps the pairs). Small, and the reader is unlikely to check.

## 3. Angular momentum that isn't kept

**Bro version.** Ok so there's a rule from chapter 2b: if an operator commutes with Ĥ, its quantity never changes. Call that "kept". Angular momentum about the vertical axis is L_z = x p_y − y p_x, distance from the axis times momentum, like the pendulum's. For a free particle it should be kept, because nothing cares which way the whole thing is turned. But work out the commutator with Dirac's Ĥ and you get iħc(α_x p_y − α_y p_x), which isn't zero. The reason is that turning the motion mixes p_x and p_y, but α_x and α_y sit on the column and don't get turned, so Ĥ changes. The fix is a second piece that acts only on the column: ħ/2 times Σ_z, which is the spin matrix Ẑ copied onto both pairs. Its commutator with Ĥ is exactly minus the first one, so the sum is kept. That extra piece is an angular momentum the electron has even at rest, and that's the spin.

**Added:** nothing essential.

**Dropped:** nothing.

**Why? with no answer:**
- "Chapter 1's argument has a quantum form: $\hat L_z$ commutes with $\hat H$ exactly when $\hat H$ looks the same after the particle's motion is turned about the vertical axis." Bro, why? This is the hinge of the "Why" paragraph and it is asserted. Either mark it as taken on trust, or give one line (the commutator with L̂_z is the rate at which a thing changes as you turn it, the way the commutator with p̂_x is a slope).
- "So it is an angular momentum too." The reason given ("the two add to a total that is kept") is followable, so this passes. Just noting it is the thinnest step in "What that means".

**Flags:**
- "Chapter 1 found that when the energy doesn't depend on a coordinate, that coordinate's momentum never changes." Chapter 1 said this of $L$ ("Suppose $L$ doesn't depend on some coordinate at all"), not of the energy. True either way, but the words don't match the earlier chapter.
- "So the commutator with $\Sigma_z$ turns $\alpha_x$ into $\alpha_y$ and $\alpha_y$ into $\alpha_x$" drops the minus sign in the second one. Fine for the gist.

## 4. Spin up and spin down

**Bro version.** A measurement gives an eigenvalue, and (ħ/2)Σ_z just multiplies ψ1 and ψ3 by +ħ/2 and ψ2 and ψ4 by −ħ/2. So spin along the vertical is +ħ/2 or −ħ/2, spin up or spin down. Chapter 2b called those +1 and −1 in units it left open, and the unit turns out to be ħ/2. That answers section 2: inside each pair, the first entry is up and the second is down, so energy picks the pair and spin picks the entry. Sideways works the same with two copies of Ŝ, whose eigenvalues are also ±1. So each pair is chapter 2a's list of two amplitudes, except each amplitude is now a whole wave function.

**Added:** nothing.

**Dropped:** nothing.

**Why? with no answer:** nothing. "a tilted direction works the same way" is bare but nobody will trip on it.

**Flags:** nothing. This section is clear.

## 5. The strength of the magnet

**Bro version.** Ok so a magnet shows up in an equation as an energy: lined up with a field B, a magnet of strength μ has its energy lowered by μB. To put a field into the equation you swap each p_x for p_x − qA_x, where A is a field of arrows that circles the field direction, and the page says to take that on trust. For a slow electron the lower pair is tiny but you can't drop it, because each α sends one pair to the other. So you solve for the lower pair, put it back, and the momentum term has acted twice. The energy that comes out is mc² + p²/2m, minus (q/2m) L_z B, minus (q/2m) ħẐ B. The third term is the magnet of the motion, with section 1's ratio q/2m. The fourth is the spin's magnet: it has ħẐ in it, which is ±ħ, a whole ħ, while the spin's angular momentum is only ħ/2. Same magnet, half the angular momentum, so the ratio is q/m, twice section 1's. For the electron that's eħ/2m, the measured value, give or take a tenth of a percent that the field theory explains later.

**Added:**
- Why the motion's term has L_z in it. The page says the arrows of A "circle the vertical axis" and then L_z is in the formula. I had to guess that a field of arrows going round the axis, multiplied into the momentum, picks out the momentum going round the axis. The main text never says it.

**Dropped:**
- "whose swirl is the magnetic field". I kept "arrows that circle the vertical axis" and dropped "swirl", which the main text doesn't explain.
- "So the field treats $\hbar\hat Z$ exactly as it treats $L_z$, with the same $q/2m$ in front (box)." It opens with "So" but doesn't follow from the ratio above it. It repeats what the formula already shows.

**Why? with no answer:**
- "We have left out one more term, which has the square of $B$ in it and is far smaller for the fields of a laboratory." Far smaller why, and for which electron? One clause with a number would do (for an electron held in an atom at one tesla it is about a millionth of the others).
- "So in the field, spin up counts as a whole $\hbar$, though as an angular momentum it is only $\hbar/2$." This is the whole puzzle, and the reader asks: why does the field see a whole ħ? "The two comes from section 3" then explains why the angular momentum is ħ/2, which I already knew. Why the field term has no ½ is only in the box. One sentence would satisfy: the momentum term acted twice, each time bringing a spin matrix, and two different spin matrices multiply to one whole spin matrix with no ½ (box).

**Flags:**
- The energy formula mixes kinds: "$E = mc^2 + \frac{p^2}{2m} - \frac{q}{2m}L_zB - \frac{q}{2m}\hbar\hat Z B$" has a hat on Ẑ and none on L_z or p, and E on the left looks like a number. The next lines read Ẑ as "+1 for spin up and −1 for spin down", so the reader copes.
- "Nothing was assumed." The replacement p_x − qA_x was taken on trust four paragraphs up. Meant is "no factor of two was assumed".
- Read three times: "The two comes from section 3: the angular momentum that goes with $\hat Z$ is $\tfrac{\hbar}{2}\hat Z$, half of $\hbar\hat Z$, because the spin matrices' two orders differ by twice a spin matrix."

## 6. One full turn flips the sign

**Bro version.** Ok so a field gives a way to turn a spin, and that shows what a turn does to the column. From section 5, a spin value s (+ħ/2 up, −ħ/2 down) has energy −(q/m) s B. A state of energy E turns its phase as e^{−iEt/ħ}, so after time t each phase has turned by (q/m)Bt times s/ħ. Call (q/m)Bt θ: the up amplitude turns by +θ/2 and the down one by −θ/2. The angle between the two arrows changes by θ, and chapter 2a said that angle is which way the atom leans, so the spin has been turned by θ while each amplitude turned by only half of that. Turn by 360° and each amplitude has turned 180°, which is times −1, so the state is minus what it was, and you need 720° to get it back. A minus sign on the whole state changes no chance, so to see it you split a beam, turn the spins in one half only, and bring the halves back together. Two groups did that with neutrons in 1975, and the count came back only at 720°.

**Added:** nothing. The reference-beam paragraph answered the question I was about to ask (who says the shared phase is real?).

**Dropped:** nothing.

**Why? with no answer:**
- "So the lean has swung round by $\theta$, and every direction the spin could point in has been carried round the vertical by $\theta$ with it." The first half follows from chapter 2a. The second half is asserted. Small: a clause like "the same θ for whatever state the spin starts in" would cover it.

**Flags:**
- "so the angle between them has grown by $\theta$". With up at +θ/2 and down at −θ/2, the down arrow falls behind the up arrow. Chapter 2a measures the lean by the down arrow's angle relative to up, so in that convention it has shrunk by θ. Chapter 2b's box has the same thing as $e^{-i\varphi}$ on the down amplitude, so the two agree in fact. "changed by θ" would be safer than "grown".
- The formula θ = (q/m)Bt can't be used for the neutron (q = 0). The page handles it ("at a rate set by its own magnet"), so no contradiction, just don't expect the reader to compute the neutron's angle.

## 7. A moving electron

**Bro version.** So far the electron sat still. Give it momentum p along z, and the α term in Ĥ is no longer zero. α_z sends the first entry to the third, so the lower pair can't stay empty: the third row of the equation says (E + mc²)ψ3 = pc ψ1. So the solution is the column (1, 0, r, 0) times the usual wave, with r = pc/(E + mc²). Put in p = γmv and E = γmc² and the mass cancels, so r depends only on the speed: 0.005 at a hundredth of light speed, 0.87 at 0.99c. The share of the chance in the lower pair is r²/(1 + r²), tiny when slow and nearly half near light speed. Moving along z keeps the spin exactly up, because α_z is built from Ẑ. Moving along x gives (1, 0, 0, r), an up entry and a down entry, so a definite energy no longer means a definite spin.

**Added:**
- Where "(E + mc²)" comes from. I had to write the third row myself: E ψ3 = pc ψ1 − mc² ψ3, the −mc² being β's entry on the lower pair, then move it across. The page gives only the result.

**Dropped:** nothing.

**Why? with no answer:**
- "So the third row of the equation ties the two together: $(E + mc^2)\,\psi_3 = pc\,\psi_1$." Which equation, and why a plus? One line would do: for a wave of energy E the equation reads Eψ = (c α_z p + βmc²)ψ, and its third row is Eψ3 = pcψ1 − mc²ψ3.

**Flags:**
- "the upper pair fills in with the same ratio $r$". For the same momentum it is −r (the box has the minus sign). Size is right.

## 8. Electron and positron

**Bro version.** Ok so the negative-energy solutions are left over. The point is that each one can be converted into a positive-energy solution for a particle of opposite charge. Step one: take the complex conjugate, which swaps i for −i, changes no chance, and turns a wave of momentum p and energy −E into one of momentum −p and energy +E. Step two: ask what equation the conjugated column obeys. The time term and the slope terms each carry an i, so they flip sign, and the mass term doesn't, so it's now out of step. A fixed matrix fixes that by swapping the upper and lower pairs, which flips the mass term, and by swapping up and down inside each pair. Meanwhile p_x − qA_x has become −(p_x + qA_x), because A is real and doesn't flip. So every term has the same minus sign, you cancel it, and what's left is the Dirac equation with +q where −q was. Energy, momentum, spin and charge are all reversed and the mass isn't, which is exactly what a hole (a missing electron) would have. That's the positron.

**Added:** nothing essential.

**Dropped:**
- "That undoes the $i$ in $\hat Y$." I couldn't see how swapping up with down undoes an i, so I just said the matrix swaps up and down.

**Why? with no answer:**
- "Inside each pair it swaps spin up with spin down, with a change of sign. That undoes the $i$ in $\hat Y$." Why would a swap undo an i? One line: the reshuffle leaves α_x and α_z as they are and changes the sign of α_y, which cancels the extra sign α_y picked up from its own i.
- "with the same chances at every point". Conjugation keeping lengths is explained. That the fixed matrix keeps them is not said (it only moves entries around and changes signs, so the sum of squared lengths is the same). One clause.

**Flags:**
- Table row "Momentum with the field": "Sign flipped, and $-qA_x$ has become $+qA_x$". I had to read it against the displayed line above to see that the whole term flips and, inside it, the charge term flips relative to the slope. It is correct.

## 9. The general solution

**Bro version.** Basically the Dirac equation is linear, so if two columns solve it, their sum does too. So take section 7's wave for every momentum, both spins and both signs of the energy, multiply each by a number saying how much of it there is, and add them all. That's the big formula: the u terms are the positive-energy waves, with a_s(p) in front, and the v terms are the negative-energy waves, with b*_s(p) in front. From here on c = 1. The v wave is written e^{+ip·x/ħ}, which on its own has energy −E_p and momentum −p, and by section 8 that is a positron with energy +E_p and momentum +p. So the p in v_s(p) is the positron's momentum. The s isn't relabelled, so the positron's spin is the opposite of what s says: v_1 goes with a spin-down positron. The star on b is only a name for now, there so the formula keeps its shape when a and b become operators next chapter.

**Added:** nothing.

**Dropped:**
- "$\int \frac{d^3p}{(2\pi\hbar)^3}\,\frac{1}{\sqrt{2E_p}}$": I kept "sum over all momenta" and the page's word that the factors are conventions.

**Why? with no answer:** nothing. Conventions are stated as conventions.

**Flags:**
- "as chapter 5's last section promised for the negative-energy waves". Chapter 5's last section is section 11, the notation box. The promise ("They describe the creation of antiparticles") is in chapter 5's section 10.
- "$v_s(p)$ | Section 7's negative-energy column for momentum $-\mathbf p$". Section 7's main text never shows a negative-energy column, only says "the lower pair is the larger and the upper pair fills in with the same ratio r". The reader can't check this row without the box.
