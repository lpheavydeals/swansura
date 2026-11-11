"""Cut-out photo roll-out for all remaining brands (user, 10 Nov 2026, overnight: 'do all the remaining ... fragrances,
then the skincare brands'). Same result as the per-brand runs (Mugler ... Tom Ford): every gallery photo of a product
replaced by <handle>-NN-cutout.webp on a transparent canvas (theme paints #EEF3F0), same order, alt text kept
(' on a white background' dropped), originals DETACHED (fileUpdate referencesToRemove), never deleted.

Work dir per brand: <root>/<slug>/  (root = scratchpad/cutout/all)

  scan  <root>                      storefront /products.json -> <root>/all.json + <root>/queue.json (brands with
                                    photos that are not cut-outs; fragrance first, skincare last)
  prep  <root> <vendor>             <slug>/in/*.webp (originals, PNG/JPG converted), gallery.json, backup copy in
                                    docs/backups/<slug>_originals_<date>/
  sheet <root> <slug>               review sheets <slug>/sheetN.jpg: numbered photo | birefnet [| isnet | flood]
  redo  <root> <slug> flood|isnet N [N...]   run the fallback method on photo numbers N (isnet takes a file lock)
  final <root> <slug>               reads <slug>/picks.json, builds <slug>/final/ + stage input <slug>/stage_in.json
        picks.json = {"default": "bire", "pick": {"N": "isnet|flood|keep|drop"}, "alt": {"N": "new alt"},
                      "skip_products": ["handle", ...], "notes": "..."}
        keep = no cut-out (designed graphic / infographic / text panel): the original is re-uploaded unchanged as
               <handle>-NN-photo.webp so the gallery order stays; drop = left out.
  mut   <root> <slug>               after `stage_images.py post` -> posted.json: writes mutN.graphql (productUpdate
                                    media batches, <= 9,000 chars each)
  admin <root> <slug> <file>        save the Admin media listing (raw GraphQL JSON of
                                    products(query:"vendor:'X'"){nodes{id handle media(first:50){nodes{id status
                                    ... on MediaImage{image{url}}}} variants(first:50){nodes{id media(first:5){nodes{id}}}}}})
                                    taken AFTER the upload; writes detach.graphql, relink.graphql (variants that
                                    pointed at an original -> the new media at the same position) and the backup/undo
                                    docs/backups/<slug>_cutout_before_<date>.json. Refuses if any new media is not READY.
  check <root> <slug>               live check (Playwright): every PDP of the brand shows only new files, 0 empty alts,
                                    no sideways scroll at 1366 + 390; brand page screenshot -> <slug>/live_*.png
"""
import json, os, re, sys, shutil, subprocess, urllib.request, time, pathlib, datetime
from PIL import Image

REPO = pathlib.Path(__file__).resolve().parents[2]
TOOLS = REPO / 'tools/shopify'
DATE = datetime.date.today().isoformat()
SKIN = {'Vilvah', 'Deyga', 'anatomē', 'Highborn London', 'Shiseido', 'Swansura - The Body Studio'}
SKIP_HANDLES = {'tom-ford-oud-wood-eau-de-parfum-50ml-unisex-1'}   # photos show Velvet Orchid (client to decide)
UA = {'User-Agent': 'Mozilla/5.0 (cutout-batch)'}


def get(url, tries=4):
    for k in range(tries):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()
        except Exception:
            if k == tries - 1:
                raise
            time.sleep(3 * (k + 1))


def slugify(v):
    s = v.lower().replace('ē', 'e').replace('é', 'e').replace('è', 'e').replace('ô', 'o').replace('&', 'and')
    return re.sub(r'[^a-z0-9]+', '_', s).strip('_')


def is_cut(src):
    return 'cutout' in src.rsplit('/', 1)[-1]


def scan(root):
    root.mkdir(parents=True, exist_ok=True)
    allp = []
    for pg in range(1, 20):
        P = json.loads(get(f'https://www.swansura.com/products.json?limit=250&page={pg}'))['products']
        if not P:
            break
        allp += P
    json.dump(allp, open(root / 'all.json', 'w'))
    by = {}
    for p in allp:
        if p['handle'] in SKIP_HANDLES or not p['images'] or all(is_cut(i['src']) for i in p['images']):
            continue
        b = by.setdefault(p['vendor'], {'vendor': p['vendor'], 'slug': slugify(p['vendor']), 'products': 0, 'photos': 0})
        b['products'] += 1
        b['photos'] += len(p['images'])
    q = sorted(by.values(), key=lambda b: (b['vendor'] in SKIN, -b['photos']))
    json.dump(q, open(root / 'queue.json', 'w'), indent=1, ensure_ascii=False)
    print(len(allp), 'products;', len(q), 'brands;', sum(b['photos'] for b in q), 'photos')


def prep(root, vendor):
    allp = json.load(open(root / 'all.json'))
    slug = slugify(vendor)
    d = root / slug
    (d / 'in').mkdir(parents=True, exist_ok=True)
    bk = REPO / f'docs/backups/{slug}_originals_{DATE}'
    bk.mkdir(parents=True, exist_ok=True)
    G = []
    n = 0
    for p in allp:
        if p['vendor'] != vendor or p['handle'] in SKIP_HANDLES or not p['images'] or all(is_cut(i['src']) for i in p['images']):
            continue
        # alt text is only in /products/<handle>.json
        full = json.loads(get(f"https://www.swansura.com/products/{p['handle']}.json"))['product']
        ims = []
        for k, im in enumerate(full['images'], 1):
            n += 1
            src = im['src'].split('?')[0]
            fn = f"{p['handle']}-{k:02d}.webp"
            if not (d / 'in' / fn).exists():
                raw = get(im['src'])
                tmp = d / 'tmp.bin'
                tmp.write_bytes(raw)
                img = Image.open(tmp)
                img = img.convert('RGBA') if img.mode in ('RGBA', 'LA', 'P') else img.convert('RGB')
                if src.lower().endswith('.webp'):
                    shutil.copy(tmp, d / 'in' / fn)
                else:
                    img.save(d / 'in' / fn, 'WEBP', quality=92)
                tmp.unlink()
            shutil.copy(d / 'in' / fn, bk / fn)
            alt = im.get('alt') or ''
            ims.append({'n': n, 'pos': k, 'src': src.rsplit('/', 1)[-1], 'in': fn, 'alt': alt,
                        'new_alt': alt.replace(' on a white background', '').strip(),
                        'variant_ids': im.get('variant_ids') or []})
        G.append({'handle': p['handle'], 'id': p['id'], 'title': p['title'], 'images': ims})
        time.sleep(0.2)
    json.dump(G, open(d / 'gallery.json', 'w'), indent=1, ensure_ascii=False)
    print(slug, len(G), 'products', n, 'photos')


def gallery(root, slug):
    return json.load(open(root / slug / 'gallery.json'))


def photos(root, slug):
    return [(g, im) for g in gallery(root, slug) for im in g['images']]


def cutpath(d, method, im):
    return d / method / (im['in'][:-5] + '-cutout.webp')


def sheet(root, slug):
    from PIL import ImageDraw
    d = root / slug
    rows = photos(root, slug)
    W, H, PER = 300, 375, 3
    cols = ['in', 'bire', 'isnet', 'flood']
    for s in range(0, len(rows), 18):
        ch = rows[s:s + 18]
        used = [c for c in cols if c == 'in' or any(cutpath(d, c, im).exists() for _, im in ch)]
        tw = W * len(used)
        nr = (len(ch) + PER - 1) // PER
        S = Image.new('RGB', (tw * PER, H * nr), 'white')
        dr = ImageDraw.Draw(S)
        for k, (g, im) in enumerate(ch):
            x0, y0 = (k % PER) * tw, (k // PER) * H
            for c, col in enumerate(used):
                p = d / 'in' / im['in'] if col == 'in' else cutpath(d, col, im)
                if not p.exists():
                    continue
                t = Image.open(p).convert('RGBA')
                bg = Image.new('RGBA', t.size, (238, 243, 240, 255) if col != 'in' else (255, 255, 255, 255))
                bg.alpha_composite(t)
                t = bg.convert('RGB')
                t.thumbnail((W - 6, H - 6))
                S.paste(t, (x0 + c * W + 3, y0 + 3))
            dr.rectangle((x0, y0, x0 + 46, y0 + 22), fill='black')
            dr.text((x0 + 5, y0 + 5), str(im['n']), fill='white')
            dr.line((x0 + tw - 1, y0, x0 + tw - 1, y0 + H), fill='#999', width=3)
        S.save(d / f'sheet{s // 18}.jpg', quality=84)
        print(d / f'sheet{s // 18}.jpg', 'photos', ch[0][1]['n'], '-', ch[-1][1]['n'], 'columns', used)


def redo(root, slug, method, nums):
    d = root / slug
    want = {int(x) for x in nums}
    tmp = d / f'redo_{method}'
    if tmp.exists():
        shutil.rmtree(tmp)
    tmp.mkdir()
    for g, im in photos(root, slug):
        if im['n'] in want:
            shutil.copy(d / 'in' / im['in'], tmp / im['in'])
    out = d / method
    if method == 'flood':
        cmd = ['python3', str(TOOLS / 'cutout_flood.py'), str(tmp), str(out)]
    else:
        cmd = ['flock', str(root / 'model.lock'), 'python3', str(TOOLS / 'cutout_photos.py'), str(tmp), str(out),
               '#EEF3F0', 'isnet-general-use']
        for f in tmp.iterdir():                       # force a fresh run for these
            (out / (f.stem + '-cutout.webp')).unlink(missing_ok=True)
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL)
    print('done', sorted(want))


def final(root, slug):
    d = root / slug
    pk = json.load(open(d / 'picks.json'))
    default = pk.get('default', 'bire')
    pick = {int(k): v for k, v in pk.get('pick', {}).items()}
    alts = {int(k): v for k, v in pk.get('alt', {}).items()}
    skip = set(pk.get('skip_products', []))
    if (d / 'classify.json').exists():          # skincare: photos not classified 'cut' stay as they are ('keep')
        cl = json.load(open(d / 'classify.json'))
        cutset = {int(x) for x in cl['cut']}
        for g0, im0 in photos(root, slug):
            if im0['n'] not in cutset:
                pick.setdefault(im0['n'], 'keep')
    if (d / 'final').exists():
        shutil.rmtree(d / 'final')
    (d / 'final').mkdir()
    G = gallery(root, slug)
    for g in G:
        g['skip'] = g['handle'] in skip
        for im in g['images']:
            m = pick.get(im['n'], default)
            im['method'] = m
            if im['n'] in alts:
                im['new_alt'] = alts[im['n']]
            if g['skip'] or m == 'drop':
                im['out'] = None
                continue
            base = f"{g['handle']}-{im['pos']:02d}"
            if m == 'keep':
                im['out'] = base + '-photo.webp'
                shutil.copy(d / 'in' / im['in'], d / 'final' / im['out'])
            else:
                src = cutpath(d, m, im)
                if not src.exists():
                    sys.exit(f'missing {m} result for photo {im["n"]} ({src.name})')
                im['out'] = base + '-cutout.webp'
                shutil.copy(src, d / 'final' / im['out'])
            if not im['new_alt']:
                sys.exit(f'empty alt for photo {im["n"]}: set one in picks.json "alt"')
        if not g['skip'] and not any(im['out'] for im in g['images']):
            sys.exit(f"{g['handle']}: every photo dropped; skip the product instead")
    json.dump(G, open(d / 'gallery.json', 'w'), indent=1, ensure_ascii=False)
    files = sorted((d / 'final').iterdir())
    json.dump([{"resource": "IMAGE", "filename": f.name, "mimeType": "image/webp", "httpMethod": "POST",
                "fileSize": str(f.stat().st_size)} for f in files], open(d / 'stage_in.json', 'w'))
    print(len(files), 'files in final/; stage input', d / 'stage_in.json')


def mut(root, slug):
    d = root / slug
    P = {os.path.basename(p['file']): p for p in json.load(open(d / 'posted.json'))}
    bad = [k for k, p in P.items() if p.get('code') != '201']
    if bad:
        sys.exit(f'POST failed: {bad}')
    parts = []
    for g in gallery(root, slug):
        if g['skip']:
            continue
        m = ','.join('{mediaContentType:IMAGE, originalSource:%s, alt:%s}' % (
            json.dumps(P[im['out']]['resourceUrl']), json.dumps(im['new_alt'], ensure_ascii=False))
            for im in g['images'] if im['out'])
        parts.append(f'p{len(parts)}: productUpdate(product:{{id:"gid://shopify/Product/{g["id"]}"}}, media:[{m}]){{ userErrors{{field message}} }}')
    for f in d.glob('mut*.graphql'):
        f.unlink()
    k, cur = 0, []
    for p in parts:
        if cur and sum(len(x) for x in cur) + len(p) > 15000:
            (d / f'mut{k}.graphql').write_text('mutation{\n' + '\n'.join(cur) + '\n}')
            k, cur = k + 1, []
        cur.append(p)
    if cur:
        (d / f'mut{k}.graphql').write_text('mutation{\n' + '\n'.join(cur) + '\n}')
        k += 1
    print(k, 'mutation files', [len((d / f'mut{i}.graphql').read_text()) for i in range(k)])


def fname(url):
    return url.split('?')[0].rsplit('/', 1)[-1]


def admin(root, slug, path):
    d = root / slug
    raw = json.load(open(path))
    if isinstance(raw, list) and raw and isinstance(raw[0], dict) and 'text' in raw[0]:
        raw = json.loads(raw[0]['text'])
    nodes = raw.get('data', raw)['products']['nodes']
    A = {n['id'].rsplit('/', 1)[-1]: n for n in nodes}
    G = gallery(root, slug)
    detach, relink, problems = [], [], []
    for g in G:
        if g['skip']:
            continue
        a = A.get(str(g['id']))
        if not a:
            problems.append(f"{g['handle']}: not in admin listing")
            continue
        media = [(m['id'], fname(m['image']['url']) if m.get('image') else '', m.get('status')) for m in a['media']['nodes']]
        by_name = {nm: (mid, st) for mid, nm, st in media}
        new = {}
        for im in g['images']:
            # originals: match by file name (Shopify may add a _<uuid> suffix to duplicates, so also try prefix)
            hit = by_name.get(im['src']) or next(((mid, st) for mid, nm, st in media
                                                  if nm.rsplit('.', 1)[0].startswith(im['src'].rsplit('.', 1)[0])
                                                  and 'cutout' not in nm and not nm.endswith('-photo.webp')), None)
            if not hit:
                problems.append(f"{g['handle']} photo {im['n']}: original {im['src']} not found")
            else:
                im['media'] = hit[0]
                detach.append({'product': f"gid://shopify/Product/{g['id']}", 'media': hit[0], 'src': im['src'], 'alt': im['alt']})
            if im['out']:
                o = next(((mid, st) for mid, nm, st in media if nm.rsplit('.', 1)[0].startswith(im['out'].rsplit('.', 1)[0])), None)
                if not o:
                    problems.append(f"{g['handle']} photo {im['n']}: new file {im['out']} not attached")
                elif o[1] != 'READY':
                    problems.append(f"{g['handle']} photo {im['n']}: {im['out']} status {o[1]}")
                else:
                    im['new_media'] = o[0]
                    new[im['pos']] = o[0]
        for v in a['variants']['nodes']:
            for vm in v['media']['nodes']:
                old = next((im for im in g['images'] if im.get('media') == vm['id']), None)
                if old is None:
                    continue
                target = new.get(old['pos']) or next(iter(new.values()), None)
                relink.append({'product': a['id'], 'variant': v['id'], 'old': vm['id'], 'new': target})
    if problems:
        print('\n'.join(problems))
        sys.exit('STOP: fix the problems above (wait for READY and re-run the Admin query)')
    json.dump(G, open(d / 'gallery.json', 'w'), indent=1, ensure_ascii=False)
    s = ','.join('{id:"%s", referencesToRemove:["%s"]}' % (x['media'], x['product']) for x in detach)
    (d / 'detach.graphql').write_text('mutation{ fileUpdate(files:[' + s + ']){ files{id} userErrors{field message} } }')
    rl = ''
    byp = {}
    for r in relink:
        byp.setdefault(r['product'], []).append(r)
    for k, (pid, rs) in enumerate(byp.items()):
        dv = ','.join('{variantId:"%s", mediaIds:["%s"]}' % (r['variant'], r['old']) for r in rs)
        av = ','.join('{variantId:"%s", mediaIds:["%s"]}' % (r['variant'], r['new']) for r in rs)
        rl += (f'd{k}: productVariantDetachMedia(productId:"{pid}", variantMedia:[{dv}]){{ userErrors{{message}} }}\n'
               f'a{k}: productVariantAppendMedia(productId:"{pid}", variantMedia:[{av}]){{ userErrors{{message}} }}\n')
    (d / 'relink.graphql').write_text('mutation{\n' + rl + '}' if rl else '')
    pk = json.load(open(d / 'picks.json'))
    B = {'note': (f"Cut-out roll-out {DATE}. Undo: fileUpdate referencesToAdd the 'detached' originals back to their product, "
                  "detach media whose file ends -cutout.webp or -photo.webp, and restore 'variant_links' (old)."),
         'picks': pk, 'detached': detach, 'variant_links': relink, 'gallery': G}
    out = REPO / f'docs/backups/{slug}_cutout_before_{DATE}.json'
    json.dump(B, open(out, 'w'), indent=1, ensure_ascii=False)
    print(len(detach), 'to detach;', len(relink), 'variant links;', 'relink.graphql' if rl else 'no relink needed', '; backup', out)


def check(root, slug):
    d = root / slug
    G = [g for g in gallery(root, slug) if not g['skip']]
    vendor = next((b['vendor'] for b in json.load(open(root / 'queue.json')) if b['slug'] == slug), slug)
    js = d / 'check.js'
    js.write_text("""
const {chromium}=require('playwright');
const hs=%s, coll=%s, dir=%s, olds=%s;
(async()=>{const b=await chromium.launch(); let bad=0;
for(const [w,vp] of [[1366,{width:1366,height:900}],[390,{width:390,height:844}]]){
 const ctx=await b.newContext({viewport:vp,userAgent:'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'});
 const p=await ctx.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
 for(const h of hs){ await p.goto('https://www.swansura.com/products/'+h+'?cb='+Date.now(),{waitUntil:'domcontentloaded',timeout:45000}).catch(()=>{});
  await p.waitForTimeout(1800);
  const r=await p.evaluate(([h,olds])=>{const g=[...document.querySelectorAll('img')].filter(i=>(i.currentSrc||i.src).includes('/files/'+h+'-'));
    const main=document.querySelector('#mainImg img')||document.querySelector('img#mainImg');
    const old=[...document.querySelectorAll('img')].filter(i=>olds.some(o=>(i.currentSrc||i.src).includes('/files/'+o))).length;
    return {imgs:g.length,old:old,mainOk:!main||/-(cutout|photo)/.test(main.src),
      empty:[...document.querySelectorAll('img')].filter(i=>i.getAttribute('alt')==='').length,sw:document.documentElement.scrollWidth,vw:innerWidth,t:document.title}},[h,olds[h]]);
  const ok=r.old===0&&r.mainOk&&r.empty===0&&r.sw<=r.vw&&!/Just a moment/.test(r.t);
  if(!ok){bad++;console.log('FAIL',w,h,JSON.stringify(r));}
 }
 if(coll){await p.goto('https://www.swansura.com/collections/'+coll,{waitUntil:'domcontentloaded',timeout:45000}).catch(()=>{});
  await p.waitForTimeout(2500); await p.screenshot({path:dir+'/live_'+w+'.png'});
  const r=await p.evaluate(()=>({cut:[...document.querySelectorAll('img.pic')].filter(i=>/-(cutout)/.test(i.src)).length,empty:[...document.querySelectorAll('img')].filter(i=>i.getAttribute('alt')==='').length,sw:document.documentElement.scrollWidth,vw:innerWidth}));
  console.log('brand page',w,JSON.stringify(r));}
 console.log(w,'js errors',JSON.stringify(errs.slice(0,3)));
 await ctx.close();}
console.log(bad?('FAILED '+bad):'ALL OK', hs.length,'products x 2 widths'); await b.close();})();
""" % (json.dumps([g['handle'] for g in G]), json.dumps(sys.argv[4] if len(sys.argv) > 4 else ''), json.dumps(str(d)), json.dumps({g['handle']: [im['src'].rsplit('.', 1)[0] + '.' for im in g['images']] for g in G})))
    subprocess.run(['node', str(js)], check=False)


if __name__ == '__main__':
    cmd, root = sys.argv[1], pathlib.Path(sys.argv[2])
    if cmd == 'scan':
        scan(root)
    elif cmd == 'prep':
        prep(root, sys.argv[3])
    elif cmd == 'sheet':
        sheet(root, sys.argv[3])
    elif cmd == 'redo':
        redo(root, sys.argv[3], sys.argv[4], sys.argv[5:])
    elif cmd == 'final':
        final(root, sys.argv[3])
    elif cmd == 'mut':
        mut(root, sys.argv[3])
    elif cmd == 'admin':
        admin(root, sys.argv[3], sys.argv[4])
    elif cmd == 'check':
        check(root, sys.argv[3])
