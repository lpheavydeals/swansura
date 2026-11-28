"""Back-links to the 28 Nov 2026 guides (perfume-gift-sets-under-30, womens-perfume-under-50)
(user, 28 Nov 2026: 'Publish both guides and add the back-links'). One sentence each, nothing else changed.

Usage: python3 tools/shopify/journal_backlinks_wave18.py <admin.json>
  admin.json = {"data":{"articles":{"nodes":[{id,handle,body}]},"collections":{"nodes":[{id,handle,copy:{value}}]}}}
Output: docs/seo/journal_backlinks_wave18_2026-11-28.json (before/after = undo)
"""
import json, sys, pathlib
GS = '<a href="/blogs/journal/perfume-gift-sets-under-30">perfume gift sets under £30 guide</a>'
WP = '<a href="/blogs/journal/womens-perfume-under-50">women’s perfume under £50 guide</a>'
ART = {
    "best-perfume-gift-sets-uk-2026": [
        ('<h2>Perfume gift sets under £30</h2>\n',
         f'<h2>Perfume gift sets under £30</h2>\n<p>Our {GS} lists what is in each box and the notes in each scent.</p>\n'),
        ('our <a href="/blogs/journal/marc-jacobs-perfume-guide">Marc Jacobs perfume guide</a>.</p>',
         f'our <a href="/blogs/journal/marc-jacobs-perfume-guide">Marc Jacobs perfume guide</a>. For a single bottle rather than a set, see our {WP}.</p>')],
    "christmas-gift-guide": [
        ('Our <a href="/blogs/journal/mugler-perfume-guide">Mugler perfume guide</a> compares Alien and Angel.</p>',
         f'Our <a href="/blogs/journal/mugler-perfume-guide">Mugler perfume guide</a> compares Alien and Angel. On a tighter budget, see our {WP}.</p>'),
        ('Our <a href="/blogs/journal/skincare-gift-sets-guide">skincare gift sets guide</a> lists what is in every Vilvah and Deyga kit.</p>',
         f'Our <a href="/blogs/journal/skincare-gift-sets-guide">skincare gift sets guide</a> lists what is in every Vilvah and Deyga kit, and our {GS} covers boxed perfume sets on a budget.</p>')],
    "mini-perfume-sets-guide": [
        ('<strong>Want a full bottle with extras instead?</strong> See our <a href="/blogs/journal/best-perfume-gift-sets-uk-2026">best perfume gift sets</a> guide.</li>',
         f'<strong>Want a full bottle with extras instead?</strong> See our <a href="/blogs/journal/best-perfume-gift-sets-uk-2026">best perfume gift sets</a> guide, or our {GS}.</li>')],
    "stocking-fillers-for-her-under-25": [
        ('For bigger gifts, read our <a href="/blogs/journal/best-perfume-gift-sets-uk-2026">perfume gift sets guide</a>',
         f'For a full bottle, see our {WP}. For bigger gifts, read our <a href="/blogs/journal/best-perfume-gift-sets-uk-2026">perfume gift sets guide</a>')],
}
COL = {
    "perfume-gift-sets": f" On a budget? Read our {GS}.",
    "perfume-gift-sets-for-her": f" For sets under £30, read our {GS}.",
    "perfume-for-women": f" For picks by mood on a budget, read our {WP}.",
}
def addfirst(copy, s):
    i = copy.find("</p>"); assert i > 0
    return copy[:i] + s + copy[i:]
d = json.load(open(sys.argv[1]))["data"]
arts = {n["handle"]: n for n in d["articles"]["nodes"]}
cols = {n["handle"]: n for n in d["collections"]["nodes"]}
out = {"articles": [], "collections": []}
for h, reps in ART.items():
    b = arts[h]["body"]; a = b
    for old, new in reps:
        assert a.count(old) == 1, (h, old); a = a.replace(old, new)
    out["articles"].append({"id": arts[h]["id"], "handle": h, "before": b, "after": a})
for h, s in COL.items():
    c = cols[h]["copy"]["value"]
    assert "perfume-gift-sets-under-30" not in c and "womens-perfume-under-50" not in c
    out["collections"].append({"id": cols[h]["id"], "handle": h, "before": c, "after": addfirst(c, s)})
p = pathlib.Path(__file__).resolve().parents[2] / "docs/seo/journal_backlinks_wave18_2026-11-28.json"
json.dump(out, open(p, "w"), ensure_ascii=False, indent=1)
print("articles", len(out["articles"]), "collections", len(out["collections"]))
