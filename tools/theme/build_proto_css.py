"""Compile the prototype's stylesheet into theme/assets/sw-proto.css, scoped to `.swp`.

The theme renders the prototype's own markup (same class names) inside `<div class="swp">` wrappers,
so the prototype CSS can be used unchanged without touching Dawn's components (cart drawer, forms…),
which share class names like .card, .grid, .drawer, .badge and .price.

  :root / html / body   -> .swp          (design tokens and base type live on each wrapper)
  #app / main#app       -> .swp.app      (content sections; header/footer wrappers have no .app)
  *                     -> .swp *
  other selectors       -> .swp <selector>
  @keyframes / @font-face / @property bodies are left alone.

Run: python3 tools/theme/build_proto_css.py
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
SCOPE = ".swp"

# Prototype classes that Dawn's stylesheets also style (base.css, component-*.css). They are renamed
# with a p- prefix in the compiled CSS and in the ported markup, so Dawn rules cannot leak into them.
RENAME = ["active", "article", "badge", "card", "dot", "grid", "light", "link", "media", "price", "top",
          "visually-hidden"]

# Neutralise Dawn's element-level rules (base.css) inside the wrappers; placed before the prototype CSS
# so prototype rules still win.
PRE = """
.swp{letter-spacing:normal;font-size:16px;line-height:1.6}
.swp h1,.swp h2,.swp h3,.swp h4,.swp h5,.swp h6{font-family:inherit;font-style:normal;font-weight:700;letter-spacing:normal;color:inherit;line-height:normal;word-break:normal}
.swp h4{font-size:1em}.swp h5{font-size:.83em}.swp h6{font-size:.67em}
.swp :focus-visible{box-shadow:none}
.swp a:not([href]){cursor:pointer}
"""

# Theme-only additions appended after the prototype CSS (kept here so the asset stays generated).
EXTRA = """
/* ---- theme additions (not in the prototype) ---- */
.swp{display:block;background:var(--paper);color:var(--ink);font-family:var(--body);font-size:16px;line-height:1.6;-webkit-font-smoothing:antialiased}
.swp h1,.swp h2,.swp h3{color:inherit}
.swp img{height:auto}
/* the prototype packs each photo whole (contain) at 86% of a 4:5 cell on the ivory mount, with white graded
   to ivory (tools/proto_gallery.py frame()); cards and brand-hero photos copy that with padding + multiply */
.swp img.pic{object-fit:contain;object-position:center}
.swp .p-card .p-media,.swp .story .imgs>a{background:var(--mount)}
.swp .p-card img.pic,.swp .story .imgs img.pic{padding:7%;background:transparent;mix-blend-mode:multiply}
.swp .p-card .p-media img.pic:not(.alt){transition:opacity .4s}
.swp .p-card:hover .p-media:has(.alt) img.pic:not(.alt){opacity:0}
/* Search and Bag are <button>s in the prototype, so they don't inherit the uppercase of .hleft/.hright */
.swp #openSearch,.swp #openBag{text-transform:none;letter-spacing:normal}
.swp-fixed{background:none!important}
.swp [hidden]{display:none!important}
/* Shopify wraps each section in a div, so the header's wrapper is the sticky element */
.shopify-section:has(> .swp > header.site){position:sticky;top:env(safe-area-inset-top,0px);z-index:40}
body:has(.stickybar.show) .swp .chatbtn{bottom:calc(84px + env(safe-area-inset-bottom,0px))}
html{scrollbar-width:thin;scrollbar-color:#CBBFAE transparent;scroll-behavior:smooth}
.swp .visually-hidden{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
/* page text (Shopify page content) and the contact form, in the prototype's type scale */
.swp .pagebody{max-width:72ch;color:var(--ink-2);font-size:16px;line-height:1.7;display:flex;flex-direction:column;gap:14px}
.swp .pagebody h2,.swp .pagebody h3{color:var(--ink);margin-top:14px}
.swp .pagebody h2{font-size:26px}.swp .pagebody h3{font-size:19px}
.swp .pagebody a{text-decoration:underline}
.swp .pagebody ul,.swp .pagebody ol{padding-left:20px;display:flex;flex-direction:column;gap:6px}
.swp .pagebody table{border-collapse:collapse;width:100%;font-size:15px}.swp .pagebody td,.swp .pagebody th{border-bottom:1px solid var(--line);padding:10px 8px;text-align:left}
.swp .cform{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(220px,100%),1fr));min-width:0;gap:14px;align-items:end}
.swp .cform label{display:flex;flex-direction:column;gap:6px;font-size:13px;letter-spacing:.06em;color:var(--ink)}
.swp .cform .full,.swp .cform .okmsg,.swp .cform .errmsg{grid-column:1/-1}
.swp .cform input,.swp .cform textarea{min-width:0;width:100%;font:inherit;font-size:15px;letter-spacing:0;padding:12px 14px;border:1px solid var(--line);border-radius:6px;background:#fff;color:var(--ink)}
.swp .cform input:focus,.swp .cform textarea:focus{outline:2px solid var(--emerald);outline-offset:1px}
.swp .cform .btn{justify-self:start}
.swp .okmsg{color:var(--emerald)}.swp .errmsg{color:var(--sale)}
/* phone tap targets (24px, WCAG 2.5.8) and fit, found by tools/qa/mobile_audit.js */
.swp .brandcell{min-width:0}.swp .brandcell .blogo img{max-width:100%}
.swp footer .legal nav a{display:inline-block;padding-block:3px}
.swp a.p-link{display:inline-flex;align-items:center;min-height:24px}
.swp .more a,.swp .more .page,.swp .more span{display:inline-block;min-width:28px;min-height:28px;padding:5px 8px;text-align:center}
/* search page: long page / article titles wrap inside their pills */
.swp .srch-links a{white-space:normal;max-width:100%}
.swp .srch-links>div{flex-wrap:wrap;overflow:visible}
/* bag drawer (user, 26 Oct 2026): items, delivery bar, extras, trust and payment marks scroll together in
   .bag-body; subtotal + checkout stay pinned in .foot, so the items and the checkout button are always visible */
.swp .bag .bag-body{flex:1;min-height:0;overflow:auto;overscroll-behavior:contain;padding:16px 24px 20px;display:flex;flex-direction:column;gap:18px}
.swp .bag .bag-body .lines{flex:none;overflow:visible;padding:0}
.swp .bag .line .pic{width:72px;height:90px;padding:6%;background:var(--mount);mix-blend-mode:multiply;border-radius:6px}
.swp .bag .extras{gap:10px;scrollbar-width:thin}
.swp .bag .extra{width:104px;max-width:104px;font-size:12px;line-height:1.35;gap:4px}
.swp .bag .extra .pic{width:104px;height:104px;padding:8px;background:var(--mount);border-radius:6px}
.swp .bag .extra span{display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;min-height:2.7em}
.swp .bag .extra button{min-height:30px;padding:4px}
.swp .bag .bag-body .bag-trust{flex-wrap:wrap;justify-content:flex-start;column-gap:14px;row-gap:6px}
.swp .bag .bag-body .pays{justify-content:flex-start}
.swp .bag .foot{flex:none;gap:10px;box-shadow:0 -8px 20px rgba(31,26,23,.06);background:var(--paper)}
.swp .bag .bag-sub{display:flex;justify-content:space-between;font-size:16px}
/* UK delivery options in the bag (user, 27 Oct 2026): standard £1.99 (free over £40), two-day £2.99, next-day £3.99 */
.swp .bag .shipopts{border:1px solid var(--line);border-radius:10px;padding:10px 14px;display:flex;flex-direction:column;gap:6px;font-size:13px}
.swp .bag .shipopts .so-h{display:flex;justify-content:space-between;align-items:baseline;font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--brass-ink);font-weight:600}
.swp .bag .shipopts .so-h small{font-size:11px;letter-spacing:0;text-transform:none;color:var(--muted,#6b6158);font-weight:400}
.swp .bag .shipopts .so{display:flex;justify-content:space-between;gap:10px}
.swp .bag .shipopts .so small{color:var(--muted,#6b6158);font-size:12px;margin-left:6px}
.swp .bag .shipopts .so b{color:var(--emerald);font-weight:600}
.swp .bag .bag-ship{display:flex;justify-content:space-between;font-size:14px}
.swp .bag .bag-view{align-self:center;font-size:13px;min-height:24px;display:inline-flex;align-items:center}
@media (max-height:620px){.swp .bag .bag-head{padding:12px 20px}.swp .bag .bag-note{display:none}}
/* phones: 'Added to your bag' bar at the bottom instead of the drawer (user, 27 Oct 2026) */
.swp .addedbar{position:fixed;left:12px;right:12px;bottom:calc(12px + env(safe-area-inset-bottom,0px));z-index:60;display:grid;grid-template-columns:48px minmax(0,1fr) auto 28px;align-items:center;gap:10px;padding:10px 8px 10px 10px;background:var(--card);border:1px solid var(--line);border-top:2px solid var(--brass);border-radius:12px;box-shadow:0 12px 36px rgba(31,26,23,.22);animation:abin .25s ease-out}
.swp .addedbar .pic{width:48px;height:60px;padding:6%;background:var(--mount);border-radius:6px;mix-blend-mode:multiply}
.swp .addedbar .ab-txt{display:flex;flex-direction:column;min-width:0;line-height:1.3}
.swp .addedbar .ab-txt b{font-size:13px;color:var(--emerald)}
.swp .addedbar .ab-txt span{font-size:12.5px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.swp .addedbar .ab-txt small{font-size:11px;color:var(--ink-2)}
.swp .addedbar .btn{min-height:38px;padding:0 12px;font-size:11px;white-space:nowrap}
.swp .addedbar .ab-x{width:28px;height:28px;font-size:20px;line-height:1;color:var(--ink-2)}
@keyframes abin{from{transform:translateY(16px);opacity:0}to{transform:none;opacity:1}}
@media (prefers-reduced-motion:reduce){.swp .addedbar{animation:none}}
@media (max-width:360px){.swp .addedbar{grid-template-columns:40px minmax(0,1fr) auto 24px;gap:8px}.swp .addedbar .pic{width:40px;height:50px}.swp .addedbar .btn{padding:0 10px}}
/* bag page: the Liquid render reserves the space so the footer never shows first */
.swp #bagPage{min-height:50vh}
/* official payment logos (Shopify payment_type_svg_tag) in the footer and the bag (user, 27 Oct 2026) */
.swp .pays{align-items:center;gap:6px}
.swp .pay-ic{display:inline-flex;line-height:0}
.swp .pay-ic svg{display:block;width:38px;height:24px;border-radius:4px}
/* announcement bar on one line at every width (user, 27 Oct 2026): full width, no wrapping; .rot (set by
   sw-proto.js when the messages don't fit side by side) shows one message at a time */
.swp .announce .wrap{max-width:none;flex-wrap:nowrap;white-space:nowrap}
.swp .announce.rot .wrap{display:grid;padding-block:9px}
.swp .announce.rot .wrap>*{grid-area:1/1;opacity:0;transition:opacity .25s;pointer-events:none}
.swp .announce.rot .wrap>.on{opacity:1;pointer-events:auto}
@media (max-width:1320px){.swp .announce .wrap>*{overflow:hidden;text-overflow:ellipsis;max-width:100%}}
@media (max-width:480px){.swp .announce{font-size:11.5px;letter-spacing:.03em}}
@media (max-width:360px){.swp .announce{font-size:11px;letter-spacing:.01em}}
/* minimal search field in the header (user, 27 Oct 2026); icon only below 900px */
.swp #openSearch.srchfield{display:flex;align-items:center;gap:10px;height:40px;width:clamp(200px,17vw,280px);padding:0 16px;border:1px solid var(--line);border-radius:999px;background:#FAF8F4;color:var(--ink-2);font-size:13.5px;transition:border-color .2s,background .2s}
.swp #openSearch.srchfield:hover,.swp #openSearch.srchfield:focus-visible{border-color:var(--brass);background:#fff}
.swp #openSearch.srchfield svg{flex:none;color:var(--ink)}
.swp #openSearch.srchfield .txt{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
@media (max-width:900px){.swp #openSearch.srchfield{width:auto;height:40px;padding:0 8px;border:0;background:none}}
/* back-in-stock email pop-up (user, 27 Oct 2026): centred card on desktop, bottom sheet on phones */
.swp .bis{position:fixed;z-index:71;left:50%;top:50%;transform:translate(-50%,-50%);width:min(420px,calc(100vw - 32px));background:var(--card);border-radius:12px;border-top:3px solid var(--brass);box-shadow:0 24px 60px rgba(0,0,0,.2);padding:28px 24px 22px;display:flex;flex-direction:column;gap:12px}
.swp .bis h3{font-size:22px;line-height:1.2;margin:0}
.swp .bis .bis-p{margin:0;color:var(--ink-2);font-size:14px}
.swp .bis input{height:46px;border:1px solid var(--line);border-radius:6px;padding:0 14px;font:inherit;font-size:15px;background:#fff;color:var(--ink)}
.swp .bis input:focus{outline:2px solid var(--brass);outline-offset:1px}
.swp .bis input[aria-invalid=true]{border-color:var(--sale)}
.swp .bis .btn{width:100%}
.swp .bis .bis-note{margin:0;font-size:12px;color:var(--ink-2)}
.swp .bis .bis-x{position:absolute;top:10px;right:12px;width:32px;height:32px;font-size:22px;line-height:1;color:var(--ink-2)}
@media (max-width:600px){.swp .bis{top:auto;bottom:0;left:0;transform:none;width:100%;border-radius:16px 16px 0 0;padding-bottom:calc(22px + env(safe-area-inset-bottom,0px));animation:abin .25s ease-out}}
/* popular searches on desktop: one row of cards, each opens its links as a dropdown (user, 27 Oct 2026) */
@media (min-width:721px){
.swp #popular .searches{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:14px;align-items:start}
.swp #popular .searches details{position:relative;background:var(--card);border:1px solid var(--line);border-radius:var(--r);transition:border-color .2s,box-shadow .2s}
.swp #popular .searches details:hover,.swp #popular .searches details[open]{border-color:var(--brass);box-shadow:0 8px 24px rgba(31,26,23,.08)}
.swp #popular .searches summary{pointer-events:auto;cursor:pointer;list-style:none;display:flex;align-items:center;justify-content:space-between;gap:10px;padding:16px 16px 15px;min-height:86px}
.swp #popular .searches summary::-webkit-details-marker{display:none}
.swp #popular .searches summary h3{margin:0 0 5px;line-height:1.35}
.swp #popular .searches summary small{display:block;font-size:12.5px;color:var(--ink-2)}
.swp #popular .searches summary::after{content:'';flex:none;width:8px;height:8px;margin-top:-4px;border-right:1.5px solid var(--brass-ink);border-bottom:1.5px solid var(--brass-ink);transform:rotate(45deg);transition:transform .2s}
.swp #popular .searches details[open] summary::after{transform:rotate(-135deg);margin-top:4px}
.swp #popular .searches details>div{position:absolute;z-index:30;top:calc(100% + 6px);left:-1px;width:max(calc(100% + 2px),280px);max-height:min(420px,60vh);overflow:auto;background:var(--card);border:1px solid var(--line);border-top:2px solid var(--brass);border-radius:var(--r);box-shadow:0 18px 40px rgba(31,26,23,.14);padding:8px}
.swp #popular .searches details:nth-child(n+4)>div{left:auto;right:-1px}
.swp #popular .searches details>div a{display:block;padding:8px 10px;border-radius:6px;font-size:14px;color:var(--ink-2)}
.swp #popular .searches details>div a:hover,.swp #popular .searches details>div a:focus-visible{background:var(--mount);color:var(--ink)}
}
@media (min-width:721px) and (max-width:1100px){.swp #popular .searches{grid-template-columns:repeat(3,minmax(0,1fr))}}
@media (max-width:720px){.swp #popular .searches summary small{display:none}.swp #popular .searches summary h3{margin:0}}
/* banner H1s (page headers + brand stories) sized by length (--n = characters, set in Liquid) so they fit on one
   line: short titles keep the full size, long ones shrink; banners are one column on desktop (user, 27 Oct 2026) */
.swp .pagehead>div:first-child,.swp .story .copy{container-type:inline-size}
.swp h1.fit{font-size:clamp(26px,calc(100cqi / (var(--n,20) * .54)),60px)!important;text-wrap:balance}
.swp .story h1.fit{font-size:clamp(26px,calc(100cqi / (var(--n,20) * .54)),64px)!important}
@media (min-width:721px){.swp .pagehead{grid-template-columns:1fr;gap:18px}.swp .pagehead .lede{max-width:780px}}
@media (max-width:720px){.swp h1.fit,.swp .story h1.fit{font-size:clamp(22px,calc(100cqi / (var(--n,20) * .54)),36px)!important}}
/* Deyga / Vilvah story buttons side by side on phones (user, 27 Oct 2026) */
@media (max-width:600px){.swp .storybtns{flex-wrap:nowrap!important;gap:10px!important}.swp .storybtns .btn{flex:1 1 0;min-width:0;padding-inline:8px;letter-spacing:.06em;white-space:normal;text-align:center;line-height:1.25}}
/* homepage H1 (hero eyebrow) on one line on phones (user, 27 Oct 2026) */
@media (max-width:600px){.swp .hero h1.eyebrow{white-space:nowrap;letter-spacing:.1em}}
@media (max-width:360px){.swp .hero h1.eyebrow{font-size:11px;letter-spacing:.06em}}
/* wishlist count sits on the heart's corner: phones give .hicon a 40 px tap box, so anchor it to the centre (user, 27 Oct 2026) */
.swp .hicon .wcount{top:calc(50% - 19px);right:calc(50% - 23px)}
.swp .bagic .bagcount{top:-10px;right:-14px}
/* Shopify's cookie banner (Customer Privacy, rendered into the page): compact card in the bottom-left corner instead of a
   centred box (user, 27 Oct 2026). Accept and Decline stay the same size, side by side (ICO: rejecting must be as easy). */
#shopify-pc__banner.shopify-pc__banner__dialog{left:20px!important;right:auto!important;top:auto!important;bottom:20px!important;transform:none!important;margin:0!important;width:min(380px,calc(100vw - 40px))!important;max-width:none!important;max-height:calc(100vh - 40px);overflow:auto;padding:0!important;border-radius:12px!important;border:1px solid #E3DACD!important;box-shadow:0 12px 36px rgba(31,26,23,.18)!important}
#shopify-pc__banner .shopify-pc__banner__wrapper{padding:18px 20px 14px!important;margin:0!important;max-width:none!important;display:block!important}
#shopify-pc__banner .shopify-pc__banner__body{margin:0 0 12px!important;max-width:none!important}
#shopify-pc__banner #shopify-pc__banner__body-title{font-size:16px!important;margin:0 0 6px!important}
#shopify-pc__banner .shopify-pc__banner__body p,#shopify-pc__banner .shopify-pc__banner__body{font-size:12.5px!important;line-height:1.5!important}
#shopify-pc__banner .shopify-pc__banner__btns{display:grid!important;grid-template-columns:1fr 1fr;gap:8px!important;margin:0!important;width:100%!important;max-width:none!important}
#shopify-pc__banner .shopify-pc__banner__btns button{width:100%!important;min-width:0!important;margin:0!important;min-height:40px!important;height:auto!important;padding:8px 10px!important;font-size:13px!important}
#shopify-pc__banner #shopify-pc__banner__btn-accept{order:1}
#shopify-pc__banner #shopify-pc__banner__btn-decline{order:2}
#shopify-pc__banner #shopify-pc__banner__btn-manage-prefs{order:3;grid-column:1/-1;min-height:32px!important;border:0!important;background:none!important;text-decoration:underline;padding:4px!important}
@media (max-width:600px){#shopify-pc__banner.shopify-pc__banner__dialog{left:12px!important;bottom:12px!important;width:calc(100vw - 24px)!important}#shopify-pc__banner .shopify-pc__banner__wrapper{padding:14px 14px 12px!important}#shopify-pc__banner .shopify-pc__banner__body p,#shopify-pc__banner .shopify-pc__banner__body{font-size:12px!important}}
/* hero entrance: slide only, no fade, so the heading and the LCP image count as painted at once (PageSpeed 27 Oct 2026) */
.swp .hero .rise{opacity:1;animation-name:riseT}
@keyframes riseT{from{transform:translateY(18px)}to{transform:none}}
/* Dawn's font variables point at Plus Jakarta Sans too, so Assistant / Cormorant are never downloaded (PageSpeed 27 Oct 2026) */
:root{--font-body-family:'Plus Jakarta Sans','Helvetica Neue',Arial,sans-serif;--font-heading-family:'Plus Jakarta Sans','Helvetica Neue',Arial,sans-serif;--font-body-style:normal;--font-heading-style:normal}
/* PageSpeed (user, 28 Oct 2026: mobile PSI 70, LCP 7.4 s): paint-only animations ran non-stop and kept the main thread busy.
   Add-button shine moves with transform (composited) instead of 'left'; the footer wordmark shimmer runs only while the
   footer is on screen (.inview, sw-proto.js); the hero price tag drops its live blur (re-rendered on every slide). */
.swp .add::after{left:-60%;will-change:transform;animation-name:addshineT}
@keyframes addshineT{0%,62%{transform:translateX(0) skewX(-18deg)}82%,100%{transform:translateX(500%) skewX(-18deg)}}
.swp footer .fmark{animation-play-state:paused}
.swp footer .fmark-wrap.inview .fmark{animation-play-state:running}
.swp .hero .tag{backdrop-filter:none;-webkit-backdrop-filter:none;background:rgba(22,42,37,.88)}
/* Shopping assistant (help panel, user 30 Oct 2026): emerald silk header with a gold line + step bar, chat log with
   ivory bot bubbles and emerald answers, chip choices, compact product rows, people cards; bottom sheet on phones */
.swp .chatbtn{gap:9px;padding:12px 18px 12px 15px;background:linear-gradient(135deg,#EACB8E 0%,#D2A35A 50%,#C4924A 100%);color:#0F2E25;border:1px solid rgba(255,255,255,.55);box-shadow:0 8px 24px rgba(140,98,38,.38),inset 0 1px 0 rgba(255,255,255,.45);letter-spacing:.01em;font-weight:700;transition:transform .15s,box-shadow .15s}
.swp .chatbtn svg{color:#0F2E25}
.swp .chatbtn:hover{transform:translateY(-1px);box-shadow:0 12px 30px rgba(140,98,38,.46),inset 0 1px 0 rgba(255,255,255,.45)}
.swp .chatbtn:focus-visible{outline:2px solid var(--emerald);outline-offset:3px}
.swp .chatpanel.asst{width:min(400px,calc(100vw - 32px));height:min(600px,calc(100vh - 112px));height:min(600px,calc(100dvh - 112px));padding:0;gap:0;overflow:hidden;border:0;border-radius:16px;box-shadow:0 24px 60px rgba(19,26,23,.26),0 0 0 1px rgba(31,26,23,.06);outline:none;transform-origin:100% 100%;animation:asin .22s cubic-bezier(.2,.8,.2,1)}
@keyframes asin{from{opacity:0;transform:translateY(10px) scale(.98)}to{opacity:1;transform:none}}
.swp .asst .as-head{position:relative;display:flex;align-items:center;gap:12px;padding:16px 12px 16px 18px;background:var(--silk,var(--emerald));color:var(--on-dark);flex:none}
.swp .asst .as-head::after{content:"";position:absolute;left:0;right:0;bottom:0;height:1px;background:var(--gold-line,var(--brass))}
.swp .asst .as-av{flex:none;display:grid;place-items:center;width:40px;height:40px;border-radius:50%;background:rgba(255,255,255,.08);border:1px solid rgba(233,203,142,.55);color:#E9CB8E}
.swp .asst .as-t{flex:1;min-width:0;display:flex;flex-direction:column;line-height:1.25}
.swp .asst .as-t b{font-size:16px;font-weight:700;letter-spacing:.01em}
.swp .asst .as-t small{font-size:12px;color:var(--on-dark-2);display:flex;align-items:center;gap:6px}
.swp .asst .as-t small::before{content:"";width:7px;height:7px;border-radius:50%;background:#7FD1A8;box-shadow:0 0 0 3px rgba(127,209,168,.18)}
.swp .asst .as-ic{flex:none;display:grid;place-items:center;width:36px;height:36px;border-radius:50%;color:var(--on-dark);transition:background .15s}
.swp .asst .as-ic:hover{background:rgba(255,255,255,.12)}
.swp .asst .as-ic:focus-visible{outline:2px solid #E9CB8E;outline-offset:1px}
.swp .asst .as-bar{position:absolute;left:0;right:0;bottom:0;height:3px;z-index:1;background:transparent}
.swp .asst .as-bar i{display:block;height:100%;width:0;background:var(--gold-fill,var(--brass));transition:width .35s ease}
.swp .asst .as-log{position:relative;flex:1;min-height:0;overflow-y:auto;overscroll-behavior:contain;padding:18px 16px 8px;display:flex;flex-direction:column;gap:12px;background:linear-gradient(#fff,#FBF9F6);scrollbar-width:thin;scrollbar-color:var(--line) transparent}
.swp .asst .as-msg{max-width:100%;display:flex;flex-direction:column;gap:10px;animation:asmsg .25s ease-out}
@keyframes asmsg{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}
.swp .asst .as-msg.bot{align-self:flex-start;width:100%}
.swp .asst .as-msg.bot>p:not(.as-note):not(.as-links),.swp .asst .as-msg.bot>.as-bub{align-self:flex-start;max-width:92%;background:var(--mount);border:1px solid #EDE5D9;border-radius:4px 14px 14px 14px;padding:11px 14px;font-size:14px;line-height:1.5;color:var(--ink)}
.swp .asst .as-msg.bot ul{margin:6px 0;padding-left:18px;list-style:disc}
.swp .asst .as-msg.bot li{margin:2px 0}
.swp .asst .as-msg.you{align-self:flex-end;max-width:85%}
.swp .asst .as-msg.you p{background:var(--emerald);color:#fff;border-radius:14px 4px 14px 14px;padding:10px 14px;font-size:14px;line-height:1.45}
.swp .asst .as-step{font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--brass-ink)}
.swp .asst .as-typing p{display:flex;gap:4px;padding:14px!important}
.swp .asst .as-typing i{width:6px;height:6px;border-radius:50%;background:var(--brass);opacity:.35;animation:asdot 1s infinite}
.swp .asst .as-typing i:nth-child(2){animation-delay:.15s}.swp .asst .as-typing i:nth-child(3){animation-delay:.3s}
@keyframes asdot{0%,80%,100%{opacity:.3;transform:none}40%{opacity:1;transform:translateY(-3px)}}
.swp .asst .as-chips{display:flex;flex-wrap:wrap;gap:8px}
.swp .asst .as-chip{min-height:36px;padding:7px 14px;border:1px solid #D9C6A5;border-radius:999px;background:#fff;color:var(--emerald-2);font-size:13.5px;font-weight:600;line-height:1.25;text-align:left;transition:background .15s,border-color .15s,color .15s,transform .15s}
@media (hover:hover){.swp .asst .as-chip:hover:not([disabled]){background:var(--emerald);border-color:var(--emerald);color:#fff}}
.swp .asst .as-chip:active:not([disabled]){transform:scale(.97)}
.swp .asst .as-chip:focus-visible{outline:2px solid var(--brass);outline-offset:2px}
.swp .asst .as-chip[disabled]{opacity:.45;cursor:default}
.swp .asst .as-note{font-size:12.5px;color:var(--ink-2);line-height:1.45}
.swp .asst .as-link{font:inherit;color:var(--emerald);font-weight:600;text-decoration:underline;text-underline-offset:2px;padding:4px 0;min-height:24px}
.swp .asst .as-links{display:flex;flex-wrap:wrap;gap:6px 16px;font-size:13.5px}
.swp .asst .as-links a{color:var(--emerald);font-weight:600;padding:3px 0;min-height:24px}
.swp .asst .as-cards{display:flex;flex-direction:column;gap:8px}
.swp .asst .as-cards[hidden]{display:none}
.swp .asst .as-card{display:grid;grid-template-columns:56px minmax(0,1fr) auto;align-items:center;gap:12px;padding:8px 10px 8px 8px;background:#fff;border:1px solid var(--line);border-radius:12px;transition:border-color .15s,box-shadow .15s}
.swp .asst .as-card:hover{border-color:#D9C6A5;box-shadow:0 4px 14px rgba(31,26,23,.06)}
.swp .asst .as-pic{display:block;width:56px;height:70px;border-radius:8px;background:var(--mount);overflow:hidden}
.swp .asst .as-pic img{width:100%;height:100%;object-fit:contain;padding:5px;mix-blend-mode:multiply}
.swp .asst .as-ct{display:flex;flex-direction:column;gap:2px;min-width:0}
.swp .asst .as-ct small{font-size:11px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--brass-ink);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.swp .asst .as-ct a{font-size:13.5px;font-weight:600;line-height:1.3;color:var(--ink);display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.swp .asst .as-ct a:hover{color:var(--emerald)}
.swp .asst .as-pr{font-size:13.5px;font-weight:700;color:var(--emerald-2)}
.swp .asst .as-pr s{font-weight:500;color:var(--ink-2);margin-left:4px}
.swp .asst .as-add{min-height:34px;padding:0 14px;border-radius:999px;background:var(--emerald);color:#fff;font-size:12.5px;font-weight:700;letter-spacing:.04em;display:inline-flex;align-items:center}
.swp .asst .as-add:hover{background:var(--emerald-2)}
.swp .asst .as-add.out{background:none;color:var(--ink-2);border:1px solid var(--line);font-weight:600}
.swp .asst .as-more{align-self:flex-start;font-size:13px;font-weight:600;color:var(--emerald);text-decoration:underline;text-underline-offset:2px;min-height:28px}
.swp .asst .as-people{display:grid;gap:8px}
.swp .asst .as-person{display:flex;flex-direction:column;gap:1px;padding:12px 14px 12px 50px;position:relative;border:1px solid var(--line);border-radius:12px;background:#fff;transition:border-color .15s}
.swp .asst .as-person:hover{border-color:var(--emerald)}
.swp .asst .as-person::before{content:"";position:absolute;left:14px;top:50%;width:24px;height:24px;margin-top:-12px;border-radius:50%;background:var(--emerald) center/14px no-repeat}
.swp .asst .as-person.wa::before{background-color:#1F8F5A;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23fff' stroke-width='2'%3E%3Cpath d='M21 12a9 9 0 0 1-13.4 7.8L3 21l1.3-4.4A9 9 0 1 1 21 12Z'/%3E%3C/svg%3E")}
.swp .asst .as-person.ig::before{background-color:#9C4A6B;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23fff' stroke-width='2'%3E%3Crect x='4' y='4' width='16' height='16' rx='5'/%3E%3Ccircle cx='12' cy='12' r='3.6'/%3E%3C/svg%3E")}
.swp .asst .as-person.em::before{background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23fff' stroke-width='2'%3E%3Crect x='3' y='5' width='18' height='14' rx='2'/%3E%3Cpath d='m3 7 9 6 9-6'/%3E%3C/svg%3E")}
.swp .asst .as-person b{font-size:14px}
.swp .asst .as-person small{font-size:12.5px;color:var(--ink-2)}
.swp .asst .as-foot{flex:none;display:flex;align-items:center;gap:8px;padding:10px 12px calc(10px + env(safe-area-inset-bottom,0px));border-top:1px solid var(--line);background:#fff}
.swp .asst .as-foot input{flex:1;min-width:0;height:42px;padding:0 14px;border:1px solid var(--line);border-radius:999px;background:var(--mount);font:inherit;font-size:16px;color:var(--ink)}
.swp .asst .as-foot input::placeholder{color:#8A7F74;font-size:14px}
.swp .asst .as-foot input:focus{outline:none;border-color:var(--brass);background:#fff;box-shadow:0 0 0 3px rgba(181,132,58,.15)}
.swp .asst .as-foot input::-webkit-search-cancel-button{display:none}
.swp .asst .as-foot button{flex:none;display:grid;place-items:center;width:42px;height:42px;border-radius:50%;background:var(--emerald);color:#fff}
.swp .asst .as-foot button:hover{background:var(--emerald-2)}
.swp .asst .vh{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.swp .as-scrim{display:none}
@media (max-width:600px){
.swp .chatbtn{padding:0}
.swp .chatpanel.asst{left:0;right:0;bottom:0;width:100%;height:88vh;height:88dvh;max-height:none;border-radius:18px 18px 0 0;z-index:58;animation:assheet .28s cubic-bezier(.2,.8,.2,1)}
.swp .asst .as-head{padding-top:20px}
.swp .asst .as-head::before{content:"";position:absolute;top:7px;left:50%;width:36px;height:4px;margin-left:-18px;border-radius:2px;background:rgba(255,255,255,.3)}
@keyframes assheet{from{transform:translateY(100%)}to{transform:none}}
html.as-open .swp .as-scrim{display:block;position:fixed;inset:0;z-index:57;background:rgba(19,26,23,.45);animation:asfade .2s}
@keyframes asfade{from{opacity:0}}
html.as-open,html.as-open body{overflow:hidden}
html.as-open .swp .chatbtn{display:none}
}
@media (prefers-reduced-motion:reduce){.swp .chatpanel.asst,.swp .asst .as-msg,.swp .as-scrim{animation:none!important}.swp .asst .as-bar i{transition:none}}
/* the bag drawer shown inline on the /cart page */
.swp #bagPage .bag{position:static;width:100%;max-width:760px;margin:24px auto 0;box-shadow:none;border:1px solid var(--line);border-radius:var(--r);z-index:auto}
.swp #bagPage .bag .bag-head button{display:none}
.swp #bagPage .bag .bag-body{overflow:visible}
.swp #bagPage .bag .foot{box-shadow:none}
"""


def rename(css):
    for c in RENAME:
        css = re.sub(r"\.%s(?![\w-])" % re.escape(c), ".p-" + c, css)
    return css


def strip_comments(css):
    return re.sub(r"/\*.*?\*/", "", css, flags=re.S)


def scope_selector(sel):
    sel = sel.strip()
    if not sel:
        return sel
    if sel in (":root", "html", "body", "html,body"):
        return SCOPE
    # 'html body .x', 'body.x', ':root .x' -> scope
    m = re.match(r"^(?::root|html|body)(?=[\s.#:\[>~+]|$)(.*)$", sel)
    if m:
        rest = m.group(1)
        return SCOPE + rest if rest[:1] in (".", "#", ":", "[") else (SCOPE + " " + rest.strip() if rest.strip() else SCOPE)
    if sel.startswith("*"):
        return SCOPE + " " + sel
    # the prototype's <main id="app">: each content section's wrapper is <div class="swp app">
    if sel == "main#app":  # min-height of the prototype's single page container; not for section wrappers
        return "main.swp-main"
    m = re.match(r"^(?:main)?#app(?![\w-])(.*)$", sel)
    if m:
        return SCOPE + ".app" + m.group(1)
    return SCOPE + " " + sel


def split_selectors(prelude):
    out, depth, cur = [], 0, ""
    for ch in prelude:
        if ch in "([":
            depth += 1
        elif ch in ")]":
            depth -= 1
        if ch == "," and depth == 0:
            out.append(cur)
            cur = ""
        else:
            cur += ch
    out.append(cur)
    return out


def scope(css):
    out, i, stack = [], 0, []  # stack of at-rule names for open blocks
    buf = ""
    while i < len(css):
        ch = css[i]
        if ch in "\"'":  # copy strings verbatim
            j = css.index(ch, i + 1)
            buf += css[i:j + 1]
            i = j + 1
            continue
        if ch == "{":
            prelude = buf.strip()
            buf = ""
            if prelude.startswith("@"):
                name = re.match(r"@([\w-]+)", prelude).group(1)
                stack.append(name)
                out.append(prelude + "{")
            else:
                inside_raw = any(n in ("keyframes", "-webkit-keyframes", "font-face", "property", "page") for n in stack)
                stack.append("rule")
                if inside_raw:
                    out.append(prelude + "{")
                else:
                    out.append(",".join(scope_selector(s) for s in split_selectors(prelude)) + "{")
            i += 1
            continue
        if ch == "}":
            out.append(buf.strip() + "}")
            buf = ""
            stack.pop()
            i += 1
            continue
        if ch == ";" and not stack:  # top-level @import / @charset
            out.append(buf.strip() + ";")
            buf = ""
            i += 1
            continue
        buf += ch
        i += 1
    return "\n".join(out)


def main():
    html = (ROOT / "prototype/index.html").read_text()
    styles = re.findall(r"<style>(.*?)</style>", html, flags=re.S)
    css = max(styles, key=len)  # the design stylesheet (the first <style> is the 1-line reset)
    scoped = scope(rename(strip_comments(css)))
    out = "/* GENERATED by tools/theme/build_proto_css.py from prototype/index.html - do not edit */\n" + PRE + scoped + EXTRA
    (ROOT / "theme/assets/sw-proto.css").write_text(out)
    print("sw-proto.css", len(out), "bytes,", scoped.count("{"), "blocks")


if __name__ == "__main__":
    main()
