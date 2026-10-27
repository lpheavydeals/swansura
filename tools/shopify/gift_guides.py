"""Diwali + Christmas 2026 gift guides for the Journal blog (user, 27 Oct 2026), as Shopify ArticleCreateInput.

Same shape as proto_journal.py: body HTML, 'Shop the story' in custom.products, FAQs in custom.faq (json [[q, a]]),
custom.read_minutes, SEO in global title/description tags. Created unpublished: the client approves and publishes.

Product links and prices come from the live storefront (collection products.json dumps), so every product named is
in stock at the time of writing. In the copy, [[key|text]] is a product link and {{key}} its price.
Facts are taken from each product's own description (contents, sizes, notes); no medical or result claims.

Usage: python3 tools/shopify/gift_guides.py <allp.json>   (handle -> storefront product, merged from the gift
collections' /collections/<handle>/products.json)
Output: docs/seo/gift_guides_2026-10-27.jsonl
"""
import json
import re
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
ALL = json.load(open(sys.argv[1]))

# key -> exact storefront handle (checked in stock 27 Oct 2026)
PICK = {
    "amber-gold": "al-haramain-amber-oud-gold-edition-eau-de-parfum-luxury-unisex-fruity-amber-fragrance",
    "amber-ruby": "al-haramain-amber-oud-ruby-edition-eau-de-parfum-luxury-unisex-amber-floral-fragrance",
    "safran": "montale-aoud-safran-eau-de-parfum-100ml-luxury-unisex-saffron-oud-fragrance",
    "malaki": "chopard-oud-malaki-eau-de-parfum-80ml-luxury-men-s-oud-fragrance",
    "gold-rose": "gold-rose-oudh-extrait-de-parfum-100ml-luxury-unisex-oud-perfume",
    "isparta": "boucheron-rose-d-isparta-eau-de-parfum-125ml-luxury-unisex-rose-amber-fragrance",
    "royal-rose": "korloff-royal-rose-eau-de-parfum-88ml",
    "milk-body": None, "polish": None, "foot-spa": "deyga-mini-foot-spa-combo", "glow": "deyga-healthy-glow-kit",
    "soft-lip": "deyga-soft-lip-combo", "lip-nourish": None, "combs": None, "deo": None, "hair-duo": None,
    "bloom-set": None, "burberry-mini": None, "ck-mini": None, "alive": None,
    "most-wanted": None, "rain": None, "dg-mini": None,
    "dior-mini": "dior-iconics-mini-perfume-discovery-set-5-x-5ml",
    "hermes-mini": "hermes-miniature-edt-gift-set-4-x-7-5ml-unisex-fragrances",
    "adp-holiday": "acqua-di-parma-holiday-discovery-set-edp-3x12ml",
    "korloff-disc": "korloff-paris-discovery-set-eau-de-parfum-3x10ml",
    "sig-disc": "signature-discovery-set-10x10ml",
    "day-night": "ultimate-day-night-moisture-set", "revive": "revive-and-defy-starter-set",
    "milk-face": None, "sleep": None,
    "bloom-mini": None, "defy-mini": None, "toit": None, "tinted": "vilvah-tinted-lip-balm-kit", "lip-scrub": None,
}
# keys without a fixed handle: unique match on the start of the product title
TITLE = {
    "milk-body": "Vilvah Milk Body Kit", "polish": "Vilvah Body Polishing Kit", "lip-nourish": "Vilvah Lip Nourishing Kit",
    "combs": "Neem Wood Comb Set of 3", "deo": "Vilvah Deo Shot Kit", "hair-duo": "Deyga Daily Use Healthy Hair Kit",
    "bloom-set": "Gucci Bloom Eau de Parfum Gift Set", "burberry-mini": "Burberry Women’s Miniature Perfume Set",
    "ck-mini": "Calvin Klein Women’s Miniature Fragrance Set", "alive": "Hugo Boss Alive Eau de Parfum 80ml",
    "most-wanted": "Azzaro The Most Wanted Eau de Toilette Intense Gift Set", "rain": "Bvlgari Man Rain Essence",
    "dg-mini": "Dolce & Gabbana Men’s Miniature Fragrance Set", "milk-face": "Vilvah Milk Face Kit",
    "sleep": "The Little Gift of Good Sleep", "bloom-mini": "Gucci Bloom Eau de Toilette 10ml",
    "defy-mini": "Calvin Klein Defy Parfum 10ml", "toit": "Hermès Un Jardin Sur Le Toit",
    "lip-scrub": "Vilvah Natural Lip Scrub",
}


def avail(p):
    return any(v["available"] for v in p["variants"])


for k, h in PICK.items():
    if h is None:
        hits = [x for x, p in ALL.items() if p["title"].startswith(TITLE[k]) and avail(p)]
        assert len(hits) == 1, (k, hits)
        PICK[k] = hits[0]
    assert PICK[k] in ALL and avail(ALL[PICK[k]]), k


def price(k):
    v = min(float(v["price"]) for v in ALL[PICK[k]]["variants"] if v["available"])
    return f"£{v:.2f}".replace(".00", "")


def fill(s):
    s = re.sub(r"\[\[([\w-]+)\|([^\]]+)\]\]", lambda m: f'<a href="/products/{PICK[m.group(1)]}">{m.group(2)}</a>', s)
    return re.sub(r"\{\{([\w-]+)\}\}", lambda m: price(m.group(1)), s)


DIWALI = {
    "title": "Diwali gift ideas 2026: oud, rose and natural skincare",
    "handle": "diwali-gift-ideas",
    "tag": "Gift guide",
    "summary": "Oud and rose perfumes, Deyga and Vilvah skincare kits and small gifts under £20 for Diwali 2026.",
    "mt": "Diwali Gift Ideas UK 2026: Oud, Rose & Skincare | Swansura",
    "md": "Diwali gift ideas for 2026: oud and amber perfumes, rose scents, Deyga and Vilvah skincare kits and small gifts under £20, all dispatched from the UK.",
    "shop": ["amber-gold", "amber-ruby", "safran", "isparta", "milk-body", "foot-spa", "soft-lip", "polish"],
    "body": """<p>Diwali falls on <strong>Sunday 8 November 2026</strong>. Alongside the lamps, sweets and rangoli, it is a time for giving gifts to family, friends and the people who host you. If you are looking for <strong>Diwali gifts in the UK</strong> that feel special without being complicated, this guide pulls together the pieces we would choose ourselves: warm oud and amber perfumes, rich rose scents, natural skincare kits from Indian brands, and small gifts for cousins, colleagues and hosts.</p>
<h2>The short answer</h2>
<p>For someone who loves deep, warm scents, choose an <strong>oud or amber perfume</strong>. For a classic floral, choose <strong>rose</strong>. For someone who prefers skincare, a <strong>Deyga or Vilvah kit</strong> brings natural Indian beauty in one box. And for a stack of smaller gifts, lip and hair sets under £20 go a long way. You can see everything in one place in our <a href="/collections/diwali-gifts">Diwali gifts</a> collection.</p>
<h2>Oud and amber perfumes</h2>
<p>Oud and amber suit the season: warm, glowing and made for evenings with family. A good first bottle is [[amber-gold|Al Haramain Amber Oud Gold Edition]] ({{amber-gold}}), a sweet unisex scent that opens with bergamot and green notes, then moves into melon, pineapple and amber over vanilla and musk. For something richer, [[amber-ruby|Amber Oud Ruby Edition]] ({{amber-ruby}}) pairs saffron and bitter almond with jasmine and ambergris.</p>
<p>If they already love oud, [[safran|Montale Aoud Safran]] ({{safran}}) is built around saffron and oud with rose, amber and woods. For him, [[malaki|Chopard Oud Malaki]] ({{malaki}}) mixes tobacco, spices and leather with oud and dark woods. And for a once-a-year gift, [[gold-rose|Tiziana Terenzi Gold Rose Oudh]] ({{gold-rose}}) is an extrait de parfum with Bulgarian rose, oud, amber, sandalwood and honey. Want it to last through a long celebration? Our guide to <a href="/blogs/journal/layer-oud-with-body-butter">layering oud with body butter</a> explains how.</p>
<h2>Rose perfumes</h2>
<p>Rose is a natural fit for a festival of colour and flowers. [[isparta|Boucheron Rose d’Isparta]] ({{isparta}}, 125ml) wraps Turkish rose in cinnamon, saffron and incense over amber, sandalwood and tonka bean. [[royal-rose|Korloff Royal Rose]] ({{royal-rose}}) is brighter: bergamot, mandarin and pink pepper first, then rose with incense and elemi.</p>
<h2>Natural skincare kits from Deyga and Vilvah</h2>
<p>Swansura is an official UK partner of both <a href="/collections/milk-drop-brightening-serum-1">Deyga</a> and <a href="/collections/milk-drop-brightening-serum">Vilvah</a>, two Indian brands built on plant-based and milk-based care, so every kit is genuine and ships from the UK. (Not sure which brand suits them? Read <a href="/blogs/journal/deyga-or-vilvah">Deyga or Vilvah</a>.)</p>
<ul>
<li>[[milk-body|Vilvah Milk Body Kit]] ({{milk-body}}): Goat Milk Body Wash with a soft vanilla scent, plus Milk Body Lotion with oat milk, olive squalane and ceramides.</li>
<li>[[polish|Vilvah Body Polishing Kit]] ({{polish}}): a coffee body scrub and a body butter with almond milk, shea butter, olive oil and argan oil.</li>
<li>[[foot-spa|Deyga Mini Foot Spa Combo]] ({{foot-spa}}): foot soak, exfoliating scrub and foot butter for an at-home pedicure.</li>
<li>[[glow|Deyga Healthy Glow Kit]] ({{glow}}): a rose and mulethi face pack with a rose toner.</li>
</ul>
<h2>Small gifts under £20</h2>
<p>Diwali often means a gift for everyone in the house. These are easy to wrap and easy to love:</p>
<ul>
<li>[[soft-lip|Deyga Soft Lip Combo]] ({{soft-lip}}): Mint Lip Scrub and Beetroot Lip Balm.</li>
<li>[[lip-nourish|Vilvah Lip Nourishing Kit]] ({{lip-nourish}}): Grapefruit Lip Balm and a lip scrub with cocoa powder and avocado oil.</li>
<li>[[deo|Vilvah Deo Shot Kit]] ({{deo}}): two solid deodorants, Rose &amp; Vanilla and Lavender &amp; Sage.</li>
<li>[[combs|Vilvah Neem Wood Comb Set of 3]] ({{combs}}): fine-tooth, wide-tooth and handle combs in neem wood.</li>
<li>[[hair-duo|Deyga Daily Use Healthy Hair Kit]] ({{hair-duo}}): shampoo and conditioner.</li>
</ul>
<p>More ideas are in <a href="/collections/gifts-under-25">gifts under £25</a>.</p>
<h2>Delivery and returns</h2>
<p>Every order is dispatched from the UK. UK delivery is free on orders over £40, and orders over £70 also get £5 off, applied automatically at checkout. Order early so gifts arrive in time; see our <a href="/policies/shipping-policy">shipping policy</a> for delivery options. Unopened items can be returned within 14 days of delivery, so keep the seal or cellophane on until the gift is opened (see our <a href="/policies/refund-policy">refund policy</a>).</p>""",
    "faq": [
        ["When is Diwali 2026?", "Diwali falls on Sunday 8 November 2026."],
        ["What is a good Diwali gift for someone who loves perfume?",
         "Oud, amber and rose scents suit the festival. Al Haramain Amber Oud Gold Edition is an easy first oud; Boucheron Rose d’Isparta is a rich rose with saffron and amber."],
        ["Are the Deyga and Vilvah gift kits genuine?",
         "Yes. Swansura is an official UK partner of both Deyga and Vilvah, and every order ships from the UK."],
        ["Can Diwali gifts be returned?",
         "Unopened items can be returned within 14 days of delivery. Faulty, damaged or wrong items are refunded or replaced; see our refund policy."],
    ],
}

CHRISTMAS = {
    "title": "Christmas gift guide 2026: perfume, skincare and stocking fillers",
    "handle": "christmas-gift-guide",
    "tag": "Gift guide",
    "summary": "Perfume gift sets for her and him, discovery sets, skincare gift sets and stocking fillers under £25.",
    "mt": "Christmas Gift Guide 2026: Perfume & Skincare | Swansura",
    "md": "Our Christmas gift guide 2026: perfume gift sets for her and him, discovery sets, skincare gift sets and stocking fillers under £25, dispatched from the UK.",
    "shop": ["bloom-set", "most-wanted", "dior-mini", "day-night", "ck-mini", "rain", "milk-face", "tinted"],
    "body": """<p>Christmas shopping is easier with a plan. This <strong>Christmas gift guide</strong> sorts our favourite gifts by who you are buying for and what you want to spend: <strong>perfume gift sets</strong> for her and for him, discovery sets for the friend whose taste you are not sure of, skincare gift sets, and stocking fillers under £25. Everything is 100% authentic and dispatched from the UK, and the full edit is in our <a href="/collections/christmas-gifts">Christmas gifts</a> collection.</p>
<h2>The short answer</h2>
<p>If you know their perfume, buy the <strong>gift set</strong>: you usually get a travel spray or body lotion alongside the full bottle. If you do not, choose a <strong>discovery set</strong> of miniatures. For skincare lovers, a two-step <strong>skincare set</strong> feels generous without guesswork. And fill stockings with miniatures and lip care.</p>
<h2>Perfume gift sets for her</h2>
<ul>
<li>[[bloom-set|Gucci Bloom Eau de Parfum Gift Set]] ({{bloom-set}}): 100ml eau de parfum, a 10ml travel spray and 100ml body lotion; a white floral of jasmine and tuberose.</li>
<li>[[alive|Hugo Boss Alive Eau de Parfum and Body Lotion Set]] ({{alive}}): 80ml eau de parfum with a 75ml matching body lotion for layering.</li>
<li>[[burberry-mini|Burberry Women’s Miniature Perfume Set]] ({{burberry-mini}}): four 5ml minis from the Burberry Her family, including Her London Dream.</li>
<li>[[ck-mini|Calvin Klein Women’s Miniature Fragrance Set]] ({{ck-mini}}): four 15ml bottles with Obsession, Eternity and CK One.</li>
</ul>
<p>See every set in <a href="/collections/gifts-for-her">gifts for her</a> and <a href="/collections/perfume-gift-sets">perfume gift sets</a>.</p>
<h2>Perfume gift sets for him</h2>
<ul>
<li>[[most-wanted|Azzaro The Most Wanted Eau de Toilette Intense Gift Set]] ({{most-wanted}}): a 100ml bottle and two 10ml travel sprays; bergamot, lavender and a moss liquor accord.</li>
<li>[[rain|Bvlgari Man Rain Essence Gift Set]] ({{rain}}): 100ml and 15ml eau de parfum; fresh green tea, white lotus, musk and guaiac wood.</li>
<li>[[dg-mini|Dolce &amp; Gabbana Men’s Miniature Fragrance Set]] ({{dg-mini}}): five minis including K, The One and Light Blue Pour Homme.</li>
<li>[[malaki|Chopard Oud Malaki]] ({{malaki}}): for the man who likes warm scents, with tobacco, leather and oud.</li>
</ul>
<p>More in <a href="/collections/gifts-for-him">gifts for him</a>.</p>
<h2>Not sure what they wear? Choose a discovery set</h2>
<p>Discovery sets are the safest perfume gift: several scents in small sizes, so they can find a favourite. [[dior-mini|Dior Iconics Mini Perfume Discovery Set]] ({{dior-mini}}) has five 5ml Dior fragrances for women and men. [[hermes-mini|Hermès Miniature Gift Set]] ({{hermes-mini}}) holds four 7.5ml scents from the Jardins collection. [[adp-holiday|Acqua di Parma Holiday Discovery Set]] ({{adp-holiday}}) brings Osmanthus, Yuzu and Lily of the Valley in 12ml sprays. On a smaller budget, [[korloff-disc|Korloff Paris Discovery Set]] ({{korloff-disc}}) has three 10ml sprays, and [[sig-disc|Signature Discovery Set]] ({{sig-disc}}) has ten. Wondering what the labels mean? Read <a href="/blogs/journal/extrait-vs-eau-de-parfum">extrait vs eau de parfum</a>.</p>
<h2>Skincare gift sets</h2>
<ul>
<li>[[day-night|Highborn London Ultimate Day &amp; Night Moisture Set]] ({{day-night}}): Imperial Moisturiser and Night Elixir, both in 50ml jars.</li>
<li>[[revive|Highborn London Revive and Defy Starter Set]] ({{revive}}): 30ml Pre-Eminent Beauty Serum and 15ml Imperial Eye Gel.</li>
<li>[[milk-face|Vilvah Milk Face Kit]] ({{milk-face}}): Milk Mud Mask and Milk Drops serum, from one of our official partner brands.</li>
<li>[[sleep|anatomē The Little Gift of Good Sleep]] ({{sleep}}): a 10ml Somali frankincense sleep oil roller ball and a 10ml pillow spray for a calm bedtime ritual.</li>
</ul>
<p>More boxed sets are in <a href="/collections/giftsets">gift sets</a>.</p>
<h2>Stocking fillers under £25</h2>
<ul>
<li>[[bloom-mini|Gucci Bloom Eau de Toilette 10ml]] ({{bloom-mini}})</li>
<li>[[defy-mini|Calvin Klein Defy Parfum 10ml]] ({{defy-mini}})</li>
<li>[[toit|Hermès Un Jardin sur le Toit 15ml]] ({{toit}})</li>
<li>[[tinted|Vilvah Tinted Lip Balm Kit]] ({{tinted}})</li>
<li>[[soft-lip|Deyga Soft Lip Combo]] ({{soft-lip}})</li>
<li>[[lip-scrub|Vilvah Natural Lip Scrub]] ({{lip-scrub}})</li>
<li>[[combs|Vilvah Neem Wood Comb Set of 3]] ({{combs}})</li>
</ul>
<p>Browse all <a href="/collections/stocking-fillers">stocking fillers</a> and <a href="/collections/gifts-under-25">gifts under £25</a>.</p>
<h2>Delivery and returns</h2>
<p>UK delivery is free on orders over £40, and orders over £70 also get £5 off, applied automatically at checkout, so a couple of gifts in one order often covers both. Everything is dispatched from the UK; order early in December so gifts arrive in time, and see our <a href="/policies/shipping-policy">shipping policy</a> for delivery options. Unopened items can be returned within 14 days of delivery, so leave the cellophane on until the big day (see our <a href="/policies/refund-policy">refund policy</a>).</p>""",
    "faq": [
        ["What is the best perfume gift if I don’t know their scent?",
         "A discovery set of miniatures, such as the Dior Iconics Mini Perfume Discovery Set or the Korloff Paris Discovery Set, lets them try several scents and find a favourite."],
        ["Are your perfume gift sets authentic?",
         "Yes. Every product at Swansura is 100% authentic and dispatched from the UK."],
        ["Do you have Christmas gifts under £25?",
         "Yes. Our stocking fillers include perfume miniatures from Gucci, Calvin Klein and Hermès, plus lip care and neem wood combs from Vilvah and Deyga."],
        ["Is delivery free at Christmas?",
         "UK delivery is free on orders over £40, and orders over £70 also get £5 off at checkout."],
    ],
}

out = []
for n, a in enumerate([CHRISTMAS, DIWALI]):
    body = fill(a["body"])
    words = len(re.sub(r"<[^>]+>", " ", body).split())
    shop = [PICK[k] for k in a["shop"]]
    hero = ALL[shop[0]]
    assert len(a["mt"]) <= 60 and len(a["md"]) <= 160, (a["handle"], len(a["mt"]), len(a["md"]))
    out.append({
        "title": a["title"], "handle": a["handle"], "author": {"name": "Swansura"}, "body": body,
        "summary": f"<p>{a['summary']}</p>", "tags": [a["tag"]], "isPublished": False,
        "image": {"url": hero["images"][0]["src"], "altText": a["title"]},
        "metafields": [
            {"namespace": "global", "key": "title_tag", "type": "single_line_text_field", "value": a["mt"]},
            {"namespace": "global", "key": "description_tag", "type": "single_line_text_field", "value": a["md"]},
            {"namespace": "custom", "key": "products", "type": "list.product_reference",
             "value": json.dumps([f"gid://shopify/Product/{ALL[h]['id']}" for h in shop])},
            {"namespace": "custom", "key": "faq", "type": "json", "value": json.dumps(a["faq"], ensure_ascii=False)},
            {"namespace": "custom", "key": "read_minutes", "type": "number_integer", "value": str(max(2, round(words / 200)))},
        ],
    })
    print(a["handle"], words, "words;", len(set(re.findall(r'href="([^"]+)"', body))), "links;", len(a["mt"]), len(a["md"]))
with open(ROOT / "docs/seo/gift_guides_2026-10-27.jsonl", "w") as f:
    for o in out:
        f.write(json.dumps(o, ensure_ascii=False) + "\n")
