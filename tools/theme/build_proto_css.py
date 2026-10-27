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
/* Shop all banner: the long keyword H1 stays on one line from 721 px (user, 27 Oct 2026) */
@media (min-width:721px){.swp .pagehead h1.h1-line{font-size:clamp(26px,3.15vw,52px)!important;white-space:nowrap}}
@media (max-width:720px){.swp .pagehead h1.h1-line{font-size:clamp(20px,6vw,26px)!important}}
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
