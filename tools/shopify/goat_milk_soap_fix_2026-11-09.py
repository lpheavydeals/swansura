"""Fix (9 Nov 2026): Vilvah Cucumber, Curd & Mint Soap has no goat milk (its INCI: cucumber juice, curd, mint, plant oils),
but the 9 Nov goat-milk-soap collection held it and called it a goat milk bar in its SEO description, and the
unpublished stocking-fillers guide listed it among 'bars made with farm-fresh goat milk'. Also the range-goat-milk copy
still said 'Swansura Selection makes three goat milk soap bars' (vendor is Vilvah since 26 Oct).
Input: <scratch>/gms_before.json (Admin read of the 3 objects, saved as the backup too).
Output: docs/seo/goat_milk_soap_fix_2026-11-09.json (before/after per field = undo list).
"""
import json, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
B = json.load(open(sys.argv[1]))
out = {"collection_leave": {"collection": "gid://shopify/Collection/714711892355", "product": "gid://shopify/Product/15979039097219"}, "fields": []}

def rep(text, pairs):
    for a, b in pairs:
        assert text.count(a) == 1, a
        text = text.replace(a, b)
    return text

g = B["goat"]
desc = "Goat milk soap bars from Vilvah: Classic, Classic Rose and Charcoal, made with goat milk and plant oils. Shipped from the UK, free delivery over £40."
assert len(desc) <= 150 and "'" not in desc
out["fields"].append({"owner": g["id"], "field": "seo.description", "before": g["seo"]["description"], "after": desc})
copy = rep(g["copy"]["value"], [(
    ' <a href="/products/cucumber-curd-mint-soap-bar-115g">Cucumber, Curd &amp; Mint Soap</a> (£9.99) has a fresh, minty scent.</p>',
    ' Prefer a fresher scent? Vilvah’s <a href="/products/cucumber-curd-mint-soap-bar-115g">Cucumber, Curd &amp; Mint Soap</a> (£9.99) is made with curd and mint rather than goat milk.</p>')])
out["fields"].append({"owner": g["id"], "field": "custom.seo_copy", "type": "multi_line_text_field", "before": g["copy"]["value"], "after": copy})

r = B["range"]
rcopy = rep(r["copy"]["value"], [
    ("from Vilvah, Deyga and Swansura Selection use", "from Vilvah and Deyga use"),
    ("Swansura Selection makes three goat milk soap bars at £9.99: Classic Goatmilk, Classic Rose and Charcoal Goatmilk.",
     "Vilvah makes three goat milk soap bars at £9.99: Classic, Classic Rose and Charcoal (see <a href=\"/collections/goat-milk-soap\">goat milk soap</a>)."),
])
out["fields"].append({"owner": r["id"], "field": "custom.seo_copy", "type": "multi_line_text_field", "before": r["copy"]["value"], "after": rcopy})

a = B["article"]
body = rep(a["body"], [(
    'The Vilvah bars are made with farm-fresh goat milk: <a href="/products/classic-rose-goat-milk-soap-bar-125g">Classic Rose Goat Milk Soap</a> (£9.99) with rose petals and pink clay, <a href="/products/classic-goatmilk-soap-bar-115g">Classic Goat Milk Soap</a> (£9.99) with lavender essential oil, and <a href="/products/cucumber-curd-mint-soap-bar-115g">Cucumber, Curd &amp; Mint Soap</a> (£9.99) for a fresh morning shower. See all four in <a href="/collections/goat-milk-soap">goat milk soap</a>.',
    'Vilvah’s goat milk bars are made with farm-fresh goat milk: <a href="/products/classic-rose-goat-milk-soap-bar-125g">Classic Rose Goat Milk Soap</a> (£9.99) with rose petals and pink clay, and <a href="/products/classic-goatmilk-soap-bar-115g">Classic Goat Milk Soap</a> (£9.99) with lavender essential oil; see them all in <a href="/collections/goat-milk-soap">goat milk soap</a>. For a fresh morning shower, <a href="/products/cucumber-curd-mint-soap-bar-115g">Cucumber, Curd &amp; Mint Soap</a> (£9.99) is made with curd and mint.')])
out["fields"].append({"owner": a["id"], "field": "article.body", "before": a["body"], "after": body})
json.dump(out, open(ROOT / "docs/seo/goat_milk_soap_fix_2026-11-09.json", "w"), ensure_ascii=False, indent=1)
print("ok", [f["field"] for f in out["fields"]])
