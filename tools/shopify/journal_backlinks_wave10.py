"""Back-links to the Mugler + lip balm guides (user, 15 Nov 2026: 'Published both, add the back-links').
Reads the journal Atom feed (<content> CDATA = stored body), inserts one sentence per link (each anchor must occur
exactly once), writes docs/seo/journal_backlinks_wave10_2026-11-15.json (id + before + after = undo).
Usage: python3 tools/shopify/journal_backlinks_wave10.py <journal.atom>"""
import json, re, sys
IDS = {'mini-perfume-sets-guide': 'gid://shopify/Article/1005662372227', 'best-perfume-gift-sets-uk-2026': 'gid://shopify/Article/1005550928259',
       'christmas-gift-guide': 'gid://shopify/Article/1005324665219', 'how-to-use-lip-scrub': 'gid://shopify/Article/1005468221827',
       'stocking-fillers-for-her-under-25': 'gid://shopify/Article/1005550993795'}
M = '<a href="/blogs/journal/mugler-perfume-guide">'
L = '<a href="/blogs/journal/lip-balm-guide">'
EDITS = {
 'mini-perfume-sets-guide': [('Browse every <a href="/collections/travel-size-minis">travel-size mini</a>.</p>',
     'Browse every <a href="/collections/travel-size-minis">travel-size mini</a>, or see the four 10ml Mugler Colognes in our ' + M + 'Mugler perfume guide</a>.</p>')],
 'best-perfume-gift-sets-uk-2026': [('What is inside each one is in our <a href="/blogs/journal/mini-perfume-sets-guide">mini perfume sets guide</a>.',
     'What is inside each one is in our <a href="/blogs/journal/mini-perfume-sets-guide">mini perfume sets guide</a>. For Mugler Alien and Angel, see our ' + M + 'Mugler perfume guide</a>.')],
 'christmas-gift-guide': [
     ('or read our <a href="/blogs/journal/best-perfume-gift-sets-uk-2026">perfume gift sets guide</a>.</p>',
      'or read our <a href="/blogs/journal/best-perfume-gift-sets-uk-2026">perfume gift sets guide</a>. Our ' + M + 'Mugler perfume guide</a> compares Alien and Angel.</p>'),
     ('Giving lip care? See <a href="/blogs/journal/how-to-use-lip-scrub">how to use a lip scrub</a>.</p>',
      'Giving lip care? See <a href="/blogs/journal/how-to-use-lip-scrub">how to use a lip scrub</a> and our ' + L + 'lip balm guide</a>.</p>')],
 'how-to-use-lip-scrub': [('<p>A scrub without a balm is only half the job. Choose the balm by what you want from it.</p>',
     '<p>A scrub without a balm is only half the job. Choose the balm by what you want from it; our ' + L + 'lip balm guide</a> compares every type.</p>')],
 'stocking-fillers-for-her-under-25': [('Our <a href="/blogs/journal/how-to-use-lip-scrub">lip scrub guide</a> explains how to use them, and every balm',
     'Our <a href="/blogs/journal/how-to-use-lip-scrub">lip scrub guide</a> explains how to use them, our ' + L + 'lip balm guide</a> compares SPF, tinted and natural balms, and every balm')],
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
assert len(out) == 5, [o['handle'] for o in out]
json.dump(out, open('docs/seo/journal_backlinks_wave10_2026-11-15.json', 'w'), ensure_ascii=False, indent=1)
print('ok', [(o['handle'], len(o['after']) - len(o['before'])) for o in out])
