"""Back-links from 5 published Journal articles to the 4 guides published 7 Nov 2026 (user, 7 Nov 2026).

Input: the blog's Atom feed (content = the stored article body, wrapped in whitespace), saved as JSON
{handle: content} by the caller. Each insertion is anchored on text that must occur exactly once.
Output: docs/seo/journal_backlinks_2026-11-07.json ({handle: {id, before, after}}) = update + undo list.

Usage: python3 tools/shopify/journal_backlinks.py <atom_bodies.json>
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
J = "/blogs/journal/"
SAUVAGE = J + "dior-sauvage-edt-vs-edp-vs-parfum"
ETERNITY = J + "calvin-klein-eternity-for-women-vs-for-men"
ARABIAN = J + "lattafa-khamrah-qahwa-arabian-perfume"
LIP = J + "how-to-use-lip-scrub"

IDS = {
    "extrait-vs-eau-de-parfum": "gid://shopify/Article/1005307888003",
    "layer-oud-with-body-butter": "gid://shopify/Article/1005307855235",
    "how-to-use-body-scrub": "gid://shopify/Article/1005324763523",
    "how-to-use-body-butter": "gid://shopify/Article/1005324829059",
    "christmas-gift-guide": "gid://shopify/Article/1005324665219",
}

# (anchor, replacement): the anchor is kept and the new text added after (or around) it.
EDITS = {
    "extrait-vs-eau-de-parfum": [
        ("parfum miniature</a>, which is an easy way to compare.</p>",
         f'parfum miniature</a>, which is an easy way to compare. Two popular examples, side by side: '
         f'<a href="{SAUVAGE}">Dior Sauvage EDT vs EDP vs Parfum</a> and '
         f'<a href="{ETERNITY}">Calvin Klein Eternity for women vs for men</a>.</p>'),
    ],
    "layer-oud-with-body-butter": [
        ("<li>\n<strong>Match the mood.</strong> Sweet butters suit amber ouds, floral butters suit rose ouds, and neutral lotions suit smoky ouds.</li>\n</ul>",
         "<li>\n<strong>Match the mood.</strong> Sweet butters suit amber ouds, floral butters suit rose ouds, and neutral lotions suit smoky ouds.</li>\n</ul>\n"
         f'<p>New to oud and Arabian perfume? Our guide to <a href="{ARABIAN}">Lattafa Khamrah Qahwa and Arabian perfume</a> explains the notes and how to choose.</p>'),
    ],
    "how-to-use-body-scrub": [
        ('is all you need; see all <a href="/collections/lip-scrub">lip scrubs</a>.</p>',
         'is all you need; see all <a href="/collections/lip-scrub">lip scrubs</a> and our guide to '
         f'<a href="{LIP}">how to use a lip scrub</a>.</p>'),
    ],
    "how-to-use-body-butter": [
        ("comes in a 15ml size, or a large 50ml.</p>",
         "comes in a 15ml size, or a large 50ml. For the softest lips, use a scrub first: see "
         f'<a href="{LIP}">how to use a lip scrub</a>.</p>'),
    ],
    "christmas-gift-guide": [
        ('See every set in <a href="/collections/gifts-for-her">gifts for her</a>',
         f'Torn between the two Eternity scents? Read <a href="{ETERNITY}">Calvin Klein Eternity for women vs for men</a>. '
         'See every set in <a href="/collections/gifts-for-her">gifts for her</a>'),
        ('<p>More in <a href="/collections/gifts-for-him">gifts for him</a>.</p>',
         '<p>More in <a href="/collections/gifts-for-him">gifts for him</a>. Buying Dior Sauvage? '
         f'<a href="{SAUVAGE}">Sauvage EDT vs EDP vs Parfum</a> explains which to choose.</p>'),
        ('and <a href="/collections/gifts-under-25">gifts under £25</a>.</p>',
         'and <a href="/collections/gifts-under-25">gifts under £25</a>. Giving lip care? See '
         f'<a href="{LIP}">how to use a lip scrub</a>.</p>'),
    ],
}

atom = json.load(open(sys.argv[1]))
out = {}
for h, edits in EDITS.items():
    before = atom[h].strip()
    after = before
    for old, new in edits:
        assert after.count(old) == 1, (h, old)
        after = after.replace(old, new)
    out[h] = {"id": IDS[h], "before": before, "after": after}
    print(h, len(before), "->", len(after))
json.dump(out, open(ROOT / "docs/seo/journal_backlinks_2026-11-07.json", "w"), ensure_ascii=False, indent=1)
