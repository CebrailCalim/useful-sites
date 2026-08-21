# -*- coding: utf-8 -*-
"""Smoke test for the build output.

    python data/test_build.py

A broken part file does not raise: `add()` simply never runs for the entries
below the error, the build reports a smaller number, and nobody notices until
a category looks thin. Nothing asserted that the count had not collapsed.

These checks are deliberately blunt. They do not judge whether a description
is good; they catch the failures that are silent -- records vanishing, a
category losing its introduction, a pick pointing at a URL that no longer
exists, the two language files falling out of step.

MIN_RECORDS is a floor, not the current count. Raise it on purpose when the
directory grows; never lower it to make a red build green.
"""
import io
import json
import os
import re
import sys

D = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(D)
sys.path.insert(0, D)

import readlinks                        # noqa: E402
from notes import CATS                  # noqa: E402
from intros import INTROS               # noqa: E402
from picks import PICKS                 # noqa: E402
from sources import SOURCES             # noqa: E402
from tags import CANON, LABELS          # noqa: E402

MIN_RECORDS = 940
MIN_CATEGORIES = 24

fails = []


def check(ok, msg):
    print(('  ok   ' if ok else '  FAIL ') + msg)
    if not ok:
        fails.append(msg)


def main():
    print('build output')
    rows = readlinks.read(ROOT)
    check(len(rows) >= MIN_RECORDS,
          'records: %d (floor %d)' % (len(rows), MIN_RECORDS))

    en = io.open(os.path.join(ROOT, 'links.en.js'), encoding='utf-8').read()
    en_n = len(json.loads(en[en.index('['):en.rindex(';')]))
    check(en_n == len(rows),
          'English descriptions match record count: %d vs %d' % (en_n, len(rows)))

    print('records')
    eksik = [d['name'] for d in rows
             if not all(d.get(f) for f in ('url', 'name', 'cat', 'tr'))]
    check(not eksik, 'every record has url, name, category and description'
          + (' -- missing: %s' % eksik[:3] if eksik else ''))

    etiketsiz = [d['name'] for d in rows if not d.get('tags')]
    check(not etiketsiz, 'every record carries at least one tag'
          + (' -- bare: %s' % etiketsiz[:3] if etiketsiz else ''))

    disi = sorted({t for d in rows for t in d['tags']} - set(CANON))
    check(not disi, 'no tag outside the canonical set'
          + (' -- stray: %s' % disi[:5] if disi else ''))

    gorunmez = sorted({t for d in rows for t in d['tags']} - set(LABELS))
    check(not gorunmez, 'every tag has a display label'
          + (' -- missing: %s' % gorunmez[:5] if gorunmez else ''))

    seen, dup = set(), []
    for d in rows:
        k = re.sub(r'^https?://(www\.)?', '', d['url'].lower()).rstrip('/')
        if k in seen:
            dup.append(d['name'])
        seen.add(k)
    check(not dup, 'no duplicate URLs' + (' -- %s' % dup[:3] if dup else ''))

    kaynaksiz = sorted({d['src'] for d in rows} - set(SOURCES))
    check(not kaynaksiz, 'every record has a declared source'
          + (' -- unknown: %s' % kaynaksiz if kaynaksiz else ''))

    print('categories')
    keys = [c[0] for c in CATS]
    kullanilan = {d['cat'] for d in rows}
    check(len(kullanilan) >= MIN_CATEGORIES,
          'categories in use: %d (floor %d)' % (len(kullanilan), MIN_CATEGORIES))

    yabanci = sorted(kullanilan - set(keys))
    check(not yabanci, 'no record in an undeclared category'
          + (' -- %s' % yabanci if yabanci else ''))

    girissiz = sorted(kullanilan - set(INTROS))
    check(not girissiz, 'every category in use has an introduction'
          + (' -- %s' % girissiz if girissiz else ''))

    print('picks')
    urls = {d['url'] for d in rows}
    kayip = sorted(PICKS - urls)
    check(not kayip, 'every start-here URL resolves to a record'
          + (' -- %s' % kayip[:3] if kayip else ''))

    print('static output')
    for name in ('sitemap.xml', 'robots.txt', 'feed.xml', 'og.png'):
        check(os.path.exists(os.path.join(ROOT, name)), 'exists: ' + name)
    for k in sorted(kullanilan):
        tr = os.path.join(ROOT, 'k', k + '.html')
        en_p = os.path.join(ROOT, 'k', 'en', k + '.html')
        if not (os.path.exists(tr) and os.path.exists(en_p)):
            check(False, 'static pages for category: ' + k)
    check(True, 'static pages present in both languages for %d categories'
          % len(kullanilan))

    ix = io.open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
    check('links.js?v=' in ix, 'links.js carries a cache stamp')
    check('KULLANICI' not in ix, 'no placeholder repository address left')

    print()
    if fails:
        print('%d check(s) failed' % len(fails))
        return 1
    print('all checks passed')
    return 0


if __name__ == '__main__':
    sys.exit(main())
