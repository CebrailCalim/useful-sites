# -*- coding: utf-8 -*-
"""One-off liveness check over the remaining links."""
import json
import io
import concurrent.futures as cf
import requests
import urllib3

urllib3.disable_warnings()

D = r'C:\Users\Cebrail\Documents\code\duzen\site\data'
links = json.load(io.open(D + r'\kept.json', encoding='utf-8'))

UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36')
HEADERS = {'User-Agent': UA, 'Accept-Language': 'tr,en;q=0.9'}


def check(rec):
    url = rec['url']
    out = dict(rec)
    for method in ('head', 'get'):
        try:
            r = requests.request(method, url, headers=HEADERS, timeout=12,
                                 allow_redirects=True, verify=False,
                                 stream=(method == 'get'))
            out['status'] = r.status_code
            out['final'] = r.url
            if method == 'get':
                r.close()
            if r.status_code < 400:
                return out
            if r.status_code in (403, 405, 501) and method == 'head':
                continue          # HEAD engelli olabilir, GET dene
            return out
        except Exception as e:
            out['status'] = 0
            out['error'] = type(e).__name__
    return out


with cf.ThreadPoolExecutor(max_workers=24) as ex:
    results = list(ex.map(check, links))

json.dump(results, io.open(D + r'\checked.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)

import collections
c = collections.Counter()
for r in results:
    s = r.get('status', 0)
    c['canli' if 0 < s < 400 else ('olu-%s' % s if s else 'baglanti-hatasi')] += 1
for k, v in c.most_common():
    print(k, v)
print('TOPLAM', len(results))
