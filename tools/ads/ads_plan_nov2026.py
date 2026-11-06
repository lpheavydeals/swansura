"""Build docs/ads/Swansura_Ads_Plan_Nov2026.xlsx: the £700 November 2026 paid-ads plan
(campaigns, ad sets, ads + copy with length checks, keywords, landing pages, checklist, rules).
Stock/prices: Shopify admin + storefront, 6 Nov 2026. Lighthouse: local mobile run, 6 Nov 2026.
Run: python3 tools/ads/ads_plan_nov2026.py
"""
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter

OUT = Path(__file__).resolve().parents[2] / 'docs/ads/Swansura_Ads_Plan_Nov2026.xlsx'
S = 'https://www.swansura.com'
P = {
 'md': '/products/milk-drops-brightening-serum-40-ml-rice-milk-alpha-arbutin-skin-brightening-treatment-for-dark-spots-uneven-skin-tone',
 'sbk': '/products/vilvah-skin-brightening-kit-milk-drops-brightening-serum-20-ml-melt-in-milk-sunscreen-spf-50-pa-50-ml-fade-dark-spots-daily-uv-protection',
 'ampm': '/products/vilvah-am-pm-serum-kit',
 'ecmk': '/products/vilvah-everyday-care-milk-kit',
 'vilvah': '/collections/vilvah', 'deyga': '/collections/deyga',
 'gifts': '/collections/perfume-gift-sets', 'xmas': '/collections/christmas-gifts',
 'oud': '/collections/oud-perfume', 'u25': '/collections/gifts-under-25',
 'bloom': '/products/gucci-bloom-eau-de-parfum-gift-set-100ml-10ml-body-lotion-100ml-women-s-fragrance-set',
 'ahgold': '/products/al-haramain-amber-oud-gold-edition-eau-de-parfum-luxury-unisex-fruity-amber-fragrance',
}
def url(key, src, med, camp, content):
    return f"{S}{P[key]}?utm_source={src}&utm_medium={med}&utm_campaign={camp}&utm_content={content}"

LIMITS = {'Meta primary text': 125, 'Meta headline': 40, 'Meta description': 27,
          'Google headline': 30, 'Google description': 90, 'TikTok caption': 100}

BUDGET = [  # platform, campaign, p1/day, p2/day, total
 ('Meta', 'M1 Skincare – Vilvah Milk Drops pilot', 8, 8),
 ('Meta', 'M2 Fragrance gifting – gift sets + oud', 8, 14),
 ('Meta', 'M3 Retargeting – viewers, add-to-bag, engagers', 3, 6),
 ('Google', 'G1 Shopping – gift sets, oud, Vilvah/Deyga', 7, 12),
 ('Google', 'G2 Search – Vilvah/Deyga brand terms', 3, 4),
 ('TikTok', 'Organic posting only (option B: £100 Spark Ads 21–25 Nov)', 0, 0),
]
P1_DAYS, P2_DAYS = 8, 10  # 13–20 Nov, 21–30 Nov

CAMPAIGNS = [  # campaign, platform, objective, bidding, ad set, audience, placements, products, dates
 ('M1 Skincare pilot', 'Meta', 'Sales (conversions)', 'Optimise for Purchase; switch to Add to cart if <5 purchases by 20 Nov',
  'M1-AS1 UK women 22–55 Advantage+', 'UK; women 22–55; Advantage+ audience with suggestions: natural skincare, clean beauty, Ayurveda, South Asian beauty; exclude purchasers 30d',
  'Advantage+ placements (IG/FB feed, Reels, Stories)', 'Vilvah Milk Drops 40ml/20ml, Skin Brightening Kit, AM PM Serum Kit, Everyday Care Milk Kit', '13–30 Nov'),
 ('M2 Fragrance gifting', 'Meta', 'Sales (conversions)', 'Optimise for Purchase',
  'M2-AS1 UK gift buyers 25–60 broad', 'UK; all genders 25–60; broad (no interests); exclude purchasers 30d',
  'Advantage+ placements', 'Product set "Gift sets + oud – in stock, has photo" + Gucci Bloom set, Azzaro TMW set, D&G The One set, Gucci Flora mini, CK mini set, Al Haramain Amber Oud Gold/Carbon', '13–30 Nov (budget up 21 Nov)'),
 ('M3 Retargeting', 'Meta', 'Sales (Advantage+ catalogue ads)', 'Optimise for Purchase',
  'M3-AS1 Site + engagers', 'Website visitors 30d + AddToCart 14d + IG/FB engagers 60d; exclude purchasers 30d',
  'Advantage+ placements', 'Dynamic: products each person viewed (product set "All in stock, has photo")', '13–30 Nov'),
 ('G1 Shopping', 'Google', 'Sales – Standard Shopping', 'Maximise clicks, max CPC £0.60 (not PMax: no conversion history)',
  'Product groups: gift sets / oud & Arabian / Vilvah / Deyga; everything else excluded', 'UK; searches only', 'Google Search Network (Shopping), no partners',
  'In-stock heroes; exclude out of stock + tag "Photo pending"', '13–30 Nov'),
 ('G2 Brand search', 'Google', 'Sales – Search', 'Maximise clicks, max CPC £0.80',
  'G2-AG1 Vilvah; G2-AG2 Deyga', 'UK; English; phrase + exact', 'Google Search only (no Display, no partners)',
  '/collections/vilvah, /collections/deyga, Milk Drops page', '13–30 Nov'),
]

ADS = []  # campaign, ad id, format, creative brief, field, text, url
def ad(c, aid, fmt, brief, fields, link):
    for f, t in fields:
        ADS.append((c, aid, fmt, brief, f, t, link))

ad('M1', 'M1-A1', 'Reel 9:16, 15–25 s', 'UGC "My Milk Drops routine": serum out of the Swansura box, dropper close-up, two drops patted in, label ingredients on screen, end card "Official UK partner of Vilvah · Ships from the UK". First person, texture + routine only.',
   [('Meta primary text', 'A lightweight serum with rice milk and alpha arbutin. Vilvah Milk Drops, from the official UK partner. Ships from the UK.'),
    ('Meta headline', 'Vilvah Milk Drops · £30.99'), ('Meta description', 'Free UK delivery over £40')],
   url('md', 'meta', 'paid_social', 'm1_skincare', 'milkdrops_reel'))
ad('M1', 'M1-A2', 'Static 4:5 + 1:1', 'Kit card on #F5F2ED: real kit photo, name, "Milk Drops serum 20ml + SPF 50 sunscreen", price, delivery line.',
   [('Meta primary text', 'Vilvah Milk Drops serum 20ml and an SPF 50 sunscreen, together in one kit. From the official UK partner of Vilvah.'),
    ('Meta headline', 'Vilvah Skin Brightening Kit £29.99'), ('Meta description', 'Ships from the UK')],
   url('sbk', 'meta', 'paid_social', 'm1_skincare', 'sbk_static'))
ad('M1', 'M1-A3', 'Static 4:5 + 1:1', 'Kit card: AM PM Serum Kit photo, "two Vilvah face serums, one for morning, one for night", £47.99, "£40+ = free UK delivery".',
   [('Meta primary text', 'Two Vilvah face serums in one kit: one for your morning routine, one for night. Free UK delivery over £40.'),
    ('Meta headline', 'Vilvah AM PM Serum Kit · £47.99'), ('Meta description', 'Official UK partner')],
   url('ampm', 'meta', 'paid_social', 'm1_skincare', 'ampm_static'))
ad('M1', 'M1-A4', 'Carousel (4 cards)', 'Cards: Milk Drops 40ml, Skin Brightening Kit, Everyday Care Milk Kit, AM PM Serum Kit (real product photos, price on each card).',
   [('Meta primary text', 'Natural skincare from Vilvah, shipped from the UK by the official UK partner. Free UK delivery over £40.'),
    ('Meta headline', 'Shop Vilvah skincare'), ('Meta description', '100% authentic')],
   url('vilvah', 'meta', 'paid_social', 'm1_skincare', 'vilvah_carousel'))
ad('M2', 'M2-A1', 'Reel 9:16, 15 s', 'Unboxing: Gucci Bloom set + Azzaro The Most Wanted set opened on a table, each item named on screen, prices, end card "£5 off orders over £70".',
   [('Meta primary text', 'Gucci Bloom and Azzaro The Most Wanted gift sets, 100% authentic and sent from the UK. £5 off orders over £70.'),
    ('Meta headline', 'Perfume gift sets from £33.99'), ('Meta description', '£5 off orders over £70')],
   url('gifts', 'meta', 'paid_social', 'm2_fragrance', 'unboxing_reel'))
ad('M2', 'M2-A2', 'Reel 9:16, 12–15 s', '"3 gifts under £45": CK women\'s mini set £33.99, Gucci Flora mini set £44.99, Al Haramain Amber Oud Gold 60ml £32.99, 4 s each with price stickers.',
   [('Meta primary text', 'Three perfume gifts under £45: Calvin Klein minis, Gucci Flora minis and Al Haramain Amber Oud Gold.'),
    ('Meta headline', '3 perfume gifts under £45'), ('Meta description', 'Free UK delivery over £40')],
   url('xmas', 'meta', 'paid_social', 'm2_fragrance', 'under45_reel'))
ad('M2', 'M2-A3', 'Advantage+ catalogue (carousel/collection)', 'Product set "Gift sets + oud – in stock, has photo". Frame: white with the delivery line.',
   [('Meta primary text', 'Gift sets they will open first. Gucci, Azzaro, D&G and Calvin Klein, 100% authentic, sent from the UK.'),
    ('Meta headline', '{{product.name}}'), ('Meta description', '{{product.price}}')],
   url('gifts', 'meta', 'paid_social', 'm2_fragrance', 'catalogue'))
ad('M2', 'M2-A4', 'Static 4:5 + 1:1', 'Al Haramain Amber Oud bottles (Gold, Carbon) on #F5F2ED, "from £32.99 for 60ml".',
   [('Meta primary text', 'Al Haramain Amber Oud from £32.99 for 60ml. Gold, Carbon and more editions, sent from the UK.'),
    ('Meta headline', 'Al Haramain Amber Oud from £32.99'), ('Meta description', 'Free UK delivery over £40')],
   url('oud', 'meta', 'paid_social', 'm2_fragrance', 'amberoud_static'))
ad('M2', 'M2-A5', 'Static 4:5 + 9:16 (from 21 Nov)', 'Black Friday week: "Christmas gifting, sorted" on emerald silk, 3 gift sets (real photos), "Free UK delivery over £40 · £5 off over £70". NO percent-off unless set up in Shopify.',
   [('Meta primary text', 'Christmas gifting, sorted. Perfume gift sets and natural skincare kits, free UK delivery over £40 and £5 off over £70.'),
    ('Meta headline', 'Christmas gifts, sent from the UK'), ('Meta description', '£5 off orders over £70')],
   url('xmas', 'meta', 'paid_social', 'm2_fragrance', 'bf_static'))
ad('M3', 'M3-A1', 'Dynamic carousel', 'Products each person viewed, catalogue frame with delivery line.',
   [('Meta primary text', 'Still thinking it over? Free UK delivery over £40 and 14-day returns on unopened items.'),
    ('Meta headline', '{{product.name}}'), ('Meta description', '{{product.price}}')],
   url('gifts', 'meta', 'paid_social', 'm3_retargeting', 'dynamic') + ' (dynamic: product URL)')
ad('M3', 'M3-A2', 'Reel (reuse best of M1/M2)', 'Re-use the best-performing Reel after 18 Nov.',
   [('Meta primary text', 'Back for another look? 100% authentic skincare and perfume, sent from the UK. £5 off orders over £70.'),
    ('Meta headline', 'Your Swansura picks'), ('Meta description', 'Free UK delivery over £40')],
   url('xmas', 'meta', 'paid_social', 'm3_retargeting', 'reel_reuse'))
VIL_H = ['Vilvah Skincare UK', 'Official UK Partner of Vilvah', 'Vilvah Milk Drops Serum', 'Ships From the UK',
         'Free UK Delivery Over £40', 'Vilvah Kits From £13.99', '100% Authentic Vilvah', 'Vilvah Goat Milk Shampoo',
         'Shop Vilvah at Swansura', '£5 Off Orders Over £70', 'Vilvah Milk Drops 40ml £30.99', 'Natural Skincare From India']
VIL_D = ['Vilvah natural skincare, shipped from the UK. Free UK delivery on orders over £40.',
         'Official UK partner of Vilvah: serums, face washes, shampoos and kits, 100% authentic.',
         'Vilvah Milk Drops serum, 40ml £30.99 or 20ml £21.99. £5 off orders over £70.',
         'Kits for face, hair and body. 14-day returns on unopened items.']
DEY_H = ['Deyga Skincare UK', 'Official UK Partner of Deyga', 'Deyga Beetroot Lip Balm', 'Ships From the UK',
         'Free UK Delivery Over £40', 'Deyga Body Butter & Lip Care', '100% Authentic Deyga', 'Shop Deyga at Swansura',
         '£5 Off Orders Over £70', 'Deyga Face Wash & Shampoo', 'Natural Skincare From India']
DEY_D = ['Deyga natural skincare, shipped from the UK. Free UK delivery on orders over £40.',
         'Official UK partner of Deyga: lip care, body butters, face washes and hair care.',
         'Deyga Beetroot Lip Balm from £10.99. £5 off orders over £70.',
         'Kits and single products, 100% authentic. 14-day returns on unopened items.']
for i, h in enumerate(VIL_H):
    ADS.append(('G2', 'G2-AG1-RSA', 'Responsive search ad', 'Vilvah brand terms', 'Google headline', h, url('vilvah', 'google', 'cpc', 'g2_brand', 'vilvah_rsa')))
for d in VIL_D:
    ADS.append(('G2', 'G2-AG1-RSA', 'Responsive search ad', 'Vilvah brand terms', 'Google description', d, url('vilvah', 'google', 'cpc', 'g2_brand', 'vilvah_rsa')))
for h in DEY_H:
    ADS.append(('G2', 'G2-AG2-RSA', 'Responsive search ad', 'Deyga brand terms', 'Google headline', h, url('deyga', 'google', 'cpc', 'g2_brand', 'deyga_rsa')))
for d in DEY_D:
    ADS.append(('G2', 'G2-AG2-RSA', 'Responsive search ad', 'Deyga brand terms', 'Google description', d, url('deyga', 'google', 'cpc', 'g2_brand', 'deyga_rsa')))
ADS.append(('G1', 'G1-feed', 'Shopping (feed)', 'No ad copy: Google uses the feed title, photo and price. Add tracking template {lpurl}?utm_source=google&utm_medium=cpc&utm_campaign=g1_shopping', 'Feed title (first 70 shown)', 'As live, e.g. "Vilvah Milk Drops Hydrating Serum 40ml"', S + P['md']))
for t, c in [('Our Vilvah Milk Drops routine, shipped from the UK #skincareroutine #vilvah', 'milkdrops'),
             ('3 perfume gifts under £45 #christmasgifts #perfumetok', 'under45'),
             ('Unboxing the Gucci Bloom gift set #giftideas #perfume', 'unboxing')]:
    ADS.append(('TikTok', 'TT-organic', 'Organic video (option B: Spark Ad)', 'Same videos as the Reels', 'TikTok caption', t, 'Link in bio: ' + S + P['xmas'] + f'?utm_source=tiktok&utm_medium=organic&utm_campaign=nov26&utm_content={c}'))

KEYWORDS = [
 ('G2-AG1 Vilvah', '"vilvah"', 'Phrase', 480), ('G2-AG1 Vilvah', '[vilvah milk drops]', 'Exact', 390),
 ('G2-AG1 Vilvah', '"vilvah uk"', 'Phrase', ''), ('G2-AG1 Vilvah', '"vilvah skincare"', 'Phrase', ''),
 ('G2-AG1 Vilvah', '[vilvah goat milk shampoo]', 'Exact', 20), ('G2-AG1 Vilvah', '"vilvah serum"', 'Phrase', ''),
 ('G2-AG2 Deyga', '"deyga"', 'Phrase', 140), ('G2-AG2 Deyga', '"deyga uk"', 'Phrase', ''),
 ('G2-AG2 Deyga', '"deyga lip balm"', 'Phrase', ''), ('G2-AG2 Deyga', '"deyga skincare"', 'Phrase', ''),
]
NEGATIVES = ['free', 'sample', 'tester', 'dupe', 'wholesale', 'india', 'amazon', 'review', 'jobs', 'career', 'login', 'franchise', 'distributor', 'how to make', 'diy', 'recipe']

LANDING = [  # page, path key, ads, in stock, score, LCP, CLS, note
 ('Vilvah Milk Drops 40ml/20ml', 'md', 'M1-A1, G2-AG1', '25 (10 + 15)', 58, '3.8 s', 0, 'Hero for the pilot'),
 ('Vilvah Skin Brightening Kit', 'sbk', 'M1-A2', '10', 62, '4.5 s', 0, 'Long claim-like handle'),
 ('Vilvah AM PM Serum Kit', 'ampm', 'M1-A3', '10', 56, '5.1 s', 0, ''),
 ('Vilvah Everyday Care Milk Kit', 'ecmk', 'M1-A4 card', '10', '', '', '', 'Not measured'),
 ('/collections/vilvah', 'vilvah', 'M1-A4, G2-AG1', '69 of 85 products', 72, '3.2 s', 0, ''),
 ('/collections/deyga', 'deyga', 'G2-AG2', '62 of 74 products', '', '', '', 'Not measured'),
 ('/collections/perfume-gift-sets', 'gifts', 'M2-A1, M2-A3', '70 of 87 products', 72, '3.3 s', 0, ''),
 ('/collections/christmas-gifts', 'xmas', 'M2-A2, M2-A5, M3-A2', '99 of 121 products', 71, '3.2 s', 0, ''),
 ('/collections/oud-perfume', 'oud', 'M2-A4', '27 of 32 products', 74, '3.3 s', 0, ''),
 ('/collections/gifts-under-25', 'u25', 'optional', '41 of 46 products', 75, '3.0 s', 0, ''),
 ('Gucci Bloom EDP gift set', 'bloom', 'catalogue', '10', 60, '4.6 s', 0, 'Over £70: £5 off applies'),
 ('Al Haramain Amber Oud Gold', 'ahgold', 'catalogue', '15 (3 sizes)', 54, '5.7 s', 0, 'Slowest page'),
]

HEROES = [  # product, line, price, stock, use
 ('Vilvah Milk Drops serum 40ml / 20ml', 'Skincare', '£30.99 / £21.99', '10 / 15', 'Pilot hero'),
 ('Vilvah Skin Brightening Kit', 'Skincare', '£29.99', 10, 'Ad'), ('Vilvah AM PM Serum Kit', 'Skincare', '£47.99', 10, 'Ad'),
 ('Vilvah Everyday Care Milk Kit', 'Skincare', '£48.99', 10, 'Carousel'), ('Vilvah Milk Face Kit', 'Skincare', '£45.99', 5, 'Catalogue only'),
 ('Gucci Bloom EDP gift set', 'Fragrance', '£84.99', 10, 'Ad'), ('Azzaro The Most Wanted EDT Intense gift set', 'Fragrance', '£68.99', 10, 'Ad'),
 ('D&G The One for Women gift set', 'Fragrance', '£64.99', 5, 'Catalogue'), ('Gucci Flora Gorgeous mini set 3x5ml', 'Fragrance', '£44.99', 10, 'Ad'),
 ("Calvin Klein women's mini set 4x15ml", 'Fragrance', '£33.99', 10, 'Ad'), ('Al Haramain Amber Oud Gold', 'Fragrance', 'from £32.99', 15, 'Ad'),
 ('Al Haramain Amber Oud Carbon', 'Fragrance', 'from £35.99', 13, 'Catalogue (best seller: 2 orders)'), ('Chopard Oud Malaki 80ml', 'Fragrance', '£48.99', 8, 'Catalogue'),
 ('Lattafa Khamrah Qahwa 100ml', 'Fragrance', '£26.99', 0, 'NOT USED: sold out (5,400 searches/mo)'),
 ('Vilvah Hairfall Control / Hair Strengthening kits', 'Skincare', '£34.99', 0, 'NOT USED: sold out'),
 ('Deyga Chocolate Body Butter', 'Skincare', '£13.99', 2, 'NOT USED: low stock'), ('Deyga Nourished Lip Care Kit', 'Skincare', '£25.99', 1, 'NOT USED: low stock'),
]

READINESS = [
 ('Meta', 'Pixel 1593636862064099: PageView, ViewContent, AddToCart, InitiateCheckout', 'Fires (browser test 6 Nov)', 'Confirm Purchase after next real order'),
 ('Meta', 'Conversions API', 'Not visible from browser', 'Client: Facebook & Instagram app → Data sharing = Maximum'),
 ('Meta', 'Domain verification', 'No meta tag, no DNS TXT found', 'Client: Business settings → Domains → verify swansura.com'),
 ('Meta', 'Aggregated event measurement', 'Unknown', 'Client: rank Purchase first'),
 ('Meta', 'Catalogue', '779 products published; ~200 sold out, 40 without photo', 'Client: product sets filtered to in stock + not "Photo pending"'),
 ('Meta', 'Instagram', '34 followers (Oct)', 'Post 6–9 Reels before launch'),
 ('Google', 'Google tag GT-NFJ2RGMF', 'Only Merchant Center page_view; no AW- conversions, no GA4 events', 'Client: link Google Ads in Google & YouTube app, turn on conversion tracking'),
 ('Google', 'Merchant Center feed', '779 products published; ~3% of variants have GTIN; Multifeeds app also installed', 'Client: send Diagnostics screenshot; keep one feed per product'),
 ('Google', 'Merchant Center shipping/returns', 'Unknown', 'Client: £1.99 / free over £40; 14-day unopened returns'),
 ('TikTok', 'Pixel + channel', 'No pixel; no TikTok sales channel; only "TikTok Shop — SPL" app', 'Install official TikTok channel (January or option B)'),
 ('Pinterest', 'Tag', 'PageVisit + checkout events fire', 'None (not in budget)'),
 ('Site', 'Cookie banner', 'Not shown to our US test address; pixels fired immediately', 'Client: confirm banner region includes UK'),
 ('Site', 'Product-page speed', 'Mobile 54–62, LCP 3.8–5.7 s; main photo starts 1.9–3.2 s late', 'Website session: eager + fetchpriority + preload'),
]

RULES = [
 ('Pause ad', 'After £15 spend with link CTR < 0.7% (feed) or < 1.0% (Reels)'),
 ('Pause ad', 'After £25 spend with no add-to-bag'),
 ('Pause ad set', 'Spend ≥ 2 × break-even cost per purchase with 0 purchases (use £40 until margin known)'),
 ('Pause product', 'Stock ≤ 2 units or sold out'),
 ('Scale', '+20% every 3–4 days only while cost per purchase < break-even; money moves within £700'),
 ('Rebalance', '18 Nov: move up to £3/day between M1 and M2 by cost per add-to-bag'),
 ('Fallback', 'M1 → optimise for Add to cart if < 5 purchases by 20 Nov'),
 ('Search terms', 'Daily: add negatives for non-shoppers'),
 ('Benchmarks (research, not promises)', 'CPM £8–12.50 · CPC £0.50–0.90 · CTR 0.7–1.4% feed / 1.2–2.1% Reels · ROAS 2.0x test / 2.5x scale · AOV £35–50'),
 ('Break-even CPA', 'AOV × gross margin: at £46 → £13.80 (30%), £18.40 (40%), £23.00 (50%) — client to confirm margin'),
]

SITE_FIXES = [
 ('1', 'Product page main photo: loading=eager + fetchpriority="high" + <link rel=preload> (LCP image starts 1.9–3.2 s late)', 'Theme (new draft)'),
 ('2', 'Meta domain-verification meta tag in theme.liquid (if client picks the meta-tag method)', 'Theme'),
 ('3', 'Shorten long Vilvah/Deyga handles (e.g. …-fade-dark-spots-…) with redirects', 'Store, needs client OK'),
 ('4', 'Optional "Black Friday gift edit" collection: in-stock gift sets ≥ £40', 'Store, needs client OK'),
 ('5', 'Restock: Lattafa Khamrah Qahwa, Vilvah hair kits, Milk Drops', 'Client'),
]

HDR = Font(bold=True, color='FFFFFF'); FILL = PatternFill('solid', fgColor='1B4D3E')
WARN = PatternFill('solid', fgColor='F3E6E0')
def sheet(wb, title, header, rows, widths):
    ws = wb.create_sheet(title)
    ws.append(header)
    for c in ws[1]:
        c.font = HDR; c.fill = FILL; c.alignment = Alignment(wrap_text=True, vertical='top')
    for r in rows:
        ws.append(list(r))
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    for row in ws.iter_rows(min_row=2):
        for c in row:
            c.alignment = Alignment(wrap_text=True, vertical='top')
    ws.freeze_panes = 'A2'
    return ws

wb = Workbook(); wb.remove(wb.active)
ws = sheet(wb, 'Budget', ['Platform', 'Campaign', 'Phase 1 £/day (13–20 Nov, 8 days)', 'Phase 2 £/day (21–30 Nov, 10 days)', 'Total £'], [], [10, 52, 18, 18, 10])
tot = 0
for i, (pl, c, a, b) in enumerate(BUDGET, 2):
    ws.append([pl, c, a, b, f'=C{i}*{P1_DAYS}+D{i}*{P2_DAYS}']); tot += a * P1_DAYS + b * P2_DAYS
n = len(BUDGET) + 2
ws.append(['—', 'Buffer (platform overspend on some days)', '', '', 700 - tot])
ws.append(['Total', '', f'=SUM(C2:C{n-1})', f'=SUM(D2:D{n-1})', f'=SUM(E2:E{n})'])
for c in ws[n + 1]: c.font = Font(bold=True)
assert tot == 672, tot
ws.append([]); ws.append(['Note', 'Option B (TikTok £100 Spark Ads 21–25 Nov): take £60 from M2 and £40 from G1; needs TikTok pixel by 18 Nov.'])
ws.append(['Note', 'Spending caps: Meta account spending limit £450; Google campaign budgets as above (no account cap).'])

sheet(wb, 'Campaigns & ad sets', ['Campaign', 'Platform', 'Objective', 'Bidding', 'Ad set / ad group', 'Audience', 'Placements', 'Products', 'Dates'], CAMPAIGNS, [18, 9, 22, 32, 30, 48, 26, 50, 16])

rows = []
for c, aid, fmt, brief, f, t, link in ADS:
    lim = LIMITS.get(f)
    n_ = len(t)
    ok = '' if lim is None or t.startswith('{{') else ('OK' if n_ <= lim else 'TOO LONG')
    rows.append((c, aid, fmt, brief, f, t, n_, lim or '', ok, link))
ws = sheet(wb, 'Ads & copy', ['Campaign', 'Ad', 'Format', 'Creative brief', 'Field', 'Text', 'Chars', 'Limit', 'Check', 'Final URL (with UTM)'], rows, [9, 12, 20, 50, 20, 60, 7, 7, 9, 70])
bad = [r for r in rows if r[8] == 'TOO LONG']
assert not bad, bad
ws2 = sheet(wb, 'Search keywords', ['Ad group', 'Keyword', 'Match', 'UK volume/mo (Semrush, Oct 2026)'], KEYWORDS, [16, 32, 10, 18])
ws2.append([]); ws2.append(['Campaign negatives (phrase)', ', '.join(NEGATIVES)])
sheet(wb, 'Landing pages', ['Page', 'URL', 'Used by', 'In stock (6 Nov)', 'Mobile score', 'LCP', 'CLS', 'Note'],
      [(a, S + P[k], u, s, sc, l, c, nt) for a, k, u, s, sc, l, c, nt in LANDING], [32, 70, 20, 18, 10, 8, 6, 28])
ws = sheet(wb, 'Hero stock', ['Product', 'Line', 'Price', 'Units (6 Nov)', 'Use in ads'], HEROES, [44, 10, 16, 12, 34])
for row in ws.iter_rows(min_row=2):
    if str(row[4].value).startswith('NOT'):
        for c in row: c.fill = WARN
ws = sheet(wb, 'Readiness & checklist', ['Platform', 'Item', 'Found (6 Nov 2026)', 'Action (client unless stated)', 'Status'], READINESS, [10, 40, 46, 52, 14])
dv = DataValidation(type='list', formula1='"To do,In progress,Done"', allow_blank=True); ws.add_data_validation(dv)
dv.add(f'E2:E{len(READINESS)+1}')
for r in range(2, len(READINESS) + 2): ws.cell(r, 5, 'To do')
sheet(wb, 'Rules & KPIs', ['Rule', 'Detail'], RULES, [30, 100])
sheet(wb, 'Site fixes', ['#', 'Fix', 'Who'], SITE_FIXES, [4, 90, 24])
OUT.parent.mkdir(parents=True, exist_ok=True)
wb.save(OUT)
print(OUT, 'ads rows', len(rows), 'planned £', tot)
