"""Back-links to the toner + mini perfume sets guides (user, 14 Nov 2026: 'Published v2, check it live and add the back-links').
Reads the journal Atom feed (CDATA body = stored body, strip whitespace), inserts one sentence per article
(each anchor must occur exactly once), writes docs/seo/journal_backlinks_wave7_2026-11-14.json (id + before + after = undo).
Usage: python3 tools/shopify/journal_backlinks_wave7.py <journal.atom>"""
import json, re, sys
IDS = {'face-wash-for-your-skin-type': 'gid://shopify/Article/1005503250819', 'face-serum-guide': 'gid://shopify/Article/1005509247363',
       'moisturiser-for-your-skin-type': 'gid://shopify/Article/1005503971715', 'best-perfume-gift-sets-uk-2026': 'gid://shopify/Article/1005550928259',
       'stocking-fillers-for-her-under-25': 'gid://shopify/Article/1005550993795', 'christmas-gift-guide': 'gid://shopify/Article/1005324665219'}
T = '<a href="/blogs/journal/toner-for-dry-skin">'
M = '<a href="/blogs/journal/mini-perfume-sets-guide">'
EDITS = {
 'face-wash-for-your-skin-type': ('Add a <a href="/collections/toner">toner</a> if you like one, then',
     'Add a <a href="/collections/toner">toner</a> if you like one (see ' + T + 'how to choose a toner</a>), then'),
 'face-serum-guide': ('of a water-based serum to slightly damp skin and press it in.',
     'of a water-based serum to slightly damp skin and press it in. A toner after cleansing leaves skin slightly damp: see our ' + T + 'toner guide</a>.'),
 'moisturiser-for-your-skin-type': ('<strong>Apply serum,</strong> if you use one, to slightly damp skin.',
     '<strong>Apply serum,</strong> if you use one, to slightly damp skin. A toner after cleansing gives that first damp layer: see ' + T + 'toner for dry skin</a>.'),
 'best-perfume-gift-sets-uk-2026': ('See them all in <a href="/collections/perfume-gift-sets-for-her">perfume gift sets for her</a>.',
     'See them all in <a href="/collections/perfume-gift-sets-for-her">perfume gift sets for her</a>. What is inside each one is in our ' + M + 'mini perfume sets guide</a>.'),
 'stocking-fillers-for-her-under-25': ('More in <a href="/collections/travel-size-minis">travel size and mini perfumes</a>.',
     'More in <a href="/collections/travel-size-minis">travel size and mini perfumes</a>. Our ' + M + 'mini perfume sets guide</a> lists what is inside each set.'),
 'christmas-gift-guide': ('Wondering what the labels mean?',
     'For what is inside each miniature set, see our ' + M + 'mini perfume sets guide</a>. Wondering what the labels mean?'),
}
feed = open(sys.argv[1], encoding='utf-8').read()
out = []
for entry in re.findall(r'<entry>(.*?)</entry>', feed, re.S):
    m = re.search(r'blogs/journal/([a-z0-9-]+)', entry)
    if not m or m.group(1) not in EDITS: continue
    h = m.group(1)
    c = re.search(r'<content[^>]*>\s*<!\[CDATA\[(.*?)\]\]>\s*</content>', entry, re.S)
    body = c.group(1).strip()
    old, new = EDITS[h]
    assert body.count(old) == 1, (h, body.count(old))
    assert 'toner-for-dry-skin' not in body or 'mini' in h or h in ('best-perfume-gift-sets-uk-2026','stocking-fillers-for-her-under-25','christmas-gift-guide'), h
    out.append({'handle': h, 'id': IDS[h], 'before': body, 'after': body.replace(old, new, 1)})
assert len(out) == 6, [o['handle'] for o in out]
json.dump(out, open('docs/seo/journal_backlinks_wave7_2026-11-14.json', 'w'), ensure_ascii=False, indent=1)
print('ok', [o['handle'] for o in out])
