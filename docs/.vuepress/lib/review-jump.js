// Review notes and jumps, for the dev server only.
//
// updates/refresh_links.py puts temporary anchors <a id="rev-P8"></a> in a page and writes
// review-notes.json from the page's tracking file. With that file filled in, this script shows:
//   - a list of every open item at the top of the page, in ascending order;
//   - a yellow note above each paragraph an item concerns;
//   - a yellow badge with the item's ID at the start of that paragraph.
// Each item has three choices: unresolved, accept suggestion, or other with a text box.
// A reply is posted to the dev server, which keeps it in updates/review-replies.json
// (see review-server.js). A link like /page.html?rev=P8-b scrolls to that place, opening the
// collapsible box around it. `--strip` on the script removes the anchors and empties the
// notes file, which is the state to commit.
import notes from './review-notes.json'

const YELLOW = 'background:#fff8e1;border-left:4px solid #ffb300;color:#172b4d;border-radius:4px;'
const CHOICES = [
  ['unresolved', 'Unresolved'],
  ['accept', 'Accept suggestion'],
  ['other', 'Other'],
]

export function setupReviewJumps(router) {
  if (typeof window === 'undefined') return
  const here = () => window.location.pathname.replace(/^.*\//, '').replace(/\.html$/, '')
  const active = () => notes.page === here()
  let replies = {}
  let loaded = false
  let serial = 0
  const reply = (id) => replies[id] || { choice: 'unresolved', text: '' }
  const sync = () => {
    document.querySelectorAll('[data-rev-form]').forEach((f) => {
      const r = reply(f.dataset.revForm)
      f.querySelectorAll('input[type=radio]').forEach((c) => (c.checked = c.value === r.choice))
      const t = f.querySelector('input[type=text]')
      if (t && document.activeElement !== t) t.value = r.text || ''
      const row = f.closest('[data-rev-row]')
      if (row) row.style.borderLeftColor = r.choice === 'unresolved' ? '#ffb300' : '#2e7d32'
    })
    const count = document.getElementById('revpanel-count')
    if (count) {
      const items = notes.items || []
      const n = items.filter((i) => reply(i.id).choice !== 'unresolved').length
      count.textContent = n + ' of ' + items.length + ' answered' + (loaded ? '' : ' (replies not loaded)')
    }
  }
  const fetchReplies = () =>
    fetch('/__review-replies')
      .then((r) => r.json())
      .then((all) => {
        replies = all[notes.page] || {}
        loaded = true
        sync()
      })
      .catch(() => {})
  const send = (id, choice, text) => {
    replies[id] = { choice, text }
    sync()
    fetch('/__review-replies', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ page: notes.page, id, choice, text }),
    }).catch(() => {})
  }
  const text = (tag, css, s) => {
    const e = document.createElement(tag)
    e.style.cssText = css
    e.textContent = s
    return e
  }
  const form = (id) => {
    const f = document.createElement('div')
    f.dataset.revForm = id
    f.style.cssText = 'display:flex;flex-wrap:wrap;align-items:center;gap:4px 14px;margin-top:6px;'
    const group = 'rev-' + id + '-' + ++serial
    const box = document.createElement('input')
    box.type = 'text'
    box.placeholder = 'your reply'
    box.style.cssText = 'flex:1 1 220px;min-width:160px;font:14px/1.4 sans-serif;padding:3px 6px;border:1px solid #c9b46a;border-radius:4px;background:#fff;color:#172b4d;'
    CHOICES.forEach(([value, label]) => {
      const l = document.createElement('label')
      l.style.cssText = 'display:inline-flex;align-items:center;gap:4px;cursor:pointer;white-space:nowrap;'
      const c = document.createElement('input')
      c.type = 'radio'
      c.name = group
      c.value = value
      c.addEventListener('change', () => send(id, value, box.value))
      l.append(c, document.createTextNode(label))
      f.append(l)
    })
    box.addEventListener('input', () => {
      replies[id] = { choice: 'other', text: box.value }
    })
    box.addEventListener('change', () => send(id, 'other', box.value))
    f.append(box)
    return f
  }
  const goTo = (place) => {
    const el = document.getElementById('rev-' + place)
    if (!el) return
    const box = el.closest('details')
    if (box) box.open = true
    el.scrollIntoView({ block: 'center' })
  }
  const describe = (item, place) => {
    const d = document.createElement('div')
    d.style.cssText = 'flex:1;min-width:0;'
    d.append(text('div', 'font-weight:600;', item.id + ' · ' + item.title + (place ? ' (' + place + ')' : '')))
    if (item.finding) d.append(text('div', '', item.finding))
    if (item.suggestion) d.append(text('div', 'margin-top:2px;', 'Suggestion: ' + item.suggestion))
    return d
  }
  const panel = () => {
    if (!active() || document.getElementById('revpanel')) return
    const h1 = document.querySelector('h1')
    if (!h1) return
    const box = document.createElement('div')
    box.id = 'revpanel'
    box.style.cssText = YELLOW + 'font:14px/1.5 sans-serif;padding:10px 14px;margin:16px 0;'
    const top = text('div', 'font-weight:700;margin-bottom:6px;', 'Review items · ')
    const count = text('span', 'font-weight:400;', '')
    count.id = 'revpanel-count'
    top.append(count)
    box.append(top)
    ;(notes.items || []).forEach((item) => {
      const row = document.createElement('div')
      row.dataset.revRow = '1'
      row.style.cssText = 'padding:6px 0 6px 8px;border-top:1px solid #ffe082;border-left:3px solid #ffb300;'
      const body = describe(item)
      if (item.places && item.places.length) {
        const links = text('div', 'margin-top:2px;', 'Go to: ')
        item.places.forEach((p, i) => {
          const a = text('a', 'cursor:pointer;text-decoration:underline;margin-right:10px;', p.place || 'place ' + (i + 1))
          a.addEventListener('click', () => goTo(p.key))
          links.append(a)
        })
        body.append(links)
      }
      body.append(form(item.id))
      row.append(body)
      box.append(row)
    })
    h1.after(box)
    fetchReplies()
  }
  const note = (a) => {
    const place = a.id.slice(4)
    const n = (notes.places || {})[place]
    if (!n || document.getElementById('revnote-' + place)) return
    const item = (notes.items || []).find((i) => i.id === n.id)
    if (!item) return
    const box = document.createElement('div')
    box.id = 'revnote-' + place
    box.dataset.revRow = '1'
    box.style.cssText = YELLOW + 'font:14px/1.5 sans-serif;padding:8px 12px;margin:12px 0 4px;'
    if (n.first) {
      const body = describe(item, n.place)
      body.append(form(item.id))
      box.append(body)
    } else {
      box.append(text('div', 'font-weight:600;', item.id + ', also here: ' + n.place))
    }
    const block = a.closest('p, li, blockquote, figure') || a.parentElement
    block.before(box)
  }
  const badge = () => {
    if (!active()) return
    panel()
    document.querySelectorAll('a[id^="rev-"]').forEach((a) => {
      note(a)
      if (a.dataset.rev) return
      a.dataset.rev = '1'
      a.textContent = a.id.slice(4)
      a.style.cssText =
        'background:#ffd54a;color:#172b4d;font:600 12px/1.6 sans-serif;padding:1px 6px;' +
        'border-radius:4px;margin-right:6px;text-decoration:none;'
    })
    sync()
  }
  const jump = () => {
    const id = new URLSearchParams(window.location.search).get('rev')
    let n = 0
    const tick = () => {
      badge()
      if (id) goTo(id)
      if (++n < 8) setTimeout(tick, 400)
    }
    tick()
  }
  router.afterEach(() => setTimeout(jump, 50))
  setInterval(badge, 1500)
}
