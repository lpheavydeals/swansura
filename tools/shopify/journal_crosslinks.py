"""Cross-links between the Dior Sauvage and CK Eternity Journal guides (user, 7 Nov 2026).

One sentence each, added just before the 'How to wear it' heading. Same method as journal_backlinks.py.
Input: {handle: Atom content} JSON of the blog feed. Output: docs/seo/journal_crosslinks_2026-11-07.json
({handle: {id, before, after}} = update + undo list).

Usage: python3 tools/shopify/journal_crosslinks.py <atom_bodies.json>
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
ANCHOR = "</ul>\n<h2>How to wear it</h2>"
EDITS = {
    "dior-sauvage-edt-vs-edp-vs-parfum": (
        "gid://shopify/Article/1005468418435",
        '<p>Like Eternity for Men? Compare it with the women\'s version in '
        '<a href="/blogs/journal/calvin-klein-eternity-for-women-vs-for-men">Calvin Klein Eternity for women vs for men</a>.</p>'),
    "calvin-klein-eternity-for-women-vs-for-men": (
        "gid://shopify/Article/1005468483971",
        '<p>Another men\'s classic that comes in more than one strength: '
        '<a href="/blogs/journal/dior-sauvage-edt-vs-edp-vs-parfum">Dior Sauvage EDT vs EDP vs Parfum</a>.</p>'),
}

atom = json.load(open(sys.argv[1]))
out = {}
for h, (gid, para) in EDITS.items():
    before = atom[h].strip()
    assert before.count(ANCHOR) == 1, h
    after = before.replace(ANCHOR, "</ul>\n" + para + "\n<h2>How to wear it</h2>")
    out[h] = {"id": gid, "before": before, "after": after}
    print(h, len(before), "->", len(after))
json.dump(out, open(ROOT / "docs/seo/journal_crosslinks_2026-11-07.json", "w"), ensure_ascii=False, indent=1)
