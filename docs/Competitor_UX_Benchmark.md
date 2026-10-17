# Competitor UX Benchmark — what Swansura's prototype is missing

Checked 17 Oct 2026 in a desktop browser (1440px): homepage, one skincare category page and one product page on each site. Screenshot sheets are in `docs/benchmark/` (`sheet_<site>[_cat|_pdp].jpg`; lf = LOOKFANTASTIC, pu = Purplle, cl = Clinikally, ts = The Skin Store).

| Site | Pages checked |
|---|---|
| LOOKFANTASTIC (UK) | Home · Shop All Skincare (4,666 items) · Shark CryoGlow mask PDP |
| Purplle (IN) | Home · Serum & Essence (535 products) · Plum 10% Niacinamide Serum PDP |
| Clinikally (IN) | Home · "Dullness" concern page (7,778 products) · Peltos Niacinamide Sleep Mask PDP |
| The Skin Store (IN) | Home · Face Moisturizer (64 products) · Aveeno Skin Relief Lotion PDP |

Legend: **Must** = add before launch · **Should** = add in the theme build · **Later** = phase 2 / ads phase · **Skip** = don't copy.

---

## 1. What we already do as well or better
- Premium, editorial look; competitors are either discount-heavy (Purplle), clinical (Clinikally) or plain template (The Skin Store).
- Routines and "Complete the ritual" bundles with *Add all*; Clinikally's "Build your routine" (Step 1 Cleanse → 4 Protect) is the closest match.
- Shop by concern, keyword pages, collection FAQs, scent notes (top/heart/base) and scent families: none of the four has fragrance notes.
- Free-delivery progress bar on the product page, the "Official UK partner" line, and an advent calendar (only LOOKFANTASTIC has an equivalent).
- Quick *Add to bag* on product cards and a sticky filter panel.

## 2. Header, navigation and search
| Gap | Who does it | Priority |
|---|---|---|
| Delivery-promise bar: "Order by 1AM tonight for Next Day Delivery" plus app and loyalty links | LOOKFANTASTIC | **Must** (use our real cut-off, e.g. "Order by 2pm for same-day dispatch") |
| Sign-in / account and wishlist icons in the header | All four | **Must** |
| Search with rotating hints ("Search 'Serum'", "Search 'Sunscreen'") and an AI "Ask" button ("ASK LIA") | Clinikally, LOOKFANTASTIC | **Should** (hints); **Later** (AI assistant) |
| Brand A-Z directory with a search box inside the brand filter | LOOKFANTASTIC | Have the A-Z; **Should** add brand search in the filter |
| Promo code strip ("20% OFF SELECTED · USE CODE: FLASH", "Flat ₹100 off your first order · APPFIRST") | LOOKFANTASTIC, Purplle | **Should**: one quiet line for a first-order code |

## 3. Homepage sections
| Gap | Who does it | Priority |
|---|---|---|
| **Shop by price band**: "Under ₹299 / ₹499 / ₹699" tiles; "Gifts under £25 / £50 / £100" | Clinikally, LOOKFANTASTIC | **Must**: Under £15 / £25 / £50 tiles (AOV ladder towards the £50 free-delivery threshold) |
| **Shop by concern with faces**: Acne, Pigmentation, Dullness, Anti-ageing, Hairfall, Dandruff, each with a one-line fix ("Reduce dark spots with kojic acid") | Clinikally | **Should**: we have concern tiles; add the hero ingredient line and real imagery |
| **Shop by ingredient** (Vitamin C, Niacinamide, Salicylic, Hyaluronic, Ceramide, Rice water) | Clinikally, Purplle | **Should**: suits Deyga/Vilvah (beetroot, goat milk, kumkumadi, red sandalwood) |
| "Behind the brand" editorial blocks and brand spotlight strips | LOOKFANTASTIC | **Should**: "Behind the brand: Deyga's farm" and "Vilvah's goat-milk dairy" |
| Product carousels with ratings: "The ones you'll rate", "Just landed", "Trending products", "Newly arrived" | All | **Should**: New in + Trending rows once there are reviews |
| "Why shop with us" block + homepage FAQ (SEO text) | Purplle, Clinikally | **Should**: short version, 5 FAQs |
| Monthly beauty box / subscription | LOOKFANTASTIC | **Later** |
| Floating rewards button ("TSS Rewards") and chat bubble | The Skin Store, LOOKFANTASTIC | **Should**: WhatsApp or chat; rewards **Later** |

## 4. Category / listing page
| Gap | Who does it | Priority |
|---|---|---|
| **Filters by concern, skin type, hair type, active ingredient, benefit, formulation** (we only have brand, price, type, availability) | Clinikally (9 filter groups), Purplle | **Must**: Concern, Skin/hair type, Key ingredient (Shopify metafields + Search & Discovery app) |
| Sub-category chips at the top ("Sets & Bundles · Moisturisers · Cleansers · Serums · Eye creams") | LOOKFANTASTIC | **Must**: cheap and fast to build |
| Quick-filter chips ("Bestseller", "Doctor's choice") | Clinikally | **Should**: "Bestseller", "Official partner", "Under £20" |
| Item count + richer sort (relevance, price, A-Z, new, rating) | All | **Should** |
| Product card: **star rating + review count**, badges (NEW IN, SAVE 20%, DERMATOLOGIST RECOMMENDED, Best Seller), wishlist heart | All four | **Must**: rating + wishlist; badges **Should** ("Official partner", "Best seller", "New") |
| Size chips on the card (10 ml / 30 ml / 50 ml) with "+1" | Purplle | **Should** where products have sizes |
| Promo tile inside the grid ("Your Haul, Tomorrow · Premier Delivery £5.95") | LOOKFANTASTIC | **Should**: "Free UK delivery over £50" or a routine tile |
| Long buying guide + price-list table under the grid ("From benefits to skin type, your go-to guide…") | Purplle | **Should**: we have FAQs; add a 300–500 word guide on the main collections |

## 5. Product page (biggest gaps)
| Gap | Who does it | Priority |
|---|---|---|
| **Real reviews**: rating snapshot with 5→1 star bars, "91% recommend", review search/sort, photos, brand replies, AI review summary | LOOKFANTASTIC (689 reviews), Purplle (4,572 ratings), Clinikally | **Must**: install a reviews app (Judge.me / Okendo); import existing reviews; request reviews by email after delivery |
| **Benefit chips** under the title ("Enhance skin texture · Soothe skin · Calm irritation") | Clinikally | **Must**: 3 chips per product, from the SEO sheet |
| **Hero ingredients** + **Key benefits** blocks (we only have Details / How to use / Delivery) | Clinikally, Purplle | **Must** |
| **Product FAQs** (8 questions: what is it, skin types, every night?, side effects…), also great for SEO | Clinikally | **Must**: 4–6 FAQs per hero product, FAQ schema |
| **Size / pack selector** with price per ml and a "Best value" tag; pack options (45 gm / 2 × 45 gm) | Purplle, Clinikally | **Must** for the AOV plan (Single / Duo / Routine) |
| Dispatch promise near the button ("In stock · Usually dispatched within 24 hours") | LOOKFANTASTIC | **Must** |
| Social proof: "292+ units sold recently", "#2 Best seller in Serum & Essence", "185,464 people saved" | Clinikally, Purplle | **Should**: only with real numbers |
| "Available offers" accordion (codes, bundles) | Purplle, Clinikally | **Should** |
| Postcode delivery check | Purplle, Clinikally | **Skip** for the UK; a dispatch cut-off line does the job |
| "Ask a question" / Q&A, AI assistant with suggested questions ("Is this suitable for sensitive skin?") | LOOKFANTASTIC | **Later** |
| Frequently bought together + "Other customers bought" + similar products | LOOKFANTASTIC, Clinikally | Have "Complete the ritual" and similar; **Should** add *Recently viewed* |
| Buy Now (straight to checkout) next to Add to cart | Clinikally | **Should** (Shopify dynamic checkout button) |
| Wishlist and share buttons on the product page | All | **Should** |
| Pay later: Klarna, Clearpay, PayPal Pay in 3 messaging under the price | LOOKFANTASTIC (footer) | **Must** for the UK (Shopify Payments + Klarna/Clearpay) |

## 6. Offers, loyalty and retention
| Gap | Who does it | Priority |
|---|---|---|
| First-order offer (5% off / ₹100 off) shown in header + pop-up | Clinikally, Purplle | **Must**: e.g. 10% for newsletter sign-up |
| Loyalty programme ("LF Beauty Plus+", "Purplle Elite", "TSS Rewards") | 3 of 4 | **Later** (Smile.io / Shopify Loyalty) |
| UK discount schemes: Student, NHS & key worker, 16-26, Over-50s | LOOKFANTASTIC | **Should**: Student Beans / NHS discount; cheap reach |
| Refer a friend | LOOKFANTASTIC | **Later** |
| Gift with purchase / "Spend £60 get a free mini", "Buy 2 get extra 5%" | LOOKFANTASTIC, Purplle | **Should**: ties to free minis and the AOV ladder |
| App-only deals | All | **Skip** |

## 7. Trust and expertise
- **Expert endorsement:** Clinikally shows "Doctor's choice" badges, dermatologist consultations and "Certified medical-grade products". **Should:** a "Studio pick" or "Ayurveda-expert approved" badge, plus an About page with the brand authorisation letters (see the research doc).
- **Footer trust row:** "Free delivery over Rs. 499 · Only the best products · Top-notch support · Secure payments" (The Skin Store). We have this. **Should** add the payment logos row (Visa, Mastercard, Amex, PayPal, Apple Pay, Google Pay, Klarna, Clearpay) as LOOKFANTASTIC does.
- **Reviews from verified buyers with age band and gender** (LOOKFANTASTIC). **Later**, via the reviews app.

## 8. What NOT to copy
- Purplle's wall of pink discount banners, "Sponsored" product rows and dozens of "Upto 50% off" tiles: cheap-looking and wrong for a premium positioning.
- The Skin Store's thin product page (title, price, description only, no reviews or ingredients) and its 70-link mega menu.
- Cookie banners covering a third of the screen (LOOKFANTASTIC). Keep ours small.
- Pincode checks, COD and app-download pushes: India-specific and not needed in the UK.

---

## Top 12 to add to the prototype (in order)
1. Reviews app + star rating and count on cards and product pages.
2. Product page: benefit chips, Hero ingredients, Key benefits, 4–6 FAQs (with FAQ schema).
3. Size / pack selector (Single · Duo · Routine) with a "Best value" tag.
4. "Usually dispatched within 24 hours" + order cut-off line by the button.
5. Klarna / Clearpay / PayPal pay-later line under the price; payment logos in the footer.
6. Category filters for Concern, Skin/Hair type and Key ingredient + sub-category chips on top.
7. Wishlist heart on cards and the product page; account + wishlist icons in the header.
8. Homepage "Shop by price" tiles (Under £15 / £25 / £50) and "Shop by ingredient".
9. First-order offer for newsletter sign-up (header line + small pop-up).
10. Badges: Official partner, Best seller, New in, Studio pick.
11. "Behind the brand" blocks for Deyga and Vilvah.
12. Recently viewed row and Buy Now button.
