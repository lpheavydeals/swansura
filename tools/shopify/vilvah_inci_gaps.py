"""Fill the missing Vilvah ingredient lists (user, 30 Oct 2026: 'source it from vilvahstore.com / deyga.in').

13 active Vilvah products had no custom.inci / custom.inci_data. Lists come from the 'View All Ingredients' popup on
vilvahstore.com product pages (scraped 30 Oct 2026, saved in docs/data/vilvah_inci_site_2026-10-30.json); kits use
their components' lists, contents from the 'What's in it?' line on the matching vilvahstore.com combo page. Components
we already show elsewhere (client catalogue, docs/data/vilvah_inci_2026-10-22.json) keep that list, so a kit and the
single product never disagree. Same shapes as the other kits: inci = 'Component: a, b, c' per line, inci_data =
[{n, l: [[name, marker]], g}]. Not filled: Charcoal Goatmilk Soap (no list on vilvahstore.com), the neem combs and
Deyga's loofah (tools, no formula).
Run: python3 tools/shopify/vilvah_inci_gaps.py  -> docs/seo/vilvah_inci_gaps_2026-10-30.jsonl (metafieldsSet input)
"""
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SITE = json.load(open(ROOT / "docs/data/vilvah_inci_site_2026-10-30.json"))
CAT = json.load(open(ROOT / "docs/data/vilvah_inci_2026-10-22.json"))
KNOWN = {}
for r in CAT:
    for c in r["components"]:
        KNOWN.setdefault(c["n"], c)

FIX = {"Helianthusannuus": "Helianthus annuus", "Aungustifolia": "Angustifolia"}


def split(s):
    for a, b in FIX.items():
        s = s.replace(a, b)
    out, depth, cur = [], 0, ""
    for i, ch in enumerate(s):
        depth += ch == "("
        depth -= ch == ")"
        # keep '1,2-Hexanediol' whole: no split on a comma between digits
        if ch == "," and depth == 0 and not (s[i - 1:i].isdigit() and s[i + 1:i + 2].isdigit()):
            out.append(cur)
            cur = ""
        else:
            cur += ch
    out.append(cur)
    items = []
    for x in out:
        x = re.sub(r"\s+", " ", x).strip().rstrip(".")
        x = re.sub(r"(\S)\(", r"\1 (", x)
        # 'Lavender oil) and Sodium Hydroxide(Lye)' -> two items
        m = re.match(r"(.*\)) and (Sodium hydroxide.*)$", x, re.I)
        items += [m.group(1), m.group(2)] if m else [x]
    return [[i, 0] for i in items if i]


def site(handle, name):
    return {"n": name, "l": split(SITE[handle]["list"]), "g": {}}


SKIN_FINISH = site("skin-finish-sunscreen-spf-50-pa", "Skin Finish Sunscreen SPF 50 PA+++")
def K(n):
    c = json.loads(json.dumps(KNOWN[n]))
    # catalogue artefact: 'Sorbitan Stearate', 'and Sucrose Cocoate' is one ingredient
    l, out = c["l"], []
    for x in l:
        if x[0].startswith("and ") and out:
            out[-1] = [out[-1][0] + " (and) " + x[0][4:], out[-1][1]]
        else:
            out.append(x)
    c["l"] = out
    return c
PRODUCTS = {
    # gid: (title, components)
    "15976330297731": ("Vilvah Skin Finish Sunscreen SPF 50 PA+++", [SKIN_FINISH]),
    "15979036180867": ("Classic Rose Goat Milk Soap Bar 125G", [site("classic-rose-goatmilk-soap", "Classic Rose Goat Milk Soap")]),
    "15979037065603": ("Classic Goatmilk Soap Bar 115G", [site("classic-goatmilk-soap", "Classic Goat Milk Soap")]),
    "15979039097219": ("Cucumber, Curd & Mint Soap Bar 115G", [site("cucumber-yogurt-and-mint-soap", "Cucumber, Curd & Mint Soap")]),
    "15976557183363": ("Vilvah Pore Minimising Kit", [K("Milk Face Toner"), K("Milk Powder Face Wash")]),
    "15976569241987": ("Vilvah Tinted Lip Balm Kit", [site("cream-bun-lip-balm", "Cream Bun Lip Balm"), site("mango-milkshake-lip-balm", "Mango Milkshake Lip Balm")]),
    "15976578351491": ("Vilvah Face Lift Kit", [K("Ultra Moisturising Cream"), site("under-eye-cream-advanced", "Under Eye Cream (Advanced)")]),
    "15976582873475": ("Vilvah AM Brightening Kit", [SKIN_FINISH, K("Milk Drops Serum")]),
    "15976586248579": ("Vilvah Oil Control Kit", [K("Milk Mud Mask"), K("Milk Powder Face Wash")]),
    "15976591950211": ("Vilvah Skin Radiance Large Kit", [SKIN_FINISH, K("Milk Powder Face Wash"), K("Milk Drops Serum")]),
    "15976626094467": ("Vilvah Tan Protection Kit", [SKIN_FINISH, K("Milk Mud Mask")]),
    "15415436476803": ("Vilvah Everyday Skincare Milk Kit", [K("Milk Face Toner"), K("Milk Drops Serum"), K("Melt-in-Milk Sunscreen SPF 50")]),
}


def inci_text(cs):
    return "\n".join(f'{c["n"]}: ' + ", ".join(i[0] for i in c["l"]) for c in cs)


if __name__ == "__main__":
    out = ROOT / "docs/seo/vilvah_inci_gaps_2026-10-30.jsonl"
    with open(out, "w") as f:
        for pid, (title, cs) in PRODUCTS.items():
            owner = f"gid://shopify/Product/{pid}"
            for key, typ, val in (("inci", "multi_line_text_field", inci_text(cs)),
                                  ("inci_data", "json", json.dumps(cs, ensure_ascii=False, separators=(",", ":")))):
                f.write(json.dumps({"ownerId": owner, "namespace": "custom", "key": key, "type": typ, "value": val}, ensure_ascii=False) + "\n")
            print(f"{title}: " + " + ".join(f'{c["n"]} ({len(c["l"])})' for c in cs))
    print(out)
