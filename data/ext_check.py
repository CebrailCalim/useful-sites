# -*- coding: utf-8 -*-
"""Liveness scan over the candidates coming from the external list."""
import json, io, concurrent.futures as cf, requests, urllib3
urllib3.disable_warnings()
UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36')
H = {'User-Agent': UA, 'Accept-Language': 'en;q=0.9'}
SOFT = {401, 403, 405, 406, 429, 500, 503}

def check(x):
    o = dict(x)
    for m in ('head', 'get'):
        try:
            r = requests.request(m, x['url'], headers=H, timeout=(6, 12),
                                 allow_redirects=True, verify=False, stream=(m == 'get'))
            if m == 'get':
                r.close()
            o['status'] = r.status_code
            o['final'] = r.url
            if r.status_code < 400:
                return o
            if m == 'head' and r.status_code in SOFT:
                continue
            return o
        except Exception as e:
            o['status'] = 0
            o['error'] = type(e).__name__
    return o

ext = json.load(io.open('ext_aday.json', encoding='utf-8'))
with cf.ThreadPoolExecutor(max_workers=20) as p:
    res = list(p.map(check, ext))
json.dump(res, io.open('ext_kontrol.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
import collections
c = collections.Counter('canli' if 0 < x.get('status', 0) < 400 else str(x.get('status')) for x in res)
print(dict(c))
