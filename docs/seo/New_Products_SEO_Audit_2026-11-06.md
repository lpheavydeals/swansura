# New products & brand pages: SEO audit and plan (6 Nov 2026)

Scope: the 202 products and 27 brand collections added on 2 Nov 2026 (plus Armaf, which gained 18 products).
Live theme at audit time: **"Swansura – Skin helper button (draft)" (200468693379, MAIN)**.
Nothing in the store has been changed yet. Every write below waits for the user's go-ahead.

## 1. Audit (read-only)

Crawl: `tools/qa/crawl.py` with THEME=200468693379 over 27 brand collections + 202 products + 16 hub pages
→ `docs/seo/new_products_crawl_live_2026-11-06.json`.

| Check | Result |
|---|---|
| Status | 229/229 pages return 200 on the live theme (2 guessed hub URLs, /collections/body-mist and /collections/deodorants, are 404 because they don't exist; the deodorant collection is `/collections/deodrants`) |
| Liquid errors | 0 |
| One H1 | 229/229 |
| Title ≤ 60 | 229/229 |
| Description 70–160 | 229/229 |
| Canonical = URL | 229/229 |
| JSON-LD | all parse; product pages have Product + BreadcrumbList + FAQPage; brand pages have BreadcrumbList + CollectionPage + FAQPage |
| Images without alt | 0 |
| 'Photo pending' | 40 products show the 'Photo coming soon' card (Maison Alhambra ×25, Vilvah ×6, Natural By Woods ×4, Arabiyat Prestige ×2, Formula 1, Jaguar Classic Gold, Franck Olivier Bella Women 75ml) |
| Inbound links | Every brand page is linked from /collections (Brands A–Z) and /pages/sitemap, plus /collections/fragrance and gender/scent pages through the product cards. Every product except the 4 new Vilvah lip balms is linked from at least one crawled listing page; the lip balms sit in /collections/lip-balm and /collections/concern-lips, which were not in this crawl set; checked separately: all 4 are linked from /collections/lip-balm. |
| Menus | **No new brand is in any menu** (sw-main, sw-footer-brands, sw-drawer). |

### Gaps found

1. **No 'About this page' copy** on any of the 27 new brand collections (`custom.seo_heading` / `custom.seo_copy` empty). Meta descriptions are a generic count sentence ('Shop X perfume at Swansura: N products…'), which goes stale.
2. **Armaf** now has 19 products, but its copy still says "we stock one bottle… Armaf Hunter… £22.99" (Hunter is now £19.99), and its header story says "1 product".
3. **Brand header 'You may also love'** on all 27 new pages lists the same five houses (anatomē, Tiziana Terenzi, Hemel, Fumeri, Al Haramain), whatever the brand. For example, Lattafa doesn't point to Armaf or Afnan, and Guess doesn't point to other designer houses.
4. **Oud / Arabian hubs are out of date:** /collections/arabian-perfume copy says "33 fragrances from Al Haramain, Signature D'orient and Armaf", but the collection holds 104 products from 13 houses. /collections/oud-perfume says "27" (32 now). Both quote old prices (Fumeri £23.95, SAP £37.95, Signature prices), and neither links Lattafa, Afnan, Maison Alhambra, Arabiyat Prestige, Swiss Arabian or Rasasi.
5. **Out-of-date counts/prices on 40 existing pages** (`docs/seo/stale_copy_scan_2026-11-06.json`). These come from the 2 Nov additions and the 3 Nov price + concern-collection changes:
   - perfume-for-women says 67 (now 150), unisex-perfume 230 (323), scent-floral 166 (250), price-15-25 108 (219) …
   - Prices quoted that no product in the collection has any more, e.g. al-haramain, signature-dorient, fumeri, sap, the-woods-collection, concern-acne/glow/sun.
   - Concern pages name products that were moved out on 3 Nov.
6. **Theme:**
   - Brand pages with one product say "Shop all **1 products**" (13 brands, plus share text).
   - The 40 photo-less product pages output `"image": []` in Product JSON-LD, which Google Search Console reports as an invalid Product item (missing image).
   - Main menu label "All 66 brands A–Z" is out of date (about 93 brand pages now).
7. **Data to confirm with the client** (found while writing copy):
   - 'Armaf Club de Nuit Intense Eau de Parfum 105ml' has the notes of Club de Nuit Intense *Woman* (rose, saffron, geranium; the client sheet says women's), but the title doesn't say Woman.
   - Unlimited Courage and Unlimited Passion have identical notes.
   - Natural By Woods Karma has no notes ('not publicly specified').
   - Rihanah Ajwaa Oud has no notes.
8. **All 202 new products are sold out (stock 0)** except Game of Spades Rouge Extrait. Pages index fine (OutOfStock offers), but Google Shopping free listings won't show them until stock is entered.

## 2. Priority by search demand ('Brand searches' / 'Top new products' tabs)

| Brand page | UK searches/mo (KD) | Products | Top product terms |
|---|---|---|---|
| Vera Wang | 5,400 (22) | 1 | – |
| David Beckham | 2,900 (16) | 1 | david beckham beyond 260 |
| Lattafa | 2,400 (24) | 4 | khamrah qahwa 5,400 · teriaq 590 · yara candy 260 |
| Guess | 1,300 (22) | 43 | guess seductive 480 · seductive noir 260 · seductive red 140 · bella vita 170 |
| Swiss Arabian | 1,000 (16) | 1 | – |
| Jaguar | 720 (16) | 5 | – |
| Rasasi | 590 (22) | 1 | hawas elixir 260 |
| Tous | 590 (17) | 1 | – |
| Afnan | 390 (36) | 3 | 9am dive 480 |
| Maison Alhambra | 390 (16) | 25 | – |
| Arabiyat Prestige | 170 (11) | 2 | nyla 1,300 |
| Formula 1 / Franck Olivier / Armand Basi / Bois 1920 / Mercedes-Benz / Notebook / Attar / Fomo / Adi Guru | 10–70 | | mercedes-benz club black 480 · armaf club de nuit precieux 590 / intense 480 · fomo gary's den 110 |
| Fun & Basics / Inaaya / Natural By Woods / Unlimited / Maison de Milan / Chris Adams / Rihanah | 0 | | |

The product terms (Khamrah Qahwa 5,400, Nyla 1,300 …) are already the H1 and title of their product pages. Each brand page's copy links to them.

## 3. Draft brand-page copy (ready, not written to the store)

Generator: `tools/shopify/new_brand_copy.py`.
- Review copy: `docs/seo/new_brand_copy_2026-11-06.md`.
- Store inputs: `docs/seo/new_brand_copy_2026-11-06.jsonl`.

**What each of the 28 brand pages gets** (27 new + Armaf rewrite):
- `custom.seo_heading` (H2) + `custom.seo_copy`: 148–266 words, with '<brand> perfume' in the H2 and the first sentence, and 5–9 internal links to live collections/products. Prices come from the live storefront; no counts are written into the copy.
- A new SEO description (≤160 characters, no count). The SEO title stays ('<Brand> Perfume | Shop at Swansura UK').
- 1–2 extra FAQs (which one to start with, sets, sizes), added after the existing two.
- A brand-specific 'You may also love' list. Arabian houses link to each other, Guess to designer houses, men's houses to men's houses, and niche to niche.
- Armaf's header story is rewritten without the old "1 product".

**Hub refresh:** arabian-perfume and oud-perfume.
- New copy linking Lattafa, Afnan, Armaf, Maison Alhambra, Arabiyat Prestige, Swiss Arabian and Rasasi.
- The new brands are added to the 'Explore more' pills.
- New meta descriptions.

**Copy rules applied:** facts from our catalogue only (notes, sizes, concentration, prices), no medical claims, no stock or sold-out mentions, no partner claim, no 'bestseller', no brand-history claims we can't check. All checks pass (words, keyword in H2 and first sentence, description length, every link is a live handle, banned words).

## 4. Internal links (proposed)

- **sw-main → Brands:**
  - Add a 4th column 'Arabian houses': Lattafa, Armaf, Afnan, Maison Alhambra, Swiss Arabian, Rasasi, Arabiyat Prestige. The mega menu is a 4-column grid, so it fits.
  - Add Guess and Franck Olivier to 'More houses' in place of Chloé and Marc Jacobs.
  - Rename 'All 66 brands A–Z' to 'All brands A–Z'.
- **sw-main → Fragrance → Houses:** add Lattafa and Guess (12 links + A–Z).
- **sw-footer-brands:** add Lattafa and Guess (8 → 10).
- **sw-drawer → Fragrance → Houses:** add Lattafa and Armaf.
- **Already fine:**
  - /collections (Brands A–Z) and /pages/sitemap list all 27 new brands.
  - arabian-perfume already shows the new Arabian brands' products; with the refresh it also links their pages in the copy and pills.
- **Optional, a collection change:** add oud-led new products to /collections/oud-perfume. These are Afnan Supremacy Gold, Armaf Club de Nuit Intense, Maison Alhambra Jean Lowe Matière, Natural By Woods Royal Night and Essence, and Mercedes-Benz Le Parfum (all list agarwood/oud in their notes).

Menus are shared store data, so a menu change shows on the live site straight away (no theme publish needed).

## 5. Duplicate listings ('F') – recommendation (no deletes)

The crawl found no new duplicates: no two products share a title.

| Pair | Same product? | Keep | Retire |
|---|---|---|---|
| Tiziana Terenzi Caput Mundi Extrait 100ml | Yes, identical notes; £99.99 'Luna Collection' (5 in stock, 7 collections) vs £106.99 'Oud' (5 in stock, 11 collections incl. oud-perfume) | `caput-mundi-…-luxury-unisex-oud-perfume` (older, more collections, linked from the oud copy); client confirms the price | `…-luna-collection-…`: set to DRAFT (not delete) + URL redirect to the kept one; client moves its 5 units if they are real extra stock |
| Game of Spades Full House 100ml | Yes; £92.99 (11 in stock, 6 photos) vs 'Jo Milano Game of Spades Full House … EDP' £94.50 (5 in stock, 2 photos) | `game-of-spades-full-house-…` (more photos, matches the other Game of Spades listings) | `jo-milano-game-of-spades-full-house-…`: DRAFT + redirect; client confirms price and combined stock |
| Hermès Un Jardin à Cythère EDT 15ml miniature | Yes; £24.99 (June, 10 in stock) vs £25.99 (Sept, 10 in stock) | `hermes-un-jardin-a-cythere-eau-de-toilette-15ml-miniature-unisex-fragrance` (older, so it has more history) | `hermes-un-jardin-a-cythere-unisex-edt-15ml-miniature`: DRAFT + redirect; client confirms whether it's 10 or 20 units |

Drafting (not deleting) keeps photos, SKUs and order history. Shopify follows a URL redirect only when the old URL 404s, and a draft product 404s on the storefront. Before-state is backed up first.

## 6. Theme fixes (new duplicate of the live theme; the user publishes)

- `sw-p-collection`: 'Shop all 1 product' (singular) in the button and the share text.
- `sw-product-schema` (+ any other Product JSON-LD): leave out `image` when the product has no media. Google treats an empty image as invalid; leaving it out until photos arrive gives a warning instead of an error.

## 7. After the go-ahead
1. Back up the before-state (`docs/backups/new_brand_copy_before_2026-11-06.json`: seo, h1, seo_heading, seo_copy, faq, brand, related for the 30 collections; the menus; the 3 duplicate pairs).
2. Write the copy, SEO, FAQ and brand lists (`collectionUpdate` + `metafieldsSet`), then the menus (`menuUpdate`), then the duplicate drafts + redirects (only for the pairs approved).
3. Theme draft with the two fixes, checked in preview.
4. Re-crawl the 229 pages + hubs on live, check the copy renders (H2 + links 200), and record the results in CLAUDE.md.

## 8. Status (6 Nov 2026, later)
Applied after the user's go-ahead ('copy, menus and theme fixes'): sections 3, 4 (menus only) and 6.
- Brand copy + SEO descriptions + FAQs + 'You may also love' lists on 28 brand pages, and the Oud / Arabian refresh, are live and verified.
- Menus are updated (live straight away).
- Theme fixes are on the draft 'Swansura – Brand pages (draft)' (200547697027), waiting for the user to publish.

Not done (not approved):
- the duplicate listings (section 5);
- adding oud-led products to /collections/oud-perfume;
- the 40 older pages with out-of-date counts/prices: DONE 7 Nov 2026 (37 pages updated; the other 3 were already fixed; see `docs/seo/stale_copy_fix_2026-11-07.md`).
