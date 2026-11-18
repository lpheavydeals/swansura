#!/usr/bin/env python3
"""Weekly check: £ prices written into Journal articles vs the live product prices.

Prices are uploaded weekly from the client sheet (column 'Final RRP'), but the Journal
guides name prices in their text, e.g. '<a href="/products/x">Deyga Beetroot Lip Balm</a> (£10.99)'.
This script lists every price in an article that no longer matches the linked product.

Usage (run after each weekly price upload; stdlib only, reads the public storefront):
    python3 tools/shopify/journal_price_check.py [--out docs/seo] [--delay 0.4] [--only handle1,handle2]

How it works:
  1. Article URLs from /sitemap.xml -> sitemap_articles_*.xml (published articles only).
  2. For each article page, only the article text is read: the <article class="abody ..."> blocks
     (the 'Shop the story' cards sit outside them and always show the live price).
  3. For each product link in that text, the £ amounts in the rest of its sentence are compared
     with the product's live variant prices (/products/<handle>.js; redirects followed).
     Amounts after 'over / under / from ... to / spend / off / below / above / than' are
     thresholds (£40 free delivery, £70 + £5 SAVE5, price bands) and are skipped.
  4. Report: <out>/journal_price_check_<date>.csv + .md (article, product, price in text,
     live price(s), in stock, the sentence). Nothing is written to the store.

Fixing a flagged price: change only that bracket in the article body (articleUpdate, body is HTML!),
as done in tools/shopify/kit_price_fix_2026-11-15.py and choc_butter_price_fix_2026-11-16.py.
"""
import argparse, csv, datetime, html, json, os, re, sys, time, urllib.request, urllib.error

BASE = 'https://www.swansura.com'
UA = {'User-Agent': 'Mozilla/5.0 (compatible; price-check)'}
THRESH = re.compile(r'(over|under|below|above|than|spend|off|to|from|upto|up to)\s*$', re.I)
PRICE = re.compile(r'£\s?(\d+(?:\.\d{1,2})?)')
LINK = re.compile(r'<a\s[^>]*href="(?:https://www\.swansura\.com)?/products/([^"?#/]+)[^"]*"[^>]*>(.*?)</a>', re.S)


def get(url, tries=3):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
                return r.read().decode('utf-8', 'replace')
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            time.sleep(3 * (i + 1))
        except Exception:
            time.sleep(3 * (i + 1))
    return None


def article_urls():
    idx = get(BASE + '/sitemap.xml') or ''
    urls = []
    for sm in re.findall(r'<loc>([^<]*sitemap_articles[^<]*)</loc>', idx):
        xml = get(html.unescape(sm)) or ''
        urls += [u for u in re.findall(r'<loc>([^<]+)</loc>', xml) if '/blogs/' in u]
    return urls


def body_text(page):
    """The article text: <article class="abody a1"> (opening section) + <div class="abody a2"> (the rest,
    after the cards). Articles without cards may hold everything in one block. The blocks hold no
    nested div/article, so the first matching close tag ends each one."""
    parts = re.findall(r'<article class="abody[^"]*">(.*?)</article>', page, re.S)
    parts += re.findall(r'<div class="abody[^"]*">(.*?)</div>', page, re.S)
    return '\n'.join(parts)


def plain(s):
    return html.unescape(re.sub(r'<[^>]+>', '', s))


def sentence_after(body, end):
    """Text from the end of a link to the end of its sentence / list item (max ~220 chars)."""
    rest = body[end:end + 600]
    cut = re.search(r'</li>|</p>|</h\d>|<br', rest)
    rest = rest[:cut.start()] if cut else rest
    t = plain(rest)
    m = re.search(r'(?<!\d)\.(\s|$)', t)
    return (t[:m.start() + 1] if m else t)[:220]


_cache = {}
def product(handle):
    if handle not in _cache:
        raw = get(f'{BASE}/products/{handle}.js')
        if raw is None:
            _cache[handle] = None
        else:
            p = json.loads(raw)
            _cache[handle] = {
                'title': p.get('title', ''),
                'prices': sorted({v['price'] / 100 for v in p.get('variants', [])}),
                'available': bool(p.get('available')),
            }
    return _cache[handle]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default='docs/seo')
    ap.add_argument('--delay', type=float, default=0.4)
    ap.add_argument('--only', default='', help='comma-separated article handles')
    a = ap.parse_args()
    only = {h.strip() for h in a.only.split(',') if h.strip()}

    urls = article_urls()
    if only:
        urls = [u for u in urls if u.rstrip('/').rsplit('/', 1)[-1] in only]
    print(f'{len(urls)} articles', file=sys.stderr)

    rows, checked, missing = [], 0, []
    for u in urls:
        page = get(u)
        time.sleep(a.delay)
        if not page:
            missing.append(u)
            continue
        body = body_text(page)
        if not body:
            missing.append(u)
            continue
        art = u.rstrip('/').rsplit('/', 1)[-1]
        for m in LINK.finditer(body):
            handle, label = m.group(1), plain(m.group(2)).strip()
            sent = sentence_after(body, m.end())
            amounts = []
            for pm in PRICE.finditer(sent):
                if THRESH.search(sent[:pm.start()][-14:]):
                    continue
                amounts.append(float(pm.group(1)))
            if not amounts:
                continue
            p = product(handle)
            time.sleep(a.delay)
            checked += 1
            if p is None:
                rows.append([art, handle, label, ' / '.join(f'£{x:.2f}' for x in amounts), 'PRODUCT NOT FOUND', '', sent.strip()])
                continue
            # the first untreated amount after a link is its price; others in the sentence may
            # belong to the next product, so only the first must match
            first = amounts[0]
            if not any(abs(first - x) < 0.005 for x in p['prices']):
                rows.append([art, handle, label, f'£{first:.2f}',
                             ' / '.join(f'£{x:.2f}' for x in p['prices']),
                             'yes' if p['available'] else 'SOLD OUT', sent.strip()])

    day = datetime.date.today().isoformat()
    os.makedirs(a.out, exist_ok=True)
    head = ['article', 'product handle', 'link text', 'price in article', 'live price(s)', 'in stock', 'sentence']
    with open(os.path.join(a.out, f'journal_price_check_{day}.csv'), 'w', newline='') as f:
        csv.writer(f).writerows([head] + rows)
    with open(os.path.join(a.out, f'journal_price_check_{day}.md'), 'w') as f:
        f.write(f'# Journal price check {day}\n\n{len(urls)} articles, {checked} priced product mentions checked, '
                f'{len(rows)} out of date.\n\n')
        if missing:
            f.write('Could not read: ' + ', '.join(missing) + '\n\n')
        for r in rows:
            f.write(f'- **{r[0]}**: {r[2]} — text says {r[3]}, live {r[4]} ({r[5]})\n  > {r[6]}\n')
    print(f'{len(urls)} articles, {checked} priced mentions, {len(rows)} out of date, {len(missing)} unreadable')
    for r in rows:
        print(' | '.join(r[:6]))


if __name__ == '__main__':
    main()
