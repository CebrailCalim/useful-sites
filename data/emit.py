# -*- coding: utf-8 -*-
"""The static output that crawlers and JavaScript-less visitors get.

The app draws itself entirely from links.js, and that has a cost: the
<main> Google sees is empty. Not one word of 717 descriptions is indexed,
which for a link directory is close to not existing.

This closes that gap. Every category gets an HTML page carrying the real
text; the app still behaves as a single page, but a crawler or a visitor
without JavaScript finds something readable.

Writes:
  robots.txt      sitemap pointer
  sitemap.xml     index + category pages
  feed.xml        newest entries (Atom) -- how anyone follows the directory
  k/<category>.html      Turkish
  k/en/<category>.html   English
"""
import io
import os
import datetime

SITE = 'https://latifkedi.github.io/useful-sites'
FEED_N = 40


def esc(s):
    return (str(s).replace('&', '&amp;').replace('<', '&lt;')
            .replace('>', '&gt;').replace('"', '&quot;'))


def _iso(ts):
    return datetime.datetime.utcfromtimestamp(ts).strftime('%Y-%m-%dT%H:%M:%SZ')


def _day(ts):
    return datetime.datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d')


# The static pages carry none of the app shell; their only job is to be
# readable. Same tokens, same typography, no JavaScript.
STYLE = """:root{--bg:#fcfbf9;--fg:#191817;--dim:#57544e;--faint:#8b8780;
--rule:#e4e0d8;--accent:#a8451f;--accent-soft:#f6ece6}
@media (prefers-color-scheme:dark){:root{--bg:#1a1c20;--fg:#e2e0da;--dim:#a3a09a;
--faint:#75726c;--rule:#33363c;--accent:#e78b62;--accent-soft:#2a211c}}
*{box-sizing:border-box}
body{margin:0 auto;padding:0 24px 72px;max-width:820px;background:var(--bg);color:var(--fg);
font:17px/1.62 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif}
a{color:var(--fg)}
header{padding:48px 0 20px;border-bottom:1px solid var(--rule)}
.up{font:12.5px/1 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;color:var(--dim);
text-decoration:none;letter-spacing:.04em}
.up:hover{color:var(--accent)}
h1{font-size:27px;letter-spacing:-.018em;margin:16px 0 0}
.intro{color:var(--dim);font-size:16px;line-height:1.7;margin:12px 0 0;max-width:66ch}
.n{font:12.5px/1 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;color:var(--faint);
margin-top:10px;display:block}
article{padding:16px 0 16px 14px;border-left:2px solid var(--rule);margin:22px 0 0}
article h2{font-size:17px;font-weight:600;margin:0;display:inline}
article h2 a{text-decoration:none}
article h2 a:hover{color:var(--accent)}
.host{font:12px ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;color:var(--faint);margin-left:8px}
p.d{color:var(--dim);font-size:15.5px;line-height:1.7;margin:7px 0 0}
p.t{font:12px ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;color:var(--faint);margin:8px 0 0}
nav.other{margin:56px 0 0;padding-top:22px;border-top:1px solid var(--rule);
font-size:15px;line-height:2}
nav.other a{color:var(--dim);text-decoration:none;margin-right:18px}
nav.other a:hover{color:var(--accent)}
footer{margin-top:40px;padding-top:20px;border-top:1px solid var(--rule);
color:var(--faint);font-size:14px;line-height:1.8}
footer a{color:var(--dim)}"""

PAGE = """<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — {site_name}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{site_name}">
<meta property="og:title" content="{title} — {site_name}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{site}/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="alternate" type="application/atom+xml" title="{site_name}" href="{site}/feed.xml">
<link rel="alternate" hreflang="tr" href="{alt_tr}">
<link rel="alternate" hreflang="en" href="{alt_en}">
<link rel="alternate" hreflang="x-default" href="{alt_tr}">
<style>{style}</style>
</head>
<body>
<header>
<a class="up" href="{home}">← {site_name}</a>
<h1>{title}</h1>
<p class="intro">{intro}</p>
<span class="n">{count} {word_links}</span>
</header>
<main>
{items}
</main>
<nav class="other">{others}</nav>
<footer>
{foot}
</footer>
</body>
</html>
"""


def _host(u):
    h = u.split('//', 1)[-1].split('/', 1)[0]
    return h[4:] if h.startswith('www.') else h


def _item(d, taglbl, desc, li):
    tags = ', '.join(taglbl.get(t, [t, t])[li] for t in d.get('tags', [])[:6])
    return (
        '<article>\n'
        '<h2><a href="%s" rel="noopener nofollow">%s</a></h2>'
        '<span class="host">%s</span>\n'
        '<p class="d">%s</p>\n'
        '%s'
        '</article>'
    ) % (esc(d['url']), esc(d['name']), esc(_host(d['url'])), esc(desc),
         ('<p class="t">%s</p>\n' % esc(tags)) if tags else '')


# Turkish and English differ only in the words around the list, so the two
# runs share everything except this table. A crawler arriving from an English
# query used to land on a Turkish page; hreflang now pairs them up.
LANGS = {
    'tr': {
        'code': 'tr', 'li': 0, 'ci': 1, 'dir': '',
        'name': 'Kullanışlı Siteler', 'links': 'bağlantı',
        'foot': ('Bu sayfa dizinin {t} bölümünün metin hâli. Arama, etiket süzgeci '
                 've İngilizce açıklamalar için <a href="{s}/?cat={k}">dizine dön</a>. '
                 '<a href="{s}/k/en/{k}.html">In English</a>'),
    },
    'en': {
        'code': 'en', 'li': 1, 'ci': 2, 'dir': 'en/',
        'name': 'Useful Sites', 'links': 'links',
        'foot': ('The plain-text edition of the {t} section. For search, tag '
                 'filtering and Turkish descriptions, <a href="{s}/?cat={k}">go to '
                 'the directory</a>. <a href="{s}/k/{k}.html">Türkçe</a>'),
    },
}


def write_all(core, cats, intros, taglbl, out_dir, en_desc):
    """core: the record list as written to links.js. cats: [(key, tr, en)].

    en_desc is the parallel list of English descriptions, so the English pages
    carry English text rather than the Turkish original with an English shell.
    """
    written = []
    for lang, L in sorted(LANGS.items()):
        kdir = os.path.join(out_dir, 'k', L['dir'].strip('/')) if L['dir'] \
            else os.path.join(out_dir, 'k')
        if not os.path.isdir(kdir):
            os.makedirs(kdir)

        order = [c[0] for c in cats]
        label = dict((c[0], c[L['ci']]) for c in cats)
        by_cat = {}
        for i, d in enumerate(core):
            by_cat.setdefault(d['cat'], []).append((i, d))

        for k in order:
            rows = by_cat.get(k)
            if not rows:
                continue
            intro = (intros.get(k) or ('', ''))[L['li']]
            others = ' '.join(
                '<a href="%s.html">%s</a>' % (esc(o), esc(label[o]))
                for o in order if o != k and by_cat.get(o))
            canon = '%s/k/%s%s.html' % (SITE, L['dir'], k)
            desc = (intro or label[k])[:180]
            items = []
            for i, d in rows:
                text = en_desc[i] if L['li'] == 1 and i < len(en_desc) else d['tr']
                items.append(_item(d, taglbl, text, L['li']))
            io.open(os.path.join(kdir, k + '.html'), 'w',
                    encoding='utf-8', newline='\n').write(PAGE.format(
                        lang=L['code'], site_name=esc(L['name']),
                        title=esc(label[k]), desc=esc(desc), canon=canon, site=SITE,
                        home=SITE + '/', style=STYLE, intro=esc(intro),
                        count=len(rows), word_links=esc(L['links']), key=esc(k),
                        alt_tr='%s/k/%s.html' % (SITE, k),
                        alt_en='%s/k/en/%s.html' % (SITE, k),
                        items='\n'.join(items), others=others,
                        foot=L['foot'].format(t=esc(label[k]), s=SITE, k=esc(k))))
            if lang == 'tr':
                written.append(k)

    _sitemap(written, out_dir)
    _robots(out_dir)
    _feed(core, dict((c[0], c[1]) for c in cats), out_dir)
    return written


def _sitemap(keys, out_dir):
    today = datetime.date.today().isoformat()
    urls = ([(SITE + '/', '1.0')]
            + [('%s/k/%s.html' % (SITE, k), '0.7') for k in keys]
            + [('%s/k/en/%s.html' % (SITE, k), '0.6') for k in keys])
    body = '\n'.join(
        '  <url><loc>%s</loc><lastmod>%s</lastmod><priority>%s</priority></url>'
        % (esc(u), today, p) for u, p in urls)
    io.open(os.path.join(out_dir, 'sitemap.xml'), 'w',
            encoding='utf-8', newline='\n').write(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + body + '\n</urlset>\n')


def _robots(out_dir):
    io.open(os.path.join(out_dir, 'robots.txt'), 'w',
            encoding='utf-8', newline='\n').write(
        'User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n' % SITE)


def _feed(core, label, out_dir):
    """Newest entries. As the directory grows this is the only sane way
    for anyone to follow it."""
    rows = sorted(core, key=lambda d: -d.get('added', 0))[:FEED_N]
    # <updated> comes from the newest entry, not from the clock. Using the
    # clock made every build produce a feed.xml diff even when no link had
    # changed, which buries real changes in noise.
    now = _iso(rows[0].get('added', 0) if rows else 0)
    parts = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<feed xmlns="http://www.w3.org/2005/Atom">',
             '<title>Kullanışlı Siteler</title>',
             '<subtitle>Yazılım, yapay zeka, güvenlik ve bilim üzerine '
             'açıklamalı bağlantı dizini</subtitle>',
             '<link href="%s/feed.xml" rel="self"/>' % SITE,
             '<link href="%s/"/>' % SITE,
             '<id>%s/</id>' % SITE,
             '<updated>%s</updated>' % now]
    for d in rows:
        parts.append(
            '<entry>\n'
            '  <title>%s</title>\n'
            '  <link href="%s"/>\n'
            '  <id>%s</id>\n'
            '  <updated>%s</updated>\n'
            '  <category term="%s"/>\n'
            '  <summary>%s</summary>\n'
            '</entry>' % (
                esc(d['name']), esc(d['url']), esc(d['url']),
                _iso(d.get('added', 0)), esc(label.get(d['cat'], d['cat'])),
                esc(d['tr'])))
    parts.append('</feed>')
    io.open(os.path.join(out_dir, 'feed.xml'), 'w',
            encoding='utf-8', newline='\n').write('\n'.join(parts) + '\n')
