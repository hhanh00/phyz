<script setup>
const groups = [
  {
    number: '01',
    name: 'Foundations',
    eyebrow: 'Motion becomes mechanics',
    desc: 'Build the language of states, operators, and discrete energy.',
    color: '#2563eb',
    soft: '#dbeafe',
    items: [
      { number: '01', title: 'Classical Mechanics', desc: 'From Newton’s laws to motion through phase space.', link: '/classical-mechanics.html', symbol: 'q, p' },
      { number: '02', title: 'First Quantization', desc: 'Replace classical coordinates with operators and commutators.', link: '/first-quantization.html', symbol: '[x̂, p̂]' },
      { number: '03', title: 'Harmonic Oscillator', desc: 'Use ladder operators to uncover a spectrum of quanta.', link: '/harmonic-oscillator.html', symbol: 'a†' },
    ],
  },
  {
    number: '02',
    name: 'Relativity',
    eyebrow: 'Space and time become spacetime',
    desc: 'Follow the cost of making quantum mechanics relativistic.',
    color: '#7c3aed',
    soft: '#ede9fe',
    items: [
      { number: '04', title: 'Special Relativity', desc: 'See how boosts, intervals, and light cones organize spacetime.', link: '/special-relativity.html', symbol: 'xμ' },
      { number: '05', title: 'Relativistic QM', desc: 'Meet the Klein–Gordon equation and the problem it exposes.', link: '/relativistic-qm.html', symbol: '□ + m²' },
      { number: '06', title: 'The Dirac Equation', desc: 'Bring spinors, antiparticles, and negative energy into view.', link: '/dirac-equation.html', symbol: 'γμ' },
    ],
  },
  {
    number: '03',
    name: 'Quantum fields',
    eyebrow: 'Particles become excitations',
    desc: 'Treat each field mode as an oscillator and quantize the whole field.',
    color: '#059669',
    soft: '#d1fae5',
    items: [
      { number: '07', title: 'Fields and Quanta', desc: 'Let field operators create and destroy particles.', link: '/qft.html', symbol: 'φ̂(x)' },
      { number: '08', title: 'Action and Lagrangians', desc: 'Move from field equations to actions and conserved structure.', link: '/qft-action.html', symbol: 'ℒ' },
      { number: '09', title: 'Field Quantization', desc: 'Assemble the free scalar field from infinitely many oscillators.', link: '/field-quantization.html', symbol: '∫d³p' },
    ],
  },
  {
    number: '04',
    name: 'Quantum Electrodynamics',
    eyebrow: 'Symmetry demands the photon',
    desc: 'Local U(1) symmetry produces the photon, and its rules yield the first amplitudes.',
    color: '#d97706',
    soft: '#fef3c7',
    items: [
      { number: '10', title: 'Quantum Electrodynamics', desc: 'Connect photons and electrons through the electromagnetic field.', link: '/qed.html', symbol: 'eAμ' },
      { number: '11', title: 'Feynman Rules for QED', desc: 'Turn the Lagrangian into rules that compute scattering amplitudes.', link: '/feynman-rules.html', symbol: 'iℳ' },
    ],
  },
  {
    number: '05',
    name: 'Electroweak',
    eyebrow: 'The weak force unifies',
    desc: 'SU(2) and the Higgs unite the weak force with QED.',
    color: '#db2777',
    soft: '#fce7f3',
    items: [
      { number: '12', title: 'Weak Interaction', desc: 'Beta decay reveals a short-range force carried by the W bosons.', link: '/weak-interaction.html', symbol: 'W±' },
      { number: '13', title: 'Electroweak Unification', desc: 'Unite the weak force with QED under SU(2)×U(1) symmetry.', link: '/electroweak-unification.html', symbol: 'Z⁰' },
      { number: '14', title: 'Higgs Mechanism', desc: 'Break the symmetry spontaneously and give the W and Z their mass.', link: '/higgs-mechanism.html', symbol: 'H' },
    ],
  },
  {
    number: '06',
    name: 'Strong & Standard Model',
    eyebrow: 'The theory completes',
    desc: 'Color, quarks, and confinement round out the gauge structure.',
    color: '#0e7490',
    soft: '#cffafe',
    items: [
      { number: '15', title: 'Quantum Chromodynamics', desc: 'Quarks carry color; SU(3) symmetry confines them into hadrons.', link: '/qcd.html', symbol: 'SU(3)' },
      { number: '16', title: 'The Standard Model', desc: 'Assemble the full gauge theory of quarks, leptons, and forces.', link: '/standard-model.html', symbol: '3·2·1', final: true },
    ],
  },
]
</script>

<template>
  <div class="phyz-home">
    <section class="home-hero" aria-labelledby="home-title">
      <div class="hero-copy">
        <p class="kicker"><span class="kicker-dot"></span>A guided physics sequence</p>
        <h1 id="home-title">From motion<br><em>to fields.</em></h1>
        <p class="hero-text">
          A connected set of notes that builds particle physics from first principles,
          one idea at a time.
        </p>
        <div class="hero-actions">
          <a class="start-button" href="/classical-mechanics.html">
            Start with mechanics
            <svg viewBox="0 0 20 20" aria-hidden="true"><path d="M4 10h11m-4-4 4 4-4 4" /></svg>
          </a>
          <span class="chapter-count"><strong>16</strong> connected chapters</span>
        </div>
      </div>

      <div class="field-visual" aria-hidden="true">
        <div class="visual-grid"></div>
        <svg class="field-lines" viewBox="0 0 520 420" fill="none">
          <path d="M20 226C87 87 176 82 256 218s172 151 244 4" />
          <path d="M20 276c68-81 142-77 217 2s169 84 263-7" />
          <path d="M42 157c74-74 136-77 202 9s149 89 238-12" />
          <ellipse cx="271" cy="215" rx="174" ry="73" transform="rotate(-24 271 215)" />
          <ellipse cx="271" cy="215" rx="174" ry="73" transform="rotate(34 271 215)" />
        </svg>
        <div class="visual-core">
          <span>ψ</span>
          <small>state</small>
        </div>
        <span class="particle particle-a"></span>
        <span class="particle particle-b"></span>
        <span class="particle particle-c"></span>
        <div class="formula formula-a">E = ℏω</div>
        <div class="formula formula-b">S = ∫ ℒ d⁴x</div>
        <div class="axis-label axis-x">space</div>
        <div class="axis-label axis-t">time</div>
      </div>
    </section>

    <div class="concept-strip" aria-label="The conceptual progression through the course">
      <span>trajectory</span><i>→</i>
      <span>wavefunction</span><i>→</i>
      <span>quantum field</span><i>→</i>
      <span>interaction</span><i>→</i>
      <span>standard model</span>
    </div>

    <section class="curriculum" aria-labelledby="curriculum-title">
      <div class="curriculum-intro">
        <div>
          <p class="section-label">The learning path</p>
          <h2 id="curriculum-title">One argument, built in stages.</h2>
        </div>
        <p>Read in order, or jump directly to the idea you need.</p>
      </div>

      <div class="stages">
        <section
          v-for="g in groups"
          :key="g.name"
          class="stage"
          :style="{ '--accent': g.color, '--accent-soft': g.soft }"
        >
          <div class="stage-marker" aria-hidden="true">
            <span>{{ g.number }}</span>
          </div>

          <header class="stage-head">
            <p>{{ g.eyebrow }}</p>
            <h3>{{ g.name }}</h3>
            <div class="stage-rule"></div>
            <p class="stage-desc">{{ g.desc }}</p>
          </header>

          <div class="cards" :class="{ 'cards-single': g.items.length === 1 }">
            <a
              v-for="s in g.items"
              :key="s.link"
              class="chapter-card"
              :class="{ 'final-card': s.final }"
              :href="s.link"
            >
              <div class="card-topline">
                <span class="chapter-number">Chapter {{ s.number }}</span>
                <span class="chapter-symbol">{{ s.symbol }}</span>
              </div>
              <h4>{{ s.title }}</h4>
              <p>{{ s.desc }}</p>
              <span class="read-link">
                Read chapter
                <svg viewBox="0 0 20 20" aria-hidden="true"><path d="M4 10h11m-4-4 4 4-4 4" /></svg>
              </span>
            </a>
          </div>
        </section>
      </div>
    </section>

    <aside class="closing-note">
      <span class="closing-symbol">∑</span>
      <div>
        <p class="section-label">The thread</p>
        <p>Each chapter carries one tool forward, so the final theory feels constructed rather than announced.</p>
      </div>
      <a href="/classical-mechanics.html">Begin chapter 01 <span aria-hidden="true">→</span></a>
    </aside>
  </div>
</template>

<style>
.vp-home .vp-hero { display: none; }
.vp-home { padding: 0; max-width: none; }
.vp-home [vp-content] { max-width: none; padding: 0; }
.vp-home [vp-content] > div { max-width: none; }

.phyz-home {
  --ink: #152238;
  --muted: #5f6b7c;
  --paper: #fbfcfe;
  --line: #dfe5ec;
  color: var(--ink);
  overflow: hidden;
}
.home-hero {
  position: relative;
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(380px, .9fr);
  align-items: center;
  gap: clamp(2rem, 6vw, 6.5rem);
  max-width: 1280px;
  min-height: 560px;
  margin: 0 auto;
  padding: clamp(4.5rem, 8vw, 7.5rem) clamp(2rem, 6vw, 5.5rem) 4.5rem;
}
.hero-copy { position: relative; z-index: 2; }
.kicker, .section-label { margin: 0; color: #2563eb; font-size: .73rem; font-weight: 750; letter-spacing: .14em; text-transform: uppercase; }
.kicker { display: flex; align-items: center; gap: .6rem; }
.kicker-dot { width: 7px; height: 7px; border-radius: 50%; background: #2563eb; box-shadow: 0 0 0 5px rgba(37, 99, 235, .12); }
.home-hero h1 { margin: 1.25rem 0 1.35rem; color: var(--ink); font-family: Georgia, 'Times New Roman', serif; font-size: clamp(3.8rem, 7vw, 6.5rem); font-weight: 500; letter-spacing: -.055em; line-height: .88; }
.home-hero h1 em { color: #2563eb; font-weight: 500; }
.hero-text { max-width: 35rem; margin: 0; color: var(--muted); font-size: clamp(1.05rem, 1.7vw, 1.3rem); line-height: 1.65; }
.hero-actions { display: flex; align-items: center; gap: 1.5rem; margin-top: 2rem; }
.start-button { display: inline-flex; align-items: center; gap: .7rem; padding: .85rem 1.1rem; border-radius: 8px; color: #fff !important; background: #152238; font-size: .9rem; font-weight: 650; text-decoration: none !important; box-shadow: 0 9px 24px rgba(21, 34, 56, .16); transition: transform .2s ease, background .2s ease, box-shadow .2s ease; }
.start-button:hover { background: #2563eb; transform: translateY(-2px); box-shadow: 0 12px 30px rgba(37, 99, 235, .2); }
.start-button:focus-visible, .chapter-card:focus-visible, .closing-note a:focus-visible { outline: 3px solid #60a5fa; outline-offset: 4px; }
.start-button svg, .read-link svg { width: 18px; stroke: currentColor; stroke-width: 1.7; stroke-linecap: round; stroke-linejoin: round; }
.chapter-count { color: var(--muted); font-size: .84rem; }
.chapter-count strong { color: var(--ink); font-family: Georgia, serif; font-size: 1.2rem; }
.field-visual { position: relative; width: min(100%, 500px); aspect-ratio: 1.18; justify-self: center; border: 1px solid rgba(37, 99, 235, .18); border-radius: 50% 50% 48% 52% / 43% 55% 45% 57%; background: radial-gradient(circle at 50% 50%, rgba(37, 99, 235, .1), transparent 24%), linear-gradient(145deg, rgba(219, 234, 254, .7), rgba(238, 242, 255, .2)); transform: rotate(-2deg); }
.visual-grid { position: absolute; inset: 7%; border-radius: inherit; opacity: .35; background-image: linear-gradient(rgba(37, 99, 235, .15) 1px, transparent 1px), linear-gradient(90deg, rgba(37, 99, 235, .15) 1px, transparent 1px); background-size: 38px 38px; mask-image: radial-gradient(circle, #000 20%, transparent 72%); }
.field-lines { position: absolute; inset: 3%; width: 94%; height: 94%; stroke: #2563eb; stroke-width: 1.2; opacity: .5; }
.field-lines ellipse { stroke-dasharray: 4 7; opacity: .65; }
.visual-core { position: absolute; top: 50%; left: 52%; display: grid; place-items: center; width: 102px; height: 102px; border: 1px solid rgba(37, 99, 235, .25); border-radius: 50%; background: rgba(255, 255, 255, .8); box-shadow: 0 22px 60px rgba(37, 99, 235, .18), inset 0 0 0 8px rgba(37, 99, 235, .04); transform: translate(-50%, -50%); }
.visual-core span { margin-top: .55rem; color: #2563eb; font-family: Georgia, serif; font-size: 2.4rem; font-style: italic; line-height: 1; }
.visual-core small { align-self: start; color: var(--muted); font-size: .62rem; letter-spacing: .14em; text-transform: uppercase; }
.particle { position: absolute; width: 10px; height: 10px; border: 3px solid #fff; border-radius: 50%; background: #7c3aed; box-shadow: 0 3px 12px rgba(124, 58, 237, .4); }
.particle-a { top: 24%; left: 18%; }
.particle-b { right: 14%; bottom: 29%; background: #059669; box-shadow: 0 3px 12px rgba(5, 150, 105, .4); }
.particle-c { right: 20%; top: 20%; width: 7px; height: 7px; background: #d97706; }
.formula { position: absolute; padding: .45rem .7rem; border: 1px solid rgba(21, 34, 56, .1); border-radius: 6px; color: var(--ink); background: rgba(255, 255, 255, .82); font-family: Georgia, serif; font-size: .82rem; box-shadow: 0 8px 22px rgba(21, 34, 56, .08); backdrop-filter: blur(8px); }
.formula-a { top: 10%; right: 9%; }
.formula-b { bottom: 11%; left: 8%; }
.axis-label { position: absolute; color: #8290a3; font-size: .6rem; letter-spacing: .12em; text-transform: uppercase; }
.axis-x { right: 5%; top: 51%; }
.axis-t { left: 51%; top: 4%; writing-mode: vertical-rl; }
.concept-strip { display: flex; align-items: center; justify-content: center; gap: clamp(.8rem, 2.5vw, 2.5rem); padding: 1.05rem 2rem; border-block: 1px solid var(--line); color: #6d7786; background: #f6f8fb; font-size: .68rem; font-weight: 700; letter-spacing: .12em; text-transform: uppercase; }
.concept-strip i { color: #aab3c0; font-size: 1rem; font-style: normal; }
.curriculum { max-width: 1280px; margin: 0 auto; padding: 6rem clamp(2rem, 6vw, 5.5rem) 5rem; }
.curriculum-intro { display: flex; align-items: end; justify-content: space-between; gap: 3rem; padding-bottom: 2.5rem; }
.curriculum-intro h2 { margin: .55rem 0 0; color: var(--ink); font-family: Georgia, serif; font-size: clamp(2rem, 4vw, 3.25rem); font-weight: 500; letter-spacing: -.035em; }
.curriculum-intro > p { max-width: 20rem; margin: 0 0 .35rem; color: var(--muted); font-size: .9rem; line-height: 1.55; }
.stages { position: relative; }
.stages::before { content: ''; position: absolute; top: 1.6rem; bottom: 1.6rem; left: 25px; width: 1px; background: var(--line); }
.stage { position: relative; display: grid; grid-template-columns: 52px minmax(180px, .72fr) minmax(0, 2.2fr); gap: clamp(1.25rem, 3vw, 3.5rem); padding: 2.8rem 0; border-top: 1px solid var(--line); }
.stage:last-child { border-bottom: 1px solid var(--line); }
.stage-marker { position: relative; z-index: 1; padding-top: .1rem; }
.stage-marker span { display: grid; place-items: center; width: 51px; height: 51px; border: 1px solid color-mix(in srgb, var(--accent) 35%, white); border-radius: 50%; color: var(--accent); background: var(--paper); font-family: Georgia, serif; font-size: .9rem; font-weight: 700; }
.stage-head > p:first-child { margin: .1rem 0 .45rem; color: var(--accent); font-size: .65rem; font-weight: 750; letter-spacing: .1em; text-transform: uppercase; }
.stage-head h3 { margin: 0; border: 0; color: var(--ink); font-family: Georgia, serif; font-size: 1.7rem; font-weight: 500; letter-spacing: -.025em; }
.stage-rule { width: 2rem; height: 2px; margin: 1.1rem 0; background: var(--accent); }
.stage-desc { max-width: 15rem; margin: 0; color: var(--muted); font-size: .82rem; line-height: 1.6; }
.cards { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: .8rem; }
.chapter-card { position: relative; display: flex; min-height: 230px; flex-direction: column; padding: 1.15rem; border: 1px solid var(--line); border-radius: 10px; color: inherit !important; background: #fff; text-decoration: none !important; box-shadow: 0 1px 0 rgba(21, 34, 56, .02); transition: border-color .2s ease, box-shadow .2s ease, transform .2s ease; }
.chapter-card::before { content: ''; position: absolute; inset: 0 0 auto; height: 3px; border-radius: 10px 10px 0 0; background: var(--accent); transform: scaleX(0); transform-origin: left; transition: transform .25s ease; }
.chapter-card:hover { border-color: color-mix(in srgb, var(--accent) 45%, white); box-shadow: 0 14px 36px rgba(21, 34, 56, .09); transform: translateY(-4px); }
.chapter-card:hover::before { transform: scaleX(1); }
.card-topline { display: flex; align-items: center; justify-content: space-between; gap: 1rem; }
.chapter-number { color: #8a94a3; font-size: .62rem; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; }
.chapter-symbol { display: grid; place-items: center; min-width: 38px; height: 30px; padding: 0 .35rem; border-radius: 6px; color: var(--accent); background: var(--accent-soft); font-family: Georgia, serif; font-size: .76rem; font-style: italic; }
.chapter-card h4 { margin: 1.5rem 0 .65rem; color: var(--ink); font-family: Georgia, serif; font-size: 1.22rem; font-weight: 600; letter-spacing: -.015em; line-height: 1.15; }
.chapter-card > p { margin: 0; color: var(--muted); font-size: .78rem; line-height: 1.55; }
.read-link { display: flex; align-items: center; gap: .4rem; margin-top: auto; padding-top: 1.1rem; color: var(--accent); font-size: .72rem; font-weight: 700; }
.read-link svg { width: 15px; transition: transform .2s ease; }
.chapter-card:hover .read-link svg { transform: translateX(3px); }
.cards-single { grid-template-columns: minmax(240px, 1fr) 2fr; }
.final-card { min-height: 200px; background: linear-gradient(135deg, #fff, color-mix(in srgb, var(--accent-soft) 52%, white)); }
.closing-note { display: grid; grid-template-columns: auto 1fr auto; align-items: center; gap: 1.5rem; max-width: calc(1280px - clamp(4rem, 12vw, 11rem)); margin: 0 auto 6rem; padding: 1.6rem 1.8rem; border-radius: 12px; color: #fff; background: var(--ink); }
.closing-symbol { display: grid; place-items: center; width: 52px; height: 52px; border: 1px solid rgba(255,255,255,.2); border-radius: 50%; color: #93c5fd; font-family: Georgia, serif; font-size: 1.7rem; }
.closing-note .section-label { color: #93c5fd; }
.closing-note div > p:last-child { max-width: 38rem; margin: .3rem 0 0; color: #cbd5e1; font-family: Georgia, serif; font-size: 1rem; line-height: 1.45; }
.closing-note a { color: #fff !important; font-size: .75rem; font-weight: 700; text-decoration: none !important; white-space: nowrap; }
.closing-note a span { margin-left: .35rem; color: #93c5fd; }
@media (max-width: 960px) {
  .home-hero { grid-template-columns: 1fr minmax(310px, .75fr); min-height: 500px; gap: 2rem; }
  .stage { grid-template-columns: 52px 1fr; }
  .cards { grid-column: 2; }
  .stage-desc { max-width: 30rem; }
}
@media (max-width: 720px) {
  .home-hero { grid-template-columns: 1fr; min-height: 0; padding-top: 4.5rem; }
  .field-visual { width: min(100%, 430px); margin-top: 1rem; }
  .concept-strip { justify-content: flex-start; overflow-x: auto; }
  .concept-strip span { white-space: nowrap; }
  .curriculum { padding-top: 4.5rem; }
  .curriculum-intro { display: block; }
  .curriculum-intro > p { margin-top: 1rem; }
  .cards { grid-template-columns: 1fr; }
  .cards-single { grid-template-columns: 1fr; }
  .chapter-card { min-height: 190px; }
  .closing-note { grid-template-columns: auto 1fr; margin-inline: 1.25rem; }
  .closing-note a { grid-column: 2; }
}
@media (max-width: 480px) {
  .home-hero, .curriculum { padding-inline: 1.25rem; }
  .home-hero h1 { font-size: 3.65rem; }
  .hero-actions { align-items: flex-start; flex-direction: column; gap: 1rem; }
  .field-visual { width: 108%; margin-left: -4%; }
  .stage { grid-template-columns: 40px 1fr; gap: 1rem; }
  .stages::before { left: 19px; }
  .stage-marker span { width: 39px; height: 39px; font-size: .72rem; }
  .cards { grid-column: 1 / -1; }
  .closing-note { padding: 1.35rem; }
  .closing-symbol { display: none; }
  .closing-note, .closing-note a { grid-column: auto; }
}
[data-theme='dark'] .phyz-home { --ink: #edf3fb; --muted: #aab6c6; --paper: #1b1b1f; --line: #343b47; }
[data-theme='dark'] .field-visual { background: radial-gradient(circle at 50% 50%, rgba(96, 165, 250, .13), transparent 24%), linear-gradient(145deg, rgba(30, 58, 138, .25), rgba(30, 41, 59, .08)); }
[data-theme='dark'] .visual-core, [data-theme='dark'] .formula { background: rgba(27, 27, 31, .82); }
[data-theme='dark'] .concept-strip { background: #202126; }
[data-theme='dark'] .chapter-card { background: #202126; }
[data-theme='dark'] .final-card { background: linear-gradient(135deg, #202126, rgba(120, 75, 10, .14)); }
[data-theme='dark'] .closing-note { color: #152238; background: #e8eef7; }
[data-theme='dark'] .closing-note div > p:last-child { color: #536072; }
[data-theme='dark'] .closing-note a { color: #152238 !important; }
@media (prefers-reduced-motion: reduce) {
  .start-button, .chapter-card, .chapter-card::before, .read-link svg { transition: none; }
}
</style>
