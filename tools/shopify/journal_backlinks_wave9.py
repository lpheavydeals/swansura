"""Back-links to the Paco Rabanne + foot cream guides (user, 15 Nov 2026: 'Published both, add the back-links').
Reads the journal Atom feed (<content> CDATA = stored body), inserts one sentence per article (each anchor must occur
exactly once), writes docs/seo/journal_backlinks_wave9_2026-11-15.json (id + before + after = undo).
Usage: python3 tools/shopify/journal_backlinks_wave9.py <journal.atom>"""
import json, re, sys
IDS = {'mini-perfume-sets-guide': 'gid://shopify/Article/1005662372227', 'best-perfume-gift-sets-uk-2026': 'gid://shopify/Article/1005550928259',
       'christmas-gift-guide': 'gid://shopify/Article/1005324665219', 'how-to-use-body-butter': 'gid://shopify/Article/1005324829059',
       'how-to-use-body-scrub': 'gid://shopify/Article/1005324763523', 'stocking-fillers-for-her-under-25': 'gid://shopify/Article/1005550993795'}
P = '<a href="/blogs/journal/paco-rabanne-perfume-guide">'
F = '<a href="/blogs/journal/foot-cream-guide">'
FB = '<a href="/products/foot-butter-40-g-deygas-deep-moisture-butter-for-dry-cracked-heels-rough-feet">Deyga Foot Butter</a>'
EDITS = {
 'mini-perfume-sets-guide': ('<p>For a set anyone can wear, the',
     '<p>To compare 1 Million, Invictus and Phantom before you choose, see our ' + P + 'Paco Rabanne perfume guide</a>.</p>\n<p>For a set anyone can wear, the'),
 'best-perfume-gift-sets-uk-2026': ('More in <a href="/collections/aftershave-gift-sets-for-him">aftershave gift sets for him</a>.</p>',
     'More in <a href="/collections/aftershave-gift-sets-for-him">aftershave gift sets for him</a>. Choosing between 1 Million, Invictus and Phantom? See our ' + P + 'Paco Rabanne perfume guide</a>.</p>'),
 'christmas-gift-guide': ('compares Black Orchid, Noir Extreme and more.</p>',
     'compares Black Orchid, Noir Extreme and more. For 1 Million, Invictus and Phantom, see our ' + P + 'Paco Rabanne perfume guide</a>.</p>'),
 'how-to-use-body-butter': ('apply it at night and pull on cotton socks.',
     'apply it at night and pull on cotton socks. Our ' + F + 'foot cream guide</a> has a simple at-home pedicure.'),
 'how-to-use-body-scrub': ('then ' + FB + ' (£12.99) before socks.',
     'then ' + FB + ' (£12.99) before socks. Our ' + F + 'foot cream guide</a> walks through a full at-home pedicure.'),
 'stocking-fillers-for-her-under-25': ('for feet after a long day in boots.</li>',
     'for feet after a long day in boots. More ideas in our ' + F + 'foot cream guide</a>.</li>'),
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
assert len(out) == 6, [o['handle'] for o in out]
json.dump(out, open('docs/seo/journal_backlinks_wave9_2026-11-15.json', 'w'), ensure_ascii=False, indent=1)
print('ok', [(o['handle'], len(o['after']) - len(o['before'])) for o in out])
