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
- `prototype/` — **the final website prototype** (from the original account's export): `index.html` (single-file HTML/JS), `products.json` (473 products scraped from swansura.com: id, title, brand, cat, price, compare, available, tags, desc, …) and `img/` (473 product images). Serve the folder over HTTP to view it (`python3 -m http.server` inside `prototype/`); `fetch('products.json')` fails from `file://`. `build-data.ps1` / `build-all.ps1` are the original Windows scrape/build scripts.
- `tools/build_product_sheet.py` — builds the client product data sheet (.xlsx).
- `reference/audit-deck/` — slide HTML of the Growth Audit deck (reference only; the live deck artifact is canonical, and some later footer edits are missing here).
- `docs/HANDOFF.md` — full handoff: audit numbers, quote, advice given, next steps.
- `docs/Swansura_Growth_Audit.pdf` — final 31-slide Growth Audit deck (PDF export; canonical over `reference/audit-deck/`).
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
- Waiting on: client's filled product sheet + Shopify collaborator access.
- Send quote to client.
- Deck footer sources: unresolved whether to add "Screaming Frog, Semrush, Ahrefs & Claude".
- Optional: add day-7 Meta pilot + product-page AOV plan to deck; refresh GSC slides (2, 14, 15) after sitemaps are submitted.
- Old artifacts (deck, research doc, prototype) are owned by abracaindia@gmail.com and not shared with this account; their exported copies are now in this repo (`docs/`, `prototype/`), which is the source of truth from here on.
