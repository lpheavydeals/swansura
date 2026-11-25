"""Journal guide 'Jo Milano Game of Spades: every scent compared, from Full House to Wildcard'
(user, 25 Nov 2026: 'Write and Publish All').

Semrush UK: game of spades full house 1,600, wildcard 880. GSC 4-10 Nov: 'game of spades full house' 72 impr at
pos 9 + ~25 more Full House / High Roller / Bid / Boston / Jackpot queries at pos 2-13, 0 clicks (strongest GSC
signal of the topics checked). One listing per scent (duplicate Rouge / Wildcard / Full House listings not linked).
Facts = stored notes + descriptions (Admin read 25 Nov): full note lists only for Wildcard, Opal, High Roller;
Queen top notes only; King / Bid / Boston / Jackpot accord level; Royale / Ruby / Yellow Sapphire / Emerald
'fresh + woody/warm' only; Full House, Rouge and Diamond have NO stored notes (said plainly, ask us).
High Roller's listing text says 'long-lasting' / 'powerhouse': not repeated. NO PRICES.

Usage: python3 tools/shopify/guide_game_of_spades.py <allp_map.json>
Output: docs/seo/guide_game_of_spades_2026-11-25.jsonl
"""
import json
import sys

from journal_lib import build

S = "game-of-spades-"
A = {
    "title": "Jo Milano Game of Spades: every scent compared, from Full House to Wildcard",
    "handle": "game-of-spades-perfume-guide",
    "tag": "Scent Studio",
    "summary": "Every Jo Milano Game of Spades eau de parfum we stock, from Full House, Wildcard and High Roller to Opal, King, Jackpot, Boston and Bid, with the notes we have and who each suits.",
    "mt": "Game of Spades: Full House, Wildcard & More | Swansura",
    "md": "Jo Milano Game of Spades compared: Full House, Wildcard, High Roller, Opal, King, Jackpot, Boston, Bid and the rest of the range.",
    "pick": {
        "fh": S + "full-house-eau-de-parfum-100ml-long-lasting-luxury-unisex-perfume-for-men-women",
        "wild": S + "wildcard-eau-de-parfum-100ml-long-lasting-luxury-unisex-perfume-woody-amber-vanilla-fragrance-for-men-women",
        "high": S + "high-roller-eau-de-parfum-100ml-luxury-unisex-fragrance-citrus-spice-patchouli-powerhouse",
        "opal": S + "opal-eau-de-parfum-100ml",
        "king": S + "king-eau-de-parfum-100ml",
        "jack": S + "jackpot-eau-de-parfum-100ml",
        "boston": S + "boston-eau-de-parfum-100ml-men",
        "bid": S + "bid-eau-de-parfum-100ml-men",
        "queen": "jo-milano-game-of-spades-queen-for-unisex-perfume-spray-100-ml",
        "rouge": S + "rouge-eau-de-parfum-100ml-long-lasting-luxury-unisex-perfume-for-men-women",
        "rougex": S + "rouge-extrait-de-parfum-100ml",
        "royale": S + "royale-eau-de-parfum-100ml-long-lasting-luxury-perfume-for-men-women",
        "ruby": S + "ruby-eau-de-parfum-100ml-luxury-long-lasting-perfume-for-men-women-designer-unisex-fragrance",
        "yellow": S + "yellow-sapphire-eau-de-parfum-100ml-fresh-luxury-unisex-perfume-designer-fragrance",
        "emerald": S + "emerald-edp-100ml-long-lasting-luxury-unisex-perfume-for-men-women",
        "diamond": S + "diamond-eau-de-parfum-100ml",
    },
    "titles": {},
    "shop": ["fh", "wild", "high", "opal", "king", "jack", "boston", "bid"],
    "body": """<p><strong>Game of Spades</strong> is a range of eau de parfums from Jo Milano Paris, each in a 100ml bottle marked with a spade. Most are made for men and women alike. Here is every Game of Spades scent we stock, what we know about each one, and how to choose.</p>
<h2>Game of Spades Full House</h2>
<p>[[fh|Game of Spades Full House]] (100ml) is a unisex eau de parfum that we list in our amber family: warm and sweet rather than fresh. We do not have a full note list for Full House yet, so if you want the detail before you buy, message us on WhatsApp or Instagram and we will help.</p>
<h2>Game of Spades Wildcard</h2>
<p>[[wild|Game of Spades Wildcard]] (100ml) has the fullest note list in the range. Bergamot, florals and coriander open it; apple, ambroxan and vanilla form the heart; and tonka bean, ambergris and woody notes make the base. Fresh at first, then soft and sweet, it suits evenings and cooler weather.</p>
<h2>Game of Spades High Roller</h2>
<p>[[high|Game of Spades High Roller]] (100ml) is the spiciest: grapefruit, bergamot and blackcurrant, then ginger, cinnamon, cardamom and citron, over pink pepper and patchouli.</p>
<h2>Game of Spades Opal, King and Jackpot</h2>
<ul>
<li>[[opal|Opal]] (white bottle, crystal-set gold spade): bergamot, lemon, pear and raspberry, then rose, jasmine and peony, over amber, sandalwood, cedar and musk. The most floral of the range.</li>
<li>[[king|King]] (golden bottle, black spade): citrus top notes, a fruity heart and an amber-vanilla base.</li>
<li>[[jack|Jackpot]] (polished gold bottle, black spade): a citrus top, a floral-spicy heart and a woody-amber base.</li>
</ul>
<h2>For men: Boston and Bid</h2>
<ul>
<li>[[boston|Boston]] (matte black bottle, teal spade): a fresh citrus top, a spicy heart and a woody-amber base.</li>
<li>[[bid|Bid]] (green bottle, gold spade): a fresh citrus opening, a spicy-woody heart and a warm amber base.</li>
</ul>
<h2>The rest of the range</h2>
<ul>
<li>[[queen|Queen]]: mandarin and freesia, then soft woods and musk. Easy for every day.</li>
<li>[[royale|Royale]], [[ruby|Ruby]], [[yellow|Yellow Sapphire]] and [[emerald|Emerald]]: each balances a fresh opening with a warmer, woodier side.</li>
<li>[[rouge|Rouge]], also as an [[rougex|extrait de parfum]], and [[diamond|Diamond]]: we do not have their note lists yet; ask us before you buy.</li>
</ul>
<h2>Which Game of Spades should you choose?</h2>
<ul>
<li><strong>Warm and sweet:</strong> Full House, King or Wildcard.</li>
<li><strong>Spicy:</strong> High Roller.</li>
<li><strong>Floral and fruity:</strong> Opal.</li>
<li><strong>Fresh, then woody, for men:</strong> Boston or Bid.</li>
<li><strong>Light for every day:</strong> Queen.</li>
</ul>
<h2>Good to know</h2>
<ul>
<li><strong>Eau de parfum or extrait?</strong> Our guide to <a href="/blogs/journal/extrait-vs-eau-de-parfum">extrait vs eau de parfum</a> explains the labels.</li>
<li><strong>Buying a gift?</strong> See our <a href="/blogs/journal/best-perfume-gift-sets-uk-2026">perfume gift sets guide</a>, or <a href="/collections/unisex-perfume">unisex perfume</a> for scents to share.</li>
<li><strong>Every bottle is 100% authentic</strong> and dispatched from the UK, with free UK delivery over £40.</li>
</ul>
<p>Shop every <a href="/collections/jo-milano">Jo Milano</a> fragrance, or browse <a href="/collections/niche-perfume">niche perfume</a>.</p>""",
    "faq": [
        ["What does Game of Spades Full House smell like?",
         "We list Full House in our amber family: warm and sweet rather than fresh. We do not have a full note list for it yet, so message us on WhatsApp or Instagram if you want more detail before you buy."],
        ["What are the notes in Game of Spades Wildcard?",
         "Wildcard opens with bergamot, florals and coriander, has apple, ambroxan and vanilla in the heart, and settles on tonka bean, ambergris and woody notes."],
        ["Is Game of Spades unisex?",
         "Most of the range is made for men and women alike. Boston and Bid are made for men."],
        ["Who makes Game of Spades?",
         "Game of Spades is a range of eau de parfums from Jo Milano Paris. Every bottle we sell is 100% authentic and dispatched from the UK."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_game_of_spades_2026-11-25.jsonl")
