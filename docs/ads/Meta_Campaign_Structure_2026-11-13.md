# Swansura – Meta campaign structure (new ad account)

Prepared 13 Nov 2026. Budget: £700 on Meta for the first 30 days. Products: Deyga and Vilvah heroes (lip balm, Milk Drops, Hair Care Kit first; more kits added as creatives are ready).

## Starting point
- Ad account act_1614052623400872: new, UK / GBP / London time, no campaigns, no spend history. Payment card and £700 spending limit still to add.
- Pixel 1593636862064099 + Conversions API working; domain verified; catalogue (983 items) linked; Instagram connected.
- Pixel data is thin: about 44 add-to-carts and 4 purchases a week. Meta needs about 50 optimisation events a week per ad set to finish "learning", so we keep the number of ad sets very small.

## Structure: 3 campaigns, 3 ad sets

| # | Campaign | Objective / optimisation | Budget | Starts |
|---|---|---|---|---|
| 1 | SW · Brand Reach · UK | Engagement → ThruPlay (video views) | £3/day | Day 1 |
| 2 | SW · Sales · Prospecting | Sales → Purchase (website) | £15/day | Day 1 |
| 3 | SW · Sales · Retargeting | Sales → Purchase (website) | £5/day | Day 4 (once audiences have people in them) |

Total about £23/day; 30 days ≈ £680, with £20–25 kept for Black Friday week.

### 1. Brand Reach (cheap awareness + audience building)
- Why: the brand is unknown in the UK (34 Instagram followers). Cheap video views reach UK Indian households and build "people who watched 50%" audiences for retargeting.
- Ad set: UK, ages 22–55, Advantage+ audience, with suggestions (not hard limits): Ayurveda, Indian cuisine, Bollywood, natural skin care, hair care, South Asian culture.
- Placements: Advantage+ (Reels, Stories, Feed).
- Ads: the 3 videos (Lip Balm, Milk Drops, Hair Care Kit), 9:16 for Reels and Stories, 4:5 for Feed.
- Measure: cost per ThruPlay, 3-second view rate (hook), follower and profile visits.

### 2. Sales – Prospecting (the main spend)
- One ad set only, so all purchases and add-to-carts train one ad set and it exits learning faster.
- Audience: UK, Advantage+ audience, suggestions women 22–55 + the same interest suggestions as campaign 1. Exclude people who purchased in the last 30 days.
- Placements: Advantage+.
- Ads (6 to start): 3 videos + 3 image ads (4:5, 9:16 and 1:1 assets in each ad). Two primary texts per ad (A = "from home" hook, B = gift / routine / value) using Meta's text options.
- Optimisation: Purchase. Fallback: if there are fewer than about 8 purchases by Day 7, duplicate the ad set optimising for Add to Cart (44 a week today) and pause the Purchase one, then switch back once purchases pick up.
- Attribution: 7-day click, 1-day view.

### 3. Sales – Retargeting
- Audiences (custom, built now, filled by campaigns 1 and 2 and organic traffic):
  - website visitors, last 30 days
  - viewed a product or added to cart, last 14 days, not purchased
  - watched 50% of any video, last 30 days
  - Instagram / Facebook engagers, last 60 days
- Ads:
  - Advantage+ catalogue ad (carousel) on a Vilvah + Deyga product set, so people see the exact products they looked at.
  - The 3 image ads with a trust line ("Official UK partner · Shipped from the UK · Free delivery over £40").
- No discount is promised. If the client wants a first-order code for retargeting only, it has to exist in Shopify first.

## Timeline
| When | What |
|---|---|
| Before launch | Card + £700 spending limit (client); custom audiences + Vilvah/Deyga product set created; everything built PAUSED for approval |
| Day 1 | Campaigns 1 and 2 on |
| Day 4 | Campaign 3 on |
| Days 1–7 | Learning phase: no edits to budgets, audiences or ads unless something is broken |
| Day 3 | Creative check: pause any ad with CTR under 0.8% after £15 spend, or 3-second view rate under 20% |
| Day 7 | First review: CPA, ROAS, add-to-cart rate; apply the Add to Cart fallback if needed |
| Black Friday week (24–30 Nov) | If CPA is on target, raise Prospecting by 20% (about £3/day) from the buffer |
| From Day 8 | Scale winners +20% every 3–4 days while CPA stays on target; add new kit creatives (Nourished Lips, AM PM Serum Kit, Face Brightening Kit Large once restocked) |

## Targets (first 30 days)
- CTR: 1%+ Feed, 1.5%+ Reels
- Cost per purchase: aim under £25 (AOV today about £46; the client to confirm margin for the true break-even)
- ROAS: 1.5x+ in month 1 is a good start for a new account; 2.5x+ once learning is done
- Add-to-cart rate from ad clicks: 5%+

## Naming
- Campaign: `SW | <objective> | <stage> | UK`, e.g. `SW | Sales | Prospecting | UK`
- Ad set: `<audience> | <optimisation>`, e.g. `Adv+ W22-55 | Purchase`
- Ad: `<product> | <format> | <hook>`, e.g. `Deyga Lip Balm | Video 9x16 | From home`
- UTM: `utm_source=meta&utm_medium=paid_social&utm_campaign={{campaign.name}}&utm_content={{ad.name}}`

## Why not more ad sets
With £15–23 a day, splitting by product (lips / skin / hair) or by audience would give each ad set 2–5 conversions a week, so none would finish learning. One prospecting ad set with several ads lets Meta find the buyers and still shows which product's ad wins (per-ad results).
