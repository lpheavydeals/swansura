"""Back-links to the Gucci + natural body wash guides (user, 16 Nov 2026: 'Published both, add the back-links').
Reads the journal Atom feed (<content> CDATA = stored body), inserts one sentence per link (each anchor must occur
exactly once), writes docs/seo/journal_backlinks_wave11_2026-11-16.json (id + before + after = undo).
Usage: python3 tools/shopify/journal_backlinks_wave11.py <journal.atom>"""
import json, re, sys
IDS = {'oud-perfume-guide': 'gid://shopify/Article/1005508723075', 'mini-perfume-sets-guide': 'gid://shopify/Article/1005662372227',
       'best-perfume-gift-sets-uk-2026': 'gid://shopify/Article/1005550928259', 'how-to-use-body-butter': 'gid://shopify/Article/1005324829059',
       'goat-milk-soap-guide': 'gid://shopify/Article/1005551059331', 'foot-cream-guide': 'gid://shopify/Article/1005664043395'}
G = '<a href="/blogs/journal/gucci-perfume-guide">'
B = '<a href="/blogs/journal/natural-body-wash-guide">'
EDITS = {
 'oud-perfume-guide': [('Expect incense and leather more than sweetness. Shop all <a href="/collections/gucci">Gucci</a>.</p>',
     'Expect incense and leather more than sweetness. Shop all <a href="/collections/gucci">Gucci</a>, or compare it with Bloom, Flora Gorgeous and Guilty in our ' + G + 'Gucci perfume guide</a>.</p>')],
 'mini-perfume-sets-guide': [('Gorgeous Magnolia (dewberries, coconut, magnolia) and Gorgeous Orchid (vanilla, vanilla orchid).</li>',
     'Gorgeous Magnolia (dewberries, coconut, magnolia) and Gorgeous Orchid (vanilla, vanilla orchid). Our ' + G + 'Gucci perfume guide</a> compares the full-size Gucci scents.</li>')],
 'best-perfume-gift-sets-uk-2026': [('50ml eau de parfum with a 50ml body lotion. Lilac, rose and violet over patchouli.</li>',
     '50ml eau de parfum with a 50ml body lotion. Lilac, rose and violet over patchouli. Every Gucci scent we stock is in our ' + G + 'Gucci perfume guide</a>.</li>')],
 'how-to-use-body-butter': [('while skin is still slightly damp. The butter seals in the water on your skin.</li>',
     'while skin is still slightly damp. The butter seals in the water on your skin. For the wash before it, see our ' + B + 'body wash and bath bar guide</a>.</li>')],
 'goat-milk-soap-guide': [('are made with raw shea butter and coconut and olive oils.</li>',
     'are made with raw shea butter and coconut and olive oils. Our ' + B + 'body wash and bath bar guide</a> compares them with Deyga’s other bars and body washes.</li>')],
 'foot-cream-guide': [('<strong>Keep showers warm, not hot,</strong> and do not leave feet soaking for long.</li>',
     '<strong>Keep showers warm, not hot,</strong> and do not leave feet soaking for long. Our ' + B + 'natural body wash guide</a> has a simple shower routine for dry skin.</li>')],
}
feed = open(sys.argv[1], encoding='utf-8').read()
out = []
for e in re.findall(r'<entry>(.*?)</entry>', feed, re.S):
    h = re.search(r'blogs/journal/([a-z0-9-]+)', e).group(1)
    if h not in EDITS: continue
    body = re.search(r'<content[^>]*>\s*<!\[CDATA\[(.*?)\]\]>\s*</content>', e, re.S).group(1).strip()
    after = body
    for old, new in EDITS[h]:
        assert after.count(old) == 1, (h, old[:40], after.count(old))
        after = after.replace(old, new, 1)
    out.append({'handle': h, 'id': IDS[h], 'before': body, 'after': after})
assert len(out) == 6, [o['handle'] for o in out]
json.dump(out, open('docs/seo/journal_backlinks_wave11_2026-11-16.json', 'w'), ensure_ascii=False, indent=1)
print('ok', [(o['handle'], len(o['after']) - len(o['before'])) for o in out])
