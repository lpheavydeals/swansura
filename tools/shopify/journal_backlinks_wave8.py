"""Back-links to the frizzy hair + Al Haramain Amber Oud guides (user, 14 Nov 2026: 'Made them visible now, add the back-links').
Reads the journal Atom feed (<content> CDATA = stored body), inserts one sentence per article (each anchor must occur
exactly once), writes docs/seo/journal_backlinks_wave8_2026-11-14.json (id + before + after = undo).
Usage: python3 tools/shopify/journal_backlinks_wave8.py <journal.atom>"""
import json, re, sys
IDS = {'natural-shampoo-guide': 'gid://shopify/Article/1005503283587', 'hair-oil-guide': 'gid://shopify/Article/1005324861827',
       'oud-perfume-guide': 'gid://shopify/Article/1005508723075', 'lattafa-khamrah-qahwa-arabian-perfume': 'gid://shopify/Article/1005468254595',
       'layer-oud-with-body-butter': 'gid://shopify/Article/1005307855235'}
F = '<a href="/blogs/journal/frizzy-hair-serum-oil-mask">'
A = '<a href="/blogs/journal/al-haramain-amber-oud-editions">'
EDITS = {
 'natural-shampoo-guide': ('read our <a href="/blogs/journal/hair-oil-guide">guide to hair oils</a>.',
     'read our <a href="/blogs/journal/hair-oil-guide">guide to hair oils</a>. For a full frizz routine, see ' + F + 'frizzy hair: serum, oil or mask</a>.'),
 'hair-oil-guide': ('Between washes, smooth a single drop over the ends',
     'Our ' + F + 'frizzy hair guide</a> explains when to reach for an oil, a serum or a mask. Between washes, smooth a single drop over the ends'),
 'oud-perfume-guide': ("Al Haramain's Amber Oud range is a popular Arabian line, but read the notes: not every edition is built around oud.",
     "Al Haramain's Amber Oud range is a popular Arabian line, but read the notes: not every edition is built around oud. Our " + A + "Amber Oud editions guide</a> compares them all."),
 'lattafa-khamrah-qahwa-arabian-perfume': ('Browse all <a href="/collections/arabian-perfume">Arabian perfume</a> and',
     'Every Al Haramain Amber Oud edition is compared in our ' + A + 'Amber Oud guide</a>. Browse all <a href="/collections/arabian-perfume">Arabian perfume</a> and'),
 'layer-oud-with-body-butter': ('For Tom Ford Oud Wood, Gucci Intense Oud and other designer ouds, see our',
     'To pick an Amber Oud edition, see ' + A + 'every Al Haramain Amber Oud edition compared</a>. For Tom Ford Oud Wood, Gucci Intense Oud and other designer ouds, see our'),
}
feed = open(sys.argv[1], encoding='utf-8').read()
out = []
for e in re.findall(r'<entry>(.*?)</entry>', feed, re.S):
    h = re.search(r'blogs/journal/([a-z0-9-]+)', e).group(1)
    if h not in EDITS: continue
    body = re.search(r'<content[^>]*>\s*<!\[CDATA\[(.*?)\]\]>\s*</content>', e, re.S).group(1).strip()
    old, new = EDITS[h]
    assert body.count(old) == 1, (h, body.count(old))
    out.append({'handle': h, 'id': IDS[h], 'before': body, 'after': body.replace(old, new, 1)})
assert len(out) == 5, [o['handle'] for o in out]
json.dump(out, open('docs/seo/journal_backlinks_wave8_2026-11-14.json', 'w'), ensure_ascii=False, indent=1)
print('ok', [(o['handle'], len(o['after']) - len(o['before'])) for o in out])
