"""Journal guide 'Women's perfume under £50: designer scents by mood'
(user, 28 Nov 2026: 'Go ahead with the two guides', the next budget guides after oud under £60 / aftershave under £50).

Why: 'perfume for women under £50' / 'gift for her' are budget questions Google and AI assistants answer with
short lists. Every scent below was in stock at £50 or less (smallest size) on the storefront on 28 Nov 2026,
and sits in perfume-for-women. Facts = each description's 'Fragrance notes' list. NO PRICES in the text (band only).

Usage: python3 tools/shopify/guide_womens_perfume_under_50.py <storefront products dump dir>
Output: docs/seo/guide_womens_perfume_under_50_2026-11-28.jsonl
"""
import glob
import json
import sys

from journal_lib import build

A = {
    "title": "Women's perfume under £50: designer scents by mood",
    "handle": "womens-perfume-under-50",
    "tag": "Gift guide",
    "summary": "Designer and Arabian women's perfumes under £50, grouped by mood: fresh and clean, classic florals, fruity and sweet, and warm for evenings. With the notes in each, for yourself or as a gift.",
    "mt": "Women's Perfume Under £50: Scents by Mood | Swansura",
    "md": "Women’s perfume under £50 in the UK: Calvin Klein, Lalique, DKNY, Marc Jacobs, Issey Miyake, Elie Saab and Paco Rabanne, grouped by mood with notes.",
    "pick": {
        "cool": "davidoff-cool-water-reborn-intense-eau-de-parfum-50ml-women-s-fresh-floral-fragrance",
        "vera": "vera-wang-embrace-green-tea-and-pear-blossom-eau-de-toilette-30ml",
        "drop": "issey-miyake-a-drop-dissey-eau-de-parfum-fraiche-90ml",
        "paradiso": "roberto-cavalli-paradiso-eau-de-parfum-100ml",
        "eternity": "calvin-klein-eternity-eau-de-parfum-women-s-classic-floral-fragrance",
        "airdutemps": "nina-ricci-lair-du-temps-eau-de-toilette-women-s-floral-fragrance",
        "amour": "lalique-lamour-eau-de-parfum-100ml",
        "elie": "elie-saab-le-parfum-eau-de-parfum-50ml-women-s-floral-amber-fragrance",
        "iris": "chopard-imperiale-iris-malika-eau-de-parfum-100ml-luxury-women-s-floral-fragrance",
        "orchard": "dkny-be-delicious-orchard-street-eau-de-parfum-100ml-women-s-fruity-floral-fragrance",
        "honey": "marc-jacobs-honey-eau-de-parfum-100ml-women-s-floral-fruity-fragrance",
        "petale": "issey-miyake-leau-dissey-pure-petale-de-nectar-eau-de-toilette-90ml",
        "ariana": "ariana-grande-thank-u-next-eau-de-parfum-100ml-women-s-fruity-floral-gourmand-fragrance",
        "yara": "lattafa-yara-candy-eau-de-parfum-100ml",
        "nyla": "arabiyat-prestige-nyla-eau-de-parfum-80ml",
        "musc": "narciso-rodriguez-musc-noir-for-her-eau-de-parfum",
        "uv": "paco-rabanne-ultraviolet-eau-de-parfum-80ml",
        "noor": "elie-saab-nuit-noor-eau-de-parfum-90ml-women-s-amber-floral-fragrance",
        "satine": "lalique-satine-eau-de-parfum-100ml",
        "clinique": "clinique-aromatics-elixir-eau-de-parfum-100ml",
    },
    "titles": {},
    "shop": ["eternity", "honey", "amour", "orchard", "drop", "noor", "uv", "elie"],
    "body": """<p><strong>A designer perfume for her does not need a big budget.</strong> Every women's fragrance below was under £50 at Swansura at the time of writing (for scents sold in more than one size, at least the smallest size is). We have grouped them by mood, with the notes in each, so you can choose one for yourself or as a gift.</p>
<h2>Fresh and clean</h2>
<p>Citrus, green notes and soft flowers. Easy for every day, the office and warmer weather.</p>
<ul>
<li>[[cool|Davidoff Cool Water Reborn Intense Eau de Parfum]] (50ml): bergamot and green notes, then rose, over vetiver, woods and musk.</li>
<li>[[vera|Vera Wang Embrace Green Tea and Pear Blossom]] (30ml eau de toilette): pear blossom, green tea and bergamot, then freesia, orange blossom and peony, over sandalwood, cedar and musk.</li>
<li>[[drop|Issey Miyake A Drop d'Issey Eau de Parfum Fraîche]] (90ml): a rain accord, then lilac and Damask rose, over sandalwood and musk. Our <a href="/blogs/journal/issey-miyake-leau-dissey-guide">L'Eau d'Issey guide</a> compares the Issey Miyake line.</li>
<li>[[paradiso|Roberto Cavalli Paradiso Eau de Parfum]] (100ml): citrus, mandarin and bergamot, then jasmine, over cypress, pine and laurel.</li>
</ul>
<h2>Classic florals</h2>
<p>Rose, jasmine and white flowers. Polished enough for occasions, gentle enough for daytime.</p>
<ul>
<li>[[eternity|Calvin Klein Eternity Eau de Parfum]] (30ml or 100ml): freesia, mandarin and sage, then lily, carnation, rose and jasmine, over sandalwood, amber and musk. Our <a href="/blogs/journal/calvin-klein-eternity-for-women-vs-for-men">Eternity guide</a> compares it with the men's version.</li>
<li>[[airdutemps|Nina Ricci L'Air du Temps Eau de Toilette]] (30ml or 100ml): carnation, rose, neroli and peach, then jasmine, ylang-ylang, violet and iris, over sandalwood, musk, cedarwood and amber.</li>
<li>[[amour|Lalique L'Amour Eau de Parfum]] (100ml): bergamot, neroli and rosebuds, then gardenia, tuberose and jasmine, over musk, cedarwood and sandalwood.</li>
<li>[[elie|Elie Saab Le Parfum Eau de Parfum]] (50ml): orange blossom, then two kinds of jasmine, over cedarwood, patchouli, honey and rose.</li>
<li>[[iris|Chopard Imperiale Iris Malika]] (100ml eau de parfum): spices and red berries, then iris and jasmine, over vanilla, benzoin and woods. Powdery rather than sweet.</li>
</ul>
<h2>Fruity and sweet</h2>
<p>Juicy fruit over vanilla, honey or musk. Cheerful, and a safe pick for someone who likes sweet scents.</p>
<ul>
<li>[[orchard|DKNY Be Delicious Orchard Street]] (100ml eau de parfum): apple, pink grapefruit and blackcurrant, then jasmine, rose and peony, over musk, cedarwood and amber.</li>
<li>[[honey|Marc Jacobs Honey Eau de Parfum]] (100ml): pear and mandarin, then honeysuckle, orange blossom and peach, over honey, vanilla and woods.</li>
<li>[[petale|Issey Miyake L'Eau d'Issey Pure Pétale de Nectar]] (90ml eau de toilette): pear and honey, then rose and peony, over cashmeran, white musk and sandalwood.</li>
<li>[[ariana|Ariana Grande Thank U, Next]] (100ml eau de parfum): white pear and wild raspberry, then coconut and pink rose, over a macaron note and musk.</li>
<li>[[yara|Lattafa Yara Candy]] (100ml eau de parfum): green mandarin and blackcurrant, then a strawberry candy accord and gardenia, over vanilla, musk, sandalwood and amber.</li>
<li>[[nyla|Arabiyat Prestige Nyla]] (80ml eau de parfum): coconut, peach, mandarin and bergamot, then tiare, jasmine and rose, over white musk and patchouli.</li>
</ul>
<h2>Warm and for evenings</h2>
<p>Spice, amber, musk and moss. Best for colder months, dinners and nights out.</p>
<ul>
<li>[[musc|Narciso Rodriguez Musc Noir For Her]] (the 10ml spray is under £50): plum, then musk and heliotrope, over suede. Our <a href="/blogs/journal/narciso-rodriguez-perfume-guide">Narciso Rodriguez guide</a> has the rest of the line.</li>
<li>[[uv|Paco Rabanne Ultraviolet Eau de Parfum]] (80ml): pepper, apricot, almond and coriander, then violet, osmanthus, rose and jasmine, over amber, vanilla, patchouli and cedar.</li>
<li>[[noor|Elie Saab Nuit Noor Eau de Parfum]] (90ml): black pepper and spices, then rose, jasmine and incense, over patchouli, amber, musk and woods.</li>
<li>[[satine|Lalique Satine Eau de Parfum]] (100ml): jasmine, gardenia and heliotrope, then vanilla, tonka and pink pepper, over patchouli, sandalwood and vetiver.</li>
<li>[[clinique|Clinique Aromatics Elixir Eau de Parfum]] (100ml): rose and orange blossom, then jasmine and ylang-ylang, over patchouli and oakmoss. Rich and mossy rather than sweet.</li>
</ul>
<h2>Which one should you choose?</h2>
<ul>
<li><strong>For every day and the office:</strong> Calvin Klein Eternity or Davidoff Cool Water Reborn Intense.</li>
<li><strong>A gift when you are not sure:</strong> Marc Jacobs Honey or DKNY Be Delicious Orchard Street.</li>
<li><strong>For weddings and occasions:</strong> Lalique L'Amour or Elie Saab Le Parfum.</li>
<li><strong>Evenings and winter:</strong> Elie Saab Nuit Noor or Paco Rabanne Ultraviolet.</li>
</ul>
<h2>Buying it as a gift</h2>
<p>If you do not know her taste, a fresh or fruity scent is the safest choice; a warm one suits someone who already wears a rich perfume. For a boxed present, see our <a href="/blogs/journal/perfume-gift-sets-under-30">perfume gift sets under £30</a> guide, <a href="/collections/perfume-gift-sets-for-her">perfume gift sets for her</a> and <a href="/collections/gifts-under-50">gifts under £50</a>, or browse every <a href="/collections/perfume-for-women">women's perfume</a>. All are 100% authentic and ship from the UK, with free UK delivery over £40.</p>""",
    "faq": [
        ["What is a good women's perfume under £50?",
         "For a fresh everyday scent, Calvin Klein Eternity or Davidoff Cool Water Reborn Intense. For a classic floral, Lalique L'Amour or Elie Saab Le Parfum. For something fruity and sweet, Marc Jacobs Honey or DKNY Be Delicious Orchard Street. For evenings, Elie Saab Nuit Noor or Paco Rabanne Ultraviolet."],
        ["What perfume should I buy her if I do not know her taste?",
         "A fresh or fruity floral is the safest choice, such as Marc Jacobs Honey, DKNY Be Delicious Orchard Street or Calvin Klein Eternity. A gift set with several small sprays also lets her try more than one scent."],
        ["What is the difference between eau de toilette and eau de parfum?",
         "An eau de parfum usually carries a higher concentration of fragrance oils than an eau de toilette, so it feels richer. Our guide to extrait vs eau de parfum explains the labels."],
        ["Are these women's perfumes authentic?",
         "Yes. Every perfume at Swansura is 100% authentic and ships from the UK, with free UK delivery over £40."],
    ],
}

if __name__ == "__main__":
    ALL = {}
    for f in glob.glob(sys.argv[1] + "/*.json"):
        d = json.load(open(f))
        if isinstance(d, dict) and "products" in d:
            for p in d["products"]:
                ALL[p["handle"]] = p
    build(A, ALL, "guide_womens_perfume_under_50_2026-11-28.jsonl")
