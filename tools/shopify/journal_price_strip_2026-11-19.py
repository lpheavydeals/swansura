#!/usr/bin/env python3
"""Remove product prices from Journal article text (user, 19 Nov 2026: 'Go with b, remove the prices
from the articles'): prices are uploaded weekly, so prices written into articles go stale.

Kept: thresholds and offers (free UK delivery over £40, £5 off over £70 with SAVE5, 'under £25',
'gifts under £50', price bands '£25 to £50'). Removed: product prices and per-gram/ml prices.

Usage: journal_price_strip_2026-11-19.py <admin_articles.json> <out plan.json>
  admin_articles.json = Admin query articles{id handle body summary seo:global.description_tag faq:custom.faq}
Plan = [{id, handle, body:[before,after], faq:[before,after]?}] (before = undo).
"""
import json, re, sys

X = r'£\d+(?:\.\d{1,2})?(?![.\d]\d)'
# a £ amount is a threshold/offer when one of these words comes just before it, or 'off' just after
PROT_BEFORE = re.compile(r'(over|under|below|above|than|spend(?:ing)?|to|from|upto|up to|and|or|budget of|around|about)\s*$', re.I)

RULES = [
    # (£X) / (from £X) / (£X each)  -> removed
    (r'\s*\((?:from )?' + X + r'(?: each| for (?:two|a pack of two|the pair))?\)', ''),
    # (£X, 100ml) / (from £X, 60ml) -> (100ml)
    (r'\((?:from )?' + X + r'(?: each)?,\s*', '('),
    # ', £X)' inside brackets: (100ml, £X) -> (100ml)
    (r',\s*(?:from )?' + X + r'\)', ')'),
]
POST = [   # (handle, old, new) hand fixes on the result, after reading every remaining price
('deyga-beetroot-lip-balm-stick-or-pot', 'The pot works out at about £1.10 per gram and the stick at about £2.54 per gram, so the pot is the better value and the stick is the tidier one to carry.', 'Gram for gram the pot is the better value, and the stick is the tidier one to carry.'),
('deyga-beetroot-lip-balm-stick-or-pot', '<strong>Price:</strong> pot £10.99 for 10g (about £1.10/g); stick £13.99 for 5.5g (about £2.54/g). Gram for gram the stick costs roughly 2.3 times as much.', '<strong>Value:</strong> the pot holds 10g and the stick 5.5g, and gram for gram the pot is the better value.'),
('deyga-beetroot-lip-balm-stick-or-pot', '<strong>Packs of two:</strong> two pots are £20.99 (about £1.05/g) and two sticks £26.99 (about £2.45/g).', '<strong>Packs of two:</strong> both also come as a pack of two.'),
('deyga-beetroot-lip-balm-stick-or-pot', 'Mint Lip Scrub with the Classic pot, less than the £23.98 they cost separately.', 'Mint Lip Scrub with the Classic pot.'),
('vilvah-milk-drops-serum', 'It comes in 20ml (about £1.10 per ml) and 40ml (about £0.77 per ml), so the 40ml is the better value if you use it daily.', 'It comes in 20ml and 40ml, and the 40ml costs less per ml if you use it daily.'),
('vilvah-milk-drops-serum', '<strong>40ml</strong>: about £0.77 per ml against £1.10 for the 20ml, and less than two 20ml bottles.', '<strong>40ml</strong>: costs less per ml than the 20ml, and less than two 20ml bottles.'),
('stocking-fillers-for-her-under-25', 'comes to about £43 to £51 with the picks above. That also takes the order over £40, so UK delivery is free.', 'comes to around £50 with the picks above, which also takes the order over £40, so UK delivery is free.'),
('narciso-rodriguez-perfume-guide', 'Both are 10ml eau de parfums at £25.99:', 'Both are 10ml eau de parfums:'),
('narciso-rodriguez-perfume-guide', 'the 10ml sizes at £25.99 let you', 'the 10ml sizes let you'),
('mugler-perfume-guide', 'in 10ml sprays at £14.99 each, a low-cost way', 'in 10ml sprays, a low-cost way'),
('versace-perfume-guide', 'start with a 5ml miniature at £13.99.', 'start with a 5ml miniature.'),
('deyga-or-vilvah', 'it makes an easy first try at under £11.', 'it makes an easy first try.'),
('deyga-organics-uk', 'compares the two versions and the price per gram.', 'compares the two versions and which is better value.'),
('vilvah-milk-drops-serum', 'It comes in 20ml and 40ml, and the 40ml costs less per ml if you use it daily.', 'It comes in 20ml and 40ml; if you use it daily, the 40ml costs less per ml.'),
]
# SEO descriptions (global.description_tag) and summaries that promised prices
META = [
('oud-perfume-guide', 'seo', 'Notes, prices, tips.', 'Notes and tips.'),
('mini-perfume-sets-guide', 'seo', 'with notes, sizes and prices, plus', 'with notes and sizes, plus'),
('al-haramain-amber-oud-editions', 'seo', 'the notes, sizes and prices, and', 'the notes and sizes, and'),
('deyga-beetroot-lip-balm-stick-or-pot', 'seo', 'the price per gram,', 'which is better value,'),
('deyga-beetroot-lip-balm-stick-or-pot', 'summary', 'the price per gram,', 'which is better value,'),
]


def strip(t):
    for p, r in RULES:
        t = re.sub(p, r, t)
    return t


def left(t):
    """£ amounts still in the text that are not thresholds."""
    out = []
    for m in re.finditer(X, t):
        before = re.sub(r'<[^>]+>', '', t[max(0, m.start() - 40):m.start()])
        after = t[m.end():m.end() + 6]
        if PROT_BEFORE.search(before) or re.match(r'\s*off', after):
            continue
        out.append(m)
    return out


def build(nodes):
    plan = []
    for n in nodes:
        rec = {'id': n['id'], 'handle': n['handle']}
        b1 = strip(n['body'])
        for h, o, nw in POST:
            if h == n['handle']:
                assert o in b1, (h, o)
                b1 = b1.replace(o, nw)
        if b1 != n['body']:
            rec['body'] = [n['body'], b1]
        f0 = (n.get('faq') or {}).get('value')
        if f0:
            f1 = strip(f0)
            for h, o, nw in POST:
                if h == n['handle'] + ':faq':
                    assert o in f1, (h, o)
                    f1 = f1.replace(o, nw)
            if f1 != f0:
                rec['faq'] = [f0, f1]
        for h, k, o, nw in META:
            if h == n['handle']:
                v0 = (n.get('seo') or {}).get('value') if k == 'seo' else n.get('summary')
                assert o in v0, (h, k, o)
                rec[k] = [v0, v0.replace(o, nw)]
        if len(rec) > 2:
            plan.append(rec)
    return plan


if __name__ == '__main__':
    nodes = json.load(open(sys.argv[1]))['data']['articles']['nodes']
    plan = build(nodes)
    json.dump(plan, open(sys.argv[2], 'w'), ensure_ascii=False, indent=1)
    by = {r['handle']: r for r in plan}
    n_left = 0
    for n in nodes:
        for key, cur in (('body', by.get(n['handle'], {}).get('body', [None, n['body']])[1]),
                         ('faq', by.get(n['handle'], {}).get('faq', [None, (n.get('faq') or {}).get('value') or ''])[1])):
            for m in left(cur):
                n_left += 1
                ctx = re.sub(r'<[^>]+>', '', cur[max(0, m.start() - 140):m.end() + 60]).replace('\n', ' ')
                print(f'LEFT {n["handle"]}:{key} | ...{ctx}...')
    print(len(plan), 'articles changed;', n_left, 'prices left', file=sys.stderr)
