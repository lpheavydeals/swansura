"""Vilvah Tinted Lip Balm Kit price £17.99 -> £17 in 2 Journal articles (user, 15 Nov 2026: 'Yes, fix the price in both').

Live price changed to £17.00 in Shopify on 14 Nov. Only the price in brackets after the kit link changes.
Usage: python3 tools/shopify/kit_price_fix_2026-11-15.py <journal.atom>
Output: docs/seo/kit_price_fix_2026-11-15.json (id, before, after per article = undo list)
"""
import json, re, sys

IDS = {"christmas-gift-guide": "gid://shopify/Article/1005324665219",
       "how-to-use-lip-scrub": "gid://shopify/Article/1005468221827"}
OLD = 'vilvah-tinted-lip-balm-kit">Vilvah Tinted Lip Balm Kit</a> (£17.99)'
NEW = 'vilvah-tinted-lip-balm-kit">Vilvah Tinted Lip Balm Kit</a> (£17)'
feed = open(sys.argv[1]).read()
out = []
for e in re.findall(r'<entry>(.*?)</entry>', feed, re.S):
    h = re.search(r'blogs/journal/([a-z0-9-]+)', e).group(1)
    if h not in IDS: continue
    before = re.search(r'<content[^>]*>\s*<!\[CDATA\[(.*?)\]\]>\s*</content>', e, re.S).group(1).strip()
    assert before.count(OLD) == 1, h
    out.append({"handle": h, "id": IDS[h], "before": before, "after": before.replace(OLD, NEW, 1)})
assert len(out) == 2
json.dump(out, open("docs/seo/kit_price_fix_2026-11-15.json", "w"), ensure_ascii=False, indent=1)
print("ok", [o["handle"] for o in out])
