"""Day 4 product updates (SEO title/description, keyword H1, vendor clean-up, full ingredients).

Inputs:  prototype/products.json (st, sd, h1, brand, inci; ids = Shopify product ids)
         docs/backups/products_before_day4_2026-10-26.jsonl (live values before the change)
Outputs: docs/seo/day4_product_updates.jsonl  (bulkOperationRunMutation variables, one productUpdate per line)
         docs/seo/day4_product_changes.csv     (old -> new for every field touched; also the undo list)

Rules
- SEO title: prototype `st` ('Final SEO' tab, 453 products) else '<h1> | Swansura' (<= 60 chars).
- Meta description: prototype `sd` (380) else a generated sentence (<= 160 chars). No medical claims.
- custom.h1: prototype `h1` (keyword H1) for all 545 products.
- Vendor: set to the prototype brand when different; 'Swansura Selection' maps to the store name.
- custom.inci: Vilvah/Deyga full ingredient lists (131 products); kits list each component on its own line.
"""
import csv
import json
import re
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
P = json.load(open(ROOT / "prototype/products.json"))
live = {}
for line in open(ROOT / "docs/backups/products_before_day4_2026-10-26.jsonl"):
    r = json.loads(line)
    if "handle" in r:
        live[r["id"].split("/")[-1]] = r

STORE = "Swansura - The Body Studio"


def cut(s, n):
    if len(s) <= n:
        return s
    s = s[:n + 1].rsplit(" ", 1)[0].rstrip(" ,–-|")
    return s


def short_name(name):
    for a, b in (("Eau de Parfum", "EDP"), ("Eau De Parfum", "EDP"), ("Eau de Toilette", "EDT"), ("Eau De Toilette", "EDT")):
        name = name.replace(a, b)
    return " ".join(name.split())


def gen_title(p):
    name = " ".join(p["h1"].split())
    for n in (name, short_name(name)):
        if len(n + " | Swansura") <= 60:
            return n + " | Swansura"
    n = short_name(name)
    if len(n) <= 60:
        return n
    if " + " in n:  # gift sets: drop the '+ extra' part rather than cut it mid-phrase
        base = n.split(" + ")[0]
        for t in (base + " | Swansura", base):
            if len(t) <= 60:
                return t
    t = cut(n, 60)
    while t.split()[-1].lower() in ("for", "and", "&", "+", "with", "de", "of"):
        t = t.rsplit(" ", 1)[0]
    return t


def truncated(st, h1):
    """Final SEO titles that were cut at 60 characters mid-word or mid-suffix."""
    st = st.strip()
    if re.search(r"\|\s*(S(w(a(n(s(u(r(a( U?)?)?)?)?)?)?)?)?)?$", st) and not re.search(r"Swansura( UK)?$", st):
        return True
    if re.search(r"\+\s*[A-Za-z]+$", st):  # '... 50ml + Body'
        return True
    last = st.split()[-1].lower()
    if last in ("for", "and", "&", "+", "with", "|"):
        return True
    words = {w.lower().strip("()") for w in h1.split()}
    return last.strip("()") not in words and not st.endswith(("Swansura", "Swansura UK")) and any(w.startswith(last) and w != last for w in words)


def gen_desc(p):
    brand = p["brand"] if p["brand"] != "Swansura Selection" else "the Swansura Selection"
    partner = p["brand"] in ("Deyga", "Vilvah")
    tail = " Official UK partner: 100% authentic, shipped from the UK." if partner else " 100% authentic, shipped from the UK, free UK delivery over £40."
    s = f"Shop {p['h1']} from {brand} at Swansura." + tail
    if len(s) > 160:
        s = f"Shop {short_name(p['h1'])} from {brand} at Swansura." + tail
    if len(s) > 160:
        s = f"Shop {short_name(p['h1'])} at Swansura." + tail
    if len(s) > 160:
        s = f"Shop {cut(short_name(p['h1']), 60)} at Swansura." + tail
    if len(s) > 160:
        s = cut(s, 157).rstrip(".") + "."
    return s


def inci_text(inci):
    parts = []
    for comp in inci:
        names = ", ".join(i[0] for i in comp["l"])
        parts.append(f"{comp['n']}: {names}" if len(inci) > 1 else names)
    return "\n".join(parts)


# Final SEO descriptions whose middle sentence was cut mid-phrase or makes a claim (tan removal,
# "instantly brightens"): replaced by the plain partner sentence (26 Oct 2026, while uploading).
TAIL = " Official UK partner: 100% authentic, shipped from the UK, free delivery over £40."
DESC_FIX = {
    "15979325948291": "Buy Deyga Neem Seed Oil, a natural neem oil for skin and hair from Deyga." + TAIL,
    "15979063378307": "Buy Deyga Sunscreen, a natural sunscreen from Deyga." + TAIL,
    "15428515594627": "Buy Deyga ABC Kit, a natural skincare kit from Deyga." + TAIL,
    "15415434346883": "Buy Vilvah Milk Face Kit, natural skincare for dry skin from Vilvah." + TAIL,
    "15415430775171": "Buy Vilvah Body Polishing Kit, natural skincare for dull skin from Vilvah." + TAIL,
    "15415430742403": "Buy Deyga Foot Butter, a natural body butter from Deyga." + TAIL,
    "15415430185347": "Buy Vilvah Milk Mud Mask, a natural face mask from Vilvah." + TAIL,
}

# 'Final SEO' rows matched to the wrong product (wrong brand / wrong size): title, description, H1.
SEO_FIX = {
    "15415431332227": ("Vilvah Natural Under Eye Cream 20ml | Swansura",
                       "Buy Vilvah Natural Under Eye Cream 20ml, a natural eye cream from Vilvah." + TAIL,
                       "Vilvah Natural Under Eye Cream 20ml"),
    "15415430152579": ("Vilvah Hair Growth Oil 50ml | Buy Online UK | Swansura",
                       "Buy Vilvah Hair Growth Oil 50ml, a natural hair growth oil from Vilvah." + TAIL,
                       "Vilvah Hair Growth Oil 50ml"),
}

# Rows where the 'Final SEO' match was wrong or lost the size: correct H1, title + description regenerated.
H1_FIX = {
    "16373060501891": "Calvin Klein Defy Parfum",
    "16368958210435": "Highborn London Night Elixir",
    "16368950346115": "anatomē Expression Eau de Parfum 10ml",
    "16383899664771": "Kenneth Cole Moonlight Blue Eau de Toilette 100ml",
    "16381167239555": "Dunhill Desire Blue Eau de Toilette 100ml",
    "16375981343107": "Elie Saab Elixir Eau de Parfum 50ml",
    "15976069693827": "Vilvah Cream Conditioner 250ML",
    "15976062452099": "Vilvah Goat Milk Shampoo 250ML",
}

lines, log = [], []
for p in P:
    pid = str(p["id"])
    cur = live[pid]
    upd = {"id": cur["id"]}
    if pid in H1_FIX:
        p = dict(p, h1=H1_FIX[pid], st=None, sd=None)
    title = p.get("st")
    if not title or truncated(title, p["h1"]):
        title = gen_title(p)
    title = " ".join(title.split())
    desc = DESC_FIX.get(pid) or p.get("sd") or gen_desc(p)
    if pid in SEO_FIX:
        title, desc, p = SEO_FIX[pid][0], SEO_FIX[pid][1], dict(p, h1=SEO_FIX[pid][2])
    assert len(title) <= 60 and len(desc) <= 160, (pid, title, desc)
    upd["seo"] = {"title": title, "description": desc}
    log += [(pid, cur["handle"], "seo.title", cur["seo"]["title"] or "", title),
            (pid, cur["handle"], "seo.description", cur["seo"]["description"] or "", desc)]
    vendor = STORE if p["brand"] == "Swansura Selection" else p["brand"]
    if vendor != cur["vendor"]:
        upd["vendor"] = vendor
        log.append((pid, cur["handle"], "vendor", cur["vendor"], vendor))
    mfs = [{"namespace": "custom", "key": "h1", "type": "single_line_text_field", "value": p["h1"]}]
    log.append((pid, cur["handle"], "custom.h1", "", p["h1"]))
    if p.get("inci"):
        txt = inci_text(p["inci"])
        mfs.append({"namespace": "custom", "key": "inci", "type": "multi_line_text_field", "value": txt})
        log.append((pid, cur["handle"], "custom.inci", "", txt[:80] + ("…" if len(txt) > 80 else "")))
    upd["metafields"] = mfs
    lines.append({"product": upd})

out = ROOT / "docs/seo"
out.mkdir(exist_ok=True)
with open(out / "day4_product_updates.jsonl", "w") as f:
    for l in lines:
        f.write(json.dumps(l, ensure_ascii=False) + "\n")
with open(out / "day4_product_changes.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["product_id", "handle", "field", "before", "after"])
    w.writerows(log)
print(len(lines), "products;", sum(1 for l in lines if "vendor" in l["product"]), "vendor changes;",
      sum(1 for l in lines if len(l["product"]["metafields"]) > 1), "with ingredients;",
      sum(1 for p in P if not p.get("st")), "generated titles;", sum(1 for p in P if not p.get("sd")), "generated descriptions")
