"""Journal guide "Chloé perfume: Nomade, Nuit d'Égypte, Jasmin Naturel, Rose Naturelle and the minis compared"
(user, 19-20 Nov 2026: 'Whats the topic of the next 5 Journals' -> 'Write and Publish All').

Semrush UK: chloe perfume 22,200, chloe nomade 2,900, chloe perfume for women 320, chloe nomade nuit d'egypte 320.
All 7 Chloé listings in stock with photos on 20 Nov (allp_map_1120.json). Facts = stored notes (custom.sw + description,
Admin read 20 Nov); the Chloé Eau de Parfum and Rose Tangerine are only in the mini sets (notes from the set texts).
8th 'Shop the story' product: Lalique Perles (rose + orris), named as a different perfume.
No longevity / 'dupe' / 'iconic' wording, no launch dates. Prices are written into the text: re-run if prices change.

Usage: python3 tools/shopify/guide_chloe.py <allp_map.json>
Output: docs/seo/guide_chloe_2026-11-20.jsonl
"""
import json
import sys

from journal_lib import build

A = {
    "title": "Chloé perfume: Nomade, Nuit d'Égypte, Jasmin Naturel, Rose Naturelle and the minis compared",
    "handle": "chloe-perfume-guide",
    "tag": "Scent Studio",
    "summary": "Every Chloé fragrance we stock, side by side: Nomade, Nomade Nuit d'Égypte, Nomade Jasmin Naturel Intense, Rose Naturelle Intense and the two miniature sets.",
    "mt": "Chloé Perfume: Nomade, Nuit d'Égypte & More | Swansura",
    "md": "Chloé Nomade, Nomade Nuit d’Égypte, Jasmin Naturel Intense, Rose Naturelle Intense and the Chloé mini sets compared: notes, sizes and gifts.",
    "pick": {
        "nomade": "chloe-nomade-eau-de-parfum-50ml-women-s-floral-chypre-fragrance",
        "nomadeset": "chloe-nomade-eau-de-parfum-gift-set-75ml-20ml-travel-spray-women-s-floral-chypre-fragrance-set",
        "nuit": "chloe-nomade-nuit-d-egypte-eau-de-parfum-50ml-women-s-warm-spicy-floral-fragrance",
        "jasmin": "chloe-nomade-jasmin-naturel-intense-eau-de-parfum-50ml-women-s-floral-woody-fragrance",
        "rose": "chloe-rose-naturelle-intense-eau-de-parfum-50ml-women-s-floral-woody-fragrance",
        "duo": "chloe-women-s-miniature-eau-de-parfum-gift-set-chloe-edp-20ml-nomade-edp-20ml",
        "mini4": "chloe-women-s-miniature-perfume-set-4x5ml-nomade-edt-rose-tangerine-edt-chloe-edp-nomade-edp",
        "perles": "lalique-perles-eau-de-parfum-100ml",
    },
    "titles": {},
    "shop": ["nomade", "nuit", "jasmin", "rose", "nomadeset", "duo", "mini4", "perles"],
    "body": """<p>Chloé fragrances are soft, natural-feeling florals: rose, freesia, jasmine and plum over woods and moss, rather than sugar or heavy spice. The Nomade line has grown into a small family of its own, and the Naturelle scents put a single flower at the centre. Here is every <strong>Chloé perfume</strong> we stock, with its notes, the sizes on offer and who each one suits.</p>
<h2>Chloé Nomade</h2>
<p>[[nomade|Chloé Nomade Eau de Parfum]] ({{nomade}}, 50ml) is a floral chypre: Mirabelle plum at the top, freesia in the heart and oakmoss in the base. The plum gives it a soft, fruity start, and the oakmoss keeps it dry and grown-up rather than sweet. It is an easy everyday scent for the office and weekends, in any season.</p>
<p>For a gift, the [[nomadeset|Chloé Nomade Eau de Parfum Gift Set]] ({{nomadeset}}) holds a 75ml bottle and a 20ml travel spray for the handbag.</p>
<h2>Nomade Nuit d'Égypte</h2>
<p>[[nuit|Chloé Nomade Nuit d'Égypte Eau de Parfum]] ({{nuit}}, 50ml) is the warm, spicy member of the family. Myrrh, ginger, cinnamon, broom flower nectar, cypriol and opopanax open it; orange blossom absolute fills the heart; and vanilla sits underneath. Resinous and glowing, it suits evenings, autumn and winter, and anyone who finds the original Nomade too light.</p>
<h2>Nomade Jasmin Naturel Intense</h2>
<p>[[jasmin|Chloé Nomade Jasmin Naturel Intense Eau de Parfum]] ({{jasmin}}, 50ml or 75ml) keeps Nomade's Mirabelle plum and adds date, with Egyptian jasmine at its heart and vanilla, sandalwood and patchouli in the base. Richer and creamier than Nomade, it is a jasmine scent for cooler days and evenings.</p>
<h2>Rose Naturelle Intense</h2>
<p>[[rose|Chloé Rose Naturelle Intense Eau de Parfum]] ({{rose}}, 50ml) is a rose scent with a woody edge: bergamot and neroli at the top, rose and oakwood in the heart, sandalwood and vanilla in the base. Fresh at first, then a warm, natural-smelling rose. A good choice for anyone who loves rose but wants it clean rather than powdery.</p>
<h2>The Chloé miniature sets</h2>
<p>The signature Chloé Eau de Parfum and Chloé Rose Tangerine are in our miniature sets, which are also the easiest way to try the range:</p>
<ul>
<li>[[duo|Chloé Women's Miniature Eau de Parfum Gift Set]] ({{duo}}): Chloé Eau de Parfum 20ml (peony, lychee, freesia, rose, magnolia, cedarwood and amber) and Nomade Eau de Parfum 20ml.</li>
<li>[[mini4|Chloé Women's Miniature Perfume Set]] ({{mini4}}): four 5ml bottles: Nomade Eau de Toilette (lychee, freesia, oakmoss), Rose Tangerine Eau de Toilette (tangerine, rose, blackcurrant, cedarwood), Chloé Eau de Parfum and Nomade Eau de Parfum.</li>
</ul>
<h2>Which Chloé perfume should you choose?</h2>
<ul>
<li><strong>A soft, mossy everyday floral:</strong> Nomade.</li>
<li><strong>Something warm and spicy for evenings:</strong> Nomade Nuit d'Égypte.</li>
<li><strong>A creamy jasmine:</strong> Nomade Jasmin Naturel Intense.</li>
<li><strong>A clean, natural rose:</strong> Rose Naturelle Intense.</li>
<li><strong>The signature Chloé rose and peony:</strong> the 20ml duo set.</li>
<li><strong>Not sure yet:</strong> the 4 x 5ml set lets you try four scents first.</li>
</ul>
<p>If you love rose with a soft, powdery edge, [[perles|Lalique Perles Eau de Parfum]] ({{perles}}, 100ml) pairs Bulgarian rose and orris with Bourbon pepper and patchouli over cashmere wood and tonka bean. It is a different perfume, warmer than the Chloé roses.</p>
<h2>Good to know</h2>
<ul>
<li><strong>Eau de parfum or eau de toilette?</strong> Our guide to <a href="/blogs/journal/extrait-vs-eau-de-parfum">extrait vs eau de parfum</a> explains the labels.</li>
<li><strong>Buying a gift?</strong> See our <a href="/blogs/journal/mini-perfume-sets-guide">mini perfume sets guide</a> and <a href="/blogs/journal/best-perfume-gift-sets-uk-2026">perfume gift sets guide</a>.</li>
<li><strong>Every bottle is 100% authentic</strong> and dispatched from the UK, with free UK delivery over £40.</li>
</ul>
<p>Shop every <a href="/collections/chloe">Chloé</a> fragrance, or browse <a href="/collections/perfume-for-women">perfume for women</a> and <a href="/collections/perfume-gift-sets-for-her">perfume gift sets for her</a>.</p>""",
    "faq": [
        ["What does Chloé Nomade smell like?",
         "Chloé Nomade Eau de Parfum is a floral chypre: Mirabelle plum at the top, freesia in the heart and oakmoss in the base. It starts soft and fruity and dries down mossy rather than sweet."],
        ["What is the difference between Nomade and Nomade Nuit d'Égypte?",
         "Nomade is a light, mossy floral with plum and freesia. Nomade Nuit d'Égypte is warm and spicy, with myrrh, ginger, cinnamon and opopanax, orange blossom absolute in the heart and vanilla in the base."],
        ["Which Chloé perfume is a rose scent?",
         "Rose Naturelle Intense, with bergamot and neroli, rose and oakwood, then sandalwood and vanilla. The signature Chloé Eau de Parfum also has rose, with peony, lychee, freesia and magnolia; we stock it in the 20ml duo and 4 x 5ml miniature sets."],
        ["Is there a Chloé gift set?",
         "Yes: the Nomade Eau de Parfum Gift Set (75ml plus a 20ml travel spray), the miniature Eau de Parfum duo (Chloé and Nomade, 20ml each) and a 4 x 5ml set with Nomade EDT, Rose Tangerine EDT, Chloé EDP and Nomade EDP."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_chloe_2026-11-20.jsonl")
