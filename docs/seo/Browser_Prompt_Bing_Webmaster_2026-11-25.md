# Browser prompt: Bing Webmaster Tools for swansura.com (25 Nov 2026)

Why: ChatGPT search leans heavily on Bing's index, and ChatGPT is now Swansura's best sales source
(Nov 2026: 6 kept orders, all fragrance, landing on product and brand pages). The site has Google
verification but no Bing setup. Free; about 10 minutes. Paste the block below into Claude in Chrome
while signed in to Google as info@swansura.com (the Search Console owner).

```
Set up Bing Webmaster Tools for https://www.swansura.com. Do not pay for anything, change DNS, or accept any marketing offers.

1. Go to https://www.bing.com/webmasters and sign in with the Google account info@swansura.com (choose "Sign in with Google").
2. Add the site by choosing "Import your sites from GSC" (Google Search Console). Allow the read-only permission it asks for, select only https://www.swansura.com/ and import. This verifies the site and copies the sitemap.
   - If import is not offered or fails: use "Add your site manually" with https://www.swansura.com/ and the HTML META TAG method. STOP and give me the full meta tag (msvalidate.01 content value) — do not try to edit the Shopify theme yourself.
3. Sitemaps: open Sitemaps. If https://www.swansura.com/sitemap.xml is not listed, submit it. Tell me its status and the number of URLs discovered.
4. URL Submission: submit these URLs (as many as the daily quota allows, in this order) and tell me the quota shown:
   https://www.swansura.com/
   https://www.swansura.com/collections/fragrance
   https://www.swansura.com/collections/franck-olivier
   https://www.swansura.com/collections/armaf
   https://www.swansura.com/collections/lattafa
   https://www.swansura.com/collections/arabiyat-prestige
   https://www.swansura.com/collections/mercedes-benz
   https://www.swansura.com/collections/jo-milano
   https://www.swansura.com/collections/tiziana-terenzi
   https://www.swansura.com/collections/al-haramain
   https://www.swansura.com/collections/perfume-gift-sets-for-her
   https://www.swansura.com/collections/aftershave-gift-sets-for-him
   https://www.swansura.com/collections/vilvah
   https://www.swansura.com/collections/deyga
   https://www.swansura.com/blogs/journal
5. Settings / Crawl control: leave everything at default. Under "URL Inspection", inspect https://www.swansura.com/products/lattafa-khamrah-qahwa-eau-de-parfum-100ml and tell me whether it is indexed and any issue shown.
6. Report back: verified yes/no and how, sitemap status + URL count, URLs submitted + quota, the inspection result, and any errors or warnings on the dashboard (SEO reports, crawl errors). Also tell me if there is any report about Copilot / AI answers / chat citations and what it shows.
```

After it is done: the site's data in Bing appears within a few days. If the agent returns a
meta tag instead of importing, Claude adds it to `layout/theme.liquid` on a new theme draft
(same as the Meta and Pinterest tags) for the user to publish.
