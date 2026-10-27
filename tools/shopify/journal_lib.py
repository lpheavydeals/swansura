"""Shared helpers for Journal guides written as ArticleCreateInput (guide_*.py).

A guide is a dict: title, handle, tag, summary, mt (SEO title <=60), md (SEO description <=160),
pick {key: handle or None}, titles {key: product-title prefix, for keys without a fixed handle},
shop [keys for 'Shop the story'], body (HTML), faq [[q, a], ...].
In the body, [[key|text]] is a product link and {{key}} its price ('from £x' when variants differ).
Every product must be in stock in the storefront dump ALL (handle -> /products.json product).
Articles are created unpublished: the client approves and publishes.
"""
import json
import re
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
BLOG = "gid://shopify/Blog/127584633219"  # The Journal


def avail(p):
    return any(v["available"] for v in p["variants"])


def build(a, ALL, out_name):
    pick = dict(a["pick"])
    for k, h in pick.items():
        if h is None:
            hits = [x for x, p in ALL.items() if p["title"].startswith(a["titles"][k]) and avail(p)]
            assert len(hits) == 1, (k, hits)
            pick[k] = hits[0]
        assert pick[k] in ALL and avail(ALL[pick[k]]), k

    def price(k):
        ps = {float(v["price"]) for v in ALL[pick[k]]["variants"] if v["available"]}
        return ("from " if len(ps) > 1 else "") + f"£{min(ps):.2f}".replace(".00", "")

    body = re.sub(r"\[\[([\w-]+)\|([^\]]+)\]\]", lambda m: f'<a href="/products/{pick[m.group(1)]}">{m.group(2)}</a>', a["body"])
    body = re.sub(r"\{\{([\w-]+)\}\}", lambda m: price(m.group(1)), body)
    assert "[[" not in body and "{{" not in body
    words = len(re.sub(r"<[^>]+>", " ", body).split())
    shop = [pick[k] for k in a["shop"]]
    assert len(a["mt"]) <= 60 and len(a["md"]) <= 160, (len(a["mt"]), len(a["md"]))
    out = {
        "blogId": BLOG, "title": a["title"], "handle": a["handle"], "author": {"name": "Swansura"}, "body": body,
        "summary": f"<p>{a['summary']}</p>", "tags": [a["tag"]], "isPublished": False,
        "image": {"url": ALL[shop[0]]["images"][0]["src"], "altText": a["title"]},
        "metafields": [
            {"namespace": "global", "key": "title_tag", "type": "single_line_text_field", "value": a["mt"]},
            {"namespace": "global", "key": "description_tag", "type": "single_line_text_field", "value": a["md"]},
            {"namespace": "custom", "key": "products", "type": "list.product_reference",
             "value": json.dumps([f"gid://shopify/Product/{ALL[h]['id']}" for h in shop])},
            {"namespace": "custom", "key": "faq", "type": "json", "value": json.dumps(a["faq"], ensure_ascii=False)},
            {"namespace": "custom", "key": "read_minutes", "type": "number_integer", "value": str(max(2, round(words / 200)))},
        ],
    }
    links = sorted(set(re.findall(r'href="([^"]+)"', body)))
    print(a["handle"], words, "words;", len(links), "links;", len(a["mt"]), len(a["md"]))
    print("non-product links:", [u for u in links if not u.startswith("/products/")])
    with open(ROOT / "docs/seo" / out_name, "w") as f:
        f.write(json.dumps(out, ensure_ascii=False) + "\n")
    return out
