"""Remove claim wording from Highborn London + anatomē product titles (user, 10 Nov 2026: 'Fix the product titles with
claim words too'). 20 products: anatomē parfum claim subtitles ('Centre the Mind & Restore Calm', 'Enhance Endurance &
Sharpen Clarity' …), sleep-product subtitles ('for an Overactive Mind', 'for Restless Sleep', 'Relax + Sleep'),
'Illuminating', Highborn 'Anti-Ageing' / 'Age-Defying'. Coined brand names kept (YOUTHBOOST, GLOWGUARD, MOISTUREBURST,
Youth Elixir, Revive and Defy, Scrub and Glow, Gift of Good Sleep). Handles (URLs) unchanged.
Per product: title, SEO title/description, custom.h1, old name in its description. Plus the old names in collection
custom.seo_copy (11 collections). argv[1] = Admin read of the 20 (before-state), argv[2] = collections dump.
Writes docs/seo/claim_titles_2026-11-10.json (before/after = undo)."""
import json, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
P = {n['handle']: n for n in json.load(open(sys.argv[1]))['data']['nodes']}
C = json.load(open(sys.argv[2]))
T = {  # handle: (title, seo title, seo description or None = keep, h1 or None = keep)
 'expression-eau-de-parfum-open-the-breath-support-expression-10ml': ('Expression Eau de Parfum Travel 10ml', 'anatomē Expression Eau de Parfum Travel 10ml | Swansura', 'anatomē Expression Eau de Parfum in a 10ml travel spray, a fresh, airy unisex scent. 100% authentic, shipped from the UK, free UK delivery over £40.', 'anatomē Expression Eau de Parfum Travel 10ml'),
 'expression-eau-de-parfum-open-the-breath-support-expression-100ml': ('Expression Eau de Parfum 100ml', None, 'anatomē Expression Eau de Parfum, a fresh, oceanic unisex scent of sea salt, cedarwood and hinoki. 10ml, 50ml or 100ml. Free UK delivery over £40.', None),
 'balance-eau-de-parfum-centre-the-mind-restore-calm-100ml': ('Balance Eau de Parfum 100ml', None, 'anatomē Balance Eau de Parfum, a soft, warm unisex scent of damask rose, saffron, amber and cedar. 10ml, 50ml or 100ml. Free UK delivery over £40.', None),
 'order-eau-de-parfum-clarify-the-mind-expand-thought-100ml': ('Order Eau de Parfum 100ml', None, None, None),
 'energy-eau-de-parfum-enhance-endurance-sharpen-clarity-100ml': ('Energy Eau de Parfum 100ml', None, 'anatomē Energy Eau de Parfum, a fresh unisex scent of Calabrian lemon, peppermint, neroli and tobacco leaf. 10ml to 100ml. Free UK delivery over £40.', None),
 'focus-eau-de-parfum-sharpen-focus-awaken-the-senses-100ml': ('Focus Eau de Parfum 100ml', 'anatomē Focus Eau de Parfum 100ml | Swansura UK', 'anatomē Focus Eau de Parfum, a spicy woody unisex scent of cardamom, black pepper and sandalwood. 10ml to 100ml. Free UK delivery over £40.', None),
 'support-eau-de-parfum-protective-herbaceous-restorative': ('Support Eau de Parfum', 'anatomē Support Eau de Parfum | Swansura UK', 'anatomē Support Eau de Parfum, a green, herbal unisex scent of watermint, sage, rosemary and oak moss. 10ml, 50ml or 100ml. Free UK delivery over £40.', None),
 'support-eau-de-parfum-travel-10ml': ('Support Eau de Parfum Travel 10ml', None, 'anatomē Support Eau de Parfum in a 10ml travel spray, a green, herbal unisex scent of watermint, sage and rosemary. Free UK delivery over £40.', 'anatomē Support Eau de Parfum Travel 10ml'),
 'energy-eau-de-parfum-travel-10ml': ('Energy Eau de Parfum Travel 10ml', 'anatomē Energy Eau de Parfum Travel 10ml | Swansura', 'anatomē Energy Eau de Parfum in a 10ml travel spray, a bright citrus-and-blossom unisex scent. 100% authentic, free UK delivery over £40.', 'anatomē Energy Eau de Parfum Travel 10ml'),
 'parfum-travel-discovery-set-6-wellbeing-parfums': ('Parfum Travel Discovery Set 6 x 10ml', 'anatomē Parfum Travel Discovery Set 6 x 10ml | Swansura', 'anatomē Parfum Travel Discovery Set: six 10ml eau de parfums, Expression, Balance, Energy, Order, Support and Focus. Free UK delivery over £40.', 'anatomē Parfum Travel Discovery Set'),
 'sleep-pillow-spray-roman-chamomile-28-botanical-extracts-anatome': ('Roman Chamomile Sleep Pillow Spray', None, None, None),
 'somali-frankincense-sleep-pillow-spray-overactive-mind-anatome': ('Somali Frankincense Sleep Pillow Spray', None, None, None),
 'sleep-oil-for-an-overactive-mind-somali-frankincense-anatome': ('Somali Frankincense Sleep Oil', 'Sleep Oil: anatomē Somali Frankincense | Swansura', 'anatomē Somali Frankincense Sleep Oil, a 16-ingredient essential oil blend for pulse points at bedtime. 15ml or 30ml. Free UK delivery over £40.', 'anatomē Somali Frankincense Sleep Oil'),
 'sleep-oil-for-restless-sleep-roman-chamomile-cornish-lavender-anatome': ('Roman Chamomile & Cornish Lavender Sleep Oil', 'Lavender Sleep Oil: anatomē Roman Chamomile | Swansura', 'anatomē Roman Chamomile and Cornish Lavender Sleep Oil, a herbal, floral blend for pulse points at bedtime. 15ml or 30ml. Free UK delivery over £40.', 'anatomē Roman Chamomile & Cornish Lavender Sleep Oil'),
 'the-little-gift-of-good-sleep-frankincense-overactive-mind': ('The Little Gift of Good Sleep | Somali Frankincense', 'anatomē The Little Gift of Good Sleep | Swansura', 'anatomē The Little Gift of Good Sleep: a 10ml Somali Frankincense pillow spray and a 10ml sleep oil roller. Free UK delivery over £40.', 'anatomē The Little Gift of Good Sleep, Somali Frankincense'),
 'relax-sleep-chamomile-bath-salts': ('Chamomile Bath Salts', 'Chamomile Bath Salts: anatomē 480g | Swansura', 'anatomē Chamomile Bath Salts, natural salts with organic botanicals for a warm evening bath. 480g jar or pouch. Free UK delivery over £40.', 'anatomē Chamomile Bath Salts'),
 'illuminating-rose-hip-grape-seed-avocado-face-oil': ('Rose-hip, Grape Seed & Avocado Face Oil', 'Rosehip Face Oil: anatomē Grape Seed & Avocado | Swansura', 'anatomē rosehip face oil with grape seed, avocado, jojoba and mandarin oils, for evening use. 30ml, £52, free UK delivery over £40.', None),
 'youthboost-anti-ageing-peptide-serum': ('YOUTHBOOST Peptide Serum', None, None, 'Highborn London YOUTHBOOST Peptide Serum'),
 'glowguard-spf30-anti-ageing-moisturiser': ('GLOWGUARD SPF30 Moisturiser', 'Highborn London GLOWGUARD SPF30 Moisturiser | Swansura', 'Highborn London GLOWGUARD SPF30 Moisturiser, a daily face moisturiser with non-nano zinc oxide. 30ml or 50ml. Free UK delivery over £40.', 'Highborn London GLOWGUARD SPF30 Moisturiser'),
 'organic-age-defying-facial-oil': ('Organic Facial Oil', 'Highborn London Organic Facial Oil 30ml | Swansura', 'Highborn London Organic Facial Oil, a lightweight blend of organic botanical oils for face and neck. 30ml. Free UK delivery over £40.', 'Highborn London Organic Facial Oil'),
}
REP = [  # old name in running text -> new (HTML and plain forms)
 ('Sleep Oil for Restless Sleep | Roman Chamomile &amp; Cornish Lavender', 'Roman Chamomile &amp; Cornish Lavender Sleep Oil'),
 ('Sleep Oil for Restless Sleep', 'Roman Chamomile &amp; Cornish Lavender Sleep Oil'),
 ('Sleep Oil for an Overactive Mind', 'Somali Frankincense Sleep Oil'),
 ('The Little Gift of Good Sleep - Frankincense', 'The Little Gift of Good Sleep, Somali Frankincense'),
 ('Relax + Sleep Chamomile Bath Salts', 'Chamomile Bath Salts'),
 ('Illuminating Rose-hip, Grape Seed &amp; Avocado Face Oil', 'Rose-hip, Grape Seed &amp; Avocado Face Oil'),
 ('Illuminating Rose-hip, Grape Seed & Avocado Face Oil', 'Rose-hip, Grape Seed & Avocado Face Oil'),
 ('YOUTHBOOST Anti-Ageing Peptide Serum', 'YOUTHBOOST Peptide Serum'),
 ('GLOWGUARD SPF30 Anti-Ageing Moisturiser', 'GLOWGUARD SPF30 Moisturiser'),
 ('Organic Age-Defying Facial Oil', 'Organic Facial Oil'),
 ('anatomē Illuminating rosehip', 'anatomē rosehip'),
]
def rep(s):
    for a, b in REP: s = s.replace(a, b)
    return s
prods, cols = [], []
for h, (t, st, sd, h1) in T.items():
    p = P[h]
    new = dict(title=t, seo_title=st or p['seo']['title'], seo_description=sd or p['seo']['description'], h1=h1 or p['h1']['value'], html=rep(p['descriptionHtml']))
    assert len(new['seo_title']) <= 60 and len(new['seo_description']) <= 155, (h, len(new['seo_title']), len(new['seo_description']))
    prods.append(dict(id=p['id'], handle=h, before=dict(title=p['title'], seo_title=p['seo']['title'], seo_description=p['seo']['description'], h1=p['h1']['value'], html=p['descriptionHtml']), after=new))
for c in C:
    v = (c.get('c') or {}).get('value') or ''
    n = rep(v)
    if n != v: cols.append(dict(id=c['id'], handle=c['handle'], before=v, after=n))
json.dump(dict(products=prods, collections=cols), open(ROOT / 'docs/seo/claim_titles_2026-11-10.json', 'w'), ensure_ascii=False, indent=1)
for x in prods: print(x['before']['title'][:58].ljust(58), '->', x['after']['title'])
print(len(prods), 'products;', sum(x['before']['html'] != x['after']['html'] for x in prods), 'descriptions changed;', len(cols), 'collections:', [c['handle'] for c in cols])
