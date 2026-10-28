# Installed apps review (27 Oct 2026)

The Shopify connector can't uninstall other apps (only itself), so uninstalling is done in admin: Settings → Apps → app → ⋯ → Uninstall.
Checked: installed apps (appInstallations), live theme app embeds (settings_data.json: only Judge.me), scripts in the live HTML (home, product, cart), selling plans (none), last 50 orders (9, all Online Store), discounts.

## Uninstall (unused; nothing on the site depends on them)
| App | Why |
|---|---|
| Instafeed (Mintt Studio) | Loads cdn.nfcube.com/instafeed-….js (28 KB) on every page, but there is no Instagram feed on the site. Speed. |
| IndexGPT: AI SEO | SEO is done in the theme + store data; an AI SEO app can overwrite titles/descriptions/alt text. |
| Subscriptions (Shopify) | No selling plans / subscription products. |
| TikTok Shop — SPL (SlashCart) | Third-party TikTok Shop connector; no TikTok orders. Use Shopify's own TikTok channel if TikTok Shop is wanted later. |
| MetaShop Instagram & Facebook (DolphinSuite) | Shoppable-comments app; no orders from it; Shopify's Facebook & Instagram channel already lists the products. |
| Clearer Address Validator (RoboTurk) | Checkout address checks need Shopify Plus checkout extensions; on Basic it does little. |
| Store Migration (Shopify) | One-off import tool; the store is built. |
| Spocket - US & EU Dropshipping | US/EU dropshipping supplier app; no Spocket products found. Check first that no live product is a Spocket listing. |

## Client to decide (may be in use)
| App | Note |
|---|---|
| UpPromote Affiliate | Active discount function 'UpPromote discount function - DO NOT DELETE' and creator-style codes (BLUSHING_BEAUTY, SAMSAF_BEAUTY, Louise5, BRISTOL_TAMIL_FAMILY); loads uppromote.js on every page. Keep if affiliates are active. |
| Sellerboard Profit Analytics | Amazon profit tool; keep if the client tracks Amazon UK + Shopify profit there. |
| Wava Carts (WhatsApp abandoned cart) | Keep only if WhatsApp cart reminders are set up and sending. |
| Multifeeds (Google Shopping feed) | Duplicates the Google & YouTube channel unless it feeds Merchant Center separately. |
| Canva Connect | Design tool, no storefront impact. Harmless. |

## Keep
Judge.me Reviews (theme embed, review block), Collective (supplies the 45 anatomē + Highborn London products — uninstalling removes them), Messaging (Shopify customer emails/Inbox), Collabs (creator partnerships for the Ads phase), Knowledge Base (Shopify, harmless), Shopify Claude Connector (this build).

## Done
- 28 Oct 2026: user uninstalled Instafeed, Store Migration and Canva Connect. Live homepage checked: the Instafeed script (cdn.nfcube.com) no longer loads.
- 28 Oct 2026 (later): IndexGPT and Subscriptions uninstalled.
- Still installed from the 'Uninstall' list: TikTok Shop — SPL, MetaShop Instagram & Facebook, Clearer Address Validator, Spocket.
