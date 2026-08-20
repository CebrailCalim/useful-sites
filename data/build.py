# -*- coding: utf-8 -*-
"""Kurator notlarini toplanan meta veriyle birlestirip links.js uretir."""
import json
import io
import re
import os
import sys

D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, D)
from notes import NOTES, CATS          # noqa: E402

meta = json.load(io.open(os.path.join(D, 'meta.json'), encoding='utf-8'))


def key(u):
    u = re.sub(r'^https?://', '', u.strip().lower())
    u = re.sub(r'^www\.', '', u)
    return u.rstrip('/')


# --- yer imi klasoru -> genel kategori
PATHMAP = [
    ('Bilişim/Yol Haritaları',              'ogrenme'),
    ('Bilişim/Eğitim Platformları',         'ogrenme'),
    ('Bilişim/Sertifika & Sınav',           'ogrenme'),
    ('Bilişim/Pratik & Egzersiz',           'pratik'),
    ('Bilişim/Programlama Dilleri',         'diller'),
    ('Bilişim/Web & Frontend',              'web'),
    ('Bilişim/Backend & Framework',         'backend'),
    ('Bilişim/Sistem Tasarımı & API',       'backend'),
    ('Bilişim/Mobil & Masaüstü',            'mobil'),
    ('Bilişim/Veritabanı',                  'veritabani'),
    ('Bilişim/DevOps & Altyapı',            'devops'),
    ('Bilişim/Ağ & Linux',                  'ag'),
    ('Bilişim/IT Destek & Sistem',          'ag'),
    ('Bilişim/Siber Güvenlik',              'guvenlik'),
    ('Bilişim/Veri Bilimi & ML',            'veri'),
    ('Bilişim/Yapay Zeka/AI Altyapı',       'yz_altyapi'),
    ('Bilişim/Yapay Zeka/API & Geliştirme', 'yz_altyapi'),
    ('Bilişim/Yapay Zeka/Agent & Claude',   'yz_altyapi'),
    ('Bilişim/Yapay Zeka/AI Araçları',      'yz_arac'),
    ('Bilişim/Yapay Zeka/Üretken Araçlar',  'yz_arac'),
    ('Bilişim/Yapay Zeka/Sohbet',           'yz_model'),
    ('Bilişim/Yapay Zeka/Model Arşivi',     'yz_model'),
    ('Bilişim/Yapay Zeka',                  'yz_model'),
    ('Bilişim/Donanım, CAD & Robotik/Akıllı Gözlük', 'gozluk'),
    ('Bilişim/Donanım, CAD & Robotik',      'donanim'),
    ('Bilişim/Kuantum Bilişim',             'kuantum'),
    ('Bilişim/Araçlar',                     'araclar'),
    ('Bilişim/Referans',                    'referans'),
    ('Bilişim/GitHub Koleksiyonları',       'referans'),
    ('Bilim & Düşünce',                     'bilim'),
]


def cat_of(path):
    for pre, c in PATHMAP:
        if path.startswith(pre):
            return c
    return 'araclar'


out, missing = [], []
seen = set()
for m in meta:
    k = key(m['url'])
    if k in seen:
        continue
    seen.add(k)
    n = NOTES.get(k)
    if not n:                       # sorgu dizesi / fragman farkini tolere et
        base = re.split(r'[?#]', k)[0].rstrip('/')
        n = NOTES.get(base)
    if not n:
        missing.append((k, m.get('title', '')[:60], (m.get('desc') or '')[:90]))
        continue
    cat = n.get('cat') or cat_of(m['path'])
    rec = {
        'url': m['url'],
        'name': n['name'],
        'cat': cat,
        'tags': n.get('tags', []),
        'tr': n['tr'],
        'en': n['en'],
    }
    if m.get('stars'):
        rec['stars'] = m['stars']
    out.append(rec)

order = [c[0] for c in CATS]
out.sort(key=lambda r: (order.index(r['cat']) if r['cat'] in order else 99,
                        r['name'].lower()))

cmap = {c[0]: (c[1], c[2]) for c in CATS}
for r in out:
    r['cat_tr'], r['cat_en'] = cmap.get(r['cat'], (r['cat'], r['cat']))

js = ('/* Otomatik uretildi - data/build.py. Elle duzenlenebilir. */\n'
      'window.LINKS = ' +
      json.dumps(out, ensure_ascii=False, indent=1) + ';\n')
io.open(os.path.join(D, '..', 'links.js'), 'w', encoding='utf-8').write(js)

print('yazilan kayit :', len(out))
print('notu olmayan  :', len(missing))
if missing:
    io.open(os.path.join(D, 'missing.txt'), 'w', encoding='utf-8').write(
        '\n'.join('%s\t%s\t%s' % t for t in missing))
    for t in missing[:20]:
        print('   -', t[0][:70])
