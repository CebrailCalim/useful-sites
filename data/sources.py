# -*- coding: utf-8 -*-
"""Where each record came from.

The directory holds records of two different origins, and they are not
equally reliable:

  kedi  : From the owner's own bookmark archive, gone through one by one.
          Descriptions written against each project's own documentation.
  dis   : Taken from an outside compilation. The source list and its own
          note are known; descriptions are shorter and carry fewer
          comparative judgements.

Letting the reader see that difference is a matter of honesty. Not all 700
records were held to the same standard, and pretending otherwise would kill
the directory.
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
