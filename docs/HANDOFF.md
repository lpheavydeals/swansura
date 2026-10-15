# Swansura Project — Handoff

Prepared 15 Oct 2026 for continuing this project in another Claude account.
To continue: start a new chat, upload this file, and say "Continue this project from here."

---

## 1. Who's who

- **Agency:** Lokesh · www.thebilliongame.com (India-based; pitching to the client).
- **Client:** Swansura — "Swansura - The Body Studio". UK online retailer of Indian natural skincare brands (e.g. Vilvah, Deyga) and Arabian fragrance brands.
  - Website: swansura.com (Shopify)
  - Instagram: @swansura_thebodystudio
  - Also sells on Amazon UK
  - Swansura is an *official* seller of its brands, not the *exclusive* partner.
- **Competitors studied:**
  - Market leaders: LOOKFANTASTIC, Cult Beauty
  - Contemporaries: Beauty Bay, Space NK

---

## 2. Links (owned by abracaindia@gmail.com — share them to the new account via each page's Share menu)

| What | Link |
|---|---|
| Growth Audit deck (31 slides) | https://claude.ai/artifact/4RwEraopJpv1XHkNWw9rZ6 |
| Research doc: UK Competitor & Meta Ads Research (includes a Digital Audit tab) | https://claude.ai/artifact/2SLfh5MdFBP2WM4GPDokDn |
| Website prototype (paused) | https://claude.ai/artifact/N2uLcT9vSsDYkUCg8ythUc |

**Local files**
- `Downloads\Swansura_Product_Data_Sheet.xlsx`: blank product sheet for the client to fill in.
- `Downloads\session-export-1792065745768.zip`: full chat transcript.

---

## 3. Key audit data (checked 9 Oct 2026 unless stated)

**Catalogue**
- 493 products live: 467 in stock, 26 sold out. 4 Shopify demo products are still live.
- 302 products (61%) are fragrance. Only 32 are in the Skincare collection.
- 170 products are filed under "Generic" (88) or "Swansura - The Body Studio" (82) instead of their real brand.
- 15 collections are empty or duplicates (e.g. fr, fr-1, frag, frag-1, hem, hem-1), plus a live "Default example products" demo collection.
- The Vilvah collection URL is /collections/milk-drop-brightening-serum, with the meta description "sample vilvah".

**Google Search Console** (10 Aug–4 Oct 2026, from the client's screenshots; we have no direct access)
- 46 clicks, 4.22K impressions, 1.1% CTR, average position 14.1.
- All known URLs: 359 indexed, 417 not indexed (10 reasons).
- Sitemap view: 44 pages, 14 indexed, 30 not indexed (2 reasons).
- The product and collection sitemaps are **not submitted yet**. This is the main reason indexing is low.

**PageSpeed**
- Desktop 97, mobile 71.
- SEO 100, accessibility 93, best practices 88.

**On-page issues**
- The homepage H1 is empty; collection H1s read "Collection: X".
- Page titles repeat the name: "… | Swansura – Swansura - The Body Studio".
- Collections have no intro text or FAQs.
- Cart, search and demo pages are indexable.
- Product schema has no ratings.
- 19 of 85 homepage images lack alt text.
- Only 1 blog post (Jan 2026); no brand pages.

**Meta and social**
- 0 Meta ads ever run (Meta Ad Library, UK, all time), although the Meta Pixel is installed.
- Instagram: 34 followers. Competitors have 697K–1.8M.

---

## 4. Growth Audit deck — current state

**Design**
- Slides type, Plus Jakarta Sans font, modern card style. All font sizes were increased by 2px.
- Footer on every slide:
  - Left: "Swansura Growth Audit · NN" (slide number).
  - Right: "Sources: Search Console, PageSpeed, Meta Ad Library, swansura.com & Claude".
- The cover says "Prepared by Lokesh · www.thebilliongame.com".

**Slide order (31 slides)**
1. Cover, summary, opportunity, scorecard.
2. Website: divider, blockers, catalogue, fix, CRO and AOV, pricing (2 slides), routines and combos.
3. SEO: divider, index, targets, on-page, rankings, brands, site structure (Indicrest.co.uk example), The Body Shop keywords, keyword map, plan.
4. Meta: divider, landscape, patterns, Swansura, plan, seasonal plan.
5. Social: benchmark, plan.
6. Roadmap.

**Roadmap**
- 30 days of website, SEO and social work.
- Meta Ads from day 31.
- Proposed addition, not added to the deck yet: a single-product Meta pilot from about day 7 (see section 6).

**Removed at the user's request:** the packages and next-steps slides.

**Open question:** the user once said "Reverse that, maybe you can include…" about the footer sources and didn't finish the sentence. They had asked whether to add "Screaming Frog, Semrush, Ahrefs & Claude". Still unresolved.

---

## 5. Website prototype (paused)

- Inspired by Forest Essentials, The Body Shop and Mamaearth. Uses the same font as the slides.
- **Shop:** full catalogue with a filter panel that stays put while the product list scrolls, coloured trust badges, a fixed Add to bag bar and a styled scrollbar.
- **Pages:** brand pages, and keyword pages built from The Body Shop's non-branded keywords.
- **Merchandising:** routines and combos in The Body Shop style, and an advent calendar concept.
- The source files were in the old session's `site` folder: index.html, products.json and product images.

---

## 6. Advice given to the client

**Can we run ads for one product (Vilvah Milk Drop serum) before the whole SEO fix?**
Yes. Meta Ads don't depend on SEO. What's needed first, in about 5–7 days:
- **That product page:** copy, reviews, UK delivery and returns info, mobile speed, a price check against Amazon UK, and a bundle or upsell.
- **Tracking:** Pixel events (ViewContent, AddToCart, Purchase), Conversions API, and domain verification.
- **Store basics:** policy pages linked in the footer, demo products removed.
- **UK ad rules (ASA):** no medical claims.

Suggested pilot: about £15–25 a day for 14 days, UK, women 22–45, UGC-style reels.

**Will one product lower the AOV?**
Advertise one product, but let the page lift the basket:
- Pack options (Single / Duo / Routine).
- "Complete the routine" items, at most 3.
- A free-delivery threshold.
- A cart add-on and an offer after payment.

Keep Add to bag as the main button, and judge results by conversion rate × AOV.

**Shopify**
- Shopify connector: https://setup.shopify.com/mcp. It manages products, collections, SEO fields and orders. It can't be relied on to deploy themes.
- The prototype **can** become a Shopify theme. Rebuild it on Dawn in Liquid, push it unpublished with the Shopify CLI (`shopify theme push --unpublished`) or as a .zip upload, and the client publishes after approval.
- Needs Shopify staff or collaborator access from the client.

---

## 7. Quote (5-day delivery, GBP, suggested prices)

**A. Templates: £1,370**

| # | Template | Price |
|---|---|---|
| 1 | Global layout (header, mega menu, footer) | £150 |
| 2 | Homepage | £250 |
| 3 | Collection / category | £120 |
| 4 | Brand page | £100 |
| 5 | Product page (standard) | £180 |
| 6 | Product page (bundle / combo) | £120 |
| 7 | Cart drawer + cart page | £80 |
| 8 | Search results | £50 |
| 9 | Blog listing + article | £80 |
| 10 | About / brand story | £60 |
| 11 | Contact + FAQ | £60 |
| 12 | Policy pages (4) | £40 |
| 13 | Seasonal / advent calendar | £80 |

The ad landing page and the 404 page were removed at the user's request.

**B. Per product: £939.50**
- Standard SEO set: £1.50 × 493 = £739.50.
- Premium description rewrite: £4 × 50 hero products = £200.
- Collection copy: £8 per collection, count to be confirmed after clean-up.

**C. Site-wide: £350**
- Technical SEO £150, speed and tracking £100, deploy and QA £100.

**Total: £2,659.50**, excluding collection copy, ad spend and paid apps.

**5-day plan**

| Day | Work |
|---|---|
| 1 | Access, Dawn setup, global layout + homepage, catalogue clean-up, sitemaps submitted |
| 2 | Collection, brand, product and bundle templates; product SEO starts |
| 3 | Remaining templates; product SEO continues |
| 4 | All products done, collection copy, schema, redirects, speed, Pixel / Conversions API |
| 5 | Testing, client review, fixes, publish, request reindexing |

**Conditions**
- Store access on day 1, client feedback within 24 hours, one revision round included.
- SEO *work* is finished in 5 days; rankings take 4–12 weeks to move.

---

## 8. Product data sheet (sent to the client)

**Columns:** S.No, Brand, Category (dropdown), Product Name, SKU, MRP (£), Selling Price (£), Discount %, H1, Meta Title, Title Length, Meta Description, Description Length.

**Built-in checks**
- Duplicate SKUs turn red.
- A warning appears if the selling price is above the MRP.
- Title length turns red above 60 characters, description length above 160.

**Notes**
- Row 3 is an example row.
- The client can leave the SEO columns blank and we'll write them.
- For now the product list was scraped from the live site; the client's own sheet will replace it.

---

## 9. Next steps

1. Get the filled product sheet and Shopify collaborator access from the client.
2. Send the client the quote. The draft reply also answers "redesign or not?": we're now offering a full theme from the prototype, priced per template.
3. Build the Dawn-based Shopify theme from the prototype, then do the 5-day delivery.
4. Optionally add the day-7 single-product Meta pilot and a product-page AOV plan to the deck.
5. Ask the client for fresh Search Console screenshots after the sitemaps are submitted, and update slides 2, 14 and 15.
