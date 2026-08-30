<template>
  <div class="st-wrap">
    <!-- Galilean -->
    <figure>
      <svg viewBox="0 0 200 210" width="200" height="210" class="st-svg"
           role="img" aria-label="Galilean boost spacetime diagram">
        <defs>
          <marker id="g-gray" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
            <path d="M0,0 L6,3 L0,6 Z" fill="#666"/>
          </marker>
          <marker id="g-blue" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
            <path d="M0,0 L6,3 L0,6 Z" fill="#2563eb"/>
          </marker>
        </defs>
        <!-- light cone -->
        <line x1="100" y1="165" x2="190" y2="75"  stroke="#d97706" stroke-width="1.5" stroke-dasharray="5,3"/>
        <line x1="100" y1="165" x2="10"  y2="75"  stroke="#d97706" stroke-width="1.5" stroke-dasharray="5,3"/>
        <!-- x = x' axis -->
        <line x1="12"  y1="165" x2="188" y2="165" stroke="#666" stroke-width="1.5" marker-end="url(#g-gray)"/>
        <!-- t axis -->
        <line x1="100" y1="190" x2="100" y2="14"  stroke="#666" stroke-width="1.5" marker-end="url(#g-gray)"/>
        <!-- t' axis (tilts right; x=vt with v=0.5) -->
        <line x1="89"  y1="190" x2="178" y2="12"  stroke="#2563eb" stroke-width="1.5" marker-end="url(#g-blue)"/>
        <!-- labels -->
        <text x="105" y="13"  font-size="13" fill="#555" font-style="italic">t</text>
        <text x="172" y="13"  font-size="13" fill="#2563eb" font-style="italic">t′</text>
        <text x="116" y="178" font-size="12" fill="#666" font-style="italic">x = x′</text>
        <text x="148" y="68"  font-size="10" fill="#d97706">light</text>
        <!-- origin -->
        <circle cx="100" cy="165" r="2.5" fill="#333"/>
      </svg>
      <figcaption>
        Galilean: <em>x′ = x</em> stays horizontal;<br/>light ray not bisected
      </figcaption>
    </figure>

    <!-- Lorentz -->
    <figure>
      <svg viewBox="0 0 200 210" width="200" height="210" class="st-svg"
           role="img" aria-label="Lorentz boost spacetime diagram">
        <defs>
          <marker id="l-gray" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
            <path d="M0,0 L6,3 L0,6 Z" fill="#666"/>
          </marker>
          <marker id="l-blue" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
            <path d="M0,0 L6,3 L0,6 Z" fill="#2563eb"/>
          </marker>
        </defs>
        <!-- light cone -->
        <line x1="100" y1="165" x2="190" y2="75"  stroke="#d97706" stroke-width="1.5" stroke-dasharray="5,3"/>
        <line x1="100" y1="165" x2="10"  y2="75"  stroke="#d97706" stroke-width="1.5" stroke-dasharray="5,3"/>
        <!-- x axis (unprimed) -->
        <line x1="12"  y1="165" x2="188" y2="165" stroke="#666" stroke-width="1.5" marker-end="url(#l-gray)"/>
        <!-- t axis (unprimed) -->
        <line x1="100" y1="190" x2="100" y2="14"  stroke="#666" stroke-width="1.5" marker-end="url(#l-gray)"/>
        <!-- t' axis (same direction as Galilean t': tilts right) -->
        <line x1="89"  y1="190" x2="178" y2="12"  stroke="#2563eb" stroke-width="1.5" marker-end="url(#l-blue)"/>
        <!-- x' axis (tilts up symmetrically: t=vx with v=0.5) -->
        <line x1="40"  y1="195" x2="184" y2="123" stroke="#2563eb" stroke-width="1.5" marker-end="url(#l-blue)"/>
        <!-- labels -->
        <text x="105" y="13"  font-size="13" fill="#555" font-style="italic">t</text>
        <text x="172" y="13"  font-size="13" fill="#2563eb" font-style="italic">t′</text>
        <text x="184" y="178" font-size="13" fill="#666" font-style="italic">x</text>
        <text x="184" y="120" font-size="13" fill="#2563eb" font-style="italic">x′</text>
        <text x="148" y="68"  font-size="10" fill="#d97706">light</text>
        <!-- origin -->
        <circle cx="100" cy="165" r="2.5" fill="#333"/>
      </svg>
      <figcaption>
        Lorentz: both axes tilt symmetrically;<br/>light ray bisects <em>t′</em> and <em>x′</em>
      </figcaption>
    </figure>
  </div>
</template>

<style scoped>
.st-wrap {
  display: flex;
  gap: 2.5rem;
  justify-content: center;
  flex-wrap: wrap;
  margin: 1.5rem 0;
}
.st-wrap figure {
  margin: 0;
  text-align: center;
}
.st-svg {
  display: block;
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 6px;
}
.st-wrap figcaption {
  margin-top: 0.5rem;
  font-size: 0.82rem;
  color: #6b7280;
  max-width: 200px;
  line-height: 1.4;
}
</style>
