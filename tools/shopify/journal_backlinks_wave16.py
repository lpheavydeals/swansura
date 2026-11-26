"""Back-links to the 5 guides published 25 Nov 2026 (Guerlain, Carolina Herrera, Elie Saab, Game of Spades,
Bvlgari); user, 25 Nov 2026: 'Add the back-links'. One sentence each, nothing else changed.

Usage: python3 tools/shopify/journal_backlinks_wave16.py <admin.json>
  admin.json = {data:{a1:{nodes:[{id,handle,body}]}, c:{nodes:[{id,handle,sc:{value,type}}]}}}
Output: docs/seo/journal_backlinks_wave16_2026-11-25.json (before/after per item = undo list)
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
G = lambda h, t: f'<a href="/blogs/journal/{h}">{t}</a>'
GUE = G("guerlain-perfume-guide", "Guerlain perfume guide")
CH = G("carolina-herrera-perfume-guide", "Carolina Herrera perfume guide")
ES = G("elie-saab-perfume-guide", "Elie Saab perfume guide")
GOS = G("game-of-spades-perfume-guide", "Game of Spades guide")
BV = G("bvlgari-perfume-guide", "Bvlgari perfume guide")

# (article handle, unique anchor, text inserted right after the anchor)
ART = [
    ("oud-perfume-guide", "A rose-and-leather oud, made unisex.", f" Every Guerlain we stock is in our {GUE}."),
    ("mini-perfume-sets-guide", "Bloom of Rose, all built on lavender and vanilla.", f" The full Guerlain range is in our {GUE}."),
    ("best-perfume-gift-sets-uk-2026", "a 10ml spray and a 75ml body lotion, with orange blossom, jasmine and tuberose.", f" Our {ES} compares the whole range."),
    ("best-perfume-gift-sets-uk-2026", "citron and calamansi over vetiver, orris and an earthy, resinous base.", f" Our {BV} compares the Essence sets."),
    ("best-perfume-gift-sets-uk-2026", "our <a href=\"/blogs/journal/versace-perfume-guide\">Versace perfume guide</a>.", f" For Bad Boy and 212, see our {CH}."),
    ("tom-ford-perfume-guide", "over guaiac wood, benzoin and tonka bean.</li>\n</ul>", None),  # handled below
    ("christmas-gift-guide", "fresh green tea, white lotus, musk and guaiac wood.", f" The Bvlgari sets in stock are in our {BV}."),
]
COL = {
    "guerlain": f" Our {GUE} compares them all.",
    "carolina-herrera": f" Our {CH} compares the Bad Boy and 212 scents.",
    "elie-saab": f" Our {ES} compares them all.",
    "jo-milano": f" Our {GOS} compares every scent.",
    "bvlgari": f" Our {BV} compares them all.",
}

d = json.load(open(sys.argv[1]))["data"]
arts = {a["handle"]: a for a in d["a1"]["nodes"]}
out = {"articles": [], "collections": []}
work = {}
for h, anchor, add in ART:
    body = work.get(h, arts[h]["body"])
    if h == "tom-ford-perfume-guide":
        anchor = "(100ml), with rum, spices and tobacco, leather, tuberose and iris, over guaiac wood, benzoin and tonka bean."
        add = f" More in our {BV}."
    assert body.count(anchor) == 1, (h, anchor, body.count(anchor))
    work[h] = body.replace(anchor, anchor + add)
for h, body in work.items():
    out["articles"].append({"id": arts[h]["id"], "handle": h, "before": arts[h]["body"], "after": body})
for c in d["c"]["nodes"]:
    v = c["sc"]["value"]
    i = v.index("</p>")
    out["collections"].append({"id": c["id"], "handle": c["handle"], "before": v, "after": v[:i] + COL[c["handle"]] + v[i:]})
p = ROOT / "docs/seo/journal_backlinks_wave16_2026-11-25.json"
json.dump(out, open(p, "w"), ensure_ascii=False, indent=1)
print(p, [a["handle"] for a in out["articles"]], [c["handle"] for c in out["collections"]])
