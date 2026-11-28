"""Back-links to the 26 Nov 2026 guides (oud-perfume-under-60, aftershave-under-50)
(user, 26 Nov 2026: 'Publish both guides and add the back-links'). One sentence each, nothing else changed.

Usage: python3 tools/shopify/journal_backlinks_wave17.py <admin_articles.json> <admin_collections.json>
  admin_articles.json = {"data":{"articles":{"nodes":[{id,handle,body}]}}}
  admin_collections.json = {"data":{"collections":{"nodes":[{id,handle,copy:{value}}]}}}
Output: docs/seo/journal_backlinks_wave17_2026-11-26.json (before/after = undo)
"""
import json, sys, pathlib
OUD = '<a href="/blogs/journal/oud-perfume-under-60">oud perfume under £60 guide</a>'
AFT = '<a href="/blogs/journal/aftershave-under-50">aftershave under £50 guide</a>'
ART = {
    "oud-perfume-guide": [("Made for men, and the most affordable oud in this guide.</li>",
        f"Made for men, and the most affordable oud in this guide. Our {OUD} has more oud scents on a smaller budget.</li>")],
    "al-haramain-amber-oud-editions": [('read our <a href="/blogs/journal/oud-perfume-guide">oud perfume guide</a>.',
        f'read our <a href="/blogs/journal/oud-perfume-guide">oud perfume guide</a>, or our {OUD} for real oud notes on a budget.')],
    "best-perfume-gift-sets-uk-2026": [('<a href="/blogs/journal/carolina-herrera-perfume-guide">Carolina Herrera perfume guide</a>.</p>',
        f'<a href="/blogs/journal/carolina-herrera-perfume-guide">Carolina Herrera perfume guide</a>. For a single bottle rather than a set, our {AFT} groups men’s fragrances by scent type.</p>')],
    "christmas-gift-guide": [('<a href="/blogs/journal/paco-rabanne-perfume-guide">Paco Rabanne perfume guide</a>.</p>',
        f'<a href="/blogs/journal/paco-rabanne-perfume-guide">Paco Rabanne perfume guide</a>. On a tighter budget, see our {AFT}.</p>')],
}
COL = {
    "oud-perfume": f" For oud scents on a budget, read our {OUD}.",
    "perfume-for-men": f" For picks by scent type, read our {AFT}.",
    "aftershave-gift-sets-for-him": f" Prefer a single bottle? Read our {AFT}.",
}
def addfirst(copy, s):
    i = copy.find("</p>")
    assert i > 0
    return copy[:i] + s + copy[i:]
arts = {n["handle"]: n for n in json.load(open(sys.argv[1]))["data"]["articles"]["nodes"]}
cols = {n["handle"]: n for n in json.load(open(sys.argv[2]))["data"]["collections"]["nodes"]}
out = {"articles": [], "collections": []}
for h, reps in ART.items():
    b = arts[h]["body"]; a = b
    for old, new in reps:
        assert a.count(old) == 1, (h, old); a = a.replace(old, new)
    out["articles"].append({"id": arts[h]["id"], "handle": h, "before": b, "after": a})
for h, s in COL.items():
    c = cols[h]["copy"]["value"]
    assert "oud-perfume-under-60" not in c and "aftershave-under-50" not in c
    out["collections"].append({"id": cols[h]["id"], "handle": h, "before": c, "after": addfirst(c, s)})
p = pathlib.Path(__file__).resolve().parents[2] / "docs/seo/journal_backlinks_wave17_2026-11-26.json"
json.dump(out, open(p, "w"), ensure_ascii=False, indent=1)
print("articles", len(out["articles"]), "collections", len(out["collections"]))
