"""Build the Day-2 Swansura templates (collection, brand, fragrance, product, bundle).

Writes compact JSON into theme/templates/:
  collection.json           every collection (auto-detects brand pages and skincare/fragrance colour)
  collection.brand.json     same sections, forced brand header (assign to brand collections later)
  collection.fragrance.json used by /collections/fragrance (oud header)
  product.json              every product
  product.bundle.json       sets and kits ('In this set' + savings near the top)
  Day 3: page.json (+ collection fallback for empty menu pages), page.contact/.about/.faq/.advent/.sitemap,
  blog.json, article.json, search.json, cart.json

Run: python3 tools/theme/build_templates.py
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / "theme" / "templates"
WHITE = "scheme-59d2f8b9-4a37-4dc1-8c6e-dfe3d9894e6e"

CATEGORIES = ["skincare", "haircare", "bodycare", "fragrance", "sets-combos", "best-sellers",
              "serum", "moisturizers-gels", "cleanser", "sunscreen", "lip-balm", "hair-oil", "shampoo"]
BRANDS = ["milk-drop-brightening-serum-1", "milk-drop-brightening-serum", "tiziana-terenzi", "al-haramain",
          "gucci", "hemel-h", "signature-sillage-dorient", "dolce-gabbana", "luxury-collection-1", "fumeri",
          "bvlgari", "calvin-klein"]


def collection_template(mode="auto", tone="auto"):
    return {
        "sections": {
            "head": {"type": "sw-collection-head", "settings": {"mode": mode, "tone": tone, "show_intro": True}},
            "product-grid": {
                "type": "main-collection-product-grid",
                "settings": {
                    "products_per_page": 24, "columns_desktop": 3, "columns_mobile": "2",
                    "color_scheme": WHITE, "image_ratio": "portrait", "image_shape": "default",
                    "show_secondary_image": True, "show_vendor": False, "show_rating": False,
                    "quick_add": "standard", "enable_filtering": True, "filter_type": "vertical",
                    "enable_sorting": True, "padding_top": 32, "padding_bottom": 32,
                },
            },
            "copy": {"type": "sw-collection-copy", "settings": {"eyebrow": "About this page"}},
            "explore": {"type": "sw-explore", "settings": {"heading": "Explore more", "categories": CATEGORIES, "brands": BRANDS}},
            "recent": {"type": "sw-recent", "settings": {"heading": "Picking up where you left off", "limit": 6}},
            "newsletter": {"type": "sw-newsletter", "settings": {}},
            "faq": {"type": "sw-auto-faq", "settings": {"eyebrow": "Good to know", "heading": "Questions about Swansura"}},
        },
        "order": ["head", "product-grid", "copy", "explore", "recent", "newsletter", "faq"],
    }


def liquid(part):
    return {"type": "custom_liquid", "settings": {"custom_liquid": "{% render 'sw-pdp', part: '" + part + "' %}"}}


def product_template(bundle=False):
    blocks = {
        "brand": liquid("brand"),
        "title": {"type": "title", "settings": {}},
        "price": {"type": "price", "settings": {}},
        "paylater": liquid("paylater"),
        "bundle": liquid("bundle"),
        "variant_picker": {"type": "variant_picker", "settings": {"picker_type": "button", "swatch_shape": "circle"}},
        "quantity_selector": {"type": "quantity_selector", "settings": {}},
        # Kept from the live theme (Shopify Subscriptions app block).
        "subscriptions_app_block_nJ7pbQ": {
            "type": "shopify://apps/subscriptions/blocks/app-block/a3bfe9ec-96f8-4508-a003-df608a36d2ad",
            "settings": {
                "widget_style": "card", "widget_style_card_selector": "radio_button", "subscription_policy_url": "",
                "color_text_body": "#222222", "dividers_color": "#D9D9D9", "background_color": "#FFFFFF",
                "border_thickness": 1, "border_radius": 8, "product": "{{product}}",
            },
        },
        "buy_buttons": {"type": "buy_buttons", "settings": {"show_dynamic_checkout": True, "show_gift_card_recipient": True}},
        "delivery": liquid("delivery"),
        "trust": liquid("trust"),
        "details": liquid("details"),
        "ingredients": liquid("ingredients"),
        "how_to_use": liquid("how_to_use"),
        "shipping": liquid("shipping"),
        "complementary": {"type": "complementary", "settings": {"block_heading": "Complete the ritual", "make_collapsible_row": False, "icon": "none", "product_list_limit": 3, "products_per_page": 3, "pagination_style": "dots", "image_ratio": "portrait", "enable_quick_add": True}},
        "share": {"type": "share", "settings": {"share_label": "Share"}},
    }
    order = ["brand", "title", "price", "paylater", "variant_picker", "quantity_selector",
             "subscriptions_app_block_nJ7pbQ", "buy_buttons", "delivery", "trust", "bundle",
             "details", "ingredients", "how_to_use", "shipping", "complementary", "share"]
    if bundle:
        order.remove("bundle")
        order.insert(order.index("paylater") + 1, "bundle")
    return {
        "sections": {
            "crumbs": {"type": "sw-breadcrumbs", "settings": {}},
            "main": {
                "type": "main-product",
                "blocks": blocks,
                "block_order": order,
                "settings": {
                    "enable_sticky_info": True, "color_scheme": WHITE, "media_size": "medium",
                    "constrain_to_viewport": True, "media_fit": "contain", "gallery_layout": "thumbnail_slider",
                    "mobile_thumbnails": "show", "media_position": "left", "image_zoom": "lightbox",
                    "hide_variants": True, "enable_video_looping": False, "padding_top": 16, "padding_bottom": 12,
                },
            },
            "more": {"type": "sw-more-from", "settings": {"limit": 4}},
            "related-products": {
                "type": "related-products",
                "settings": {
                    "heading": "You may also like", "heading_size": "h2", "products_to_show": 4,
                    "columns_desktop": 4, "columns_mobile": "2", "color_scheme": WHITE, "image_ratio": "portrait",
                    "image_shape": "default", "show_secondary_image": True, "show_vendor": False,
                    "show_rating": False, "padding_top": 36, "padding_bottom": 28,
                },
            },
            "recent": {"type": "sw-recent", "settings": {"heading": "Recently viewed", "limit": 6}},
            "newsletter": {"type": "sw-newsletter", "settings": {}},
            "faq": {"type": "sw-auto-faq", "settings": {"eyebrow": "Good to know", "heading": "Questions about Swansura"}},
            "sticky": {"type": "sw-sticky-atc", "settings": {}},
        },
        "order": ["crumbs", "main", "more", "related-products", "recent", "newsletter", "faq", "sticky"],
    }


# ---------------- Day 3 ----------------
PAGE_MAP = """fragrance:fragrance
skincare:skincare
haircare:haircare
body-care:bodycare
lipcare:lip-balm
gift-set:sets-combos
best-sellers:best-sellers
cleanser:cleanser
moisturiser:moisturizers-gels
toner:toner
serum:serum
under-eye-cream:skincare
for-her:fragrance
for-him:fragrance
lipbalm:lip-balm
lib-scrub:lip-scrub
shampoo:shampoo
conditioner:shampoo
hair-oil:hair-oil
hair-serum:hair-styling-products
comb:haircare-tools-kits
body-lotion:body-cream-exfoliants
body-wash:body-cream-exfoliants
body-scrub-mask:body-cream-exfoliants
foot-cream:body-cream-exfoliants
body-butter:body-cream-exfoliants
body-scrub:body-cream-exfoliants
bath-bar:body-cream-exfoliants
jo-milano:luxury-collection-1
diamond-collection:diamond-collection
make-up-products:makeup-product"""

NEWS = {"type": "sw-newsletter", "settings": {}}


def page_head(**kw):
    st = {"eyebrow": "", "tone": "auto", "show_content": True, "map": PAGE_MAP}
    st.update(kw)
    return {"type": "sw-page", "settings": st}


def faq_blocks(pairs):
    blocks = {f"q{i}": {"type": "faq", "settings": {"q": q, "a": a}} for i, (q, a) in enumerate(pairs)}
    return blocks, list(blocks)


STORE_FAQ = [
    ("Are your products authentic?", "<p>Yes. Every product we sell is 100% authentic, and Swansura is an official UK partner of Deyga and Vilvah.</p>"),
    ("How quickly do you dispatch?", "<p>Orders are dispatched from the UK within 1–2 working days.</p>"),
    ("How much is UK delivery?", "<p>UK delivery is free on orders over £40, and orders over £70 get free delivery plus £5 off.</p>"),
    ("Do you deliver outside the UK?", "<p>At the moment we deliver to UK addresses only.</p>"),
    ("Can I return an item?", "<p>You can return unopened, sealed items within 14 days of delivery (return postage is paid by you). Damaged, faulty or wrong items are replaced or refunded at no cost. Our <a href=\"/policies/refund-policy\">refund policy</a> has the details.</p>"),
    ("How can I pay?", "<p>We accept Visa, Mastercard, American Express, Maestro, PayPal, Apple Pay, Google Pay and Shop Pay. Eligible orders can also be split into interest-free payments where this is offered at checkout.</p>"),
    ("How do I track my order?", "<p>Sign in to <a href=\"/account\">your account</a> with the email you ordered with to see your orders and tracking.</p>"),
    ("How can I contact you?", "<p>Use our <a href=\"/pages/contact\">contact page</a>, email us, or send us a message on Instagram.</p>"),
]

ADVENT_SKIN = ["vilvah-natural-lip-scrub-10-g-lemon-shea-butter-exfoliator-for-pigmented-dry-chapped-lips-gentle-sugar-polish-for-soft-even-lips", "vilvah-natural-lemon-lip-balm-10g-deep-hydration-pigmentation-reduction-with-shea-butter-avocado-oil-vitamin-e", "vilvah-grape-fruit-lip-balm-10g", "deyga-natural-vanilla-lip-balm-8g", "cucumber-curd-mint-soap-bar-115g", "charcoal-goatmilk-soap-bar-115g", "classic-goatmilk-soap-bar-115g", "classic-rose-goat-milk-soap-bar-125g", "vilvah-fragrance-free-cream-face-wash-100ml-gentle-hydrating-cleanser-for-sensitive-dry-skin-sulfate-free-paraben-free-silicone-free-enriched-with-banana-coconut-milk-extracts", "vilvah-lavender-sage-deo-shot-20g-natural-deodorant-for-men-women-chemical-free-long-lasting-odour-protection", "vilvah-deo-shot-rose-vanilla-20g-natural-deodorant-cream-for-women-men-24-hour-odour-protection-skin-soothing-paraben-sulphate-free", "vilvah-milk-lip-balm-spf-30-pa-natural-uv-protection-hydrating-lip-care-for-all-skin-types"]
ADVENT_SCENT = ["trussardi-pure-jasmine-eau-de-parfum-7ml-miniature-women-s-floral-fragrance", "trussardi-black-extreme-eau-de-toilette-7ml-miniature-men-s-woody-leather-fragrance", "jimmy-choo-i-want-choo-forever-eau-de-parfum-4-5ml-miniature-women-s-floral-gourmand-fragrance", "gucci-bloom-profumo-di-fiori-eau-de-parfum-10ml-pen-spray-women-s-floral-fragrance", "gucci-flora-gorgeous-orchid-eau-de-parfum-10ml-miniature-women-s-floral-gourmand-fragrance", "gucci-bloom-eau-de-toilette-10ml-miniature-women-s-floral-perfume", "calvin-klein-my-euphoria-eau-de-parfum-10ml-miniature-women-s-floral-gourmand-fragrance", "calvin-klein-eternity-aromatic-essence-parfum-intense-10ml-miniature-women-s-aromatic-floral-fragrance", "calvin-klein-eternity-parfum-10ml-miniature-men-s-warm-aromatic-fragrance", "calvin-klein-defy-parfum-10ml-miniature-men-s-warm-woody-fragrance", "calvin-klein-defy-eau-de-parfum-10ml-miniature-men-s-fresh-woody-fragrance", "gucci-guilty-pour-femme-eau-de-parfum-10ml-miniature-women-s-fragrance"]


def day3_templates():
    t = {}
    t["page.json"] = {"sections": {"head": page_head(), "newsletter": NEWS}, "order": ["head", "newsletter"]}

    t["page.contact.json"] = {
        "sections": {
            "head": page_head(eyebrow="Customer care", intro="<p>Questions about a product, an order or delivery? We're happy to help.</p>"),
            "cards": {"type": "sw-contact", "settings": {"heading": "How can we help?", "email_note": "We reply on working days", "help_url": "/pages/faq"}},
            "form": {"type": "contact-form", "settings": {"heading": "Send us a message", "heading_size": "h2", "color_scheme": WHITE, "padding_top": 20, "padding_bottom": 48}},
        },
        "order": ["head", "cards", "form"],
    }

    vb = {
        "v1": ("Official UK partner of Deyga & Vilvah", "We are an official UK partner of Deyga and Vilvah, two Indian natural skincare brands, so you can shop their range in the UK.", "/collections/milk-drop-brightening-serum-1", "Shop Deyga"),
        "v2": ("100% authentic", "Every product we sell is 100% authentic, from natural skincare to designer perfume.", "", ""),
        "v3": ("Fine fragrance", "Niche, Arabian and designer perfume from houses such as Tiziana Terenzi, Al Haramain, Hemel and Gucci.", "/collections/fragrance", "Shop fragrance"),
        "v4": ("Dispatched from the UK", "Orders leave our UK base within 1–2 working days, with free UK delivery over £40.", "/pages/faq", "Delivery questions"),
    }
    t["page.about.json"] = {
        "sections": {
            "head": page_head(eyebrow="Our story", show_content=True),
            "about": {"type": "sw-about", "blocks": {k: {"type": "value", "settings": {"title": a, "text": b, "link": c, "link_label": d}} for k, (a, b, c, d) in vb.items()}, "block_order": list(vb),
                      "settings": {"eyebrow": "About Swansura", "heading": "Natural skincare and fine fragrance, from one UK studio",
                                   "text": "<p>Swansura – The Body Studio is a UK online store for natural skincare and fine fragrance. We bring Indian natural skincare from Deyga and Vilvah to the UK, alongside niche, Arabian and designer perfume.</p><p>Everything is chosen with care, 100% authentic and delivered from the UK.</p>"}},
            "newsletter": NEWS,
        },
        "order": ["head", "about", "newsletter"],
    }

    blocks, order = faq_blocks(STORE_FAQ)
    t["page.faq.json"] = {
        "sections": {
            "head": page_head(eyebrow="Help", intro="<p>Delivery, returns, payment and orders: the quick answers.</p>"),
            "faq": {"type": "sw-faq", "blocks": blocks, "block_order": order, "settings": {"eyebrow": "Good to know", "heading": "Frequently asked questions"}},
            "newsletter": NEWS,
        },
        "order": ["head", "faq", "newsletter"],
    }

    t["page.advent.json"] = {
        "sections": {
            "head": page_head(eyebrow="Christmas 2026", intro="<p>Two advent calendars, twelve days each: natural skincare from Deyga and Vilvah, and designer fragrance miniatures.</p>"),
            "advent": {"type": "sw-advent", "blocks": {
                "skin": {"type": "calendar", "settings": {"title": "The Skin Studio Advent", "tag": "12 days of natural rituals", "tone": "skin",
                         "blurb": "Twelve natural lip, skin and body favourites from Deyga, Vilvah and the Swansura Selection, one for each day of the countdown.", "contents": ADVENT_SKIN}},
                "scent": {"type": "calendar", "settings": {"title": "The Scent Studio Advent", "tag": "12 days of fine fragrance", "tone": "scent",
                          "blurb": "Twelve designer fragrance miniatures from Gucci, Calvin Klein, Jimmy Choo and Trussardi to discover your next signature scent.", "contents": ADVENT_SCENT}},
            }, "block_order": ["skin", "scent"], "settings": {}},
            "newsletter": NEWS,
        },
        "order": ["head", "advent", "newsletter"],
    }

    t["page.sitemap.json"] = {"sections": {"head": page_head(eyebrow="Find anything"), "map": {"type": "sw-sitemap", "settings": {}}}, "order": ["head", "map"]}

    t["blog.json"] = {"sections": {"main": {"type": "sw-blog", "settings": {"eyebrow": "The Journal", "intro": "<p>Skincare routines, fragrance know-how and gift ideas from the Swansura studio.</p>"}}, "newsletter": NEWS}, "order": ["main", "newsletter"]}

    t["article.json"] = {
        "sections": {
            "main": {"type": "main-article", "blocks": {
                "title": {"type": "title", "settings": {"blog_show_date": True, "blog_show_author": False}},
                "featured_image": {"type": "featured_image", "settings": {"image_height": "adapt"}},
                "content": {"type": "content", "settings": {}},
                "share": {"type": "share", "settings": {"share_label": "Share"}},
            }, "block_order": ["title", "featured_image", "content", "share"], "settings": {}},
            "more": {"type": "sw-article-more", "settings": {"heading": "Keep reading"}},
            "newsletter": NEWS,
            "faq": {"type": "sw-auto-faq", "settings": {}},  # prototype article FAQs (custom.faq)
        },
        "order": ["main", "more", "newsletter", "faq"],
    }

    t["search.json"] = {
        "sections": {
            "main": {"type": "main-search", "settings": {
                "columns_desktop": 4, "columns_mobile": "2", "image_ratio": "portrait", "image_shape": "default",
                "show_secondary_image": True, "show_vendor": False, "show_rating": False, "enable_filtering": True,
                "filter_type": "vertical", "enable_sorting": True, "article_show_date": True, "article_show_author": False,
                "padding_top": 32, "padding_bottom": 32}},
            "recent": {"type": "sw-recent", "settings": {"heading": "Recently viewed", "limit": 6}},
        },
        "order": ["main", "recent"],
    }

    t["cart.json"] = {
        "sections": {
            "goal": {"type": "sw-cart-goal", "settings": {}},
            "cart-items": {"type": "main-cart-items", "settings": {"color_scheme": WHITE, "padding_top": 16, "padding_bottom": 24}},
            "cart-footer": {"type": "main-cart-footer", "blocks": {"subtotal": {"type": "subtotal", "settings": {}}, "buttons": {"type": "buttons", "settings": {}}},
                            "block_order": ["subtotal", "buttons"], "settings": {"color_scheme": WHITE, "padding_top": 20, "padding_bottom": 40}},
            "recent": {"type": "sw-recent", "settings": {"heading": "Recently viewed", "limit": 6}},
        },
        "order": ["goal", "cart-items", "cart-footer", "recent"],
    }
    return t


def write(name, data):
    (OUT / name).write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")))
    print(name, (OUT / name).stat().st_size)


if __name__ == "__main__":
    write("collection.json", collection_template())
    write("collection.brand.json", collection_template(mode="brand"))
    write("collection.fragrance.json", collection_template(mode="category", tone="scent"))
    write("product.json", product_template())
    write("product.bundle.json", product_template(bundle=True))
    for name, data in day3_templates().items():
        write(name, data)
