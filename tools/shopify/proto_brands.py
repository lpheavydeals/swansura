"""Brand page data (brandPage() in the prototype) for the custom.brand (json) metafield on each brand collection:
  world (skin|scent), partner, line, story, count (prototype count, corrected brands), and 'others':
  the five 'You may also love' brands (topBrands(world, 12): brands with a story first, then by size)
  as [name, url, line, logo] with logo = theme asset name (prototype/logos/<slug>.webp -> assets/logo-<slug>.webp).
Output: docs/seo/proto_brands.json {collection handle: data}."""
import json
import re
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from proto_menus import ROOT, link  # noqa: E402

X = json.load(open(ROOT / "docs/data/prototype_export.json"))
BR = X["brands"]
html = (ROOT / "prototype/index.html").read_text()
block = html[html.index("const STORIES = {"):]
block = block[:block.index("\n};")]
STORIES = set(re.findall(r"^\s*'([^']+)':\s*\{", block, re.M) + re.findall(r'^\s*"([^"]+)":\s*\{', block, re.M))
LOGOS = {p.stem for p in (ROOT / "prototype/logos").glob("*.webp")}

# corrected brands: Azzaro (5, from Bentley) and Boucheron (2, from Antonio Banderas)
BR["Bentley"]["count"] = 6
BR["Antonio Banderas"]["count"] = 4
for name, n in (("Azzaro", 5), ("Boucheron", 2)):
    BR[name] = {"slug": name.lower(), "count": n, "world": "scent", "partner": False, "line": "Fragrance house",
                "story": f"{name} at Swansura: {n} products, 100% authentic and shipped from the UK.", "h1": f"{name} Perfume"}


def logo_slug(name, slug):
    for s in (slug, re.sub(r"[^a-z0-9]+", "-", name.lower().replace("&", "and")).strip("-")):
        if s in LOGOS:
            return s
    return None


def top(world, n):
    names = [b for b in BR if BR[b]["world"] == world]
    return sorted(names, key=lambda b: (-(b in STORIES), -BR[b]["count"]))[:n]


out = {}
for b, v in BR.items():
    url = link("", "b-" + v["slug"])["url"]
    m = re.match(r"^/collections/([^/?]+)$", url)
    if not m:
        print("no collection for", b, url)
        continue
    others = [k for k in top(v["world"], 12) if k != b][:5]
    out[m.group(1)] = {"name": b, "world": v["world"], "partner": bool(v.get("partner")), "line": v["line"], "story": v["story"],
                       "count": v["count"],
                       "others": [[k, link("", "b-" + BR[k]["slug"])["url"], BR[k]["line"], logo_slug(k, BR[k]["slug"])] for k in others]}
json.dump(out, open(ROOT / "docs/seo/proto_brands.json", "w"), ensure_ascii=False, indent=1)
print(len(out), "brand collections; stories:", sorted(STORIES))
print(json.dumps(out.get("milk-drop-brightening-serum-1"), ensure_ascii=False)[:700])
