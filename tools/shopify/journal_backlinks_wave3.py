"""Back-links to the moisturiser + face mask guides (published by the client 7 Nov 2026; user: 'add the back-links').

One short sentence per anchor, nothing else changed. Same method as journal_backlinks.py: input = the blog Atom feed
saved as {handle: content} (content = stored body plus surrounding whitespace); every anchor must occur once.
Output: docs/seo/journal_backlinks_wave3_2026-11-07.json ({handle: {id, before, after}} = update + undo list).

Usage: python3 tools/shopify/journal_backlinks_wave3.py <atom_bodies.json>
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
MOIST = '<a href="/blogs/journal/moisturiser-for-your-skin-type">'
MASK = '<a href="/blogs/journal/face-mask-guide">'

EDITS = {
    "face-wash-for-your-skin-type": ("gid://shopify/Article/1005503250819", [
        ('see our <a href="/collections/moisturiser-for-dry-skin">moisturisers for dry skin</a>.',
         'see our <a href="/collections/moisturiser-for-dry-skin">moisturisers for dry skin</a>, '
         f'or read {MOIST}moisturiser for your skin type</a>. Once or twice a week, add a mask: see our {MASK}face mask guide</a>.'),
    ]),
    "how-to-use-aloe-vera-gel": ("gid://shopify/Article/1005324730755", [
        ("Apply a thicker layer for 10 minutes, then rinse or press the rest into the skin.</li>",
         f"Apply a thicker layer for 10 minutes, then rinse or press the rest into the skin. For clay, charcoal and powder masks, see our {MASK}face mask guide</a>.</li>"),
    ]),
}

atom = json.load(open(sys.argv[1]))
out = {}
for h, (gid, edits) in EDITS.items():
    before = atom[h].strip()
    after = before
    for old, new in edits:
        assert after.count(old) == 1, (h, old)
        after = after.replace(old, new)
    out[h] = {"id": gid, "before": before, "after": after}
    print(h, len(before), "->", len(after))
json.dump(out, open(ROOT / "docs/seo/journal_backlinks_wave3_2026-11-07.json", "w"), ensure_ascii=False, indent=1)
