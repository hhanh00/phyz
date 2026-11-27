# Bro test, chapter 6 (The Dirac Equation), run 2

Reader: has read chapters 1, 2a, 2b, 3, 4, 5 (main text; boxes only where chapter 6 leans on them). High-school maths. Main text of chapter 6 only, sections intro to 9.

## Intro

**Bro version.** Ok so last chapter left us with Dirac's equation and a state that is four wave functions stacked in a column. Two have positive energy, two have negative energy, and nobody said what the difference is between the two that share a sign. This chapter says the difference is the electron's spin, and the wild part is that nobody put spin in, it just falls out. Two bonus results come with it: the equation gets the strength of the electron's magnet right, and it says that turning an electron once round doesn't put its state back. After that the chapter makes the electron move, matches each negative-energy solution with a positron, and writes the big sum of waves the next chapter needs. The table is the cheat sheet: entries 1 and 2 are the electron spin up and spin down, entries 3 and 4 are the positron, with its spin the opposite of the entry's.

**Added:** nothing.

**Dropped:** nothing.

**Why? with no answer:** nothing. The intro is a roadmap and every claim is tagged with the section that pays it off.

**Flags:** nothing.

## 1. A puzzle: a magnet twice too strong

**Bro version.** Basically, a charge going round in a circle is a little current loop, and a current loop is a magnet. Anything with mass going round also has angular momentum, which is how much turning motion it carries. Spin it faster and both go up together, so the magnet strength is a fixed multiple of the angular momentum, and the multiple is q/2m. Now look at the Stern and Gerlach plate from chapter 2a. The number of spots, two, says the electron's own angular momentum is ħ/2. The gap between the spots measures the magnet, and it comes out as eħ/2m. Put ħ/2 into the rule and you get eħ/4m, half of what was measured. A whole ħ would fix the gap but would give three spots. So the rule can't give both, and physicists just bolted on a factor of two with no reason. That's the puzzle.

**Added:**
- That the two values have to be symmetric about zero because nothing makes "up" different from "down". The page only says "placed evenly either side of zero" and never says why evenly.
- That the m in the answer is the electron's mass and not the silver atom's. The page says "Put ħ/2 into the rule above, with the electron's charge e" but the thing flying through the magnet is a whole atom.

**Dropped:**
- "By 1925 physicists had learned from the light of atoms that angular momentum along a chosen direction comes in steps of ħ". I repeated it as a fact. "From the light of atoms" tells me nothing I can picture, and the reason is in a box.

**Why? with no answer:**
- "μ = q/2m × angular momentum". The sentence before only shows the ratio is fixed, not that it is q/2m. One line would do it: the 2 comes from the loop's area πr² against its rim 2πr, and the box does the sum.
- "angular momentum along a chosen direction comes in steps of ħ (second box)". Wanted: one plain sentence, such as "a wave going round a circle must join up with itself, so only whole numbers of wavelengths fit".
- "Two results, one step apart and placed evenly either side of zero, have to be +ħ/2 and −ħ/2." Wanted: why evenly either side of zero.
- "a whole ħ would give three results, +ħ, 0 and −ħ". Follows from steps of ħ plus symmetry, but only if the symmetry is stated.
- "a force equal to the strength of the atom's magnet times how fast the field grows from one pole to the other". Asserted. Chapter 2a gave the picture (one end pulled harder), so I let it pass, but the "times" is new.

**Flags:**
- The page says steps of ħ come from experiment, then proposes ħ/2. A reader wonders whether half a step is even allowed. The main text never says "steps of ħ fix the spacing, not the starting point".
- Figure `magnet-twice-too-strong.png` agrees with the text and is clear.

## 2. Four wave functions and one question

**Bro version.** Ok so here is the Dirac equation in full space. It has the same shape as Schrödinger's, iħ times the rate of change equals the energy operator on the state, but the energy operator is now c times a matrix in front of each part of the momentum, plus another matrix times mc². The four matrices are four-by-four tables made of two-by-two blocks, and the blocks are the three spin matrices from before. Because of the blocks, think of the column as an upper pair and a lower pair. β keeps each pair to itself, and each α sends upper to lower and back. For a particle at rest only the β part is left, and it gives the upper pair energy +mc² and the lower pair −mc². So ψ1 and ψ2 have the same energy and the same momentum, and energy and momentum can't tell them apart. The question is what measurement can.

**Added:**
- That "at rest" for a wave function means it is the same at every point in space, so every slope is zero and the momentum operators give zero. The page says "For a particle at rest the momentum is zero" as if momentum were still a number.
- That these four matrices really do meet chapter 5's conditions (each squares to 1, every pair anticommutes). The page shows them and moves on.

**Dropped:** nothing.

**Why? with no answer:**
- "The four matrices are ..." Wanted: one sentence saying they pass chapter 5's test, with one pair checked, or a pointer to where it is checked. Chapter 5 only promised them.
- "Each α has its blocks off the diagonal, so it sends the upper pair to the lower and the lower to the upper." Wanted: one small worked line, for example α_z acting on (ψ1, ψ2, ψ3, ψ4) gives (ψ3, −ψ4, ψ1, −ψ2). A high-school reader doesn't see it from "off the diagonal".

**Flags:**
- Ŷ has an i in it. The page says "Chapter 5 showed Ŷ only in a box" and nothing more. A reader who skipped that box meets a measurable magnet with imaginary entries and gets no comment.

## 3. Angular momentum that isn't kept

**Bro version.** The point is, there's a rule from chapter 2b: if a quantity's operator commutes with the energy operator, that quantity never changes. Call it "kept". Angular momentum about the vertical axis is distance from the axis times the momentum that carries you round, which works out to x·p_y − y·p_x. For a free particle it should be kept, because a free particle has the same energy whichever way you turn it, just like momentum is kept when the energy doesn't care where you are. For Schrödinger's free particle it is kept. For Dirac's it isn't: the commutator comes out as something that isn't zero. The reason given is that Dirac's energy operator glues α_x to p_x and α_y to p_y, so turning the motion without turning the column changes it. So you look for a second piece that acts only on the column and cancels the leftover. That piece is ħ/2 times two copies of Ẑ, and the ħ/2 is forced. The sum is kept, the new piece is an angular momentum the electron has even at rest, and that's the spin.

**Added:**
- That L_z turns into an operator by putting hats on x, y, p_x, p_y (chapter 2b's rule). The page goes from "L_z = x p_y − y p_x" to "[L̂_z, Ĥ]" without saying so.
- That the fixed matrices commute with the momentum operators because they shuffle the column's entries while the slopes act on where the particle is. The page says "those all commute with p̂_x" with no reason.
- Why Ẑ is the one to try: it is the spin matrix for the vertical axis, and the turn is about the vertical axis. The page says "Take two copies of Ẑ".

**Dropped:**
- "and L̂_z leaves the column alone." I could not connect it. The paragraph talks about "a turn of the motion", and nothing told me that L̂_z is the thing that does the turning. Chapter 1 said a symmetry gives a kept momentum, not that the momentum performs the shift.

**Why? with no answer:**
- "For a particle going round a circle of radius r with momentum p, this comes to r p wherever the particle is on the circle." Wanted: one check, for example the particle at the top of the circle.
- "The coordinate is the angle of the turn, and its momentum is the angular momentum L_z." Wanted: a nod to chapter 1's pendulum, where the angle's momentum was mℓ²θ̇.
- "For the free Schrödinger equation it is." Wanted: one line, such as "its energy has only p_x² + p_y² + p_z², which a turn doesn't change".
- "[L̂_z, Ĥ] = iħc(α_x p̂_y − α_y p̂_x)". Appears whole. Wanted: one sentence on where it comes from, such as "x̂ fails to commute only with p̂_x, which pulls out the α_x and leaves p̂_y".
- "Its commutator with Ĥ is exactly minus the first one." Wanted: the one fact behind it, that Ẑ with Ŝ in the two orders differs by 2i Ŷ, which swaps α_x and α_y.
- "The new piece has to be added to an angular momentum to make a total that is kept, so it is itself an angular momentum." I can repeat it, but "you add it to one, so it is one" needs a half sentence, for example that it has the same units and is what the turn does to the column.

**Flags:**
- Read three times: "So turning the motion alone changes Ĥ. The energy stays the same only if the column is turned too, and L̂_z leaves the column alone."
- "and has it even at rest, where L_z is zero" is fine but silent on why L_z is zero at rest (p = 0).
- Figure `angular-momentum-parts.png` agrees with the text and is clear.

## 4. Spin up and spin down

**Bro version.** Ok so a measurement gives one of the operator's eigenvalues, and this operator is a table with ħ/2 times 1, −1, 1, −1 down the diagonal. So the spin along the vertical is +ħ/2 or −ħ/2, spin up or spin down. Chapter 2b called those +1 and −1 in units it left open, and the unit turns out to be ħ/2. That's the size Uhlenbeck and Goudsmit guessed, and it's why the electron is called spin one half. So in each pair of the column the first entry is spin up and the second is spin down, which answers section 2. Sideways works the same with two copies of Ŝ, and its eigenstates are equal mixes of up and down, like right and left in chapter 2a. So each pair is the old list of two amplitudes, except each amplitude is now a whole wave function. Chapter 5's column of two was not a spin, it was the two signs of the energy; in space the energy picks the pair and the spin picks the entry.

**Added:** nothing of substance.

**Dropped:** nothing.

**Why? with no answer:**
- "and the two results are the two spots on Stern and Gerlach's plate." The plate sorts atoms by their magnet, and the magnet isn't tied to this operator until section 5. Wanted: "section 5 shows the magnet points along this spin".
- "The spin along any direction is +ħ/2 or −ħ/2." Only vertical and sideways are shown. Wanted: "a tilted direction works the same way" or soften "any".

**Flags:**
- Figure `rest-spinor-basis.png` agrees with the text. It writes 1 and 0 in the boxes while the text says each entry is a wave function; small, and the caption "one entry of the column filled" covers it.
- This section is clear.

## 5. The strength of the magnet

**Bro version.** Basically, a magnet shows up in an equation as an energy: lined up with a field B its energy drops by μB, lined up against it the energy goes up by μB. To put a magnetic field into the equation of a charged particle you swap each bit of momentum for momentum minus q times a thing called A that describes the field. Do that for a slow, positive-energy electron in a field pointing up. The lower pair is almost empty at low speed, so you can get rid of it and keep an equation for the upper pair only. The energy then comes out as mc², plus the energy of motion, minus or plus (q/m)(ħ/2)B for spin up or down. Compare that last bit with μB and you read off μ = (q/m) × spin. That's q/m where a spinning charge has q/2m, so twice as strong, with nothing assumed. The measured value is 1.001 times that, and the leftover tenth of a percent comes from the electron and light acting on each other, which this equation doesn't cover.

**Added:**
- That "removed" means "solved for in terms of the upper pair and substituted back", not "thrown away". The page says "So the lower pair can be removed from the equation" and two paragraphs later "Removing the lower pair squares the momentum term". If you just delete something nothing gets squared. I had to guess the substitution.
- That A is related to B at all. The page says A "describes the field" and never says how you get the field of strength B out of A.

**Dropped:**
- "The angular momentum of the motion sits inside that term, so it keeps section 1's ratio q/2m." I can't say where inside p²/2m an angular momentum sits, or what magnet it is supposed to make. Nothing before this says the motion's angular momentum makes a magnet in the equation.
- "It comes from the products of the spin matrices in the square, where the order of the factors matters, and it comes out with q/m". I repeated "it comes out twice as big" and dropped the mechanism.

**Why? with no answer:**
- "Each part of the momentum, such as p̂_x, is replaced by p̂_x − qA_x". Wanted: what A is in one picture (a field of arrows whose swirl is the magnetic field), and why momentum is where it goes. "Classical physics uses the same replacement" is an appeal to something the reader never saw.
- "A magnet of strength μ, lined up with a field of strength B, has its energy lowered by μB." Wanted: half a line, such as "that is what strength of a magnet means: energy per unit of field", or the compass needle from chapter 2b.
- "E = mc² + energy of motion ∓ (q/m)(ħ/2)B". Appears whole. Wanted: one sentence of mechanism before it, such as "the small lower pair feeds back into the upper pair's equation, and that feedback is the momentum term applied twice".
- "Removing the lower pair squares the momentum term". Why squares? Same fix as above.
- "it comes out with q/m". This is the pay-off of the chapter's puzzle and the main text gives no reason the reader can hold. Wanted: one concrete line, such as "the square has 1/2m in front, and the order-matters part of two spin matrices carries a 2, so 2 × q/2m = q/m".

**Flags:**
- Read three times: the whole "Where the two comes from" paragraph.
- "The electron's charge is negative, q = −e ... for the electron spin up has the higher energy in a field pointing up", and then section 6 opens with "Say up has −ε and down has +ε". Not a contradiction because of "Say", but it reads like one right after this sentence.
- Section 1 used e as "the electron's charge"; here the charge is −e. First time the sign is mentioned.

## 6. One full turn flips the sign

**Bro version.** Ok so section 3 said a turn has to do something to the column, and a magnetic field is a way to turn a spin, so watch what it does. Put a tilted atom in a vertical field. Up gets energy −ε and down gets +ε. Each amplitude's phase turns at its own energy's rate, so the up arrow turns one way and the down arrow turns the other way by the same amount. Chapter 2a said the angle between the two arrows is the direction the atom leans, so when the lean has swung round by θ, each arrow has turned by only θ/2. Let the lean go all the way round, 360°: the atom points where it started, but each amplitude has turned 180°, which is times −1. It takes 720° to get back to plus. On its own a minus sign on the whole state changes no chance, so you split a beam, turn one half, leave the other alone, and recombine. In 1975 two groups did that with neutrons and a silicon crystal: at 360° the two paths cancelled where they used to add, and the count came back only at 720°. A column that does this is called a spinor.

**Added:**
- That "the lean swinging round the vertical by θ" is the same thing as "turning the electron by θ about the vertical". The summary line says "Turning an electron by an angle" while the derivation is about a lean swinging in a field. I joined them myself.
- That the two amplitudes c_up and c_down here are one pair of the Dirac column, so the result carries over to the column of four. Section 4 said each pair is chapter 2a's list, but this section never says "so the same happens to the Dirac column".

**Dropped:**
- "The half is the ½ in section 3's ħ/2 Σ_z. Up and down have spin +ħ/2 and −ħ/2, and each amplitude's phase turns by the angle times its spin divided by ħ." In the derivation the half came from splitting the angle between two arrows that turn opposite ways. The spin's size ħ/2 never entered it. So I can't say why the two halves are the same half.
- "An amplitude whose spin is a whole number of ħ turns by a whole multiple of the angle". Nothing with whole-number spin has been shown turning.

**Why? with no answer:**
- "Each amplitude's phase turns at its own energy's rate, so after a time t c_up → c_up e^{+iεt/ħ}". The sign in the exponent needs "a state of energy E turns as e^{−iEt/ħ}, and up has E = −ε". That formula is in chapter 2b's box and chapter 5's wave; a four-word reminder would do.
- "The half is the ½ in section 3's ħ/2 Σ_z." Wanted: the link, such as "the energy gap 2ε is the field times the gap between the two spin values, ħ/2 − (−ħ/2) = ħ, so a spin of s turns its phase by s/ħ times the angle".
- "The half that is left alone has the energy without a field, which lies exactly midway between −ε and +ε". Good that it is there. A reader still asks why the left-out "rest of the energy" doesn't change the comparison; half a sentence ("both halves carry it, so it cancels") would close it.
- "It has no charge overall, but it is made of smaller charged particles, so it is still a small magnet." Fine as a statement of fact.

**Flags:**
- θ is used two ways within a few lines. First "the lean has swung round by θ" (an angle round the vertical, which chapter 2a's box called φ), then "a spin tilted by θ from the vertical" (chapter 2a's θ). The "first hint" paragraph is about a different kind of turn from the one the section just did, and the page doesn't say so.
- Figure `spinor-rotation-sign.png` agrees with the text and is clear.
- Figure `neutron-full-turn.png` agrees with the text. The curve touches zero at 360°; the caption says "sketched", which is enough.

## 7. A moving electron

**Bro version.** So far the electron sat still and a positive-energy solution lived only in the upper pair. Give it momentum and the α terms wake up, and α sends upper to lower, so the lower pair can't stay empty. For an electron going up along z with spin up, the column is (1, 0, r, 0) times the usual wave, with r = pc/(E + mc²). At rest r is 0. r depends only on the speed: 0.005 at a hundredth of light speed, 0.27 at half, 0.87 at 0.99. The share of the chance in the lower pair is r²/(1 + r²), so 0.0025% when slow and 43% near light speed. That's why Schrödinger plus two spin amplitudes works for slow electrons. So "upper pair means positive energy" is only true at rest. If the electron goes sideways along x instead, the column is (1, 0, 0, r), which has a spin-up entry and a spin-down entry, so a vertical spin measurement can go either way. The four solutions for each momentum get names: u1, u2 for positive energy and v1, v2 for negative.

**Added:**
- Why the third entry fills for motion along z and the fourth for motion along x: α_z is built from Ẑ, which keeps up as up, and α_x from Ŝ, which swaps up and down. The page gives both columns and never says why they differ.
- How r in terms of speed looks: r = (v/c)·γ/(γ + 1). The page says "so r depends only on the speed" and jumps to the table. I can redo the table with that, and the numbers check out.

**Dropped:** nothing.

**Why? with no answer:**
- "r = pc/(E + mc²)". Appears whole. Wanted: one line, such as "the third row of the equation reads (E + mc²) × third entry = pc × first entry".
- "Spin along the direction of motion is the one case where the spin is kept." Wanted: "section 3's leftover, α_x p_y − α_y p_x, is zero when the momentum has no x or y part".
- "the solution is (1, 0, 0, r)". Wanted: the Ŝ-swaps reason above.
- "For a negative-energy solution it's the other way round: the lower pair is the larger and the upper pair fills in with the same ratio r." Asserted; acceptable with "by the same steps".

**Flags:**
- "Take an electron ... spin up" and then for sideways motion the solution with the same label "can then give either result". The page explains it, but "spin up" as a label for u1 when the spin isn't definitely up needs the sentence "the number says which entry of the larger pair is filled" to come before the sideways example, not after.
- "For each momentum there are four solutions ... v1(p) and v2(p)" says v(p) has momentum p. Section 9 then says the p on v_s(p) is not the wave's momentum. See section 9.

## 8. Electron and positron

**Bro version.** Ok so what about the negative-energy solutions. Take one and conjugate it, meaning swap every i for −i. For a wave that reverses how the phase turns in space and in time, so momentum p becomes −p and energy E becomes −E, and a negative energy becomes positive. The conjugated column doesn't quite obey the Dirac equation: the mass term has the wrong sign next to the others and Ŷ has its own i. A fixed matrix that swaps entries and flips some signs fixes both; it swaps upper pair with lower pair and spin up with spin down. Then look at the field term: p̂ − qA is −iħ∂/∂x − qA, and conjugating flips the −i but not the qA, so after pulling out an overall minus the charge has changed sign. So the result obeys the Dirac equation for charge −q. Put together, a negative-energy electron solution matches a positive-energy solution for a particle with the same mass, charge +e, opposite momentum and opposite spin. That's the positron, and it's what you'd expect from a hole: a missing electron has minus everything the electron had. It's still one equation for one particle though, so it can relabel but it can't make a pair appear from light.

**Added:**
- Why the mass term is the odd one out after conjugating: the time term has an i and the momentum terms have an i, so both flip, and βmc² has no i so it stays. The page says "the mass term ends up with the wrong sign compared with the others" and only two paragraphs later mentions that "conjugation also flips the sign of iħ ∂/∂t".
- Why swapping the pairs repairs the mass sign: β is +1 on the upper pair and −1 on the lower, so trading the pairs flips its sign. The page says "A fixed matrix ... repairs both (box)".
- That A is an ordinary real number at each point, which is why conjugation "leaves qA_x alone".

**Dropped:**
- Why the repair also swaps spin up with spin down. The page states it with "(box)" and gives no reason; I repeated it as a fact.

**Why? with no answer:**
- "A fixed matrix that swaps entries of the column and changes some signs repairs both (box)." Wanted: the β reason above, and "the up-down swap inside each pair is what undoes Ŷ's own i".
- "inside each pair it swaps spin up with spin down". Wanted: the same.
- "A negative-energy solution of the electron's equation matches a positive-energy solution of the equation for a particle of charge +e". A reader asks: matching is a relabelling, so why does that make it "describe" a positron? The page answers honestly in "What this doesn't do", so this is half answered. One sentence earlier, saying "matches" means "has the same wave, chances and behaviour in a field", would help.

**Flags:**
- Order: "the mass term ends up with the wrong sign" comes before the reader is told which terms flipped.
- Chapter 5 said the hole has opposite charge and positive energy. Here "a hole ... has minus that electron's energy, momentum, spin and charge" adds momentum and spin. It is reasonable, but it is new here and presented as if chapter 5 said it ("which is what chapter 5's hole leads us to expect").

## 9. The general solution

**Bro version.** The point is, the Dirac equation is linear, so if two waves each solve it, their sum solves it too. So the most general free state is a sum over every momentum, both spins and both signs of the energy. With c set to 1, it's one formula: sum over spins, sum over momenta, and inside, a number a times a u column times a wave, plus a number b-star times a v column times the wave with its phase turning the other way. a and b-star say how much of each wave is in the state. The 1/√(2E_p) and the (2πħ)³ are conventions. If only a_1 at one momentum is switched on you get section 7's moving electron. The second term's wave has both signs reversed, so by section 8 it's the wave that matches a positron of momentum p, which is why the p on v means the positron's momentum and not the wave's own. The star on b is there because next chapter the numbers become operators: a removes an electron and b-star becomes b-dagger, which creates a positron.

**Added:**
- That **p**·**x** means p_x x + p_y y + p_z z. The page uses the dot and bold letters without saying.
- That the x in ψ(x) and in p·x means a point in space and time together, not the x coordinate of earlier sections.
- That d³p means "over all three parts of the momentum".

**Dropped:**
- "The label s is different: it names the filled entry of the column, and the positron's spin is the opposite one." I kept it as a rule and can't say why the momentum label got flipped to the positron's and the spin label didn't.

**Why? with no answer:**
- "v_s(p) e^{+ip·x/ħ}: A negative-energy solution, with its phase turning the other way". Why is the negative-energy part written with the phase reversed in space as well as in time, when section 7's negative-energy solution at momentum p would be e^{i(p·x + Et)/ħ}? Wanted: "we relabel p as −p in the second term so that p is the positron's momentum; the sum runs over all momenta, so nothing is lost".
- "b_s*(p) becomes b̂†_s(p), which creates a positron." Why does the coefficient of a negative-energy wave create something? Chapter 5 section 10 promised this; a pointer to it would do.
- "The star is written now so that the formula keeps its shape then." Fine, but a reader asks whether b* is the conjugate of some b that matters now. Wanted: "for now b* is just a name for a number".

**Flags:**
- Contradiction inside the chapter: the table row says "u_s(p), v_s(p): Section 7's columns, multiplied by √(E_p + m) by convention", and section 7 says "For each momentum there are four solutions ... v1(p) and v2(p)". The next paragraph says "the label p on v_s(p) is the positron's momentum, not the momentum that the wave's own phase gives, which is −p". So v_s(p) here is section 7's column for momentum −p. The table row and section 7 say one thing, the paragraph says another.
- Read three times: "So the label p on v_s(p) is the positron's momentum, not the momentum that the wave's own phase gives, which is −p (first box). The label s is different: it names the filled entry of the column, and the positron's spin is the opposite one."
- "as chapter 5 said for the Klein–Gordon equation": chapter 5 said "linear" only inside boxes.
- "$E_p t − \mathbf p·\mathbf x$, the sum chapter 4's box wrote p^μ x_μ" leans on a box in a chapter that told the reader they didn't need it.
- The formula is the densest thing in the main text and arrives before the table that explains it. A two-wave version first (one u wave plus one v wave, with a and b*) would let the reader see the shape before the integral.

---

# The ten gaps that would most confuse the reader, ranked

1. **Section 5**, "So the lower pair can be removed from the equation" and then "Removing the lower pair squares the momentum term". Deleting something can't square anything. Fix: say the second pair of rows gives the lower pair in terms of the upper pair, and putting that back applies the momentum term twice.

2. **Section 5**, "It comes from the products of the spin matrices in the square, where the order of the factors matters, and it comes out with q/m". The chapter's headline result has no reason in the main text. Fix: one concrete line, "the square carries 1/2m, and two different spin matrices in the two orders differ by a factor 2, so the spin term gets 2 × q/2m = q/m".

3. **Section 9**, table row "u_s(p), v_s(p): Section 7's columns" against "the label p on v_s(p) is the positron's momentum, not the momentum that the wave's own phase gives, which is −p". The two disagree. Fix: in the table say "v_s(p) is section 7's negative-energy column for momentum −p, relabelled so that p is the positron's momentum", and say the sum over all momenta makes the relabelling harmless.

4. **Section 6**, "The half is the ½ in section 3's ħ/2 Σ_z ... each amplitude's phase turns by the angle times its spin divided by ħ." The derivation's half came from two arrows turning opposite ways; the spin's size never entered. Fix: add "the energy gap 2ε is the field times the gap ħ between the two spin values, so each phase turns by spin/ħ times the angle".

5. **Section 5**, "Each part of the momentum, such as p̂_x, is replaced by p̂_x − qA_x, where ... A is a quantity with a size and a direction at each point that describes the field". The reader can't picture A or see why it goes with momentum. Fix: one sentence, "A is a field of arrows whose swirl is the magnetic field; a field B pointing up is arrows circling the vertical", and admit the replacement is taken on trust until the QED chapter.

6. **Section 3**, "The energy stays the same only if the column is turned too, and L̂_z leaves the column alone." Nothing has said that L̂_z is what does the turning. Fix: add "L̂_z is the momentum that goes with turning where the particle is, as chapter 1's momentum went with shifting it, and it contains no matrix, so it can't turn the column".

7. **Section 3**, "Take two copies of Ẑ ... Its commutator with Ĥ is exactly minus the first one." The candidate comes from nowhere and the cancellation is bare. Fix: say "Ẑ is the spin matrix for the vertical axis, and swapping its order with Ŝ or Ŷ turns one into the other, which is what trades α_x for α_y in the leftover".

8. **Section 8**, "A fixed matrix that swaps entries of the column and changes some signs repairs both (box) ... inside each pair it swaps spin up with spin down". No reason for either swap. Fix: "β is +1 on the upper pair and −1 on the lower, so trading the pairs flips the mass term; trading up and down inside a pair undoes Ŷ's own i".

9. **Section 1**, "comes in steps of ħ (second box). Two results, one step apart and placed evenly either side of zero, have to be +ħ/2 and −ħ/2." The step rule has no reason in the main text and "evenly either side of zero" has none at all. Fix: one sentence on the wave joining up round a circle, and "nothing makes up different from down, so the values are symmetric about zero".

10. **Section 7**, "r = pc/(E + mc²)", "the solution is (1, 0, 0, r)" and "Spin along the direction of motion is the one case where the spin is kept." Three bare results. Fix: "the third row reads (E + mc²) × third entry = pc × first entry"; "α_z is built from Ẑ, which keeps up as up, α_x from Ŝ, which swaps up and down"; "section 3's leftover α_x p_y − α_y p_x is zero when the momentum points along z".

Runners-up: section 2 never checks that the four matrices pass chapter 5's conditions; section 6 uses θ for two different angles; section 9 uses **p**·**x**, ψ(x) and d³p without saying what the bold dot or the bare x mean; section 4 says the two results "are the two spots" before the magnet is tied to the spin.

Sections that are clear as written: the intro, section 4, most of section 2, the first half of section 6 (up to the table), the table and "How much" part of section 7. All six figures agree with the text.
