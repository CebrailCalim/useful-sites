# -*- coding: utf-8 -*-
"""Kayitlarin nereden geldigi.

Dizinde iki farkli kokene sahip kayit var ve bunlarin guvenilirligi ayni degil:

  kedi  : Kendi yer imi arsivimden gelen, tek tek gozden gecirilmis kayitlar.
          Aciklamalar projenin kendi belgelerine bakilarak yazildi.
  dis   : Disaridaki derlemelerden alinan kayitlar. Kaynak liste ve o listenin
          kendi notu belli; aciklama daha kisa, karsilastirmali yargi daha az.

Okuyucunun bu ayrimi gorebilmesi durustluk meselesi: 700 kaydin hepsi ayni
titizlikte degil, oyleymis gibi gostermek dizini oldurur.
"""

SOURCES = {
    'kedi': {
        'label_tr': 'Kedi',
        'label_en': 'Kedi',
        'note_tr': 'Kendi arşivinden, tek tek gözden geçirilmiş',
        'note_en': 'From the curator’s own archive, reviewed one by one',
        'url': None,
    },
    'bwapsv': {
        'label_tr': 'Dış Liste',
        'label_en': 'External List',
        'note_tr': 'Best-websites-a-programmer-should-visit derlemesinden alındı',
        'note_en': 'Taken from the Best-websites-a-programmer-should-visit collection',
        'url': 'https://github.com/sdmg15/Best-websites-a-programmer-should-visit',
    },
}

DEFAULT = 'kedi'
