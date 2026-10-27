"""Journal guide 'Aloe vera gel: how to use it on your face, hair and body' (user, 27 Oct 2026), as ArticleCreateInput.

Target keyword: 'aloe vera gel' (UK 18,100/mo, KD 16, Semrush Tier 2); 'vilvah aloe vera gel' 20/mo.
Same shape as gift_guides.py: 'Shop the story' in custom.products, FAQs in custom.faq, custom.read_minutes,
SEO in global title/description tags; created unpublished for the client to approve.
Facts come from the product descriptions and the Vilvah INCI list (docs/data/vilvah_inci_2026-10-22.json:
aloe vera juice, xanthan gum, guar gum, Geogard ECT). The product copy's claims (calms acne, anti-bacterial,
soothes sunburn) are NOT repeated (ASA); sunburn and skin conditions are referred to a pharmacist.
Deyga Pure Aloe Vera Gel is sold out on 27 Oct 2026, so it is not linked.

Usage: python3 tools/shopify/guide_aloe_vera.py <allp.json>   (handle -> storefront product, from
/collections/all/products.json pages)
Output: docs/seo/guide_aloe_vera_2026-10-27.jsonl
"""
import json
import re
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
ALL = json.load(open(sys.argv[1]))

PICK = {
    "gel": "vilvah-aloe-vera-gel-100ml-100-pure-multi-purpose-face-skin-hair-gel-soothing-sunburn-hydrating-acne-calming",
    "sensitive": "vilvah-sensitive-skin-set-rose-toner-aloe-vera-gel-calms-redness-soothes-irritation-restores-moisture",
    "oily-kit": "vilvah-anti-acne-kit-honey-fix-face-cleanser-aloe-vera-gel-natural-acne-skincare-combo-for-oily-acne-prone-skin",
    "ff-wash": None, "honey-wash": "vilvah-honey-face-wash-raw-honey-fruit-extracts-100ml",
    "rose-water": "deyga-pure-rose-water-toner-100-ml", "spf": "vilvah-skin-finish-sunscreen-spf-50-pa",
    "serum": None, "milk-drops": None, "lotion": None, "shampoo": None, "comb": None,
}
TITLE = {
    "ff-wash": "Vilvah Fragrance-Free Cream Face Wash", "serum": "Vilvah Anti-Frizz Hair Serum",
    "milk-drops": "Vilvah Milk Drops Hydrating Serum", "lotion": "Vilvah Milk Body Lotion 250ml",
    "shampoo": "Vilvah Goat Milk Shampoo 250ML", "comb": "Neem Wood Comb Set of 3",
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
    ps = {float(v["price"]) for v in ALL[PICK[k]]["variants"] if v["available"]}
    return ("from " if len(ps) > 1 else "") + f"£{min(ps):.2f}".replace(".00", "")


def fill(s):
    s = re.sub(r"\[\[([\w-]+)\|([^\]]+)\]\]", lambda m: f'<a href="/products/{PICK[m.group(1)]}">{m.group(2)}</a>', s)
    return re.sub(r"\{\{([\w-]+)\}\}", lambda m: price(m.group(1)), s)


A = {
    "title": "Aloe vera gel: how to use it on your face, hair and body",
    "handle": "how-to-use-aloe-vera-gel",
    "tag": "Skin Studio",
    "summary": "What to look for in a jar of aloe vera gel, and simple ways to use it on your face, hair and body.",
    "mt": "Aloe Vera Gel: How to Use It on Face, Hair & Body | Swansura",
    "md": "How to use aloe vera gel on your face, hair and body: what to look for in a jar, where it fits in your routine and simple tips for everyday use.",
    "shop": ["gel", "sensitive", "oily-kit", "ff-wash", "rose-water", "spf", "serum", "lotion"],
    "body": """<p><strong>Aloe vera gel</strong> is one of the most searched skincare products in the UK, and it is easy to see why. One jar can work as a light moisturiser, a cooling layer after a day outdoors, a leave-in for hair and an after-shower gel for the body. Here is what to look for when you buy it, and how to use it on your face, hair and body.</p>
<h2>What is aloe vera gel?</h2>
<p>Aloe vera gel comes from the clear, jelly-like inside of the leaves of the aloe plant (<em>Aloe barbadensis</em> on an ingredient list). It is mostly water, which is why it feels so light: it sinks in quickly and does not leave a greasy film. A good gel is clear or very pale, with a soft, wobbly texture that melts when you spread it.</p>
<h2>What to look for in a jar</h2>
<ul>
<li><strong>Aloe first on the list.</strong> The first ingredient should be aloe vera juice or aloe leaf extract, not water.</li>
<li><strong>A short ingredient list.</strong> Aloe gels need little else: a thickener to make the gel and a preservative to keep it safe once opened.</li>
<li><strong>No added fragrance or colour</strong> if your skin is sensitive. A green tint usually means a dye has been added.</li>
</ul>
<p>[[gel|Vilvah Aloe Vera Gel]] (100ml, {{gel}}) ticks all three. Its full ingredient list is just four items: aloe vera juice, xanthan gum, guar gum and Geogard ECT, a natural preservative. It is free from harsh alcohols, silicones and synthetic fragrance, and it is made by Vilvah, one of our official partner brands, and dispatched from the UK.</p>
<h2>How to use aloe vera gel on your face</h2>
<ul>
<li><strong>As a light moisturiser.</strong> After cleansing, smooth a pea-sized amount over damp skin. On oily or combination skin this may be all you need; on dry skin, follow with your usual cream.</li>
<li><strong>Under your serum or cream.</strong> A thin layer first gives your routine extra slip, and serums such as [[milk-drops|Vilvah Milk Drops]] ({{milk-drops}}) spread easily over it.</li>
<li><strong>As a quick mask.</strong> Apply a thicker layer for 10 minutes, then rinse or press the rest into the skin.</li>
<li><strong>After a day outdoors.</strong> A cool layer feels comforting on skin that has had a lot of sun or wind. Keep the jar in the fridge for an extra-cool feel.</li>
</ul>
<p>In the morning, aloe gel is not a sunscreen, so finish with SPF, such as [[spf|Vilvah Skin Finish Sunscreen SPF 50 PA+++]] ({{spf}}).</p>
<h2>A simple routine with aloe vera gel</h2>
<ol>
<li><strong>Cleanse</strong> with a gentle face wash such as [[ff-wash|Vilvah Fragrance-Free Cream Face Wash]] ({{ff-wash}}) or the [[honey-wash|Vilvah Honey Face Wash]] ({{honey-wash}}).</li>
<li><strong>Tone</strong> with a mist of [[rose-water|Deyga Pure Rose Water Toner]] ({{rose-water}}).</li>
<li><strong>Hydrate</strong> with aloe vera gel.</li>
<li><strong>Protect</strong> with sunscreen in the morning, or a richer cream at night if your skin is dry.</li>
</ol>
<p>Prefer it ready-made? The [[sensitive|Vilvah Sensitive Skin Kit]] ({{sensitive}}) pairs a steam-distilled rose toner with the aloe gel, and the [[oily-kit|Vilvah Anti-Acne Kit]] ({{oily-kit}}) pairs the Honey Face Wash with the aloe gel for oily skin. You will find more routines on our <a href="/pages/rituals">routines page</a>.</p>
<h2>How to use aloe vera gel on your hair</h2>
<ul>
<li><strong>As a light leave-in.</strong> Smooth a small amount through damp lengths and ends to tame flyaways and add shine without weighing hair down.</li>
<li><strong>As a soft styling gel.</strong> Use it to smooth a ponytail or define curls, without the crunch of a styling gel.</li>
<li><strong>With a serum.</strong> For very frizzy hair, mix a little gel with a drop of [[serum|Vilvah Anti-Frizz Hair Serum]] ({{serum}}) and comb through with a wide-tooth [[comb|neem wood comb]] ({{comb}}).</li>
</ul>
<p>For more ideas, see our <a href="/collections/hair-serum-for-frizzy-hair">hair serums for frizzy hair</a> and <a href="/collections/haircare">haircare</a>.</p>
<h2>How to use aloe vera gel on your body</h2>
<ul>
<li><strong>After a shower,</strong> as a light, fast-drying layer on warm days.</li>
<li><strong>After shaving or hair removal,</strong> for a cool, fresh feel on the skin.</li>
<li><strong>Under body lotion</strong> on dry skin: let the gel sink in, then lock it in with a cream such as [[lotion|Vilvah Milk Body Lotion]] ({{lotion}}), made with oat milk, ceramides and olive squalane.</li>
</ul>
<h2>Good to know</h2>
<ul>
<li><strong>Patch test first.</strong> Apply a little to your inner arm and wait 24 hours, especially if your skin is sensitive.</li>
<li><strong>Use clean hands or a spatula</strong> and close the jar after use, so the gel stays fresh. Check the pack for how long it lasts once opened.</li>
<li><strong>Sunburn or a skin condition?</strong> Speak to a pharmacist or your GP. Aloe gel is a cosmetic, not a treatment.</li>
</ul>
<p>Explore more <a href="/collections/natural-skincare">natural skincare</a>, or shop by need: <a href="/collections/sensitive-skin">sensitive skin</a>, <a href="/collections/oily-skin">oily skin</a> and <a href="/collections/dry-skin">dry skin</a>.</p>""",
    "faq": [
        ["Can I use aloe vera gel on my face every day?",
         "Yes. Most people can use a gentle aloe vera gel morning and night, as a light moisturiser or under a cream. Patch test first, and add sunscreen in the morning."],
        ["Can I put aloe vera gel in my hair?",
         "Yes. Smooth a small amount through damp lengths and ends as a light leave-in, or use it as a soft styling gel to tame flyaways."],
        ["Is aloe vera gel good for oily skin?",
         "Aloe vera gel is light and non-greasy, so many people with oily or combination skin use it instead of a heavier cream."],
        ["What is in Vilvah Aloe Vera Gel?",
         "Four ingredients: aloe vera juice, xanthan gum, guar gum and Geogard ECT, a natural preservative. It has no harsh alcohols, silicones or synthetic fragrance."],
    ],
}

body = fill(A["body"])
words = len(re.sub(r"<[^>]+>", " ", body).split())
shop = [PICK[k] for k in A["shop"]]
assert len(A["mt"]) <= 60 and len(A["md"]) <= 160, (len(A["mt"]), len(A["md"]))
out = {
    "title": A["title"], "handle": A["handle"], "author": {"name": "Swansura"}, "body": body,
    "summary": f"<p>{A['summary']}</p>", "tags": [A["tag"]], "isPublished": False,
    "image": {"url": ALL[shop[0]]["images"][0]["src"], "altText": A["title"]},
    "metafields": [
        {"namespace": "global", "key": "title_tag", "type": "single_line_text_field", "value": A["mt"]},
        {"namespace": "global", "key": "description_tag", "type": "single_line_text_field", "value": A["md"]},
        {"namespace": "custom", "key": "products", "type": "list.product_reference",
         "value": json.dumps([f"gid://shopify/Product/{ALL[h]['id']}" for h in shop])},
        {"namespace": "custom", "key": "faq", "type": "json", "value": json.dumps(A["faq"], ensure_ascii=False)},
        {"namespace": "custom", "key": "read_minutes", "type": "number_integer", "value": str(max(2, round(words / 200)))},
    ],
}
print(A["handle"], words, "words;", len(set(re.findall(r'href="([^"]+)"', body))), "links;", len(A["mt"]), len(A["md"]))
with open(ROOT / "docs/seo/guide_aloe_vera_2026-10-27.jsonl", "w") as f:
    f.write(json.dumps(out, ensure_ascii=False) + "\n")
