# Chapter 6: `/bro what?` replies, first draft (2026-11-26)

Reader: has read chapters 1, 2a, 2b, 3, 4, 5 (main text), high-school maths. Main text of chapter 6 only, sections intro to 9.

## Intro

**Bro version.** Ok so last chapter left us with Dirac's equation and a state that's a stack of four wave functions, two with positive energy and two with negative. Nobody said what makes the two positive ones different from each other. This chapter says the difference is spin, and the wild part is that nobody put spin into the equation, it falls out. Two bonus results come along: the equation gets the strength of the electron's magnet right, and it says that turning an electron once round doesn't give you back the same state. Then we look at a moving electron, match each negative-energy solution with a positron, and finish with one big sum of waves for the next chapter. The table is the destination: entries 1 and 2 are an electron with spin up and down, entries 3 and 4 are a positron with spin down and up.

**Added:** nothing.

**Dropped:** nothing. The table's rows 3 and 4 show "Spin: up" next to "A positron, spin down", which looks like a typo on first read, but the header points to section 8, so I let it ride.

**Flags:** nothing serious. A reader skimming the table will stop at "$-mc^2$ | up | A positron, spin down" and wonder whether the up/down mismatch is a mistake. A half-line under the table ("the flip in the last two rows is explained in section 8") would stop that.

## 1. A puzzle: a magnet twice too strong

**Bro version.** Basically, anything charged that spins is a little magnet, because charge going in a circle is a current loop and a current loop is an electromagnet. Anything with mass that spins also has angular momentum, which is "how much turning it's got". Both come from the same spinning, so the magnet strength is the angular momentum times a fixed number, $q/2m$. In 1925 two guys said the electron has a built-in angular momentum of $\hbar/2$ even when it isn't going round anything, and called it spin. Plug $\hbar/2$ into the rule and the electron's magnet should be $e\hbar/4m$. The measured value is $e\hbar/2m$, twice that. So people jammed in a factor of two by hand, Pauli included, and nobody knew why the spin is $\hbar/2$ or why the magnet is double.

**Added:**
- That "go up together" means "exactly proportional". The page says "Spin the body faster, and both go up together. So the two are tied by a fixed ratio." Two things can both go up without having a fixed ratio; I had to take the proportionality on faith (the box shows it, the main text only asserts it).
- What "the strength of the magnet, written $\mu$" is a strength *of*, in the sense of what you would measure. The main text gives no meaning to $\mu$ until section 5 ("has its energy lowered by $\mu B$").

**Dropped:** "It explained why many of the colours in the light of atoms come in close pairs." Nothing so far connects spin to colours, so I couldn't say how.

**Flags:**
- "charge", "electric current" and "electromagnet" appear for the first time on the site with no gloss. Probably fine at high-school level, but it is the first electricity in the main text of any chapter.
- Otherwise clear. The two-row table does the job.

## 2. Four wave functions and one question

**Bro version.** Ok so here's the Dirac equation written out in full: the usual "$i\hbar$ times the rate of change equals $\hat H$ on the state", where $\hat H$ is $c$ times (a matrix times each of the three momentum operators) plus $\beta\,mc^2$. The four matrices are four-by-four, made of two-by-two blocks, and the blocks are the spin matrices $\hat S$, $\hat Y$, $\hat Z$. Think of the column of four as an upper pair and a lower pair. $\beta$ leaves each pair alone (plus sign on the upper, minus on the lower), and each $\alpha$ swaps stuff between the upper and lower pairs. For a particle at rest the momentum is zero, only $\beta\,mc^2$ survives, and you can read it off: the upper pair has energy $+mc^2$, the lower pair $-mc^2$. But $\psi_1$ and $\psi_2$ have the same energy and the same momentum, so something else has to be different about them.

**Added:**
- That the "0" in the block matrices stands for a two-by-two block of zeros. The page only says "In $\beta$, each 1 stands for the two-by-two matrix that changes nothing."
- Why off-diagonal blocks mean "sends the upper pair to the lower and the lower to the upper". The page states it as a consequence ("Each $\alpha$ has its blocks off the diagonal, so it sends...") but a high-school reader has never multiplied a block matrix by a column; I just believed it.

**Dropped:** "This is chapter 5's result on a line, twice over." I think it means "chapter 5's two-entry result, happening once in each spin slot", but I wasn't sure enough to say it.

**Flags:**
- "The blocks are the three spin matrices of chapter 5, $\hat S$ ..., $\hat Y$ ... and $\hat Z$". Chapter 5's main text only ever showed $\hat Z$ and $\hat S$ and said "and one more (box)". $\hat Y$ and "front-to-back magnet" live only in a chapter 5 box, so a main-text reader meets $\hat Y$ here for the first time, with no entries shown.
- "If they were the same state, the equation wouldn't need both." Chapter 5 already gave a different reason the column has four entries (four matrices that all anticommute need four-by-four). So "the equation wouldn't need both" reads as a new claim, and the jump to "So some other measurable quantity must have one value for $\psi_1$ and another for $\psi_2$" is asserted, not argued.

## 3. Angular momentum that isn't kept

**Bro version.** Ok so chapter 2b had a rule: the average of a quantity changes at a rate set by its commutator with $\hat H$. If the commutator is zero, the quantity never changes, and the page calls that "kept". A free particle has nothing twisting it, so its angular momentum round the vertical axis, $L_z = x\,p_y - y\,p_x$, should be kept. For Schrödinger's equation it is. For Dirac's it isn't: the commutator comes out as some leftover with $\alpha$ matrices in it. The fix is to add a second piece that only acts on the column, $\hbar/2$ times a matrix made of two copies of $\hat Z$. Its commutator is exactly minus the first one, so the sum is kept. The point is the electron carries an extra angular momentum that has nothing to do with its motion, it has it even sitting still, and that's the spin. Dirac never asked for it; the equation can't balance its angular momentum without it.

**Added:**
- Why $x\,p_y - y\,p_x$ is angular momentum. The page drops the formula in and says "For a particle on a circle of radius $r$ this is $r$ times its momentum, as in section 1's ring." But section 1's main text never said the ring's angular momentum is $r$ times momentum; that ($mvr$) is inside section 1's box. The main text of section 1 only gave the pendulum's $m\ell^2\dot\theta$. I had to work out $m\ell^2\dot\theta = \ell \times (m\ell\dot\theta)$ myself.
- That "vertical axis" is the $z$ axis. The first place the page says so is section 7 ("moving up, along $z$").
- That the extra piece counts as an *angular momentum* because it is the thing you must add to angular momentum to get a kept total. The page jumps from "the sum is kept" to "The electron carries a second angular momentum" without that sentence.

**Dropped:** the whole "**Why.**" paragraph: "A turn about the vertical axis mixes the $x$ and $y$ parts of the momentum. Unless the matrices are mixed in the same way, $\hat H$ changes. So a turn has to act on the column as well, and $\hat L_z$ leaves the column alone." Nothing before this says angular momentum has anything to do with *turning the system*, or that "kept" has anything to do with "$\hat H$ doesn't change when you turn". Chapter 1 has one sentence linking shifting to momentum, nothing for turning. I couldn't re-explain it, so I left it out.

**Flags:**
- The "Why." paragraph is the read-three-times one (quoted above). It needs the idea "angular momentum is the quantity that goes with turning, the way momentum goes with shifting" stated first.
- "those all commute with $\hat p_x$": chapter 2b never said $\hat p_x$ commutes with $\hat p_y$ (it was one-dimensional). Small, but it is a first.
- "Look, then, for a second quantity that acts only on the column and whose commutator cancels the first. There is one (box)." Why $\hat Z$ and why $\hbar/2$ are box-only, so in the main text the $\hbar/2$, the number the whole chapter is about, appears from nowhere.

## 4. Spin up and spin down

**Bro version.** Basically, a measurement gives one of the operator's eigenvalues, so just read them off the spin matrix. Written out, $\tfrac{\hbar}{2}\Sigma_z$ multiplies $\psi_1$ and $\psi_3$ by $+\hbar/2$ and $\psi_2$ and $\psi_4$ by $-\hbar/2$. So spin along the vertical is either $+\hbar/2$ (spin up) or $-\hbar/2$ (spin down), exactly the size Uhlenbeck and Goudsmit guessed, and those two values are the two spots on Stern and Gerlach's plate. That answers section 2: in each pair, the first entry is spin up and the second is spin down. Energy tells the pairs apart, spin tells the two entries in a pair apart. Sideways works the same with $\hat S$, and its eigenstates are equal mixes of up and down, like right and left in chapter 2a. So each pair is just chapter 2a's two amplitudes, except each amplitude is now a whole wave function.

**Added:** nothing.

**Dropped:** nothing.

**Flags:**
- Chapter 5 section 7 said of its two-entry column "We're borrowing only the arithmetic of the spin matrices here. This column isn't a spin". Now each pair of the column *is* a spin. It isn't a contradiction (chapter 5's two entries were the energy signs), but a reader who remembers that warning gets no word here on why it no longer applies.
- Chapter 2b called up and down "$+1$" and "$-1$" and said the numbers were "our choice of units". This section quietly switches to $\pm\hbar/2$. One clause tying the two together would help ("in ordinary units chapter 2b's $\pm1$ is $\pm\hbar/2$").
- Otherwise this section is clear and the figure carries it.

## 5. The magnet comes out right

**Bro version.** Ok so now check the magnet. A magnet shows up in an equation as an energy: strength $\mu$ lined up with a field $B$ lowers the energy by $\mu B$, lined up against it raises it by $\mu B$. Put a magnetic field into the Dirac equation the standard way, look at a slow particle with positive energy, and the energy comes out as $mc^2$ plus energy of motion, minus or plus $\frac{q}{m}\cdot\frac{\hbar}{2}B$ for spin up or down. That last bit is a magnet's energy, so $\mu = \frac{q}{m}\times$ spin. The spinning-charge rule had $q/2m$, Dirac gives $q/m$, twice as much, and nobody put the two in by hand. For the electron that's $e\hbar/2m$, the measured number. Measured super carefully it's about a tenth of a percent bigger, and that leftover comes from the electron's dealings with light, which later chapters handle.

**Added:**
- What "the standard way" actually is. The main text says only "Physics has one standard way to put a magnetic field into the equation of a charged particle, and classical physics uses the same one (box)." The recipe ($\hat{\mathbf p}\to\hat{\mathbf p}-q\mathbf A$) is box-only, so in the main text the result is a pure "trust me". That is fine for this section on its own, but section 8's main text then leans on the recipe as if it had been shown (see section 8).

**Dropped:** nothing.

**Flags:**
- "For a slow particle the lower pair of the column is small (section 7)" is a forward reference to something not yet shown. Tolerable, but it is the step the whole reduction rests on.
- "The electron's charge is negative, so its magnet points opposite to its spin." Fine, but it means that for the electron spin up has the *higher* energy, while the line above says "with the minus sign for spin up". The sentence is right for general $q$; a reader plugging in the electron has to notice $q=-e$ flips it.
- The table mixes forms: rows 1 and 2 are "$q/2m$" and "$q/m$", row 3 is "$1.001\times e/m$". Small.

## 6. One full turn flips the sign

**Bro version.** Ok so remember chapter 2b's tilted atom in a vertical field, whose lean swings round like a top. The field makes up's energy $-\varepsilon$ and down's $+\varepsilon$, so the up arrow turns one way and the down arrow turns the other way, at the same rate. The angle between the two arrows is what sets the lean, and that angle grows twice as fast as either arrow turns. So when the lean has swung by $\theta$, each amplitude has only turned by $\theta/2$. Swing the lean a full $360°$ and the atom points where it started, but each amplitude has done a half turn, which is times $-1$. You need $720°$ to really get back. A lone minus sign changes no chance, so to see it you split a beam, turn the spins in one half by a full turn, and recombine: in 1975 people did this with neutrons and the two paths cancelled at $360°$ and came back at $720°$. A column that turns at half the angle like this is called a spinor.

**Added:**
- That "swinging the lean round with a magnetic field" is the same thing as "turning the electron". The section opens "Section 3 found that turning an electron means turning its column too. The way the column turns is the strangest thing in this chapter", then never uses section 3's $\Sigma_z$; it gets the turn from a field instead. I had to assume the two are the same operation.
- How a neutron can be a magnet at all. The page says "it has no charge, so a magnetic field turns its spin without bending its path." But section 1 says a magnet comes from spinning *charge*, and section 5's result is $\mu = \frac{q}{m}\times$ spin, which is zero for $q=0$. By the chapter's own formula a neutron's spin shouldn't feel the field. I had to just accept that it does.

**Dropped:**
- "The half comes from the $\hbar/2$ of section 3: a quantity whose angular momentum is a whole number of $\hbar$ comes back to itself after one turn." In this section the half came from the two arrows turning opposite ways, not from $\hbar/2$. Nothing shows how the size of the angular momentum sets the turning rate, so I couldn't say it.
- "Section 10 has the general rule for how the column changes when it is turned or set moving."

**Flags:**
- "Chapter 2a had the first sign of this. Its box gave the amplitudes of a spin tilted by $\theta$ as $\cos(\theta/2)$ and $\sin(\theta/2)$, with half angles." In chapter 2a's box, $\theta$ is the tilt *away from* vertical, and the angle *round* the vertical is $\varphi$, about which that same box says "the direction $\varphi$ round the circle becomes the phase of $c_1$ unchanged", so not halved. This section's $\theta$ is the round-the-vertical angle. So the cited evidence is about a different angle, the same letter now means something else, and what chapter 2a said about this section's angle looks like the opposite claim (full angle, not half). The shared-phase remark does reconcile it, but only if the reader works it out.
- "that's why chapter 2b left this shared phase out": chapter 2b's main text never mentions a shared phase; "With the shared phase removed" is only in its box.
- "neutron" appears for the first time on the site here, with no gloss (chapter 5 introduced only the electron and the proton).
- "The way the column turns is the strangest thing in this chapter, and chapter 2b already had it in its hands." Flourish; fine, but the second half is vague until the next paragraph.
- The core argument (two arrows, opposite ways, angle between them doubles) is clear and I could re-explain it without help.

## 7. A moving electron

**Bro version.** So far the electron sat still. At rest, a positive-energy solution lives only in the upper pair. Once there's momentum, the $\alpha$ terms switch on, and those shuttle between upper and lower pairs, so the lower pair can't stay empty. For an electron moving up along $z$ with spin up, the column is $(1, 0, r, 0)$ times the usual wave, with $r = pc/(E+mc^2)$. $r$ depends only on the speed: at $0.01\,c$ it's 0.005 and the lower pair holds 0.0025% of the chance; at $0.99\,c$ it's 0.87 and the lower pair holds 43%. So for slow electrons the lower pair is basically nothing, which is why Schrödinger plus two spin amplitudes works so well, and near light speed the pairs are nearly equal. Negative-energy solutions are the mirror image, lower pair big, upper pair filling in. For each momentum there are four solutions, named $u_1(p)$, $u_2(p)$ for positive energy and $v_1(p)$, $v_2(p)$ for negative.

**Added:**
- "Chapter 4 gave $p = \gamma mv$": chapter 4's main text gives "the energy is gamma times $mc^2$" but $p=\gamma mv$ is only in its box. Small.
- Which of "1" and "2" is spin up. "The number says which spin" doesn't say which is which.

**Dropped:** "If the electron moves sideways instead, along $x$, the lower pair fills in at its spin-down entry. That is section 3 again: for a moving electron the spin alone isn't kept, only the total angular momentum." Section 3's "not kept" meant "changes in time". Here nothing changes in time; it's one fixed solution that happens to mix a spin-up entry with a spin-down entry. I couldn't get from "changes in time" to "this solution has both entries filled" with what I was given, and why it's the spin-down entry is box-only.

**Flags:**
- The "Spin in motion" paragraph, quoted above, is the one I read three times. It needs the link "a quantity that doesn't commute with $\hat H$ can't have a definite value in a state of definite energy" (chapter 2b section 2 has the ingredients, shared eigenstates, but the page doesn't call on them).
- Section 3's summary table says $\tfrac{\hbar}{2}\Sigma_z$ is not kept for a free electron, yet the $z$-moving example has pure spin up. The paragraph half-explains ("the spin points along the motion") but never says outright that spin along the direction of motion is the exception.
- The speed table and the "share is $r^2/(1+r^2)$" line are clear; I could redo the numbers.

## 8. Electron and positron

**Bro version.** Ok so what about the negative-energy solutions. Trick in two steps. Step one: take the complex conjugate of the wave, which makes its phase turn the other way in both space and time, so a wave with momentum $p$ and energy $E$ becomes one with $-p$ and $-E$; a negative energy becomes positive. Step two: conjugating alone doesn't quite give a solution, because one of the matrices has an $i$ in it, so you also multiply by a fixed matrix that shuffles the entries, and that shuffle swaps spin up and down. The result, $\psi_c$, solves the Dirac equation for the opposite charge. So every negative-energy electron solution matches a positive-energy solution for a particle with the same mass and charge $+e$, opposite momentum, opposite spin. That's the positron, and it lines up with chapter 5's hole: a missing electron has minus the electron's energy, momentum, spin and charge. But it's still a one-particle equation, it only relabels; it can't make pairs appear out of light.

**Added:**
- What "complex conjugate" means. No earlier main text defines it (the star shows up only inside boxes in chapters 2a, 2b and 5), and there is no Math Refresher link here. The page gives its effect on a wave ("reverses the way its phase turns"), but "Conjugating every entry" and "Conjugation turns the $-i$ into $+i$" need the plain definition "swap $i$ for $-i$ everywhere".
- Why conjugating the *solution* means conjugating the *operator in the equation*. The page goes straight from $\psi^*$ to "Conjugation turns the $-i$ into $+i$ and leaves $q\mathbf A$ alone". The missing step is "conjugate the whole equation, so every $i$ in it flips".

**Dropped:** the "**The charge flips.**" derivation as an argument. "Section 5 put a field into the equation through the combination $\hat{\mathbf p} - q\mathbf A$, which is $-i\hbar\nabla - q\mathbf A$." Section 5's *main text* never showed this; it said "one standard way ... (box)". So $\mathbf A$ is an undefined symbol in the main text, and $\nabla$ has only appeared in boxes (and once, unexplained, in chapter 4 section 6). Then "$= -\left(-i\hbar\nabla + q\mathbf A\right)$. Inside the bracket the charge has changed sign": what happens to the minus sign *outside* the bracket is never said. I kept the conclusion and dropped the reasoning.

**Flags:**
- "Every item in the table is reversed" but the table's last row is "Mass | $m$ | $m$", which is not reversed. The next sentence lists only "energy, momentum, spin and charge", so the claim should say "every item but the mass".
- "The reshuffle also swaps spin up and spin down." Asserted with no reason in the main text. It's the fact that explains the odd-looking intro table, so it carries weight.
- "matches" is doing a lot of work: the positive-energy solution solves a *different* equation (charge $+e$). The page says so in the table header ("Charge in the equation"), but a reader may still ask whether the positron is a solution of the electron's equation or not.

## 9. The general solution

**Bro version.** Ok so the last thing is one formula that bundles the lot. The Dirac equation is linear, so you can add solutions and still have a solution. The most general free state is therefore a sum over every momentum, both spins, and both energy signs. Each positive-energy piece is a $u$ column times its wave times a number $a_s(p)$; each negative-energy piece is a $v$ column times a wave whose phase turns the other way, times a number $b_s^*(p)$. The numbers say how much of each wave is in the state. The $1/\sqrt{2E_p}$ and $(2\pi\hbar)^3$ are bookkeeping conventions. The label $\mathbf p$ on the $v$ term is the *positron's* momentum, because by section 8 that backwards wave matches a positron with momentum $\mathbf p$ and energy $+E_p$. Next chapter the numbers become operators: $a$ removes an electron, and $b^*$ becomes $\hat b^\dagger$, which creates a positron; the star is written now so the formula doesn't change shape later.

**Added:**
- What "we set $c = 1$" means. The main text of no chapter explains it; chapter 4 says "expressions that leave out $c$ use $c = 1$" inside a box. A high-school reader has to guess that it is a choice of units.
- That plain $p$ in "$p\cdot x$" is energy and momentum bundled, while bold $\mathbf p$ is the ordinary momentum. The table says "Chapter 4's short form for $E_pt - \mathbf p\cdot\mathbf x$", but that short form is in chapter 4's notation box ("You don't need it to follow this chapter"), and written there as $A^\mu B_\mu$, never with a dot.
- That section 7's column $(1,0,r,0)$ and $u_s(p)$ are the same thing up to an overall factor. The table says "Section 7's positive-energy solution"; section 7 named $u_1(p)$ but never wrote "$u_1(p) = (1,0,r,0)$".

**Dropped:** "a sum over every momentum" as an integral: "$\int \frac{d^3p}{(2\pi\hbar)^3}$" with "$d^3p$" is new notation. I just said "sum over every momentum" as the table does and left the symbol alone.

**Flags:**
- "So the label $\mathbf p$ on $v_s(p)$ is the positron's momentum, not the momentum the negative-energy wave has on paper (first box)." Followable with section 8 in hand, but I had to read it twice and unpack $e^{+ip\cdot x/\hbar}$ by hand to see "both signs reversed".
- The spin label on $v_s(p)$: section 8 says the match swaps spin up and down, and this section says the momentum label is the positron's. It never says whether $s$ on $v_s$ is the positron's spin or the negative-energy wave's spin.
- "which collects everything above": the formula has no magnet and no full turn in it. Harmless overstatement.
- "as chapter 3 turned the spring's position and momentum into operators that step up and down the rungs" matches chapter 3; fine.
