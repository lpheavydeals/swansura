#!/usr/bin/env python3
"""Cut-out roll-out for SKINCARE brands (galleries that are mostly graphics).

Unlike cutout_batch.py (which re-uploads the whole gallery), this only uploads the cut-outs,
puts each one in the place of the photo it replaces and detaches just those originals.
Graphics / kept photos are not touched (same media id, same alt, same position).

Run cutout_batch.py `final <root> <slug>` first (it fills gallery.json: im.out / im.new_alt).

  stage <root> <slug>              -> <slug>/stage_cut.json   (stagedUploadsCreate input, cut-outs only)
     then: stage_images.py post <slug>/final/*-cutout.webp > <slug>/posted.json
  mut <root> <slug>                -> <slug>/mutc*.graphql     (productUpdate adding the cut-outs)
  plan <root> <slug> <admin.json>  -> <slug>/reorder.graphql, relink.graphql, detach.json (+ backup in docs/backups)
  check <root> <slug> [collection] -> live PDP check (replaced originals gone, no empty alt, no sideways scroll)
"""
import json, os, subprocess, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import cutout_batch as cb  # noqa: E402

REPO = Path(__file__).resolve().parents[2]
DATE = '2026-11-11'


def cut_items(G):
    for g in G:
        for im in g['images']:
            if im.get('out') and im['out'].endswith('-cutout.webp'):
                yield g, im


def stage(root, slug):
    d = root / slug
    G = cb.gallery(root, slug)
    L = [{"resource": "IMAGE", "filename": im['out'], "mimeType": "image/webp", "httpMethod": "POST",
          "fileSize": str((d / 'final' / im['out']).stat().st_size)} for g, im in cut_items(G)]
    json.dump({'input': L}, open(d / 'stage_cut.json', 'w'))
    print(len(L), 'cut-outs ->', d / 'stage_cut.json')


def mut(root, slug):
    d = root / slug
    P = {os.path.basename(p['file']): p for p in json.load(open(d / 'posted.json'))}
    bad = [k for k, p in P.items() if p.get('code') != '201']
    if bad:
        sys.exit(f'POST failed: {bad}')
    G = cb.gallery(root, slug)
    parts = []
    for g in G:
        ims = [im for gg, im in cut_items([g])]
        if not ims:
            continue
        m = ','.join('{mediaContentType:IMAGE, originalSource:%s, alt:%s}' % (
            json.dumps(P[im['out']]['resourceUrl']), json.dumps(im['new_alt'], ensure_ascii=False)) for im in ims)
        parts.append(f'{slug[:3]}{len(parts)}: productUpdate(product:{{id:"gid://shopify/Product/{g["id"]}"}}, media:[{m}]){{ userErrors{{field message}} }}')
    for f in d.glob('mutc*.graphql'):
        f.unlink()
    k, cur = 0, []
    for p in parts + [None]:
        if p is None or (cur and sum(len(x) for x in cur) + len(p) > 15000):
            if cur:
                (d / f'mutc{k}.graphql').write_text('mutation{\n' + '\n'.join(cur) + '\n}')
                k += 1
            cur = []
        if p:
            cur.append(p)
    print(k, 'mutation files', [len((d / f'mutc{i}.graphql').read_text()) for i in range(k)], len(parts), 'products')


def plan(root, slug, path):
    d = root / slug
    raw = json.load(open(path))
    nodes = raw.get('data', raw)['products']['nodes']
    A = {n['id'].rsplit('/', 1)[-1]: n for n in nodes}
    G = cb.gallery(root, slug)
    reorder, relink, detach, problems = [], [], [], []
    for g in G:
        ims = [im for gg, im in cut_items([g])]
        if not ims:
            continue
        a = A.get(str(g['id']))
        if not a:
            problems.append(f"{g['handle']}: not in admin listing")
            continue
        media = [(m['id'], cb.fname(m['image']['url']) if m.get('image') else '', m.get('status'), m.get('createdAt') or '')
                 for m in a['media']['nodes']]
        repl = {}  # old media id -> new media id
        olds = []
        for im in ims:
            old = next((mid for mid, nm, st, c in media if nm == im['src']), None) or next(
                (mid for mid, nm, st, c in media if nm.rsplit('.', 1)[0].startswith(im['src'].rsplit('.', 1)[0]) and 'cutout' not in nm), None)
            if not old:
                problems.append(f"{g['handle']} photo {im['n']}: original {im['src']} not found")
            olds.append(old)
        # new cut-outs: media added today, in upload order (Shopify truncates very long file names, so match by order)
        known = {im['src'] for im in g['images']}
        altof = {m['id']: m.get('alt') for m in a['media']['nodes']}
        newm = [(mid, st) for mid, nm, st, c in media if c.startswith(DATE) and nm not in known]
        if len(newm) != len(ims):
            problems.append(f"{g['handle']}: {len(newm)} new media vs {len(ims)} cut-outs")
            continue
        for im, old, (nid, st) in zip(ims, olds, newm):
            if not old:
                continue
            if st != 'READY':
                problems.append(f"{g['handle']} photo {im['n']}: new media {st}")
                continue
            if altof.get(nid) != im['new_alt']:
                problems.append(f"{g['handle']} photo {im['n']}: new media alt does not match (pairing off)")
                continue
            repl[old] = nid
            im['media'], im['new_media'] = old, nid
            detach.append({'product': a['id'], 'media': old, 'src': im['src'], 'alt': im['alt']})
        newids = set(repl.values())
        order = [repl.get(mid, mid) for mid, nm, st, c in media if mid not in newids]
        reorder.append((a['id'], order))
        for v in a['variants']['nodes']:
            for vm in v['media']['nodes']:
                if vm['id'] in repl:
                    relink.append({'product': a['id'], 'variant': v['id'], 'old': vm['id'], 'new': repl[vm['id']]})
    if problems:
        print('\n'.join(problems))
        sys.exit('STOP: fix the problems above (wait for READY and re-run the Admin query)')
    json.dump(G, open(d / 'gallery.json', 'w'), indent=1, ensure_ascii=False)
    # reorder in chunks of ~15k characters
    parts = []
    for i, (pid, order) in enumerate(reorder):
        mv = ','.join('{id:"%s",newPosition:"%d"}' % (mid, k) for k, mid in enumerate(order))
        parts.append(f'r{i}: productReorderMedia(id:"{pid}", moves:[{mv}]){{ mediaUserErrors{{field message}} }}')
    for f in d.glob('reorder*.graphql'):
        f.unlink()
    k, cur = 0, []
    for p in parts + [None]:
        if p is None or (cur and sum(len(x) for x in cur) + len(p) > 15000):
            if cur:
                (d / f'reorder{k}.graphql').write_text('mutation{\n' + '\n'.join(cur) + '\n}')
                k += 1
            cur = []
        if p:
            cur.append(p)
    rl, byp = '', {}
    for r in relink:
        byp.setdefault(r['product'], []).append(r)
    for i, (pid, rs) in enumerate(byp.items()):
        dv = ','.join('{variantId:"%s", mediaIds:["%s"]}' % (r['variant'], r['old']) for r in rs)
        av = ','.join('{variantId:"%s", mediaIds:["%s"]}' % (r['variant'], r['new']) for r in rs)
        rl += (f'd{i}: productVariantDetachMedia(productId:"{pid}", variantMedia:[{dv}]){{ userErrors{{message}} }}\n'
               f'a{i}: productVariantAppendMedia(productId:"{pid}", variantMedia:[{av}]){{ userErrors{{message}} }}\n')
    (d / 'relink.graphql').write_text('mutation{\n' + rl + '}' if rl else '')
    json.dump({'f': [{'id': x['media'], 'referencesToRemove': [x['product']]} for x in detach]},
              open(d / 'detach.json', 'w'), separators=(',', ':'))
    B = {'note': (f"Skincare cut-out roll-out {DATE}: only the photos classified 'cut' were replaced; graphics untouched. "
                  "Undo: fileUpdate referencesToAdd the 'detached' originals back, detach media whose file ends -cutout.webp, "
                  "restore 'variant_links' (old) and the original order (gallery pos)."),
         'picks': json.load(open(d / 'picks.json')), 'detached': detach, 'variant_links': relink, 'gallery': G}
    out = REPO / f'docs/backups/{slug}_cutout_before_{DATE}.json'
    json.dump(B, open(out, 'w'), indent=1, ensure_ascii=False)
    print(len(detach), 'to detach;', len(reorder), 'products to reorder in', k, 'files;', len(relink), 'variant links; backup', out)


def check(root, slug, coll=''):
    d = root / slug
    G = cb.gallery(root, slug)
    hs = sorted({g['handle'] for g, im in cut_items(G)})
    olds = {h: [im['src'].rsplit('.', 1)[0] + '.' for g, im in cut_items(G) if g['handle'] == h] for h in hs}
    js = d / 'check_skin.js'
    js.write_text("""
const {chromium}=require('playwright');
const hs=%s, olds=%s, coll=%s;
(async()=>{const b=await chromium.launch(); let bad=0;
for(const vp of [{width:1366,height:900},{width:390,height:844}]){
 const ctx=await b.newContext({viewport:vp,userAgent:'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'});
 const p=await ctx.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
 for(const h of hs){ await p.goto('https://www.swansura.com/products/'+h+'?cb='+Date.now(),{waitUntil:'domcontentloaded',timeout:45000}).catch(()=>{});
  await p.waitForTimeout(1500);
  const r=await p.evaluate(([olds])=>({cut:[...document.querySelectorAll('img')].filter(i=>/-cutout/.test(i.currentSrc||i.src)).length,
    old:[...document.querySelectorAll('img')].filter(i=>olds.some(o=>(i.currentSrc||i.src).includes('/files/'+o))).length,
    empty:[...document.querySelectorAll('img')].filter(i=>i.getAttribute('alt')==='').length,sw:document.documentElement.scrollWidth,vw:innerWidth,t:document.title}),[olds[h]]);
  const ok=r.cut>0&&r.old===0&&r.empty===0&&r.sw<=r.vw&&!/Just a moment/.test(r.t);
  if(!ok){bad++;console.log('FAIL',vp.width,h,JSON.stringify(r));}
 }
 if(coll){await p.goto('https://www.swansura.com/collections/'+coll,{waitUntil:'domcontentloaded',timeout:45000}).catch(()=>{});
  await p.waitForTimeout(2500);
  console.log('brand page',vp.width,JSON.stringify(await p.evaluate(()=>({cut:[...document.querySelectorAll('img')].filter(i=>/-cutout/.test(i.src)).length,sw:document.documentElement.scrollWidth,vw:innerWidth}))));}
 console.log(vp.width,'js errors',JSON.stringify(errs.slice(0,3))); await ctx.close();}
console.log(bad?('FAILED '+bad):'ALL OK', hs.length,'products x 2 widths'); await b.close();})();
""" % (json.dumps(hs), json.dumps(olds), json.dumps(coll)))
    subprocess.run(['node', str(js)], check=False)


if __name__ == '__main__':
    cmd, root, slug = sys.argv[1], Path(sys.argv[2]), sys.argv[3]
    if cmd == 'stage':
        stage(root, slug)
    elif cmd == 'mut':
        mut(root, slug)
    elif cmd == 'plan':
        plan(root, slug, sys.argv[4])
    elif cmd == 'check':
        check(root, slug, sys.argv[4] if len(sys.argv) > 4 else '')
