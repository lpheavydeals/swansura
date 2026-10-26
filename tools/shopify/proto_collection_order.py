"""Moves that put each new collection's products in the prototype order (c-all rank).

Shopify stores manual-collection selections in ascending product-ID order, so the moves are
computed by simulating that list and moving each product to its target slot in turn.
Output: docs/seo/proto_collection_moves.json  {collection gid: [MoveInput, ...]}  (≤250 moves per call)
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
IDS = dict(l.split(":") for l in """range-rice-water:714068558211 concern-acne:714068656515 concern-glow:714068689283
concern-hydration:714068722051 concern-lips:714068754819 concern-sun:714068787587 concern-hairfall:714068820355
concern-dandruff:714068853123 concern-calm:714068984195 price-0-15:714069016963 price-15-25:714069049731
price-25-50:714069082499 price-50-9999:714069311875 body-butter:714069344643 shower-gel-body-wash:714069377411
body-lotion:714069410179 body-scrub:714069442947 vitamin-c-serum:714069475715 eye-cream:714069508483
conditioner:714069541251 moisturiser-for-dry-skin:714069574019 hair-mask-for-dry-hair:714069639555
hair-oil-for-dry-hair:714069672323 face-wash-for-dry-skin:714069705091 face-wash-for-oily-skin:714069737859
shampoo-for-dandruff:714069770627 body-lotion-for-dry-skin:714069803395 hair-serum-for-frizzy-hair:714069836163
lip-balm-for-dry-lips:714069868931 toner-for-dry-skin:714069901699 natural-sunscreen:714069934467
natural-shampoo:714069967235 body-butter-for-dry-skin:714070327683 hair-growth-oil:714070360451
face-mask-for-oily-skin:714070393219 shampoo-for-hair-loss:714070425987 dry-skin:714070458755
oily-skin:714070491523 sensitive-skin:714070524291 dull-skin:714070557059 hair-fall:714070720899
natural-skincare:714070753667 oud-perfume:714070786435 arabian-perfume:714070819203 perfume-for-women:714070851971
perfume-for-men:714070884739 unisex-perfume:714070950275 niche-perfume:714070983043 perfume-gift-sets:714071015811
travel-size-minis:714071048579 gifts-for-her:714071081347 gifts-for-him:714071114115 gifts-under-25:714071146883
gifts-25-to-50:714071179651 gifts-over-50:714071212419 diwali-gifts:714071245187 ramadan-eid-gifts:714071277955
christmas-gifts:714071310723 stocking-fillers:714071343491 mens-grooming:714071376259 range-beetroot:714071409027
range-goat-milk:714071441795 range-charcoal:714071474563 range-vitamin-c:714071507331 range-rose:714071540099
range-neem:714071572867 range-oud:714071605635 scent-amber:714071671171 scent-oud:714071638403
scent-floral:714071703939 scent-woody:714071736707 scent-fresh:714071769475""".split())
X = json.load(open(ROOT / "docs/data/prototype_export.json"))
RANK = {i: n for n, i in enumerate(X["listings"]["c-all"]["ids"])}



def lis(a):
    """Indexes of one longest strictly increasing subsequence of a."""
    import bisect
    tails, tidx, prev = [], [], [-1] * len(a)
    for i, x in enumerate(a):
        j = bisect.bisect_left(tails, x)
        if j == len(tails):
            tails.append(x); tidx.append(i)
        else:
            tails[j] = x; tidx[j] = i
        prev[i] = tidx[j - 1] if j else -1
    out, i = [], tidx[-1] if tidx else -1
    while i != -1:
        out.append(i); i = prev[i]
    return out[::-1]


out, total = {}, 0
for line in open(ROOT / "docs/seo/proto_collection_creates.jsonl"):
    c = json.loads(line)
    ids = [s["productId"].rsplit("/", 1)[1] for src in c["sources"] for s in src["source"]["inclusion"]["selections"]]
    cur = sorted(ids, key=int)
    want = sorted(ids, key=lambda i: RANK.get(i, 9999))
    # Keep the longest run already in the right relative order; move only the rest, each straight
    # after its predecessor in the target order.
    r = [RANK.get(i, 9999) for i in cur]
    keep = set(cur[j] for j in lis(r))
    moves = []
    for k, pid in enumerate(want):
        if pid in keep:
            continue
        cur.remove(pid)
        pos = cur.index(want[k - 1]) + 1 if k else 0
        cur.insert(pos, pid)
        moves.append({"id": f"gid://shopify/Product/{pid}", "newPosition": str(pos)})
    assert cur == want
    if moves:
        out[f"gid://shopify/Collection/{IDS[c['handle']]}"] = moves
        total += len(moves)
json.dump(out, open(ROOT / "docs/seo/proto_collection_moves.json", "w"), indent=0)
print(len(IDS), "collections mapped;", len(out), "need moves;", total, "moves")
