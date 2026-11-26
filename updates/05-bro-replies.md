# Chapter 5: `/bro what?` replies (2026-11-26)

These are the replies a fresh agent wrote for each section of `docs/relativistic-qm.md` during the bro-what test (iteration I in `05-relativistic-qm.md`). They are kept as raw material for revising the page. "Added" lists what the reply had to supply that the page and earlier chapters don't state. "Dropped" lists what the reply left out to make sense.

## Intro

Ok so last chapter the Schrödinger equation flunked relativity, because it treats time and space differently. Here we build the equation for fast particles. The first attempt is quick but has two problems. Fixing one gave Dirac's 1928 equation. The other problem turned out to be a prediction of a new kind of matter, and we open with the photo that found it.

- Added: nothing.
- Dropped: the table. Its "squared / not squared" row can't be read before section 6.

## 1. The trail

Anderson, 1932, photographs cosmic-ray trails in a cloud chamber inside a magnet. Plus and minus charges curve opposite ways, but only if you know the direction of travel. A lead plate settles that: the particle loses energy in it and curves tighter after. One trail came out curving like a positive charge. The only known positive particle was the proton, but a proton curving that tightly would be crawling and the gas would stop it almost at once. So: electron-light, but positive.

- Added: a heavy proton must be slow to curve that tightly, and the gas stops slow particles quickly.
- Dropped: nothing.

## 2. The recipe

Reminder of the trick. A free particle with definite momentum and energy is a wave whose phase turns steadily in space and time. Time-rate times iħ pulls out E, and slope times −iħ pulls out p. So take any rule linking E and p, swap each letter for its operation, and you get a wave equation. E = p²/2m gives Schrödinger: one time-rate, two slopes. That lopsidedness is what failed relativity.

- Added: nothing.
- Flags: "by p/ħ per metre" has no angle unit, and 2b's main text says "p/h turns per metre". The wave with −Et appears only in 2b's boxes.

## 3. Klein–Gordon

Same recipe, with the any-speed rule E² = (pc)² + (mc²)². E is squared, so the time operation is done twice. Tidy up and you get the Klein–Gordon equation: two time-rates, two slopes, a minus between them, like the interval. So it looks the same to every observer. Plug the wave back in and it works exactly when E and p obey the relativistic rule. Good so far, but two problems are coming.

- Added: nothing. The cleanest section.

## 4. Negative energies

The rule fixes E², and a square has two roots, so every momentum has a +E and a −E. Classically you bin the negative one, because energy changes smoothly and can't cross the gap between −mc² and +mc². Quantum things jump, like chapter 3's rungs. So an electron could jump down into negative energy, spit out light, and jump again, with no bottom rung. Every electron would fall forever. You can't ban those solutions either.

- Added: "things drop to lower energy by giving off light when they can". No earlier chapter says it.
- Dropped: "The same push from light that moves an electron between two positive-energy states". Light moving electrons between states was never introduced.

## 5. Negative chance

|ψ|² works as a chance because it's never negative and its total stays one. Klein–Gordon doesn't keep that total. It keeps a different quantity, which for a wave of energy E is (E/mc²)|ψ|². That's fine for positive energy and negative for negative energy, and a negative chance means nothing. So one candidate isn't kept, and the kept one isn't always positive.

- Added: nothing.
- Dropped: the Newton paragraph ("need ψ and how fast it's changing") and its table row. It ends in "it turns out", so it doesn't explain why the total fails.

## 6. Dirac's idea

Dirac blames the two time-rates, which come from E². So he wants a rule with plain E. Relativity says time and space get equal treatment, so p must be plain too: E = α·pc + β·mc². Squaring it must give back the relativistic rule, so α² = 1, β² = 1, and the cross term αβ + βα must vanish. No ordinary numbers do that.

- Added: nothing. "Keep them in the order they come" is well placed.

## 7. The Dirac equation

Matrices can do it, because order matters for them. The spin operators Ẑ and Ŝ from 2b already square to 1 and flip sign when swapped ("anticommute"). The price is that the state becomes a column of two wave functions. Run the recipe: one time-rate, one slope. In real space there are three momentum parts plus the mass, so four mutually anticommuting matrices are needed. Two-by-two only has three, three-by-three fails, so it's four-by-four and a column of four.

- Added: the right-hand side is now an operator acting on the column, like 2b's Ĥ. The text leaves "E = a matrix" unexplained.
- Dropped: the three-by-three eigenvalue argument, and most of "why the four must all be different".

## 8. Chance fixed

With a column, the chance per metre is the sum of the entries' squared lengths. Sums of squares can't be negative, and the Dirac equation keeps the total at one. Problem two is solved.

- Added: nothing.
- Dropped: nothing. It could say it worked because there is one time-rate, to close section 6's loop.

## 9. Antimatter

Negative energies survive. At rest the rule is E = β·mc², and β = Ẑ gives the top entry +mc² and the bottom −mc². Dirac's patch: say all negative states are already full (the "sea"), and since two electrons can't share a state, nothing can fall. Kick one sea electron up with 2mc² and it leaves a hole, which looks like a positive-charge, positive-energy electron. Dirac predicted it in 1931 and Anderson photographed it in 1932: the positron.

- Added: "the allowed energies are the matrix's eigenvalues".
- Flags: "two get +mc² and two get −mc²" doesn't say why two. "A way of counting more than a picture" stands as a one-liner.

## 10. Why fields

The sea got dropped. It needs infinitely many invisible electrons, and particles that ignore exclusion have antiparticles too. The real lesson is that light went in and two particles came out, so the particle number changed. A wave function describes one particle and can't count. Chapter 3's rungs can. Treat ψ as a field, where each wave is a spring and its rung is the number of particles. Then negative-energy waves mean making antiparticles, and section 5's negative quantity is charge.

- Added: nothing, but the reply could only repeat the last paragraph, not explain it.
- Flag: "antiparticles" is used without definition.
