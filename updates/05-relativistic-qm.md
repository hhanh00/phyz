# Chapter 5 updates: Relativistic Quantum Mechanics

This file tracks the work on chapter 5: the page `docs/relativistic-qm.md` and the script `video/scripts/05-relativistic-qm.txt`.

Each round of work is an iteration with a letter (A, B, C and so on). Each item in it has a number, so an item is referred to as, for example, C8 or F4. Add a new iteration at the end for each new round, and never renumber old items. The index at the bottom lists the items by section.

Status words: **Done** (applied), **Open** (waiting for a decision or for work), **Kept** (decided to leave as is), **Noted** (for the record, no action).

## What is left to resolve

This section always lists every open item, one per row. When an item is settled, its row leaves this section and its status changes in the iteration table below.

### The page: final

Hanh, 2026-11-26: "page is final". No decision is open on the page.

### The page: waiting for work

| ID | Where | What has to happen | Waiting on |
| --- | --- | --- | --- |

### The script (resumed)

Hanh, 2026-11-26: "commit and push, then resume the script". Claude rewrote the script in one pass from the final page (iteration N). The earlier open items F4 to F10 are settled by that rewrite and listed under N.

The closing review (N10) returned no must-fix: fidelity 9.5/10, overall 9/10, "ready to record". Every date and number matches the page, the format is clean, and the two-waves passage is faithful to the page's box.

It made five optional suggestions (N11 to N15). Hanh, 2026-11-26: "leave N11-N15". The script is unchanged since the closing review.

### The deck: done

Hanh, 2026-11-26: "take your recommendations for P". P1 to P9, P11 and P14 are applied; P10, P12, P13 and P15 are left as they are. The anchor check passes with 0 problems, the eleven changed slides are re-rendered, and Claude looked at each one. No decision is open on the deck.

### The video: built, waiting for Hanh to watch

Hanh, 2026-11-26: "commit and push, then do the video". The video is built: `video/out/05-relativistic-qm/05-relativistic-qm-video.mp4`, 23 minutes 56 seconds, 1920 by 1080, with audio and a subtitle track. See iteration Q.

| ID | Where | The question | Claude's recommendation |
| --- | --- | --- | --- |
| Q6 | Whole video | Hanh to watch it. Claude checked nine frames against the narration's timings, not the whole video. | Watch at least "Second problem" (8:13) and "The Dirac equation" (12:41). |
| P12 | Slides 46 to 48, at 8:50 to 9:10 | In the frames Claude checked, the two arrows and their sum are small inside their circles. Enlarge them? | Hanh's call after watching. A change means re-rendering three slides and rebuilding the video, about five minutes. |

### Waiting for work

| ID | Where | What has to happen | Waiting on |
| --- | --- | --- | --- |
| Q10 | YouTube | Upload the video with its description, cover and playlist place. Hanh has to drop the file, as before. | Hanh asking for it. |

## Status

| Step | State |
| --- | --- |
| Page | Final (Hanh, 2026-11-26), committed as `841bb7c`, merged to `main` and live on the site. |
| Script | Resumed. Rewritten from the final page (about 3,380 words, format clean); the closing review returned no must-fix (9/10, ready to record). Hanh left its five optional suggestions as they are. Committed as `57b3c8f` on the branch, not pushed. Hanh chose not to read it before the deck. |
| Pause file | Written and checked. Not committed. |
| Deck | Built, 125 slides, anchor check clean. Fresh review 9/10, ready to render, no must-fix. Eleven of its optional points applied and checked. Committed as `963b3e5` and pushed; eight places were fixed afterwards during the video build (Q3) and committed with the build changes. |
| Cover | Rendered and checked. |
| Narration | Rendered with the Azure voice: 23.8 minutes. |
| Video | Built: 23:56, with subtitles. Description file written. Hanh has not watched it. |

---

# The page

## A. First draft and its two reviews (2026-11-26)

Claude rewrote the page in one pass, then ran one `/bro` gap pass (7/10 against chapter 4) and one correctness check, and applied both in one cleanup pass. Section numbers here are today's numbers.

| ID | Section | Item | Status |
| --- | --- | --- | --- |
| A1 | Whole page | Rewrote the old textbook version in the style of chapters 3 and 4, with $c$ and $\hbar$ explicit in the main text. | Done |
| A2 | Figures | Redrew `relativistic-energy-solutions.png`, added `dirac-sea-hole.png` and `positron-track.png`, removed `klein-gordon-density.png` and `dirac-linearization.png`. | Done |
| A3 | Other chapters | Repointed 28 links in six files to the new section names and numbers. | Done |
| A4 | §4 | Correctness: the draft said a molecule in chapter 3 dropped a rung by giving off light. Chapter 3 doesn't show that. Now: the bond's energy changed a whole rung at a time. | Done |
| A5 | §7 | Correctness: the draft treated the two-entry column as the spin. On a line the two entries are the two energy signs. The text now says it borrows the spin matrices' arithmetic only. | Done |
| A6 | §11 | Correctness: small components are smaller by about half the speed over $c$, not the full speed. | Done |
| A7 | §3 | Cut the anecdote about Schrödinger dropping the equation over hydrogen's energies; no earlier chapter gives atoms energy levels. | Done |
| A8 | §5 | "With that extra freedom the total no longer has to stay at one" became a plain statement. Cut the "hint for later" about charge. | Done |
| A9 | §6 | Said why $\alpha$ and $\beta$ keep their order before squaring. | Done |
| A10 | §9 | Gave the reason negative energies survive: at rest $E = \beta\,mc^2$, and $\beta$ gives both signs. | Done |
| A11 | §9 | "The only positive particle known" became "the lightest"; "every kind of particle" became "other particles". | Done |
| A12 | Whole page | Replaced about eight idioms ("set it aside", "by hand", "leans on" and similar). | Done |

## B. Restructure (2026-11-26)

Claude rated the structure 7.5/10 and named three weaknesses. Hanh: "do all three". Rating after: 8.5/10.

| ID | Section | Item | Status |
| --- | --- | --- | --- |
| B1 | §1 | New opening section: Anderson's photograph as a puzzle. The trail figure and Anderson's numbers moved here, and §9 returns to it. | Done |
| B2 | §6, §7 | Split the Dirac section: §6 ends on the three conditions, §7 finds the matrices and writes the equation. | Done |
| B3 | §11 | New closing section for the notation later chapters use (three dimensions, four-by-four matrices, small components, gamma form). | Done |
| B4 | Other chapters | Repointed the 28 links again; eight links from `dirac-equation.md` now go to §11. | Done |
| B5 | §8 | Claude's suggestion: a sentence saying one problem is solved and one remains. Hanh approved the page without it. | Kept |
| B6 | §2–§8 | Claude's note: nothing reminds the reader that §1's trail is still unexplained. Hanh approved the page without it. | Kept |

## C. Hanh's read (2026-11-26)

| ID | Section | Item | Status |
| --- | --- | --- | --- |
| C1 | §2 | Hanh: shorten the recap. Main text cut from about 330 to 235 words; the table carries the recipe. | Done |
| C2 | §4 | Hanh: "having the values does not add anything". Removed 0.511 MeV and the electron-volt definition; the unit is now defined in §1's box. | Done |
| C3 | §4 | Hanh asked what "any force mixes them into its wave... on trust" meant. Replaced with "Could we just declare the negative energies off limits?" | Done |
| C4 | §5 | The table restates the prose above it. Hanh: keep both, "the table helps having pros/cons side by side". | Kept |
| C5 | §6 | Hanh: "set out to get the chance back" is a weird sentence, and "per metre" isn't needed. Now: "went looking for a relativistic equation with a chance that is never negative". | Done |
| C6 | §7 | Hanh: after numbers, a reader thinks of matrices, and the text leaned on them already. First half rewritten around matrices; "list" became "column" in §7–§9. | Done |
| C7 | §7 | Hanh: the step from a line to space was unclear (which matrix goes with what, why not reuse a pair, why not three-by-three). Now four labelled steps and a new box. | Done |
| C8 | §7 | Hanh: put the check of the two matrices in a box. | Done |
| C9 | §7, §11 | Hanh: "spinor" comes out of nowhere. Moved to §8 with its reason, then to §11's opening when C12 removed the spin. | Done |
| C10 | §8 | Hanh: why $\rho$ and not $\lvert\psi\rvert^2$? Now $\lvert\psi\rvert^2$, with a sentence on the squared length of a column. | Done |
| C11 | §8 | Hanh didn't recall chapter 2a calling anything a "spin state". It doesn't. Sentence corrected, then removed by C12. | Done |
| C12 | §8 | Hanh: "remove the spin. i don't think it fits here." Spin result and magnet strength removed; section retitled "A chance that is never negative"; intro and a link in `dirac-equation.md` adjusted. | Done |
| C13 | §9 | Hanh: "On one line β is the matrix..." is a weird sentence. Reworded. | Done |
| C14 | §9 | Hanh: "i thought there were 4 wave fns", then "you assume that the reader can keep the 4 eqs in his head". The passage now says it goes back to the line case, shows $\hat Z$ acting on the column of two, then mentions the four. | Done |
| C15 | §9 | Hanh: is it important now that the two in each pair are the spin? Cut; a back-reference in `dirac-equation.md` removed. | Done |
| C16 | §9, §10 | Hanh: keep the sea but present it as Dirac's first answer, "it feels like an accounting trick". New lead-in, a paragraph calling it a trick and a way of counting, and a new opening for §10. | Done |
| C17 | §9 | Hanh: "section 9 is good for me now". | Noted |
| C18 | Whole page | Hanh: "rest is good". Claude took this as final approval and started the script. Hanh later said the page is not finalized. | Noted |

## D. Closing correctness check (2026-11-26)

A fresh agent re-derived every equation after Hanh's read. It found no errors.

| ID | Section | Item | Status |
| --- | --- | --- | --- |
| D1 | Whole page | Every displayed equation and box re-derives correctly, including §7's new box. Cross-references to chapters 1–4 and between sections match. Figures agree with the text. | Noted |
| D2 | §5 | A "(box)" pointer claimed the box shows the total of $\lvert\psi\rvert^2$ drifting. It doesn't. Pointer removed. | Done |
| D3 | §1, figure | "Loses speed in the lead": at 63 and 23 MeV the particle is within a hair of light speed on both sides and loses energy. "Loses energy, and a particle with less energy bends more" would be exact; the figure labels would change too. Hanh, 2026-11-26: go with Claude's recommendation. Changed in the page, the figure and the script. | Done |
| D4 | §9 | "One for each sign of the energy" holds for a particle at rest. The paragraph opens with "Take a particle at rest". Hanh, 2026-11-26: go with Claude's recommendation, which was to leave it. | Kept |
| D5 | §1 | Anderson's numbers (6 mm, 1.5 T, 63 and 23 MeV, trail over 5 cm, proton about 5 mm): the checker is confident, and a rough calculation agrees. | Noted |
| D6 | §9 | "He hadn't been looking for it" matches the checker's recollection of Anderson's accounts, but is not confirmed against a source. Hanh, 2026-11-26: go with Claude's recommendation, which was to keep the sentence. | Kept |
| D7 | §7 | Pauli's matrices in 1927 and Dirac building on them: the checker is confident. | Noted |
| D8 | §9 | Dirac first proposed that the holes were protons. The page skips that. | Noted |

## H. Rating review (2026-11-26)

A fresh agent read chapters 1 to 4, then chapter 5 cold. Overall 8/10 against chapters 3 and 4. It found no wrong physics, dates or numbers. Its verdict: nearly ready to publish; the shortest list is H1 to H6 and H9.

Section scores: intro 9, §1 9, §2 8, §3 9, §4 9, §5 7, §6 9, §7 6.5, §8 7, §9 9, §10 8, §11 8.

| ID | Section | Item | Status |
| --- | --- | --- | --- |
| H1 | §7 | Three-by-three paragraph is heavy and unexplained; proposes a pointer, a table of matrix sizes, and a line in the box. Hanh, 2026-11-26: "you can shorten the explanations in the main text and refer to the box". Both "Why..." paragraphs are now one or two sentences that point to the box. The box now states $\beta^2 = 1$ and says why the eigenvalues are $\pm1$. No table. | Done |
| H2 | §5 | "It turns out" step has no reason; proposes the two-waves picture in place of the Newton comparison. Hanh, 2026-11-26: "just leave the neg energy arg that we can explain. it's enough". The claim that the total of $\lvert\psi\rvert^2$ drifts is gone, with the Newton comparison and two table rows. §5 now makes one argument: the quantity the equation keeps contains a rate of change in time, so it carries the energy's sign and is negative for negative-energy waves. | Done |
| H3 | §5 | $\rho$ arrives unannounced; proposes one introducing clause. Done as part of H2: the text now says the kept quantity contains a rate of change in time (box) before giving its value. | Done |
| H4 | §7 | The Dirac equation is never said to pass chapter 4's test. Hanh, 2026-11-26: "take it". The sentence after the one-line equation now says it treats time and space alike, as chapter 4 asks, and that each entry of the column also obeys the Klein–Gordon equation. | Done |
| H5 | §8 | Thin; doesn't close §6's loop; one agentless passive. Hanh, 2026-11-26: "take it", and questioned "so it keeps the total at one". That "so" claimed more than the page shows. The paragraph now mirrors §5 after H2: the equation has the single rate of change §6 asked for, so no rate of change, and no energy sign, gets into the quantity it keeps. | Done |
| H6 | §8 box | $\gamma$ used before §11 defines it. Hanh, 2026-11-26: "take it". The sentence on $j^\mu$ and the Dirac adjoint moved to the end of §11's box, after the gamma matrices are defined. | Done |
| H7 | §2, §7 | Two claims about chapter 2b point at its boxes. Hanh, 2026-11-26: "take it". §2 now says "A box in chapter 2b built...". §7 says chapter 2b met the two as operators, shows them "written as matrices, as in that chapter's box", and ties the opposite results to 2b applying both orders to up. | Done |
| H8 | §4, §9 | Few numbers in the main text after §1. Hanh, 2026-11-26: agreed with Claude's recommendation to leave it (C2). | Kept |
| H9 | Figure 1 | Title names the positron before the text does. Retitled "Anderson's trail, 1932" and re-rendered. | Done |
| H10 | §11 box | Repeats §7. The box now points back to §7 for the rule in space and its conditions, and names §7's three matrices as the Pauli matrices. The forward link to the next chapter is gone. | Done |
| H11 | Several | Six idioms. Four replaced: "off limits" (forbidden), "So far so good" (That all works), "ended stuck" (ended with a problem), "reads like a trick" (looks like). The other two went away with H1 and H2. | Done |
| H12 | Figures 2, 3 | Squiggle over the dots; hyphen for a minus sign. The squiggle now ends in the gap, and the label helper draws a real minus sign. Both figures re-rendered. | Done |

## I. Bro-what test (2026-11-26)

A fresh agent wrote the `/bro what?` reply for the intro and sections 1 to 10, then compared each with the text. 7.5/10 against chapter 4: sections 1, 3, 4, 6 and 9 match it; sections 5 and 7 are denser and lean on boxes. The replies themselves are in `updates/05-bro-replies.md`.

| ID | Section | Item | Status |
| --- | --- | --- | --- |
| I1 | §4 | Nothing earlier says systems drop by giving off light; "the same push from light" rests on something never introduced. Added "And anything that can lose energy by giving off light sooner or later does." Kept "the same push from light" (C3). | Done |
| I2 | §7, §9 | Energy equals a matrix, with no comment. Added: "The right side of the rule is now an operator, like chapter 2b's $\hat H$, and the allowed energies are its eigenvalues." | Done |
| I3 | §5 | Same as H2. | Done with H2 |
| I4 | §7 | "Chapter 2b met two of them": same as H7. | Done with H7 |
| I5 | §7 | Three-by-three argument assumes matrix facts: same as H1. | Done with H1 |
| I6 | §1 | Why a proton would be slow, and why it would stop. Now: a proton is so heavy that, to bend that tightly, it would have to be slow, and the gas stops a slow proton. | Done |
| I7 | §2 | "Chapter 2b built...": same as H7. Also "$p/\hbar$ per metre" against 2b's "$p/h$ turns per metre" (I7b). | Done with H7. I7b done: the phase now turns "$p/h$ turns per metre" and "$E/h$ turns per second". |
| I8 | §9, §10 | "Antiparticle" unnamed; the fields paragraph can't be re-explained. §9 now names the antiparticle; the §10 paragraph opens with "The coming chapters show that". | Done |
| I9 | §9 | Why two of each sign. Left as is; Hanh cut this pointer (C15). | Kept |
| I10 | §10 | "Chapter 4 already allowed it" overstates chapter 4. Now "Chapter 4 makes room for it". | Done |
| I11 | §5 | The Newton paragraph's purpose is unclear: with H2. | Done with H2 |
| I12 | Intro | The table's "squared / not squared" row can't be read before §6. Harmless as a preview. | Noted |
| I13 | §9 | "A way of counting" stands as a one-liner. Hanh, 2026-11-26: "agree that 'counting' isn't great here". The sentence is cut; the paragraph keeps "looks like a trick", "nobody has seen the sea" and "what matters is what follows from it". | Done |

## J. Closing correctness check on the final text (2026-11-26)

Hanh: "run J1". A fresh agent re-derived every equation and box, tested the reasoning sentences added during H and I, and checked every reference to an earlier chapter, section or box. One error, three borderline points. Cross-references, goal lines, the opening table, history and numbers all passed, and nothing left over refers to removed text.

Hanh, 2026-11-26: "take your recommendations for J".

| ID | Section | Item | Status |
| --- | --- | --- | --- |
| J1 | Whole page | Run the check. | Done |
| J2 | Whole page | Hanh to say whether the page is final. Hanh, 2026-11-26: "page is final". | Done |
| J3 | §7 box | Error: "the second relation" now points at the wrong one of three. Now "Multiply the last relation by $\alpha$ on the left. Since $\alpha^2 = 1$, the left side is just $\beta$". | Done |
| J4 | Figure 3 | The arrow seems to start from a filled dot, not from the hole. The hole is now in the top row of the sea, with the arrow starting at it. Re-rendered. | Done |
| J5 | §8 | "Chance per metre" with four wave functions, which belong to space. Now "the chance of finding the particle near a point". | Done |
| J6 | §5 | The "(box)" pointer covers the fact, not the causal link. Left as is; it is the level of reasoning Hanh chose in H2. | Kept |

## K. Second rating review (2026-11-26)

Hanh, 2026-11-26: K1 "no", K2 "take", then "take remaining K".

A fresh agent, cold, barred from `updates/`. Overall 8.5/10 against chapters 3 and 4 (first round: 8). It checked the physics, dates, Anderson's numbers and the box algebra and found no errors. Verdict: ready to publish; it would make K1 and K2 first.

Section scores: intro 8, §1 8.5, §2 9, §3 9, §4 9, §5 8.5, §6 9, §7 7.5, §8 9, §9 9, §10 8, §11 8.5. (First round: 9, 9, 8, 9, 9, 7, 9, 6.5, 7, 9, 8, 8.)

| ID | Section | Item | Status |
| --- | --- | --- | --- |
| K1 | §6, §7 | "Straight-line rule" collides with "on a line". Proposed "first-power rule". Hanh, 2026-11-26: "no. first-power rule is less clear". | Kept |
| K2 | §10 | "Both problems" contradicts §8; the sign of the charge. Hanh, 2026-11-26: "take". Now "the negative energies stop being a problem", and the charge has "one sign for particles and the opposite sign for antiparticles". | Done |
| K3 | §1 | "Light, like an electron" is an unsupported jump. Now "So the particle was positive, but far too light to be a proton." The puzzle line and the section's closing line say "a light, positive particle" and "far lighter than a proton". | Done |
| K4 | §7 | Two jobs in one section. The part on space now sits under an unnumbered sub-heading, "Four matrices in space", so §8 to §11 keep their numbers and links. | Done |
| K5 | Several | Five idioms. Replaced: "step by step", "Where the trouble came from", "Chapter 4 allows it", "has only three", "looks at the equation piece by piece". | Done |
| K6 | Intro | One awkward sentence. Now "The other problem stayed, and it turned out to predict a kind of matter nobody had seen." | Done |
| K7 | §4 | "Clearly". Now "That doesn't happen." | Done |
| K8 | §9 | "At rest" (same as D4). Now "So for a particle at rest, that's what the column's two entries are". This reverses the earlier decision to leave it (D4). | Done |

## L. Second bro-what test (2026-11-26)

Hanh, 2026-11-26: L1 "take it but then add a box", then "take your recommendations for remaining L".

A fresh agent, barred from `updates/`. 8/10 against chapter 4 (first round: 7.5). No section needed outside knowledge to re-explain except where listed. No claim about an earlier chapter is false.

| ID | Section | Item | Status |
| --- | --- | --- | --- |
| L1 | §5 | Why the squared length stops being the chance. Hanh, 2026-11-26: "take it but then add a box that explains why it is no longer kept". The main text now says the total of $\lvert\psi\rvert^2$ doesn't have to stay constant, with a pointer to a new box. The box adds a positive-energy and a negative-energy wave of the same momentum and shows the squared length is $4\cos^2(Et/\hbar)$, rising and falling everywhere at once. The table row "Total of $\lvert\psi\rvert^2$" is back, and the closing lines name both failures again. This reverses part of H2, now with the explanation H2 lacked. The new box has had no correctness check (M1). | Done |
| L2 | §10 | "The positron's discovery points at the real issue." Now "Dirac's hole points at the real issue." | Done |
| L3 | §10 | Sign of the charge: with K2. | Done with K2 |
| L4 | §4 | "The same push from light" points at nothing. Sentence cut; the paragraph ends on "a solution like any other". This reverses C3's wording, which Hanh had approved. | Done |
| L5 | §7 | No rule for a matrix acting on a column. Left as is; §7 links the Math Refresher's section on matrices. | Kept |
| L6 | §7 | Purpose of "each entry obeys the Klein–Gordon equation". Sentence cut; "so it treats time and space alike, as chapter 4 asks" stays. This removes half of what H4 added. | Done |
| L7 | §9 | What tells the two of each sign apart. Added "The next chapter says what tells the two of each sign apart." It doesn't name the spin (C15). This reverses the earlier decision on I9. | Done |
| L8 | §1 | "Light, like an electron": with K3. | Done with K3 |
| L9 | §7 | The operator sentence is used only in §9. Moved there, just before the matrix is applied to the column. | Done |
| L10 | §4 | "The forbidden gap" appears in the main text before the main text says the energies in between aren't allowed; only the caption does. Minor. | Noted |
| L11 | §2 | "Chapter 1's rule for a slow free particle" is loose: chapter 1 writes the rule with a potential and doesn't say "slow" or "free". Harmless. | Noted |

## M. Correctness check after K and L (2026-11-26)

Hanh: "run M1". A fresh agent, barred from `updates/`, checked §5's new box first, then the K and L edits, then the whole page again. No errors. All seven groups of checks passed: every equation and box step, every reference to an earlier chapter, section or box, the opening table, the closing lines, the dates and numbers, and the three figures.

| ID | Section | Item | Status |
| --- | --- | --- | --- |
| M1 | Whole page | Run the check. | Done |
| M2 | §5 box, §8, §9 | The new box blames two energies per momentum; Dirac has both too, yet keeps its total. Claude proposed one sentence in §9. Hanh, 2026-11-26: "do not take M recommendations". | Kept |
| M3 | §5 box | "A quarter of a turn" is ambiguous. Claude proposed "After each arrow has made a quarter of a turn". Hanh: not taken. | Kept |
| M4 | §5 box | The Euler link's target shows only one of the two formulas. Left as is. | Kept |
| M5 | Where this comes back | The link text "Fields and Quanta" differs from chapter 2b's "Quantum Field Theory" for the same page. The page's title is "Quantum Field Theory: Fields and Quanta", so both are right. | Noted |

---

# The script

**On hold since 2026-11-26.** Claude started this work before the page was final, and Hanh stopped it. Iterations E and F record what was done up to then.

The script leaves out the page's §11 and its boxes, and refers to formulas as "on screen" instead of reading them out. Copies of each version are in the session scratchpad.

## E. First draft and review round 1 (2026-11-26)

Round 1 (fresh agent): fidelity 9/10, overall 8.5/10, every number matching the page.

| ID | Spoken section | Item | Status |
| --- | --- | --- | --- |
| E1 | Whole script | First draft, about 3,180 words, format clean. | Done |
| E2 | The Dirac equation | Must-fix: earlier videos never said "matrix"; video 2b said "vertical operator" and "sideways operator". The script now uses those names first, then "tables of numbers". "Up-and-down matrix" became "vertical matrix". | Done |
| E3 | The Dirac equation | Must-fix: "as many of one as of the other" is heard as the number one. Now "as many plus ones as minus ones" (later reworded by F2). | Done |
| E4 | Dirac's idea | Must-fix: the third condition was read aloud symbol by symbol. Now "the two orders of multiplying alpha and beta have to cancel each other". | Done |
| E5 | Second problem | The kept quantity is described as the squared length times the energy over the rest energy, with the reason it is almost the squared length for a slow particle. | Done |
| E6 | Second problem | "And then the total..." became "And it turns out the total...". | Done |
| E7 | Second problem | "The state now fixes the state a moment later" became "if you know the state at one moment, you know it a moment later". | Done |
| E8 | Dirac's idea | "We keep them in the order they come" became "we don't swap their order, in case the order matters". | Done |
| E9 | The Dirac equation | Why one matrix can't be used twice now gives the page's reason (twice its square, which is two). | Done |
| E10 | The Dirac equation | "The two-by-two matrices run out" became "no two-by-two matrix anticommutes with all three". | Done |
| E11 | Antimatter | The script now says a packet of light lifts the electron out of the sea. | Done |
| E12 | One particle isn't enough | The sentence introducing the field was reworded (and again by F1). | Done |

## F. Closing review of the script (2026-11-26)

A fresh agent with no history: fidelity 9.5/10, overall 8.5/10, format clean, one must-fix. Claude applied F1 to F3; the rest are suggestions waiting for Hanh. The script is now about 3,250 words.

| ID | Spoken section | Item | Status |
| --- | --- | --- | --- |
| F1 | One particle isn't enough | Must-fix: "it's no longer one particle's wave function. It's a field" had no clear subject. Now: "The coming chapters change what the wave function is. It no longer belongs to one particle. It becomes a field." | Done |
| F2 | The Dirac equation | Three-by-three: reminds the listener what eigenvalues are, and says "it turns out" for the equal split. | Done |
| F3 | Dirac's idea | Why numbers fail: "the two orders give the same product. Adding them gives twice that product. That's zero only if alpha or beta is zero." | Done |
| F4 | An energy rule becomes an equation | Suggestion: "Its energy is the momentum squared, over twice the mass" borders on reading a formula. Could become "Its energy rule is the low-speed one, on screen." | Open |
| F5 | Dirac's idea | Suggestion: "The square has three terms" never says the result is on screen. Add "It's on screen." | Open |
| F6 | The Dirac equation | Suggestion: "column" is new; video 2b said "list". Add "A column is just our list of amplitudes, written top to bottom." | Open |
| F7 | Antimatter | Suggestion: "antiparticles" is used later without being named. After "we call them antimatter", add "Each partner is called an antiparticle." The page has the same gap. | Open |
| F8 | Antimatter | Suggestion: "a way of counting" invites "counting what?". Could become "Treat it as a working assumption, not as a picture of what's really there." This would move away from the page's wording (C16). | Open |
| F9 | A trail that bends the wrong way | Suggestion: "It had come out, the year before, of an attempt..." is hard to parse by ear. Could become two sentences. | Open |
| F10 | The Dirac equation | Preferences: tie the on-screen matrices to "multiplies" and "swaps"; say "Pauli's exclusion principle" the second time. | Open |
| F11 | Whole script | F1–F3 were applied after this review, so the script needs one more fresh review with no must-fix before recording. | Open |
| F12 | Whole script | `check.py 05` can't run until the deck exists, so slide anchors are unchecked. | Open |
| F13 | Whole script | Hanh has not read the script. | Open |

## N. Script rewritten from the final page (2026-11-26)

The page changed in every section after iterations E and F, so Claude rewrote the script in one pass instead of patching it. It follows the page's final wording section by section, and adds a spoken heading, "Four matrices in space", to match the page's sub-heading.

| ID | Spoken section | Item | Status |
| --- | --- | --- | --- |
| N1 | Whole script | Rewrite from the final page. About 3,380 words. Format clean: allowed characters, numbers in words, no sentence over 20 words, thirteen headings of at most 7 words. | Done |
| N2 | Whole script | Fresh review against the final page: fidelity 9.5/10, overall 9/10, one must-fix. | Done |
| N3 | A trail that bends the wrong way | Must-fix: "a year earlier" dates the attempt, not the answer. Now "It had come out the year before. It came from an attempt to make quantum mechanics agree with relativity." | Done |
| N4 | Second problem | The two-waves passage skips two reasons. It now says a sum of two solutions is a solution, that the arrows turn opposite ways because the energies have opposite signs, and that the same momentum makes it happen at every position at once. | Done |
| N5 | Opening | "Its chance can be negative" before the listener knows which chance. Now "the chance it gives for finding the particle can come out negative". | Done |
| N6 | Dirac's idea | The third term's two orders aren't mentioned before they "cancel". Added, without symbols: "That term holds alpha and beta multiplied in both orders." The reviewer's wording, which read the formula aloud, was not used (E4). | Done |
| N7 | The Dirac equation | "Just". Removed. | Done |
| N8 | Where this leads | "The next chapter is the Dirac equation." Now "The next chapter looks at the Dirac equation piece by piece. It shows what its four wave functions do." | Done |
| N9 | Antimatter | The operator sentence is compressed. Now four short sentences: a matrix acts on the state, so it's an operator; an operator's eigenvalues are what a measurement can give; so the allowed energies are the matrix's eigenvalues. | Done |
| N10 | Whole script | Closing fresh review after N3 to N9: no must-fix, fidelity 9.5/10, overall 9/10, ready to record. | Done |
| N11 | Second problem | Optional: introduce the arrows before "both arrows turn the same way". Hanh: leave it. | Kept |
| N12 | Dirac's idea | Optional: "alpha and beta each square to one". Hanh: leave it. | Kept |
| N13 | An energy rule becomes an equation | Optional, a preference: say the last chapter recalled the recipe. Hanh: leave it. | Kept |
| N14 | Second problem | Optional, a preference: "the particle's rest energy". Hanh: leave it. | Kept |
| N15 | Second problem | Optional: plainer wording for "puts a rate of change in time into the quantity it keeps". Hanh: leave it. | Kept |
| F4 | An energy rule becomes an equation | "The momentum squared, over twice the mass": left as is, as recommended. | Kept |
| F5 | Dirac's idea | "The square has three terms, and it's on screen." | Done |
| F6 | The Dirac equation | "A column is just our list of amplitudes, written top to bottom." | Done |
| F7 | Antimatter | "We call each partner an antiparticle." The page names it too (I8). | Done |
| F8 | Antimatter | The "way of counting" sentence is gone from the page (I13) and from the script. | Done |
| F9 | A trail that bends the wrong way | The hard sentence is now two: "A year earlier, someone had tried to make quantum mechanics agree with relativity. The answer came out of that attempt..." | Done |
| F10 | Antimatter | "Pauli's exclusion principle", without the first name the second time. The other half of F10 was not taken. | Done |
| F11 | Whole script | Superseded by N2. | Done |

## P. The deck (2026-11-26)

Hanh: "do the pause file and the deck". One agent built `video/slides/deck_05.py` from a full brief: 125 slides, about 2.9 sentences per slide, no slide over four sentences, every slide with two to four build steps. Colours: blue for positive energies, orange for negative energies and what comes from them (the sea, the hole, the trail, the positron), purple for alpha, beta and their matrices, teal for what works, red for what fails. Claude looked at all eleven contact sheets. A fresh review then gave 9/10 with no must-fix.

| ID | Slide | Item | Status |
| --- | --- | --- | --- |
| P1 | 100 | Two electrons per shell under the exclusion principle. | Done |
| P2 | 99 | The dot falls smoothly through the forbidden gap. | Done |
| P3 | 38 | The light wiggle points at the wrong line. | Done |
| P4 | 14 | The proton's range mark is a stray tick. | Done |
| P5 | 42 | The negative-energy wave carries the positive-energy formula. | Done |
| P6 | 81 | "Square it" labels the wrong arrow. | Done |
| P7 | 85 | The vertical matrix sits in a momentum place. | Done |
| P8 | 66 | Red crosses on both conditions. | Done |
| P9 | 120 | The particles dot isn't blue. | Done |
| P10 | 11 | The example trail bends like a negative charge. Left as is. | Kept |
| P11 | 103 | The light squiggle runs into the sea's dots. | Done |
| P12 | 46–48 | The sum arrow is hard to see when the arrows nearly cancel. Left as is; to be checked in the video. | Kept |
| P13 | 110–111 | A heavy red strike through the sea. Left as is. | Kept |
| P14 | 122 | The first recap bullet appears under the spoken heading. | Done |
| P15 | 116, 118 | Rung labels 0 to 4. Left as is. | Kept |
| P16 | Whole deck | After the fixes: `check.py 05` reports 125 anchors, 0 problems; the eleven changed slides re-rendered; Claude looked at all eleven. Two needed a second pass by the agent (slide 42's arrow, slide 81's label spacing) and are right now. | Done |

## Q. Cover, narration and video (2026-11-26)

| ID | Step | Item | Status |
| --- | --- | --- | --- |
| Q1 | Cover | Added chapter 5 to `COVERS` in `video/slides/cover.py`: the two energy curves with the gap between them. Rendered and checked; one axis line that crossed a label was removed. | Done |
| Q2 | Narration | Rendered with the Azure voice from the final script and the pause file: 23.8 minutes, 18,401 characters sent. | Done |
| Q3 | Slide video | The first build crashed on slide 9 and `make_video.sh` hid the error, so it looked like success. Cause: slides 9 and 117 faded in an object that is redrawn every frame, which fails when the object's shape changes. Six more places used the same pattern without failing (slides 8, 41, 48, 99 and 118). The preview renders only last frames, so neither the builder nor the review could see it. Claude changed all eight places to add the object directly. Anchor check still 0 problems. | Done |
| Q4 | Final video | Built: 1,435 seconds (23:56), h264 at 1920 by 1080, aac audio, subtitle track with 372 cues. | Done |
| Q5 | Description | `video/out/05-relativistic-qm/05-relativistic-qm-description.txt`, in chapter 4's format, with thirteen chapter timestamps from the heading timings plus the five-second cover hold. | Done |
| Q6 | Check | Claude pulled nine frames at the times of key sentences (the cover, the cloud chamber, the odd trail, the two-arrows passage twice, the two matrices, the Dirac equation, the sea, the rungs). Each shows the right slide for its sentence. Hanh has not watched the video. | Open |
| Q7 | Build script | `make_video.sh` hides a failed step. Hanh, 2026-11-26: "take your recommendations for Q". The script now sets `pipefail`, keeps the slide build's full log in the work folder, and on failure prints its last 25 lines and stops. | Done |
| Q8 | Workflow | The preview can't catch animation crashes. `build.py` has a new mode, `smoke`, which plays every slide once at low resolution without needing narration and lists the slides that crash. Run on the committed, unfixed deck it reports slides 9 and 117; on the fixed deck, 0 of 125. `BRIEF.md` has the rule against animating a redrawn object, and `WORKFLOW.md` has the smoke step before and after the deck review and a check that the video file exists. | Done |
| Q9 | Repository | Commit and push the deck fixes, cover entry, build changes and this file. Hanh, 2026-11-26: "commit and push". | Done |
| Q10 | YouTube | Upload. | Open |

---

# The rest of the pipeline

## G. Pause file, deck, video and commit

Nothing here has started. Each step is listed so it has an ID.

| ID | Step | Item | Status |
| --- | --- | --- | --- |
| G1 | Pause file | Write `video/prosody/05-relativistic-qm.pauses.txt`: the final script plus breath commas. Written on 2026-11-26 with 16 added commas, in the script's long sentences that had none. Checked: 357 sentences, differing from the script by commas only. Not committed. | Done |
| G2 | Deck | Build `video/slides/deck_05.py`, run `check.py 05` until clean, make contact sheets, run one fresh deck review. Done on 2026-11-26; see iteration P. | Done |
| G3 | Cover and video | Add the chapter to `COVERS` in `slides/cover.py`, render the narration, build the video, write the description file. Done on 2026-11-26; see iteration Q. | Done |
| G4 | Repository | Commit when Hanh asks. Committed as `841bb7c` on `classical-mechanics-rewrite` and pushed, 2026-11-26. The script draft was left out. `main` is not updated (G4b). | Done |
| G4b | Repository | Merge into `main` and publish. Hanh, 2026-11-26: "merge into main and push". `main` fast-forwarded to `841bb7c` and pushed; the deploy succeeded and the live page shows the new chapter. | Done |
| G5 | Page source | Remove the temporary review anchors from `docs/relativistic-qm.md`. Done on 2026-11-26, once every H and I item was settled (`python3 updates/refresh_links.py --strip`). | Done |
| G6 | Dev helper | `docs/.vuepress/lib/review-jump.js`, wired in `client.js` behind `__VUEPRESS_DEV__`: makes `?rev=ID` links scroll to a review anchor and badges every anchor. Added 2026-11-26 after Hanh reported the first deep links landing in different places. Hanh, 2026-11-26: "G6 keep". | Kept |

---

# Index by section

**Page**

| Section | Items |
| --- | --- |
| Whole page, figures, other chapters | A1, A2, A3, A12, B4, C18, D1 |
| §1 A puzzle | B1, D3, D5, H9, I6 |
| §2 From an energy rule to a wave equation | C1, H7, I7 |
| §3 The Klein–Gordon equation | A7 |
| §4 First problem | A4, C2, C3, H8, H11, I1 |
| §5 Second problem | A8, C4, D2, H2, H3, I3, I11 |
| §6 Dirac's idea | A9, B2, C5 |
| §7 The Dirac equation | A5, B2, C6, C7, C8, C9, D7, H1, H4, H7, I2, I4, I5 |
| §8 A chance that is never negative | B5, C10, C11, C12, H5, H6 |
| §9 The negative energies predict antimatter | A10, A11, C13, C14, C15, C16, C17, D4, D6, D8, H8, H12, I8, I9, I13 |
| §10 Why a one-particle equation isn't enough | C16, I8, I10 |
| §11 The notation later chapters use | A6, B3, C9, H10 |

**Script**

| Spoken section | Items |
| --- | --- |
| Whole script | E1, F11, F12, F13 |
| A trail that bends the wrong way | D3, F9 |
| An energy rule becomes an equation | F4 |
| Second problem, a negative chance | E5, E6, E7 |
| Dirac's idea | E4, E8, F3, F5 |
| The Dirac equation | E2, E3, E9, E10, F2, F6, F10 |
| The negative energies predict antimatter | E11, F7, F8 |
| One particle isn't enough | E12, F1 |
