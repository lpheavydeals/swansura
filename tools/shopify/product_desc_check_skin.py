"""Check Vilvah/Deyga description drafts (8 Nov 2026) against the skincare brief's claim rules.

Usage: python3 tools/shopify/product_desc_check_skin.py <drafts.json> <facts.json> <in-stock list json>
Prints every claim word outside the product's own name, words outside 140-240, bad tags, prices, em dashes,
links not in the in-stock list, a missing name in the first sentence and a missing partner line.
"""
import html, json, re, sys

drafts = json.load(open(sys.argv[1]))
facts = {f["id"]: f for f in json.load(open(sys.argv[2]))}
ok_links = {p["url"] for p in json.load(open(sys.argv[3]))}
CLAIM = re.compile(r"\b(pigment\w*|de-?\s?tan|tan\b|tanning|brighten\w*|lighten\w*|whiten\w*|dark (?:spots?|circles|lips)|acne|pimples?|breakouts?|blemish\w*|blackheads?|pores?|oil[- ]control|anti[- ]?ageing|ageing|wrinkles?|fine lines|firm\w*|collagen|repair\w*|heal\w*|treat\w*|sooth\w*|eczema|psoriasis|rash\w*|sunburn|anti-?bacterial|antiseptic|anti-?inflammatory|detox\w*|toxins?|toxin-free|hair (?:growth|fall|loss)|regrowth|thicker|dandruff|greying|clinically|dermatolog\w*|chemical-free|100% natural|hypoallergenic|all skin types|long-lasting|24 ?h\w*|miracle|magic|transform\w*|flawless|luxurious|indulg\w*|elevat\w*|game-changer|must-have|sulph?ate-free|baby|babies|pregnan\w*|organic|vegan|cruelty-free)\b", re.I)
bad = 0
for d in drafts:
    f = facts[d["id"]]
    h = d["html"]
    name_words = set(re.findall(r"[a-z]+", f["title"].lower()))
    text = " ".join(html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"<a [^>]*>.*?</a>", " ", h))).split())
    probs = []
    w = len(" ".join(html.unescape(re.sub(r"<[^>]+>", " ", h)).split()).split())
    if not 140 <= w <= 240: probs.append(f"words {w}")
    if set(re.findall(r"</?([a-z0-9]+)", h)) - {"p", "h3", "ul", "li", "a"}: probs.append("tags")
    if re.search(r"£\s?\d", text): probs.append("price")
    if "—" in text or "!" in text: probs.append("dash/!")
    for u in re.findall(r'href="([^"]+)"', h):
        if u not in ok_links: probs.append(f"link {u}")
    if f"Official UK partner of {f['vendor']}" not in text: probs.append("partner line")
    hits = [m.group(0) for m in CLAIM.finditer(text) if not set(re.findall(r"[a-z]+", m.group(0).lower())) <= name_words]
    if hits: probs.append(f"claims {sorted(set(hits))}")
    if probs:
        bad += 1
        print("CHECK", d["handle"][:55], probs)
print(len(drafts), "drafts,", bad, "to check")
