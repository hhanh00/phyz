<script setup>
const sections = [
  { title: 'Classical Mechanics', desc: 'Newton, Lagrangian, and Hamiltonian mechanics — the phase-space stage.', link: '/classical-mechanics.html' },
  { title: 'First Quantization', desc: 'Promote coordinates to operators; the commutator.', link: '/first-quantization.html' },
  { title: 'Harmonic Oscillator', desc: 'Ladder operators and the spectrum of quanta.', link: '/harmonic-oscillator.html' },
  { title: 'Special Relativity', desc: 'Spacetime, boosts, and the light cone.', link: '/special-relativity.html' },
  { title: 'Relativistic QM', desc: 'The Klein–Gordon equation and its trouble.', link: '/relativistic-qm.html' },
  { title: 'The Dirac Equation', desc: 'Spinors, antiparticles, and negative energies.', link: '/dirac-equation.html' },
  { title: 'Fields and Quanta', desc: 'Field operators create and destroy particles.', link: '/qft.html' },
  { title: 'Action and Lagrangians', desc: 'Read the Hamiltonian off the field equations.', link: '/qft-action.html' },
  { title: 'Field Quantization', desc: 'The free scalar field as a stack of oscillators.', link: '/field-quantization.html' },
  { title: 'Quantum Electrodynamics', desc: 'Photons, electrons, and the interaction.', link: '/qed.html', soon: true },
]
</script>

<template>
  <div class="section-grid">
    <a v-for="s in sections" :key="s.link" class="card" :href="s.link">
      <h3>{{ s.title }}</h3>
      <p>{{ s.desc }}</p>
      <span v-if="s.soon" class="soon">coming soon</span>
    </a>
  </div>
</template>

<style scoped>
.section-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  margin: 1.5rem 0;
}
@media (max-width: 900px) {
  .section-grid { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 600px) {
  .section-grid { grid-template-columns: 1fr; }
}
.card {
  display: block;
  padding: 1.1rem 1.2rem;
  border: 1px solid var(--vp-c-divider, #e2e2e2);
  border-radius: 8px;
  text-decoration: none;
  color: inherit;
  transition: border-color .2s, box-shadow .2s;
}
.card:hover {
  border-color: var(--vp-c-brand, #3a6cf4);
  box-shadow: 0 2px 8px rgba(0, 0, 0, .06);
}
.card h3 {
  margin: 0 0 .4rem;
  font-size: 1.05rem;
  font-weight: 600;
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
  font-size: .7rem;
  text-transform: uppercase;
  letter-spacing: .05em;
  color: #d97706;
}
</style>
