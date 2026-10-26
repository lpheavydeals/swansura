# Swansura new theme – Day 5 QA report (26 Oct 2026)

Theme checked: **"Swansura – New Theme (Day 2 build)"** (ID 200301314435, unpublished draft).
Preview: https://www.swansura.com/?preview_theme_id=200301314435

## What was checked

| Check | Scope | Result |
|---|---|---|
| Page crawl | 701 pages: home, all 545 products, all 139 collections, cart, search, blog, contact, policies, About/FAQ/Advent/Sitemap templates, 404 | 699 × 200 OK; 2 × 404 (a test URL, and `/policies/shipping-policy`, which has no text in Shopify yet) |
| Liquid errors | 701 pages | 0 |
| One H1 per page | 699 pages | 699 / 699 (cart and one product description had two; fixed) |
| Page title | 699 pages | All ≤ 70 characters with the "– Swansura" suffix; no duplicated "Swansura - The Body Studio" |
| Meta description | 699 pages | All present and ≤ 160 characters (blog, contact, policies, cart and 'all products' had none; homepage had 167 characters; fixed) |
| Structured data (JSON-LD) | 699 pages | All valid JSON (Product, CollectionPage, ItemList, BreadcrumbList, FAQPage, Organization) |
| Search engines | cart, search | `noindex, follow` added (robots.txt already blocks them) |
| Internal links | 1,463 unique links found on those pages | 1 broken link (`/pages/faq`, the FAQ page isn't created yet). It now points to the refund policy until the page exists. The 409 responses on `/cart/<id>:1` are Shopify's own Shop Pay links for sold-out items. |
| Images | all pages | 0 images without alt text, 0 broken images |
| Phone 390 px + desktop 1366 px | 18 key pages | 0 sideways scroll, 0 JavaScript errors from the theme, 0 text under 11 px |
| Speed (load, no throttling) | 18 pages × 2 | Largest paint: phone median 0.9 s, worst 1.2 s; desktop median 0.9 s, worst 1.1 s. Layout shift (CLS): worst 0.089 (cart, phone), all others < 0.04 (target < 0.1). |
| Accessibility (axe, WCAG 2.1 AA) | 18 pages × 2 | Quantity box label fixed. Remaining flags: (1) Shopify's preview-bar iframe (only in preview), (2) product cards that are still fading in (Dawn scroll animation) when the test runs. Real colours pass. |
| Tap targets ≥ 24 px (phone) | 18 pages | Announcement bar, 'Shop all' / 'View all' links and footer links fixed. What's left: hidden variant inputs, Dawn's sort dropdown (its visible box is larger), Shopify's "More payment options" link, product-card titles (the whole card is the tap area). |
| Shopping journey (phone + desktop) | menu, search, product, add to bag, bag drawer, bag page, checkout, sort | All pass. Add to bag opens the drawer with the £40/£70 progress bar. The bag total shows £30.99 (no "GBP") and carries through to Shopify checkout. |

## Fixed during QA (all on the draft theme, plus 3 store fixes)

- `layout/theme.liquid`: meta description fallback for pages without one, homepage description ≤ 160, long titles skip the "– Swansura" suffix, `noindex` on cart/search.
- `sections/main-cart-items.liquid`: "Your cart is empty" is no longer a second H1.
- `sections/main-product.liquid`: quantity box has an accessible label.
- `sections/sw-contact.liquid`, `sections/sw-about.liquid`: links to pages that don't exist yet (FAQ) fall back to the shipping/refund policy.
- `sections/sw-recent.liquid` + `assets/swansura.js`: 'Recently viewed' reserves its space before loading (cart CLS 0.21 → 0.09).
- `assets/swansura.css`: 24 px tap areas (announcement, links, footer), no text under 11 px (tax note, hero brand line, share and field labels).
- Store: the Hugo Boss Alive gift set lost its meta description when its title was corrected (Shopify replaces both SEO fields together); restored. The anatomē Sleep Pillow Spray description had its own H1; changed to H2. The three Antonio Banderas descriptions were brought in line with the Day 4 list.

## Not fixable from the theme (client / admin)

1. **Shipping policy is empty** → `/policies/shipping-policy` is a 404. Draft text: `docs/policies/Shipping_Policy_DRAFT.md` (Settings → Policies).
2. **Free delivery over £40 and £5 off over £70** are promised on the site, but checkout has no such rate or discount yet (Settings → Shipping and delivery; Discounts → automatic discount).
3. **Two pay-later lines on product pages**: Shopify shows "Pay in 3 … over £50 with Shop Pay" (Shop Pay Installments is switched on), and our line says PayPal Pay in 3. Keep one: either turn off Shop Pay Installments, or ask us to remove the PayPal line.
4. **Main menu** is still the old one (Home, Shop, Fragrance …, Blog). It is shared with the live theme, so changing it needs the client's OK.
5. **Pages to create** (then pick the template): About (`page.about`), FAQ (`page.faq`), Advent (`page.advent`), Sitemap (`page.sitemap`); then add them to the footer menu.
6. **Clean-up**: demo products, empty or duplicate collections (fr, frag, hem, ma, mar, tr, nin …, which are indexable with titles like "frag – Swansura"), and duplicate listings (anatomē Expression, Hermès Cythère, Jo Milano Full House, Caput Mundi).
7. **Category collections are incomplete** (Skincare 32, Haircare 10, Bath & Body 20 products). Make them smart collections by product type or tag.
8. **After publishing**: submit `https://www.swansura.com/sitemap.xml` in Google Search Console and request indexing of the homepage and top collections.

## Scripts

Crawler, browser checks and journeys: `tools/qa/` (`crawl.py`, `browse.js`, `journey.js`).
