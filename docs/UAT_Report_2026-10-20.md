# Swansura UAT report, 20 Oct 2026

Scope: the website prototype (`prototype/index.html`, the design and flow the Shopify theme is built from) and the live store www.swansura.com (the product photos, alt text and WebP updates made on 19 Oct, plus the shopper journey up to the checkout page). The new Shopify theme is not built yet, so it is not covered here.

Method: automated Chromium tests (Playwright) on desktop 1440×900 and mobile 390×844, plus 360, 768, 1024, 1280 and 1920 widths; axe-core 4.10 for WCAG 2.1 AA; throttled 4G for performance. Scripts and raw results are in the session scratchpad (`uat/`).

## Summary

| Area | Checks | Result |
|---|---|---|
| Every page renders (all 617 routes × 2 viewports) | JS errors, failed requests, broken images, missing alt, one H1, empty pages, mobile overflow, empty listings | Pass: 0 issues |
| User journeys (desktop + mobile) | 62 per viewport | Pass, except 2 accessibility items below |
| Accessibility (WCAG 2.1 AA, 31 page states) | axe-core | No critical issues; 2 serious, 5 moderate/minor |
| Responsive (7 widths × 17 pages) | Overflow, tap targets, text size | Fail at ≤365 px: header overflows |
| Performance (throttled 4G mobile, cable desktop) | FCP, LCP, CLS, weight | FCP good; CLS and mobile LCP poor on listing/PDP (prototype architecture) |
| Live store: 14 updated products | Status, image count, alt text, format, broken images | Pass: all match Shopify, all WebP, all alt text present |
| Live store: shopper journey | Home → search → add to cart → cart → checkout page | Pass (stopped at checkout; no order placed; cart cleared) |
| Live store: required pages | robots, sitemap, policies, contact, 404 | Fail: shipping policy page is missing (404) |

## User journeys tested (all pass on desktop and mobile)

- **Welcome offer pop-up:**
  - appears for new visitors
  - blocks an empty email
  - closes and stays closed after reload
- **Home:**
  - the hero, H1 and sections render
  - the announcement bar link scrolls to the newsletter
  - the bestseller tabs switch
- **Navigation:**
  - desktop mega menu on hover
  - every top-nav link routes correctly
  - mobile burger drawer opens, navigates and closes; Escape closes it
- **Search:**
  - shows results
  - a result opens the product
  - a no-results message appears
  - the misspelling "vilva" still finds products
- **Listings:**
  - the product count matches the grid
  - sort by price (both directions) and A–Z is correct
  - the filters work: a single filter narrows the results; two filters show chips and "Clear all"; removing a chip restores the list
  - "Load more" adds products
  - the mobile filter panel opens
  - "Shop by price" pages only contain products in range
- **Product page:**
  - title, price and gallery render
  - thumbnails switch the main image
  - quantity +/− works, with a minimum of 1
  - add to bag; the Duo pack adds 2; Buy it now opens the bag
  - out-of-stock items can't be added
  - "Read more" and "Write the first review" jump without errors
  - the mobile sticky add-to-bag bar appears
  - recently viewed works
- **Bag:**
  - the subtotal is correct
  - + and remove work
  - the free-delivery message updates
  - "Little extras" adds an item
  - checkout responds
  - an empty bag disables checkout
  - Close and Escape close the bag
  - the bag persists after reload
- **Wishlist:**
  - the heart adds the product
  - the count updates
  - it persists after reload
  - the product is listed on the wishlist page
- **Other:**
  - newsletter validation and thank-you message
  - Brands A–Z letter jump
  - brand pages
  - advent doors and "Notify me"
  - all info and policy pages
  - browser Back/Forward
  - new pages open at the top
  - a visible focus outline on Tab
  - all prices valid
  - the 404 page

## Issues found

| # | Severity | Where | Issue | Fix |
|---|---|---|---|---|
| 1 | High | Live store | `/policies/shipping-policy` returns 404. A shipping policy is needed for UK consumer law, Google Merchant Center and Meta ads. | Client adds it in Shopify admin → Settings → Policies (we can draft the text). |
| 2 | High | Prototype, phones ≤365 px (e.g. Galaxy S 360 px) | The header has a fixed ~366 px minimum width, so the Bag icon is pushed off-screen and every page scrolls sideways. | Shrink the logo and tighten icon spacing below 380 px. |
| 3 | Serious (a11y) | Prototype, all pages | `<html>` has no `lang` attribute. | `lang="en-GB"` (Dawn sets this automatically in the theme). |
| 4 | Serious (a11y) | Bag drawer | The Klarna payment badge text contrast is 4.34:1, below the 4.5:1 minimum. | Darken the badge text. |
| 5 | Moderate (a11y) | Prototype | There is no "Skip to content" link. | Add one (Dawn has it built in). |
| 6 | Moderate (a11y) | FAQ and footer | Heading levels jump (h2 → h4). | Use h3. |
| 7 | Moderate (a11y) | Prototype | Some content sits outside landmarks; the bag drawer adds a second `<header>`; `aside` has `role=dialog`. | Use `<main>`, and a `div` for the drawer header and dialog. |
| 8 | Medium (perf) | Listing and product pages opened directly | The layout shifts heavily (CLS 0.4–0.8; target <0.1), and mobile LCP is ~4 s (target <2.5 s). The prototype loads the catalogue by JavaScript and then draws the page. | This goes away in Liquid (server-rendered). In the theme: reserve image space, preload the hero/product image, and use responsive `srcset`. |
| 9 | Low (SEO) | Prototype | Every page has the same `<title>`; there is no meta description, favicon or Open Graph tags. | Expected in a prototype; must be in the theme (per-page title and description from the 'Final SEO' tab, OG image, favicon). |
| 10 | Low | 47–52 links per page | Tap targets are under 24 px high (footer links, brand chips, A–Z letters). | Raise them to at least 24 px (WCAG 2.2) in the theme. |
| 11 | Info | Live Deyga Aloe Vera Gel and Beetroot Lip Balm pages | The current theme's gallery shows one more slide than the product has images (it repeats the variant image). | Theme behaviour; check in the new theme. |

## Live store detail (14 sampled updated products: 6 fragrance, 4 Vilvah, 4 Deyga)

- Every page returned 200.
- The image count in Shopify matched our upload plan on all 14.
- Every image carries the new descriptive alt text.
- Every product image was served as `image/webp`.
- There were no broken images and no JavaScript errors.
- The shopper journey worked:
  - search for "vilvah" found 44 products
  - add to cart and the cart page worked
  - the Shopify checkout page loaded (contact/delivery step)
- robots.txt, sitemap.xml, contact, refund, privacy and terms are all 200; the 404 page returns a proper 404.
