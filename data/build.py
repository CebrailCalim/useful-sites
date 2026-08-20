# -*- coding: utf-8 -*-
"""Kurator notlarini toplanan meta veriyle birlestirip site verisini uretir.

Cikti:
  ../links.js      cekirdek veri + Turkce aciklama  (ilk yuklemede gelen)
  ../links.en.js   Ingilizce aciklamalar            (dil degistirilince yuklenir)

Ayirmanin sebebi: iki dilin aciklamalari toplam yukun buyuk kismi.
Tek dil yuklemek ilk acilisi belirgin hafifletiyor.
"""
import json
import io
import re
import os
import sys
import html
import collections

D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, D)
from notes import NOTES, CATS          # noqa: E402
from tags import normalise             # noqa: E402
from picks import PICKS               # noqa: E402

BOOKMARKS = r'C:\Users\Cebrail\Documents\code\duzen\bookmarks_duzenli.html'
meta = json.load(io.open(os.path.join(D, 'meta.json'), encoding='utf-8'))


def key(u):
    u = re.sub(r'^https?://', '', u.strip().lower())
    u = re.sub(r'^www\.', '', u)
    return u.rstrip('/')


# ------------------------------------------------------------------ ekleme tarihleri
# Yer imi dosyasindaki ADD_DATE alani, baglantinin ne zaman toplandigini veriyor.
ADDED = {}
if os.path.exists(BOOKMARKS):
    for ln in io.open(BOOKMARKS, encoding='utf-8'):
        m = re.search(r'<DT><A HREF="([^"]*)"[^>]*ADD_DATE="(\d+)"', ln.strip())
        if m:
            k = key(html.unescape(m.group(1)))
            ts = int(m.group(2))
            if 946684800 < ts < 2200000000:        # 2000-2039 arasi makul
                ADDED[k] = max(ADDED.get(k, 0), ts)

PATHMAP = [
    ('Bilişim/Yol Haritaları', 'ogrenme'), ('Bilişim/Eğitim Platformları', 'ogrenme'),
    ('Bilişim/Sertifika & Sınav', 'ogrenme'), ('Bilişim/Pratik & Egzersiz', 'pratik'),
    ('Bilişim/Programlama Dilleri', 'diller'), ('Bilişim/Web & Frontend', 'web'),
    ('Bilişim/Backend & Framework', 'backend'), ('Bilişim/Sistem Tasarımı & API', 'backend'),
    ('Bilişim/Mobil & Masaüstü', 'mobil'), ('Bilişim/Veritabanı', 'veritabani'),
    ('Bilişim/DevOps & Altyapı', 'devops'), ('Bilişim/Ağ & Linux', 'ag'),
    ('Bilişim/IT Destek & Sistem', 'ag'), ('Bilişim/Siber Güvenlik', 'guvenlik'),
    ('Bilişim/Veri Bilimi & ML', 'veri'), ('Bilişim/Yapay Zeka/AI Altyapı', 'yz_altyapi'),
    ('Bilişim/Yapay Zeka/API & Geliştirme', 'yz_altyapi'),
    ('Bilişim/Yapay Zeka/Agent & Claude', 'yz_altyapi'),
    ('Bilişim/Yapay Zeka/AI Araçları', 'yz_arac'),
    ('Bilişim/Yapay Zeka/Üretken Araçlar', 'yz_arac'),
    ('Bilişim/Yapay Zeka/Sohbet', 'yz_model'), ('Bilişim/Yapay Zeka/Model Arşivi', 'yz_model'),
    ('Bilişim/Yapay Zeka', 'yz_model'),
    ('Bilişim/Donanım, CAD & Robotik/Akıllı Gözlük', 'gozluk'),
    ('Bilişim/Donanım, CAD & Robotik', 'donanim'), ('Bilişim/Kuantum Bilişim', 'kuantum'),
    ('Bilişim/Araçlar', 'araclar'), ('Bilişim/Referans', 'referans'),
    ('Bilişim/GitHub Koleksiyonları', 'referans'), ('Bilim & Düşünce', 'bilim'),
]


def cat_of(path):
    for pre, c in PATHMAP:
        if path.startswith(pre):
            return c
    return 'araclar'


# ayni kaynagin ikinci URL bicimi - listede tekrar gostermeye gerek yok
SKIP = {
    'servicedesk-simulator.com/#ticket/inc0012871/ad',
    'learn-anything.xyz/c-libraries',
}

out, missing, seen = [], [], set()
for m in meta:
    k = key(m['url'])
    if k in seen or k in SKIP:
        continue
    seen.add(k)
    n = NOTES.get(k) or NOTES.get(re.split(r'[?#]', k)[0].rstrip('/'))
    if not n:
        missing.append((k, m.get('title', '')[:60]))
        continue
    rec = {
        'url': m['url'],
        'name': n['name'],
        'cat': n.get('cat') or cat_of(m['path']),
        'tags': normalise(n.get('tags', [])),
        'tr': n['tr'],
        'en': n['en'],
    }
    ts = ADDED.get(k) or ADDED.get(re.split(r'[?#]', k)[0].rstrip('/'))
    if ts:
        rec['added'] = ts
    if m['url'] in PICKS:
        rec['pick'] = 1
    out.append(rec)

FALLBACK = 1787000000          # derleme sirasinda eklenen YZ araclari
for r in out:
    r.setdefault('added', FALLBACK)

order = [c[0] for c in CATS]
out.sort(key=lambda r: (order.index(r['cat']) if r['cat'] in order else 99,
                        r['name'].lower()))

cmap = {c[0]: (c[1], c[2]) for c in CATS}

core, en = [], []
for r in out:
    ct, ce = cmap.get(r['cat'], (r['cat'], r['cat']))
    core.append({
        'url': r['url'], 'name': r['name'], 'cat': r['cat'],
        'cat_tr': ct, 'cat_en': ce, 'tags': r['tags'],
        'tr': r['tr'], 'added': r['added'],
    })
    if r.get('pick'):
        core[-1]['pick'] = 1
    en.append(r['en'])

J = dict(ensure_ascii=False, separators=(',', ':'))
io.open(os.path.join(D, '..', 'links.js'), 'w', encoding='utf-8').write(
    '/* Otomatik uretildi - data/build.py */\nwindow.LINKS=' + json.dumps(core, **J) + ';\n')
io.open(os.path.join(D, '..', 'links.en.js'), 'w', encoding='utf-8').write(
    '/* Otomatik uretildi - data/build.py */\nwindow.LINKS_EN=' + json.dumps(en, **J) + ';\n')

tc = collections.Counter(t for r in out for t in r['tags'])
print('kayit          :', len(out))
print('etiket cesidi  :', len(tc))
print('etiketsiz kayit:', sum(1 for r in out if not r['tags']))
print('notu olmayan   :', len(missing))
print('gercek tarihli :', sum(1 for r in out if r['added'] != FALLBACK))
print('baslangic nok. :', sum(1 for r in out if r.get('pick')), '/', len(PICKS))
if missing:
    io.open(os.path.join(D, 'missing.txt'), 'w', encoding='utf-8').write(
        '\n'.join('%s\t%s' % t for t in missing))
