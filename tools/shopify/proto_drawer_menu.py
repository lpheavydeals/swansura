"""Phone menu 'sw-drawer' from the prototype's drawer (docs/data/prototype_drawer.html, captured from drawerNav()).
details.dn-g -> item with columns (eyebrow spans) -> links; plain links and the advent link -> items.
Output: docs/seo/proto_drawer_menu.json (menuCreate arguments)."""
import json
import re
import sys
import html as H
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from proto_menus import ROOT, link  # noqa: E402

src = (ROOT / "docs/data/prototype_drawer.html").read_text()
body = src[src.index("</div>", src.index('class="dn-feat"')) + 6: src.index('<div class="dn-foot">')]
items = []
for m in re.finditer(r'<details class="dn-g"><summary>(.*?)</summary><div class="dn-in">(.*?)</div></details>|<a href="([^"]+)"[^>]*>(.*?)</a>', body, re.S):
    if m.group(1):
        title = H.unescape(m.group(1))
        inner = m.group(2)
        first = re.search(r'<a href="([^"]+)">', inner).group(1)
        top = link(title, first)
        cols, cur = [], None
        for part in re.finditer(r'<span class="eyebrow">(.*?)</span>|<a href="([^"]+)">(.*?)</a>', inner):
            if part.group(1):
                cur = {"title": H.unescape(part.group(1)), "type": "HTTP", "url": top["url"], "items": []}
                cols.append(cur)
            elif cur is not None:
                cur["items"].append(link(H.unescape(part.group(3)), part.group(2), title, cur["title"]))
        top["items"] = cols
        items.append(top)
    else:
        t = re.sub(r"\s*<small>.*?</small>", "", m.group(4))
        items.append(link(H.unescape(t).strip(), m.group(3)))
menu = {"handle": "sw-drawer", "title": "Swansura phone menu", "items": items}
json.dump(menu, open(ROOT / "docs/seo/proto_drawer_menu.json", "w"), ensure_ascii=False, indent=1)
for i in items:
    print(i["title"], i["url"], [(c["title"], [x["title"] + "=" + x["url"] for x in c["items"]]) for c in i.get("items", [])])
