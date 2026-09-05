<script setup>
const groups = [
  {
    name: 'Quantum Mechanics',
    desc: 'The stage and the rules — phase space, operators, and the oscillator.',
    color: '#2563eb',
    items: [
      { title: 'Classical Mechanics', desc: 'Newton, Lagrangian, and Hamiltonian mechanics — the phase-space stage.', link: '/classical-mechanics.html' },
      { title: 'First Quantization', desc: 'Promote coordinates to operators; the commutator.', link: '/first-quantization.html' },
      { title: 'Harmonic Oscillator', desc: 'Ladder operators and the spectrum of quanta.', link: '/harmonic-oscillator.html' },
    ],
  },
  {
    name: 'Relativity',
    desc: 'Spacetime and its quantum price — boosts, wave equations, spinors.',
    color: '#7c3aed',
    items: [
      { title: 'Special Relativity', desc: 'Spacetime, boosts, and the light cone.', link: '/special-relativity.html' },
      { title: 'Relativistic QM', desc: 'The Klein–Gordon equation and its trouble.', link: '/relativistic-qm.html' },
      { title: 'The Dirac Equation', desc: 'Spinors, antiparticles, and negative energies.', link: '/dirac-equation.html' },
    ],
  },
  {
    name: 'Quantum Field Theory',
    desc: 'Promote the field — operators, actions, and quanta.',
    color: '#059669',
    items: [
      { title: 'Fields and Quanta', desc: 'Field operators create and destroy particles.', link: '/qft.html' },
      { title: 'Action and Lagrangians', desc: 'Read the Hamiltonian off the field equations.', link: '/qft-action.html' },
      { title: 'Field Quantization', desc: 'The free scalar field as a stack of oscillators.', link: '/field-quantization.html' },
    ],
  },
  {
    name: 'Quantum Electrodynamics',
    desc: 'The next step — turning the interaction on.',
    color: '#d97706',
    items: [
      { title: 'Quantum Electrodynamics', desc: 'Photons, electrons, and the interaction.', link: '/qed.html', soon: true },
    ],
  },
]
</script>

<template>
  <div class="home-body">
    <p class="lead">
      Notes that run from classical mechanics to quantum electrodynamics, written to be read
      in order. Each page hands the next its tools — the harmonic oscillator becomes a field
      mode, the Dirac equation's negative energies become antiparticles.
    </p>

    <section v-for="g in groups" :key="g.name" class="group" :style="{ '--accent': g.color }">
      <header class="group-head">
        <h2 class="group-title">{{ g.name }}</h2>
        <p class="group-desc">{{ g.desc }}</p>
      </header>
      <div class="cards">
        <a v-for="s in g.items" :key="s.link" class="card" :href="s.link">
          <h3>{{ s.title }}</h3>
          <p>{{ s.desc }}</p>
          <span v-if="s.soon" class="soon">coming soon</span>
        </a>
      </div>
    </section>
  </div>
</template>

<style scoped>
.home-body {
  margin: 2rem 0;
}
.lead {
  max-width: 44rem;
  margin: 0 auto 2.5rem;
  text-align: center;
  font-size: 1.05rem;
  line-height: 1.6;
  color: var(--vp-c-text-mute, #666);
}
.group + .group {
  margin-top: 2.25rem;
}
.group-head {
  margin-bottom: .75rem;
}
.group-title {
  margin: 0;
  font-size: 1.05rem;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--accent);
}
.group-desc {
  margin: .15rem 0 0;
  font-size: .9rem;
  color: var(--vp-c-text-mute, #666);
}
.cards {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
}
@media (max-width: 900px) {
  .cards { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 600px) {
  .cards { grid-template-columns: 1fr; }
}
.card {
  display: block;
  padding: 1rem 1.1rem;
  border: 1px solid var(--vp-c-divider, #e2e2e2);
  border-left: 3px solid var(--accent);
  border-radius: 10px;
  text-decoration: none;
  color: inherit;
  background: var(--vp-c-bg, #fff);
  transition: border-color .2s, box-shadow .2s, transform .2s;
}
.home-body a.card,
.home-body a.card:hover,
.home-body a.card:active,
.home-body a.card:visited,
.home-body a.card h3,
.home-body a.card p {
  text-decoration: none;
}
.card:hover {
  border-color: var(--accent);
  box-shadow: 0 4px 14px rgba(0, 0, 0, .08);
  transform: translateY(-2px);
}
.card h3 {
  margin: 0 0 .35rem;
  font-size: 1.05rem;
  font-weight: 600;
  color: var(--accent);
}
.card p {
  margin: 0;
  font-size: .9rem;
  color: var(--vp-c-text-mute, #666);
  line-height: 1.5;
}
.soon {
  display: inline-block;
  margin-top: .5rem;
  padding: .1rem .5rem;
  border: 1px solid var(--accent);
  border-radius: 999px;
  font-size: .68rem;
  text-transform: uppercase;
  letter-spacing: .05em;
  color: var(--accent);
}
</style>
