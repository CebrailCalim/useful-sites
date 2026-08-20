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
from sources import SOURCES, DEFAULT  # noqa: E402
from intros import INTROS             # noqa: E402

BOOKMARKS = r'C:\Users\Cebrail\Documents\code\duzen\bookmarks_duzenli.html'
def _load(name):
    p = os.path.join(D, name)
    return json.load(io.open(p, encoding='utf-8')) if os.path.exists(p) else []


# Uc ayri meta kaynagi: ilk yer imi arsivi, dis liste, yeni disa aktarim.
# NOTES'ta karsiligi olmayanlar zaten asagida eleniyor.
meta = _load('meta.json') + _load('ext_meta.json')
def _base(k):
    return re.split(r'[?#]', k)[0].rstrip('/')


# Mevcut meta'daki URL'lerin hem tam hem sorgusuz bicimi.
# Ikisini de tutmazsak 'site.com/' ile 'site.com/?utm=x' ayri kayit sayilir.
_have = set()
for _m in meta:
    _k = re.sub(r'^https?://(www\.)?', '', _m['url'].lower()).rstrip('/')
    _have.add(_k)
    _have.add(_base(_k))

# NOTES'ta olup hicbir meta dosyasinda olmayanlar (yeni eklenenler) icin
# notun kendi URL'sinden sahte bir meta kaydi uret.
for _k, _n in sorted(NOTES.items()):
    if _n.get('url') and _k not in _have and _base(_k) not in _have:
        meta.append({'url': _n['url'], 'path': '', 'title': _n['name']})
        _have.add(_k)
        _have.add(_base(_k))


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

# Kayit bazinda son dogrulama: ci_check.py her hafta verified.json'i tazeliyor.
VERIFIED = {}
_vp = os.path.join(D, 'verified.json')
if os.path.exists(_vp):
    VERIFIED = json.load(io.open(_vp, encoding='utf-8'))

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
        'src': n.get('src') or DEFAULT,
    }
    ts = ADDED.get(k) or ADDED.get(re.split(r'[?#]', k)[0].rstrip('/'))
    if ts:
        rec['added'] = ts
    if m['url'] in PICKS:
        rec['pick'] = 1
    v = VERIFIED.get(k) or VERIFIED.get(re.split(r'[?#]', k)[0].rstrip('/'))
    if v:
        rec['ver'] = v['d']
        if v['s'] != 'ok':
            rec['verw'] = 1          # bot engeli - elle dogrulanmali
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
        'tr': r['tr'], 'added': r['added'], 'src': r['src'],
    })
    if r.get('ver'):
        core[-1]['ver'] = r['ver']
    if r.get('verw'):
        core[-1]['verw'] = 1
    if r.get('pick'):
        core[-1]['pick'] = 1
    en.append(r['en'])

# ------------------------------------------------------------------ ilgili kayitlar
# Ayni kategoride, etiketleri en cok ortusen uc kayit. Amac "bunu begendiysen
# suna bak" baglantisi kurmak; arastirmada dizinlerin bir eksigi de kategoriler
# arasi tekrari gorunur kilmamasiydi.
by_cat = {}
for i, r in enumerate(core):
    by_cat.setdefault(r['cat'], []).append(i)

for i, r in enumerate(core):
    ts = set(r['tags'])
    if not ts:
        continue
    puan = []
    for j in by_cat[r['cat']]:
        if j == i:
            continue
        ort = len(ts & set(core[j]['tags']))
        if ort >= 2:
            puan.append((ort, -abs(j - i), j))
    puan.sort(reverse=True)
    rel = [core[j]['name'] for _, _, j in puan[:3]]
    if rel:
        r['rel'] = rel

J = dict(ensure_ascii=False, separators=(',', ':'))
io.open(os.path.join(D, '..', 'links.js'), 'w', encoding='utf-8').write(
    '/* Otomatik uretildi - data/build.py */\n'
    'window.SOURCES=' + json.dumps(SOURCES, **J) + ';\n'
    'window.INTROS=' + json.dumps(INTROS, **J) + ';\n'
    'window.LINKS=' + json.dumps(core, **J) + ';\n')
io.open(os.path.join(D, '..', 'links.en.js'), 'w', encoding='utf-8').write(
    '/* Otomatik uretildi - data/build.py */\nwindow.LINKS_EN=' + json.dumps(en, **J) + ';\n')

tc = collections.Counter(t for r in out for t in r['tags'])
print('kayit          :', len(out))
print('etiket cesidi  :', len(tc))
print('etiketsiz kayit:', sum(1 for r in out if not r['tags']))
print('notu olmayan   :', len(missing))
print('gercek tarihli :', sum(1 for r in out if r['added'] != FALLBACK))
print('baslangic nok. :', sum(1 for r in out if r.get('pick')), '/', len(PICKS))
_sc = collections.Counter(r['src'] for r in out)
print('kaynak         :', dict(_sc))
print('dogrulanmis    :', sum(1 for r in core if r.get('ver')))
print('ilgili baglanti:', sum(1 for r in core if r.get('rel')))
if missing:
    io.open(os.path.join(D, 'missing.txt'), 'w', encoding='utf-8').write(
        '\n'.join('%s\t%s' % t for t in missing))
