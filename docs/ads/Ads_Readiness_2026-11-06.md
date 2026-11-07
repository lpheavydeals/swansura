# Paid ads readiness + November plan (6 Nov 2026)

Client plan (Claude Docs, private until shared): https://claude.ai/artifact/TWzSsWNgHbV6vuwhVd5icg
Spreadsheet: `docs/ads/Swansura_Ads_Plan_Nov2026.xlsx` (generator `tools/ads/ads_plan_nov2026.py`).

## Budget (£700, approved 6 Nov 2026)
Meta £432 (M1 skincare pilot £144, M2 fragrance gifting £204, M3 retargeting £84), Google £240 (G1 Standard Shopping £176, G2 Vilvah/Deyga brand search £64), TikTok £0 (organic; option B £100), buffer £28. Phase 1 13–20 Nov £29/day, Phase 2 21–30 Nov £44/day.

## Tracking found (browser journey on live site + Shopify Admin, 6 Nov)
- Meta Pixel 1593636862064099 (Facebook & Instagram channel web pixel): PageView, ViewContent, AddToCart, InitiateCheckout fire. Purchase not tested (needs a real order). CAPI not visible from the browser.
- Meta domain verification: no `facebook-domain-verification` meta tag, no DNS TXT (Google + Pinterest verified by DNS).
- Google tag GT-NFJ2RGMF: only `merchant-center-analytics.goog` page_view; no Google Ads (AW-) conversion or GA4 events → Google Ads not linked in the Google & YouTube app.
- TikTok: no pixel, no TikTok sales channel publication; only the 'TikTok Shop — SPL' app installed.
- Pinterest tag: PageVisit + checkout events fire.
- Publications: Online Store 780, Google & YouTube 779, Facebook & Instagram 779, Pinterest 775 products. Multifeeds (Google Shopping feed app) also installed.
- Cookie banner did not show to our US test IP and pixels fired at once; client to confirm the banner region covers the UK.
- Sales last 365 days: 13 product orders online (£709 gross), all fragrance. Last 30 days: search sessions convert 1.8%, direct 0.2%.

## Landing pages (local Lighthouse 12 mobile, slower CPU than PSI)
Collections 71–75 (LCP 3.0–3.3 s); product pages 54–62 (LCP 3.8–5.7 s; the main photo starts loading 1.9–3.2 s late). CLS 0 everywhere. Facebook + Shopify + GTM ≈ 1.5–2 s main thread.

## Site fixes for the website session
1. PDP main image eager + fetchpriority high + preload. 2. Meta domain-verification tag if the client chooses it. 3. Shorten long claim-like Vilvah/Deyga handles with redirects (needs OK). 4. Optional Black Friday gift-edit collection. 5. Client restocks: Lattafa Khamrah Qahwa (0), Vilvah hair kits (0), Milk Drops (25).

## Re-check 7 Nov 2026 (GSC, GA4, Meta)
- **Meta Pixel 1593636862064099** (Facebook & Instagram channel web pixel): PageView, ViewContent, AddToCart, InitiateCheckout fire on the live site (browser journey home → PDP → Add to bag → checkout). Purchase, CAPI (data sharing level) and domain verification can only be confirmed in Meta Events Manager / Business settings; no domain-verification meta tag or DNS TXT found.
- **GA4: not connected.** The site's only Google tag is GT-NFJ2RGMF (Google & YouTube app). Its config (page `webPixelsConfigList`) and the served gtag.js contain one destination, Merchant Center MC-X30FHZXTP7 (page_view, view_item, purchase). No G- (GA4) or AW- (Google Ads) ID anywhere. `target_country` is "ZZ" (not set) → set United Kingdom in the Google & YouTube app.
- **Search Console:** verified (google-site-verification meta tag + DNS TXT rwXEHe1L…); robots.txt lists https://www.swansura.com/sitemap.xml. Sitemap submission + index status need GSC access (none here).
- Cookie banner settings: not readable (connector lacks read_privacy_settings); our test browser is outside the UK so no banner showed.
