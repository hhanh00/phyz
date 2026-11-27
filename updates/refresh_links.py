"""Rebuild the temporary review anchors in a page, the Jump lines in its tracking file,
and the notes the dev server shows on the page.

Usage: python3 updates/refresh_links.py STEM [--strip]
STEM is the tracking file's name without .md, e.g. 06-dirac-equation: the page is
docs/<STEM without its number>.md. With no STEM it uses chapter 5.

The tracking file holds one block per item:

    #### P8 Restatement inside a section
    - Status: Done
    - Finding: ...            (optional; otherwise the third cell of the table row "| P8 | ...")
    - Suggestion: ...         (optional; what Claude recommends, shown with the choices)
    - Change: ...             (optional; what was done about it)
    - Jump: [rendered page](...) · [source, line N](...) · search text: `...` (which place)

The script removes every <a id="rev-..."></a> from the page. Then, for each Jump line, it
finds the one line of the page that contains the search text, puts an anchor rev-ID
(rev-ID-b, ...) at its start and rewrites the link and the line number in the Jump line.
A search text must not sit on a heading, a list item, a table row or a displayed equation.

It also writes docs/.vuepress/lib/review-notes.json. On the dev server, the page then shows
every block that has a Change line or a Jump line as a list at the top, in ascending order
with three choices each (unresolved, accept suggestion, other with a text box), and as a note above each place. Blocks without a Jump line appear in
the list only. Older blocks with neither line are left out.
So is any block whose Status starts with Done, Kept or Noted: only items that are still
open go on the page.

Replies given on the page are stored by the dev server in updates/review-replies.json.

With --strip it only removes the anchors and empties the notes file. Do that before a commit.
"""
import json, re, sys
STEM = next((a for a in sys.argv[1:] if not a.startswith('--')), '05-relativistic-qm')
NAME = STEM.split('-', 1)[1]
PAGE = f'docs/{NAME}.md'
TRACK = f'updates/{STEM}.md'
NOTES = 'docs/.vuepress/lib/review-notes.json'
BASE = f'http://localhost:8080/{NAME}.html'
page = [re.sub(r'<a id="rev-[^"]*"></a>', '', l) for l in open(PAGE).read().split('\n')]
notes = {}
SETTLED = ('done', 'kept', 'noted')
if '--strip' not in sys.argv:
    pat = re.compile(r'^- Jump: \[rendered page\]\([^)]*\) · \[source, line \d+\]\([^)]*\) · search text: `(.*?)`(.*)$')
    track = open(TRACK).read().split('\n')
    rows = {}
    for l in track:
        if l.startswith('| ') and l.count('|') >= 4:
            cells = [c.strip() for c in l.strip().strip('|').split(' | ')]
            if len(cells) >= 3 and re.fullmatch(r'[A-Z]\d+', cells[0]):
                rows[cells[0]] = cells[2]
    out, cur, prefix, items = [], None, {}, {}
    for l in track:
        h = re.match(r'^#### (\S+)\s*(.*)$', l)
        if h:
            cur = h.group(1)
            items[cur] = {'id': cur, 'title': h.group(2), 'status': '', 'finding': '', 'suggestion': '', 'change': '', 'places': []}
        elif l.startswith('## ') or l.startswith('### '):
            cur = None
        for field in ('Status', 'Finding', 'Suggestion', 'Change'):
            f = re.match(rf'^- {field}: (.*)$', l)
            if f and cur:
                items[cur][field.lower()] = f.group(1)
        m = pat.match(l)
        # A settled item keeps its Jump line as a record, but gets no anchor and no check.
        if m and cur and not items[cur]['status'].lower().startswith(SETTLED):
            needle, rest = m.group(1), m.group(2)
            hits = [i for i, x in enumerate(page) if needle in x]
            if len(hits) != 1:
                sys.exit(f'{cur}: search text matches {len(hits)} lines: {needle}')
            i = hits[0]
            if re.match(r'\s*(#|\||- |\d+\. |\$\$|<)', page[i]):
                sys.exit(f'{cur}: search text is on a heading, list item, table row or equation: {needle}')
            k = len(items[cur]['places'])
            aid = f'rev-{cur}' + ('' if k == 0 else '-' + 'bcdefgh'[k - 1])
            prefix.setdefault(i, []).append(aid)
            items[cur]['places'].append({'key': aid[4:], 'place': rest.strip().strip('()')})
            l = f'- Jump: [rendered page]({BASE}?rev={aid[4:]}) · [source, line {i + 1}](../{PAGE}#L{i + 1}) · search text: `{needle}`{rest}'
        out.append(l)
    shown = [v for v in items.values() if (v['change'] or v['places']) and not v['status'].lower().startswith(SETTLED)]
    for v in shown:
        v['finding'] = v['finding'] or rows.get(v['id'], '')
    order = lambda v: (re.match(r'[A-Z]+', v['id']).group(0), int(re.search(r'\d+', v['id']).group(0)))
    shown.sort(key=order)
    places = {}
    for v in shown:
        for k, pl in enumerate(v['places']):
            places[pl['key']] = {'id': v['id'], 'place': pl['place'], 'first': k == 0}
    notes = {'page': NAME, 'items': shown, 'places': places}
    keep = {p['key'] for v in shown for p in v['places']}
    for i, ids in prefix.items():
        page[i] = ''.join(f'<a id="{a}"></a>' for a in ids if a[4:] in keep) + page[i]
    open(TRACK, 'w').write('\n'.join(out))
    print(len(shown), 'items,', len(keep), 'anchors')
open(PAGE, 'w').write('\n'.join(page))
open(NOTES, 'w').write(json.dumps(notes, indent=1, ensure_ascii=False) + '\n')
