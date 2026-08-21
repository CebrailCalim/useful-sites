# -*- coding: utf-8 -*-
"""Pulls the technology links out of the sorted bookmark file.

The owner's calls on what stays:
  - YouTube videos STAY (grouped by tag)
  - Turkish institutions STAY
  - Deep GitHub links (issue/blob/wiki) STAY
  - Google search URLs GO
  - Account-gated dashboard URLs are REPLACED by the site root
"""
import re
import html
import io
import json

SRC = r'C:\Users\Cebrail\Documents\code\duzen\bookmarks_duzenli.html'
OUT = r'C:\Users\Cebrail\Documents\code\duzen\site\data'

lines = io.open(SRC, encoding='utf-8').read().split('\n')
stack, recs, pending = [], [], None
for ln in lines:
    s = ln.strip()
    if s.startswith('<DT><H3'):
        m = re.search(r'>([^<]*)</H3>', s)
        pending = html.unescape(m.group(1)) if m else '?'
    elif s.startswith('<DL>'):
        stack.append(pending if pending is not None else '_')
        pending = None
    elif s.startswith('</DL>'):
        if stack:
            stack.pop()
    elif s.startswith('<DT><A'):
        h = re.search(r'HREF="([^"]*)"', s)
        t = re.search(r'>([^<]*)</A>', s)
        recs.append({
            'path': '/'.join(stack[2:]),
            'url': h.group(1) if h else '',
            'title': html.unescape(t.group(1)) if t else '',
        })

tech = [r for r in recs
        if r['path'].startswith('Bilişim') or r['path'].startswith('Bilim & Düşünce')]

# --- account-gated dashboard -> site root
REWRITE = [
    (r'^https://[a-z0-9-]+\.console\.aws\.amazon\.com/.*',  'https://aws.amazon.com/'),
    (r'^https://dashboard\.composio\.dev/.*',               'https://composio.dev/'),
    (r'^https://app\.privacy\.com/.*',                      'https://privacy.com/'),
    (r'^https://aistudio\.google\.com/.*',                  'https://aistudio.google.com/'),
    (r'^https://feedly\.com/i/.*',                          'https://feedly.com/'),
    (r'^https://huggingbay\.xyz/.*',                        'https://huggingbay.xyz/'),
]

# --- the ones actually dropped
DROP = [
    # Google and on-site search queries - a query, not content
    ('arama-sorgusu', r'google\.[a-z.]+/search|tineye\.com/search|'
                      r'star-history\.com/'),
    # personal file shares - meaningless to anyone else
    ('kisisel-dosya', r'drive\.google\.com|mega\.nz|disk\.yandex|\.notion\.site|'
                      r'seemless\.link'),
    # account-gated social profile or group
    ('sosyal-profil', r'linkedin\.com/(groups|in/|feed|posts)|'
                      r'(^|//|\.)x\.com/|(^|//|\.)twitter\.com/|instagram\.com'),
    # personal hardware and shopping
    ('urun-sayfasi',  r'support\.hp\.com|teknosa\.com|avantajbilisim|robocombo'),
    # dead (confirmed by scanning)
    ('olu',           r'templeos\.org|cslegasse/CS-Tech-Resource-Hub|'
                      r'nxp\.com/company/about-nxp/smarter-world-blog'),
]

kept, dropped = [], []
for r in tech:
    for rx, new in REWRITE:
        if re.match(rx, r['url'], re.I):
            r['url'] = new
            r['rewritten'] = True
            break

    hit = None
    for name, rx in DROP:
        if re.search(rx, r['url'], re.I):
            hit = name
            break
    if hit:
        r['drop_reason'] = hit
        dropped.append(r)
    else:
        kept.append(r)

# clear the duplicates the rewrite creates
seen, uniq = set(), []
for r in kept:
    k = re.sub(r'/$', '', r['url'].lower())
    if k in seen:
        r['drop_reason'] = 'tekrar'
        dropped.append(r)
        continue
    seen.add(k)
    uniq.append(r)
kept = uniq

json.dump(kept, io.open(OUT + r'\kept.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
json.dump(dropped, io.open(OUT + r'\dropped.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)

import collections
print('teknoloji toplam :', len(tech))
print('elenen           :', len(dropped))
for k, v in collections.Counter(d['drop_reason'] for d in dropped).most_common():
    print('   -', k, v)
print('kalan            :', len(kept))
print('youtube          :', sum(1 for r in kept if 'youtube.com' in r['url'] or 'youtu.be' in r['url']))
