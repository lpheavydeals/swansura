"""Rebuild the concern collections from clear rules (user, 3 Nov 2026: the assistant suggested a greying hair oil for
dandruff; LOOKFANTASTIC's advisor gives relevant products). The concern collections made on 26 Oct from loose concern
tags held hair oils under 'glow', combs under 'acne', shampoos under 'hydration' etc.

Rule = product AREA (face / body / lip / hair / tool, from the title) + concern WORDS in the title (kits: words or the
kit name). Fragrance is never included. Prints the diff against the live members and writes
docs/seo/concern_rebuild_2026-11-03.json {collection: {keep, add, remove}} (handles).
Input: storefront /products.json dump + live members (scratchpad, fetched first).
"""
import json, re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
S = pathlib.Path(sys.argv[1])
P = json.load(open(S / 'storefront_products.json'))
M = json.load(open(S / 'concern_members.json'))
CARE = {'Deyga', 'Vilvah', 'Highborn London', 'anatomē', 'Swansura - The Body Studio', 'Shiseido'}
low = lambda s: s.lower()


def area(t):
    t = low(t)
    if re.search(r'\bcomb\b|loofah', t): return 'tool'
    if re.search(r'\blip', t): return 'lip'
    if re.search(r'shampoo|conditioner|\bhair|scalp|eyebrow|neem seed oil', t): return 'hair'
    if re.search(r'body|bath|soap|foot|deo|shower|hand|pedicure|ubtan', t): return 'body'
    if re.search(r'perfume|parfum|pillow spray|room|candle|diffuser|sleep oil|perfume oil|good sleep', t): return 'sleep'
    return 'face'      # face wash, serum, toner, cream, moisturiser, mask, eye, sunscreen, balm, facial oil, gel


R = {   # collection: (areas allowed, include regex, exclude regex)
    'concern-dandruff': ({'hair', 'tool'}, r'dandruff|neem|tea tree|scalp', r'eyebrow|greying'),
    'concern-hairfall': ({'hair'}, r'growth|hair ?fall|strengthen|bhringraj|hair care kit|nourishment kit|bestseller hair', r'eyebrow|greying|dandruff'),
    'hair-oil-for-dry-hair': ({'hair'}, r'(oil|serum)', r'dandruff|greying|eyebrow|neem'),
    'concern-hydration': ({'face', 'body'}, r'hyaluronic|moistur|hydrat|hydro|cream|milk|aloe|ceramide|\bgel\b|facial oil|face oil|balm|elixir|rose ?water|butter|lotion|four phase|beautifying|age|caviar|day & night',
                          r'charcoal|tea tree|acne|oil control|clear skin|cleansing balm|scrub|polish|exfoliat|soap|bath bar|body wash|deo|mud'),
    'concern-glow': ({'face'}, r'vitamin c|bright|glow|radian|\btan\b|lumin|saffron|turmeric|orange|mulethi|gold|beautifying|pigment|rose glow|wild rose|spirulina|ubtan|abc kit|game changer|honey',
                     r'charcoal|acne|dandruff'),
    'concern-acne': ({'face', 'body'}, r'charcoal|tea tree|\bneem|acne|oil control|clear skin|\bpore|spot|salicylic|mud mask|clay|spirulina|exfoliat',
                     r'\blip|hair|\bcomb\b|bath & shower oil|hydration gel|rose ?hip|beautifying|moringa'),
    'concern-calm': ({'face', 'body', 'sleep'}, r'sensitive|fragrance-free|\boat|aloe|chamomile|calm|sooth|cucumber|under eye|eye gel|eye mask|rose ?water|hyaluronic|lavender|sleep|frankincense|bath salts',
                     r'charcoal|scrub|polish|exfoliat|vitamin c|acne|dandruff|deo|perfume|parfum'),
    'concern-lips': ({'lip'}, r'lip', r'$^'),
    'concern-sun': ({'face', 'lip', 'body'}, r'spf|sunscreen|sun protection|tan protection|sun ', r'cleansing balm'),
}
care = [p for p in P if p['vendor'] in CARE and 'Fragrance' not in p['tags'] and p['product_type'] not in ('Fragrance', 'perfume', 'Perfume')]
title = {p['handle']: p['title'] for p in P}
out = {}
for c, (areas, inc, exc) in R.items():
    want = [p['handle'] for p in care if area(p['title']) in areas and re.search(inc, low(p['title'])) and not re.search(exc, low(p['title']))]
    cur = M.get(c, [])
    out[c] = {'keep': [h for h in cur if h in want], 'add': [h for h in want if h not in cur], 'remove': [h for h in cur if h not in want]}
    print(f'\n== {c}: now {len(cur)} -> {len(want)}')
    print('  REMOVE:', '; '.join(title.get(h, h)[:42] for h in out[c]['remove']))
    print('  ADD   :', '; '.join(title.get(h, h)[:42] for h in out[c]['add']))
    print('  KEEP  :', '; '.join(title.get(h, h)[:42] for h in out[c]['keep']))
json.dump(out, open(ROOT / 'docs/seo/concern_rebuild_2026-11-03.json', 'w'), ensure_ascii=False, indent=1)
