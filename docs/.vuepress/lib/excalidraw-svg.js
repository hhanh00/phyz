// Minimal Excalidraw scene → SVG renderer.
// Runs in Node (build/dev time), no DOM, no dependencies.
// Understands the .excalidraw JSON file format for the element types a
// physics site actually uses: ellipses, rectangles, diamonds, lines,
// arrows (triangle/bar/circle heads), freedraw strokes, and text —
// including rotation, dashed strokes, fill style, and opacity.
// Unknown element types (images, embeds, …) are skipped silently.

const FONT_FAMILIES = {
  1: "'Segoe Print', 'Comic Sans MS', cursive",
  2: 'Helvetica, Arial, sans-serif',
  3: "ui-monospace, 'Cascadia Code', Menlo, monospace",
}

const round = (n) => Math.round(n * 100) / 100

const esc = (s) =>
  String(s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')

// Stroke/fill/transform attributes shared by all shapes.
function commonAttrs(el, fill, fillOpacity) {
  const attrs = []
  if (el.angle) {
    const deg = (el.angle * 180) / Math.PI
    const cx = el.x + el.width / 2
    const cy = el.y + el.height / 2
    attrs.push(`transform="rotate(${round(deg)} ${round(cx)} ${round(cy)})"`)
  }
  attrs.push(`stroke="${esc(el.strokeColor || '#1e1e1e')}"`)
  attrs.push(`stroke-width="${el.strokeWidth ?? 1}"`)
  if (el.strokeStyle === 'dashed') attrs.push('stroke-dasharray="8 6"')
  if (el.strokeStyle === 'dotted') attrs.push('stroke-dasharray="2 4"')
  const opacity = (el.opacity ?? 100) / 100
  if (opacity < 1) attrs.push(`opacity="${round(opacity)}"`)
  if (fill) {
    attrs.push(`fill="${esc(fill)}"`)
    if (fillOpacity) attrs.push(`fill-opacity="${fillOpacity}"`)
  } else {
    attrs.push('fill="none"')
  }
  return attrs.join(' ')
}

// 'hachure' / 'cross-hatch' fills get a subtle tint instead of the sketchy
// hatch pattern; 'solid' gets a solid fill.
function shapeFill(el) {
  const bg = el.backgroundColor
  if (!bg || bg === 'transparent') return null
  if (el.fillStyle === 'solid') return { color: bg }
  return { color: bg, opacity: 0.2 }
}

function renderEllipse(el) {
  const fill = shapeFill(el)
  return `<ellipse cx="${round(el.x + el.width / 2)}" cy="${round(el.y + el.height / 2)}" ` +
    `rx="${round(el.width / 2)}" ry="${round(el.height / 2)}" ` +
    `${commonAttrs(el, fill?.color, fill?.opacity)}/>`
}

function renderRectangle(el) {
  const fill = shapeFill(el)
  const rx = Math.min(el.roundness?.radius ?? 0, el.width / 2, el.height / 2)
  return `<rect x="${round(el.x)}" y="${round(el.y)}" width="${round(el.width)}" height="${round(el.height)}" ` +
    (rx ? `rx="${round(rx)}" ry="${round(rx)}" ` : '') +
    `${commonAttrs(el, fill?.color, fill?.opacity)}/>`
}

function renderDiamond(el) {
  const fill = shapeFill(el)
  const cx = el.x + el.width / 2
  const cy = el.y + el.height / 2
  const pts = [
    [cx, el.y],
    [el.x + el.width, cy],
    [cx, el.y + el.height],
    [el.x, cy],
  ].map(([x, y]) => `${round(x)},${round(y)}`).join(' ')
  return `<polygon points="${pts}" ${commonAttrs(el, fill?.color, fill?.opacity)}/>`
}

function renderLinear(el) {
  const pts = (el.points || []).map(([px, py]) => [el.x + px, el.y + py])
  if (pts.length < 2) return ''
  const d = `M ${round(pts[0][0])} ${round(pts[0][1])} ` +
    pts.slice(1).map(([x, y]) => `L ${round(x)} ${round(y)}`).join(' ')
  const color = el.strokeColor || '#1e1e1e'
  const head =
    el.type === 'arrow' && el.endArrowhead ? arrowhead(pts.at(-1), pts.at(-2), color, el.strokeWidth ?? 1) : ''
  const tail =
    el.type === 'arrow' && el.startArrowhead ? arrowhead(pts[0], pts[1], color, el.strokeWidth ?? 1, true) : ''
  return `<path d="${d}" ${commonAttrs(el)}/>${head}${tail}`
}

function arrowhead(tip, prev, color, sw, reverse = false) {
  const angle = Math.atan2(tip[1] - prev[1], tip[0] - prev[0]) + (reverse ? Math.PI : 0)
  const len = Math.max(12, sw * 3.2)
  const base = [tip[0] - len * Math.cos(angle), tip[1] - len * Math.sin(angle)]
  const a = [base[0] + len * 0.45 * Math.sin(angle), base[1] - len * 0.45 * Math.cos(angle)]
  const b = [base[0] - len * 0.45 * Math.sin(angle), base[1] + len * 0.45 * Math.cos(angle)]
  const pts = [tip, a, b].map(([x, y]) => `${round(x)},${round(y)}`).join(' ')
  return `<polygon points="${pts}" fill="${esc(color)}" stroke="${esc(color)}" stroke-width="1"/>`
}

function renderFreedraw(el) {
  const pts = (el.points || []).map(([px, py]) => [el.x + px, el.y + py])
  if (pts.length < 2) return ''
  return `<polyline points="${pts.map(([x, y]) => `${round(x)},${round(y)}`).join(' ')}" ${commonAttrs(el)}/>`
}

function renderText(el) {
  const fontSize = el.fontSize || 20
  const lines = String(el.text ?? '').split('\n')
  const lineHeight = fontSize * (el.lineHeight || 1.25)
  const totalH = lineHeight * (lines.length - 1)
  let startY
  if (el.verticalAlign === 'middle') startY = el.y + el.height / 2 - totalH / 2
  else if (el.verticalAlign === 'bottom') startY = el.y + el.height - lineHeight * (lines.length - 1)
  else startY = el.y
  const anchor =
    el.textAlign === 'left' ? 'start' : el.textAlign === 'right' ? 'end' : 'middle'
  const x =
    el.textAlign === 'left'
      ? el.x
      : el.textAlign === 'right'
        ? el.x + el.width
        : el.x + el.width / 2
  const tspans = lines
    .map((line, i) => {
      const dy = i === 0 ? 0 : lineHeight
      const tspan = `<tspan x="${round(x)}" dy="${round(dy)}">${esc(line)}</tspan>`
      return i === 0 ? esc(line) : tspan
    })
    .join('')
  const attrs = []
  if (el.angle) {
    const deg = (el.angle * 180) / Math.PI
    const cx = el.x + el.width / 2
    const cy = el.y + el.height / 2
    attrs.push(`transform="rotate(${round(deg)} ${round(cx)} ${round(cy)})"`)
  }
  attrs.push(
    `x="${round(x)}" y="${round(startY + fontSize * 0.8)}"`,
    `font-size="${fontSize}"`,
    `font-family="${FONT_FAMILIES[el.fontFamily || 1]}"`,
    `text-anchor="${anchor}"`,
    `fill="${esc(el.strokeColor || '#1e1e1e')}"`,
  )
  if ((el.opacity ?? 100) < 100) attrs.push(`opacity="${round(el.opacity / 100)}"`)
  return `<text ${attrs.join(' ')}>${tspans}</text>`
}

function renderElement(el) {
  switch (el.type) {
    case 'ellipse':
      return renderEllipse(el)
    case 'rectangle':
      return renderRectangle(el)
    case 'diamond':
      return renderDiamond(el)
    case 'line':
    case 'arrow':
      return renderLinear(el)
    case 'freedraw':
      return renderFreedraw(el)
    case 'text':
      return renderText(el)
    default:
      return '' // image, embed, frame, … — skipped
  }
}

// Scene JSON (the "Export → file" format) → self-contained SVG fragment.
export function renderExcalidrawSvg(sceneJson) {
  let scene
  try {
    scene = JSON.parse(sceneJson)
  } catch {
    return '<!-- invalid excalidraw scene JSON -->'
  }
  const elements = (scene.elements || []).filter((el) => !el.isDeleted)
  if (elements.length === 0) return '<!-- empty excalidraw scene -->'

  let minX = Infinity,
    minY = Infinity,
    maxX = -Infinity,
    maxY = -Infinity
  for (const el of elements) {
    if (el.type === 'line' || el.type === 'arrow' || el.type === 'freedraw') {
      // linear elements carry their extent in `points`, not width/height
      for (const [px, py] of el.points || []) {
        minX = Math.min(minX, el.x + px)
        minY = Math.min(minY, el.y + py)
        maxX = Math.max(maxX, el.x + px)
        maxY = Math.max(maxY, el.y + py)
      }
    } else {
      minX = Math.min(minX, el.x)
      minY = Math.min(minY, el.y)
      maxX = Math.max(maxX, el.x + (el.width || 0))
      maxY = Math.max(maxY, el.y + (el.height || 0))
    }
  }
  const pad = 40
  minX -= pad
  minY -= pad
  maxX += pad
  maxY += pad
  const w = maxX - minX
  const h = maxY - minY

  const bg = scene.appState?.viewBackgroundColor
  const bgRect =
    bg && bg !== 'transparent'
      ? `<rect x="${round(minX)}" y="${round(minY)}" width="${round(w)}" height="${round(h)}" fill="${esc(bg)}"/>`
      : ''
  const body = elements.map(renderElement).join('\n')

  return (
    `<div class="excalidraw-diagram">` +
    `<svg viewBox="${round(minX)} ${round(minY)} ${round(w)} ${round(h)}" ` +
    `xmlns="http://www.w3.org/2000/svg" role="img" ` +
    `style="max-width:100%;height:auto;display:block;margin:1.5rem auto;background:${bg ? esc(bg) : '#ffffff'}">` +
    `${bgRect}\n${body}</svg></div>`
  )
}
