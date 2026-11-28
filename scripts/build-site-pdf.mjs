import { createServer } from 'node:http'
import { spawn } from 'node:child_process'
import {
  access,
  cp,
  mkdir,
  open,
  readFile,
  readdir,
  rm,
  stat,
  writeFile,
} from 'node:fs/promises'
import { constants } from 'node:fs'
import { dirname, extname, join, relative, resolve, sep } from 'node:path'
import { fileURLToPath } from 'node:url'

const scriptDir = dirname(fileURLToPath(import.meta.url))
const projectDir = resolve(scriptDir, '..')
const docsDir = join(projectDir, 'docs')
const workDir = join(projectDir, 'tmp', 'pdfs', 'whole-site')
const printDocsDir = join(workDir, 'docs')
const distDir = join(workDir, 'dist')
const chromeProfileDir = join(workDir, 'chrome-profile')
const outputDir = join(projectDir, 'output', 'pdf')
const outputPath = join(outputDir, 'phyz-complete.pdf')

// Keep this order aligned with the site's intended reading order. The optional
// Yang-Mills derivation and math appendices are included so the PDF is complete.
const chapters = [
  ['Classical Mechanics', 'classical-mechanics.md'],
  ['First Quantization', 'first-quantization.md'],
  ['Harmonic Oscillator', 'harmonic-oscillator.md'],
  ['Special Relativity', 'special-relativity.md'],
  ['Relativistic Quantum Mechanics', 'relativistic-qm.md'],
  ['The Dirac Equation', 'dirac-equation.md'],
  ['Fields and Quanta', 'qft.md'],
  ['Action and Lagrangians', 'qft-action.md'],
  ['Field Quantization', 'field-quantization.md'],
  ['Quantum Electrodynamics', 'qed.md'],
  ['From Lagrangian to Experiment', 'lagrangian-to-experiment.md'],
  ['Perturbation Theory', 'perturbation-theory.md'],
  ['Feynman Rules for QED', 'feynman-rules.md'],
  ['Symmetries', 'symmetries.md'],
  ['Weak Interaction', 'weak-interaction.md'],
  ['Yang-Mills Fields', 'yang-mills.md'],
  ['Electroweak Unification', 'electroweak-unification.md'],
  ['Higgs Mechanism', 'higgs-mechanism.md'],
  ['Quantum Chromodynamics', 'qcd.md'],
  ['The Standard Model', 'standard-model.md'],
  ['Path Integrals in Quantum Mechanics', 'path-integrals.md'],
  ['Path Integrals for Fields', 'path-integrals-fields.md'],
  ['Fermionic Path Integrals', 'path-integrals-fermions.md'],
  ['Gauge Fixing', 'path-integrals-gauge-fixing.md'],
  ['Renormalization at One Loop', 'path-integrals-renormalization.md'],
  ['Final Recap', 'recap.md'],
  ['Calculus', 'appendix-math-calculus.md'],
  ['Complex Numbers', 'appendix-math-complex.md'],
  ['Linear Algebra', 'appendix-math-linear-algebra.md'],
  ['Index Notation and Tensors', 'appendix-math-tensors.md'],
  ['Groups and Symmetry', 'appendix-math-groups.md'],
]

function slugFor(filename) {
  return filename.replace(/\.md$/, '')
}

function stripFrontmatter(markdown) {
  return markdown.replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n/, '')
}

function namespaceFootnotes(markdown, namespace) {
  return markdown.replace(/\[\^([^\]]+)\]/g, `[^${namespace}-$1]`)
}

async function createPrintMarkdown() {
  const contents = [
    '---',
    'title: Phyz - Complete Notes',
    'pageClass: print-book',
    'navbar: false',
    'sidebar: false',
    'contributors: false',
    'editLink: false',
    'lastUpdated: false',
    'prev: false',
    'next: false',
    '---',
    '',
    '<div class="pdf-title-page">',
    '',
    '# Phyz',
    '',
    'A connected path from classical mechanics to the Standard Model',
    '',
    '</div>',
    '',
    '# Contents',
    '',
    ...chapters.map(([title, filename], index) =>
      `${index + 1}. [${title}](#chapter-${slugFor(filename)})`
    ),
    '',
  ]

  for (const [, filename] of chapters) {
    const slug = slugFor(filename)
    const source = await readFile(join(docsDir, filename), 'utf8')
    const markdown = namespaceFootnotes(stripFrontmatter(source), slug)
    contents.push(
      '<div class="pdf-chapter-break"></div>',
      '',
      `<a id="chapter-${slug}"></a>`,
      '',
      markdown.trim(),
      '',
    )
  }

  await writeFile(join(printDocsDir, 'print.md'), `${contents.join('\n')}\n`)
}

async function verifyChapterList() {
  const markdownFiles = (await readdir(docsDir))
    .filter((filename) => filename.endsWith('.md') && filename !== 'README.md')
  const configuredFiles = chapters.map(([, filename]) => filename)
  const configuredSet = new Set(configuredFiles)
  const missing = markdownFiles.filter((filename) => !configuredSet.has(filename))
  const duplicates = configuredFiles.filter(
    (filename, index) => configuredFiles.indexOf(filename) !== index,
  )

  if (missing.length || duplicates.length || markdownFiles.length !== configuredSet.size) {
    throw new Error([
      missing.length ? `Missing chapters: ${missing.join(', ')}` : '',
      duplicates.length ? `Duplicate chapters: ${[...new Set(duplicates)].join(', ')}` : '',
    ].filter(Boolean).join('\n'))
  }
}

async function commandExists(path) {
  try {
    await access(path, constants.X_OK)
    return true
  } catch {
    return false
  }
}

async function findChrome() {
  const configured = process.env.CHROME_PATH
  const candidates = [
    configured,
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge',
    '/usr/bin/google-chrome',
    '/usr/bin/chromium',
    '/usr/bin/chromium-browser',
  ].filter(Boolean)

  for (const candidate of candidates) {
    if (await commandExists(candidate)) return candidate
  }

  throw new Error('Chrome or Chromium was not found. Set CHROME_PATH to its executable.')
}

function run(command, args, options = {}) {
  return new Promise((resolvePromise, rejectPromise) => {
    const child = spawn(command, args, {
      cwd: projectDir,
      stdio: 'inherit',
      ...options,
    })
    child.once('error', rejectPromise)
    child.once('exit', (code, signal) => {
      if (code === 0) resolvePromise()
      else rejectPromise(new Error(`${command} exited with ${code ?? signal}`))
    })
  })
}

function wait(milliseconds) {
  return new Promise((resolvePromise) => setTimeout(resolvePromise, milliseconds))
}

async function connectDevTools(webSocketUrl) {
  const socket = new WebSocket(webSocketUrl)
  await new Promise((resolvePromise, rejectPromise) => {
    socket.addEventListener('open', resolvePromise, { once: true })
    socket.addEventListener('error', rejectPromise, { once: true })
  })

  let nextId = 1
  const pending = new Map()
  const listeners = new Map()

  socket.addEventListener('message', async (event) => {
    const raw = typeof event.data === 'string' ? event.data : await event.data.text()
    const message = JSON.parse(raw)
    if (message.id) {
      const request = pending.get(message.id)
      if (!request) return
      pending.delete(message.id)
      if (message.error) request.reject(new Error(message.error.message))
      else request.resolve(message.result)
      return
    }

    for (const listener of listeners.get(message.method) ?? []) {
      listener(message.params)
    }
  })

  function send(method, params = {}) {
    return new Promise((resolvePromise, rejectPromise) => {
      const id = nextId++
      pending.set(id, { resolve: resolvePromise, reject: rejectPromise })
      socket.send(JSON.stringify({ id, method, params }))
    })
  }

  function once(method) {
    return new Promise((resolvePromise) => {
      const listener = (params) => {
        listeners.get(method)?.delete(listener)
        resolvePromise(params)
      }
      if (!listeners.has(method)) listeners.set(method, new Set())
      listeners.get(method).add(listener)
    })
  }

  return { send, once, close: () => socket.close() }
}

async function launchChrome(chrome) {
  const child = spawn(chrome, [
    '--headless=new',
    '--disable-gpu',
    '--disable-extensions',
    '--hide-scrollbars',
    '--remote-debugging-port=0',
    `--user-data-dir=${chromeProfileDir}`,
    'about:blank',
  ], {
    cwd: projectDir,
    stdio: ['ignore', 'ignore', 'pipe'],
  })

  child.stderr.on('data', (chunk) => {
    const message = chunk.toString()
    if (!message.includes('CVDisplayLinkCreateWithCGDisplay')) process.stderr.write(message)
  })

  const portFile = join(chromeProfileDir, 'DevToolsActivePort')
  for (let attempt = 0; attempt < 100; attempt += 1) {
    try {
      const [port] = (await readFile(portFile, 'utf8')).trim().split('\n')
      return { child, port: Number(port) }
    } catch {
      if (child.exitCode !== null) throw new Error(`Chrome exited with ${child.exitCode}`)
      await wait(100)
    }
  }

  child.kill()
  throw new Error('Timed out while starting Chrome.')
}

async function printWithChrome(chrome, url) {
  await rm(chromeProfileDir, { recursive: true, force: true })
  const { child, port } = await launchChrome(chrome)

  try {
    const targets = await fetch(`http://127.0.0.1:${port}/json/list`).then((response) => response.json())
    const page = targets.find((target) => target.type === 'page')
    if (!page?.webSocketDebuggerUrl) throw new Error('Chrome did not expose a printable page.')

    const devtools = await connectDevTools(page.webSocketDebuggerUrl)
    try {
      await devtools.send('Page.enable')
      const loaded = devtools.once('Page.loadEventFired')
      await devtools.send('Page.navigate', { url })
      await loaded

      const readiness = await devtools.send('Runtime.evaluate', {
        expression: `(async () => {
          await document.fonts.ready;
          await Promise.all([...document.images].map((image) => image.complete
            ? Promise.resolve()
            : new Promise((resolve) => {
                image.addEventListener('load', resolve, { once: true });
                image.addEventListener('error', resolve, { once: true });
              })));
          await new Promise((resolve) => requestAnimationFrame(() => requestAnimationFrame(resolve)));
          return {
            textLength: document.body.innerText.length,
            height: document.documentElement.scrollHeight,
          };
        })()`,
        awaitPromise: true,
        returnByValue: true,
      })

      const dimensions = readiness.result?.value
      if (!dimensions || dimensions.textLength < 100000 || dimensions.height < 10000) {
        throw new Error(`The print page did not render completely: ${JSON.stringify(dimensions)}`)
      }
      console.log(`Print page ready (${dimensions.textLength.toLocaleString()} characters).`)

      const printed = await devtools.send('Page.printToPDF', {
        displayHeaderFooter: true,
        headerTemplate: '<div></div>',
        footerTemplate: '<div style="box-sizing:border-box;width:100%;padding:0 15mm;color:#777;font:8px sans-serif;text-align:center"><span class="pageNumber"></span> / <span class="totalPages"></span></div>',
        printBackground: true,
        preferCSSPageSize: true,
        generateTaggedPDF: true,
        generateDocumentOutline: true,
        transferMode: 'ReturnAsStream',
      })

      const output = await open(outputPath, 'w')
      try {
        while (true) {
          const chunk = await devtools.send('IO.read', {
            handle: printed.stream,
            size: 1024 * 1024,
          })
          await output.write(Buffer.from(chunk.data, chunk.base64Encoded ? 'base64' : 'utf8'))
          if (chunk.eof) break
        }
      } finally {
        await output.close()
        await devtools.send('IO.close', { handle: printed.stream })
      }
    } finally {
      devtools.close()
    }
  } finally {
    child.kill()
    await new Promise((resolvePromise) => {
      if (child.exitCode !== null) resolvePromise()
      else child.once('exit', resolvePromise)
    })
  }
}

function contentType(pathname) {
  return {
    '.css': 'text/css; charset=utf-8',
    '.html': 'text/html; charset=utf-8',
    '.js': 'text/javascript; charset=utf-8',
    '.json': 'application/json; charset=utf-8',
    '.png': 'image/png',
    '.svg': 'image/svg+xml',
    '.woff': 'font/woff',
    '.woff2': 'font/woff2',
  }[extname(pathname)] ?? 'application/octet-stream'
}

async function startServer() {
  const server = createServer(async (request, response) => {
    try {
      const url = new URL(request.url ?? '/', 'http://127.0.0.1')
      let pathname = decodeURIComponent(url.pathname)
      if (pathname.endsWith('/')) pathname += 'index.html'

      const requestedPath = resolve(distDir, `.${pathname}`)
      const rel = relative(distDir, requestedPath)
      if (rel.startsWith(`..${sep}`) || rel === '..') {
        response.writeHead(403).end('Forbidden')
        return
      }

      const fileStat = await stat(requestedPath)
      const filePath = fileStat.isDirectory()
        ? join(requestedPath, 'index.html')
        : requestedPath
      const body = await readFile(filePath)
      response.writeHead(200, { 'Content-Type': contentType(filePath) })
      response.end(body)
    } catch {
      response.writeHead(404).end('Not found')
    }
  })

  await new Promise((resolvePromise, rejectPromise) => {
    server.once('error', rejectPromise)
    server.listen(0, '127.0.0.1', resolvePromise)
  })

  return server
}

async function main() {
  console.log('Preparing the complete print edition...')
  await verifyChapterList()
  await rm(workDir, { recursive: true, force: true })
  await mkdir(printDocsDir, { recursive: true })
  await mkdir(outputDir, { recursive: true })

  await cp(docsDir, printDocsDir, {
    recursive: true,
    filter: (source) => {
      const rel = relative(docsDir, source)
      return !['.vuepress/.cache', '.vuepress/.temp', '.vuepress/dist'].some(
        (excluded) => rel === excluded || rel.startsWith(`${excluded}${sep}`),
      )
    },
  })
  await createPrintMarkdown()

  console.log('Building the print edition with VuePress...')
  await run('pnpm', ['exec', 'vuepress', 'build', printDocsDir, '--dest', distDir])

  const chrome = await findChrome()
  const server = await startServer()
  const address = server.address()
  const port = typeof address === 'object' && address ? address.port : null
  if (!port) throw new Error('Could not determine the temporary web server port.')

  console.log('Printing the complete site to PDF...')
  try {
    await printWithChrome(chrome, `http://127.0.0.1:${port}/print.html`)
  } finally {
    await new Promise((resolvePromise) => server.close(resolvePromise))
  }

  const result = await stat(outputPath)
  if (result.size < 100 * 1024) throw new Error('Chrome created an unexpectedly small PDF.')
  console.log(`Created ${relative(projectDir, outputPath)} (${Math.ceil(result.size / 1024)} KiB)`)
  await rm(workDir, { recursive: true, force: true })
}

main().catch((error) => {
  console.error(error instanceof Error ? error.message : error)
  process.exitCode = 1
})
