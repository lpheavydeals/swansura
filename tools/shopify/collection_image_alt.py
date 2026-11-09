"""Collection cover image alt text (9 Nov 2026, user: 'Go ahead with the ... collection alt text').

Every collection that has a cover image had altText null/'' (Shopify admin + SEO apps flag them).
Writes docs/backups/collection_image_alt_before_2026-11-09.json (before = all empty) and
docs/seo/collection_image_alt_2026-11-09.json (id, handle, image id, new alt) for collectionUpdate(collection:{id, image:{id, altText}}).
"""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
# (collection id, handle, image id, alt) — ids from the Admin collections query of 9 Nov 2026
C = [
 (687767716227, 'vilvah', 2061701611907, 'Vilvah natural skincare and haircare at Swansura'),
 (687768011139, 'deyga', 2061701644675, 'Deyga natural skincare and bodycare at Swansura'),
 (689023713667, 'jo-milano-paris-1', 2062153941379, 'Jo Milano Paris Game of Spades perfumes at Swansura'),
 (689090396547, 'serum', 2062165737859, 'Face serums at Swansura'),
 (689285038467, 'lip-balm', 2062210728323, 'Natural lip balms at Swansura'),
 (689285104003, 'lip-scrub', 2062210793859, 'Lip scrubs at Swansura'),
 (689285333379, 'shampoo', 2062210826627, 'Shampoo and conditioner at Swansura'),
 (689285693827, 'hair-oil', 2062210859395, 'Natural hair oils at Swansura'),
 (689286316419, 'hair-mask', 2062210990467, 'Hair masks at Swansura'),
 (689291919747, 'moisturizers-gels', 2062212006275, 'Moisturisers and gels at Swansura'),
 (689292050819, 'toner', 2076250407299, 'Face toners at Swansura'),
 (689292575107, 'deodrants', 2062211875203, 'Natural deodorants at Swansura'),
 (689293558147, 'giftsets', 2062224130435, 'Vilvah skincare sets and kits at Swansura'),
 (689293951363, 'bestsellers', 2062211940739, 'Deyga bestsellers at Swansura'),
 (689294344579, 'vilvah-bestsellers', 2062224163203, 'Vilvah bestsellers at Swansura'),
 (689297293699, 'deyga-kits', 2062224228739, 'Deyga skincare sets and kits at Swansura'),
 (689298735491, 'luxury-collection', 2062212694403, 'Luxury perfume collection at Swansura'),
 (689352507779, 'vilvah-solo-products', 2062224097667, 'Vilvah single products at Swansura'),
 (689355260291, 'deyga-solo-products', 2062224195971, 'Deyga single products at Swansura'),
 (689522835843, 'vilvah-gift-bundle', 2062326694275, 'Vilvah gift bundles at Swansura'),
 (689522868611, 'deyga-gift-bundle', 2062326727043, 'Deyga gift bundles at Swansura'),
 (689527685507, 'fragrance', 2074431324547, 'Designer, niche and Arabian perfume at Swansura'),
 (689549017475, 'jo-milano', 2062332068227, 'Jo Milano Paris perfumes at Swansura'),
 (689549083011, 'diamond-collection', 2062332035459, 'Jo Milano Diamond Collection perfumes at Swansura'),
 (689549115779, 'prestige-collection', 2062332100995, 'Prestige perfume collection at Swansura'),
 (689549148547, 'gift-sets', 2062332166531, 'Perfume gift sets at Swansura'),
 (693969322371, 'blushing-beauty-solo-glow', 2064260006275, 'Blushing Beauty skincare at Swansura'),
 (704188907907, 'fumeri', 2074085982595, 'Fumeri perfumes at Swansura'),
 (704189694339, 'hemel', 2074096566659, 'Hemel perfumes at Swansura'),
 (704189759875, 'sap', 2074090406275, 'SAP perfumes at Swansura'),
 (704189858179, 'the-woods-collection', 2074432799107, 'The Woods Collection perfumes at Swansura'),
 (704189923715, 'signature-dorient', 2074421559683, "Signature D'orient perfumes at Swansura"),
 (704189956483, 'korloff', 2074314310019, 'Korloff perfumes at Swansura'),
 (704773816707, 'abercrombie-fitch', 2074423329155, 'Abercrombie & Fitch perfumes at Swansura'),
 (705698988419, 'yves-saint-laurent', 2075015479683, 'Yves Saint Laurent perfumes at Swansura'),
 (705824522627, 'hermes', 2075079672195, 'Hermès perfumes at Swansura'),
 (705825964419, 'hugo-boss', 2075080851843, 'Hugo Boss perfumes at Swansura'),
 (705881833859, 'david-beckham', 2075094843779, 'David Beckham perfumes at Swansura'),
 (711733444995, 'tiziana-terenzi', 2076431122819, 'Tiziana Terenzi extrait de parfum at Swansura'),
 (712998453635, 'skincare', 2076945908099, 'Natural skincare at Swansura'),
]
out = [{'id': f'gid://shopify/Collection/{c}', 'handle': h, 'image_id': f'gid://shopify/CollectionImage/{i}', 'alt': a} for c, h, i, a in C]
assert all(len(x['alt']) <= 125 for x in out)
json.dump([{'id': x['id'], 'handle': x['handle'], 'image_id': x['image_id'], 'altText': None} for x in out],
          open(ROOT / 'docs/backups/collection_image_alt_before_2026-11-09.json', 'w'), indent=1)
json.dump(out, open(ROOT / 'docs/seo/collection_image_alt_2026-11-09.json', 'w'), ensure_ascii=False, indent=1)
print(len(out))
