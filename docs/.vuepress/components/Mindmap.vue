<script setup>
import { onMounted, onBeforeUnmount, ref, watch } from 'vue'
import { layoutMindmap } from '../lib/mindmap.js'

const props = defineProps({ source: { type: String, required: true } })
const host = ref(null)
const ready = ref(false)
const error = ref('')
const selected = ref('')
const topics = ref([])
const navigation = ref('pan')
let mouseButtons
let graph, observer, themeObserver, SpriteText
let collapsed = new Set()
let all = []
let parents = new Map()
let disposed = false
let fitPending = true
let duration = 700

function overview() {
  all = layoutMindmap(props.source).nodes
  topics.value = all.filter(n => n.depth === 1)
  const root = all[0]
  if (root) {
    Object.assign(root, { fx: 0, fy: 0, fz: 0 })
    function position(node, angle, spread, elevation) {
      const radius = 125 + (node.depth - 1) * 90
      Object.assign(node, {
        fx: Math.cos(angle) * Math.cos(elevation) * radius,
        fy: Math.sin(angle) * Math.cos(elevation) * radius,
        fz: Math.sin(elevation) * radius,
      })
      node.children.forEach((child, i) => {
        const offset = (i + .5) / node.children.length - .5
        position(child, angle + offset * spread, spread / Math.max(1, node.children.length), elevation + offset * .65)
      })
    }
    root.children.forEach((node, i) => position(node, i * Math.PI * 2 / root.children.length, Math.PI * 2 / root.children.length * .9, (i % 3 - 1) * .48))
  }
  parents = new Map(all.flatMap(n => n.children.map(c => [c.id, n.id])))
  collapsed = new Set(all.filter(n => n.depth >= 2 && n.children.length).map(n => n.id))
  selected.value = ''
  fitPending = true
  update()
}
function update() {
  if (!graph) return
  const visible = all.filter(n => {
    let parent = parents.get(n.id)
    while (parent !== undefined) {
      if (collapsed.has(parent)) return false
      parent = parents.get(parent)
    }
    return true
  })
  const ids = new Set(visible.map(n => n.id))
  graph.graphData({
    nodes: visible.map(n => ({ id: n.id, label: n.label, color: n.color, depth: n.depth, count: n.children.length, fx: n.fx, fy: n.fy, fz: n.fz, x: n.fx, y: n.fy, z: n.fz })),
    links: visible.filter(n => parents.has(n.id) && ids.has(parents.get(n.id))).map(n => ({ source: parents.get(n.id), target: n.id, color: n.color })),
  })
}
function focus(node) {
  selected.value = node.label
  const ids = new Set()
  function expand(n) {
    ids.add(n.id)
    collapsed.delete(n.id)
    n.children.forEach(expand)
  }
  expand(all.find(n => n.id === node.id))
  update()
  requestAnimationFrame(() => graph?.zoomToFit(duration, 100, n => ids.has(n.id)))
}
function collapseSelected() {
  const node = all.find(n => n.label === selected.value)
  if (node?.depth > 0) { collapsed.add(node.id); update() }
}
function setNavigation(mode) {
  navigation.value = mode
  if (!graph) return
  const controls = graph.controls()
  controls.mouseButtons.LEFT = mode === 'pan' ? mouseButtons.PAN : mouseButtons.ROTATE
  controls.touches.ONE = mode === 'pan' ? 1 : 0
}
function zoom(factor) {
  if (!graph) return
  const camera = graph.camera()
  const target = graph.controls().target
  const offset = camera.position.clone().sub(target).multiplyScalar(factor)
  graph.cameraPosition({ x: target.x + offset.x, y: target.y + offset.y, z: target.z + offset.z }, target, duration)
}
function resetView() {
  graph?.cameraPosition({ x: 160, y: 100, z: 700 }, { x: 0, y: 0, z: 0 }, 0)
  fit()
}
function fit() { graph?.zoomToFit(duration, 70) }
function theme() {
  const dark = document.documentElement.dataset.theme === 'dark'
  graph?.backgroundColor(dark ? '#171b24' : '#f5f7fb')
}
watch(() => props.source, overview)
onMounted(async () => {
  try {
    const [module, sprites, three] = await Promise.all([import('3d-force-graph'), import('three-spritetext'), import('three')])
    mouseButtons = three.MOUSE
    if (disposed) return
    SpriteText = sprites.default
    const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches
    duration = reduced ? 0 : 700
    graph = new module.default(host.value, { controlType: 'orbit' })
      .showNavInfo(false)
      .nodeId('id')
      .nodeLabel(n => `${n.label}${n.count ? ' — click to expand and focus' : ''}`)
      .nodeThreeObject(n => {
        const label = new SpriteText(`${n.label}${n.count ? (collapsed.has(n.id) ? '  +' : '  −') : ''}`)
        label.color = n.color
        label.textHeight = n.depth === 0 ? 15 : n.depth === 1 ? 11 : 8
        label.backgroundColor = document.documentElement.dataset.theme === 'dark' ? '#202634' : '#ffffff'
        label.padding = 3
        label.borderRadius = 3
        return label
      })
      .linkColor(l => l.color)
      .linkOpacity(0.45)
      .linkWidth(1)
      .enableNodeDrag(false)
      .onNodeClick(focus)
      .cooldownTicks(0)
      .onEngineStop(() => { if (fitPending) { fitPending = false; fit() } })
    setNavigation('pan')
    graph.controls().minDistance = 60
    graph.controls().maxDistance = 6000
    graph.d3Force('charge').strength(0)
    graph.d3Force('link').distance(l => l.target.depth === 1 ? 160 : 90)
    observer = new ResizeObserver(() => {
      graph.width(host.value.clientWidth).height(host.value.clientHeight)
    })
    observer.observe(host.value)
    themeObserver = new MutationObserver(() => { theme(); update() })
    themeObserver.observe(document.documentElement, { attributes: true, attributeFilter: ['data-theme'] })
    theme()
    overview()
    requestAnimationFrame(resetView)
    ready.value = true
  } catch (err) {
    error.value = 'The 3D view could not load. Your outline is available below.'
    console.error(err)
  }
})
onBeforeUnmount(() => {
  disposed = true
  observer?.disconnect()
  themeObserver?.disconnect()
  graph?._destructor()
})
</script>

<template>
  <section class="thought-map" aria-label="Physics concept network">
    <div class="map-toolbar">
      <span>Drag to move · scroll or pinch to zoom · click a topic to focus</span>
      <div class="map-controls">
        <button :disabled="!ready" :aria-pressed="navigation === 'pan'" @click="setNavigation('pan')">Pan</button>
        <button :disabled="!ready" :aria-pressed="navigation === 'rotate'" @click="setNavigation('rotate')">Rotate</button>
        <button :disabled="!ready" aria-label="Zoom in" @click="zoom(.8)">+</button>
        <button :disabled="!ready" aria-label="Zoom out" @click="zoom(1.25)">−</button>
        <button :disabled="!ready" @click="overview">Overview</button>
        <button :disabled="!ready" @click="fit">Fit all</button>
        <button :disabled="!ready" @click="resetView">Reset view</button>
      </div>
    </div>
    <nav class="map-topics" aria-label="Jump to topic">
      <button v-for="topic in topics" :key="topic.id" :disabled="!ready" @click="focus(topic)">{{ topic.label }}</button>
    </nav>
    <p v-if="error" role="alert">{{ error }}</p>
    <p v-else-if="!ready" class="map-status" role="status">Loading 3D mindmap…</p>
    <div ref="host" class="map-viewport" aria-label="Interactive 3D mindmap" />
    <div class="map-footer" aria-live="polite">{{ selected || 'Select a topic to reveal its connections.' }} <button v-if="selected" @click="collapseSelected">Collapse branch</button></div>
    <details class="map-outline">
      <summary>Text outline</summary>
      <pre>{{ source }}</pre>
    </details>
  </section>
</template>

<style scoped>
.thought-map { border: 1px solid var(--vp-c-border); border-radius: 12px; overflow: hidden; margin: 1.5rem 0; }
.map-toolbar { display: flex; align-items: center; justify-content: space-between; gap: 1rem; padding: .8rem 1rem; border-bottom: 1px solid var(--vp-c-border); flex-wrap: wrap; }
.map-toolbar > span { font-size: .85rem; color: var(--vp-c-text-mute); }
.map-controls { display: flex; gap: .5rem; flex-wrap: wrap; }
.map-topics { display: flex; gap: .5rem; padding: .75rem 1rem; flex-wrap: wrap; }
.map-topics button, .map-footer button { border: 1px solid var(--vp-c-border); border-radius: 6px; padding: .35rem .6rem; background: var(--vp-c-bg); color: var(--vp-c-text); cursor: pointer; }
.map-controls button[aria-pressed="true"] { border-color: var(--vp-c-accent); background: var(--vp-c-bg-alt); }
.map-controls button { padding: .35rem .65rem; border: 1px solid var(--vp-c-border); border-radius: 6px; background: var(--vp-c-bg); color: var(--vp-c-text); cursor: pointer; font: inherit; }
.map-controls button:hover { border-color: var(--vp-c-accent); }
.map-controls button:disabled { opacity: .5; cursor: default; }
.map-viewport { height: max(460px, calc(100dvh - 270px)); width: 100%; }
.map-footer, .map-status, .map-outline { padding: .75rem 1rem; font-size: .85rem; }
.map-footer { border-top: 1px solid var(--vp-c-border); }
.map-outline pre { overflow: auto; max-height: 24rem; }
</style>
