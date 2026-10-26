"""Crawl the draft theme preview: status, Liquid errors, H1, title, description, canonical, JSON-LD, img alt, internal links."""
import json, re, sys, http.cookiejar, urllib.request, concurrent.futures, html
BASE = "https://www.swansura.com"
import os
THEME = os.environ.get("THEME", "200308064643")
cj = http.cookiejar.CookieJar()
op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
op.addheaders = [("User-Agent", "Mozilla/5.0 (QA crawl)")]
op.open(f"{BASE}/?preview_theme_id={THEME}").read()

def get(path):
    try:
        r = op.open(BASE + path, timeout=40)
        return r.status, r.read().decode("utf-8", "replace"), r.geturl()
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace"), path
    except Exception as e:
        return 0, str(e), path

def check(path):
    st, s, final = get(path)
    out = {"path": path, "status": st}
    if st != 200 and st != 404:
        return out
    m = re.search(r"Shopify\.theme = (\{[^}]*\})", s)
    out["theme"] = json.loads(m.group(1))["id"] if m else None
    out["liquid_error"] = re.findall(r"Liquid (?:syntax )?error[^<]{0,160}", s)[:3]
    out["h1"] = [" ".join(re.sub("<[^>]+>", "", h).split()) for h in re.findall(r"<h1[^>]*>(.*?)</h1>", s, re.S)]
    t = re.search(r"<title>(.*?)</title>", s, re.S)
    out["title"] = html.unescape(" ".join(t.group(1).split())) if t else None
    d = re.search(r'<meta name="description" content="([^"]*)"', s)
    out["desc"] = html.unescape(d.group(1)) if d else None
    c = re.search(r'<link rel="canonical" href="([^"]*)"', s)
    out["canonical"] = c.group(1) if c else None
    out["robots"] = re.findall(r'<meta name="robots" content="([^"]*)"', s)
    ld_ok, ld_types, ld_bad = 0, [], 0
    for blk in re.findall(r'<script type="application/ld\+json"[^>]*>(.*?)</script>', s, re.S):
        try:
            j = json.loads(blk); ld_ok += 1
            items = j.get("@graph", [j]) if isinstance(j, dict) else j
            for it in items if isinstance(items, list) else [items]:
                if isinstance(it, dict): ld_types.append(it.get("@type"))
        except Exception:
            ld_bad += 1
    out["ld_types"], out["ld_bad"] = ld_types, ld_bad
    imgs = re.findall(r"<img\b[^>]*>", s)
    out["img_noalt"] = sum(1 for i in imgs if not re.search(r'\salt="[^"]', i) and 'role="presentation"' not in i and 'alt=""' not in i)
    out["img_emptyalt"] = sum(1 for i in imgs if 'alt=""' in i)
    out["links"] = sorted(set(l for l in re.findall(r'href="(/[^"#]*)"', s) if not l.startswith("//")))
    out["size"] = len(s)
    return out

if __name__ == "__main__":
    paths = [l.strip() for l in open(sys.argv[1]) if l.strip()]
    with concurrent.futures.ThreadPoolExecutor(6) as ex:
        res = list(ex.map(check, paths))
    json.dump(res, open(sys.argv[2], "w"), ensure_ascii=False)
    print(len(res), "pages")
