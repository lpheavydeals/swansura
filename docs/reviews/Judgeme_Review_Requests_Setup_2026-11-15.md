# Judge.me review requests: setup steps (15 Nov 2026)

Why manual: Judge.me settings live inside the Judge.me app. The Shopify connector used for the store cannot read or change app settings, and there is no Judge.me API access in this project. Someone with Shopify admin access does these steps (about 10 minutes).

## Steps (Shopify admin → Apps → Judge.me)
1. Open **Judge.me → Settings → Review Requests** (older menus: **Emails & Requests → Review Request**).
2. Turn **Review request emails ON**.
3. **When to send:** choose "after the order is **delivered**" (if only "fulfilled" is offered, add ~3 days to each delay below for UK post).
   - **Perfume / fragrance:** 7 days.
   - **Skincare / haircare / body (Vilvah, Deyga, anatomē, Highborn, Shiseido):** 12 days.
   - If your Judge.me plan allows only one delay for all products: use **10 days after delivery**.
   - If your plan allows different timing by product tag/collection: set fragrance = 7, everything else = 12 (product tags: perfumes carry `Fragrance`; Vilvah/Deyga carry `Skincare`).
4. **Reminder:** ON, **one** reminder, **5–7 days** after the first email, only if no review yet.
5. **Who gets it:** **all** customers / all orders. Do NOT filter to "happy" customers only (UK fake-review rules ban review gating).
6. **Incentive / coupon for reviews:** leave **OFF** (Google may ignore incentivised reviews for Shopping stars; any incentive must apply to good and bad reviews and be disclosed).
7. **Photo/video reviews:** ON (allowed, no reward needed).
8. **Email sender name:** Swansura. **Reply-to:** info@swansura.com.
9. **Email text** (replace the default if you like):
   - Subject: `How are you finding your {{ product_name }}?`
   - Body: `Hi {{ customer_first_name }}, thank you for shopping with Swansura. We'd love to hear what you think of {{ product_name }} – good or bad. Your review helps other shoppers choose. It takes a minute.` + the Judge.me stars/button.
   - Reminder subject: `A quick review of {{ product_name }}?`
10. **Past orders (one-off):** in Judge.me → **Requests / Send requests for past orders**, send to orders from the last 60–90 days (about 20 orders since Oct 2026). Same wording, sent to everyone.
11. Save. Then place or pick a test order and check **Judge.me → Requests** shows it as scheduled.

## After it's on
- Tell Claude when it is switched on; next steps: connect Judge.me → Google Shopping (product ratings in Merchant Center) and add the star rating to the product page's Google data (new theme draft).
