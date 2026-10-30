"""Brand page addresses (user, 30 Oct 2026: 'go ahead' with the e-commerce SEO fixes).

Old brand collections still had typing-leftover handles: Vilvah was /collections/milk-drop-brightening-serum,
Deyga milk-drop-brightening-serum-1, Jo Milano luxury-collection-1, Tom Ford tomford, ... ('vilvah' = 480 UK
searches/month, 'deyga' = 140, and neither was in its own URL). This file holds the old -> new map and the helpers
that rewrite stored links; the store writes go through the Shopify connector:
  collectionUpdate(handle, redirectNewHandle: true)  -> Shopify adds the 301 old -> new
  urlRedirectUpdate for redirects that pointed at an old handle (no chains)
  menuUpdate for sw-main / sw-footer-brands / sw-drawer (HTTP links)
  metafields / article bodies with /collections/<old> links
Backup + undo list: docs/backups/brand_handles_before_2026-10-30.json
"""
import json
import re
import sys

MAP = {
    "milk-drop-brightening-serum-1": "deyga",
    "milk-drop-brightening-serum": "vilvah",
    "luxury-collection-1": "jo-milano",
    "tomford": "tom-ford",
    "antonio": "antonio-banderas",
    "ysl": "yves-saint-laurent",
    "phillip-plein": "philipp-plein",
    "joop-homme": "joop",
    "jean-paul": "jean-paul-gaultier",
    "hemel-h": "hemel",
    "signature-sillage-dorient": "signature-dorient",
}
RE = re.compile(r"/collections/(" + "|".join(sorted(map(re.escape, MAP), key=len, reverse=True)) + r")(?![\w-])")


def fix(text):
    """Rewrite every /collections/<old> link in a string (also inside JSON / HTML)."""
    return RE.sub(lambda m: "/collections/" + MAP[m.group(1)], text) if isinstance(text, str) else text


def menu_items(items):
    out = []
    for it in items:
        o = {"id": it["id"], "title": it["title"], "type": it["type"], "url": fix(it["url"])}
        if it.get("resourceId"):
            o["resourceId"] = it["resourceId"]
        o["items"] = menu_items(it.get("items") or [])
        out.append(o)
    return out


if __name__ == "__main__":
    # python3 brand_handles.py menus MENUS_QUERY_RESULT.json  -> menuUpdate variables for menus with old links
    if sys.argv[1] == "menus":
        menus = json.load(open(sys.argv[2]))["data"]["menus"]["nodes"]
        for m in menus:
            if RE.search(json.dumps(m)) and m["handle"].startswith("sw-"):
                print(json.dumps({"id": m["id"], "title": m["title"], "handle": m["handle"], "items": menu_items(m["items"])}, ensure_ascii=False))
