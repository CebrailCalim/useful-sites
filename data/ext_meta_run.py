# -*- coding: utf-8 -*-
"""Fetches the real page metadata for each link (title, description).

The point is to write descriptions from what a project says about itself
rather than from guesswork. For GitHub links the API supplies the repo
description, star count and language.

Note: the patterns are deliberately non-backtracking ([^"]* and such). The
first version used .*? and hit catastrophic backtracking on large pages --
it burned 580 seconds of CPU before it was killed.
"""
import json
import io
import re
import os
import html as htmllib
import concurrent.futures as cf
import requests
import urllib3

urllib3.disable_warnings()

D = os.path.dirname(os.path.abspath(__file__))
links = [x for x in json.load(io.open(os.path.join(D, 'ext_kontrol.json'), encoding='utf-8'))
         if 0 < x.get('status', 0) < 400 or x.get('status') in (403, 429, 503)]

UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36')
HEADERS = {'User-Agent': UA, 'Accept-Language': 'en,tr;q=0.9',
           'Accept': 'text/html,application/xhtml+xml'}

RE_TITLE = re.compile(r'<title[^>]*>([^<]{0,300})', re.I)
RE_META = re.compile(r'<meta\s+([^>]{0,600})>', re.I)
RE_ATTR = re.compile(r'(name|property|content)\s*=\s*"([^"]{0,600})"'
                     r'|(name|property|content)\s*=\s*\'([^\']{0,600})\'', re.I)

GH_TOKENless_SKIP = ('topics', 'features', 'education', 'sponsors', 'orgs')


def page_meta(body):
    """Collect the meta tags in a single pass."""
    desc = ''
    for m in RE_META.finditer(body):
        attrs = {}
        for a in RE_ATTR.finditer(m.group(1)):
            k = (a.group(1) or a.group(3) or '').lower()
            v = a.group(2) if a.group(2) is not None else a.group(4)
            if k:
                attrs[k] = v or ''
        key = (attrs.get('name') or attrs.get('property') or '').lower()
        if key in ('description', 'og:description', 'twitter:description'):
            c = htmllib.unescape(attrs.get('content', '')).strip()
            if c and (key == 'description' or not desc):
                desc = c
                if key == 'description':
                    break
    return re.sub(r'\s+', ' ', desc)[:400]


def fetch(rec):
    url = rec['url']
    out = dict(rec)

    gh = re.match(r'https://github\.com/([^/]+)/([^/#?]+)', url)
    if gh and gh.group(1).lower() not in GH_TOKENless_SKIP:
        try:
            r = requests.get('https://api.github.com/repos/%s/%s'
                             % (gh.group(1), gh.group(2)),
                             headers={'User-Agent': UA}, timeout=12)
            if r.status_code == 200:
                j = r.json()
                out['desc'] = j.get('description') or ''
                out['stars'] = j.get('stargazers_count')
                out['lang'] = j.get('language')
                out['topics'] = j.get('topics', [])
                out['archived'] = j.get('archived')
                out['pushed'] = (j.get('pushed_at') or '')[:10]
                out['src'] = 'github-api'
                return out
        except Exception:
            pass

    try:
        r = requests.get(url, headers=HEADERS, timeout=(6, 12), verify=False,
                         allow_redirects=True, stream=True)
        out['status'] = r.status_code
        chunks, total = [], 0
        for c in r.iter_content(16384):
            chunks.append(c)
            total += len(c)
            if total > 120000:
                break
        r.close()
        body = b''.join(chunks).decode(r.encoding or 'utf-8', 'replace')
        t = RE_TITLE.search(body)
        out['page_title'] = htmllib.unescape(t.group(1)).strip()[:200] if t else ''
        out['desc'] = page_meta(body)
        out['src'] = 'html'
    except Exception as e:
        out['status'] = 0
        out['error'] = type(e).__name__
    return out


with cf.ThreadPoolExecutor(max_workers=24) as ex:
    results = list(ex.map(fetch, links))

json.dump(results, io.open(os.path.join(D, 'ext_meta.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)

ok = sum(1 for r in results if r.get('desc'))
print('aciklama alinan :', ok, '/', len(results))
print('github api      :', sum(1 for r in results if r.get('src') == 'github-api'))
print('bos             :', len(results) - ok)
