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
.swp img.pic{object-fit:cover;object-position:center}
.swp-fixed{background:none!important}
/* Shopify wraps each section in a div, so the header's wrapper is the sticky element */
.shopify-section:has(> .swp > header.site){position:sticky;top:env(safe-area-inset-top,0px);z-index:40}
body:has(.stickybar.show) .swp .chatbtn{bottom:calc(84px + env(safe-area-inset-bottom,0px))}
html{scrollbar-width:thin;scrollbar-color:#CBBFAE transparent;scroll-behavior:smooth}
.swp .visually-hidden{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
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
