"""Journal guide 'Best perfume gift sets UK 2026: for her, for him and under £30' (user, 9 Nov 2026: "Go ahead
with the gift guides", plan item 5 in docs/seo/SEO_Orders_Audit_2026-11-09.md).

Targets the dated gift-guide format that ranks next to category pages (competitor_research_2026-11-09.md:
P-Eleven 'Best Perfume Gift Sets UK 2026', LOOKFANTASTIC / Superdrug 'perfume gift sets for her', Next / Notino
'aftershave gift sets'). No Semrush volume for these heads yet (not in our batches). Supports the 9 Nov gift
collections perfume-gift-sets-for-her / aftershave-gift-sets-for-him / gifts-under-50 / black-friday.
Facts = the products' own descriptions and titles (storefront dump of 9 Nov). Left out: longevity, 'long-lasting',
hype, discount claims (no Black Friday discount exists), last-order dates (client to confirm).
Prices are written into the text: re-run the generator and update the body if prices change.

Usage: python3 tools/shopify/guide_perfume_gift_sets.py <allp.json>   (handle -> storefront product)
Output: docs/seo/guide_perfume_gift_sets_2026-11-09.jsonl
"""
import json
import sys

from journal_lib import build

A = {
    "title": "Best perfume gift sets UK 2026: for her, for him and under £30",
    "handle": "best-perfume-gift-sets-uk-2026",
    "tag": "Gift guide",
    "summary": "Our pick of perfume gift sets for Christmas 2026: full-bottle sets and miniature sets for her, aftershave gift sets for him, discovery sets for anyone, and gifts under £30.",
    "mt": "Perfume Gift Sets UK 2026: Her, Him & Under £30 | Swansura",
    "md": "Our pick of perfume gift sets for Christmas 2026: sets for her, aftershave gift sets for him, discovery sets and gifts under £30, shipped from the UK.",
    "pick": {
        "bloom": "gucci-bloom-eau-de-parfum-gift-set-100ml-10ml-body-lotion-100ml-women-s-fragrance-set",
        "nomade": "chloe-nomade-eau-de-parfum-gift-set-75ml-20ml-travel-spray-women-s-floral-chypre-fragrance-set",
        "theone": "dolce-gabbana-the-one-for-women-eau-de-parfum-gift-set-50ml-50ml-luxury-women-s-fragrance-set",
        "lumiere": "elie-saab-le-parfum-lumiere-eau-de-parfum-gift-set-90ml-10ml-body-lotion-75ml-women-s-fragrance-set",
        "guilty": "gucci-guilty-pour-femme-eau-de-parfum-gift-set-50ml-body-lotion-50ml-women-s-fragrance-set",
        "girlnow": "elie-saab-girl-of-now-lovely-eau-de-parfum-gift-set-50ml-body-lotion-75ml-new-pack-women-s-fragrance-set",
        "chloemini": "chloe-women-s-miniature-perfume-set-4x5ml-nomade-edt-rose-tangerine-edt-chloe-edp-nomade-edp",
        "jcmini": "jimmy-choo-women-s-miniature-fragrance-gift-set-5x4-5ml-5-piece-perfume-collection",
        "mjmini": "marc-jacobs-women-s-miniature-fragrance-gift-set-2025-daisy-daisy-eau-so-fresh-perfect-daisy-wild",
        "dgwmini": "dolce-gabbana-women-s-miniature-fragrance-set-devotion-q-blue-jasmine-the-one-light-blue",
        "dknymini": "product-title-dkny-women-s-miniature-eau-de-parfum-set-4x7ml-be-delicious-golden-delicious-be-extra-delicious-be-100-delicious",
        "sauvage": "dior-sauvage-eau-de-parfum-100ml-10ml-men-s-gift-set",
        "glacial": "bvlgari-man-glacial-essence-eau-de-parfum-gift-set-100ml-15ml-men-s-fragrance-set",
        "terrae": "bvlgari-man-terrae-essence-eau-de-parfum-gift-set-100ml-15ml-new-pack-men-s-fragrance-set",
        "wood": "bvlgari-man-wood-essence-eau-de-parfum-gift-set-100ml-15ml-soft-box-men-s-fragrance-set",
        "azzaro": "azzaro-the-most-wanted-eau-de-toilette-intense-gift-set-100ml-2x10ml-men-s-fragrance-set",
        "k": "dolce-gabbana-k-eau-de-parfum-gift-set-50ml-5ml-men-s-fragrance-set",
        "dgmmini": "dolce-gabbana-men-s-miniature-fragrance-set-devotion-k-edt-k-edp-the-one-light-blue-pour-homme",
        "dior5": "dior-iconics-mini-perfume-discovery-set-5-x-5ml",
        "hermes": "hermes-miniature-edt-gift-set-4-x-7-5ml-unisex-fragrances",
        "chopard": "chopard-gardens-of-paradise-discovery-set-4x10ml-luxury-unisex-eau-de-parfum-gift-set",
        "adp": "acqua-di-parma-blu-mediterraneo-discovery-set-3x12ml",
        "korloff": "korloff-paris-discovery-set-eau-de-parfum-3x10ml",
        "jasmine": "trussardi-pure-jasmine-lifestyle-mini-gift-set-eau-de-parfum-60ml-10ml-7ml",
        "ruby": "trussardi-ruby-red-eau-de-parfum-gift-set-60ml-stardust-body-emulsion-125ml-women-s-fragrance-set",
        "bloommini": "gucci-bloom-parfum-10ml-miniature-luxury-women-s-floral-fragrance",
        "eternity": "calvin-klein-eternity-parfum-10ml-miniature-men-s-warm-aromatic-fragrance",
        "defy": "calvin-klein-defy-parfum-10ml-miniature-men-s-warm-woody-fragrance",
    },
    "shop": ["bloom", "nomade", "chloemini", "sauvage", "glacial", "dgmmini", "hermes", "jasmine"],
    "body": """<p>A perfume gift set is the easiest way to give someone a scent they already love, with something extra in the box: a travel spray, a matching body lotion or a few miniatures. This guide is our pick of the <a href="/collections/perfume-gift-sets">perfume gift sets</a> in stock for Christmas 2026, sorted by who you are buying for and what you want to spend. Every set is 100% authentic and shipped from the UK.</p>
<h2>How to choose a perfume gift set</h2>
<ul>
<li><strong>You know their perfume:</strong> buy the set of that scent. A full bottle with a travel spray or lotion costs little more than the bottle alone.</li>
<li><strong>You know the brand, not the scent:</strong> a miniature set lets them try several perfumes from the same house.</li>
<li><strong>You know neither:</strong> choose a discovery set, then they can buy the full bottle of the one they like.</li>
</ul>
<h2>Perfume gift sets for her</h2>
<p>Full-bottle sets, from the biggest box down:</p>
<ul>
<li>[[bloom|Gucci Bloom Eau de Parfum Gift Set]] ({{bloom}}): 100ml eau de parfum, a 10ml travel spray and a 100ml body lotion. A creamy white floral of jasmine and tuberose.</li>
<li>[[nomade|Chloé Nomade Gift Set]] ({{nomade}}): a 75ml eau de parfum and a 20ml travel spray. Mirabelle plum, freesia and oakmoss, a floral chypre that suits the office as well as an evening out.</li>
<li>[[theone|Dolce &amp; Gabbana The One for Women Gift Set]] ({{theone}}): two 50ml bottles of a fruity amber floral with peach, lychee, jasmine and vanilla. One for home, one for her bag.</li>
<li>[[lumiere|Elie Saab Le Parfum Lumière Gift Set]] ({{lumiere}}): 90ml eau de parfum, a 10ml spray and a 75ml body lotion, with orange blossom, jasmine and tuberose.</li>
<li>[[guilty|Gucci Guilty Pour Femme Gift Set]] ({{guilty}}): 50ml eau de parfum with a 50ml body lotion. Lilac, rose and violet over patchouli.</li>
<li>[[girlnow|Elie Saab Girl of Now Lovely Gift Set]] ({{girlnow}}): 50ml eau de parfum and a 75ml body lotion, a sweeter scent of red berries, rose, almond and vanilla.</li>
</ul>
<p>Miniature sets, for trying a whole range: [[chloemini|Chloé Women’s Miniature Set (4 x 5ml)]] ({{chloemini}}), [[jcmini|Jimmy Choo Women’s Miniature Set (5 x 4.5ml)]] ({{jcmini}}), [[mjmini|Marc Jacobs Daisy and Perfect Miniature Set]] ({{mjmini}}), [[dgwmini|Dolce &amp; Gabbana Women’s Miniature Set]] ({{dgwmini}}) with Devotion, Q, Blue Jasmine, The One and Light Blue, and [[dknymini|DKNY Delicious Miniature Set (4 x 7ml)]] ({{dknymini}}). See them all in <a href="/collections/perfume-gift-sets-for-her">perfume gift sets for her</a>.</p>
<h2>Aftershave gift sets for him</h2>
<ul>
<li>[[sauvage|Dior Sauvage Eau de Parfum 100ml + 10ml]] ({{sauvage}}): bergamot and Sichuan pepper over vanilla and ambroxan. If you only know he likes a fresh, popular scent, this is the safe choice. Our <a href="/blogs/journal/dior-sauvage-edt-vs-edp-vs-parfum">Sauvage EDT vs EDP vs Parfum guide</a> explains the versions.</li>
<li>[[glacial|Bvlgari Man Glacial Essence 100ml + 15ml]] ({{glacial}}): juniper, ginger and geranium over clean woods. Crisp and easy to wear every day.</li>
<li>[[terrae|Bvlgari Man Terrae Essence 100ml + 15ml]] ({{terrae}}): citron and calamansi over vetiver, orris and an earthy, resinous base.</li>
<li>[[wood|Bvlgari Man Wood Essence 100ml + 15ml]] ({{wood}}): citrus, coriander, cypress and vetiver, a green woody scent.</li>
<li>[[azzaro|Azzaro The Most Wanted Intense Gift Set]] ({{azzaro}}): a 100ml eau de toilette and two 10ml travel sprays, with bergamot, lavender and a moss liquor accord.</li>
<li>[[k|Dolce &amp; Gabbana K Eau de Parfum 50ml + 5ml]] ({{k}}): blood orange, lemon and juniper, then sage and lavender over cedarwood.</li>
</ul>
<p>For a man who likes to switch, the [[dgmmini|Dolce &amp; Gabbana Men’s Miniature Set]] ({{dgmmini}}) holds Devotion, K in two versions, The One and Light Blue Pour Homme. More in <a href="/collections/aftershave-gift-sets-for-him">aftershave gift sets for him</a>.</p>
<h2>Discovery sets for anyone</h2>
<p>When you do not know their taste, a discovery set is the kindest gift. [[dior5|Dior Iconics Mini Set (5 x 5ml)]] ({{dior5}}) has J’adore, Miss Dior, Hypnotic Poison and Sauvage. [[hermes|Hermès Miniature Set (4 x 7.5ml)]] ({{hermes}}) holds four unisex scents from the Jardins collection. [[chopard|Chopard Gardens of Paradise (4 x 10ml)]] ({{chopard}}) holds Orange Mauresque, Miel d’Arabie, Jasmin Moghol and Rose Seljuke, and [[adp|Acqua di Parma Blu Mediterraneo (3 x 12ml)]] ({{adp}}) three bright Mediterranean scents. Not sure what EDP or EDT means on the box? Read <a href="/blogs/journal/extrait-vs-eau-de-parfum">extrait vs eau de parfum</a>.</p>
<h2>Perfume gift sets under £30</h2>
<ul>
<li>[[korloff|Korloff Paris Discovery Set (3 x 10ml)]] ({{korloff}}): three women’s scents, from fresh and fruity to soft and warm.</li>
<li>[[jasmine|Trussardi Pure Jasmine Gift Set]] ({{jasmine}}): a 60ml eau de parfum plus 10ml and 7ml minis, jasmine with bergamot, pistachio and vanilla.</li>
<li>[[ruby|Trussardi Ruby Red Gift Set]] ({{ruby}}): a 60ml eau de parfum with a 125ml body emulsion.</li>
<li>Single 10ml minis in a gift-ready size: [[bloommini|Gucci Bloom Parfum]] ({{bloommini}}) for her, [[eternity|Calvin Klein Eternity Parfum]] ({{eternity}}) or [[defy|Calvin Klein Defy Parfum]] ({{defy}}) for him.</li>
</ul>
<p>For more under a budget, see <a href="/collections/gifts-under-50">gifts under £50</a> and <a href="/collections/gifts-under-25">gifts under £25</a>, or our <a href="/blogs/journal/christmas-gift-guide">Christmas gift guide</a> for skincare and stocking fillers too.</p>
<h2>Good to know</h2>
<ul>
<li>Every set is 100% authentic and shipped from the UK.</li>
<li>UK delivery is free on orders over £40, and orders over £70 get £5 off at checkout. Shopping around Black Friday? Our <a href="/collections/black-friday">Black Friday edit</a> gathers in-stock gift sets in one place.</li>
<li>We hold limited stock of each set, so buy early if you have one in mind.</li>
</ul>""",
    "faq": [
        ["What is the best perfume gift set for her?",
         "If you know her perfume, buy the gift set of that scent. If you do not, a miniature set such as the Chloé or Jimmy Choo minis lets her try several perfumes and find a favourite."],
        ["What is a good aftershave gift set for him?",
         "Dior Sauvage Eau de Parfum 100ml + 10ml is the classic choice. Bvlgari Man Glacial, Terrae and Wood Essence each come with a 15ml travel spray, and the Dolce & Gabbana men’s minis hold five scents."],
        ["Are there perfume gift sets under £30?",
         "Yes: the Korloff Paris Discovery Set, the Trussardi Pure Jasmine and Ruby Red sets, and 10ml minis from Gucci and Calvin Klein."],
        ["Are the gift sets genuine?",
         "Yes. Every product at Swansura is 100% authentic and shipped from the UK, with free UK delivery on orders over £40."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_perfume_gift_sets_2026-11-09.jsonl")
