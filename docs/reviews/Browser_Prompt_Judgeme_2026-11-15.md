# Browser prompt: Judge.me review requests + Amazon review import (15 Nov 2026)

Paste the block below into Claude in Chrome while logged in to Shopify admin with Judge.me open.

```
You are helping set up Judge.me product reviews for the Shopify store "Swansura - The Body Studio" (swansura.com, UK). I am logged in and the Judge.me app is open in Shopify admin. Work step by step, tell me what you see, and follow these rules:
- Do NOT upgrade the Judge.me plan, add a card, buy anything or accept new terms. If a step needs a paid plan, stop and tell me which plan and price.
- Do NOT turn on any coupon, discount or reward for reviews.
- Send requests to ALL customers. Never filter to "happy" or high-rated customers.
- Before clicking any button that SENDS emails, stop and tell me how many emails will go out and to which orders; wait for my "yes".
- Do not delete, hide or edit any review.

PART 1 – Automatic review requests
1. Go to Judge.me Settings → Review Requests (or "Emails & Requests" → "Review Request").
2. Turn review request emails ON.
3. Trigger: after the order is DELIVERED. If only "fulfilled" exists, use fulfilled and add 3 days to the delays below.
4. Delay: if Judge.me allows different timing by product tag or collection, set products tagged "Fragrance" = 7 days and everything else = 12 days. If only one delay is allowed, set 10 days.
5. Reminder: ON, 1 reminder, 6 days after the first email, only if no review was left.
6. Photo/video reviews: ON. Review coupon / incentive: OFF.
7. Sender name "Swansura", reply-to "info@swansura.com" (only if these fields exist).
8. Email text (if editable):
   Subject: How are you finding your {product name}?
   Body: Hi {first name}, thank you for shopping with Swansura. We'd love to hear what you think of {product name}, good or bad. Your review helps other shoppers choose. It only takes a minute.
   Reminder subject: A quick review of {product name}?
   (Use Judge.me's own variable names for product and first name.)
9. Save. Tell me exactly which options you set and which were not available on our plan.

PART 2 – Review requests for existing customers
1. Find Judge.me's option to send review requests for PAST orders (often under Requests / "Send review requests" / "Past orders").
2. Choose orders from the last 90 days (all orders, all customers). The store has about 20 orders since October 2026.
3. Use the same email text as Part 1.
4. STOP before sending: tell me the number of orders/emails and the date range. Send only after I say yes.

PART 3 – Import our reviews from Amazon UK
1. Find Judge.me's import tool (Settings or Reviews → Import → "Import from Amazon" / "AliExpress / Amazon"). If it needs a paid plan, stop and tell me.
2. Ask me for our Amazon UK seller storefront link if you can't find it. Only use Amazon listings that WE (Swansura) sell.
3. For each Amazon listing, import its reviews onto the Shopify product that is EXACTLY the same item: same brand, same product name, same size (ml/g) and same type (EDP / EDT / Parfum / set). If you are not sure it is the same item, skip it and add it to a "not imported" list.
4. Import only genuine reviews as they are: do not edit text, do not change star ratings, do not leave out low ratings. Keep the option that shows the source / marks them as imported ON if Judge.me offers it.
5. Do NOT import reviews from vilvahstore.com, deyga.in, brand websites or any other seller.
6. At the end give me a table: Amazon listing (ASIN or URL) → Swansura product → number of reviews imported, average rating; plus the "not imported" list with the reason.
```
