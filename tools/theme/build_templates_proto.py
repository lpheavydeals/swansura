"""JSON templates on the prototype markup (design port, 26 Oct 2026). Overwrites the Day-2/3 versions
written by build_templates.py for the page types already ported.
Order on listings (prototype): listing → 'About this page' → Studio Letter → FAQs → footer."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
T = ROOT / "theme/templates"
NEWS = {"type": "sw-p-news", "settings": {}}
FAQ = {"type": "sw-auto-faq", "settings": {"eyebrow": "Good to know", "heading": "Questions about Swansura"}}


def write(name, sections, order):
    (T / name).write_text(json.dumps({"sections": sections, "order": order}, ensure_ascii=False, indent=1))
    print(name, order)


listing = {"main": {"type": "sw-p-collection", "settings": {"explore_menu": "sw-footer-shop"}},
           "seo": {"type": "sw-p-seocopy", "settings": {"eyebrow": "About this page"}},
           "newsletter": NEWS, "faq": FAQ}
for name in ("collection.json", "collection.fragrance.json"):
    write(name, listing, ["main", "seo", "newsletter", "faq"])
