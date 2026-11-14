"""Journal guide 'Gucci perfume: Bloom, Flora Gorgeous, Guilty and Intense Oud compared' (user, 16 Nov 2026: 'Write the next 2 Journal guides').

Semrush UK: gucci perfume 18,100 (KD 41), gucci flora gorgeous gardenia 4,400 (KD 29), gucci guilty pour homme 1,600
(KD 23), gucci perfume for women 1,000 (KD 33), gucci perfume for men 880 (KD 15). No Gucci guide yet; 10 of the 13
Gucci listings in stock on 16 Nov (storefront dump allp_map_1116.json). Sold out, linked in the text only: Bloom Parfum
10ml, Guilty Pour Femme EDP 10ml. The 4x5ml Guilty / Flora / Bloom set (sold out) is not linked.
Facts = each product's stored notes (custom.sw + description, Admin read 16 Nov 2026). Intense Oud is covered in the oud
guide (linked, not repeated). No longevity / projection / 'dupe' / 'iconic' / 'most popular' wording, no launch dates or
designer history (not in our data). Prices are written into the text: re-run the generator and update the body if prices change.

Usage: python3 tools/shopify/guide_gucci.py <allp_map.json>   (handle -> storefront product)
Output: docs/seo/guide_gucci_2026-11-16.jsonl
"""
import json
import sys

from journal_lib import build

G = "gucci-"
A = {
    "title": "Gucci perfume: Bloom, Flora Gorgeous, Guilty and Intense Oud compared",
    "handle": "gucci-perfume-guide",
    "tag": "Scent Studio",
    "summary": "Every Gucci fragrance we stock, side by side: the Bloom family, Flora Gorgeous Gardenia, Orchid and Magnolia, Guilty for her and for him, and Intense Oud.",
    "mt": "Gucci Perfume: Bloom, Flora Gorgeous and Guilty | Swansura",
    "md": "Gucci Bloom, Flora Gorgeous Gardenia, Guilty and Intense Oud compared: the notes, the sizes and which Gucci perfume to choose.",
    "pick": {
        "bloomset": G + "bloom-eau-de-parfum-gift-set-100ml-10ml-body-lotion-100ml-women-s-fragrance-set",
        "bloomedt": G + "bloom-eau-de-toilette-10ml-miniature-women-s-floral-perfume",
        "profumo": G + "bloom-profumo-di-fiori-eau-de-parfum-10ml-pen-spray-women-s-floral-fragrance",
        "bloomparfum": G + "bloom-parfum-10ml-miniature-luxury-women-s-floral-fragrance",
        "gardenia": G + "flora-gorgeous-gardenia-eau-de-parfum-50ml-women-s-floral-fragrance",
        "orchid": G + "flora-gorgeous-orchid-eau-de-parfum-10ml-miniature-women-s-floral-gourmand-fragrance",
        "floraset": G + "flora-gorgeous-miniature-perfume-set-3x5ml-gardenia-magnolia-orchid",
        "duoset": G + "women-s-miniature-perfume-set-4x5ml-bloom-edp-flora-gorgeous-gardenia-edp",
        "guiltyset": G + "guilty-pour-femme-eau-de-parfum-gift-set-50ml-body-lotion-50ml-women-s-fragrance-set",
        "guiltymini": G + "guilty-pour-femme-eau-de-parfum-10ml-miniature-women-s-fragrance",
        "homme": G + "guilty-pour-homme-eau-de-toilette-90ml-men-s-woody-aromatic-fragrance",
        "oud": G + "intense-oud-eau-de-parfum-90ml-luxury-unisex-oud-fragrance",
    },
    "titles": {},
    "soldout": ["bloomparfum", "guiltymini"],
    "shop": ["bloomset", "gardenia", "guiltyset", "homme", "oud", "floraset", "bloomedt", "orchid"],
    "body": """<p>Gucci's fragrances fall into a few clear lines: Bloom, a family of white florals; Flora Gorgeous, three sweeter, brighter florals; Guilty, with a version for her and one for him; and Intense Oud, a darker unisex scent. Here is every <strong>Gucci perfume</strong> we stock, with its notes, the sizes on offer and who each one suits.</p>
<h2>Gucci Bloom: a family of white florals</h2>
<p>Every Bloom fragrance is built around jasmine, tuberose and Rangoon creeper, a climbing flower with a soft, almondy scent. The versions differ in what surrounds those flowers:</p>
<ul>
<li>[[bloomset|Gucci Bloom Eau de Parfum]] is the full, creamy original, here in a gift set ({{bloomset}}) with a 100ml bottle, a 10ml travel spray and a 100ml body lotion for layering.</li>
<li>[[bloomedt|Bloom Eau de Toilette]] ({{bloomedt}}, 10ml) is the lightest: neroli, bergamot and mandarin brighten the flowers, over musk and sandalwood. An easy daytime floral.</li>
<li>[[profumo|Bloom Profumo di Fiori]] ({{profumo}}, 10ml pen spray) adds ylang-ylang to the bouquet, over sandalwood, benzoin, orris and musk: lusher and more golden.</li>
<li>[[bloomparfum|Bloom Parfum]] (10ml, currently out of stock) is the richest, with apricot and cardamom at the top and vanilla, a sweet moss accord and Peru balsam underneath.</li>
</ul>
<p>Want two Bloom minis plus two of Flora Gorgeous Gardenia? The [[duoset|Gucci women's miniature set]] ({{duoset}}) holds four 5ml bottles.</p>
<h2>Gucci Flora Gorgeous: sweeter, brighter florals</h2>
<p>[[gardenia|Gucci Flora Gorgeous Gardenia Eau de Parfum]] ({{gardenia}}, 50ml) centres on white gardenia and jasmine grandiflorum, with pear blossom for a light fruity touch and a brown sugar accord for softness. Bright rather than heavy, it suits sunny days, brunch and the office.</p>
<p>[[orchid|Flora Gorgeous Orchid]] ({{orchid}}, 10ml) is the creamy one: a vanilla duo and vanilla orchid, lifted by an airy ozonic accord. A cosy choice for winter evenings.</p>
<p>Can't decide? The [[floraset|Flora Gorgeous Miniature Set]] ({{floraset}}) has 5ml each of Gardenia, Orchid and Magnolia. Magnolia, only in the set, is the fruitiest: dewberries and coconut with magnolia and jasmine sambac, over patchouli and blond woods.</p>
<h2>Gucci Guilty: for her and for him</h2>
<p>The [[guiltyset|Gucci Guilty Pour Femme Eau de Parfum Gift Set]] ({{guiltyset}}) pairs a 50ml bottle with a 50ml body lotion. It opens with mandora, bergamot and pink pepper, has a powdery heart of lilac, rose, violet and geranium, and settles on patchouli and amber: a warm floral amber for evenings and cooler months. The 10ml [[guiltymini|Guilty Pour Femme mini]] is currently out of stock.</p>
<p>[[homme|Gucci Guilty Pour Homme Eau de Toilette]] ({{homme}}, 90ml) is fresh and aromatic: Italian lemon and pink pepper, then orange blossom, neroli and French lavender, over patchouli and cedarwood. Clean and easy to wear, it suits the office, weekends and warmer days.</p>
<h2>Gucci Intense Oud</h2>
<p>[[oud|Gucci Intense Oud Eau de Parfum]] ({{oud}}, 90ml) is the darkest Gucci we stock and is unisex: black pepper and olibanum (frankincense) open it, amber woods, sandalwood and cedarwood follow, and leather, patchouli, gurjun balsam and an oud accord make the base. Our <a href="/blogs/journal/oud-perfume-guide">oud perfume guide</a> compares it with Tom Ford Oud Wood and other oud fragrances.</p>
<h2>Which Gucci perfume should you choose?</h2>
<ul>
<li><strong>You love classic white flowers:</strong> Bloom eau de parfum, or the Bloom eau de toilette for something lighter.</li>
<li><strong>You want a bright, cheerful floral:</strong> Flora Gorgeous Gardenia.</li>
<li><strong>You like vanilla and soft sweetness:</strong> Flora Gorgeous Orchid.</li>
<li><strong>You prefer a warmer, powdery evening scent:</strong> Guilty Pour Femme.</li>
<li><strong>Buying for him:</strong> Guilty Pour Homme for fresh and clean, Intense Oud for smoky and woody.</li>
<li><strong>You want to try before you commit:</strong> one of the 10ml minis or a 5ml set.</li>
</ul>
<h2>Good to know</h2>
<ul>
<li><strong>Eau de toilette, eau de parfum or parfum?</strong> Our guide to <a href="/blogs/journal/extrait-vs-eau-de-parfum">extrait vs eau de parfum</a> explains the labels.</li>
<li><strong>Layering:</strong> the Bloom and Guilty Pour Femme sets come with a matching body lotion; apply the lotion first and spray over it.</li>
<li><strong>As a gift:</strong> see our <a href="/blogs/journal/best-perfume-gift-sets-uk-2026">perfume gift sets guide</a> and <a href="/blogs/journal/mini-perfume-sets-guide">mini perfume sets guide</a>.</li>
<li><strong>Every bottle is 100% authentic</strong> and dispatched from the UK, with free UK delivery over £40.</li>
</ul>
<p>Shop every <a href="/collections/gucci">Gucci</a> fragrance, or browse <a href="/collections/perfume-for-women">perfume for women</a>, <a href="/collections/perfume-for-men">perfume for men</a> and <a href="/collections/scent-floral">floral fragrances</a>.</p>""",
    "faq": [
        ["What does Gucci Bloom smell like?",
         "Gucci Bloom is a white floral built around jasmine, tuberose and Rangoon creeper. The eau de toilette adds neroli, bergamot and mandarin for a lighter feel; Profumo di Fiori adds ylang-ylang over sandalwood and orris; the Parfum adds apricot and cardamom over vanilla and Peru balsam."],
        ["What is the difference between Gucci Bloom and Flora Gorgeous Gardenia?",
         "Bloom is a creamy white floral of jasmine and tuberose. Flora Gorgeous Gardenia is brighter and sweeter, with pear blossom, white gardenia and jasmine over a brown sugar accord."],
        ["Which Gucci perfume is for men?",
         "We stock Gucci Guilty Pour Homme Eau de Toilette, a fresh aromatic scent with Italian lemon, pink pepper, neroli and lavender over patchouli and cedarwood, and the unisex Gucci Intense Oud, which is darker, with olibanum, woods, leather and an oud accord."],
        ["Do you sell Gucci perfume minis?",
         "Yes. We stock 10ml minis of Bloom Eau de Toilette, Bloom Profumo di Fiori and Flora Gorgeous Orchid, plus 5ml sets: the Flora Gorgeous set (Gardenia, Orchid and Magnolia) and a four-bottle set with Bloom and Flora Gorgeous Gardenia."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_gucci_2026-11-16.jsonl")
