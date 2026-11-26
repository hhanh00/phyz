"""Rebuild the temporary review anchors in a page and the Jump lines in its tracking file.

Usage: python3 updates/refresh_links.py
Removes every <a id="rev-..."></a> from the page, then, for each open item in the
tracking file ("#### ID ..." blocks with "- Jump: ... search text: `...`" lines),
finds the line by its search text, puts an anchor rev-ID (rev-ID-b, ...) at its start
and rewrites the line number in the Jump line. Run with --strip to only remove anchors.
"""
import re, sys
PAGE = 'docs/relativistic-qm.md'
TRACK = 'updates/05-relativistic-qm.md'
BASE = 'http://localhost:8080/relativistic-qm.html'
page = [re.sub(r'<a id="rev-[^"]*"></a>', '', l) for l in open(PAGE).read().split('\n')]
if '--strip' not in sys.argv:
    pat = re.compile(r'^- Jump: \[rendered page\]\([^)]*\) · \[source, line \d+\]\([^)]*\) · search text: `(.*?)`(.*)$')
    out, cur, count, prefix = [], None, {}, {}
    for l in open(TRACK).read().split('\n'):
        h = re.match(r'^#### (\S+)', l)
        if h:
            cur = h.group(1); count[cur] = 0
        m = pat.match(l)
        if m and cur:
            needle, rest = m.group(1), m.group(2)
            hits = [i for i, x in enumerate(page) if needle in x]
            if len(hits) != 1:
                sys.exit(f'{cur}: search text matches {len(hits)} lines: {needle}')
            i = hits[0]; k = count[cur]; count[cur] += 1
            aid = f'rev-{cur}' + ('' if k == 0 else '-' + 'bcdefgh'[k - 1])
            prefix.setdefault(i, []).append(aid)
            l = f'- Jump: [rendered page]({BASE}?rev={aid[4:]}) · [source, line {i + 1}](../{PAGE}#L{i + 1}) · search text: `{needle}`{rest}'
        out.append(l)
    for i, ids in prefix.items():
        page[i] = ''.join(f'<a id="{a}"></a>' for a in ids) + page[i]
    open(TRACK, 'w').write('\n'.join(out))
    print(sum(len(v) for v in prefix.values()), 'anchors')
open(PAGE, 'w').write('\n'.join(page))
