# Browser prompts: tracking setup before the ads (9 Nov 2026)

Paste one prompt at a time into the browser assistant (e.g. Claude in Chrome), signed in to the right account. Run them in this order. Each prompt ends with what to send back to us.

Rules in every prompt: the assistant never enters payment details, never creates or turns on a campaign, never deletes anything, and stops to ask you before accepting any terms or changing anything not listed.

| # | Prompt | Account to be signed in with | Time |
| --- | --- | --- | --- |
| 1 | Check Search Console owner + submit sitemap | Google account that owns Search Console | 5 min |
| 2 | Create GA4 | info@swansura.com (if prompt 1 confirms it owns Search Console) | 10 min |
| 3 | Connect GA4 in Shopify (Google & YouTube app) | Shopify admin + the same Google account | 10 min |
| 4 | GA4 settings + Search Console link | Same Google account | 5 min |
| 5 | Meta: domain verification + Conversions API | Meta Business admin + Shopify admin | 10 min |
| 6 | Shopify checkout: old scripts check | Shopify admin | 3 min |
| 7 | Google Ads: link + conversion tracking | Google account + Shopify admin | 10 min |

After prompts 1–7: place one small real test order and refund it (by hand, not by the assistant), then tell us so we can check Purchase in Meta, GA4 and Google Ads.

---

## Prompt 1 — Search Console: who owns it, and submit the sitemap

```
You are helping me check Google Search Console for my Shopify store www.swansura.com. Do not delete anything, do not remove any users, and do not change verification settings.

1. Open https://search.google.com/search-console and tell me which Google account I am signed in as (top-right avatar).
2. Open the property list. Tell me every property that matches swansura.com: is it a "Domain" property (swansura.com) or a "URL prefix" property (https://www.swansura.com/ or https://swansura.com/)? If there is none, stop and tell me.
3. For each matching property, open Settings → Users and permissions. List every user with their email and permission level (Owner, Full, Restricted), and say which one is the "Verified owner".
4. In the property for https://www.swansura.com/ (or the Domain property if that is the only one), open Indexing → Sitemaps. List the sitemaps already submitted with their status and "Discovered pages".
5. If https://www.swansura.com/sitemap.xml is not listed, type "sitemap.xml" in "Add a new sitemap" and click Submit. Report the status shown.
6. Open Indexing → Pages and tell me the numbers for "Indexed" and "Not indexed", and the top 5 reasons under "Why pages aren't indexed" with their counts.

Send me back: signed-in account, property type(s), the full users list with the verified owner, sitemap status, and indexing numbers.
```

**What to do with the answer:** if info@swansura.com is the verified owner (or an Owner), create GA4 with info@swansura.com in Prompt 2. If another account owns it, add info@swansura.com as an Owner in Search Console first (Settings → Users and permissions → Add user → Owner), signed in as the current owner. Or tell us, and we'll adjust the plan.

---

## Prompt 2 — Create the GA4 property

```
You are helping me create a Google Analytics 4 property for my Shopify store. Make sure I am signed in to Google as info@swansura.com; if not, stop and tell me. Do not paste any tracking code anywhere, do not link Google Ads, and do not accept any agreement without showing it to me first.

1. Open https://analytics.google.com. If a GA4 property for swansura.com already exists in any account I can see, stop and tell me its account name, property name and property ID instead of creating a new one.
2. Otherwise go to Admin → Create → Account.
   - Account name: Swansura Ltd
   - Leave the data sharing settings at their defaults.
3. Property:
   - Property name: swansura.com
   - Reporting time zone: United Kingdom
   - Currency: British Pound (GBP)
4. Business details: industry "Shopping" (or "Beauty & Fitness" if Shopping is not offered), business size Small.
5. Business objectives: choose "Drive online sales" (and "Understand web and/or app traffic" if more than one can be chosen).
6. Show me the Google Analytics terms page and wait for me to accept it myself (country: United Kingdom).
7. Data stream: choose Web.
   - Website URL: https://www.swansura.com
   - Stream name: swansura.com
   - Keep Enhanced measurement ON.
   - Click Create stream.
8. Do NOT copy the "Google tag" code into the website. Shopify will add it.

Send me back: the account name, property ID (numbers only), the Measurement ID (starts with G-), and the stream URL.
```

---

## Prompt 3 — Connect GA4 in Shopify's Google & YouTube app

```
You are helping me connect Google Analytics 4 to my Shopify store "Swansura - The Body Studio" (www.swansura.com) through the official Google & YouTube sales channel. Do not add or change any payment method, do not create any Google Ads campaign, and do not install any other app.

1. Open Shopify admin → Sales channels → Google & YouTube (or Settings → Apps and sales channels → Google & YouTube).
2. Tell me which Google account the app is connected to, and which Merchant Center account ID it shows.
3. Find the Google Analytics section ("Google Analytics" or "Connect Google Analytics"). Connect the GA4 property "swansura.com" with the Measurement ID I give you: [PASTE G- ID FROM PROMPT 2]. If the property is not offered, tell me which Google account is linked; it must be the same account that owns the GA4 property.
4. In the app's settings, check these and tell me what each is set to before changing anything:
   - Target country / market. It should be United Kingdom. Change it to United Kingdom if it is not.
   - Consent mode / "Google consent mode" / customer privacy: turn it ON if there is a switch.
   - Enhanced conversions: turn it ON if there is a switch. Accept its terms only after showing them to me.
5. Do not change the product feed or which products are synced.

Send me back: the connected Google account, Merchant Center ID, GA4 property now connected (name + G- ID), target country, consent mode on/off, enhanced conversions on/off, and anything the app says is missing.
```

---

## Prompt 4 — GA4 settings and Search Console link

```
You are helping me finish the settings of my GA4 property "swansura.com" in https://analytics.google.com (signed in as info@swansura.com). Do not delete anything and do not link Google Ads yet.

1. Admin → Data collection and modification → Data retention: set "Event data retention" to 14 months and save.
2. Admin → Data display → Key events (or Events): check whether "purchase" is marked as a key event. If "purchase" is listed and not marked, mark it. If it is not listed yet, tell me (it appears after the first order).
3. Admin → Product links → Search Console links: click Link, choose the Search Console property for www.swansura.com (or swansura.com), choose the web stream "swansura.com", and submit. If no Search Console property is offered, stop and tell me which Google account the Search Console property belongs to.
4. Admin → Data streams → swansura.com: tell me whether it says "Receiving traffic in past 48 hours" or "No data received".
5. Reports → Realtime: tell me how many users are shown in the last 30 minutes. I will open www.swansura.com in another tab while you look.

Send me back: data retention value, purchase key-event status, Search Console link status, stream status, and the Realtime count.
```

---

## Prompt 5 — Meta: verify the domain and turn on the Conversions API

```
You are helping me set up Meta tracking for my Shopify store www.swansura.com. Do not create, edit or turn on any ad or campaign, do not add a payment method, and do not delete anything.

Part A: Meta Business (business.facebook.com)
1. Open Meta Business Suite → Settings (Business settings). Tell me the business name and ID.
2. Brand safety and suitability → Domains. If swansura.com is listed, tell me whether it is "Verified".
3. If it is not listed or not verified: click Add, enter swansura.com, and choose the method "Update DNS TXT record". Copy the full TXT value (starts with facebook-domain-verification=) and show it to me. Do not click Verify yet.
4. Data sources → Datasets/Pixels: confirm pixel 1593636862064099 is listed and owned by this business. Tell me its name and the ad accounts assigned to it.

Part B: Where the DNS is managed
5. In Shopify admin → Settings → Domains, tell me whether swansura.com is "Managed by Shopify" or connected from another provider (and which one, if shown).
6. If it is managed by Shopify: open swansura.com → Domain settings → Edit DNS settings → Add custom record → TXT. Name: @ . Value: the facebook-domain-verification= value from step 3. Save. Do not change or delete any other record.
   If it is managed elsewhere (e.g. GoDaddy, 123-reg, Namecheap), stop and tell me the provider; I will add the TXT record there.
7. Wait 10 minutes, go back to Meta → Domains → swansura.com and click Verify. Tell me the result.

Part C: Conversions API in Shopify
8. Shopify admin → Sales channels → Facebook & Instagram → Settings → Data sharing (Customer data sharing). Tell me the current level. If it is not "Maximum", select Maximum, choose pixel 1593636862064099, and save. Show me any terms before accepting.

Part D: Events Manager check
9. Open Events Manager (business.facebook.com/events_manager) → pixel 1593636862064099 → Overview. List the events shown in the last 7 days (PageView, ViewContent, AddToCart, InitiateCheckout, Purchase…) and for each one whether the connection method is "Browser", "Server" or "Browser • Server", plus the Event match quality score if shown.
10. If you see "Aggregated event measurement" or "Web event configuration" for swansura.com, tell me what it shows, but do not change it.

Send me back: business name/ID, domain verification status, DNS provider, TXT record added (yes/no), data sharing level, and the Events Manager table from step 9.
```

---

## Prompt 6 — Shopify checkout: check for old tracking scripts

```
You are helping me check my Shopify checkout settings for old tracking code. Do not delete or change anything; only report.

1. Shopify admin → Settings → Checkout. Scroll to "Order status page" → "Additional scripts". Tell me whether the box is empty or has code. If it has code, copy the full code and show it to me.
2. Shopify admin → Settings → Customer events. List every pixel shown (App pixels and Custom pixels) with its name, status (Connected / Disconnected) and, for custom pixels, the first 10 lines of its code.
3. Shopify admin → Settings → Customer privacy (or "Cookie banner"). Tell me whether the cookie banner is ON, which regions it shows in (it must include the United Kingdom), and whether "Limit data collection until consent" or similar is on.

Send me back: the Additional scripts content (or "empty"), the Customer events list, and the cookie banner settings.
```

---

## Prompt 7 — Google Ads: link the account and set up conversions

Run this only once you have decided to use the Google budget (£240 in the plan). Creating the Google Ads account itself, with billing, is done by you, not the assistant.

```
You are helping me connect Google Ads to my Shopify store www.swansura.com through the Google & YouTube app. Do not create any campaign, do not enter or change payment details, and do not turn on any automatic campaign or "Performance Max" suggestion. If any screen asks for payment, stop and tell me.

1. Open https://ads.google.com signed in as info@swansura.com. Tell me the Google Ads account name and customer ID (xxx-xxx-xxxx), and whether billing is already set up. If no account exists, stop and tell me (I will create it myself).
2. In Shopify admin → Sales channels → Google & YouTube → Settings, find "Google Ads account" and connect the account with the customer ID from step 1. If it offers to create a campaign, skip it.
3. In the same app, find "Conversion tracking" / "Google Ads conversion measurement" and turn it ON. Tell me which conversions it lists (e.g. Purchase, Add to cart, Begin checkout, Page view).
4. Back in Google Ads → Goals → Conversions → Summary: list every conversion action with its source, status and whether it is "Primary" or "Secondary". Purchase should be Primary; tell me if it is not, but do not change anything else.
5. Google Ads → Tools → Linked accounts: tell me whether Google Analytics (GA4) and Google Merchant Center are linked. If GA4 "swansura.com" is offered, link it.

Send me back: Ads customer ID, billing status, conversions list with status/primary, and linked accounts.
```
