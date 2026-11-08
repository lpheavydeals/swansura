"""Back-links to the Tom Ford + face serum guides (published by the client 8 Nov 2026, second pair; user: 'add the back-links').

One short sentence per anchor, nothing else changed. Same method as journal_backlinks.py: input = the blog Atom feed
saved as {handle: content} (CDATA content; parse without unescaping, see journal_backlinks_wave4 note); every anchor must occur once.
Output: docs/seo/journal_backlinks_wave5_2026-11-08.json ({handle: {id, before, after}} = update + undo list).

Usage: python3 tools/shopify/journal_backlinks_wave5.py <atom_bodies.json>
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
TF = '<a href="/blogs/journal/tom-ford-perfume-guide">'
FS = '<a href="/blogs/journal/face-serum-guide">'

EDITS = {
    "oud-perfume-guide": ("gid://shopify/Article/1005508723075", [
        ('See every <a href="/collections/tom-ford">Tom Ford</a> fragrance.</p>',
         f'See every <a href="/collections/tom-ford">Tom Ford</a> fragrance, or read our {TF}Tom Ford perfume guide</a> for Black Orchid, Noir Extreme and Neroli Portofino.</p>'),
    ]),
    "christmas-gift-guide": ("gid://shopify/Article/1005324665219", [
        ("explains which to choose.</p>",
         f"explains which to choose, and our {TF}Tom Ford perfume guide</a> compares Black Orchid, Noir Extreme and more.</p>"),
    ]),
    "moisturiser-for-your-skin-type": ("gid://shopify/Article/1005503971715", [
        ('Browse every <a href="/collections/serum">serum</a>.</p>',
         f'Browse every <a href="/collections/serum">serum</a>, or read our {FS}face serum guide</a>.</p>'),
    ]),
    "under-eye-cream-guide": ("gid://shopify/Article/1005508854147", [
        ('For moisturiser, see <a href="/blogs/journal/moisturiser-for-your-skin-type">moisturiser for your skin type</a>.</p>',
         'For moisturiser, see <a href="/blogs/journal/moisturiser-for-your-skin-type">moisturiser for your skin type</a>. '
         f'For more on serums, read our {FS}face serum guide</a>.</p>'),
    ]),
}

atom = json.load(open(sys.argv[1]))
out = {}
for h, (gid, edits) in EDITS.items():
    # the Atom feed now serves bodies as CDATA (parse without html.unescape); guard against any bare '&'
    before = re.sub(r"&(?!amp;|lt;|gt;|quot;|#\d+;|#x[0-9a-fA-F]+;|[a-z]+;)", "&amp;", atom[h].strip())
    after = before
    for old, new in edits:
        assert after.count(old) == 1, (h, old)
        after = after.replace(old, new)
    out[h] = {"id": gid, "before": before, "after": after}
    print(h, len(before), "->", len(after))
json.dump(out, open(ROOT / "docs/seo/journal_backlinks_wave5_2026-11-08.json", "w"), ensure_ascii=False, indent=1)
