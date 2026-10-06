const colors = ['#2563eb', '#7c3aed', '#0891b2', '#059669', '#c2410c', '#be185d', '#4f46e5', '#a16207', '#0f766e']

export function layoutMindmap(source, collapsed = new Set()) {
  const nodes = []
  const stack = []
  for (const line of source.split('\n')) {
    if (!line.trim() || line.trim() === 'mindmap') continue
    const indent = line.match(/^\s*/)[0].length
    while (stack.length && stack.at(-1).indent >= indent) stack.pop()
    const parent = stack.at(-1)
    const label = line.trim().replace(/^root\(\(([\s\S]*)\)\)$/, '$1').replace(/<br\s*\/?\s*>/gi, ' ')
    const depth = parent ? parent.depth + 1 : 0
    const node = { id: nodes.length, label, indent, depth, children: [], x: 32 + depth * 280, width: 224, height: 56, color: parent?.color ?? '#475569' }
    if (depth === 1) node.color = colors[parent.children.length % colors.length]
    parent?.children.push(node)
    nodes.push(node)
    stack.push(node)
  }
  if (!nodes.length) return { nodes: [], links: [], width: 800, height: 400 }
  const visible = []
  function collect(node) {
    visible.push(node)
    node.childCount = node.children.length
    node.collapsed = collapsed.has(node.id)
    if (node.collapsed) node.children = []
    node.children.forEach(collect)
  }
  collect(nodes[0])
  let cursor = 32
  function place(node) {
    if (!node.children.length) {
      node.y = cursor
      cursor += 76
    } else {
      node.children.forEach(place)
      node.y = (node.children[0].y + node.children.at(-1).y) / 2
      if (node.depth === 1) cursor += 40
    }
  }
  place(nodes[0])
  const links = visible.flatMap(parent => parent.children.map(child => {
    const x = parent.x + parent.width
    const y = parent.y + parent.height / 2
    const cy = child.y + child.height / 2
    const mid = (x + child.x) / 2
    return { id: child.id, color: child.color, path: `M ${x} ${y} C ${mid} ${y}, ${mid} ${cy}, ${child.x} ${cy}` }
  }))
  return { nodes: visible, links, width: Math.max(...visible.map(n => n.x + n.width)) + 32, height: cursor + 32 }
}
