# Chapter 6 updates: The Dirac Equation

This file tracks the work on chapter 6: the page `docs/dirac-equation.md`, and later its script, deck and video.

**Since iteration L the chapter is two pages.** Chapter 6a is `docs/dirac-equation.md` (old sections 1 to 6). Chapter 6b is `docs/dirac-solutions.md`, "Solutions of the Dirac Equation" (old sections 7 to 10, now its sections 1 to 4). Items from iterations A to K use the old section numbers. From L on, a section of the second page is written "6b §2". Both pages are tracked in this file.

Each round of work is an iteration with a letter (A, B, C and so on). Each item in it has a number, so an item is referred to as, for example, A3. A new round gets a new letter, and old items are never renumbered.

Status words: **Done** (applied), **Open** (waiting for a decision or for work), **Kept** (decided to leave as is), **Noted** (for the record, no action).

Rules carried over from chapter 5: Claude doesn't start the script until Hanh says the page is final. Open items on the page get a Jump line (a `?rev=ID` link into the dev site, a source line and the exact search text), rebuilt with a refresh script. A new deck is smoke-tested before its review.

## What is left to resolve

This section always lists every open item, one per row.

### Waiting for Hanh's decision

Claude wrote the draft on its own recommendations for A2 to A9, so that Hanh has a page to read. Each can still be overruled.

| ID | The question | Claude's recommendation |
| --- | --- | --- |
| A2 | **The story.** The page follows the outline under iteration A: the magnet puzzle, the question about the four wave functions, spin from the angular momentum that isn't kept, the magnet's strength, the full turn, a moving electron, electron and positron, the general solution. Keep this order? | Yes. |
| A3 | **The opening puzzle.** The page opens on the electron's magnet being twice as strong as a spinning charge's. Keep? | Yes. |
| A4 | **The full-turn section.** Section 6 has the sign flip and the 1975 neutron experiments. Keep? | Yes. Names and dates are checked (C1). |
| A5 | **The old derivations.** They are kept as boxes, close to their old wording, with section 10 for the notation. Keep? | Yes. |
| A6 | **Dirac's sea and the backward-in-time reading** are gone from this page; chapter 5 has them. | Leave them out. |
| A9 | **Section names** are new, and 17 links from other pages are repointed. | Keep. |
| C16 | **Order of sections 5 and 7.** Section 5 (the magnet) uses one fact from section 7 (a slow electron's lower pair is small). The rating review offered two fixes: quote the number in section 5 with a pointer forward (done), or move "A moving electron" before the magnet section. | Keep the present order. Moving it delays the answer to the opening puzzle. |
| C17 | **The Heisenberg-equation box** in section 3 isn't used by this chapter. The review would move it to section 10. | Keep it in section 3 with its "nothing here depends on it" line. It belongs beside the rule it restates. |
| C18 | **The preview box** in section 9 (positive energies once the coefficients are operators) uses the next chapter's terms. The review would cut it. | Keep it, with its new first line telling the reader to skip it for now. The next chapter links to it. |
| C19 | **Section 10's last box** multiplies out four block products term by term. The review would keep one and say the others go the same way. | Leave it. It is reference material and later chapters link into it. |

Still open from iteration D:

| ID | The item | Claude's recommendation |
| --- | --- | --- |
| E3 | Structure: open section 7 with the question it answers; consider folding section 9 into section 10. | See E3. |

### Waiting for work

| ID | What has to happen | Waiting on |
| --- | --- | --- |
| C20 | In the carried-over boxes, several displayed equations end with a comma and are followed by a new sentence. Change them to full stops. | Claude, in the next pass. |
| C21 | Neutron figure: the vertical axis has no zero mark, and the "silicon crystal" label sits over one mirror. | Claude, in the next pass. |
| C22 | The charge-conjugation box writes the same matrix as $\sigma^2$ and $\sigma_2$. Pick one. | Claude, in the next pass. |

## Status

| Step | State |
| --- | --- |
| Page | Rewritten (B), revised after three reviews (C) and a closing review (D), then section 1 reworked with Hanh (E) and a whole pass for gaps after a second bro-what test (F). A third check (G) rated it 8 out of 10 and its eight fixes are in. Not committed. |
| Script, pause file, deck, video | Not started. They wait until Hanh says the page is final. |

---

# The page

## A. Reading the old page, and a plan (2026-11-26)

Hanh: "let's do chap 6". Claude read `docs/dirac-equation.md` in full (487 lines, about 4,100 words) with the links other pages make into it, and has edited nothing.

| ID | Item | Status |
| --- | --- | --- |
| A1 | Rating of the old page against chapters 3, 4 and 5: **4 out of 10** as a chapter of this site. Its physics is careful and, as far as Claude can tell, right. | Noted |
| A2–A9 | The decisions listed above. Claude drafted on its recommendations; A7 (recall chapter 2b's rule, keep the derivation as a box) and A8 ($c$ and $\hbar$ explicit in the main text) are applied the same way. | Open for Hanh |
| A10 | Write the page. | Done (B1) |

**Why 4 out of 10 (A1)**

- It opens on a commutator, $[H, L_i]$, with no experiment and no question the reader already has.
- The main text is in the textbook register: $\boldsymbol\Sigma$, $\varepsilon_{ijk}$, $S(\Lambda)$, $\sigma^{\mu\nu}$, "minimal substitution", "Weyl spinors" and "charge conjugation" all arrive without a plain statement of what they are for.
- It leans on chapter 5's notation section, which chapter 5 tells the reader they don't need, and it sets $c = 1$ throughout.
- About half its words are derivations, and the sections are named after topics ("Spin", "Spinors", "General Solution"), not after steps in an argument.
- Section 2 re-derives a rule chapter 2b already gave, and sections 3 and 4 retell parts of chapter 5.
- What is good and should survive: every derivation is complete, the result that the electron's magnet strength comes out right, the sign flip under one full turn, and the general solution that the next chapter starts from.

**The proposed outline (A2)**

1. **A puzzle: a magnet twice too strong.** The electron is a small magnet (chapter 2a's silver atoms). A spinning ball of charge with the electron's spin would be half as strong as what is measured.
2. **Four wave functions, and a question.** Chapter 5 left two with each sign of the energy. What tells the two apart?
3. **Something that should be kept, and isn't.** For a free particle, the angular momentum of its motion should stay constant. Under the Dirac equation it doesn't, unless a second piece is added. That piece is built from Pauli's three matrices, and it is the spin.
4. **Up and down.** The spin along any direction comes out as plus or minus half of $\hbar$. So the two wave functions of each energy sign are spin up and spin down, which answers section 2.
5. **The magnet strength comes out right.** Put the electron in a magnetic field. At low speed the equation gives a magnet twice as strong as the spinning ball's, which answers section 1. The calculation goes in a box.
6. **One full turn isn't enough.** Turn a spin state through a full circle and it comes back with a minus sign; two full turns restore it. Chapter 2a's half angles were the first sign of this. The neutron experiments of 1975.
7. **A moving electron.** At rest the four entries separate. In motion the two pairs mix, with a large pair and a small pair, and the solutions get their names.
8. **Electron and positron.** The negative-energy solutions, reread as chapter 5's last section promised, pair up with the positive ones: same mass, same two spins, opposite charge.
9. **The general solution, and the notation later chapters use.** The sum over all waves that the next chapter starts from, and the boxes on how the four entries change between observers.

About 3,000 words of main text, plus the derivations, which stay close to their present length.

## B. First draft (2026-11-26)

| ID | Item | Status |
| --- | --- | --- |
| B1 | `docs/dirac-equation.md` rewritten in one pass around the A2 outline. Ten sections; the old derivations kept as boxes; section 10 holds the notation and the three boxes on how a spinor changes between observers. | Done |
| B2 | Figures: `rest-spinor-basis.png` and `spinor-rotation-sign.png` redrawn in plain words; `neutron-full-turn.png` is new. `spin-measurement.png` is no longer used here but stays, because Symmetries uses it. | Done |
| B3 | Links into this page from `qft.md`, `qft-action.md`, `field-quantization.md`, `qed.md` and `appendix-math-groups.md` repointed. Four links in `qft.md` about Dirac's sea now point to chapter 5. Every anchor resolves in the built site. | Done |
| B4 | `updates/refresh_links.py` takes the chapter as an argument: `python3 updates/refresh_links.py 06-dirac-equation`. | Done |

## C. Three fresh reviews of the first draft, and one revision pass (2026-11-26)

A correctness check, a rating review and a bro-what test, each by a fresh agent that saw no history. The bro-what replies are in `06-bro-replies.md`.

**Ratings of the first draft:** 7 out of 10 against chapters 3 to 5, 7.5 for structure. The correctness check found no wrong sign, factor or number in any derivation.

**Themes that came up in more than one review.** These are structural, so they are listed first.

1. The page never said that angular momentum is the quantity that goes with turning, so section 3's reason and section 6's opening didn't follow (rating review and bro-what).
2. The main text of sections 5 and 8 leaned on things only a box had shown: the way a field enters the equation, and the symbol $\mathbf A$ (rating review and bro-what).
3. Section 7's "spin in motion" used "not kept" for a state that doesn't change in time (all three).
4. The label on $v_s(p)$ and the positron's spin (correctness and bro-what).

| ID | Section | Finding | What changed | Status |
| --- | --- | --- | --- | --- |
| C1 | 6 | History checked: Rauch's group (Vienna) and Werner, Colella, Overhauser and Eagen, both 1975; Uhlenbeck and Goudsmit 1925; Pauli 1927; Kusch and Foley 1947. | "one from Vienna led by Helmut Rauch". | Done |
| C2 | 3 | Theme 1. | New paragraph "Why it should be kept", built on chapter 1's missing coordinate; $L_z$ introduced from the pendulum; "Why" rewritten. | Done |
| C3 | 3 | The $\hbar/2$ came from a box with no reason in the main text; three formulas in a row. | One formula removed; a sentence says why no other number works; a sentence says why the new piece is an angular momentum. | Done |
| C4 | 5 | Theme 2: four steps in one paragraph, and no plain reason for the two. | Split into "Put the field in", "A slow particle", "Read off the magnet", "Where the two comes from". Header is now "The strength of the magnet". | Done |
| C5 | 8 | The reason for the reshuffle was incomplete (the mass term also gets the wrong sign). | Step two rewritten. | Done |
| C6 | 8 | Theme 2, and a minus sign left unexplained in "The charge flips". | Written with $\hat p_x - qA_x$; a sentence follows the minus sign. | Done |
| C7 | 8 | "Every item in the table is reversed" contradicted the Mass row. | "Every item except the mass". | Done |
| C8 | 8 | "Complex conjugate" was never defined in a main text. | One-line definition with a Math Refresher link. | Done |
| C9 | 7 | Theme 3. | "Spin in motion" rewritten: a state with a definite energy needn't have a definite spin; spin along the motion is the exception. | Done |
| C10 | 7, 9 | Theme 4. | Sections 7 and 9 say what the number on $u$ and $v$ labels, and that the positron's spin is the opposite. | Done |
| C11 | 6 | The half angle was tied to $\hbar/2$ by assertion; chapter 2a's half angle is about a different angle; the reference beam wasn't mentioned; a neutron has no charge, so why is it a magnet. | Each has a sentence now. | Done |
| C12 | 2 | $\hat Y$ was never shown; "twice over"; the question paragraph asserted more than it argued. | The three spin matrices displayed; two sentences rewritten. | Done |
| C13 | 9 | The formula arrived with no example; $c = 1$ unexplained; $p\cdot x$ credited to chapter 4. | Example before and after; table rows added. | Done |
| C14 | boxes | Stale cross-references in the carried-over boxes; the symbol $\chi$ used for two things. | References fixed; the basis columns are $\xi_\uparrow$, $\xi_\downarrow$. | Done |
| C15 | all | Idioms: "by hand", "in its hands", "lives in", "in play", "dealings with light", "tidy", "the first sign of this". Small items: section 1 box numbers, section 4's link to chapter 2b's $\pm1$ and to chapter 5's warning, the table under the intro. | Replaced or added. | Done |
| C16–C19 | | Review suggestions Claude did not take. See the top of this file. | | Open for Hanh |
| C20–C22 | | Small leftovers. See the top of this file. | | Open |

## D. Closing review of the revised draft (2026-11-26)

One fresh agent, no history, did a rating review and a reader test of the page after iteration C. Claude has changed nothing since, so these are all open.

**Ratings:** 7.5 out of 10 against chapters 3 to 5, 8 for structure (up from 7 and 7.5). It rechecked the physics and found it right.

**A theme that keeps coming back.** D3 is the third review in a row to say section 3's "Why" doesn't follow, and D2 is the second to say section 5's main text doesn't carry its own argument. Both sections hold the chapter's two main results, so they deserve Hanh's eye first.

#### D2 Section 5: the lower pair is fed back, not removed

- Kind: GAP, recurring
- Status: Done in iteration F.
- Finding: The text says the lower pair is tiny "so" it can be removed. A reader takes that as "ignore it", and ignoring it gives no magnet at all. The result comes from the small lower pair fed back into the upper pair's equation.
- Claude's recommendation: Take it. Replace the paragraph up to "The energy comes out as" with:

> **A slow particle.** Take a slow particle with positive energy, in a field of strength $B$ pointing up. Its lower pair is tiny: at a hundredth of the speed of light it holds 0.0025% of the chance (section 7 works this out). But we can't drop it, because each $\alpha$ sends one pair to the other, so the equation for the upper pair contains the lower pair. The equation for the lower pair gives it as the momentum term acting on the upper pair, divided by $2mc$. Put that back into the upper pair's equation, and the momentum term has acted twice, once on the way down and once on the way back (box). That leaves an equation for the upper pair alone, and its energy comes out as

And start "Where the two comes from" with: "The momentum term acted twice, so it appears squared, and that square gives the energy of motion, $p^2/2m$, with its $2m$."

#### D3 Section 3: "Why" still jumps from turning to the commutator

- Kind: GAP, recurring (third review to raise it)
- Status: Done in iteration F.
- Finding: No chapter says that "$\hat L_z$ commutes with $\hat H$" and "$\hat H$ looks the same after a turn" are the same statement.
- Claude's recommendation: Take it. Replace the paragraph with:

> **Why.** Chapter 1's argument has a quantum form: $\hat L_z$ commutes with $\hat H$ exactly when $\hat H$ looks the same after the particle's motion is turned about the vertical axis. So look at what such a turn does to Dirac's $\hat H$. The turn mixes the $x$ and $y$ parts of the momentum. After a quarter turn, what was $\hat p_x$ is $\hat p_y$. But $\alpha_x$ and $\alpha_y$ act on the column, and turning the motion doesn't change the column. So after the turn $\alpha_x$ stands in front of the wrong part of the momentum, and $\hat H$ has changed. $\hat H$ stays the same only if the turn also mixes $\alpha_x$ with $\alpha_y$, which means turning the column too. $\hat L_z$ contains only positions and momenta, so it can't do that.

#### D4 Section 3: the formula for $L_z$ arrives unexplained

- Kind: GAP
- Status: Done, see E9.
- Finding: A reader can't see why $x\,p_y - y\,p_x$ is "distance times momentum", or why it has a minus sign.
- Claude's recommendation: Take it. Replace the sentence "For a particle anywhere in space, the same quantity for turning about the vertical axis, $z$, is" with:

> A particle anywhere in space gets the same quantity in two parts, for turning about the vertical axis, $z$. If it sits a distance $x$ out along the $x$ direction and moves along $y$ with momentum $p_y$, it is going round the axis one way, and it contributes $x\,p_y$. If it sits a distance $y$ out along the $y$ direction and moves along $x$, it is going round the other way, and it contributes $-y\,p_x$. Together,

#### D5 Section 8: three sign changes tracked in prose

- Kind: GAP
- Status: Done in iteration F.
- Finding: The reader has to follow three terms through two steps in one sentence.
- Claude's recommendation: Take it. Keep the displayed line. Replace "Inside the bracket ... charge $-q$." with a table:

> Follow the three terms of the equation through both steps.
>
> | Term | After conjugating | After the fixed matrix |
> | --- | --- | --- |
> | Rate of change in time, $i\hbar\,\partial/\partial t$ | Sign flipped | Sign flipped |
> | Momentum with the field, $-i\hbar\,\partial/\partial x - qA_x$ | Sign flipped, and $-qA_x$ has become $+qA_x$ | The same |
> | Mass, $\beta mc^2$ | Unchanged | Sign flipped |
>
> After both steps every term carries the same minus sign. Multiply the whole equation by $-1$ and the signs are gone. What remains is the Dirac equation with $+qA_x$ where $-qA_x$ stood, so $\psi_c$ obeys the Dirac equation for a particle of charge $-q$.

#### D6 Section 9: the second term, and the table row for $v_s(p)$

- Kind: GAP and a small error
- Status: Done in iteration F.
- Finding: "The label $s$ is different" doesn't say different from what, and the step to the positron's momentum skips a reading. The table row says $v_s(p)$ is section 7's column times a factor, which is true only for momentum $-\mathbf p$.
- Claude's recommendation: Take it. Replace the paragraph with:

> **The second term.** Its wave is $e^{+ip\cdot x/\hbar}$, with both signs reversed. Read on its own, it has energy $-E_p$ and momentum $-\mathbf p$. By section 8, a negative-energy wave with momentum $-\mathbf p$ matches a positron with energy $+E_p$ and momentum $+\mathbf p$. So the $\mathbf p$ in $v_s(p)$ names the positron's momentum. The $s$ doesn't get the same treatment. It still names which entry of the larger pair is filled, 1 for the spin-up entry and 2 for the spin-down entry, so the positron's spin is the opposite of the one $s$ names. $v_1$ goes with a spin-down positron.

And split the table row in two: "$u_s(p)$: section 7's positive-energy column, multiplied by $\sqrt{E_p + m}$ by convention" and "$v_s(p)$: section 7's negative-energy column for momentum $-\mathbf p$, with the same factor (first box)".

#### D7 Section 6: the reference beam, in one overloaded sentence

- Kind: GAP
- Status: Done in iteration F.
- Finding: One sentence carries the whole reason the two halves can be compared.
- Claude's recommendation: Take it. Replace the last sentence of the paragraph with:

> The half that is left alone needs a phase to compare with, and it has one. Without a field, up and down both have the energy we left out above, which lies midway between the $-\varepsilon$ and $+\varepsilon$ of the half in the field. So the untouched half's phase turns at the midway rate. Against it, the up amplitude of the turned half has gained $+\theta/2$ and the down amplitude $-\theta/2$, as in the formulas above.

#### D8 Section 6: chapter 2a's hint reuses $\theta$ for a different angle

- Kind: GAP
- Status: Done in iteration F.
- Finding: Two paragraphs earlier $\theta$ was the swing round the vertical; here it is the tilt away from it.
- Claude's recommendation: Take it. Replace with:

> Chapter 2a had a first hint of this, for a different turn: a tilt away from the vertical, where this section swings round it. Its box gave a spin tilted from the vertical by some angle the amplitudes cos and sin of half that angle. Tilt it all the way round, by $360°$, and the up amplitude is $\cos 180° = -1$.

#### D9 Section 8: $E$ is signed in step one and positive in the table

- Kind: GAP
- Status: Done in iteration F.
- Finding: Step one says "energy $E$ ... if $E$ was negative"; the table writes $-E$ and $+E$ with $E$ positive.
- Claude's recommendation: Take it. After the definition of the conjugate, write:

> Take a negative-energy wave, with momentum $p$ and energy $-E$, where $E$ is positive. Conjugating it gives
> $$\left(e^{i(px + Et)/\hbar}\right)^* = e^{i\left((-p)x - Et\right)/\hbar},$$
> a wave with momentum $-p$ and energy $+E$. Conjugating has reversed both.

#### D10 Section 9 table: $p\cdot x$ credited wrongly

- Kind: ERROR (cross-reference)
- Status: Done in iteration F.
- Finding: Chapter 4's box wrote $A^\mu B_\mu$, never $p^\mu x_\mu$. Nothing says $x$ in $\psi(x)$ now means time and position together.
- Claude's recommendation: Take it: "Short for $E_pt - \mathbf p\cdot\mathbf x$, which is chapter 4's summing rule $A^\mu B_\mu$ applied to $p$ and $x$. The $x$ in $\psi(x)$ stands for the time and the position together."

#### D11 Reference boxes: three signposting slips

- Kind: ERROR (signposting)
- Status: Done in iteration F.
- Finding: (a) "The box below" is two boxes down. (b) Section 8's box runs the map from positive to negative energy, the opposite way from the main text, without saying so. (c) The Heisenberg box writes operators as bold $\mathbf A$, which is the vector potential two sections later.
- Claude's recommendation: Take all three: (a) "The last box of this section"; (b) a first line in the section 8 box saying it runs the same map the other way and that applying it twice gives back the start; (c) $\hat A_H$ in the Heisenberg box.

#### D12 Section 1: the $q/2m$ rule needs the charge spread like the mass

- Kind: ERROR (overstated)
- Status: Done in iteration F.
- Finding: Only the box states the condition.
- Claude's recommendation: Take it: "For a body of charge $q$ and mass $m$, with the charge spread through it the same way as the mass,".

#### D13 Style: three agentless passives and one line standing alone

- Kind: STYLE
- Status: Done in iteration F.
- Finding: "is said to have spin one half" (section 4), "is replaced by" (section 5), "The star is written now" (section 9); and "He didn't ask for spin." (section 3, at the jump) stands alone as a punch line.
- Claude's recommendation: Take them: "physicists say the electron has spin one half"; "Replace each part of the momentum ... by"; "We write the star now"; and "Dirac asked only for an equation that agrees with relativity and has one rate of change in time, and the spin came out of it without his putting it in."

#### D14 Section 6 carries six threads; split it in two

- Kind: STRUCTURE
- Closed by M4; its jump link is removed.
- Finding: The review would split at "When a minus sign shows" into "One full turn flips the sign" and "Seeing the sign", so each section has one idea.
- Claude's recommendation: Hanh's call. Claude leans yes: the experiment gets its own section and header. It renumbers sections 7 to 10, and the links from other pages need repointing again.

#### D15 Section 7: $u$ and $v$ here are not chapter 5's $u$ and $v$

- Kind: GAP
- Status: Done in iteration F.
- Finding: Chapter 5's last section used $u$ and $v$ for the two pairs. Only the box says these are different.
- Claude's recommendation: Take it. Add: "Chapter 5's last section used the same two letters for the upper and lower pairs. From here on they mean whole solutions."

## E. Hanh's read (2026-11-26)

| ID | Section | Item | Status |
| --- | --- | --- | --- |
| E1 | 1 | Hanh on "It accounted for details in the light of atoms that nothing else explained": "what details?" The sentence now names the detail: close pairs of lines, with sodium's yellow as the example, and says why a magnet that points two ways along the field of the electron's own motion gives two energies. | Done |
| E2 | 1 | Hanh: the two-row table "just repeats the text but doesn't explain what was measured and how". Table removed. New paragraph "What was measured" says how chapter 2a's experiment gives the strength (the gap between the spots), before the spin proposal; "The mismatch" follows. "To within a tenth" is checked; the size of the gap is left out because Claude couldn't confirm it. | Done |
| E4 | 1 | Hanh: "put a diagram for this. the puzzles should be clearly presented with diagrams and emphasis since they drive the narrative". Two new figures: `sodium-pair.png` (one yellow line is two, with the two energy levels behind it) after "The spin", and `magnet-twice-too-strong.png` (expected gap against measured gap on the plate) after "The mismatch". | Done |
| E5 | 1 | Hanh: "so there are 2 puzzles?", then "remove the sodium one then altogether". Sodium text and figure removed. The puzzle is now built from chapter 2a's plate alone: two spots give $\hbar/2$ (new stated fact: angular momentum comes in steps of $\hbar$), the gap gives the magnet of a whole $\hbar$, and a table and a three-plate figure show the clash. Supersedes the sodium parts of E1 and E4. | Done |
| E6 | 1 | Hanh: "but why two spots mean ħ/2", "what wave?", "we haven't seen this kind of wave before", then "go with the box version". The main text states "steps of $\hbar$" as something physicists had learned from the light of atoms. A new box, "why angular momentum comes in steps of ħ", introduces the wave on a circle from chapter 2a's wavelength, with a figure (`wave-on-circle.png`), the odd count of results (stated without proof), and why two results need $\pm\hbar/2$. | Done |
| E7 | 1 | Hanh, after E1 to E6: section 1 "is ok so far". D12 is the only open item left in it. | Noted |
| E8 | 2 | Hanh on "Two different states can't agree in everything that can be measured": "why?" The general claim is gone. "The question" now says that energy and momentum can't tell $\psi_1$ from $\psi_2$, recalls that a vertical magnet tells up from down, and asks whether some measurement does the same here. | Done |
| E9 | 3 | Hanh on $L_z = x\,p_y - y\,p_x$: "why?", then "both". D4's text is in, with a sentence checking it on a circle, and a new figure `angular-momentum-parts.png` showing the two parts from above. Closes D4. | Done |
| E3 | all | Hanh asked for a structure rating. Claude: 7.5 out of 10. Proposed: split section 6 (D14), open section 7 with the question it answers, one sentence in section 6 tying the field's swing to section 3's turn, and perhaps fold section 9 into section 10. | Open for Hanh |

## F. Second bro-what test, and a whole pass for gaps (2026-11-26)

Hanh: "seems that there are quite a few gaps. can you run the bro what test?", then "if it finds gaps, it can fix them". A fresh agent ran a stricter test: any result stated with no reason the reader can follow counts as a gap, even when a box proves it. Its replies are in `06-bro-replies-2.md`. Claude then revised the page in one pass, taking the test's findings and the open D items together. The jump anchors were stripped for this pass.

| ID | Section | What changed | Status |
| --- | --- | --- | --- |
| F1 | 1 | The rule's condition (charge spread like the mass, D12); where its 2 comes from; whose mass $m$ is; why the results lie evenly either side of zero. | Done |
| F2 | 2 | The four matrices meet chapter 5's conditions; $\alpha_z$ worked on the column; what "at rest" means for a wave function; a remark on $\hat Y$'s imaginary entries. | Done |
| F3 | 3 | Each bare result has a reason: where the commutator comes from, why $\hat Z$ is the matrix to try, why the two commutators cancel. "Why" rewritten (D3). The lone closing line merged (D13). | Done |
| F4 | 4 | The link from the two results to the plate now points to section 5; one passive removed (D13). | Done |
| F5 | 5 | Rewritten (D2). The lower pair is fed back, not removed. The energy shows both magnets in one line, the motion's with $L_z$ and the spin's with $\hbar\hat Z$, each with $q/2m$ in front. "Where the two comes from" now says: the field treats $\hbar\hat Z$ like $L_z$, but the angular momentum is only half of $\hbar\hat Z$. $\mathbf A$ gets a picture. The box gains the motion's magnet. | Done |
| F6 | 6 | The derivation starts from section 5's energy, so the half is visibly the $\tfrac12$ of $\hbar/2$ (no more $\varepsilon$). It says why the swing is a turn of the spin and that the Dirac column turns the same way. Chapter 2a's hint is marked as a different turn (D8). The reference beam is spelled out (D7). Section 1's half wavelength is picked up. | Done |
| F7 | 7 | The row of the equation behind $r$; $r$ in terms of the speed; why motion along $z$ fills the third entry and along $x$ the fourth; names moved before the sideways case (D15). | Done |
| F8 | 8 | One meaning of $E$ (D9). Which terms change sign and why the mass term is the odd one out; what each swap of the fixed matrix repairs; the three-term table (D5). "Matches" became "becomes". | Done |
| F9 | 9 | Table rows for $\mathbf p\cdot\mathbf x$, $p\cdot x$, $u_s$ and $v_s$ (D6, D10); "The second term" rewritten (D6); what $x$ and the star mean. | Done |
| F10 | boxes | Signposting slips (D11). | Done |

## G. Third check, and its fixes (2026-11-26)

A fresh agent ran the bro-what test again and redid the algebra of sections 1, 3, 5, 6, 7, 8 and 9. Its replies are in `06-bro-replies-3.md`.

**Result:** 8 out of 10 for how well a reader with the earlier chapters can follow the main text. All the algebra checks out. It found no complaint that repeats across sections. Claude applied its eight fixes. No review has run since, so G1 to G8 are unreviewed.

| ID | Section | Finding | Fix | Status |
| --- | --- | --- | --- | --- |
| G1 | 9 | Wrong cross-reference: the promise is in chapter 5's section 10, not its last section. | Corrected. | Done |
| G2 | 5 | The left-out $B^2$ term is small for an electron held in an atom, not for a free one circling in the field. | The sentence now says so, with the size. | Done |
| G3 | 5 | The main text said why the angular momentum is $\hbar/2$ but not why the field sees a whole $\hbar$. "Nothing was assumed" overstated. | One sentence: the momentum term acted twice, and $\hat S\hat Y = i\hat Z$ has no $\tfrac12$. "No factor of two was put in." | Done |
| G4 | 5 | $L_z$ appeared in the energy with no reason in the main text. | One clause on $\mathbf A$ going round the axis. | Done |
| G5 | 8 | "That undoes the $i$ in $\hat Y$" was wrong as stated: the swap inside a pair alone doesn't do it. | The bullet now says the two pairs also get opposite signs, and what the net effect on the three $\alpha$'s is. | Done |
| G6 | 7 | The row equation appeared rearranged. | The row is shown before the term is moved across. | Done |
| G7 | 3 | The hinge of "Why" was asserted. | Marked as taken on trust, with the comparison to $\hat p_x$ as a slope. Chapter 1's rule is quoted in its own words (the Lagrangian). | Done |
| G8 | 6 | "Grown by $\theta$" had the sign loose; "every direction" was asserted. | "Changed by"; "whatever state the spin starts in". | Done |

## H. Hanh's read, sections 1 to 3 (2026-11-26)

Hanh read the page after iterations F and G and sent eight notes. The common thread, in Hanh's words on the first: "i dont need to know that in the main text if it's in the box". Several of these undo reasons that the pass for gaps (F, G) had added to the main text.

| ID | Section | Hanh's note | What changed | Status |
| --- | --- | --- | --- | --- |
| H1 | 1 | On "The 2 comes from comparing the ring's area...": "i dont need to know that in the main text if it's in the box". | Sentence removed (it was added in F1). | Done |
| H2 | 1 | "the table repeats the diagram. discard the table". | The two-row table of spots and strengths removed; the three-plate figure stays. | Done |
| H3 | 2 | On "the two-by-two matrix that changes nothing": "add the identity def". | Named the identity matrix and displayed it. | Done |
| H4 | 3 | On the pendulum sentence: "awkward prose". | Rewritten without the formula. | Done |
| H5 | 3 | On the two parts of $L_z$: "hard to read. simplify the English". | Two short bullets, then "Add the two". The check at two points of the circle (F3) removed. | Done |
| H6 | 3 | On "as the pendulum's angle had the momentum...": "don't repeat equations that aren't relevant". | Removed, with the extra reason for the Schrödinger case (both from F3). | Done |
| H7 | 3 | On "Why": "very hard to follow". | Five sentences: each direction of momentum has its own matrix; a turn changes the directions and not the matrices; so they no longer match. The "quantum form taken on trust" (G7) is gone. | Done |
| H8 | 3 | On the missing piece: "If you are saying that you need to add a term to compensate for the non zero commutator, you probably just do that. It would be easier to understand". | It now says: add a term whose commutator cancels the first; here it is; the sum is kept. The reasons about the spin matrices' orders (F3) stay in the box only. | Done |
| H9 | 3 | On "For the free Schrödinger equation it is.": "?", then "just ditch it". | Sentence removed. The box keeps the Schrödinger line. | Done |
| H10 | 3 box | On "Operators for different directions commute": "how do we know that?", then "i want this in the box, but use equations". | The commutator box now shows $\hat p_x(x\psi)$ against $\hat p_y(x\psi)$, then $[\hat x,\hat p_y]=0$, then the two momenta. | Done |

## I. Section 3 without the symmetry argument (2026-11-26)

Hanh worked through section 3 line by line (H9, H10), then stopped at the "Why" paragraph after three attempts to reword it: "the worst part is that i know what you are trying to say. you are trying to present rotational symmetry. but this is very hard to understand". Claude proposed dropping the symmetry argument from the section; Hanh: "yes, ditch the why".

| ID | Section | What changed | Status |
| --- | --- | --- | --- |
| I1 | 3 | "Why" removed. The page no longer says why the check fails for the motion alone; "Where this comes back" points to Symmetries for it. | Done |
| I2 | 3 | "Why it should be kept" no longer uses chapter 1's rule about a coordinate. It says nothing twists a free particle, with the skater as the everyday case. | Done |
| I3 | 3 | "The missing piece" is motivated by angular momentum not coming from nowhere, then adds the term. | Done |
| I4 | 3 | "What that means" no longer claims the term "is what a turn does to the column", which the page never showed. | Done |
| I5 | 3 | Opening says what the section does. Cut: the reason inside the momentum example, the sentence about the circle, the three-row kept/not-kept table (it restated the text). | Done |
| I6 | 3 | Proposed, not done: move the Heisenberg reference box to section 10. | Waiting for Hanh |
| I7 | 3 | Hanh on "So look for a second term... There is one": "this is out of a hat". The term is now found in steps: write what its commutator must be; it can be a matrix; it must swap $\alpha_x$ and $\alpha_y$; the spin matrices do that, so try $\Sigma_z$; the number in front fixes $\hbar/2$. | Done |

Hanh, after I7: "section 3 is ok". Sections 1 to 3 are now read and accepted, apart from I6.

## J. Hanh's read, section 4 (2026-11-26)

| ID | Section | Hanh's note | What changed | Status |
| --- | --- | --- | --- | --- |
| J1 | 4 | On "the matrix is two copies of $\hat S$": "S?", then "i don't think we need the explicit formula. the reader understands that Z isn't special". | "Any direction" no longer names $\hat S$ or its eigenvalues. It says the result is the same along any direction and that a sideways state is an equal mix. The sentence on chapter 2a's two amplitudes is its own paragraph. | Done |
| J2 | 4 | On "On a line, the two entries were the two signs of the energy...": "ditch this". | The paragraph comparing chapter 5's column of two with the pairs is removed, with its lead-in sentence. | Done |
| J3 | 4 | "what's the point of bringing back chapter 2a. from so far back", then "yes, ditch it". | "Any direction" is now two sentences. The sideways mix and the paragraph on chapter 2a's two amplitudes are removed. To check when Hanh reads section 6: it uses chapter 2a's two amplitudes and must now introduce them without help from section 4. | Done |

Hanh, after J3: "section 4 is ok". Sections 1 to 4 are read and accepted.

## K. Section 5 rebuilt around the puzzle (2026-11-26)

Claude listed four passages to lighten. Hanh: "i don't see what's the point of this section". The section reached section 1's puzzle only in its fourth part, after three parts of machinery. Claude proposed leading with the puzzle and moving the machinery to the box; Hanh: "yes, rewrite it".

| ID | Section | What changed | Status |
| --- | --- | --- | --- |
| K1 | 5 | New order: the puzzle again; what to ask the equation (a magnet is an energy difference in a field); the answer as the two energies of spin up and spin down; twice the rule, as a ratio; the table; the sign of the charge; the small excess. | Done |
| K2 | 5 | Out of the main text: $\mathbf A$ and the replacement of the momentum, the elimination of the lower pair told in words, the four-term energy, the bullets reading off two magnets, the $B^2$ term, and the paragraph on $\hat S\hat Y = i\hat Z$ (G3, G4, G2). | Done |
| K3 | 5 box | The box gained "All the terms": the full energy with each term named, the link to the main text's $E_0$, and the $B^2$ term with its size. | Done |

## L. The chapter split in two (2026-11-26)

Hanh, after section 5: "this chapter seems too long. no?" Claude counted the main text without formulas: 6,380 words, against 3,790 for chapter 5 and about 2,300 to 2,500 for chapters 3 and 4. Claude proposed a split along the page's two stories, as chapters 2a and 2b do; Hanh: "yes, split it".

After the split: 6a has 4,140 words of main text and 1,590 in boxes; 6b has 2,470 and 2,070.

| ID | What changed | Status |
| --- | --- | --- |
| L1 | New page `docs/dirac-solutions.md`, "Solutions of the Dirac Equation", with old sections 7 to 10 as its sections 1 to 4. Its opening lists three facts carried over from 6a and has the table of four entries with the positron column. | Done |
| L2 | `docs/dirac-equation.md` ends after section 6. Its opening no longer promises the moving electron or the positron, and its table has lost the positron column. "Where this comes back" and Previous/Next point to 6b. | Done |
| L3 | Cross-references inside 6b renumbered; references to old sections 1 to 6 now say "chapter 6a's section N" and link across. | Done |
| L4 | Links from other pages repointed: `qft.md`, `field-quantization.md`, `qft-action.md`, `appendix-math-groups.md`, `feynman-rules.md` (the $u(p)$ link). Every anchor link into the two pages checked against the built site. | Done |
| L5 | Sidebar and navbar (`config.js`), the home page grid (card "06b"), and the PDF chapter list have the new page. | Done |
| L6 | Chapter 5's "Where this comes back" line about the next chapter now says the chapter after it does the pairing with positrons. One sentence changed on a finished page. | Done |
| L7 | Section 6's first sentence cited section 3's removed "Why" paragraph. Removed. The review anchor for D14 sat on the heading's line and stopped the heading rendering; moved to its own line. | Done |
| L8 | Names chosen by Claude without asking: the file name, the title "Solutions of the Dirac Equation", the sidebar label "Dirac Solutions", the labels "6a" and "6b". | Waiting for Hanh |
| L9 | Not done: the quiz still lists one "The Dirac Equation" set covering both pages. 6a is still long (4,140 words), mostly section 6 (1,180 words, no box). | Open |

## M. Section 6 shortened (2026-11-26)

Hanh: "i have read section 6 and it is quite tedious". The section derived the half-angle rule step by step before saying what it was for, with callbacks to chapters 2a, 2b and sections 1 and 5.

| ID | Section | What changed | Status |
| --- | --- | --- | --- |
| M1 | 6 | New order: the claim (one full turn gives $-1$) with its figure; where the half comes from, as one paragraph and the two formulas; how a minus sign can show; the experiment; the name. Main text went from 1,180 words to about 430. | Done |
| M2 | 6 | New box, "The calculation: a spin turning in a magnetic field", holds the derivation, why $\theta$ is the angle of the turn, what cancels, and the two earlier hints from chapter 2a and section 1. | Done |
| M3 | 6 | Cut: the three-row table (the figure shows the same), the sentence on whole-number spins. | Done |
| M4 | 6 | D14 (split section 6 in two) is closed by this rewrite; its review anchor is removed from the page. | Done |

## N. Section 5's box simplified (2026-11-26)

Hanh on the box: "the derivation is long and complex". Claude proposed doing it for a field pointing up only; Hanh: "yes".

| ID | Section | What changed | Status |
| --- | --- | --- | --- |
| N1 | 5 box | The calculation is four numbered steps for a field along $z$. Gone: $\nabla\times\mathbf A$, the cross product, the general identity for $(\boldsymbol\sigma\cdot\mathbf a)(\boldsymbol\sigma\cdot\mathbf b)$, and the letter $\boldsymbol\sigma$. It reuses section 3's box for $[\hat x,\hat p_x]$ and chapter 5's box for $\hat S\hat Y = i\hat Z$. Claude checked each line by hand; no fresh agent has. | Done |
| N2 | 5 box | The motion's magnet, the full list of terms and the name $g$ moved to a second box, "Reference: the motion's magnet, and the usual name". The $B^2$ term is now written out as $q^2B^2(x^2+y^2)/8m$. | Done |
| N3 | 6b §2 | To check when Hanh reads 6b: its "The charge flips" says section 5 "put the field in by replacing $\hat p_x$ with $\hat p_x - qA_x$" and speaks of the arrows of $\mathbf A$. Since K, 6a's main text no longer introduces $\mathbf A$; only the box does. | Open |
| N4 | 5 | Hanh: "section 5, remove the small excess part". | The paragraph on Kusch and Foley's 1947 measurement is removed. | Done |
| N5 | 5 | Hanh: "drop the table". | The table of three ratios is removed; with the excess gone its measured row had no explanation. | Done |
| N6 | 5 box | Hanh: "remove too". | The measured $g = 2.0023$ is removed from the reference box. The page no longer mentions the excess over Dirac's value. | Done |
| N7 | 5 box | Hanh on $\mathbf A = (-By/2, Bx/2, 0)$: "why /2 ?", then "yes, add it". | Step 1 now says the field is the swirl of the arrows and shows $\partial A_y/\partial x - \partial A_x/\partial y = B/2 + B/2 = B$. | Done |

Hanh, after N7: "section 5 is ok". Sections 1 to 5 of 6a are read and accepted.

## O. Section 6 rebuilt on the half angle (2026-11-27)

Hanh read the shortened section 6 (M) and asked three questions about its box and its claim: whether the phase's rate depends on the energy and the energy on the spin (yes); "but why does it relate to 'turning' the electron in space?"; "but here you are talking about the spin from its state representation in the wave fn?". Then: "it seems that the result isn't so surprising when we consider that one is space (full turn) and the other is state (half turn). no?" and "it was already strange when up/down are orth in state space, no?". Claude agreed that this is the same fact and proposed building the section on it; Hanh: "yes, rewrite it".

| ID | Section | What changed | Status |
| --- | --- | --- | --- |
| O1 | 6 | New spine: up and down are opposite in space and at right angles in the state; chapter 2a's tilted state has cos and sin of half the angle; carry the tilt once round and the state is $(-1, 0)$. The field and the two phase formulas are out of the main text. | Done |
| O2 | 6 | New figure `half-angle-state.png` (scene `HalfAngleState`): the spin in space above, the state's arrow below, for 0°, 180°, 360°, 720°. It replaces `spinor-rotation-sign.png` on the page; that file and its scene are left in place, unused. A four-row table sits beside it. | Done |
| O3 | 6 | "Seeing the sign" now says what a direction in space is (what a measurement finds), so that the sign lives in the state only. The tone of a surprise is toned down; the heading is unchanged to keep its links. | Done |
| O4 | 6 box | Retitled "a turn about the vertical, made by a magnetic field". Its opening is reworded in Hanh's order (the phase's rate depends on the energy, the energy on the spin), without the letter $s$. It now carries the two phase formulas and the line for one full turn. | Done |
| O5 | 6 | The table and the figure showed the same four cases. Hanh: "drop the table". Table removed; the $360°$ case is now worked from the formula in one line, and the figure follows. | Done |

Hanh, after O5: "section 6 is ok." All six sections of 6a are read and accepted. Iterations G to O have had no fresh review.

| ID | Section | What changed | Status |
| --- | --- | --- | --- |
| O6 | Where this comes back | The pointer to Symmetries (added in I1) said that chapter explains why the check of section 3 fails for the motion alone. Claude read the chapter: it does not. Its sections 3 and 4 are about space against state and how turns act on a spin state, so the pointer now says that and refers to section 6. | Done |

## P. Five fresh reviews of 6a (2026-11-27)

Hanh asked for five reviews of `docs/dirac-equation.md` after accepting sections 1 to 6: structure, physics accuracy, legibility, bro what, prose. Five fresh agents ran in parallel with no history, barred from `updates/`, `video/`, `audio/` and later chapters. Hanh decided P5, P7, P16 and P17 and said "rest follow recommendations". The fixes are applied; each item's block below says what changed.

**Ratings:** structure 7 · legibility 7.5 · bro what 8 for the main text and 7.5 for the boxes, nothing blocking · prose 8 · physics: accurate, no wrong physics, all algebra and all references to earlier chapters check out.

"Raised by" uses S (structure), A (accuracy), L (legibility), B (bro what), R (prose).

### Errors

| ID | Section | Finding | Raised by | Status |
| --- | --- | --- | --- | --- |
| P1 | 2 | "That matters in sections 5 and 7." The page has no section 7 since the split. Only section 5's box uses the swap. | S A L B R | Done: "Section 5's box uses this." |
| P2 | Intro | "The electron stays at rest throughout" is false: section 3 has a moving electron, section 5 a slow one. Added in L2. | S L B | Done: sentence removed; the next one says 6b follows a moving electron. |
| P3 | 4, 5 | Section 4 says the magnet "points along this spin"; section 5 ends "points opposite to its spin". | L | Done: section 4 now says the magnet "lies along the same line as this spin". |
| P4 | 2 | The line " These four meet..." starts with a space and has no blank line after the identity matrix, so it may render attached to the equation. | S L B R | Done: blank line added, space removed, "These four" is now "The four matrices". |
| P5 | 4, 6 | Section 6 argues with chapter 2a's list of two amplitudes and then names the Dirac column a spinor. Nothing says a pair of the column is that list, and chapter 5 told the reader "this column isn't a spin". The bro-what test calls this its strongest stumble. **The sentence that made this link was cut from section 4 at Hanh's request (J2, J3).** | S B R | Done. Hanh: "can you bring it back in section 5?" Section 5's "The answer" now says that for a slow particle the equation reduces to one for the upper pair, and that this pair is chapter 2a's list of two amplitudes. Section 6's "The name" picks it up in one clause. |

### Themes (raised by two or more reviews)

| ID | Section | Finding | Raised by | Status |
| --- | --- | --- | --- | --- |
| P6 | 3, 4 | Section openings with a noun that has nothing to refer to: "The quantity turns up in a check", "A measurement gives one of the operator's eigenvalues". | S L B R | See its block |
| P7 | 3 box | The Heisenberg reference box is off the page's line and written in textbook words ("time-independent Hamiltonian", "state-evolution factors", $H$ without a hat, a comma after the display). Move it to 6b or cut it to its first paragraph. Same as I6 and C17. | S L B R | See its block |
| P8 | 1, 3, 5, 6 | Restatement inside a section: section 1's factor of two "as an assumption" twice in two sentences; section 3's "nothing twists" four times; section 5's "The puzzle again. Section 1 left a puzzle" and the numbers re-run in "Twice the rule"; section 6's bold mid-section line nearly the same as the closing summary; the neutron caption repeating the text. | S L R | See its block |
| P9 | 2 | Notes about the site, not the story ("Chapter 5 showed the matrices only in its last section", "Chapter 5 showed $\hat Y$ only in a box"). The paragraph after the matrices holds three ideas; split it and label the second part "Two pairs". | S L R | See its block |
| P10 | 6 | "The state turns by the angle in space times the spin divided by $\hbar$" doesn't parse on a first read, and "The box checks this" overpromises: the box never mentions spin over $\hbar$. | L B | See its block |
| P11 | all | Pointers that don't land: bare "(box)" where a section has two or three boxes, "(second box)" for the light of atoms though that box doesn't mention light, "Section 1's box" when section 1 has three. | L B R | See its block |
| P12 | 5 | The end of "Twice the rule": the answer is followed by two afterthoughts (the motion's magnet, the sign of the charge). | S L | See its block |
| P13 | 1, 5 | $e$ against $q = -e$: section 1 says "the electron's charge $e$", section 5 "For the electron that is $e\hbar/2m$" and then "$q = -e$". $e$ is used a paragraph before it is named. | B | See its block |
| P14 | boxes | Notation: $\pi$ is the momentum in section 5's box and the number in section 1's; section 5's box sets $E$ equal to an expression with $\hat Z$ in it; section 6's box "turns it the other way, round the vertical" reads as the opposite direction; "vanishes" against "is zero". | L B R | See its block |
| P15 | boxes | Skipped steps in boxes: section 3's "how did $\hat p_y$ and $\alpha_x$ get outside"; section 5 step 2's block multiplication; the steps-of-$\hbar$ box moving from "the angular momentum" to "along a chosen direction". | B A | See its block |

### Accuracy, loose but not wrong

| ID | Section | Finding | Status |
| --- | --- | --- | --- |
| P16 | 6 | The neutron result is idealised. The experiments saw a count repeating every 720° (Rauch: about 704° ± 38°) with partial contrast; the page and figure say it fell to zero at exactly 360°. | See its block |
| P17 | 1 | Uhlenbeck and Goudsmit's proposal is placed after the two-spot argument, but their evidence was the light of atoms. The sodium material was removed at Hanh's request. | See its block |
| P18 | 5 | "Which is what is measured": the measured factor is 2.0023. Hanh removed the excess on purpose (N4 to N6). | Kept |
| P19 | 6 | Chapter 2a's formula has a free overall phase, so its sign at 360° is a convention when read as a label. The conclusion is right because the formula is the state carried round by a real turn; the box makes the physical case. | Noted |

### Suggestions that go against a decision Hanh has made

| ID | Section | Suggestion | Status |
| --- | --- | --- | --- |
| P20 | 3 | Move the search for $\hat T$ (the spin-matrix commutators) from the main text to the box (S). Hanh accepted this passage after calling the earlier version "out of a hat" (I7). | Kept |
| P21 | 3 | Mention the Schrödinger comparison in the main text (S). Hanh: "just ditch it" (H9). | Kept |
| P22 | 2 | Cut the display of the identity matrix, unused later (L). Hanh asked for it (H3). | Kept |

### Figures and small prose

| ID | Where | Finding | Status |
| --- | --- | --- | --- |
| P23 | figures | Half-angle figure: state arrows thin and short. Three-plate figure: the measured plate has no strength label. Neutron figure: title "turn one half" reads as half a turn; the crystal label crowds the magnet label. Captions repeat the sentence printed inside three figures. | See its block |
| P24 | prose | One "just" (section 1, "proposed just that"). Four agentless passives. "Dirac's equation" three times against "the Dirac equation" five. "Two values" as a label where the text says "results". "So" opens 24 sentences, "Chapter N" 18. "To within a tenth" should say of what. | See its block |

### The items of P, one block each

These blocks feed the notes on the dev page: the list at its top and the note above each place. Hanh ticks an item there once it is checked. Run `python3 updates/refresh_links.py 06-dirac-equation` after editing the page or this file, and with `--strip` before a commit.

#### P1 Stale reference to a section 7

- Status: Done
- Change: Now reads "Section 5's box uses this."
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P1) · [source, line 123](../docs/dirac-equation.md#L123) · search text: `Section 5's box uses this.` (section 2)

#### P2 "The electron stays at rest throughout"

- Status: Done
- Change: Sentence removed. The next one says 6b follows a moving electron.
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P2) · [source, line 5](../docs/dirac-equation.md#L5) · search text: `The next chapter, 6b, follows a moving electron` (introduction)

#### P3 The magnet "along" the spin against "opposite to" it

- Status: Done
- Change: Section 4 now says the magnet "lies along the same line as this spin".
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P3) · [source, line 256](../docs/dirac-equation.md#L256) · search text: `lies along the same line as this spin` (section 4)

#### P4 Stray space after the identity matrix

- Status: Done
- Change: Blank line added, space removed, "These four" is now "The four matrices".
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P4) · [source, line 117](../docs/dirac-equation.md#L117) · search text: `The four matrices meet chapter 5's conditions` (section 2)

#### P5 A pair of the column is chapter 2a's list

- Status: Done
- Change: Hanh asked for the link in section 5. "The answer" says the equation reduces to one for the upper pair, which is chapter 2a's list of two amplitudes. Section 6's "The name" picks it up.
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P5) · [source, line 274](../docs/dirac-equation.md#L274) · search text: `is chapter 2a's list of two amplitudes` (section 5)
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P5-b) · [source, line 408](../docs/dirac-equation.md#L408) · search text: `Each pair of the Dirac column is such a list of two amplitudes` (section 6)

#### P6 Section openings with nothing to refer to

- Status: Done
- Change: Section 3 opens "The quantity that tells psi-1 from psi-2 turns up in a check". Section 4 names the spin's operator in its first sentence, and its label is now "Two results".
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P6) · [source, line 137](../docs/dirac-equation.md#L137) · search text: `The quantity that tells $\psi_1$ from $\psi_2$ turns up in a check` (section 3)
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P6-b) · [source, line 252](../docs/dirac-equation.md#L252) · search text: `A measurement of a quantity gives one of the eigenvalues of its operator` (section 4)

#### P7 The Heisenberg reference box

- Status: Done
- Change: Hanh: "move it". The box is now in chapter 6b, section 4, after the table of names, reworded in the page's terms ("energy operator", hats on every H, no stray comma). The three links from Fields and Quanta and Action and Lagrangians point there.

#### P8 Restatement inside a section

- Status: Done
- Change: Section 1: one sentence on the assumptions. Section 3: "nothing twists" is down from four times to two. Section 5: "Section 1 left a puzzle" removed. Section 6: the mid-section line is plain text; the neutron caption is one sentence.
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P8) · [source, line 40](../docs/dirac-equation.md#L40) · search text: `both the spin and the factor of two went in as assumptions` (section 1)
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P8-b) · [source, line 270](../docs/dirac-equation.md#L270) · search text: `**The puzzle again.** By section 1's rule` (section 5)
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P8-c) · [source, line 382](../docs/dirac-equation.md#L382) · search text: `So an angle in space shows up as half that angle in the state.` (section 6)
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P8-d) · [source, line 404](../docs/dirac-equation.md#L404) · search text: `*The neutron experiment, sketched.*` (section 6, caption)
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P8-e) · [source, line 166](../docs/dirac-equation.md#L166) · search text: `If the motion's share changes, the electron must carry` (section 3)

#### P9 Section 2: notes about chapter 5, and a paragraph with three ideas

- Status: Done
- Change: The two notes about what chapter 5 showed are gone. The paragraph is split, with a new label "Two pairs". "At rest" says why the wave function is the same everywhere.
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P9) · [source, line 105](../docs/dirac-equation.md#L105) · search text: `**The four matrices.** Each is` (the notes about chapter 5)
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P9-b) · [source, line 119](../docs/dirac-equation.md#L119) · search text: `**Two pairs.** Think of the column` (the new label)
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P9-c) · [source, line 125](../docs/dirac-equation.md#L125) · search text: `**At rest.** A particle at rest has zero momentum` (at rest)

#### P10 Section 6: "Where the half comes from"

- Status: Done
- Change: Rewritten in short sentences: the state turns by a fraction of the angle, the fraction is the spin divided by h-bar, one half for the electron and one for a whole h-bar. The box has a new line showing that fraction.
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P10) · [source, line 394](../docs/dirac-equation.md#L394) · search text: `**Where the half comes from.** The half is` (main text)
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P10-b) · [source, line 419](../docs/dirac-equation.md#L419) · search text: `Each phase is $\tfrac{q}{m}Bt$ times the spin` (the box)

#### P11 Pointers that do not land

- Status: Done
- Change: Section 1 names its boxes ("the box on the ring of charge", "the box on steps of h-bar"). Section 5 points to step 1 and step 2 of the first box. Section 6's box names section 1's box. Other bare "(box)" pointers in sections with one calculation box are unchanged.
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P11) · [source, line 26](../docs/dirac-equation.md#L26) · search text: `The box on the ring of charge works this out.` (section 1)
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P11-b) · [source, line 274](../docs/dirac-equation.md#L274) · search text: `which we state without deriving it (step 1 of the first box)` (section 5)

#### P12 Section 5: two afterthoughts after the answer

- Status: Done
- Change: The sign of the charge now sits under "The answer". The sentence on the motion's magnet is gone from the main text; the reference box has it.
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P12) · [source, line 282](../docs/dirac-equation.md#L282) · search text: `For the electron its size is $e\hbar/2m$, the measured value.` (section 5)
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P12-b) · [source, line 284](../docs/dirac-equation.md#L284) · search text: `**Twice the rule.**` (the paragraph now ends on the answer)

#### P13 e against q = -e

- Status: Done
- Change: Section 1 names e as the size of the electron's charge where it first appears. Section 5 says "its size is".
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P13) · [source, line 28](../docs/dirac-equation.md#L28) · search text: `Here $e$ is the size of the electron's charge` (section 1)
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P13-b) · [source, line 34](../docs/dirac-equation.md#L34) · search text: `with a charge of size $e$` (section 1)

#### P14 Notation in the boxes

- Status: Done
- Change: The momentum with the field is now capital Pi, so it no longer clashes with the number pi. The result line says Z-hat stands for its value. Section 6's box says "a different kind of turn". "Vanishes" is "is zero".
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P14) · [source, line 301](../docs/dirac-equation.md#L301) · search text: `Write $\Pi$ for the momentum after the replacement:` (section 5's box)
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P14-b) · [source, line 341](../docs/dirac-equation.md#L341) · search text: `With $\hat Z$ standing for its value` (section 5's box, the result)
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P14-c) · [source, line 413](../docs/dirac-equation.md#L413) · search text: `makes a different kind of turn, round the vertical` (section 6's box)

#### P15 Skipped steps in the boxes

- Status: Done
- Change: Section 3's box says why the other factors move out of the commutator. Section 5's step 2 shows the two equations before the mc-squared terms are moved. The steps-of-h-bar box says the count is about the axis of the circle and that the circle can be tilted.
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P15) · [source, line 222](../docs/dirac-equation.md#L222) · search text: `so they move out of the commutator:` (section 3's box)
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P15-b) · [source, line 313](../docs/dirac-equation.md#L313) · search text: `Move the $mc^2$ terms to the left:` (section 5's box)
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P15-c) · [source, line 82](../docs/dirac-equation.md#L82) · search text: `The circle can be tilted away from the direction we measure along` (steps-of-h-bar box)

#### P16 Section 6: the neutron result is idealised

- Status: Kept
- Change: Hanh: "leave it. no need to be pedantic".
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P16) · [source, line 406](../docs/dirac-equation.md#L406) · search text: `As the field went up, the count of neutrons coming out rose and fell.` (section 6)

#### P17 Section 1: Uhlenbeck and Goudsmit's motive

- Status: Done
- Change: Reworded so the page claims no motive: they "proposed an angular momentum of that size, belonging to the electron itself". It is its own paragraph.
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P17) · [source, line 32](../docs/dirac-equation.md#L32) · search text: `In 1925 George Uhlenbeck and Samuel Goudsmit proposed an angular momentum of that size` (section 1)

#### P18 The measured factor is 2.0023

- Status: Kept
- Change: Hanh removed the excess on purpose (N4 to N6).

#### P19 Chapter 2a's formula has a free overall phase

- Status: Noted
- Change: The conclusion is right, and the box makes the physical case. No change.

#### P20 Move the search for T-hat to the box

- Status: Kept
- Change: Hanh accepted this passage (I7). Two of its sentences were reworded for P6 and the bro-what test: why a matrix will do, and that the matrix is not alpha-z.
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P20) · [source, line 179](../docs/dirac-equation.md#L179) · search text: `It isn't $\alpha_z$, which swaps the two pairs.` (section 3)

#### P21 Bring back the Schrödinger comparison

- Status: Kept
- Change: Hanh: "just ditch it" (H9).

#### P22 Cut the identity matrix display

- Status: Kept
- Change: Hanh asked for it (H3).

#### P23 Figures

- Status: Done
- Change: Half-angle figure: thicker state arrows. Three-plate figure: the measured plate now carries its strength. Neutron figure: title says "turn one path". Two captions shortened so they no longer repeat the sentence printed in the figure. Not done: the crowded crystal label in the neutron figure, the small "axis" labels in the angular-momentum figure.
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P23) · [source, line 36](../docs/dirac-equation.md#L36) · search text: `./manim/magnet-twice-too-strong.png` (three plates)
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P23-b) · [source, line 390](../docs/dirac-equation.md#L390) · search text: `./manim/half-angle-state.png` (half angle)
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P23-c) · [source, line 402](../docs/dirac-equation.md#L402) · search text: `./manim/neutron-full-turn.png` (neutrons)

#### P24 Small prose items

- Status: Done
- Change: Fixed: the one "just", four passives, "the Dirac equation" throughout, "Two results", "to within ten percent", pronouns that leaned on a bold label. Not done: "So" still opens many sentences and "Chapter N" many others; the reviews counted 24 and 18.
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P24) · [source, line 30](../docs/dirac-equation.md#L30) · search text: `Nothing makes the up direction differ from the down direction` (section 1)
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P24-b) · [source, line 408](../docs/dirac-equation.md#L408) · search text: `Physicists call a column whose entries turn at half the angle` (section 6)

#### P25 "So" and "Chapter N" as sentence openers

- Status: Done. Hanh accepted the suggestion on the page.
- Change: Eight "So" openers changed where two or more followed each other closely (sections 1, 2, 3 and 6, and section 6's box), using "which means" or "therefore". Two "Chapter 2a" openers in section 6 changed. The rest are left.
- Finding: The prose review counted 24 sentences that open with "So" and 18 that open with "Chapter N". Left over from P24. Changing them all touches most paragraphs.
- Suggestion: Change only the runs, where two or three such sentences follow each other, and leave the rest.
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P25) · [source, line 20](../docs/dirac-equation.md#L20) · search text: `So anything charged that spins is a magnet.` (section 1: two "So" sentences in a row)
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P25-b) · [source, line 105](../docs/dirac-equation.md#L105) · search text: `**The four matrices.** Each is` (section 2: "Chapter 5" three times in a few sentences nearby)

#### P26 Two figure details

- Status: Done. Hanh accepted the suggestion on the page.
- Change: Neutron figure: the crystal label now sits inside the diamond of paths and says the plates are cut from one crystal, so it no longer crowds the magnet label. Angular-momentum figure: the "axis" labels are larger. Both rendered again.
- Finding: Left over from P23. In the neutron figure the "silicon crystal" label sits over one of the four plates and the magnet label crowds it. In the angular-momentum figure the "axis" labels are small.
- Suggestion: Fix both now and render the two figures again. Neither misleads as it is.
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P26) · [source, line 402](../docs/dirac-equation.md#L402) · search text: `./manim/neutron-full-turn.png` (neutron figure)
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P26-b) · [source, line 154](../docs/dirac-equation.md#L154) · search text: `./manim/angular-momentum-parts.png` (angular-momentum figure)

#### P27 Bare "(box)" pointers

- Status: Kept. Hanh accepted the suggestion on the page: leave them.
- Finding: Left over from P11. Section 3 has two bare "(box)" pointers and section 6 one. Each of those sections has one calculation box, so the pointer is not ambiguous.
- Suggestion: Leave them as they are.
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=P27) · [source, line 160](../docs/dirac-equation.md#L160) · search text: `work out its commutator with Dirac's $\hat H$ (box):` (section 3)

## Q. Closing review of 6a (2026-11-27)

One fresh agent, no history, errors only, after all the fixes of P. **Result: 9 out of 10. No error of physics, algebra or rendering.** It redid every calculation, opened all six figures, and checked every reference to an earlier chapter and every pointer inside the page. It found three small slips, all in how the page credits chapter 5 or sets up a step. They are on the dev page for Hanh to answer.

#### Q1 Section 2 credits chapter 5's box with a block-by-block product

- Status: Done. Hanh accepted all three suggestions (said in chat; the replies file was empty).
- Change: Now reads "using the two-by-two products from chapter 5's box".
- Finding: "Multiplying them block by block shows it, as in chapter 5's box." Chapter 5's box multiplies only two-by-two matrices. It never does a block-by-block product. The sentence was added in P9.
- Suggestion: Change it to "Multiplying them block by block shows it, using the two-by-two products from chapter 5's box."
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=Q1) · [source, line 117](../docs/dirac-equation.md#L117) · search text: `Multiplying them block by block shows it, as in chapter 5's box.` (section 2)

#### Q2 Boxes say chapter 5's box "gave" products that it only wrote out as matrices

- Status: Done. Hanh accepted all three suggestions (said in chat; the replies file was empty).
- Change: Both boxes now say chapter 5's box worked out the products and that their entries are those of i Z, -i Z and -i S.
- Finding: Section 5's box, step 3: "Chapter 5's box gave S Y = i Z and Y S = -i Z". Chapter 5's box shows those products as written-out matrices and never names them i Z. Section 3's box has the same slip in "In the same way Z Y = -i S".
- Suggestion: Say in both places that chapter 5's box worked out the products and that their entries are those of i Z, -i Z and -i S, as section 3's box already does for Z S.
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=Q2) · [source, line 329](../docs/dirac-equation.md#L329) · search text: `Chapter 5's box gave $\hat S\hat Y = i\hat Z$` (section 5's box, step 3)
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=Q2-b) · [source, line 240](../docs/dirac-equation.md#L240) · search text: `In the same way $\hat Z\hat Y = -i\hat S$ gives` (section 3's box)

#### Q3 Section 5's box, step 4, names one pair and then uses two

- Status: Done. Hanh accepted all three suggestions (said in chat; the replies file was empty).
- Change: Step 4 now names both pairs: Pi-x contains p-x and y, and Pi-y contains p-y and x.
- Finding: "With the field, Pi-x contains y and Pi-y contains p-y" introduces one pair that doesn't commute, and the sentence then quotes a second commutator, for p-x and x, whose pair it never mentioned. The algebra on the next line is right.
- Suggestion: Name both pairs: "With the field, Pi-x contains p-x and y, and Pi-y contains p-y and x."
- Jump: [rendered page](http://localhost:8080/dirac-equation.html?rev=Q3) · [source, line 333](../docs/dirac-equation.md#L333) · search text: `With the field, $\Pi_x$ contains $y$ and $\Pi_y$ contains $\hat p_y$` (section 5's box, step 4)

## R. The script for 6a (2026-11-27)

Hanh: "6a is final, commit and push", then "then work on the slide script". The page and the review tooling were committed and pushed (two commits on `classical-mechanics-rewrite`).

| ID | What | Status |
| --- | --- | --- |
| R1 | First draft of `video/scripts/06a-dirac-equation.txt`, written in one pass from the final page. About 3,340 words, against 3,420 for chapter 5. Format checked: allowed characters only, no sentence over 20 words, seven headings of at most 7 words, no questions. Formulas are pointed at as "on screen", not read out. A copy is kept as `script-v1.txt` in the scratchpad. | Done |
| R2 | First fresh review of the script. **Fidelity 9, overall 8.5, format clean.** Five must-fix items, four of them places where the script told the listener an earlier video had shown something it never showed: the four matrices, the word "spinor", the tilted-spin formula (it sat in a box of 2a), and the third spin matrix with the undefined word "imaginary". The fifth was a skipped step at 360 degrees. | Done |
| R3 | Applied all five, and the should-fix and bro-test items that fix a real problem: one name for "the momentum matrix for x", the swap told term by term, why a plain matrix leaves the momenta alone, "a multiple of" for the spin matrices' commutators, the two results tied back to the two spots, "exactly" dropped from the measured value, "from Vienna", arrows "on the page, not in space". Now about 3,490 words. Copy kept as `script-v2.txt`. Left as they are, both marked preferences by the review: the ratio rule said once in words, and "we met it in chapter one". | Done |
| R4 | Second fresh review, with no list of earlier fixes, reading the six earlier scripts to check every claim about what the listener has heard. **Fidelity 9, overall 9, format clean.** Two must-fix items: the magnet "points along its spin" and two sentences later "opposite to its spin" (the script had dropped the page's general charge); and "for the pendulum, it was the bob's momentum times its distance", which script 1 never said. | Done |
| R5 | Applied both, and six smaller items: two sentences that read a formula aloud, "the leftover" named where it first appears, the four matrices said to meet the last chapter's conditions, the new matrix distinguished from the momentum matrix for the vertical, the three plates introduced as "two predicted and one measured", and two bro-test rewordings. Not taken: the review's shorter version of the swap paragraph, which is what the first review had asked to be expanded. Now about 3,560 words. Copy kept as `script-v3.txt`. | Done |
| R6 | Closing review: a fresh agent, must-change items only. **Fidelity 9, overall 9, format clean, every back-reference borne out by the earlier scripts.** Two findings. A sign error in the swap step: the script compared the energy operator with "the leftover" but stated the signs of the requirement, which is minus the leftover (the page compares with the requirement). And "lies along this spin" in section 4 against "opposite to its spin" in section 5. | Done |
| R7 | Both fixed with the review's own wording: three sentences now say "the requirement", and section 4 says "lies along the same line as this spin". Claude checked the signs against the page's two displayed commutators. About 3,560 words. Copy kept as `script-v4.txt`. No review has run after these four one-phrase edits. | Done |
| R8 | For the deck: the slide for the swap step must show the requirement with its minus sign multiplied through, beside the energy operator, with terms aligned by momentum. Both reviews said this is where the script leans hardest on the screen. | Noted |
| R9 | Hanh read the script: "script is ok, do the pause file and the deck". | Done |
| R10 | Pause file `video/prosody/06a-dirac-equation.pauses.txt`: the script with 34 breath commas added, in the 32 sentences of 13 words or more that had none. Checked that it differs from the script by commas only. | Done |
| R11 | Deck `video/slides/deck_06a.py`, built by one agent against the final script: 129 slides for 369 sentences, 2.9 sentences a slide, none over 4. `check.py`: 0 problems. Smoke run: 0 of 129 slides failed. Colour choices to know: ORANGE is the x-momentum and TEAL the y-momentum (needed for the swap step), so negative energy is grey, unlike chapter 5's deck. | Done |
| R12 | Hanh: "finish unattended". Narration rendered with the Azure voice: 24.7 minutes, pauses from the pause file. Cover added to `video/slides/cover.py` and rendered: one full turn in space against a half turn in the state. | Done |
| R13 | Fresh deck review, with every contact sheet, about fifty full-size frames and the narration's timings: **8 out of 10, no wrong fact, sign or formula; all 23 "on screen" pointers have their formula on the slide when spoken; the swap step's signs are right.** Six must-fix items, all layout (frames and crosses cutting through symbols, braces on top of brackets, a label touching a box). Sixteen should-fix items (three slides opening blank, small type on key results, three reveals about 2 s off). | Done |
| R14 | The builder applied all six must-fix items, all the should-fix items, and one from Claude: the slide "One half, or one" drew a spin-one state in the electron's two-amplitude plane, which is not meaningful; it now shows a dial that turns by the whole angle. 28 slides changed, each re-rendered and opened at full size. `check.py`: 0 problems. Smoke run: 0 failures. Claude opened two of the changed slides (73 and 115). No fresh review has run after these fixes. | Done |
| R15 | Video built: `video/out/06a-dirac-equation/06a-dirac-equation-video.mp4`, 1920 by 1080, with audio and a subtitle track of 386 cues. Length 1,484.8 s (24 min 45 s), which is the narration's 1,479.9 s plus the 5 s cover hold. Claude looked at three frames taken from the video itself: the cover, the swap step mid-animation, and the neutron count. | Done |
| R16 | Description written, `06a-dirac-equation-description.txt`, with seven timestamps from the heading starts plus 5 s. Its "next chapter" link is the 6b page, which is on the branch but not yet read or reviewed. | Done |
| R17 | Hanh: "commit and push". The script, pause file, deck and cover entry are committed and pushed. Not done: upload. Everything in `video/out/` and `video/timings/` is generated and not committed. | Done |
| R18 | Hanh: "merge to main", then "always push to main". `main` fast-forwarded to `2eeca67` and pushed, which deploys the site with 6a and the unreviewed 6b page. | Done |
| R19 | YouTube. Hanh dropped the file on 2026-11-27 and said "finish up the yt publication". Claude reused chapter 5's details in Studio (playlist "QFT for dummies", tags, language, category, not made for kids), set the title "Phyz, Chapter 6a: The Dirac Equation" and the description from the description file, uploaded the cover as the thumbnail, waited for YouTube's checks (no issues found) and set it to public: https://youtu.be/krNvXJRgW4M. It is seventh in the playlist, after chapter 5. The "notify subscribers" setting was left as Studio had it. Nobody had watched the video end to end before publication. | Done |

---

## Index by section

| Section | Items |
| --- | --- |
| Whole page | A1–A10, B1–B4, C15, E3 |
| 1 | D12, E1, E2 |
| 2 | C12, E8 |
| 3 | C2, C3, C17 |
| 5 | C4, C16 |
| 6 | A4, C1, C11, C21 |
| 7 | C9, C10, C16 |
| 8 | C5–C8, C22 |
| 9 | C10, C13, C18 |
| 10 and boxes | C14, C19, C20, D11 |
| Iteration D | 1: D12 · 3: D3, D4, D13 · 5: D2 · 6: D7, D8, D14 · 7: D15 · 8: D5, D9 · 9: D6, D10 |
| Iteration R | script, pause file, deck and video for 6a: R1 to R19 |
| Iteration Q | closing review of 6a: Q1 to Q3 |
| Iteration P | reviews of 6a: P1 to P27 |
| Iteration O | 6: O1 to O5 |
| Iteration N | 5: N1, N2, N4 to N7 · 6b §2: N3 |
| Iteration M | 6: M1 to M4 |
| Iteration L | whole chapter: L1 to L9 |
| Iteration K | 5: K1 to K3 |
| Iteration J | 4: J1 to J3 |
| Iteration I | 3: I1 to I7 |
| Iteration H | 1: H1, H2 · 2: H3 · 3: H4 to H10 |
| Iteration F | 1: F1 · 2: F2 · 3: F3 · 4: F4 · 5: F5 · 6: F6 · 7: F7 · 8: F8 · 9: F9 · boxes: F10 |
