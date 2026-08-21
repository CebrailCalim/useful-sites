# -*- coding: utf-8 -*-
"""Scans the links in links.js and writes the failures to rapor.md.

Meant for GitHub Actions; runs locally too:  python data/ci_check.py

Bot blocking (403/429) is kept apart from real death (404/410/DNS). The
former is reported as "suspect", because those pages open fine in a
browser and removing them would be a mistake.
"""
import json
import re
import io
import os
import sys
import datetime
import concurrent.futures as cf

import requests
import urllib3

urllib3.disable_warnings()

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import readlinks  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36')
HEADERS = {'User-Agent': UA, 'Accept-Language': 'tr,en;q=0.9'}

# These codes mean bot blocking; the link itself may be perfectly fine.
SOFT = {401, 403, 405, 406, 429, 500, 503}


def load_links():
    return readlinks.read(ROOT)


def check(rec):
    url = rec['url']
    out = {'name': rec['name'], 'url': url, 'cat': rec.get('cat_tr', '')}
    for method in ('head', 'get'):
        try:
            r = requests.request(method, url, headers=HEADERS, timeout=(6, 14),
                                 allow_redirects=True, verify=False,
                                 stream=(method == 'get'))
            if method == 'get':
                r.close()
            out['status'] = r.status_code
            if r.status_code < 400:
                return None                     # fine
            if method == 'head' and r.status_code in SOFT:
                continue                        # try again with GET
            return out
        except requests.exceptions.RequestException as e:
            out['status'] = 0
            out['error'] = type(e).__name__
    return out


def write_verified(links, bad_by_url):
    """Refreshes the per-record verification date.

    The site shows "last verified" on every entry and this file is where
    that comes from. Blocked ones are marked "engel" but still dated.
    """
    path = os.path.join(ROOT, 'data', 'verified.json')
    ver = {}
    if os.path.exists(path):
        ver = json.load(io.open(path, encoding='utf-8'))
    today = datetime.date.today().isoformat()
    for l in links:
        k = re.sub(r'^https?://(www\.)?', '', l['url'].strip().lower()).rstrip('/')
        b = bad_by_url.get(l['url'])
        if b is None:
            ver[k] = {'d': today, 's': 'ok'}
        elif b['status'] in SOFT:
            ver[k] = {'d': today, 's': 'engel'}
        else:
            # Genuinely dead. The date is left alone -- a stale date carries
            # its own warning -- but the status is recorded so the site can
            # flag the entry and point at the archive. A finding that stays
            # inside an issue never reaches the person reading the page.
            ver[k] = {'d': ver.get(k, {}).get('d', today), 's': 'olu'}
    # Entries removed from the directory leave their verification behind. The
    # file had accumulated 251 such keys against 988 records -- a quarter of it
    # describing links nobody can reach any more. Anything with no record is
    # dropped on each run.
    live = set()
    for l in links:
        k = re.sub(r'^https?://(www\.)?', '', l['url'].strip().lower()).rstrip('/')
        live.add(k)
        live.add(re.split(r'[?#]', k)[0].rstrip('/'))
    stale = [k for k in ver if k not in live]
    for k in stale:
        del ver[k]

    json.dump(ver, io.open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('verified.json updated: %d kept, %d stale keys dropped'
          % (len(ver), len(stale)))


def main():
    links = load_links()
    with cf.ThreadPoolExecutor(max_workers=16) as ex:
        results = [r for r in ex.map(check, links) if r]
    write_verified(links, {r['url']: r for r in results})

    dead = [r for r in results if r['status'] == 404 or r['status'] == 410 or r['status'] == 0]
    soft = [r for r in results if r not in dead]

    print('scanned: %d | dead: %d | suspect: %d' % (len(links), len(dead), len(soft)))

    if not results:
        # Clear any previous report so a clean week reads as clean.
        if os.path.exists(os.path.join(ROOT, 'rapor.md')):
            os.remove(os.path.join(ROOT, 'rapor.md'))
        return 0

    today = datetime.date.today().isoformat()
    L = ['# Link check - %s' % today, '',
         '`%d` links scanned.' % len(links), '']

    if dead:
        L += ['## Dead (%d)' % len(dead), '',
              'These returned 404/410 or did not answer at all. Replace or remove.', '',
              '| Entry | Category | Status | URL |', '|---|---|---|---|']
        for r in sorted(dead, key=lambda x: x['cat']):
            st = r.get('error') or r['status']
            L.append('| %s | %s | `%s` | %s |' % (r['name'], r['cat'], st, r['url']))
        L.append('')

    if soft:
        L += ['## Suspect (%d)' % len(soft), '',
              'Probably bot blocking (403/429/503) - these most likely open fine '
              'in a browser. Worth a manual look.', '',
              '| Entry | Category | Status | URL |', '|---|---|---|---|']
        for r in sorted(soft, key=lambda x: x['cat']):
            L.append('| %s | %s | `%s` | %s |' % (r['name'], r['cat'], r['status'], r['url']))
        L.append('')

    L.append('<sub>Generated by `data/ci_check.py`.</sub>')
    io.open(os.path.join(ROOT, 'rapor.md'), 'w', encoding='utf-8').write('\n'.join(L))
    return 1 if dead else 0


if __name__ == '__main__':
    sys.exit(main())
