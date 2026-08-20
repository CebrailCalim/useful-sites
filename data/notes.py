# -*- coding: utf-8 -*-
"""Kurator notlari kayit defteri.

Notlarin kendisi part_*.py dosyalarinda; her biri load(add) sunar.
Anahtar = normalize edilmis URL (sema, www ve sondaki / atilmis).

tr/en alanlarinda hedef: "bu ne ise yarar" + "benzerlerinden farki ne".
Reklam cumlesi degil, secim yapmaya yarayan cumle.
"""
import re

# key, TR ad, EN ad
CATS = [
    ('ogrenme',    'Öğrenme & Yol Haritaları',      'Learning & Roadmaps'),
    ('pratik',     'Pratik & Alıştırma',            'Practice & Challenges'),
    ('diller',     'Programlama Dilleri',           'Programming Languages'),
    ('web',        'Web & Frontend',                'Web & Frontend'),
    ('backend',    'Backend, API & Sistem Tasarımı', 'Backend, API & System Design'),
    ('mobil',      'Mobil & Masaüstü',              'Mobile & Desktop'),
    ('veritabani', 'Veritabanı',                    'Databases'),
    ('devops',     'DevOps & Altyapı',              'DevOps & Infrastructure'),
    ('ag',         'Ağ & Sistem Yönetimi',          'Networking & Sysadmin'),
    ('guvenlik',   'Güvenlik & Gizlilik',           'Security & Privacy'),
    ('veri',       'Veri Bilimi & Makine Öğrenmesi', 'Data Science & ML'),
    ('yz_model',   'YZ · Modeller & Asistanlar',    'AI · Models & Assistants'),
    ('yz_altyapi', 'YZ · Agent, RAG & Altyapı',     'AI · Agents, RAG & Infra'),
    ('yz_arac',    'YZ · Uygulama Araçları',        'AI · Applied Tools'),
    ('donanim',    'Donanım, CAD & Gömülü',         'Hardware, CAD & Embedded'),
    ('gozluk',     'Akıllı Gözlük & Giyilebilir',   'Smart Glasses & Wearables'),
    ('kuantum',    'Kuantum Bilişim',               'Quantum Computing'),
    ('araclar',    'Araçlar & Yardımcılar',         'Tools & Utilities'),
    ('referans',   'Referans & Koleksiyonlar',      'Reference & Collections'),
    ('bilim',      'Bilim & Akademik',              'Science & Academia'),
]

NOTES = {}


def add(url, name, tags, tr, en, cat=None):
    k = re.sub(r'^https?://', '', url.strip().lower())
    k = re.sub(r'^www\.', '', k).rstrip('/')
    NOTES[k] = {'name': name, 'tags': tags, 'tr': tr, 'en': en, 'cat': cat}


PARTS = [
    'part_ai_model', 'part_ai_infra', 'part_ai_tools',
    'part_dev', 'part_ops', 'part_infra', 'part_sec',
    'part_hw', 'part_misc', 'part_extra',
]

import importlib  # noqa: E402

for _name in PARTS:
    importlib.import_module(_name).load(add)
