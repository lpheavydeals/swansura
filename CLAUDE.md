# Swansura — Project Memory

Read this first in every session. Full history: `docs/HANDOFF.md` (handoff from the original account, 15 Oct 2026).

## Project
- **Agency:** Lokesh · www.thebilliongame.com (India-based).
- **Client:** Swansura — "Swansura - The Body Studio". UK online retailer of Indian natural skincare (Vilvah, Deyga, …) and Arabian fragrance brands. Official seller, not exclusive partner.
  - Store: swansura.com (Shopify) · Instagram @swansura_thebodystudio · also on Amazon UK.
- **Competitors:** LOOKFANTASTIC, Cult Beauty (leaders); Beauty Bay, Space NK (contemporaries).
- **Design benchmarks:** Forest Essentials, The Body Shop, Mamaearth. SEO-structure reference: indicrest.co.uk.

## Phases
1. **Done:** Growth Audit (31-slide deck) + UK competitor / Meta Ads research.
2. **Now: Shopify website** — turn the prototype into a Dawn-based Liquid theme, full SEO, 5-day delivery.
3. **Later: Ads** — Meta Ads (single-product pilot on Vilvah Milk Drop serum, then full plan from ~day 31).

## Repo layout
- Prototype preview link (this account, private — share via Share menu): https://claude.ai/artifact/9Hixbi7Kiu1nBZYJaFoiGH . Republish `prototype/index.html` from this repo to update it (images go up in batches of ≤255 files).
- `prototype/` — **the final website prototype** (from the original account's export): `index.html` (single-file HTML/JS), `products.json` (473 products scraped from swansura.com: id, title, brand, cat, price, compare, available, tags, desc, …) and `img/` (473 product images). Serve the folder over HTTP to view it (`python3 -m http.server` inside `prototype/`); `fetch('products.json')` fails from `file://`. `build-data.ps1` / `build-all.ps1` are the original Windows scrape/build scripts.
- Prototype status (17 Oct 2026): all 12 items from the benchmark top-12 are built in (reviews slots with no invented reviews, product FAQs + hero ingredients, Single/Duo/Routine packs at 10%, concern/skin-type/ingredient filters, pay-in-3 + dispatch line, wishlist + header icons, Shop by price, first-order pop-up, Studio pick badges, Deyga + Vilvah 'Behind the brand', recently viewed, Buy it now). Client to confirm: pack discounts, dispatch time, pay-later providers, 10% welcome offer.
- `seo/Swansura_Keyword_Research.xlsx` — 18 Oct 2026 keyword research for all 546 products in the client's data sheet (`docs/data/Swansura_Product_Data_Sheet_2026-10-18.xlsm`: 387 fragrance + 159 Vilvah/Deyga). Per-product core / UK / buy online / price / concentration keywords, Google UK autocomplete phrases, draft H1 + meta title + meta description, brand-cleanup notes; 3,751 keywords in 38 Semrush batches (Tier 1 = batches 1–9). Volumes fill in automatically once Semrush Keyword Overview (UK) exports are pasted into the 'Semrush Data' tab. Rebuild with `tools/keywords/`.
- Semrush Tier 1 merged (18 Oct 2026; exports in `seo/semrush_exports/`, merge with `tools/keywords/merge_semrush.py` + `add_insights.py`): 446/900 keywords have UK volume; 265 products' primary keyword has volume (247 fragrance, only 18 Vilvah/Deyga at 10–30/mo). Brand: vilvah 480, vilvah milk drops 390, deyga 140. Big non-branded skincare terms: moisturiser for dry skin 2,900, hair mask for dry hair 2,400, hair oil for dry hair 1,900, face wash for dry/oily skin 1,600, shampoo for dandruff 1,600 → build concern collection pages. 'Insights' tab has Top 50 hero products (all fragrance by volume). Semrush account currency is USD.
- 18 Oct 2026 (later): research workbook has a 'VD Content' tab (159 Vilvah/Deyga products: concern target keyword + volume, H1, meta title/description within limits, intro paragraph from real product facts, FAQ ideas; 73 flagged where source copy has medical-style claims, kept out of the copy). Prototype has 15 high-volume 'Skin & hair needs' keyword pages (k-moisturiser-for-dry-skin etc.) with intros + FAQs, linked from Skincare/Haircare 'Most searched' menu columns. Focused Tier 2 = 242 keywords / 3 batches in `seo/Semrush_Tier2_Prompts.xlsx` (exports to be named Tier2_Batch_N_UK_keywords.xlsx; merge with all exports, see tools/keywords/README.md).
- Tier 2 merged (18 Oct 2026): 1,142 keywords checked, 638 with volume. Primary keyword stays the product name for every product (variants are secondary, e.g. 'dior sauvage eau de parfum' 4,400). Big easy generic terms: aloe vera gel 18.1K (KD16), body scrub 12.1K (KD18), body butter 6.6K (KD12), hair growth oil 5.4K, lip scrub 5.4K, shampoo for hair loss 5.4K, night cream 3.6K, under eye cream 2.9K, amla hair oil 2.9K (KD9). VD Content targets are now data-driven (highest-volume of concern keyword vs product-type term in the name; kits keep concern targets; 31 distinct targets). Prototype pages added: lip-scrub, shampoo-for-hair-loss, night-cream (hidden: 1 product), hair-oil-for-hair-loss renamed hair-growth-oil.
- `tools/build_product_sheet.py` — builds the client product data sheet (.xlsx).
- `reference/audit-deck/` — slide HTML of the Growth Audit deck (reference only; the live deck artifact is canonical, and some later footer edits are missing here).
- `docs/HANDOFF.md` — full handoff: audit numbers, quote, advice given, next steps.
- `docs/Swansura_Growth_Audit.pdf` — final 31-slide Growth Audit deck (PDF export; canonical over `reference/audit-deck/`).
- `docs/Competitor_UX_Benchmark.md` — 17 Oct 2026 UX benchmark of LOOKFANTASTIC, Purplle, Clinikally, The Skin Store vs our prototype (gaps by section, priorities, top-12 list); screenshot sheets in `docs/benchmark/`.
- `docs/Competitors_Meta_Ads.docx` — "Swansura UK Competitor & Meta Ads Research" (4 Oct 2026). Main input for the Ads phase.

## Design system (from deck + prototype)
- Font: **Plus Jakarta Sans** everywhere.
- Colours: paper `#F7F4EE`, mount `#F2EDE4`, card `#FFFDF9`, ink `#1F1A17`, line `#E3DACD`, emerald `#1F3B34`, oud `#3A2421`, brass `#9A7536`, on-dark `#F4EEE4`, sale `#8A2F2A`.
- Prototype features to carry into the theme: shop with sticky filter panel, coloured trust badges, fixed Add-to-bag bar, styled scrollbar, brand pages, keyword pages (The Body Shop non-branded keywords), routines & combos, advent-calendar concept.

## Shopify build — agreed approach
- Rebuild on **Dawn** in Liquid; push unpublished (`shopify theme push --unpublished`) or upload .zip; client publishes after approval.
- Shopify MCP connector (https://setup.shopify.com/mcp) for products, collections, SEO fields, orders — not for theme deploys.
- Needs Shopify staff/collaborator access from the client.
- Templates quoted (13, £1,370): global layout, homepage, collection, brand page, product (standard), product (bundle/combo), cart drawer + page, search, blog listing + article, about, contact + FAQ, policy pages (4), seasonal/advent. (Ad landing page and 404 removed at user's request.)
- Per product: SEO set £1.50 × 493; premium rewrite £4 × 50 hero products; collection copy £8 each. Site-wide £350. **Total £2,659.50** (excl. collection copy, ad spend, apps).
- 5-day plan: D1 access, Dawn, layout + homepage, catalogue clean-up, sitemaps · D2 collection/brand/product/bundle templates, product SEO · D3 remaining templates · D4 all products, collection copy, schema, redirects, speed, Pixel/CAPI · D5 QA, client review, publish, reindex.

## Must-fix issues found in audit (9 Oct 2026)
- 493 products (467 in stock); 4 Shopify demo products + "Default example products" collection still live.
- 170 products filed under "Generic"/"Swansura - The Body Studio" instead of the real brand.
- 15 empty/duplicate collections (fr, fr-1, frag, frag-1, hem, hem-1 …). Vilvah collection URL is `/collections/milk-drop-brightening-serum`, meta "sample vilvah".
- Product + collection sitemaps **not submitted** in Search Console (main indexing problem).
- Empty homepage H1; collection H1 "Collection: X"; duplicated title suffix "| Swansura – Swansura - The Body Studio"; no collection intros/FAQs; cart/search/demo pages indexable; no rating schema; 19/85 homepage images missing alt; 1 blog post; no brand pages.
- PageSpeed: desktop 97, mobile 71.

## Ads (future phase) — what was advised
- Meta Ads don't depend on SEO. Pilot one product after ~5–7 days of prep: product page (copy, reviews, UK delivery/returns, mobile speed, price vs Amazon UK, bundle/upsell), Pixel events (ViewContent, AddToCart, Purchase) + Conversions API + domain verification, policy pages in footer, demo products removed, ASA-compliant (no medical claims).
- Pilot: ~£15–25/day × 14 days, UK, women 22–45, UGC-style reels.
- Protect AOV: Single/Duo/Routine pack options, ≤3 "complete the routine" items, free-delivery threshold, cart add-on + post-purchase offer. Judge by conversion rate × AOV.
- Baseline: 0 Meta ads ever run (Pixel installed); Instagram 34 followers.

### From the research doc (`docs/Competitors_Meta_Ads.docx`)
- **Positioning:** "the UK home of farm-to-skin Indian natural care". Lead with skincare; use fragrance as gifting add-on / basket builder (fragrance is a crowded price war). Treat skincare and fragrance as two product lines with separate audiences/creatives.
- **Trust lines:** "Official UK partner of Deyga & Vilvah" (no other UK seller found); "Ships from the UK in 1–2 days" (rivals ship from India).
- **Competitors:** Indian importers (Indicrest UK, The Desi Food, Distacart, Ubuy); Indian brands direct (Forest Essentials UK, Kama Ayurveda, Minimalist at Superdrug, Kay Beauty via Space NK); fragrance e-tailers (Friday Charm, Scents Angel, Aromique, etc.); model to copy: Skin Cupid.
- **Current offer:** free UK shipping over £50, Buy 1 Get 1, code SPRING10; prices £9.99–~£85.
- **Unit economics:** UK beauty cost per purchase £22–45 vs items £10–30 → need AOV £35–50 via bundles ("Glow Ritual", "Hair Oil Ritual", "Skincare + Mini Perfume Gift Set"). Break-even CPA = AOV × margin.
- **Benchmarks:** CPM £8–12.50, CPC £0.50–0.90, CTR 0.7–1.4% feed / 1.2–2.1% Reels, ROAS 2.5–4.8x.
- **Structure:** Advantage+ prospecting 60–70% (UK women 22–55, broad); testing 15–20% (seeds: clean beauty, Ayurveda curious, South Asian diaspora, fragrance gifters); retargeting 15–20%.
- **Creative:** UGC testimonials, ingredient explainers, farm-to-skin story, before/after, bundle statics, partnership ads with 5–10 UK micro-creators; 2–3 new creatives a week. Post 9–12 Reels before spending.
- **Budget:** £20–30/day weeks 1–4; scale +20% every 3–4 days under break-even. Seasonal: Diwali 8 Nov, Black Friday 27 Nov, Christmas to ~18 Dec, Valentine's, Mothering Sunday 7 Mar 2027.
- **90-day KPIs:** AOV £35–50, ROAS 2.0x+ test / 2.5x+ scale, CTR 1%+ feed / 1.5%+ Reels, 60-day repeat 20%+, 1,000+ IG followers, 50+ reviews.
- Send ad traffic to swansura.com, not Amazon (Meta can't see Amazon sales).

## Open items
- **Shopify connector connected (15 Oct 2026)** to "Swansura - The Body Studio" (www.swansura.com, Basic plan, GBP). Admin counts that day: 706 products (549 active, 157 draft), vendor "Generic" 121, vendor "Swansura - The Body Studio" 82, 138 collections. These differ from the 9 Oct audit (493 live, 88 Generic) — the audit counted storefront products only; recheck before quoting.
- **Theme deploy route (confirmed 15 Oct):** no network change or browser needed. Via the Shopify connector: `themeCreate`/`themeDuplicate` → new unpublished theme, then `themeFilesUpsert` (allowed on unpublished themes only). Publishing is blocked by the connector — a person clicks Publish in admin after approval.
- Store themes (15 Oct): live MAIN = "SWANSURA Website"; "Working" (unpublished) was being edited by someone else on 15 Oct — don't touch it, confirm with client who owns it; plus 6 old Dawn copies and a "Be Yours" demo.
- **On hold (user, 15 Oct):** do not build or deploy the Shopify theme yet — the prototype is to be optimised first.
- Waiting on: client's filled product sheet + Shopify collaborator access.
- Send quote to client.
- Deck footer sources: unresolved whether to add "Screaming Frog, Semrush, Ahrefs & Claude".
- Optional: add day-7 Meta pilot + product-page AOV plan to deck; refresh GSC slides (2, 14, 15) after sitemaps are submitted.
- Old artifacts (deck, research doc, prototype) are owned by abracaindia@gmail.com and not shared with this account; their exported copies are now in this repo (`docs/`, `prototype/`), which is the source of truth from here on.
