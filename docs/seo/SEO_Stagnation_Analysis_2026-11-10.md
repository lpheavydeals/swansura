# Why search traffic is flat: analysis, 10 Nov 2026

Question (user): Search Console impressions and clicks have been flat for 20 days, with no gradual growth. Some pages were submitted for indexing by hand.

No Search Console access in this session. Sources: a live crawl of all 1,160 sitemap URLs (`docs/seo/sitemap_crawl_live_2026-11-10.json`), Shopify session analytics, and a public search-engine snapshot.

## 1. What is NOT the problem (technical health is clean)
- All 1,160 sitemap URLs (893 products, 232 collections, 9 pages, 25 articles) return 200, with no redirects.
- Canonical = the page's own URL on every page; only /pages/wishlist is noindex (on purpose).
- 0 Liquid errors, one H1 per page.
- Duplicate titles: only the 3 known duplicate listings (Caput Mundi, Full House, Cythère).
- robots.txt is Shopify's default, nothing important blocked.
- http/non-www → https://www 301.
- No Shopify Markets copies (/en-us etc. 404); search pages are noindex; pagination is self-canonical.
- Product pages are not thin: median ~770 words on the page.

## 2. What the data shows
Shopify sessions from Google, UK visitors only, per week:

| Weeks | Sessions per week |
|---|---|
| Sep 7 – Sep 28 | 1–2 |
| Oct 5 | 11 |
| Oct 12 – Nov 2 | 4–9 |
| Last 30 days, total | 30 UK + 34 India + 27 elsewhere |

UK landing pages (last 30 days):
- Homepage: 7 (brand searches).
- About 20 single visits to long-tail fragrance product pages (Chopard Oud Malaki, Davidoff Cool Water Reborn Intense, Gucci minis …).
- **0 visits from the 25 Journal guides, 0 from the ~230 collection / concern / keyword pages, 1 from skincare.**

A public search-engine snapshot still shows old pages and old titles:
- legacy collections: 'Deyga Bestsellers', 'Deyga Solo Glow', 'Bodycare Kits', 'Deodrants';
- a La Maison product deleted on 6 Nov.

A search for the brand with Vilvah/Deyga finds nothing about Swansura.

## 3. Causes, most important first
1. **Low authority.** There are almost no external links to the domain, and the brand is barely known to search engines. The pages we wrote target terms owned by LOOKFANTASTIC, Boots, Notino, Cult Beauty and the brands themselves: vitamin c serum KD 44, face mask, tom ford perfume KD 55, dior sauvage. A new domain gets impressions there at page 3–6, which barely move and get no clicks. Only very long-tail product names reach page 1.
2. **Too new and too much change.** Google needs several weeks of stable pages to rank them. In the last 3 weeks:
   - 25 Journal guides were published (9 of them in the last 3 days);
   - 331 new products were created (202 on 2 Nov, 129 on 8 Nov), all with 0 stock, many without photos;
   - 11 brand URLs were renamed (31 Oct, 301s);
   - titles and descriptions of nearly every product were rewritten one to three times;
   - 7 theme publishes went out.

   Each change sends pages back into evaluation. A request to index a page by hand only speeds up the crawl, not the ranking.
3. **Sitemap.** As of 28 Oct /sitemap.xml had never been submitted. Check in Search Console → Sitemaps when it was submitted and how many URLs are 'Discovered – currently not indexed'. If it went in on ~9 Nov, the 20 days mostly predate it.
4. **Old duplicate collections still indexed.** 21 legacy collections are in the sitemap with no menu or internal link and no SEO text. They repeat the real pages and compete with them:

   | Legacy collection | Products | Duplicates |
   |---|---|---|
   | deyga-solo-products | 53 | /collections/deyga |
   | vilvah-solo-products | 45 | /collections/vilvah |
   | bestsellers | 22 | |
   | vilvah-bestsellers | 31 | |
   | best-sellers | 17 | |
   | deyga-kits | 21 | |
   | body-cream-exfoliants | 26 | |
   | lipcare-sets | 9 | |
   | bodycare-kits | 5 | |
   | blushing-beauty-solo-glow | 2 | |
   | makeup-product | 2 | |
   | luxury-collection-2 | 1 | |
   | prestige-collection | 1 | |
   | davidoff-1 | 1 | |
   | vilvah-gift-bundle | 1 | |
   | deyga-gift-bundle | 0 | |
   | luxury-collection | 0 | |
   | giorgia-armani | 0 | |
   | diamond-collection | 5 | |
   | gift-sets | 4 | |
   | jo-milano-paris-1 | 3 | |

   These are what search engines show for Swansura today.
5. **Many low-value URLs.**
   - 127 product pages are sold out, and 102 have no photo (28 are both).
   - 71 collections hold 3 products or fewer, mostly one-product brand pages.

   A low-authority site with a large share of thin or sold-out URLs gets crawled less often and ranked lower overall.

## 4. What to do
Ours to do (needs the user's OK where it changes the store):
- A. Redirect the 21 legacy collections to their real page (delete + 301, data backed up first).
- B. noindex (or leave out) one-product brand pages whose only product is sold out; keep the ones with stock.
- C. Freeze titles, descriptions and URLs for 4–6 weeks, so Google can settle.
- D. Get photos + stock on the 2 Nov / 8 Nov products, or move the photo-less sold-out ones back to draft.

Client / account side:
- E. Search Console: confirm the sitemap is submitted. Then export, so the analysis can use real data:
  - Performance (last 3 months: Queries + Pages, with impressions and position);
  - Pages (indexing) report counts and examples.
- F. Links: the backlink plan's priority 1. Stockist links from Deyga, Vilvah and anatomē, and Highborn's stockist page. Then UK beauty journalists (#journorequest) and the gift-guide pitches.
- G. Merchant Center free listings already bring orders (4 of 15). Keep the feed healthy: barcodes (GTINs), stock, photos.

Realistic expectation: for a 1–2-month-old domain with no links, steady growth usually starts 6–12 weeks after the pages stop changing. The quickest wins are the Vilvah/Deyga product and brand names, where few UK shops compete.
