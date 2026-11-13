#!/usr/bin/env python3
"""Store copy for the £5-off-over-£70 offer now being code SAVE5 (user, 12-13 Nov 2026: 'auto apply … removed … manual
apply code'; 'Yes, go ahead' to rewording the store text).

  save5_copy_2026-11-13.py <collections_all.json> <pages_articles.json> <out.json>
Inputs = Admin reads (collections: id/handle/seo/custom.seo_copy/custom.faq; pages + articles: id/handle/body/custom.faq).
Output = list of changes {kind, id, handle, field, before, after} (= undo list) + the mutation batches.
"""
import json, sys

REPL = [  # (old, new) applied in this order, exact text
    ('and orders over £70 also get £5 off at checkout', 'and orders over £70 get £5 off with code SAVE5 at checkout'),
    ('and orders over £70 also get £5 off, applied automatically at checkout,', 'and orders over £70 get £5 off with code SAVE5 at checkout,'),
    ('and orders over £70 also get £5 off.', 'and orders over £70 get £5 off with code SAVE5.'),
    ('and orders over £70 get £5 off at checkout', 'and orders over £70 get £5 off with code SAVE5 at checkout'),
    ('and orders over £70 get free delivery plus £5 off.', 'and orders over £70 get free delivery plus £5 off with code SAVE5.'),
    ('<strong>Free</strong>, plus £5 off the order', '<strong>Free</strong>, plus £5 off the order with code SAVE5'),
    ('<h2>Spend £70: free delivery + £5 off</h2>', '<h2>Spend £70: free delivery + £5 off with code SAVE5</h2>'),
    ('Spend £70 or more and we take £5 off your order automatically at checkout, on top of free delivery. No code needed.',
     'Spend £70 or more and enter code SAVE5 in your bag or at checkout for £5 off your order, on top of free delivery.'),
    ('Orders under £40 ship from £2.', 'Orders under £40 ship for £1.99.'),
]
SEO_BF = ('Free delivery over £40, £5 off over £70.', 'Free delivery over £40, £5 off over £70 with SAVE5.')


def fix(s):
    out = s
    for a, b in REPL:
        out = out.replace(a, b)
    return out


def main(colf, paf, outf):
    cols = json.load(open(colf))
    pa = json.load(open(paf))['data']
    ch = []
    for c in cols:
        for field, key in [('custom.faq', 'faq'), ('custom.seo_copy', 'copy')]:
            v = (c.get(key) or {}).get('value')
            if v and fix(v) != v:
                ch.append({'kind': 'collection', 'id': c['id'], 'handle': c['handle'], 'field': field, 'before': v, 'after': fix(v)})
        d = c['seo']['description'] or ''
        if SEO_BF[0] in d:
            nd = d.replace('100% authentic and shipped from the UK.', '100% authentic, shipped from the UK.').replace(*SEO_BF)
            assert len(nd) <= 155, len(nd)
            ch.append({'kind': 'collection', 'id': c['id'], 'handle': c['handle'], 'field': 'seo', 'title': c['seo']['title'], 'before': d, 'after': nd})
    for kind in ['pages', 'articles']:
        for n in pa[kind]['nodes']:
            b = n.get('body') or ''
            if fix(b) != b:
                ch.append({'kind': kind[:-1], 'id': n['id'], 'handle': n['handle'], 'field': 'body', 'before': b, 'after': fix(b)})
            f = (n.get('faq') or {}).get('value')
            if f and fix(f) != f:
                ch.append({'kind': kind[:-1], 'id': n['id'], 'handle': n['handle'], 'field': 'custom.faq', 'before': f, 'after': fix(f)})
    # every offer mention must now name the code
    import re
    for x in ch:
        for m in re.finditer(r'£5 off[^.<"\]]*', x['after']):
            assert 'SAVE5' in m.group(0) or 'SAVE5' in x['after'][m.start() - 60:m.end() + 40], (x['handle'], m.group(0))
    json.dump(ch, open(outf, 'w'), ensure_ascii=False, indent=1)
    from collections import Counter
    print(len(ch), Counter((x['kind'], x['field']) for x in ch))


if __name__ == '__main__':
    main(*sys.argv[1:])
