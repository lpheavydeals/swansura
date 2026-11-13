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

---

## Prompt 8 — Microsoft Clarity: create the project (added 9 Nov 2026)

We add the Clarity code to the theme ourselves (it must wait for cookie consent for UK visitors), so this prompt only creates the project and links GA4.

```
You are helping me create a Microsoft Clarity project for my Shopify store www.swansura.com. Do not install any code on the website, do not install any Shopify app, and do not accept any terms without showing them to me first.

1. Open https://clarity.microsoft.com and sign in with Google using info@swansura.com. If I am signed in with another account, stop and tell me.
2. If a project for swansura.com already exists, stop and tell me its name and Project ID instead of creating another.
3. Otherwise click "New project":
   - Name: Swansura
   - Website URL: https://www.swansura.com
   - Site category: "E-commerce" (or "Shopping")
   Show me the terms, wait for me to accept, then create the project.
4. When Clarity shows "How would you like to install Clarity?", do NOT choose any install option. Go to Settings → Overview (or Setup) and copy the Project ID (about 10 letters and numbers).
5. Settings → Setup → Advanced settings (or Settings → Consent): tell me what the cookie / consent options say (e.g. "Cookies", "Consent mode", "Masking"). Do not change them. Set masking to "Balanced" if it is not already.
6. Settings → Setup → "Google Analytics integration": click Get started / Connect, sign in with info@swansura.com, choose the GA4 property "swansura.com" (Measurement ID G-548F2L8DJE) and save. Show me any permissions screen before allowing.
7. Settings → Team: tell me who has access.

Send me back: the Project ID, the masking setting, the consent options shown, and whether the GA4 integration is connected.
```

After this, send us the Project ID. We add Clarity to a new draft theme so it only starts after a visitor accepts analytics cookies in the Shopify cookie banner, then you publish the draft.

## Prompt 9a — Meta for Developers: create the app (run BEFORE Prompt 9; added 9 Nov 2026)

Run logged in at developers.facebook.com with the 'Swansura - The Body Studio' portfolio selected. The app stays in Development mode (enough for a token on the portfolio's own ad account); no App Review, no publishing.

```text
I'm logged in at developers.facebook.com (Meta for Developers). Create ONE app for reading Swansura's ad results. Rules: do NOT accept any terms, policies or developer registration yourself, do NOT enter or change any password or 2-factor code, do NOT add payment details: if any of these appear, stop and tell me so I can do it. Do NOT switch the app to Live / publish it, do NOT submit anything for App Review, do NOT generate or copy any access token or App Secret.

1. Go to My Apps (developers.facebook.com/apps). If an app named "Swansura Reporting" already exists, stop and give me its App ID and the business portfolio it belongs to.
2. Click "Create app".
   - App name: Swansura Reporting
   - App contact email: info@swansura.com
3. Use case: choose the Marketing API use case for ads, e.g. "Measure ad performance data with Marketing API" if offered, otherwise "Create & manage ads with Marketing API". Do not add any other use case (no Facebook Login, WhatsApp, Instagram, Messenger, Threads, games).
4. Business portfolio: select "Swansura - The Body Studio" (ID 1523489705546215). If it isn't listed, stop and tell me which portfolios are listed.
5. Review the requirements screen and tell me what it lists (e.g. business verification). Don't start verification. If nothing blocks it, go to the overview and click "Create app"/"Go to dashboard". If Meta asks for my password, stop and tell me to type it.
6. On the app dashboard, report only (change nothing): App ID, app mode (should be "Development"), the use case added, and whether "Marketing API" appears under Products/Use cases. If the Marketing API use case has a "Customize" page listing permissions, tell me whether ads_read and read_insights are available (do not request Advanced Access).
7. App settings → Basic: tell me the App ID, app domain field (leave empty), Privacy Policy URL field (leave empty unless required; if required to proceed, use https://www.swansura.com/policies/privacy-policy), category (choose "Business and pages" only if it is required). Save only if a required field blocked progress.

At the end give me: app name, App ID, mode, use case, business portfolio, and anything you could not do.
```

Then run Prompt 9 in Business Settings: step 1 there will find "Swansura Reporting" under Accounts → Apps (if not listed, Accounts → Apps → Add → "Connect an app ID" and enter this App ID).

## Prompt 9 — Meta: read-only system user token for Claude (added 9 Nov 2026)

Run logged in to Meta Business Settings as an admin of the 'Swansura - The Body Studio' portfolio. The browser agent prepares everything; **you click 'Generate token' and copy it yourself**, so the token never appears in a chat.

```text
I'm in Meta Business Settings (business.facebook.com/settings) for the business portfolio "Swansura - The Body Studio" (ID 1523489705546215). Set up a READ-ONLY system user so an assistant can read ad results. Rules: do NOT create, edit, pause or delete any campaign, ad set, ad or audience; do NOT add payment methods or change spending limits; do NOT remove any person, app or asset; do NOT accept any terms or policies yourself — if Meta asks me to accept Platform/Developer terms or to verify my identity, stop and tell me. Do NOT click "Generate token" and do NOT read out, copy or type any token: stop at that point and hand over to me.

1. App for the token: "Swansura Reporting", App ID 2390616515090214 (already created in Meta for Developers, owned by this portfolio). Check it is listed under Accounts → Apps. If it is not, click Add → "Connect an app ID" and enter 2390616515090214. Do not create another app.

2. System user. Users → System users → Add. Name: "Claude Reporting". Role: Employee (NOT Admin). Create it. If Meta says the portfolio has reached its system user limit, stop and tell me which system users exist.

3. Assign assets to "Claude Reporting" (button "Assign assets"):
   - Ad accounts → "SwansuraTheBodyStudio's ad account" (1614052623400872): turn on ONLY the view/performance permission (called "View performance" or "Manage campaigns: off, View performance: on"). Leave "Manage campaigns", "Manage ad account" and "Manage payments" OFF.
   - Datasets / Pixels → pixel 1593636862064099: view-only permission ("View dataset"/"Use dataset" only, not "Manage").
   - Apps → the app from step 1: "Develop app" is fine (needed to generate a token); nothing else.
   Save, and tell me exactly which permission boxes are ticked for each asset.

4. Open the "Generate token" dialog for "Claude Reporting" but do NOT finish it. Select the app from step 1, set Token expiration to "60 days" if offered (else note what is offered), and tick ONLY these permissions: ads_read, plus read_insights if it is listed. Leave ads_management, business_management and everything else unticked. Then STOP and tell me: "Ready — click Generate token yourself."

At the end give me a short summary: app name + App ID, system user name + ID, assets and permissions assigned, and anything you could not do.
```

After you click **Generate token**:
1. Copy the token (Meta shows it once). Do not paste it into Claude's chat.
2. In this Claude Code session, open the cloud environment menu in the title bar → **Edit** → **Network secrets** (or environment variables, if that is what is offered) and add `META_ACCESS_TOKEN` = the token. Also make sure the environment's network access allows `graph.facebook.com`.
3. Start a new session: Claude reads ad account 1614052623400872 and pixel 1593636862064099 read-only (spend, results, Purchase events with "Browser • Server").
4. To withdraw access later: Business Settings → System users → Claude Reporting → Revoke tokens (or remove the user).

## Prompt 10 — Meta: give the "Claude MCP" system user what it needs to build campaigns (added 9 Nov 2026)

API check, 9 Nov: the token already has ads_management, ads_read, business_management, pages_show_list and pages_read_engagement. The system user already has full control (Manage) of ad account 1614052623400872 and of the Facebook Page "SwansuraThebodystudio" (788176181050418). Still missing: the pixel is not assigned to the system user, no Instagram account is in the portfolio, the ad account time zone is America/Los_Angeles, no payment method was found, and the Catalog API is not enabled on the app. **The token does not need to be regenerated** unless step 6 is done.

```text
I'm in Meta Business Settings (business.facebook.com/settings) for the business portfolio "Swansura - The Body Studio" (ID 1523489705546215). Prepare it so the system user "Claude MCP" can build ad campaigns. Rules: do NOT create, publish or turn on any campaign, ad set or ad; do NOT spend money; do NOT remove any person, app or asset; do NOT generate or copy any token; do NOT accept new terms yourself; do NOT enter card details. If any of these come up, stop and tell me.

1. Pixel → system user. Data sources → Datasets (or Pixels) → "Swansura Thebodyshop" (1593636862064099) → Assign people / Add people → "Claude MCP" → full control ("Manage dataset" / "Manage pixel"). Save. Also confirm the dataset is connected to ad account 1614052623400872 (Connected assets).

2. Instagram. Accounts → Instagram accounts. If @swansura_thebodystudio is NOT listed, click Add → "Claim an Instagram account" (or "Connect your Instagram account") and stop when Meta asks for the Instagram login, so that I can type it. Once it is listed: Assign people → "Claude MCP" → full control; Connected assets → add ad account 1614052623400872. Also check that the Facebook Page "SwansuraThebodystudio" (788176181050418) shows the Instagram account as connected. Report what you see.

3. Page. Accounts → Pages → "SwansuraThebodystudio" (788176181050418): confirm "Claude MCP" has full control, or at least "Advertise"/"Create ads" + "Content". Report only; change nothing else.

4. Ad account settings. Accounts → Ad accounts → "SwansuraTheBodyStudio's ad account" (1614052623400872) → open in Ads Manager → Ad account settings:
   a. Time zone is America/Los_Angeles. Change it to "(GMT+00:00) Europe/London" and keep the currency as GBP. If Meta says that changing it will close this ad account and create a new one, STOP and tell me the exact message (don't confirm).
   b. Account spending limit: set it to £700 (this is a safety cap, not a budget). If a different screen is needed, tell me where.
   c. Report the business name, address and country shown for advertiser info. Don't change them.

5. Payment. Ads Manager → Billing & payments (or Payment settings) for 1614052623400872: report only whether a payment method exists and what type. Do NOT add or remove a card. I'll add the card myself.

6. Optional, for catalog ads later: open developers.facebook.com → app "Swansura Reporting" (2390616515090214) → Use cases → Add use case. If there is one about the Catalog API (e.g. "Manage products with Catalog API" or "Create & manage ads with Marketing API"), tell me the names offered and the permissions each lists. Do NOT add anything yet.

At the end give me a short list: what you changed (field → value), what failed, and anything waiting on me (Instagram login, card, time zone message).

---

## Prompt 11 – Switch the 'Swansura Reporting' app to Live (13 Nov 2026)

Why: Meta refuses to create ads through an app in Development mode ("Ads creative post was created by an app that is in development mode"). The campaign + ad set already exist PAUSED; the 6 ads are built once the app is Live.

```
You are in Meta for Developers (developers.facebook.com), already logged in and inside the app "Swansura Reporting" (App ID 2390616515090214). Goal: switch this app from Development mode to Live mode. Do not submit anything for App Review, do not request new permissions, do not remove any use case, do not change the app type, and do not pay for or start Business Verification. If a step needs something not listed here, stop and report what it asks for.

1. Open App settings → Basic in the left menu. Check these fields and fill only the empty ones:
   - Privacy Policy URL: https://www.swansura.com/policies/privacy-policy
   - User data deletion: choose "Data deletion instructions URL" and enter https://www.swansura.com/policies/privacy-policy
   - Terms of Service URL (if asked): https://www.swansura.com/policies/terms-of-service
   - Category: Business and pages (or Shopping, whichever is offered)
   - Contact email: leave whatever is already there
   - App icon: only if it is required to go Live, upload the Swansura logo (ask me for the file if you cannot find one; do not use any other brand's logo).
   Click "Save changes" and confirm the page shows no red errors.
2. Go to the "Publish" (or "Go live") item in the left menu, or use the App Mode switch at the top of the page (Development → Live).
3. If a checklist appears, read each item. Complete only items that are about the fields in step 1. Ignore anything that says "App Review", "Advanced access" or "Business Verification" unless it blocks the switch; if it blocks, stop and tell me the exact wording.
4. Click "Publish" / switch to "Live" and confirm.
5. Report back: the App Mode shown at the top of the page (should read "Live"), and any warning or banner that appears afterwards (copy the exact text).
```

After it reports "Live": tell Claude, and the 6 engagement ads are created PAUSED with `docs/ads/meta_setup/mk.py`.

---

## Prompt 12 – Put the card on the ad account (13 Nov 2026)

Why: the card was added, but the Marketing API still shows no payment method on ad account 1614052623400872, so Meta refuses to create even paused ads.

```
You are logged in to Meta Business Suite / Ads Manager for the business portfolio "Swansura - The Body Studio" (ID 1523489705546215). Goal: make sure the card that was just added is the payment method of the ad account "SwansuraTheBodyStudio's ad account" (ID 1614052623400872). Do not create, publish or turn on any campaign, ad set or ad. Do not add a second card, do not remove any card, and do not make any payment or prepay funds. Never type or read out the full card number; refer to cards only by brand and last 4 digits. If a step asks for something not listed here (new card details, ID documents, a code sent by SMS or email), stop and tell me what it asks for.

1. Open https://business.facebook.com/billing_hub/accounts/details?asset_id=1614052623400872 (Billing & payments for this ad account). If it does not open, go to Ads Manager → menu → Billing & payments, and pick "SwansuraTheBodyStudio's ad account" in the account switcher at the top.
2. Look at the "Payment methods" section of THIS ad account.
   - If a card is already listed there as the primary/default payment method: report its brand, last 4 digits and status (Active / Pending verification / Declined) and go to step 5.
   - If no card is listed: click "Add payment method". If Meta offers to use a card already saved in the business portfolio ("Use an existing payment method" / a card with the same last 4 digits), choose that card. Do NOT type new card details; if Meta only offers a new-card form, stop and tell me.
3. If asked, set that card as the primary payment method for this ad account and confirm. Accept any 3-D Secure / bank approval only if the screen says it is for adding the payment method (not for a charge); if anything mentions a payment amount other than a temporary £0–£1 verification hold, stop and tell me.
4. Check the account's payment settings page: Country United Kingdom, Currency GBP, Time zone Europe/London should already be set; do not change them.
5. Still in Billing & payments → Payment settings, look for "Account spending limit". If it can be set now, set it to £700 and save. If the option is not shown, just report that.
6. Report back:
   - the payment method shown for this ad account (brand, last 4 digits, status, whether it is primary),
   - whether the account spending limit is set and to what amount,
   - any red warning or banner on the Billing & payments page (copy the exact text).
```

After it reports the card as Active on the ad account: tell Claude, and the 6 engagement ads are created PAUSED with `docs/ads/meta_setup/mk.py` (it reuses the creatives in `creatives.json`).

---

## Prompt 13 – Verify a phone number on the ad account (13 Nov 2026)

Why: all 6 engagement ads were paused by Meta with error 3858013 'Phone number required: You need to verify a phone number for this ad account before you can run ads.' Needs an SMS/WhatsApp code, so a person finishes it.

```
You are logged in to Meta Ads Manager / Business Suite for the business portfolio "Swansura - The Body Studio" (ID 1523489705546215). Goal: verify a phone number for the ad account "SwansuraTheBodyStudio's ad account" (ID 1614052623400872), so its ads can run. Do not create, edit, publish or turn on any campaign, ad set or ad. Do not change the payment method, spending limit, currency or time zone. Do not start Business Verification and do not upload any ID document.

1. Open https://adsmanager.facebook.com/adsmanager/manage/ads?act=1614052623400872 . Look for a banner or a red error on the ads saying "Phone number required" / "Verify phone number". Click its "Verify" / "Add phone number" button.
   If there is no banner: open https://business.facebook.com/settings/ad-accounts/1614052623400872 and look for "Verify phone number"; or Ads Manager → Account settings (https://adsmanager.facebook.com/adsmanager/manage/account_settings?act=1614052623400872) → Business information / Contact → phone number.
2. Enter the phone number I give you (ask me for it; do not guess one, do not use a number already shown unless I confirm it). Country code United Kingdom (+44) unless I say otherwise.
3. Choose to receive the code by SMS (or WhatsApp if that is the only option). STOP here and ask me for the code. Type exactly the code I give you and submit.
4. Report back: whether Meta now shows the phone number as verified, and the exact text of any remaining banner or error on the Ads Manager page (copy it).
```

After it reports 'verified': tell Claude, and the 6 ads are switched back on (their status was set to PAUSED by Meta).
