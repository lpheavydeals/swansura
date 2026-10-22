# Swansura vs LOOKFANTASTIC — website comparison (22 Oct 2026)

**Method:** I loaded these LOOKFANTASTIC pages live on desktop (1440 px) and mobile (390 px):

- the homepage
- Skincare (`/c/health-beauty/face/`)
- Fragrance
- The Ordinary brand page
- the "vitamin c serum" search, which lands on their Vitamin C Serums page
- one product page: The Ordinary Lacto-PDRN Eye Cream

I compared them with our prototype (preview v36, 722 pages), which the Shopify theme is being built from. Screenshots are in `docs/benchmark/lf_2026-10-22_*.jpg`. The first benchmark, from 17 Oct, is `docs/Competitor_UX_Benchmark.md`.

LOOKFANTASTIC is a 660-brand marketplace. We are a specialist store. The aim is to beat them where a specialist can and to copy what earns trust and sales.

## Scorecard

| Area | LOOKFANTASTIC | Swansura (prototype → theme) | Who wins |
|---|---|---|---|
| Homepage H1 | **None** | "Rituals for the skin, signatures for the senses." | **Us** |
| FAQs on category, brand and search pages | Only on some brand pages (The Ordinary); none on Skincare, Fragrance or Vitamin C Serums | FAQs and FAQ structured data on all 97 listing and brand pages, Routines, Brands A–Z and every product | **Us** |
| SEO copy on listing pages | One generic ~300-word block on Skincare; none on the Vitamin C Serums keyword page | 150–380 words on every brand, category, concern, scent, range, price and keyword page (158 pages), each targeting a Semrush keyword, with internal links | **Us** |
| Image alt text | 43–55 images per page have no alt text (about 40%) | 0 missing; every product image has descriptive alt text | **Us** |
| Mobile first visit | A cookie banner covers the whole product page | Small pop-up; nothing covers the product | **Us** |
| Distraction on product pages | Sponsored ads for unrelated products (a £480 Dyson on an £8.70 eye cream) | No ads; only related products, routines and similar items | **Us** |
| Specialist range | Doesn't stock Deyga or Vilvah | Official UK partner of Deyga and Vilvah; Indian natural care, Arabian and niche oud | **Us** |
| Ways to browse | By category, brand and concern | Also by scent family, hero ingredient, range, price band, skin type and 58 search-led pages | **Us** |
| Routines and bundles | "Frequently bought together: add both" | 16 step-by-step routines at 15% off, plus Single, Duo and Routine packs on every product | **Us** (theirs is quicker to use) |
| HTML sitemap in the footer | Yes | Yes (714 links) | Tie |
| Brand directory, breadcrumbs, wishlist, pay-in-3 line | Yes | Yes | Tie |
| **Reviews and star ratings** | 4.8★ (187) on the product page, star ratings in Google results, "Write a review", "Ask a question" | Review slots only, no real reviews yet | **Them** |
| **Structured data** | Product (price, stock, rating), BreadcrumbList, CollectionPage, Organization, WebSite | FAQPage only in the prototype | **Them** (the theme fixes this) |
| **Title and description per page** | Every page has its own, e.g. "Shop Skincare at LOOKFANTASTIC… Free delivery available." | The prototype uses one title for every page; the 546 product titles and descriptions are ready in the 'Final SEO' tab | **Them** until the theme launches |
| **Speed** | Server-rendered; mobile pages are 0.5–1.4 MB and load in 0.6–2.2 s | The prototype draws pages with JavaScript (mobile LCP about 4 s) | **Them** (the Liquid theme fixes this) |
| **Delivery offer** | Free over **£25**; "Order by 1am for next day" with a live countdown; Premier Delivery at £5.95 a year | Free over £50 is promised but **not set up in Shopify**; "dispatched in 1–2 working days" | **Them** |
| **Offers and loyalty** | Code strip ("25% off · TREAT"), points shown on the product page, Student, Key Worker, Disability and 16–26 discounts, Refer a Friend, app | 10% first-order pop-up only | **Them** |
| **Help while shopping** | "Ask LIA" AI assistant and a chat bubble on every page | Contact page | **Them** |
| **Free gift with purchase** | A hub of brand gifts ("spend £30, get a 10 ml cream") | None | **Them** |
| **Ingredients on product pages** | "Ingredient benefits" plus the full ingredients list | Hero ingredients and benefits; the full list says "printed on the pack" | **Them** |
| Category page visuals | Large circular sub-category images ("Cleansers, Moisturisers, Serums, SPF") and brand banners | Compact category row and concern cards with product images | Similar |

## What we did better
1. **Search basics they skip.** They have no homepage H1 and about 40% of their images have no alt text. We have both, plus an HTML sitemap and clean breadcrumbs.
2. **Content depth on the pages that rank.** They have no copy and no FAQ on a page like "Vitamin C Serums". We have keyword-led copy, FAQs and FAQ structured data on 158 non-product pages. For smaller searches, such as "body butter for dry skin", "oud perfume" or "jimmy choo perfume", this is how a small store outranks a big one.
3. **A specialist story they can't match.** Official UK partner of Deyga and Vilvah, Indian natural care, oud and Arabian scents, scent-family browsing, routines and ingredient-led pages.
4. **A cleaner, calmer product page.** No sponsored ads, no full-screen cookie wall on mobile, and pack options and routines that raise the basket value.
5. **Accessibility.** The accessibility scan finds 0 problems, tap targets are at least 24 px and no text is under 11 px on phones.

## What we missed (to add, in priority order)
1. **Real reviews and star ratings.** Install Judge.me or Okendo, import any existing reviews and email buyers after delivery. Stars in Google results and on the product page are LOOKFANTASTIC's biggest advantage. *Theme, day 4.*
2. **Structured data.** Product (price, availability and, once reviews exist, aggregateRating), BreadcrumbList, CollectionPage, Organization and WebSite. Dawn provides Product; we add the rest. *Theme.*
3. **Titles and meta descriptions per page.** Products come from the 'Final SEO' tab. Collections, brands and keyword pages get a "Shop X at Swansura… Free UK delivery over £50" pattern. *Theme.*
4. **The delivery offer.** First set up the free-over-£50 rate, which the site promises but Shopify doesn't apply. Then consider a lower threshold: LOOKFANTASTIC is at £25, while our basket maths favoured £50. Add a cut-off line with a countdown, e.g. "Order by 2pm for same-day dispatch". *Client decision, then theme.*
5. **Speed.** Server-rendered Liquid pages, sized images and the hero and product images preloaded. Target LCP under 2.5 s on 4G. *Theme.*
6. **An offers strip and discount schemes.** One quiet line for the current code. Later: Student Beans, NHS / key worker discounts and refer-a-friend (cheap reach in the UK). *Theme plus client.*
7. **"Frequently bought together: add both" on product pages.** A one-tap version of our routines.
8. **Full ingredients list** on each skincare product (the client supplies these, or we take them from Deyga and Vilvah).
9. **Chat or WhatsApp button**; an AI shopping assistant later.
10. **Free gift with purchase** (e.g. "spend £40, get a Deyga mini"), which supports the free-delivery threshold.
11. Later: loyalty points, an app, a beauty box or subscription, and a Christmas gift shop. The advent calendar concept already covers part of the gift shop.

## Not worth copying
- Sponsored ads for other products on product pages.
- A cookie banner that covers the whole screen on mobile.
- A homepage without an H1 heading.
