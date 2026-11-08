"""Back-links to the oud perfume + under eye cream guides (published by the client 8 Nov 2026; user: 'add the back-links').

One short sentence per anchor, nothing else changed. Same method as journal_backlinks.py: input = the blog Atom feed
saved as {handle: content} (CDATA content; parse without unescaping, see journal_backlinks_wave4 note); every anchor must occur once.
Output: docs/seo/journal_backlinks_wave4_2026-11-08.json ({handle: {id, before, after}} = update + undo list).

Usage: python3 tools/shopify/journal_backlinks_wave4.py <atom_bodies.json>
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUD = '<a href="/blogs/journal/oud-perfume-guide">'
EYE = '<a href="/blogs/journal/under-eye-cream-guide">'

EDITS = {
    "layer-oud-with-body-butter": ("gid://shopify/Article/1005307855235", [
        ("explains the notes and how to choose.</p>",
         f"explains the notes and how to choose. For Tom Ford Oud Wood, Gucci Intense Oud and other designer ouds, see our {OUD}oud perfume guide</a>.</p>"),
    ]),
    "lattafa-khamrah-qahwa-arabian-perfume": ("gid://shopify/Article/1005468254595", [
        ('<p>Browse all <a href="/collections/arabian-perfume">Arabian perfume</a> and <a href="/collections/oud-perfume">oud perfume</a>.</p>',
         '<p>Browse all <a href="/collections/arabian-perfume">Arabian perfume</a> and <a href="/collections/oud-perfume">oud perfume</a>. '
         f'For designer ouds such as Tom Ford Oud Wood and Gucci Intense Oud, read our {OUD}oud perfume guide</a>.</p>'),
    ]),
    "moisturiser-for-your-skin-type": ("gid://shopify/Article/1005503971715", [
        ("with upward strokes, avoiding the eyes.</li>",
         f"with upward strokes, avoiding the eyes. For the eye area, see our {EYE}under eye cream guide</a>.</li>"),
    ]),
    "face-mask-guide": ("gid://shopify/Article/1005504332163", [
        ("carrot seed oils with beeswax, to dab on at night.</p>",
         f"carrot seed oils with beeswax, to dab on at night. For eye creams and gels, read our {EYE}under eye cream guide</a>.</p>"),
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
json.dump(out, open(ROOT / "docs/seo/journal_backlinks_wave4_2026-11-08.json", "w"), ensure_ascii=False, indent=1)
