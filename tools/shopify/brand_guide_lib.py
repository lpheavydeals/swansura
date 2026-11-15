"""Helpers for the Deyga / Vilvah brand guides (16 Nov 2026): variant prices and price per gram/ml from the storefront dump."""


def find(ALL, prefix):
    hits = [h for h, p in ALL.items() if p["title"].startswith(prefix) and any(v["available"] for v in p["variants"])]
    assert len(hits) == 1, (prefix, hits)
    return hits[0]


def vprice(ALL, prefix, variant):
    p = ALL[find(ALL, prefix)]
    vs = [v for v in p["variants"] if v["available"] and variant in v["title"]]
    assert len(vs) == 1, (prefix, variant, [v["title"] for v in p["variants"]])
    return float(vs[0]["price"])


def gbp(x):
    return f"£{x:.2f}".replace(".00", "")


def fill(body, values):
    for k, v in values.items():
        body = body.replace("%%" + k + "%%", v)
    assert "%%" not in body, body[body.index("%%"):body.index("%%") + 40]
    return body
