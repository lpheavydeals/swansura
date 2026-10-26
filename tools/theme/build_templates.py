"""Build the Day-2 Swansura templates (collection, brand, fragrance, product, bundle).

Writes compact JSON into theme/templates/:
  collection.json           every collection (auto-detects brand pages and skincare/fragrance colour)
  collection.brand.json     same sections, forced brand header (assign to brand collections later)
  collection.fragrance.json used by /collections/fragrance (oud header)
  product.json              every product
  product.bundle.json       sets and kits ('In this set' + savings near the top)

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


def write(name, data):
    (OUT / name).write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")))
    print(name, (OUT / name).stat().st_size)


if __name__ == "__main__":
    write("collection.json", collection_template())
    write("collection.brand.json", collection_template(mode="brand"))
    write("collection.fragrance.json", collection_template(mode="category", tone="scent"))
    write("product.json", product_template())
    write("product.bundle.json", product_template(bundle=True))
