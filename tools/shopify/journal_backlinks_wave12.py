"""Wave 12 back-links (16 Nov 2026): the 4 Deyga/Vilvah brand guides.

Usage: python3 journal_backlinks_wave12.py <journal.atom> <admin.json>
admin.json = {"articles": {handle: body}, "collections": {handle: {id, metafield_id, value}}}
(articles older than the Atom feed's 30 entries are read from Admin).
Writes docs/seo/journal_backlinks_wave12_2026-11-16.json (before/after = undo).
"""
import json, re, sys
J = '/blogs/journal/'
BEET = f'<a href="{J}deyga-beetroot-lip-balm-stick-or-pot">'
DOU = f'<a href="{J}deyga-organics-uk">'
MD = f'<a href="{J}vilvah-milk-drops-serum">'
VUK = f'<a href="{J}vilvah-uk">'
IDS = {'deyga-or-vilvah': 1005307822467, 'lip-balm-guide': 1005690519939,
       'indian-skincare-uk-guide': 1005560562051, 'face-serum-guide': 1005509247363,
       'goat-milk-soap-guide': 1005551059331}
EDITS = {
 'deyga-or-vilvah': [
  ("one of the brand's top searches in the UK.</p>",
   f"one of the brand's top searches in the UK. Our {MD}Vilvah Milk Drops guide</a> goes through its ingredients and the 20ml and 40ml sizes.</p>"),
  ("it makes an easy first try at under £11.</p>",
   f"it makes an easy first try at under £11. Not sure whether to buy the pot or the stick? Read {BEET}Deyga Beetroot Lip Balm: stick or pot</a>.</p>"),
  ("<a href=\"/collections/vilvah\">all Vilvah</a> products.</p>",
   f"<a href=\"/collections/vilvah\">all Vilvah</a> products. New to either brand? Start with our {DOU}Deyga Organics guide</a> or our {VUK}Vilvah guide</a>.</p>"),
 ],
 'lip-balm-guide': [
  ("(from £13.99, 5.5g) for your pocket.</li>",
   f"(from £13.99, 5.5g) for your pocket. We compare the two in {BEET}Deyga Beetroot Lip Balm: stick or pot</a>.</li>"),
 ],
 'indian-skincare-uk-guide': [
  ("Swansura is an official UK partner of both Deyga and Vilvah, so every product is genuine.</li>",
   f"Swansura is an official UK partner of both Deyga and Vilvah, so every product is genuine. Read more in our brand guides: {DOU}Deyga Organics in the UK</a> and {VUK}Vilvah in the UK</a>.</li>"),
 ],
 'face-serum-guide': [
  ("Apply either to slightly damp skin.</p>",
   f"Apply either to slightly damp skin. Our {MD}Vilvah Milk Drops guide</a> covers its full ingredient list and which size to buy.</p>"),
 ],
 'goat-milk-soap-guide': [
  ("castor oil a cushioned foam.</p>",
   f"castor oil a cushioned foam. For the rest of the brand, see our {VUK}Vilvah guide</a>.</p>"),
 ],
}
COLL = {
 'vilvah': [("You will also find it in the Milk Face Kit (£45.99) with the Milk Mud Mask.",
   f"You will also find it in the Milk Face Kit (£45.99) with the Milk Mud Mask. Our {MD}Vilvah Milk Drops guide</a> explains what is in it and which size to buy, and our {VUK}Vilvah guide</a> covers the whole brand.")],
 'deyga': [("The Deyga beetroot lip balm is a cult favourite.",
   f"The Deyga beetroot lip balm is a cult favourite, sold as a pot and a stick: our {BEET}stick or pot guide</a> helps you choose."),
  ("If you know the brand as Deyga Organics, it is the same range.",
   f"If you know the brand as Deyga Organics, it is the same range: our {DOU}Deyga Organics guide</a> explains the brand and where to start.")],
}

def main(atom, admin):
    feed = open(atom).read(); adm = json.load(open(admin))
    bodies = dict(adm['articles'])
    for e in re.findall(r'<entry>(.*?)</entry>', feed, re.S):
        h = re.search(r'blogs/journal/([a-z0-9-]+)', e).group(1)
        if h in EDITS and h not in bodies:
            bodies[h] = re.search(r'<content[^>]*>\s*<!\[CDATA\[(.*?)\]\]>\s*</content>', e, re.S).group(1).strip()
    out = {'articles': [], 'collections': []}
    for h, eds in EDITS.items():
        b = a = bodies[h]
        for old, new in eds:
            assert a.count(old) == 1, (h, old); a = a.replace(old, new)
        out['articles'].append({'handle': h, 'id': f'gid://shopify/Article/{IDS[h]}', 'before': b, 'after': a})
    for h, eds in COLL.items():
        c = adm['collections'][h]; b = a = c['value']
        for old, new in eds:
            assert a.count(old) == 1, (h, old); a = a.replace(old, new)
        out['collections'].append({'handle': h, 'id': c['id'], 'metafield_id': c['metafield_id'], 'before': b, 'after': a})
    json.dump(out, open('docs/seo/journal_backlinks_wave12_2026-11-16.json', 'w'), ensure_ascii=False, indent=1)
    print('ok', len(out['articles']), len(out['collections']))

if __name__ == '__main__':
    main(*sys.argv[1:3])
