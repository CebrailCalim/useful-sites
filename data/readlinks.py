# -*- coding: utf-8 -*-
"""links.js icindeki kayit listesini okur.

Kendi basina bir dosya olmasinin sebebi bir hata: once bu is her betikte
`src[src.index('['):src.rindex(';')]` diye yapiliyordu. links.js'e sonradan
window.TAGLABELS eklendi, onun ilk `[` karakteri artik daha onde -- dilim
bozuk JSON'a denk geldi ve iki CI betigi de sessizce cokmeye basladi.
Workflow'da continue-on-error acik oldugu icin haftalarca yesil gorundu.

Buradaki okuyucu window.LINKS= isaretini aciktan ariyor ve parantez sayarak
bitis yerini buluyor; links.js'e yeni bir degisken eklenmesi onu bozmuyor.
"""
import io
import json
import os

MARK = 'window.LINKS='


def read(root):
    path = os.path.join(root, 'links.js')
    src = io.open(path, encoding='utf-8').read()

    i = src.find(MARK)
    if i < 0:
        raise ValueError('links.js icinde %s yok' % MARK)
    i += len(MARK)
    if src[i] != '[':
        raise ValueError('%s ardindan dizi beklenirken %r geldi' % (MARK, src[i]))

    depth, instr, esc = 0, False, False
    for j in range(i, len(src)):
        c = src[j]
        if instr:
            if esc:
                esc = False
            elif c == '\\':
                esc = True
            elif c == '"':
                instr = False
            continue
        if c == '"':
            instr = True
        elif c == '[':
            depth += 1
        elif c == ']':
            depth -= 1
            if depth == 0:
                return json.loads(src[i:j + 1])
    raise ValueError('links.js icindeki dizi kapanmiyor')
