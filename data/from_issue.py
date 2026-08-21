# -*- coding: utf-8 -*-
"""Turns an approved issue into a directory record.

Run by .github/workflows/approve-link.yml when a maintainer puts the
`approved` label on a "Suggest a link" issue. It appends an add(...) call to
part_new.py, rebuilds, and the workflow opens a pull request with the result.

The point is not to save typing. It is that a submission which sits in an
issue is worth nothing until someone transcribes it, and transcription is
exactly the step that gets postponed. This closes that gap while leaving the
final say with a human: the workflow opens a PR, it does not merge one.

Nothing here trusts the issue text. The URL is checked, duplicates are
refused, tags go through the canonical table, and every value is written as a
quoted Python string with no interpolation into code.
"""
import io
import json
import os
import re
import sys

D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, D)

import readlinks                      # noqa: E402
from notes import CATS                # noqa: E402
from tags import normalise            # noqa: E402

PART = os.path.join(D, 'part_new.py')
CAT_BY_EN = dict((c[2], c[0]) for c in CATS)


class Refused(Exception):
    """Something in the issue makes it unusable. The workflow reports it."""


def fields(body):
    """Splits a GitHub issue-form body into {heading: value}.

    Issue forms render as '### Label' followed by the value. Empty optional
    fields come through as the literal '_No response_'.
    """
    out, key, buf = {}, None, []
    for line in (body or '').replace('\r\n', '\n').split('\n'):
        if line.startswith('### '):
            if key:
                out[key] = '\n'.join(buf).strip()
            key, buf = line[4:].strip().lower(), []
        elif key:
            buf.append(line)
    if key:
        out[key] = '\n'.join(buf).strip()
    for k, v in list(out.items()):
        if v == '_No response_':
            out[k] = ''
    return out


def norm(u):
    u = re.sub(r'^https?://', '', u.strip().lower())
    u = re.sub(r'^www\.', '', u)
    return u.rstrip('/')


def parse(body):
    f = fields(body)
    url = f.get('url', '').strip()
    if not re.match(r'^https?://[^\s<>"]+\.[^\s<>"]+$', url):
        raise Refused('URL does not look like a URL: %r' % url[:120])
    if len(url) > 400:
        raise Refused('URL is absurdly long')

    name = ' '.join(f.get('name', '').split())[:80]
    if not name:
        raise Refused('Name is empty')

    what = ' '.join(f.get('what does it do?', '').split())
    diff = ' '.join(f.get('how does it differ?', '').split())
    if not what:
        raise Refused('"What does it do?" is empty')

    cat = CAT_BY_EN.get(f.get('category', '').strip())

    raw = [t.strip() for t in re.split(r'[,;]', f.get('tags (optional)', '')) if t.strip()]
    tg = normalise(raw)[:6]

    return {'url': url, 'name': name, 'cat': cat, 'tags': tg,
            'what': what[:400], 'diff': diff[:400]}


def already_there(url):
    have = set()
    for d in readlinks.read(os.path.dirname(D)):
        k = norm(d['url'])
        have.add(k)
        have.add(re.split(r'[?#]', k)[0].rstrip('/'))
    k = norm(url)
    return k in have or re.split(r'[?#]', k)[0].rstrip('/') in have


def py(s):
    """A Python string literal. json.dumps gives valid, escaped output."""
    return json.dumps(s, ensure_ascii=False)


def render(rec, issue):
    tr = rec['what'] + ((' ' + rec['diff']) if rec['diff'] else '')
    body = [
        '',
        '    # from issue #%d -- description needs a pass: the submitter wrote'
        % issue,
        '    # one language and one voice; both fields below carry the same text.',
        '    add(%s, %s,' % (py(rec['url']), py(rec['name'])),
        '        %s,' % py(rec['tags']).replace('"', "'"),
        '        %s,' % py(tr),
        '        %s%s' % (py(tr), ',' if rec['cat'] else ')'),
    ]
    if rec['cat']:
        body.append('        %s)' % py(rec['cat']))
    return '\n'.join(body) + '\n'


def append(text):
    src = io.open(PART, encoding='utf-8').read().rstrip('\n')
    io.open(PART, 'w', encoding='utf-8', newline='\n').write(src + '\n' + text)


def main():
    body = os.environ.get('ISSUE_BODY', '')
    issue = int(os.environ.get('ISSUE_NUMBER', '0') or 0)
    try:
        rec = parse(body)
        if already_there(rec['url']):
            raise Refused('This URL is already in the directory')
    except Refused as e:
        io.open(os.path.join(D, '..', 'issue-error.txt'), 'w',
                encoding='utf-8').write(str(e))
        print('refused:', e)
        return 1

    append(render(rec, issue))
    print('appended to part_new.py:', rec['name'], '->', rec['url'])
    print('category:', rec['cat'] or '(from bookmark path / fallback)')
    print('tags    :', rec['tags'] or '(none)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
