"""Back-links to the 28 Nov 2026 guides skincare-gifts-under-25 + unisex-perfume-under-50
(user, 28 Nov 2026: 'Publish both guides and add the back-links'). One sentence each, nothing else changed.

Usage: python3 tools/shopify/journal_backlinks_wave19.py <admin.json>
  admin.json = {"data":{"articles":{"nodes":[{id,handle,body}]},"collections":{"nodes":[{id,handle,copy:{value}}]}}}
Output: docs/seo/journal_backlinks_wave19_2026-11-28.json (before/after = undo)
"""
import json, sys, pathlib
SK = '<a href="/blogs/journal/skincare-gifts-under-25">skincare gifts under £25 guide</a>'
UP = '<a href="/blogs/journal/unisex-perfume-under-50">unisex perfume under £50 guide</a>'
ART = {
    "skincare-gift-sets-guide": [
        ('<a href="/blogs/journal/stocking-fillers-for-her-under-25">stocking fillers guide</a> has more ideas.</p>',
         f'<a href="/blogs/journal/stocking-fillers-for-her-under-25">stocking fillers guide</a> has more ideas, and our {SK} lists every small kit with what is inside.</p>')],
    "stocking-fillers-for-her-under-25": [
        ('More small kits are in our <a href="/blogs/journal/skincare-gift-sets-guide">skincare gift sets guide</a>.</li>',
         f'More small kits are in our <a href="/blogs/journal/skincare-gift-sets-guide">skincare gift sets guide</a> and our {SK}.</li>')],
    "perfume-gift-sets-under-30": [
        ('<a href="/blogs/journal/stocking-fillers-for-her-under-25">stocking fillers for her guide</a> adds lip care and soaps.</p>',
         f'<a href="/blogs/journal/stocking-fillers-for-her-under-25">stocking fillers for her guide</a> adds lip care and soaps. For skincare rather than perfume, see our {SK}.</p>'),
        ('<a href="/blogs/journal/aftershave-under-50">aftershave under £50 guide</a> lists single bottles for him.</p>',
         f'<a href="/blogs/journal/aftershave-under-50">aftershave under £50 guide</a> lists single bottles for him. For a scent to share, see our {UP}.</p>')],
    "womens-perfume-under-50": [
        ('a warm one suits someone who already wears a rich perfume.',
         f'a warm one suits someone who already wears a rich perfume. For a scent you can share, see our {UP}.')],
    "aftershave-under-50": [
        ('a warm, sweet one is a better pick for someone who already wears a rich fragrance.',
         f'a warm, sweet one is a better pick for someone who already wears a rich fragrance. For a scent he can share, see our {UP}.')],
    "oud-perfume-under-60": [
        ('Browse every <a href="/collections/oud-perfume">oud perfume</a>',
         f'For amber, rose and incense scents without oud, see our {UP}. Browse every <a href="/collections/oud-perfume">oud perfume</a>')],
}
COL = {
    "skincare-gift-sets": f" For small kits on a budget, read our {SK}.",
    "gifts-under-25": f" For skincare picks with what is in each kit, read our {SK}.",
    "unisex-perfume": f" For picks by mood on a budget, read our {UP}.",
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
    assert "skincare-gifts-under-25" not in c and "unisex-perfume-under-50" not in c
    out["collections"].append({"id": cols[h]["id"], "handle": h, "before": c, "after": addfirst(c, s)})
p = pathlib.Path(__file__).resolve().parents[2] / "docs/seo/journal_backlinks_wave19_2026-11-28.json"
json.dump(out, open(p, "w"), ensure_ascii=False, indent=1)
print("articles", len(out["articles"]), "collections", len(out["collections"]))
