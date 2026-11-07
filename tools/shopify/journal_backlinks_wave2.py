"""Back-links to the face wash + natural shampoo guides (published by the client 7 Nov 2026; user: 'add the back-links').

One short sentence per anchor, nothing else changed. Same method as journal_backlinks.py: input = the blog Atom feed
saved as {handle: content} (content = stored body plus surrounding whitespace); every anchor must occur once.
Output: docs/seo/journal_backlinks_wave2_2026-11-07.json ({handle: {id, before, after}} = update + undo list).

Usage: python3 tools/shopify/journal_backlinks_wave2.py <atom_bodies.json>
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
FACE = '<a href="/blogs/journal/face-wash-for-your-skin-type">'
SHAMPOO = '<a href="/blogs/journal/natural-shampoo-guide">'

EDITS = {
    "hair-oil-guide": ("gid://shopify/Article/1005324861827", [
        ("If flaking or itching does not settle, ask a pharmacist.</p>",
         f"If flaking or itching does not settle, ask a pharmacist. For more on choosing a shampoo, read our {SHAMPOO}natural shampoo guide</a>.</p>"),
    ]),
    "how-to-use-aloe-vera-gel": ("gid://shopify/Article/1005324730755", [
        ("Vilvah Honey Face Wash</a> (£12.99).</li>",
         f"Vilvah Honey Face Wash</a> (£12.99). Not sure which? See {FACE}face wash for your skin type</a>.</li>"),
    ]),
    "deyga-or-vilvah": ("gid://shopify/Article/1005307822467", [
        ("puts the shampoo with its partners in one box.</p>",
         f"puts the shampoo with its partners in one box. Our {SHAMPOO}natural shampoo guide</a> compares more options.</p>"),
        ("page compares the options side by side.</p>",
         f"page compares the options side by side, and our guide to {FACE}face wash for your skin type</a> explains how to choose.</p>"),
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
json.dump(out, open(ROOT / "docs/seo/journal_backlinks_wave2_2026-11-07.json", "w"), ensure_ascii=False, indent=1)
