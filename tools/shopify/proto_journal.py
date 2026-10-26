"""Journal articles from the prototype (JOURNAL in prototype/index.html) as Shopify ArticleCreateInput.

Links are mapped from prototype routes to live URLs; 'Shop the story' goes to custom.products
(read by sw-article-more), the FAQs to custom.faq (json [[q, a], ...]), SEO to global title/description tags.
The hero image is the first shop-the-story product's first Shopify image.
Output: docs/seo/proto_journal_articles.jsonl (blogId filled in at upload)
"""
import ast
import json
import re
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from proto_collections_create import ROOT, X, P, url  # noqa: E402

BY = {str(p["id"]): p for p in P}


def lst(v):
    return ast.literal_eval(v) if isinstance(v, str) else v


out = []
for n, j in enumerate(X["journal"]):
    body = re.sub(r'href="#([^"]+)"', lambda m: f'href="{url(m.group(1))}"', j["body"])
    shop = [i for i in lst(j["shop"]) if i in BY]
    hero = BY[shop[0]]
    out.append({
        "title": j["t"], "handle": j["s"], "author": {"name": "Swansura"}, "body": body,
        "summary": f"<p>{j['d']}</p>", "tags": [j["tag"]], "isPublished": True,
        "publishDate": j["date"] + f"T09:0{len(X['journal']) - 1 - n}:00Z",  # newest first = prototype order
        "image": {"url": hero["i0"], "altText": j["t"]},
        "metafields": [
            {"namespace": "global", "key": "title_tag", "type": "single_line_text_field", "value": j["mt"]},
            {"namespace": "global", "key": "description_tag", "type": "single_line_text_field", "value": j["md"]},
            {"namespace": "custom", "key": "products", "type": "list.product_reference",
             "value": json.dumps([f"gid://shopify/Product/{i}" for i in shop])},
            {"namespace": "custom", "key": "faq", "type": "json", "value": json.dumps(lst(j["faq"]), ensure_ascii=False)},
        ],
    })
with open(ROOT / "docs/seo/proto_journal_articles.jsonl", "w") as f:
    for o in out:
        f.write(json.dumps(o, ensure_ascii=False) + "\n")
for o in out:
    print(o["handle"], len(o["body"]), "chars;", len(json.loads(o["metafields"][2]["value"])), "products;",
          sorted(set(re.findall(r'href="([^"]+)"', o["body"])))[:40])
