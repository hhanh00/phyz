# Chapter 6b updates: Electron and Positron (dissolved in iteration I)

This file tracks the work on chapter 6b: the page `docs/dirac-solutions.md`, and later its script, deck and video. The page was titled "Solutions of the Dirac Equation" until iteration D; the file name is unchanged.

The page was split off from chapter 6 on 2026-11-27. Its history before that is in `06-dirac-equation.md`, iterations A to L, where its sections carry the old numbers 7 to 10. Here they are sections 1 to 4.

Each round of work is an iteration with a letter. Each item in it has a number, so an item is referred to as, for example, A3. A new round gets a new letter, and old items are never renumbered.

Status words: **Done** (applied), **Open** (waiting for a decision or for work), **Kept** (decided to leave as is), **Noted** (for the record, no action).

Rules carried over: Claude doesn't start the script until Hanh says the page is final and it is committed. Open items go on the dev page with three choices (unresolved, accept suggestion, other), through `python3 updates/refresh_links.py 06b-dirac-solutions`; only open items show there. Run it with `--strip` before a commit. Pushes go to `main`.

## What is left to resolve

### Waiting for Hanh

| ID | The question | Claude's suggestion |
| --- | --- | --- |
| | Nothing here. Hanh moved the moving electron into chapter 6 and renamed 6a to 6; see `06-dirac-equation.md`, iteration S, for what that leaves open about the video. | |

### Waiting for work

Nothing. The page is dissolved.

---

## A. First pass, with the lessons of 6a (2026-11-27)

Hanh: "let's do chap 6b". The page was the second half of the old chapter 6, last revised in iterations F and G of the old file, which had added reasons to the main text. Hanh then cut that kind of sentence from 6a section after section ("i dont need to know that in the main text if it's in the box"). This pass applies the same cuts to 6b before Hanh reads it. It adds one sentence of new content, in the opening.

Main text: 2,470 words before, 2,060 after. Boxes: 2,220 before, 2,820 after.

| ID | Section | What changed | Status |
| --- | --- | --- | --- |
| A1 | Opening | Says what the page is for: chapter 5 could only say what the negative-energy solutions are through the filled sea, and this chapter gets it from the equation. "At rest throughout" is now "at rest or slow", the fault the reviews found in 6a's opening. | Done |
| A2 | 1 | Opens with what the section finds. The row-by-row algebra for the third entry moved to the top of the box; the main text states the solution. The note about chapter 5's use of $u$ and $v$ is gone from the main text (the box has it). "Spin in motion" is two sentences, and its two paragraphs are a new box, "More detail: the spin of a moving electron". | Done |
| A3 | 2 | "Step two" states what the fixed matrix does in two clauses; the two bullets on which matrix changes sign moved to the box. "The charge flips" is three sentences; the displayed conjugation and the table of three terms moved to the box. This also settles N3 of the old file: the main text no longer leans on $\\mathbf A$, which 6a's main text stopped introducing. | Done |
| A4 | 3 | "The second term" is shorter. The remark that the sum leaves no wave out moved to the box. | Done |
| A5 | all | "Dirac's equation" is "the Dirac equation", as in 6a. | Done |

#### A6 Section 1: the table of five speeds

- Status: Done. Hanh on the page: "keep but fewer rows".
- Change: The table keeps three rows: 0.01 c, 0.5 c and 0.99 c.
- Finding: The table gives the size of the lower entry and its share of the chance at five speeds, from a hundredth of the speed of light to 0.99 of it. It is the section's only worked numbers. Hanh cut several tables from 6a, each because it repeated a figure or the sentences beside it. This one repeats neither.
- Suggestion: Keep the table.

#### A7 Section 3: the table of the formula's pieces

- Status: Done. Hanh accepted keeping the table; the whole section then left the page in C.
- Change: Moved with section 3 to the reference page.
- Finding: The general solution is followed by a table of ten rows, one for each piece of the formula. It is long, but it is the only place the pieces are explained, and the next chapter starts from this formula.
- Suggestion: Keep the table.

#### A8 Section 3: the preview box

- Status: Done. Hanh accepted keeping the box; it then left the page in C.
- Change: Moved with section 3 to the reference page.
- Finding: The box "Preview: positive energies once the coefficients are operators" uses the next chapter's terms. An earlier review would have cut it. Its first line tells the reader to skip it for now, and the next chapter links to it.
- Suggestion: Keep the box.

#### A9 Section 4: the last box

- Status: Done.
- Change: Moved with section 4 to the reference page in C.
- Finding: "Working out rotations and boosts explicitly" is 1,070 words and multiplies out four block products term by term. An earlier review would keep one product and say the others go the same way. It is reference material in a box, and Action and Lagrangians links into it.
- Suggestion: Leave the box as it is.

## B. Four fresh reviews (2026-11-27)

Hanh, after the first pass and before reading: "rate it with for accuracy, prose, physics, bro what?". Four fresh agents ran in parallel, one per dimension, with no history. Nothing on the page has been changed in response.

| Review | Rating | In one line |
| --- | --- | --- |
| Physics | 9 | No wrong equation, sign, factor or table entry; many checks done numerically. Five plain-language sentences need a caveat. |
| Accuracy | 8 | No link, anchor or number is broken; all five rows of the speed table recomputed. Two errors and several loose credits to other chapters. |
| Prose | 8 main text, 4 boxes | The main text holds 6a's voice. The carried-over boxes read as a different, textbook site. |
| Bro what | 7.5 main text, 5 boxes | Nothing blocking in the main text; the reader can say what section 2 did. The thread is lost in section 3. The second half of section 2's box is blocking. |

**The theme all three reading reviews share:** the page has two voices. Every box passage written for the new page rates about 8; every passage carried over from the old page rates about 3 or 4. The old text says block, spinor, component, rotation, Hamiltonian, plane wave and negative-frequency where the page says pair, column, entry, turn, energy operator and wave.

The findings are grouped into seven items. Each is on the dev page with a suggestion.

#### B1 Seven plain errors

- Status: Done.
- Change: All five corrected in the rewrite of D: the summary says "has entries in both pairs"; the opening says chapter 5 explained the negative energies with the filled sea and only promised the modern answer; step two says conjugating leaves two terms as they were, and the box names them (the mass term and the slope along y); the wave is written along z; the box on the spin says "can't".
- Finding: Five of the seven remain after the cut in C. (1) Section 1's summary says a moving electron's solution "fills all four entries"; its examples fill two each, and the opening says "both pairs". (2) The opening says chapter 5 "could only say" what the negative-energy solutions are through the filled sea; chapter 5 also drops the sea and says they describe the creation of antiparticles. (3) Section 2 says conjugating flips "every term except the mass term"; the term with the slope along y has two i's and doesn't flip either. (4) Section 2 writes its wave along x and then speaks of spin up and down, but section 1's box says a sideways-moving state has no definite vertical spin. (5) That box says such a state "needn't" have a definite spin; it can't.
- Suggestion: Fix all five with the reviews' own corrections: "fills both pairs"; "chapter 5 explained those with Dirac's filled sea, and only promised the modern answer"; say conjugating flips the time term and two of the three slope terms, and the fixed matrix flips the rest; write section 2's wave along z; "can't".

#### B2 Section 2: the reason comes after the act

- Status: Done.
- Change: Done in the rewrite of D: a paragraph "What we want" comes before step one; the wave is built from $e^{i(pz - Et)/\\hbar}$ by putting in $-E$; the hole paragraph now says outright that it explains the spin's flip; "The pairs" is "What changes".
- Finding: Step one conjugates the wave and only then says what that achieved. The wave $e^{i(px + Et)/\hbar}$ appears with nothing saying why that is the negative-energy wave. The swap of spin up and down by the fixed matrix has no reason in the main text, though the later sentence about the hole supplies one. The label "The pairs" uses "pair" for two solutions, where the page uses it for the upper and lower pair.
- Suggestion: Open step one with what we want: to flip the sign of the energy without changing any chance. Show the wave as $e^{i(pz - (-E)t)/\hbar}$ before simplifying. After the fixed matrix, point ahead to the hole for the spin. Rename "The pairs" to "What changes".

#### B3 Section 3: where the reader loses the thread

- Status: Done.
- Change: Section 3 left the page in C, so its notation no longer has to be mended here. The findings go with it to whoever rewrites Fields and Quanta.
- Finding: Section 1 wrote the wave with a plus sign on the space part, and the formula here has a minus sign in the exponent, with nothing showing the two agree. Plain $p$ and $x$ now include the energy and the time, and differ from bold $\mathbf p$ and $\mathbf x$ only in weight. The table's pointer to chapter 4's summing rule goes to a box. The star on $b$ is explained two paragraphs after it appears. The sentence that sets $c = 1$ sits between the lead-in and the formula. One sentence is broken ("Add a second with a different momentum, each multiplied by...").
- Suggestion: In the table, say that plain $p$ and $x$ carry the energy and the time as well, and that $-p\cdot x = \mathbf p\cdot\mathbf x - E_pt$, which is section 1's exponent. Drop the pointer to chapter 4's rule. Add "(the star is explained below)" to the last row. Move the sentence about $c = 1$ before the lead-in. Mend the broken sentence.

#### B4 Section 4: a stray paragraph of index notation

- Status: Done.
- Change: Section 4 left the page in C.
- Finding: "The spin obeys $[S_i, S_j] = i\hbar\,\varepsilon_{ijk}S_k$..." sits in the main text between boxes, with no reason given. It makes "You don't need either to follow this chapter" untrue of the section. The section's opening also says "spinor" one paragraph before the table introduces the word.
- Suggestion: Move the paragraph into the first notation box, as one more name later chapters use. Say "how the column changes between observers" in the opening.

#### B5 The carried-over halves of the calculation boxes in sections 1 to 3

- Status: Done.
- Change: The three old halves left the page in C, unchanged, for the reference page. The boxes that remain are in the page's voice.
- Finding: Three boxes each have a new half in the page's voice and an old half in textbook voice: "Any direction" in section 1's box, "The same check on the two pairs" in section 2's, and the box on the columns in the sum in section 3. The bro-what test calls section 2's old half blocking: it runs the map in the opposite direction from the main text, writes $i\sigma^2$ where the line above has $\sigma_2$, uses "frequency sign", "standard representation" and "fixed-momentum convention" undefined, and repeats the charge argument in index notation. The physics in all three is correct.
- Suggestion: Rewrite the three old halves in the page's words and symbols, keeping every step: $\hat S$, $\hat Y$, $\hat Z$ for the spin matrices, "pair" for block, "column" for spinor, "wave" for plane wave. Cut the tail of section 2's box from "To restore charge" on, since the new half already makes the charge argument. Then have the physics checked again.

#### B6 Section 4's three reference boxes

- Status: Done.
- Change: The three reference boxes left the page in C, unchanged, for the reference page.
- Finding: "The notation: how a spinor changes between observers", "Deriving the covariant spinor transformation" and "Working out rotations and boosts explicitly" come from the old site. Two reviews say this reader cannot follow them: a matrix exponential and a double index sum arrive cold, with tanh, cosh, rapidity, "Hermitian", "unitary", "generator" and "covariance". The physics check confirmed all of it numerically. Action and Lagrangians and Fields and Quanta link into these boxes. The boxes never say which sense the angle of a turn has. This is also A9.
- Suggestion: Leave the content, since later chapters depend on it and it is correct. Put one plain line at the top of each box saying it is reference material written at the level of the later chapters. Fix only the mechanical faults: commas after displayed equations (ten), "thus" and "therefore" to "so", "rotation" to "turn", one index style for the matrices, and one sentence saying which way the angle turns. A full rewrite at this page's level would be a chapter's worth of work for material this page says the reader can skip.

#### B7 Small prose items in the main text

- Status: Done.
- Change: Done in the rewrite of D: "fills in" is down to one use; section 1 no longer opens with "That leaves"; the hole's reasoning is spelled out; "What this doesn't do" ends on what the next chapter does; the sentence pointing back to the table is gone; the passive is gone; z is named as the vertical.
- Finding: "Fills in" five times in section 1. "That leaves the negative-energy solutions", where "That" points at nothing. "The same reasoning covers the rest" (which reasoning). "For that, the wave function has to become a field" closes section 2 with no plain follow-up. "That's the table at the top of this chapter" comes straight before a summary that says it again. One agentless passive ("Every item except the mass is reversed"). The opening's last sentences have no joins. "Moving up along z" and later "the vertical" are never tied together.
- Suggestion: Apply the prose review's rewrites for each, which change wording only.

## C. Material for later chapters cut (2026-11-27)

Hanh, on the amount of maths in the boxes: "this section has ramped up significantly the math, esp in the boxes. is it required?" Claude: not for this page; the heavy material is there for later chapters. Hanh: "cut material that is used later. we will be either introducing it then, or not cover it. there is no point in doing it here". Asked two questions, Hanh chose to cut all of it, including section 3, and to park the cut text on a holding page with the later chapters' links repointed.

Main text: 2,060 words before, 1,220 after. Boxes: 2,820 before, 560 after. The page is now two sections.

| ID | What changed | Status |
| --- | --- | --- |
| C1 | Section 3, "The general solution", is gone from the page: the formula, the table of its pieces, "The second term", "Why a star on the b", and its two boxes. So is section 1's paragraph naming $u$ and $v$. | Done |
| C2 | Section 4, "The notation later chapters use", is gone: the table of names, the Heisenberg box, the commutation relations, and the three boxes on how a spinor changes between observers. | Done |
| C3 | The old halves of two calculation boxes are gone: "Any direction" in section 1's box, and the check on the two pairs in section 2's box. | Done |
| C4 | New page `docs/dirac-reference.md`, "The Dirac Equation: Reference Material", holds all of it, unchanged apart from its cross-references. It is not in the sidebar or the menu. Its first paragraph says what it is and that later chapters will take over what they need. | Done |
| C5 | Links repointed to the reference page in `qft.md`, `qft-action.md`, `field-quantization.md`, `feynman-rules.md` and `appendix-math-groups.md`. Every link into the three Dirac pages checked against the built site. | Done |
| C6 | 6a, a final and published page, lost one sentence and one clause that pointed at 6b's section 4. The home page card for 6b no longer promises the general solution. "Where this comes back" on 6b has one bullet. | Done |
| C7 | Debt for later: when Fields and Quanta, Action and Lagrangians, Field Quantization and Feynman Rules are rewritten, each introduces what it uses from the reference page or drops it, and the page is deleted once nothing links to it. The reviews' findings on that material (B3 to B6) apply then. | Noted |
| C8 | No review has run since the cut. The four ratings of B are for the page before it. | Open |

## D. The page restructured around the positron (2026-11-27)

Hanh: "rate this page structure". Claude: 6 out of 10. After the cut, the page had two sections that don't depend on each other: the opening raised the negative-energy solutions, and section 1 then spent a third of the page on the moving electron, which section 2 never uses. The title described the page before the cut, and there was no figure. Claude proposed putting the positron first; Hanh: "yes, restructure it".

Main text: about 1,290 words. Boxes: about 600.

| ID | What changed | Status |
| --- | --- | --- |
| D1 | The page is now titled "Electron and Positron". The file is still `dirac-solutions.md`. The sidebar, the menu, the home page card, the PDF list and the link labels in 6a, Fields and Quanta and the reference page follow. | Done |
| D2 | Section 1 is now "A negative-energy solution becomes a positron", the page's question and its answer. Section 2 is "A moving electron", shortened, and it opens as a correction to the table at the top: the upper pair has positive energy only at rest. Links from Fields and Quanta, Field Quantization and the reference page follow the new section numbers. | Done |
| D3 | New figure `electron-positron-flip.png` (scene `ElectronPositronFlip`): the negative-energy solution and the positron solution side by side, with energy, momentum, spin and charge reversed and the mass the same. It replaces the five-row table, which said the same thing. | Done |
| D4 | The open review items B1, B2 and B7 are absorbed in the rewrite; each block says how. Hanh had not answered them on the page. | Done |
| D5 | Not done: the figure Claude had proposed for section 2, the lower pair's share against speed. Hanh had already chosen to keep the table with fewer rows (A6), so it stays and no figure repeats it. | Kept |
| D6 | The published 6a video's description on YouTube calls the next chapter "Solutions of the Dirac Equation". The link still works; only the name is out of date. | Noted |
| D7 | Nothing had reviewed the page since the cut or the restructure. The four reviews of E then ran. Hanh has not read it. | Done |

## E. Four fresh reviews of the restructured page (2026-11-27)

Hanh: "run the reviews". Four fresh agents in parallel, one per dimension, on the page as it stood after the cut (C) and the restructure (D). Nothing has been changed in response.

| Review | Rating | Before the cut | In one line |
| --- | --- | --- | --- |
| Physics | 9 | 9 | Every equation, sign, table entry and number survived recalculation, most of it numerical. No physics error in the main claims. |
| Accuracy | 8.5 | 8 | Every reference, anchor and number checks out. Two errors, both from the restructure. |
| Prose | 7.5 main text, 8 boxes | 8 and 4 | The boxes now match the page. The main text lost half a point to sentences written in the restructure. |
| Bro what | 7 main text, 6 boxes | 7.5 and 5 | Nothing blocking. The recipe lands; the meaning of the result is where the reader wobbles. |

**What the reader says after section 1** (the bro-what test's words): "You take a negative-energy solution and flip every i to minus i, which turns the energy positive (and reverses the momentum) without changing any chance. That alone breaks the equation, because two terms didn't change sign, so a matrix shuffles the four entries to repair it. The result obeys the equation for the opposite charge with the same mass, so it's a positron."

**Two themes.** First, the page uses "lower pair", "entry" and "negative-energy solution" as if they were one thing, and section 2 then separates them (bro what, physics, accuracy). Second, most of the errors are in sentences Claude wrote during the restructure, and the opening has now overstated what chapter 5 and this page do in two different wordings (accuracy, both rounds).

#### E1 Six errors, all from the restructure

- Status: Done.
- Change: All six fixed in the pass of G: the alt text says up and down; the opening says this chapter takes the first step toward the full answer; section 1 opens on "a negative-energy solution"; "One operation does both" is gone; the charge's sign "comes out reversed against the momentum beside it"; the caption no longer credits the two steps with the charge.
- Finding: (1) The figure's alt text says the momentum arrows point right and left; the figure draws them up and down. (2) The opening says chapter 5 "only promised the modern answer" and that this chapter "gets that answer from the equation itself". The modern answer is the field, which this page doesn't deliver, as its own "What this doesn't do" says. (3) Section 1 opens "so the lower pair can't describe an electron as it stands"; that is true only at rest, and the section then uses a moving solution. (4) "It takes two steps" is followed a paragraph later by "One operation does both". (5) "The charge flips" says the term "comes out with the opposite sign from every other term"; the box says every term carries the same minus sign. (6) The caption says "the two steps" reverse the charge, which the text treats as a separate matter.
- Suggestion: Fix all six. Alt text: up and down. Opening: "This chapter takes the first step toward it: the equation itself pairs each negative-energy solution with a positron." Section 1: "so a negative-energy solution can't describe an electron as it stands". Drop "One operation does both" and say in step one that conjugating does both. The charge: "its sign against the momentum beside it is reversed". Caption: "The energy, the momentum, the spin and the charge are reversed. The mass is the same."

#### E2 Lower pair, entry and negative-energy solution used as one thing

- Status: Done.
- Change: Done in G: section 2 opens by saying a moving electron is still one electron and that the sign of the energy, not the filled entries, says which particle; after the table, "The share is not a chance of finding a positron"; section 1's summary says "At rest".
- Finding: Section 1 calls the lower pair the positron. Section 2 then gives a fast electron 43% of its chance in the lower pair, and a reader asks whether a fast electron is 43% positron. Nothing on the page answers. The bold summary of section 1 says "The four entries describe the electron and the positron" with no "at rest". In step two, "It swaps the upper pair with the lower pair" sounds like a second flip of the energy.
- Suggestion: Add three sentences and two words. After the speed table: "This is not a chance of finding a positron. The solution has positive energy, so all of it is electron." At the end of section 2: "The sign of the energy, not the pair, says which particle a solution describes." In step two: "The swap puts the larger part of the solution in the upper pair, where a positive-energy solution has it." And "at rest" in section 1's summary.

#### E3 The paragraph about chapter 5's hole

- Status: Done.
- Change: Done in G: the paragraph has its own label, "The same signs as chapter 5's hole", says physicists have dropped the sea, and presents the rule as a check that gives the same particle.
- Finding: It half helps, because "missing means minus" is easy to remember. But chapter 5 dropped the sea, and the paragraph's "That is why" gives a second cause for the spin's flip, two paragraphs after the fixed matrix gave the first. "The momentum and the spin follow in the same way" says nothing definite.
- Suggestion: Keep the paragraph as a check, not a cause. Open with "Chapter 5's hole, a picture physicists have since dropped, gives the same signs." Cut "The momentum and the spin follow in the same way." Replace "That is why" with "This agrees with".

#### E4 Prose: restatement, passives, and one word for a change of sign

- Status: Done.
- Change: Done in G: the result is stated once after the figure; the passives are gone; "reversed" is the one word for a quantity and "change the sign" for a term; "reshuffle" is kept.
- Finding: Section 1 says the result three times in a row (the paragraph "What changes", the caption, and the sentence after the figure). Four agentless passives, among them "No particle is ever seen with a negative energy" and "can be turned into". Four words for a change of sign: reversed, flipped, changes the sign, opposite. "Reshuffle" appears four times and in a label; the review reads it as an idiom and offers "reorder". "So" opens three sentences within a screen in section 1, and the page's first two sentences both open "Chapter 5". "Dirac's equation" once, where 6a says "the Dirac equation".
- Suggestion: Apply the review's rewrites, which change wording only: one statement of the result where there are three; active sentences; "flip" for a quantity and "change the sign" for a term. Keep "reshuffle", which is a plain word for what the matrix does, unless Hanh prefers "reorder".

#### E5 The boxes: what the fixed matrix is, and three loose wordings

- Status: Done.
- Change: Done in G: the box opens with $\\psi_c = (\\psi_4^*, -\\psi_3^*, -\\psi_2^*, \\psi_1^*)$ and the at-rest case; its table has a row for the momentum along y; it says $\\alpha_y$ is built from $\\hat Y$; the moving-electron box checks the first row; the spin box is reworded in three places. Claude checked numerically that this $\\psi_c$ turns a negative-energy solution of momentum p into a positive-energy solution of momentum minus p.
- Finding: Section 1's box never writes down what the fixed matrix does to the column, so its two bullets are asserted. Its table follows "the three terms" but leaves out the slope along y, one of the two terms the matrix repairs. It says "One of the matrices, Y-hat"; the equation's matrix is alpha-y, which is built from Y-hat. Section 2's first box uses only the third row of the equation. The box on the spin says the spin "doesn't commute, so" a definite spin is impossible, which doesn't follow from that alone, calls 6a's commutator "its leftover", and says spin along the motion is "the one case" where spin is kept, forgetting the electron at rest.
- Suggestion: In section 1's box, show the result once, $\psi_c = (\psi_4^*, -\psi_3^*, -\psi_2^*, \psi_1^*)$, and apply it to the third entry at rest, which also shows the spin's flip. Add the row for the slope along y to the table. Say "alpha-y, which is built from Y-hat". In section 2's first box, add one line saying the first row agrees. In the spin box, say "and here no state of definite energy has a definite vertical spin", "the commutator", and "for a moving electron".

#### E6 Things the reader still asks at the end of section 1

- Status: Done.
- Change: Done in G: the opening of section 1 says the steps can be undone; "What this doesn't do" says it doesn't stop chapter 5's fall either; the page's opening mentions section 2.
- Finding: Two questions stay open for the bro-what reader. Why does a solution that can be converted into a positron's solution count as describing a positron? And does this stop the electron falling forever, which was chapter 5's problem with negative energies? The opening also never mentions section 2.
- Suggestion: One clause in section 1's opening: the two steps can be undone, so the new solution holds the same information as the old. One clause in "What this doesn't do": it doesn't stop chapter 5's fall either, which also waits for the field. One sentence at the end of the opening: the second section says what changes when the electron moves.

#### E7 The figure

- Status: Done.
- Change: Done in G: the momentum arrow is shorter, the spin arrow sits in a circle, and the sentence at the foot is gone.
- Finding: The momentum arrow and the spin arrow are stacked and nearly touch, so they read as one arrow. The sentence printed at the foot of the figure repeats the caption. The figure shows before and after but not which step reverses what.
- Suggestion: Put the momentum arrow beside the spin arrow, not above it, and drop the sentence at the foot. Leave out which step does what; the text says it.

## F. Two understandability reviews (2026-11-27)

Hanh: "do a review that focuses on understandibility. essentially, the page should not make the reader go: 'bro what?'". Two fresh agents read the page as it stood for E, each as a different reader, sentence by sentence, with no outside physics allowed. Each played back what it believed each section said and wrote a plain replacement for every place it was stuck. Nothing has been changed in response.

| Reader | Rating | Lost | Stuck | Blinks |
| --- | --- | --- | --- | --- |
| Attentive: has just read chapters 1 to 6a with care; opens a box when curious | 7 main text, 7 boxes | 0 | 4 | 6 |
| Hurried: read the earlier chapters over some weeks, remembers stories but not symbols, never opens a box | 6.5 | 0 | 6 | 7 |

**What landed for both.** A positron is a particle with the electron's mass and a positive charge and energy, and it is what a negative-energy solution describes. The conjugate is taken because it turns $-E$ into $+E$ without changing any chance. The table at the top, the speed table, "A hole is a missing electron" and "What this doesn't do" were named as the clearest places.

**What both readers were stuck on.** These four are the page's real problems, since two different readers hit each one.

| # | Where | The reader's words |
| --- | --- | --- |
| 1 | Section 1, step two | "What terms? Wrong against what?" and "I just saw the conjugate become a proper +E wave, so why isn't it a solution?" The hurried reader on the fixed matrix: "it fixes some signs the conjugate got wrong; I can't say which or why." |
| 2 | Section 2, the share in the lower pair | "43% chance of what? The lower pair was the positron a minute ago." The hurried reader calls this the worst place on the page and says section 2 seems to undo section 1. |
| 3 | Section 1, the charge | "There was no field in anything so far; why are we adding one now?" and "is minus q the same as plus e?" |
| 4 | Section 1, the hole | "Same way as what? I thought we dropped the sea. Does the hole flip the spin a second time?" (stuck for the attentive reader; the hurried reader found the last sentence of the paragraph one of the clearest on the page) |

**Raised by one reader.** The conjugate equation jumps from $+Et$ to $-Et$ with no middle step (hurried, stuck). Section 2's opening leans on $\alpha$ and $\hat H$, which the hurried reader has forgotten; the attentive reader named the same passage as the clearest on the page. "Can't have a definite spin along the vertical" is asserted and dropped (hurried, stuck). The table at the top lists $-mc^2$ beside "a positron", so does a positron have negative energy (hurried, blink; no earlier review saw this). "Call the result $\psi_c$": c for what (attentive, blink). "It takes two steps" against "One operation does both" (both, blink).

**The most useful replacement.** For step two, the attentive reader proposes a reason the reader can see, using the particle at rest: after conjugating, the wave turns in time like a wave of energy $+mc^2$, but its filled entry still sits in the lower pair, where the equation gives $-mc^2$. The wave and its place in the column disagree, so the entries have to move, and what was in $\psi_3$ ends up in the place of $\psi_2$. Claude checked this against the equation at rest; it is correct, and it also shows the spin's flip in the table at the top.

#### F1 One pass over both sections, using the two readers' replacements

- Status: Done.
- Change: Done in G.
- Finding: Both readers follow the story and neither follows the mechanism. The four places both were stuck on are step two, the share in the lower pair, the charge, and the hole. Each reader wrote a plain replacement for every stuck place, keeping the page's facts and symbols. The open items E1 to E6 point at the same passages.
- Suggestion: Rewrite sections 1 and 2 in one pass. Step two gets the at-rest reason. The charge paragraph first says a free particle's equation has no charge in it, and that the electron's charge is $q = -e$. The hole becomes a comparison with chapter 5, not a second cause. Section 2 says, straight after its first sentence, that a moving electron is still one electron of positive energy and that the sign of the energy, not the pair, says which particle. The conjugate equation shows its middle step. Section 2 reminds the reader in place what $\alpha$ does. The table at the top gets a column heading that says the energy is that of the entry, not of the positron. This pass absorbs E1 to E6; E7, the figure, is separate. About ten sentences are added and about as many cut.

## G. One pass for understandability (2026-11-27)

Hanh, on F1: "yes". Both sections rewritten in one pass with the two readers' replacements, absorbing E1 to E7.

Main text: about 1,290 words before, about 1,650 after. Boxes: about 600 before, about 750 after. Claude had said about ten sentences would be added and as many cut; more were added than cut.

| ID | Section | What changed | Status |
| --- | --- | --- | --- |
| G1 | Opening | Says this chapter takes the first step toward the full answer and mentions section 2. The table's headings say "Energy of its solution" and "Spin of the entry", and the sentence after it says the positron itself has a positive energy. | Done |
| G2 | 1 | Step one says what we want before conjugating, and the conjugate equation shows its middle step. Step two gives the reason at rest: after conjugating, the wave has the energy $+mc^2$ but its entry still sits in the lower pair, where the equation gives $-mc^2$; the matrix moves $\psi_3$ to the place of $\psi_2$. $\psi_c$ is said to have c for conjugate. | Done |
| G3 | 1 | "The charge" first says a free particle's equation has no charge in it, then follows the term with $q$, then says the electron's charge is $q = -e$. The hole has its own label and is a comparison. "What this doesn't do" mentions chapter 5's fall. | Done |
| G4 | 2 | Opens with what a moving electron still is. "The lower pair fills in" reminds the reader what $\alpha$ does, in place. "How much" says what $\gamma$ is and gives the formula for the share before the table. A sentence after the table says what the share is not. "Spin in motion" gives the reason in a clause. | Done |
| G5 | boxes | See E5. | Done |
| G6 | figure | See E7. | Done |
| G7 | all | The same two readers ran again on the same brief. See H. | Done |

## H. The two readers again, after the pass (2026-11-27)

The same two briefs as F, two fresh agents. Nothing has been changed in response.

| Reader | Before (F) | After (H) | Lost | Stuck | Blinks |
| --- | --- | --- | --- | --- | --- |
| Attentive | 7 main text, 7 boxes | 8 main text, 7 boxes | 0 | 4 | 5 |
| Hurried | 6.5 | 7 | 0 | 4 | 5 |

**What the pass fixed.** Step two now lands for both: the hurried reader says the fixed matrix is for "moving the filled entry to the upper pair, where the equation gives +mc²", and both name "The wave and its place in the column disagree" among the clearest lines. Asked whether a fast electron is partly a positron, the hurried reader answers "No, the page says so flatly". The attentive reader says section 2 needs nothing.

**What both are still stuck on.** Three places, each hit by both readers.

| # | Where | The reader's words |
| --- | --- | --- |
| 1 | Step two, the swap of spin up and down | "The pair swap had a reason. This one has none." The whole reversal of the spin rests on it. |
| 2 | The charge | "What momentum beside it?" The hurried reader calls "reversed against the momentum beside it" the least sayable phrase on the page. Chapter 6a's main text never shows the term. |
| 3 | "It doesn't stop chapter 5's endless fall either" | "You just turned the negative energies into positive-energy positrons. What is left to fall into?" Claude added this clause in G without the reason. |

**Stuck for one reader.** "What was in ψ₃ ends up in the place of ψ₂": the table says ψ₂ is an electron with spin down, so is it an electron now (hurried; the sentence is new in G). The share: the page says what it is not, and the reader can't say what it is (hurried; the attentive reader named the same passage among the clearest). "The equation allows another reading": am I allowed to change a solution and say it describes the same thing (attentive).

**Over-explained, both readers.** The three bullets under "What chapter 6a found" say what the table directly below them says. "That settles the table at the top..." restates the sentence under the table. The hurried reader would also move "Spin in motion" and the formulas from chapter 4 out of the main text.

**Pattern worth saying.** Two of this round's stuck places are sentences added in G to answer the round before. Each pass that adds reasons also adds a few new places to trip. The remaining items are small, and three of the four suggested fixes are a clause each.

#### H1 Three places both readers are still stuck on

- Status: Done.
- Change: The three rewrites went into the positron section as it moved to Fields and Quanta (I).
- Finding: The swap of spin up and down has no reason in the main text. The charge sentence leans on "the momentum beside it", which the reader has never been shown. "It doesn't stop chapter 5's endless fall either" seems to contradict what the section just did.
- Suggestion: Three small rewrites, each from the readers' own replacements and each checked against the physics. (1) "Swapping the pairs fixes the particle at rest. For a particle moving in some directions, one more term comes out of the conjugate with the wrong sign, and swapping spin up with spin down inside each pair fixes that one (box). This second swap is why the positron's spin comes out opposite." (2) "The field adds one piece to the equation, with q in it. Do the two steps to the whole equation (box). Everything comes back as it started except that piece, whose sign has changed." (3) "We have renamed the negative-energy solutions, but the electron's equation still has them, and nothing here stops an electron from dropping into one."

#### H2 Two smaller stuck places, one reader each

- Status: Done.
- Change: The sentence on the place of psi-2 went in with the move (I). The sentence on the share is moot: the moving electron is parked on the reference page unchanged.
- Finding: After "What was in ψ₃ ends up in the place of ψ₂", the hurried reader asks whether it is now an electron with spin down, as the table says of ψ₂. After "The share is not a chance of finding a positron", the same reader can't say what the share is.
- Suggestion: One sentence each. "That doesn't make it an electron with spin down, because the new column obeys a different equation, as the next paragraph shows." And: "The share only describes the column: how much of its squared length sits in the lower two entries."

#### H3 Two passages both readers call repeated

- Status: Done.
- Change: Moot: the page is dissolved (I). The bullets are gone, and the restatement is one sentence in the moved section.
- Finding: The three bullets under "What chapter 6a found" and the table straight after them say the same thing. "That settles the table at the top. The entry ψ₃ is spin up with the energy −mc², and the positron it describes is spin down with the energy +mc²." restates the sentence under the table.
- Suggestion: Cut the three bullets and keep the table, with one lead-in sentence that says the column has an upper and a lower pair and that the spin is ħ/2 in size. Cut "That settles the table at the top" down to one sentence. Leave "Spin in motion" and the formulas from chapter 4 where they are; only one reader raised them, and Hanh has already been through that part of the old page.

#### H4 Section 1's box skips the step it exists for

- Status: Kept.
- Change: Not done. The box moved with the positron section to Fields and Quanta and still leaves the product out. It is a debt for that chapter's rewrite (I5).
- Finding: The box says the matrix leaves two of the three momentum matrices as they were and changes the sign of the third, then "Multiplying the matrices out confirms it, and we leave that out." The attentive reader: "I opened the box for exactly this." The first bro-what test and the prose review said the same of the earlier version.
- Suggestion: Show the four-by-four matrix once and work one product, for the matrix that changes sign. About six lines of algebra in the box, none in the main text. Then have that algebra checked.

## I. Chapter 6b dissolved (2026-11-28)

Hanh, on the reviews of H: "yeah, i agree with the reviewers. this section lacks meaning. we know the E < 0, and we want to fix it. but it doesn't say what would a satisfactory solution be. we find something called the positron, but why is this OK and not E<0 ?"

Claude's answer: within this chapter it isn't a fix. A way out of negative energies has to stop the fall, account for the positrons and pairs that are seen, and keep the equation. The conjugation only shows what kind of particle the negative-energy solutions are about. It leaves the fall and the pairs to the fields. So the section can't supply its own meaning, and by Hanh's rule from C it belongs where the fix is made. Hanh: "move the positron to fields and dissolve 6b".

| ID | What changed | Status |
| --- | --- | --- |
| I1 | The page `docs/dirac-solutions.md` is removed. It is gone from the sidebar, the menu, the home page grid and the PDF list. | Done |
| I2 | The positron section is now the first section of `docs/qft.md`, "From a negative energy to a positron", with its box and its figure. It opens with the three things a way out has to do and says the section does only the first part. It carries the table of the four entries, and the H1 and H2 rewrites. The rest of that chapter is still in the old style and has not been touched. | Done |
| I3 | "A moving electron", with its two boxes, is parked as section 4 of `docs/dirac-reference.md`, unchanged apart from its first sentences. Claude chose this over adding it to 6a, which is final and has a published video. Hanh then overruled this: "move it to 6a, rename 6a to 6". It is section 7 of the chapter (`06-dirac-equation.md`, S1). | Done |
| I4 | 6a's opening, its "Where this comes back" and its Next link now name Fields and Quanta as the next chapter. Links in Fields and Quanta, Field Quantization and the reference page follow. Every link into the three pages checked against the built site. | Done |
| I5 | Debts for the rewrite of Fields and Quanta: the positron section's box still leaves out the matrix product (H4); the section is in the new voice inside an old-voice chapter; its promise that "the rest of the chapter needs fields for both" has to be made good there. | Noted |
| I6 | The 6a video is published as "Chapter 6a", and its description on YouTube links to `dirac-solutions.html` as the next chapter. That link will stop working when this is pushed. The local description file now points to Fields and Quanta; the YouTube description is not changed. Whether the chapter stays "6a" with no 6b is also open. | Waiting for Hanh |
| I7 | This file is now a record only. Further work on the positron section is tracked with Fields and Quanta. | Noted |

---

## Index by section

| Iteration | Items |
| --- | --- |
| Iteration I | the page dissolved: I1 to I7 |
| Iteration H | Opening: H3 · 1: H1 to H4 · 2: H2 |
| Iteration G | Opening: G1 · 1: G2, G3 · 2: G4 · boxes: G5 · figure: G6 |
| Iteration F | 1 and 2: F1 |
| Iteration E | Opening: E1, E6 · 1: E1 to E7 · 2: E2, E5 |
| Iteration D | whole page: D1 to D7 |
| Iteration C | whole page: C1 to C8 |
| Iteration B | Opening and all sections: B1 · 1: B5, B7 · 2: B2, B5, B7 · 3: B3, B5 · 4: B4, B6 |
| Iteration A | Opening: A1 · 1: A2, A6 · 2: A3 · 3: A4, A7, A8 · 4: A9 · all: A5, A10 |
