# Writing listening scripts

These scripts turn the chapters in `docs/` into an audiobook read by a text-to-speech voice. The listener has only their ears, cannot look back at a formula, and may be walking or driving. The reference for voice, density, and technique is `audio/scripts/01-classical-mechanics.txt`. Read it in full, alongside `docs/classical-mechanics.md`, before writing anything.

## Replacing what can't be heard

Replace every equation and table with prose instead of dropping its content. Say what an equation does as a procedure or a relationship ("multiply each entry by the generator for its position, then add up the results"), and carry its logical role into the sentence that follows.

Narrate a table when it makes a point, as a short story of what changes and what stays the same. When a table or a run of numbers only confirms a result, state what it confirms in a sentence or two, keeping a number only if the listener can hold it in their head. Keep the worked examples that show something happening, such as a ball that would fall upward with the wrong sign, and tell them with small numbers.

Keep all the concepts, arguments, and reasons for each step, and keep the informal explanation of why cheating fails. Each protocol step should survive, though the listener needs the idea and its order rather than a term-by-term expansion.

Expect a script of roughly 75 to 80 percent of the chapter's non-math word count. Shorter is fine when a chapter's bulk is numeric, but don't remove arguments to reach a length.

## Naming things

Refer to objects by what they are. Use a role-based name ("the kinetic energy", "the momentum", "the bracket of position with momentum") rather than a symbol. A letter is acceptable only when a chapter juggles several similar objects and a letter genuinely helps, and then introduce it in a sentence first ("we'll call it L").

Keep the site's technical terms (Lagrangian, action, phase space, Poisson bracket, and so on) and define each at its first appearance in the same way the chapter does. Say an equation's content in words ("momentum changes at a rate set by the force") rather than reading its symbols aloud.

Replace visual and positional references. "Section 4", "the table below", "the figure above", and "as shown" become "the pendulum from earlier" or "the chapter on the harmonic oscillator". Drop links, and describe a diagram only if it carries an idea that the surrounding text doesn't.

Leave out derivations that the chapter puts in collapsible boxes. Keep what each one shows.

## Accuracy

Everything in a script must come from its chapter. Add no new claims or numbers, and copy any number exactly from the chapter text.

Keep the chapter's distinctions between what is measured, what is a model choice, and what is derived, and keep any statement that a result is given without proof.

## Writing style

Write the way a person explains something out loud to a friend who is following closely, not the way the site reads. The site's prose is careful and formal; a script that keeps that register sounds robotic and pedantic when spoken. So:

- Use contractions (it's, we'll, doesn't, that's) and talk to the listener with "you" and "we". "Let's" is welcome when we do something together, such as working an example.
- Prefer everyday words to formal ones: "says yes" over "holds", "fails the test" over "falls outside the relation", "comes to" over "evaluates to", "pin down" over "say precisely", "check" over "verify" when either fits. Keep the technical terms themselves.
- Give the idea first and its name second: "Only the prover knows the secret number, and we call that the witness", not "The secret part is called the witness."
- One idea per sentence. Break up sentences that stack clauses with "which", "such that" or "exactly when".
- Use the active voice, with someone doing the action: "we call this grinding", not "this is called grinding"; "the cheater fixes the errors", not "the errors are fixed"; "we reconstructed this from the code", not "this is reconstructed from the code".
- Don't open a sentence with a long gerund phrase as its subject ("Attaching to each header a proof that covers... means..."). Say it as steps: "Now give each header a proof. That proof covers..."
- Prefer plain, concrete words over abstract or mathematical ones: ranges that "connect", not ranges that "meet".
- Cut announcements about the text itself, such as "This chapter supplies that vocabulary" or "The following section shows". Just do the thing, or say plainly what comes next ("Next, let's see why the order matters").
- Pass the "bro test". Imagine a friend listening who would say "bro, what?" the moment a passage stops making sense. Before the details, say in plain words what question the passage answers. After them, say what the answer means. When the same math does two jobs in the chapter, say which job it is doing here. For example, the Schnorr subtraction shows that passing proves knowledge, and later it shows why reusing a mask leaks the secret.
- No unstated premises. Every "so", "otherwise" and "because" must rest on something the listener has already heard. Ask "why?" of each claim, and make sure the script answers it, in that sentence or earlier. For example, "otherwise the sender could watch for the nullifier" failed until the script said the sender made the note, so it knows everything in it.
- Don't overdo it. No filler ("basically", "super", "pretty much"), no jokes or exclamation marks, no rhetorical questions, and no hype. The tone is relaxed, not chatty.

Before and after, from chapter one:

> Before: The rule that selects the real path is the principle of stationary action. Bend the real path a little, by an amount epsilon, keeping its two endpoints fixed. The action changes, but only by an amount that grows like epsilon squared.
>
> After: Now the rule. Bend the real path a little, keeping its two ends fixed. The action changes, but only by an amount that grows like the square of the bend. Halve the bend, and the change drops to a quarter.

The prose rules in `CLAUDE.md` still apply. Give sentences real subjects and active verbs, motivate a step before asserting it, avoid "simply" and "of course", and use plain declarative headings. Connect ideas with "because", "so", and "which means". Avoid colon- and dash-heavy sentences, since neither sounds like anything when spoken.

Listening adds a few requirements. Keep sentences short, with one idea each. Aim for about ten words on average, and never go over twenty. When a sentence joins two ideas with "and", "which", "so" or "because", split it into two. A run of short sentences is fine when spoken, though an occasional longer one keeps the rhythm from sounding clipped. Signpost often, and say where the argument has got to before moving on. Restating an object's role when it returns after a gap is helpful here, because the listener can't scroll back, though the rule against repeating a whole point in different words still applies.

## File format

The text goes straight to the speech engine, so:

- Use plain text with paragraphs separated by one blank line and no line breaks inside a paragraph.
- Begin with `Chapter <number in words>. <Title>.` as its own paragraph, using the number given in your assignment.
- Put each spoken section heading in its own paragraph, ending with a period, at most 7 words. Every other paragraph must be longer than 7 words, because the renderer uses that word count to detect headings and adds pauses around them.
- Write all numbers in words ("forty-three", "two to the two hundred fifty-five"). Write out abbreviations you want spoken as words.
- Use only letters, digits-free words, and the punctuation `. , ; ' ? -` (hyphens only within compound words). Use no markdown, symbols, Greek letters, brackets, slashes, or parentheses. Spell out Greek letters and symbols by name if you must mention them.
- Write names with accents without them ("Schrodinger"), since the voice reads them correctly and the format allows only plain letters.
- End the chapter with a short spoken wrap-up and a pointer to the next chapter, following the chapter's own closing.

Each slide in `audio/slides/deck_NN.py` starts at the script sentence that begins with its `@slide("opening words", ...)`. After editing a script, run `../../.manim-venv/bin/python check.py NN` from `audio/slides/`. It reports anchors that no longer match, format problems, and spoken numbers that differ from the committed script. When a rewrite changes a sentence's opening, update that slide's anchor to the new opening words, long enough to match only that sentence.
