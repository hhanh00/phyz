// Dev server only: stores the replies given on a page's review notes.
// The notes (see review-jump.js) post each reply to /__review-replies, and this plugin keeps
// them in updates/review-replies.json, keyed by page and item:
//   { "dirac-equation": { "P25": { "choice": "accept", "text": "", "at": "2026-11-27T10:00:00Z" } } }
// choice is "unresolved", "accept" or "other"; text is what was typed beside "other".
// The plugin applies to `vuepress dev` only, so a production build never includes it.
import fs from 'node:fs'
import path from 'node:path'

const FILE = path.resolve(process.cwd(), 'updates/review-replies.json')

const load = () => {
  try {
    return JSON.parse(fs.readFileSync(FILE, 'utf8'))
  } catch {
    return {}
  }
}

export function reviewReplies() {
  return {
    name: 'phyz-review-replies',
    apply: 'serve',
    configureServer(server) {
      server.middlewares.use('/__review-replies', (req, res) => {
        res.setHeader('Content-Type', 'application/json')
        if (req.method === 'GET') {
          res.end(JSON.stringify(load()))
          return
        }
        if (req.method !== 'POST') {
          res.statusCode = 405
          res.end('{}')
          return
        }
        let body = ''
        req.on('data', (c) => {
          body += c
          if (body.length > 20000) req.destroy()
        })
        req.on('end', () => {
          try {
            const { page, id, choice, text } = JSON.parse(body)
            const ok =
              /^[a-z0-9-]+$/.test(page) && /^[A-Z]+\d+$/.test(id) && ['unresolved', 'accept', 'other'].includes(choice)
            if (!ok) throw new Error('bad reply')
            const all = load()
            all[page] = all[page] || {}
            all[page][id] = { choice, text: String(text || '').slice(0, 4000), at: new Date().toISOString() }
            fs.writeFileSync(FILE, JSON.stringify(all, null, 1) + '\n')
            res.end(JSON.stringify(all))
          } catch {
            res.statusCode = 400
            res.end('{}')
          }
        })
      })
    },
  }
}
