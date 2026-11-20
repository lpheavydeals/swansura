"""Remove product prices from the 5 Journal guides published 20 Nov 2026 (chloe, dolce-gabbana, lalique,
armaf-club-de-nuit, skincare-gift-sets). Keeps the £40 free-delivery threshold and price bands.
Usage: journal_price_strip_new5_2026-11-20.py <admin articles json> <out json>
"""
import json, re, sys
src, out = sys.argv[1], sys.argv[2]
nodes = json.load(open(src))['data']['articles']['nodes']
HAND = {
 'dolce-gabbana-perfume-guide': [
  ('(£66.54, 100ml, or <a href="/products/dolce-gabbana-the-one-for-men-eau-de-parfum-150ml-luxury-men-s-fragrance">150ml</a> at £80.99)',
   '(100ml, or <a href="/products/dolce-gabbana-the-one-for-men-eau-de-parfum-150ml-luxury-men-s-fragrance">150ml</a>)')],
 'lalique-perfume-guide': [
  ('is a 100ml or 125ml bottle at around £30.', 'is a 100ml or 125ml bottle.'),
  ('<strong>Buying a gift?</strong> Every Lalique bottle we stock costs under £35: see <a href="/collections/gifts-under-50">gifts under £50</a>',
   '<strong>Buying a gift?</strong> See <a href="/collections/gifts-under-50">gifts under £50</a>')],
 'armaf-club-de-nuit-guide': [
  ('in 100ml bottles at £44.99 each.', 'in 100ml bottles.')],
 'skincare-gift-sets-guide': [
  ('The best value hair set we stock.', ''),
  ('The most affordable face set, and a good one for someone who likes traditional ingredients.', 'A good face set for someone who likes traditional ingredients.'),
  ('<p>For stockings and Secret Santa: the Deyga hair combo (from £11.99), Vilvah Tinted Lip Balm Kit (£17), Deo Shot Kit (£17.99) and Deyga Healthy Glow Kit (£19.99). The Annapoorna box is just over, at £20.99. Our',
   '<p>For stockings and Secret Santa: the Deyga hair combo, Vilvah Tinted Lip Balm Kit, Deo Shot Kit and Deyga Healthy Glow Kit. Our'),
  ('<strong>Spend £40 or more</strong> for free UK delivery: the Deyga Nourished Lip Care Kit and the Vilvah Tinted Lip Balm Kit together come to just over.',
   '<strong>Spend £40 or more</strong> for free UK delivery.')],
}
SUMMARY = {'skincare-gift-sets-guide': ('with exactly what is in each kit and the prices.', 'with exactly what is in each kit.')}
res = []
for n in nodes:
    h, b = n['handle'], n['body']
    for a, c in HAND.get(h, []):
        assert b.count(a) == 1, (h, a[:50]); b = b.replace(a, c)
    b = re.sub(r' \((?:from )?£\d[\d.]*\)', '', b)            # (£X) / (from £X)
    b = re.sub(r'\((?:from )?£\d[\d.]*, ', '(', b)              # (£X, 100ml) -> (100ml)
    b = b.replace(' </li>', '</li>').replace('  ', ' ')
    s = n['summary']
    if h in SUMMARY:
        a, c = SUMMARY[h]; assert s.count(a) == 1; s = s.replace(a, c)
    res.append({'id': n['id'], 'handle': h, 'body': [n['body'], b], 'summary': [n['summary'], s]})
json.dump(res, open(out, 'w'), ensure_ascii=False, indent=1)
for r in res:
    print(r['handle'], 'left:', re.findall(r'£\d[\d.,]*', r['body'][1]))
