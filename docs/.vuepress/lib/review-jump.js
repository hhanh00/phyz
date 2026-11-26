// Review jumps, for the dev server only.
// A link like /page.html?rev=M2 scrolls to the temporary anchor <a id="rev-M2"></a> in that page,
// opening the collapsible box around it if there is one. It repeats the scroll for a few seconds,
// because formulas and figures change the page's height after it first appears.
// Every review anchor also gets a yellow badge with its ID, so the place is easy to see.
export function setupReviewJumps(router) {
  if (typeof window === 'undefined') return
  const badge = () => {
    document.querySelectorAll('a[id^="rev-"]').forEach((a) => {
      if (a.dataset.rev) return
      a.dataset.rev = '1'
      a.textContent = a.id.slice(4)
      a.style.cssText =
        'background:#ffd54a;color:#172b4d;font:600 12px/1.6 sans-serif;padding:1px 6px;' +
        'border-radius:4px;margin-right:6px;text-decoration:none;'
    })
  }
  const jump = () => {
    const id = new URLSearchParams(window.location.search).get('rev')
    let n = 0
    const tick = () => {
      badge()
      if (id) {
        const el = document.getElementById('rev-' + id)
        if (el) {
          const box = el.closest('details')
          if (box) box.open = true
          el.scrollIntoView({ block: 'center' })
        }
      }
      if (++n < 8) setTimeout(tick, 400)
    }
    tick()
  }
  router.afterEach(() => setTimeout(jump, 50))
  setInterval(badge, 1500)
}
