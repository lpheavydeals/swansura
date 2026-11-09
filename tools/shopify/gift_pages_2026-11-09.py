"""Christmas / Black Friday gift pages (user, 9 Nov 2026: 'Go ahead with the gift pages').

New manual collections (all returned 404 before):
  perfume-gift-sets-for-her, aftershave-gift-sets-for-him, gifts-under-50, skincare-gift-sets, goat-milk-soap, black-friday
+ new SEO title/description on the 5 existing gift pages, + 'related' chips linking the new pages, + menu items.

Usage: python3 tools/shopify/gift_pages_2026-11-09.py <scratch dir with storefront dumps>
  needs sfall_live.json (all /products.json) and <handle>.json dumps of perfume-gift-sets, perfume-for-women, perfume-for-men,
  gifts-for-her, gifts-for-him, stocking-fillers, christmas-gifts, travel-size-minis, gifts-under-25, gifts-25-to-50.
Writes docs/seo/gift_pages_2026-11-09.json (collectionCreate inputs, product lists, SEO updates, related chips)
and docs/seo/gift_pages_2026-11-09.md (review copy).
Rules: facts only from the catalogue; only real offers (free UK delivery over £40, £5 off over £70, 14-day returns on
unopened items); no last-order dates (client has not confirmed them); no claims; prices written into the copy are from the dump.
"""
import html, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
S = pathlib.Path(sys.argv[1])
L = {p['handle']: p for p in json.load(open(S / 'sfall_live.json'))}
C = lambda h: [p['handle'] for p in json.load(open(S / f'{h}.json')) if p['handle'] in L]
ins = lambda h: bool(any(v['available'] for v in L[h]['variants']) and L[h]['images'])


def mn(h):
    av = [float(v['price']) for v in L[h]['variants'] if v['available']] or [float(v['price']) for v in L[h]['variants']]
    return min(av)


def name(h):
    return L[h]['title'].split(' – ')[0].strip()


def a(h, text=None):
    assert h in L and ins(h), h
    return f'<a href="/products/{h}">{html.escape(text or name(h), quote=False)}</a> (£{mn(h):.2f})'


def c(h, text):
    return f'<a href="/collections/{h}">{text}</a>'


def order(hs):  # in stock first, keep given order
    hs = list(dict.fromkeys(hs))
    return [h for h in hs if ins(h)] + [h for h in hs if not ins(h)]


GS = C('perfume-gift-sets')
WOMEN, MEN = set(C('perfume-for-women')), set(C('perfume-for-men'))
HER = order([h for h in GS if (h in WOMEN or h in set(C('gifts-for-her'))) and h not in MEN])
HIM = order([h for h in GS if (h in MEN or h in set(C('gifts-for-him'))) and h not in WOMEN])
pool = []
for col in ['christmas-gifts', 'perfume-gift-sets', 'gifts-for-her', 'gifts-for-him', 'stocking-fillers', 'travel-size-minis',
            'gifts-under-25', 'gifts-25-to-50']:
    pool += C(col)
U50 = [h for h in dict.fromkeys(pool) if ins(h) and mn(h) <= 50]
SKV = {'vilvah', 'deyga', 'highborn london', 'anatomē', 'swansura - the body studio'}
KIT = re.compile(r'\b(kit|set|combo|gift|bundle|duo|trio|collection)\b', re.I)
SKIN = order([h for h, p in L.items() if p['vendor'].lower() in SKV and KIT.search(name(h))
              and not re.search(r'parfum|perfume|pillow|sleep|fragrance|comb', p['title'], re.I)])
SOAP = order([h for h, p in L.items() if re.search(r'goat ?milk', p['title'], re.I) and re.search(r'soap', p['title'], re.I)]
             + [h for h, p in L.items() if re.search(r'curd & mint soap', p['title'], re.I)])
BF = [h for h in order(GS) + SKIN if ins(h)]
BF = list(dict.fromkeys(BF))

DELIV = ('Every order ships from Swansura in the UK. UK delivery is free on orders over £40, and orders over £70 also get £5 off at '
         'checkout. Unopened items can be returned within 14 days.')
GENUINE = 'Yes. Every product at Swansura is 100% authentic. Swansura is an official UK partner of Deyga and Vilvah.'


def rng(hs):
    p = [mn(h) for h in hs if ins(h)]
    return f'£{min(p):.2f} to £{max(p):.2f}'


EXPLORE = [["All products", "/collections/all"], ["Skincare", "/collections/skincare"], ["Haircare", "/collections/haircare"],
           ["Bath & Body", "/collections/bodycare"], ["Fragrance", "/collections/fragrance"], ["Gifts & Sets", "/collections/sets-combos"],
           ["Deyga", "/collections/deyga"], ["Vilvah", "/collections/vilvah"], ["Highborn London", "/collections/highborn-london"],
           ["Al Haramain", "/collections/al-haramain"], ["Gucci", "/collections/gucci"], ["Calvin Klein", "/collections/calvin-klein"]]
CH = {'her': ["Perfume gift sets for her", "/collections/perfume-gift-sets-for-her"],
      'him': ["Aftershave gift sets for him", "/collections/aftershave-gift-sets-for-him"],
      'u50': ["Gifts under £50", "/collections/gifts-under-50"], 'skin': ["Skincare gift sets", "/collections/skincare-gift-sets"],
      'soap': ["Goat milk soap", "/collections/goat-milk-soap"], 'bf': ["Black Friday", "/collections/black-friday"],
      'xmas': ["Christmas gifts", "/collections/christmas-gifts"], 'gs': ["Perfume gift sets", "/collections/perfume-gift-sets"],
      'stock': ["Stocking fillers", "/collections/stocking-fillers"], 'u25': ["Gifts under £25", "/collections/gifts-under-25"],
      'minis': ["Travel size & mini perfumes", "/collections/travel-size-minis"], 'gher': ["Gifts for her", "/collections/gifts-for-her"],
      'ghim': ["Gifts for him", "/collections/gifts-for-him"], 'goat': ["Goat milk range", "/collections/range-goat-milk"],
      'vk': ["Vilvah", "/collections/vilvah"], 'dk': ["Deyga", "/collections/deyga"], 'o50': ["Luxury gifts over £50", "/collections/gifts-over-50"]}


def related(keys):
    return json.dumps({"facet_label": "", "facet": [], "chips": [CH[k] for k in keys], "explore": EXPLORE}, ensure_ascii=False)


H = lambda *k: next(h for h in L if all(x in h for x in k))
PAGES = []


def page(handle, title, h1, eyebrow, seo_t, seo_d, heading, copy, faq, chips, products):
    assert len(seo_t) <= 60, (handle, len(seo_t))
    assert len(seo_d) <= 150 and "'" not in seo_d, (handle, len(seo_d))
    words = len(re.sub(r'<[^>]+>', ' ', copy).split())
    mf = lambda k, t, v: {'namespace': 'custom', 'key': k, 'type': t, 'value': v}
    PAGES.append({'handle': handle, 'words': words, 'products': products, 'in_stock': sum(map(ins, products)),
                  'input': {'title': title, 'handle': handle, 'sortOrder': 'MANUAL', 'seo': {'title': seo_t, 'description': seo_d},
                            'metafields': [mf('h1', 'single_line_text_field', h1), mf('eyebrow', 'single_line_text_field', eyebrow),
                                           mf('seo_heading', 'single_line_text_field', heading),
                                           mf('seo_copy', 'multi_line_text_field', copy),
                                           mf('faq', 'json', json.dumps(faq, ensure_ascii=False)), mf('related', 'json', related(chips))]}})


# 1 perfume gift sets for her
ck4 = H('calvin-klein-women-s-miniature-fragrance-set-4x15ml')
page('perfume-gift-sets-for-her', 'Perfume gift sets for her', 'Perfume Gift Sets for Her', 'Gifts',
     'Perfume Gift Sets for Her UK | Christmas 2026 | Swansura',
     f'Perfume gift sets for her from £{min(mn(h) for h in HER if ins(h)):.2f}: designer sets, minis and body lotion duos. 100% authentic, UK delivery free over £40.',
     'Perfume gift sets for her',
     f'<p>Perfume gift sets for her take the guesswork out of Christmas: a full bottle with a travel spray or body lotion, or a box of '
     f'minis so she can try several scents before choosing a favourite. Everything here is 100% authentic and ships from the UK.</p>'
     f'<h3>Sets with a full bottle</h3><p>{a(H("chloe-nomade-eau-de-parfum-gift-set"), "Chloé Nomade with a 20ml travel spray")} and '
     f'{a(H("gucci-guilty-pour-femme-eau-de-parfum-gift-set"), "Gucci Guilty Pour Femme with body lotion")} pair her perfume with an extra '
     f'for her bag or bathroom shelf. {a(H("dkny-be-delicious-be-delicious-fresh-blossom"), "DKNY Be Delicious & Fresh Blossom (2 x 30ml)")} '
     f'gives her two bottles to switch between.</p>'
     f'<h3>Miniature sets to explore</h3><p>Not sure of her taste? The {a(ck4, "Calvin Klein Women’s Miniature Set (4 x 15ml)")}, '
     f'{a(H("guerlain-mon-guerlain-miniature-perfume-gift-set"), "Mon Guerlain Miniature Set")} and '
     f'{a(H("burberry-women-s-miniature-perfume-set-4x5ml"), "Burberry Her Miniature Set")} let her try a whole family of scents. '
     f'Single minis such as {a(H("calvin-klein-my-euphoria-eau-de-parfum-10ml"), "CK My Euphoria 10ml")} make easy stocking fillers.</p>'
     f'<p>Browse more in {c("gifts-for-her", "gifts for her")}, {c("perfume-for-women", "perfume for women")} and '
     f'{c("stocking-fillers", "stocking fillers")}. UK delivery is free on orders over £40, and orders over £70 also get £5 off.</p>',
     [['How much are the perfume gift sets for her?', f'Sets in stock run from {rng(HER)}.'],
      ['Are the perfume gift sets genuine?', GENUINE], ['How does delivery work?', DELIV]],
     ['gs', 'gher', 'him', 'u50', 'minis', 'stock', 'xmas', 'skin'], HER)

# 2 aftershave gift sets for him
page('aftershave-gift-sets-for-him', 'Aftershave gift sets for him', 'Aftershave Gift Sets for Him', 'Gifts',
     'Aftershave Gift Sets for Him UK | Christmas 2026 | Swansura',
     f'Aftershave and perfume gift sets for him from £{min(mn(h) for h in HIM if ins(h)):.2f}: Dior, Bvlgari, Azzaro and minis. 100% authentic, UK delivery free over £40.',
     'Aftershave gift sets for him',
     f'<p>Aftershave gift sets for him make Christmas simple: a full bottle with a travel spray, or a box of minis so he can find the scent '
     f'he reaches for every day. Every set is 100% authentic and ships from the UK.</p>'
     f'<h3>Full-size sets</h3><p>{a(H("dior-sauvage-eau-de-parfum-100ml-10ml"), "Dior Sauvage Eau de Parfum 100ml + 10ml")} is the classic '
     f'choice. {a(H("bvlgari-man-wood-essence-eau-de-parfum-gift-set"), "Bvlgari Man Wood Essence 100ml + 15ml")}, '
     f'{a(H("azzaro-the-most-wanted-eau-de-toilette-intense-gift-set"), "Azzaro The Most Wanted Intense with two 10ml sprays")} and '
     f'{a(H("dolce-gabbana-k-eau-de-parfum-gift-set-50ml"), "Dolce & Gabbana K 50ml + 5ml")} each add a travel size for the gym bag or '
     f'office drawer.</p>'
     f'<h3>Minis to try</h3><p>The {a(H("dolce-gabbana-men-s-miniature-fragrance-set"), "Dolce & Gabbana Men’s Miniature Set")} '
     f'brings four scents in one box, and single 10ml minis such as {a(H("calvin-klein-defy-parfum-10ml"), "CK Defy Parfum")} suit a '
     f'stocking.</p>'
     f'<p>See also {c("gifts-for-him", "gifts for him")}, {c("perfume-for-men", "perfume for men")} and '
     f'{c("mens-grooming", "men’s grooming")}. UK delivery is free on orders over £40, and orders over £70 also get £5 off.</p>',
     [['How much are the aftershave gift sets?', f'Sets in stock run from {rng(HIM)}.'],
      ['Are the aftershave gift sets genuine?', GENUINE], ['How does delivery work?', DELIV]],
     ['gs', 'ghim', 'her', 'u50', 'minis', 'stock', 'xmas', 'o50'], HIM)

# 3 gifts under £50
page('gifts-under-50', 'Gifts under £50', 'Gifts Under £50', 'Gifts',
     'Gifts Under £50 UK | Perfume & Skincare Gifts | Swansura',
     'Gifts under £50: perfume minis and sets, natural skincare kits and stocking fillers. 100% authentic, shipped from the UK, free delivery over £40.',
     'Gifts under £50',
     f'<p>Gifts under £50 do not have to feel small. This edit brings together perfume gift sets, miniatures and natural skincare kits, '
     f'all in stock and all under £50, so you can shop by budget and still give something she or he will use.</p>'
     f'<h3>Perfume</h3><p>{a(H("dkny-be-delicious-be-delicious-fresh-blossom"), "DKNY Be Delicious & Fresh Blossom set")}, the '
     f'{a(ck4, "Calvin Klein Women’s Miniature Set")} and the '
     f'{a(H("dolce-gabbana-men-s-miniature-fragrance-set"), "Dolce & Gabbana Men’s Miniature Set")} all sit under £50.</p>'
     f'<h3>Natural skincare</h3><p>{a(H("vilvah-am-pm-serum-kit"), "Vilvah AM PM Serum Kit")} and '
     f'{a(H("deyga-mini-foot-spa-combo"), "Deyga Mini Foot Spa Combo")} are ready-made routines in one box, and lip sets such as '
     f'{a(H("deyga-soft-lip-combo"), "Deyga Soft Lip Combo")} make easy add-ons.</p>'
     f'<p>Spending less? Try {c("gifts-under-25", "gifts under £25")} or {c("stocking-fillers", "stocking fillers")}. Orders over '
     f'£40 ship free in the UK, and orders over £70 also get £5 off at checkout.</p>',
     [['What can I buy under £50?', f'Gifts in this edit run from {rng(U50)}, from perfume minis to skincare kits and gift sets.'],
      ['Are the gifts genuine?', GENUINE], ['How does delivery work?', DELIV]],
     ['u25', 'stock', 'her', 'him', 'skin', 'xmas', 'minis', 'o50'], U50)

# 4 skincare gift sets
page('skincare-gift-sets', 'Skincare gift sets', 'Skincare Gift Sets', 'Gifts',
     'Skincare Gift Sets UK | Natural Skincare Kits | Swansura',
     'Skincare gift sets and natural skincare kits from Vilvah, Deyga and Highborn London. 100% authentic, shipped from the UK, free delivery over £40.',
     'Skincare gift sets',
     f'<p>Skincare gift sets turn a routine into a present: two or three products chosen to work together, in one box. Swansura is the '
     f'official UK partner of Vilvah and Deyga, so every kit here is authentic and ships from the UK.</p>'
     f'<h3>Face care</h3><p>{a(H("vilvah-am-pm-serum-kit"), "Vilvah AM PM Serum Kit")} pairs a morning and an evening serum, '
     f'{a(H("deyga-healthy-glow-kit"), "Deyga Healthy Glow Kit")} brings a rose face pack and rose water toner, and '
     f'{a(H("ultimate-day-night-moisture-set"), "Highborn London Ultimate Day & Night Moisture Set")} is a luxury choice.</p>'
     f'<h3>Hair, body and lips</h3><p>{a(H("vilvah-goat-milk-hair-kit"), "Vilvah Goat Milk Hair Kit")}, '
     f'{a(H("deyga-mini-foot-spa-combo"), "Deyga Mini Foot Spa Combo")} and '
     f'{a(H("deyga-nourished-lip-care-kit") if any("deyga-nourished-lip-care-kit" in x for x in L) else H("nourished-lip-care-kit"), "Deyga Nourished Lip Care Kit")} cover the rest of the routine.</p>'
     f'<p>Browse each brand in {c("vilvah", "Vilvah")} and {c("deyga", "Deyga")}, or see {c("gifts-for-her", "gifts for her")}. '
     f'UK delivery is free on orders over £40, and orders over £70 also get £5 off.</p>',
     [['How much are the skincare gift sets?', f'Kits in stock run from {rng(SKIN)}.'],
      ['Are the skincare gift sets genuine?', GENUINE], ['How does delivery work?', DELIV],
      ['Can I see the full ingredients?', 'Yes. Every Vilvah and Deyga kit lists the full ingredients of each product on its Ingredients tab.']],
     ['gher', 'u50', 'soap', 'vk', 'dk', 'xmas', 'stock', 'her'], SKIN)

# 5 goat milk soap
page('goat-milk-soap', 'Goat milk soap', 'Goat Milk Soap', 'Bath & Body',
     'Goat Milk Soap UK | Handmade Vilvah Soap Bars | Swansura',
     'Goat milk soap bars from Vilvah: Classic, Classic Rose, Charcoal and Cucumber, Curd & Mint. Shipped from the UK, free delivery over £40.',
     'Goat milk soap',
     f'<p>Goat milk soap gives a creamy lather that leaves skin feeling soft rather than tight. Vilvah makes these bars with goat milk and '
     f'plant oils such as olive, coconut and castor oil, and Swansura is the brand’s official UK partner.</p>'
     f'<h3>The bars</h3><p>{a(H("classic-goatmilk-soap-bar-115g"), "Classic Goat Milk Soap")} is lightly scented with lavender '
     f'essential oil, {a(H("classic-rose-goat-milk-soap-bar-125g"), "Classic Rose Goat Milk Soap")} adds rose petals and French pink clay, '
     f'and {a(H("charcoal-goatmilk-soap-bar-115g"), "Charcoal Goat Milk Soap")} pairs activated charcoal with goat milk. '
     f'{a(H("cucumber-curd-mint-soap-bar-115g"), "Cucumber, Curd & Mint Soap")} has a fresh, minty scent.</p>'
     f'<h3>How to use</h3><p>Lather between wet hands, massage over damp skin and rinse well. Keep the bar on a draining soap dish so it '
     f'lasts, and follow with a body lotion if your skin tends to feel dry. Patch test before first use.</p>'
     f'<p>See the whole {c("range-goat-milk", "goat milk range")} or {c("skincare-gift-sets", "skincare gift sets")}. UK delivery is free '
     f'on orders over £40.</p>',
     [['How much is the goat milk soap?', f'Each bar costs £{mn(H("classic-goatmilk-soap-bar-115g")):.2f}.'],
      ['Is the soap genuine Vilvah?', 'Yes. Swansura is an official UK partner of Vilvah and every bar ships from the UK.'],
      ['How does delivery work?', DELIV]],
     ['goat', 'vk', 'skin', 'u50', 'stock', 'gher'], SOAP)

# 6 black friday
page('black-friday', 'Black Friday', 'Black Friday Perfume & Skincare Gifts', 'Black Friday 2026',
     'Black Friday Perfume & Skincare Gifts UK 2026 | Swansura',
     'Black Friday at Swansura: perfume gift sets and skincare kits, 100% authentic and shipped from the UK. Free delivery over £40, £5 off over £70.',
     'Black Friday at Swansura',
     f'<p>Black Friday at Swansura brings our perfume gift sets and natural skincare kits together on one page, so you can get Christmas '
     f'shopping done early. Every product is 100% authentic and ships from the UK.</p>'
     f'<h3>The offers that apply</h3><p>UK delivery is free on orders over £40, and orders over £70 also get £5 off at checkout. These '
     f'offers run all year, including Black Friday. Any extra Black Friday offer will be shown on this page.</p>'
     f'<h3>Where to start</h3><p>For her, try {a(H("chloe-nomade-eau-de-parfum-gift-set"), "Chloé Nomade with a travel spray")}; '
     f'for him, {a(H("dior-sauvage-eau-de-parfum-100ml-10ml"), "Dior Sauvage 100ml + 10ml")}. For natural skincare, '
     f'{a(H("vilvah-am-pm-serum-kit"), "Vilvah AM PM Serum Kit")} is a two-step routine in one box.</p>'
     f'<p>Shop by recipient in {c("perfume-gift-sets-for-her", "perfume gift sets for her")} and '
     f'{c("aftershave-gift-sets-for-him", "aftershave gift sets for him")}, or by budget in {c("gifts-under-50", "gifts under £50")}.</p>',
     [['What are the Black Friday offers?', 'UK delivery is free on orders over £40, and orders over £70 also get £5 off at checkout. '
       'Any extra Black Friday offer will be shown on this page.'],
      ['Are the products genuine?', GENUINE], ['How does delivery work?', DELIV]],
     ['her', 'him', 'u50', 'skin', 'xmas', 'stock', 'gs'], BF)

# existing gift pages: SEO refresh + chips for the new pages
def lo(col): return min(mn(h) for h in C(col) if ins(h))
SEO = {
 'perfume-gift-sets': ('Perfume Gift Sets UK | Christmas 2026 | Swansura',
                       f'Perfume gift sets from £{lo("perfume-gift-sets"):.2f}: Dior, Chloé, Gucci, Bvlgari and miniature sets. 100% authentic, UK delivery free over £40.'),
 'gifts-for-her': ('Gifts for Her UK | Perfume & Skincare Gifts | Swansura',
                   f'Gifts for her from £{lo("gifts-for-her"):.2f}: perfume gift sets, minis and natural skincare kits. 100% authentic, shipped from the UK, free over £40.'),
 'gifts-for-him': ('Gifts for Him UK | Aftershave & Grooming Gifts | Swansura',
                   f'Gifts for him from £{lo("gifts-for-him"):.2f}: aftershave gift sets, minis and grooming. 100% authentic, shipped from the UK, free delivery over £40.'),
 'christmas-gifts': ('Christmas Gifts UK 2026 | Perfume & Skincare | Swansura',
                     f'Christmas gifts 2026 from £{lo("christmas-gifts"):.2f}: perfume gift sets, minis and skincare kits. 100% authentic, UK delivery free over £40.'),
 'stocking-fillers': ('Stocking Fillers UK | Minis & Lip Care Gifts | Swansura',
                      f'Stocking fillers from £{lo("stocking-fillers"):.2f}: perfume minis, lip care and small gifts. 100% authentic, shipped from the UK, free delivery over £40.'),
}
for k, (t, d) in SEO.items():
    assert len(t) <= 60 and len(d) <= 150 and "'" not in d, (k, len(t), len(d))
ADD = {'perfume-gift-sets': ['her', 'him', 'u50'], 'gifts-for-her': ['her', 'u50', 'skin'], 'gifts-for-him': ['him', 'u50'],
       'christmas-gifts': ['her', 'him', 'u50', 'skin', 'bf'], 'stocking-fillers': ['u50', 'soap']}

out = {'pages': PAGES, 'seo': SEO, 'add_chips': {k: [CH[x] for x in v] for k, v in ADD.items()}}
json.dump(out, open(ROOT / 'docs/seo/gift_pages_2026-11-09.json', 'w'), ensure_ascii=False, indent=1)
with open(ROOT / 'docs/seo/gift_pages_2026-11-09.md', 'w') as f:
    f.write('# Gift pages, 9 Nov 2026\n\n')
    for p in PAGES:
        i = p['input']; m = {x['key']: x['value'] for x in i['metafields']}
        f.write(f"## /collections/{p['handle']} ({len(p['products'])} products, {p['in_stock']} in stock, {p['words']} words)\n\n"
                f"- SEO title: {i['seo']['title']}\n- SEO description: {i['seo']['description']}\n- H1: {m['h1']}\n\n{m['seo_copy']}\n\n"
                f"FAQ: {m['faq']}\n\n")
    f.write('## Existing gift pages: new SEO\n\n' + ''.join(f'- {k}: {t} / {d}\n' for k, (t, d) in SEO.items()))
for p in PAGES:
    print(p['handle'], len(p['products']), p['in_stock'], p['words'], len(p['input']['seo']['title']), len(p['input']['seo']['description']))
