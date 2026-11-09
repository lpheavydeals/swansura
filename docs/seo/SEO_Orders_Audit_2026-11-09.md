# Swansura SEO + orders audit, 9 Nov 2026

## 1. New products (added 8–9 Nov)
- 129 new fragrance products are ACTIVE (created by the other 8–9 Nov session; photos added to 111): Paco Rabanne 23, Salvatore Ferragamo 21, Mugler 13, Lalique 12, Thomas Kosmala 12, Narciso Rodriguez 9, Issey Miyake 8, Roberto Cavalli 7, Versace 7, Ralph Lauren 4, and 10 more from smaller houses.
- SEO on all 129 is complete: SEO title ≤60, meta description ≤160, custom.h1, custom.sw / custom.pdp, 5–12 collections each. Their brand pages (/collections/versace, paco-rabanne, mugler …) return 200.
- Live crawl of 22 of them: one H1, no Liquid errors, valid JSON-LD, all images have alt.
- Problems:
  - **All 129 have 0 stock**, so they show as sold out and Google Shopping will not list them.
  - **18 have no photos.**
  - Descriptions are short, 45–90 words.

## 2. Alt text
- Earlier on 9 Nov another session fixed the main cause: the theme printed alt="" on gallery thumbnails, Frequently bought together, Complete the ritual and Beauty Advisor cards (fixed in theme 200592195971, now live), and 481 stored image alts were empty (filled). It also added photos to 111 of the 129 new products.
- Re-check now:
- Product images: **3,701 images on 893 active products, 0 without alt.**
- Live pages crawled (homepage, 12 key collections, 8 new brand pages, Journal, Routines, Contact, 22 new products): **0 `<img>` without alt.**
- What the client is likely seeing:
  - About 45 **collection cover images** have no alt (vilvah, deyga, fragrance, jo-milano, hemel, fumeri, giftsets …). Shopify admin and SEO apps flag these.
  - Old **Content → Files** images from Sep–Oct 2025 (the images replaced in October) have empty alt. They are not used on the site.
- Fix: set collection image alt to '<Collection title> at Swansura' (≈45 writes; waiting for OK).

## 3. H1 / meta titles / meta descriptions
- All 893 active products have an SEO title (≤60), a meta description (70–160) and custom.h1.
- Duplicates are only the 3 known duplicate listings (Game of Spades Full House, Hermès Cythère, Caput Mundi).
- Collections, pages and articles crawled: one H1, titles ≤60, descriptions ≤160, canonical = URL, valid JSON-LD.
- **On-page SEO is not the bottleneck.**

## 4. Orders and traffic (Shopify Analytics + Orders)
- **Orders:** 15 orders since 10 Aug (#SWAN1004–1018, all from 2 Oct); 13 paid, 2 refunded. That is about 2–3 orders a week from all channels, not 5 organic a week.
- **Where attributed orders came from:**
  - Google Shopping free listings (`utm_medium=product_sync`, `sag_organic`): 4 orders (Chopard Oud Malaki ×2, Philipp Plein deo, Bvlgari set refunded).
  - Google organic: 1 (to the homepage).
  - ChatGPT: 1 (Al Haramain Amber Oud Gold, 7 Nov).
  - Unattributed: 9. Customers who decline cookies show no source.
- **Sessions, last 30 days:** 1,182. About 690 are US desktop "direct" hits on the homepage, i.e. bots.
  - Real UK sessions: 125 (89 mobile). Of these, 14 added to bag and 6 bought, so **UK conversion is about 5%, which is healthy**.
  - Search sessions: 111 in 30 days (Google 174 in 90 days). That is about 4 a day.
- **The gap is traffic.** Two orders a day at 3–5% conversion needs about 1,500–2,000 real UK sessions a month, roughly 12× today.
  - The site is new (redesigned 26 Oct) and Google has not been told about it: `/sitemap.xml` has never been submitted in Search Console.
  - The domain has almost no backlinks.
  - Most best-sellers / heroes are sold out (e.g. Lattafa 0/4 in stock, Arabian 32/104 in stock, the 129 new products at 0 stock).
- Note: 67 sessions in 30 days landed on /password, so the store was password-locked for part of the period.

## 5. Competitors and season
Full research with sources: `docs/seo/competitor_research_2026-11-09.md`. Rankings are approximate, because Google UK blocked automated searches; confirm positions in Semrush UK.

- **Who ranks:**
  - Gift sets: LOOKFANTASTIC, Superdry/Superdrug, Next, Notino, The Perfume Shop.
  - Arabian / Lattafa: small specialists (soghaat.co.uk, oudhshop.co.uk, emiratesoud.co.uk). These are winnable.
  - Oud: Next, fragrancehub, LOOKFANTASTIC, p-eleven.
  - "Indian skincare UK": only articles rank, so it is an opening.
- **Season:**
  - Nearly half of UK fragrance sales fall in Oct–Dec.
  - The peak buying week is 14–20 Dec, and Black Friday is 27 Nov.
  - What sells: gift sets for her/him, minis and travel sets, under £25/£50 gifts, oud/Arabian heroes, aftershave sets (Dior Sauvage was the 2025 UK top seller).
  - Skincare gift set (3,600/mo, KD 22), hair care gift set (880), goat milk soap (880, KD 15).
- **Who searches:**
  - Gift buyers who don't know the scent (28% of UK perfume users mainly give or receive it as a gift; they buy late, by price band).
  - Young TikTok-driven Arabian-perfume buyers (£20–45).
  - Oud enthusiasts / Muslim and Middle-Eastern UK communities.
  - South Asian diaspora and Ayurveda-curious shoppers for Indian skincare.
  - Natural-gift buyers.

## 6. Plan to get to 2 orders a day (priority order)
1. **Search Console:** the client owns it (Prompt 1 in `docs/ads/Browser_Prompts_Tracking_Setup_2026-11-09.md`). Confirm /sitemap.xml is submitted and request indexing of the top 30 pages. This is the biggest single blocker.
2. **Google Merchant Center / free listings.** This is already the best-converting channel.
   - Fix diagnostics and keep heroes in stock.
   - Add GTINs (only ~3% + 107 have them).
   - Paid Standard Shopping for Black Friday (the November ads plan, G1 £176).
3. **Stock:** restock the sellers (Al Haramain Amber Oud editions, Chopard Oud Malaki, gift sets). Put stock on the 129 new products or hide them until stocked, because sold-out pages don't convert or list.
4. **Season pages before 20 Nov:**
   - Create /collections/black-friday, gifts-under-50, skincare-gift-sets and goat-milk-soap (all 404 today).
   - Give perfume-gift-sets, gifts-for-her/him, stocking-fillers and christmas-gifts titles and descriptions with 'UK', 'Christmas 2026', 'from £X' and 'free delivery over £40'.
   - Add last-order dates once the client confirms them.
5. **Content:**
   - 'Best perfume gift sets UK 2026' guide (by recipient and budget).
   - 'Stocking fillers for her under £25' guide.
   - 'Indian skincare UK' guide.
   - Goat milk soap guide.
6. **Trust:** Judge.me review requests on every order. Competitors all show stars.
7. **Links:** the backlink plan (`Swansura_Backlink_Plan_2026-10-28.xlsx`): brand-partner stockist links (Vilvah, Deyga) and gift-guide PR pitches this month.
8. **Housekeeping:** collection image alt text, and retire the 3 duplicate listings.
