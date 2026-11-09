"""Journal guide 'Stocking fillers for her under £25: perfume minis, lip care and soaps' (user, 9 Nov 2026:
"Go ahead with the gift guides", plan item 5 in docs/seo/SEO_Orders_Audit_2026-11-09.md).

Targets 'stocking fillers for her' (M&S, NOTHS, Cult Beauty guides rank; price-capped, dated). No Semrush volume yet.
Supports /collections/stocking-fillers, gifts-under-25, lip-balm, lip-scrub, goat-milk-soap, travel-size-minis.
Facts = the products' own descriptions (storefront dump of 9 Nov). Left out (ASA): every claim in older product
copy (stretch marks, dark circles, pigmentation, cracked heels, sleep), longevity, hype.
Prices are written into the text: re-run the generator and update the body if prices change.

Usage: python3 tools/shopify/guide_stocking_fillers.py <allp.json>   (handle -> storefront product)
Output: docs/seo/guide_stocking_fillers_2026-11-09.jsonl
"""
import json
import sys

from journal_lib import build

A = {
    "title": "Stocking fillers for her under £25: perfume minis, lip care and soaps",
    "handle": "stocking-fillers-for-her-under-25",
    "tag": "Gift guide",
    "summary": "Small gifts she will use: designer perfume minis, lip balms and scrubs, goat milk soaps and bath treats, all under £25 and shipped from the UK.",
    "mt": "Stocking Fillers for Her Under £25 UK 2026 | Swansura",
    "md": "Stocking fillers for her under £25: designer perfume minis, lip balms and scrubs, goat milk soaps and bath treats. 100% authentic, sent from the UK.",
    "pick": {
        "bloom": "gucci-bloom-parfum-10ml-miniature-luxury-women-s-floral-fragrance",
        "euphoria": "calvin-klein-my-euphoria-eau-de-parfum-10ml-miniature-women-s-floral-gourmand-fragrance",
        "daisy": "marc-jacobs-daisy-love-eau-de-toilette-10ml-miniature-women-s-floral-fruity-fragrance",
        "fortune": "viktor-rolf-good-fortune-eau-de-parfum-10ml-miniature-women-s-floral-fragrance",
        "choo": "jimmy-choo-i-want-choo-forever-eau-de-parfum-4-5ml-miniature-women-s-floral-gourmand-fragrance",
        "jasmine": "trussardi-pure-jasmine-eau-de-parfum-7ml-miniature-women-s-floral-fragrance",
        "toit": "hermes-un-jardin-sur-le-toit-eau-de-toilette-15ml-miniature-unisex-fragrance",
        "korloff": "korloff-paris-discovery-set-eau-de-parfum-3x10ml",
        "grape": "vilvah-grape-fruit-lip-balm-10g",
        "vscrub": "vilvah-natural-lip-scrub-10-g-lemon-shea-butter-exfoliator-for-pigmented-dry-chapped-lips-gentle-sugar-polish-for-soft-even-lips",
        "spf": "vilvah-milk-lip-balm-spf-30-pa-natural-uv-protection-hydrating-lip-care-for-all-skin-types",
        "dbalm": "deyga-natural-vanilla-lip-balm-8g",
        "straw": "strawberry-lip-scrub-16g-deygas-natural-exfoliating-lip-care-avocado-almond-oils-shea-butter-and-vitamin-e-hydrates-softens-smooths-lips",
        "softlip": "deyga-soft-lip-combo",
        "lipkit": "vilvah-lip-nourishing-kit-grapefruit-lip-balm-lip-scrub-exfoliates-hydrates-softens-natural-tint-shea-butter-graperfruit-avocado-oil",
        "rose": "classic-rose-goat-milk-soap-bar-125g",
        "classic": "classic-goatmilk-soap-bar-115g",
        "mint": "cucumber-curd-mint-soap-bar-115g",
        "saffron": "deyga-shea-saffron-bath-bar-100g",
        "pinkclay": "deyga-rose-pink-clay-bath-bar-100g",
        "salts": "relax-sleep-chamomile-bath-salts",
        "wildrose": "vilvah-wild-rose-face-mask-100ml-natural-brightening-clay-mask-for-even-skin-tone-deep-hydration",
        "footbutter": "foot-butter-40-g-deygas-deep-moisture-butter-for-dry-cracked-heels-rough-feet",
        "deo": "vilvah-deo-shot-kit-pocket-size-solid-deodorant-bundle-rose-vanilla-lavender-sage-natural-butters-essential-oils-for-day-to-night-freshness",
    },
    "shop": ["bloom", "euphoria", "choo", "softlip", "lipkit", "rose", "saffron", "wildrose"],
    "body": """<p>The best stocking fillers are small things she will actually use: a mini of a perfume she loves, a lip balm for her coat pocket, a good soap. Everything in this guide costs under £25, is 100% authentic and ships from the UK, so you can fill a whole stocking from one order. For the full range, see our <a href="/collections/stocking-fillers">stocking fillers</a> and <a href="/collections/gifts-under-25">gifts under £25</a>.</p>
<h2>Designer perfume minis</h2>
<p>A miniature is a lovely way to give a designer scent on a small budget, and it fits in a handbag afterwards.</p>
<ul>
<li>[[bloom|Gucci Bloom Parfum 10ml]] ({{bloom}}): the richest Bloom, with tuberose and jasmine over vanilla and Peru balsam.</li>
<li>[[euphoria|Calvin Klein My Euphoria 10ml]] ({{euphoria}}): blackcurrant, orchid and rose over vanilla and amber, sweet and warm.</li>
<li>[[daisy|Marc Jacobs Daisy Love 10ml]] ({{daisy}}): cloudberry and daisy over cashmere musk, light and cheerful for daytime.</li>
<li>[[fortune|Viktor &amp; Rolf Good Fortune 10ml]] ({{fortune}}): fennel and jasmine over bourbon vanilla.</li>
<li>[[choo|Jimmy Choo I Want Choo Forever 4.5ml]] ({{choo}}) and [[jasmine|Trussardi Pure Jasmine 7ml]] ({{jasmine}}): the smallest budgets, still in a proper bottle.</li>
<li>[[toit|Hermès Un Jardin sur le Toit 15ml]] ({{toit}}): apple, pear and rose with a green grass accord.</li>
</ul>
<p>If she likes to try a few, the [[korloff|Korloff Paris Discovery Set (3 x 10ml)]] ({{korloff}}) holds three scents in one box. More in <a href="/collections/travel-size-minis">travel size and mini perfumes</a>.</p>
<h2>Lip balms and lip scrubs</h2>
<p>Lip care is the classic stocking filler: cheap, useful and welcome in winter.</p>
<ul>
<li>[[grape|Vilvah Grapefruit Lip Balm]] ({{grape}}): shea butter, avocado and almond oils with a sheer tint and a zesty scent.</li>
<li>[[spf|Vilvah Milk Lip Balm SPF 30 PA+++]] ({{spf}}): mineral filters with shea, soy and kokum butters, for winter walks and ski trips.</li>
<li>[[dbalm|Deyga Natural Lip Balm]] ({{dbalm}}): almond oil, jojoba and shea butter, in vanilla or shea.</li>
<li>[[vscrub|Vilvah Lip Scrub]] ({{vscrub}}) or [[straw|Deyga Strawberry Lip Scrub]] ({{straw}}): sugar in plant oils and butter to buff away dry flakes.</li>
<li>Ready-made pairs: [[lipkit|Vilvah Lip Nourishing Kit]] ({{lipkit}}), a lip scrub and grapefruit balm, and [[softlip|Deyga Soft Lip Combo]] ({{softlip}}), a mint lip scrub and beetroot balm.</li>
</ul>
<p>Our <a href="/blogs/journal/how-to-use-lip-scrub">lip scrub guide</a> explains how to use them, and every balm and scrub is in <a href="/collections/lip-balm">lip balm and lip care</a>.</p>
<h2>Goat milk soaps and bath bars</h2>
<p>A handmade soap looks generous wrapped in tissue and costs very little. Vilvah’s goat milk bars are made with farm-fresh goat milk: [[rose|Classic Rose Goat Milk Soap]] ({{rose}}) with rose petals and pink clay, and [[classic|Classic Goat Milk Soap]] ({{classic}}) with lavender essential oil; see them all in <a href="/collections/goat-milk-soap">goat milk soap</a>. For a fresh morning shower, [[mint|Cucumber, Curd &amp; Mint Soap]] ({{mint}}) is made with curd and mint. From Deyga, the [[saffron|Shea Saffron Bath Bar]] ({{saffron}}) and [[pinkclay|Rose Pink Clay Bath Bar]] ({{pinkclay}}) are made with raw shea butter and coconut and olive oils.</p>
<h2>Small pamper gifts</h2>
<ul>
<li>[[wildrose|Vilvah Wild Rose Face Mask]] ({{wildrose}}): three ingredients, aloe vera, French pink clay and rose hydrosol, for a 15-minute Sunday mask.</li>
<li>[[footbutter|Deyga Foot Butter]] ({{footbutter}}): coconut oil, olive oil and beeswax with a soft vanilla scent, for feet after a long day in boots.</li>
<li>[[salts|anatomē Chamomile Bath Salts]] ({{salts}}): natural salts with organic botanicals for a slow evening bath, in a refill pouch or a jar.</li>
<li>[[deo|Vilvah Deo Shot Kit]] ({{deo}}): two pocket-size solid deodorants, Rose &amp; Vanilla and Lavender &amp; Sage.</li>
</ul>
<h2>How to fill a stocking for around £50</h2>
<p>One perfume mini, one lip balm, one lip scrub and a soap comes to about £43 to £51 with the picks above. That also takes the order over £40, so UK delivery is free. For bigger gifts, read our <a href="/blogs/journal/best-perfume-gift-sets-uk-2026">perfume gift sets guide</a> or the <a href="/blogs/journal/christmas-gift-guide">Christmas gift guide</a>.</p>
<h2>Good to know</h2>
<ul>
<li>Patch test new skincare before first use, especially products with essential oils.</li>
<li>Every product is 100% authentic and shipped from the UK. Swansura is an official UK partner of Deyga and Vilvah.</li>
<li>UK delivery is free on orders over £40, and orders over £70 get £5 off at checkout.</li>
</ul>""",
    "faq": [
        ["What are good stocking fillers for her under £25?",
         "Designer perfume minis such as Gucci Bloom or Calvin Klein My Euphoria, lip balms and lip scrubs from Vilvah and Deyga, handmade goat milk soaps and small pamper gifts such as a clay face mask."],
        ["What are good stocking fillers under £10?",
         "Vilvah lip balms and the Vilvah lip scrub, the Deyga Natural Lip Balm and the Vilvah soap bars are all under £10."],
        ["Are perfume miniatures real perfume?",
         "Yes. The minis are the brand’s own perfume in a smaller bottle, 100% authentic and shipped from the UK."],
        ["How do I get free delivery on stocking fillers?",
         "UK delivery is free on orders over £40, so a few stocking fillers in one order usually qualify."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_stocking_fillers_2026-11-09.jsonl")
