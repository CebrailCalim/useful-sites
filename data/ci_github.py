# -*- coding: utf-8 -*-
"""Audits the health of linked GitHub repositories: archived, or untouched.

A repository can die without ever returning 404 -- it gets archived, turns
read-only, or simply goes years without a commit. A link check cannot see
any of that. This script can.

Runs inside GitHub Actions with GITHUB_TOKEN (5000 requests/hour).
Locally it hits the anonymous limit after 60; pass a token:
    GH_TOKEN=ghp_xxx python data/ci_github.py
"""
import json
import io
import os
import re
import sys
import datetime
import concurrent.futures as cf

import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import readlinks  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOKEN = os.environ.get('GITHUB_TOKEN') or os.environ.get('GH_TOKEN')

HEADERS = {'User-Agent': 'link-directory-health', 'Accept': 'application/vnd.github+json'}
if TOKEN:
    HEADERS['Authorization'] = 'Bearer ' + TOKEN

# A repository untouched for this long counts as stale.
STALE_DAYS = 730          # iki yil
SKIP_OWNERS = {'topics', 'features', 'education', 'sponsors', 'orgs', 'collections'}


def repos():
    rows = readlinks.read(ROOT)
    out = []
    for r in rows:
        m = re.match(r'https://github\.com/([^/]+)/([^/#?]+)', r['url'])
        if m and m.group(1).lower() not in SKIP_OWNERS:
            out.append((r['name'], r.get('cat_tr', ''), m.group(1), m.group(2), r['url']))
    return out


def check(t):
    name, cat, owner, repo, url = t
    try:
        r = requests.get('https://api.github.com/repos/%s/%s' % (owner, repo),
                         headers=HEADERS, timeout=15)
    except requests.exceptions.RequestException as e:
        return {'name': name, 'cat': cat, 'url': url, 'state': 'hata', 'detail': type(e).__name__}

    if r.status_code == 404:
        return {'name': name, 'cat': cat, 'url': url, 'state': 'yok', 'detail': 'depo silinmiş'}
    if r.status_code in (403, 429):
        return {'name': name, 'cat': cat, 'url': url, 'state': 'kota', 'detail': str(r.status_code)}
    if r.status_code != 200:
        return {'name': name, 'cat': cat, 'url': url, 'state': 'hata', 'detail': str(r.status_code)}

    j = r.json()
    pushed = (j.get('pushed_at') or '')[:10]
    rec = {'name': name, 'cat': cat, 'url': url, 'pushed': pushed,
           'stars': j.get('stargazers_count')}
    if j.get('archived'):
        rec['state'] = 'arşiv'
        return rec
    if pushed:
        age = (datetime.date.today() - datetime.date.fromisoformat(pushed)).days
        if age > STALE_DAYS:
            rec['state'] = 'bayat'
            rec['detail'] = '%d gün' % age
            return rec
    rec['state'] = 'aktif'
    return rec


def main():
    rs = repos()
    if not TOKEN:
        print('UYARI: token yok, 60 istek sonrasi kotaya takilacak', file=sys.stderr)
    with cf.ThreadPoolExecutor(max_workers=8 if TOKEN else 3) as ex:
        results = list(ex.map(check, rs))

    by = {}
    for r in results:
        by.setdefault(r['state'], []).append(r)

    print('taranan depo: %d' % len(rs))
    for k in sorted(by):
        print('  %-7s %d' % (k, len(by[k])))

    flagged = by.get('arşiv', []) + by.get('bayat', []) + by.get('yok', [])
    if not flagged:
        return 0

    L = ['# GitHub depo sağlığı — %s' % datetime.date.today().isoformat(), '',
         '`%d` depo tarandı. Bunlar 404 döndürmüyor ama artık bakımda değil.' % len(rs), '']

    for state, baslik, aciklama in [
        ('yok',    'Silinmiş', 'Depo artık yok.'),
        ('arşiv',  'Arşivlenmiş', 'Salt okunur. Sorunlar kapanmıyor, ölü bağlantılar temizlenmiyor. '
                                  'Açıklamaya not düşülmeli ya da kayıt çıkarılmalı.'),
        ('bayat',  'Bayat (2+ yıl dokunulmamış)', 'Terk edilmiş olabilir; alternatifi var mı bakılmalı.'),
    ]:
        rows = by.get(state, [])
        if not rows:
            continue
        L += ['## %s (%d)' % (baslik, len(rows)), '', aciklama, '',
              '| Kayıt | Kategori | Son itme | Yıldız | URL |', '|---|---|---|---|---|']
        for r in sorted(rows, key=lambda x: x.get('pushed') or ''):
            L.append('| %s | %s | %s | %s | %s |' % (
                r['name'], r['cat'], r.get('pushed') or r.get('detail', '—'),
                r.get('stars', '—'), r['url']))
        L.append('')

    if by.get('kota'):
        L.append('> %d depo API kotası yüzünden denetlenemedi.' % len(by['kota']))
        L.append('')

    L.append('<sub>`data/ci_github.py` tarafından otomatik üretildi.</sub>')
    io.open(os.path.join(ROOT, 'rapor-github.md'), 'w', encoding='utf-8').write('\n'.join(L))
    return 0


if __name__ == '__main__':
    sys.exit(main())
