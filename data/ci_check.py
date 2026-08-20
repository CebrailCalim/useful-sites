# -*- coding: utf-8 -*-
"""links.js icindeki baglantilari tarar, olenleri rapor.md olarak yazar.

GitHub Actions icin. Yerelde de calisir:  python data/ci_check.py

Bot engeli (403/429) ile gercek olum (404/410/DNS) ayri tutulur; ilki
raporda "supheli" olarak isaretlenir cunku tarayicida acilir.
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

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36')
HEADERS = {'User-Agent': UA, 'Accept-Language': 'tr,en;q=0.9'}

# Bu kodlar bot engeli demek, baglanti calisiyor olabilir.
SOFT = {401, 403, 405, 406, 429, 500, 503}


def load_links():
    src = io.open(os.path.join(ROOT, 'links.js'), encoding='utf-8').read()
    return json.loads(src[src.index('['):src.rindex(';')])


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
                return None                     # saglam
            if method == 'head' and r.status_code in SOFT:
                continue                        # GET ile bir daha dene
            return out
        except requests.exceptions.RequestException as e:
            out['status'] = 0
            out['error'] = type(e).__name__
    return out


def write_verified(links, bad_by_url):
    """Kayit bazinda son dogrulama tarihini tazeler.

    Site her satirda 'son dogrulama' gosteriyor; bu dosya onun kaynagi.
    Sorunlu olanlar 'engel' olarak isaretlenir, tarihleri yine guncellenir."""
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
        # gercekten olu olanin tarihini tazelemiyoruz: eski tarih uyari degeri tasiyor
    json.dump(ver, io.open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('verified.json guncellendi:', len(ver))


def main():
    links = load_links()
    with cf.ThreadPoolExecutor(max_workers=16) as ex:
        results = [r for r in ex.map(check, links) if r]
    write_verified(links, {r['url']: r for r in results})

    dead = [r for r in results if r['status'] == 404 or r['status'] == 410 or r['status'] == 0]
    soft = [r for r in results if r not in dead]

    print('taranan: %d | olu: %d | supheli: %d' % (len(links), len(dead), len(soft)))

    if not results:
        # eski rapor varsa temizle ki issue "temiz" kalsin
        if os.path.exists(os.path.join(ROOT, 'rapor.md')):
            os.remove(os.path.join(ROOT, 'rapor.md'))
        return 0

    today = datetime.date.today().isoformat()
    L = ['# Bağlantı kontrolü — %s' % today, '',
         '`%d` bağlantı tarandı.' % len(links), '']

    if dead:
        L += ['## Ölü (%d)' % len(dead), '',
              'Bunlar 404/410 döndü ya da hiç yanıt vermedi. Değiştirilmeli veya çıkarılmalı.', '',
              '| Kayıt | Kategori | Durum | URL |', '|---|---|---|---|']
        for r in sorted(dead, key=lambda x: x['cat']):
            st = r.get('error') or r['status']
            L.append('| %s | %s | `%s` | %s |' % (r['name'], r['cat'], st, r['url']))
        L.append('')

    if soft:
        L += ['## Şüpheli (%d)' % len(soft), '',
              'Bot engeli olabilir (403/429/503) — tarayıcıda büyük ihtimalle açılıyor. '
              'Elle doğrulanmalı.', '',
              '| Kayıt | Kategori | Durum | URL |', '|---|---|---|---|']
        for r in sorted(soft, key=lambda x: x['cat']):
            L.append('| %s | %s | `%s` | %s |' % (r['name'], r['cat'], r['status'], r['url']))
        L.append('')

    L.append('<sub>`data/ci_check.py` tarafından otomatik üretildi.</sub>')
    io.open(os.path.join(ROOT, 'rapor.md'), 'w', encoding='utf-8').write('\n'.join(L))
    return 1 if dead else 0


if __name__ == '__main__':
    sys.exit(main())
