// Export per-product PDP data computed by the prototype's own functions (productPage() in prototype/index.html).
// Serve prototype/ on :8765 first. node tools/proto/export_pdp.js OUT.json
const { chromium } = require('playwright');
const out = process.argv[2];
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('http://localhost:8765/#home', { waitUntil: 'networkidle' }); await p.waitForTimeout(1500);
  const data = await p.evaluate(() => {
    const R = {};
    for (const x of P) {
      const sameBrand = P.filter(y => y.brand === x.brand && y.id !== x.id && y.available);
      const sameCat = P.filter(y => y.cat === x.cat && y.brand !== x.brand && y.available);
      let pair;
      if (x.cat === 'fragrance') pair = [findP(/body butter/i, 'Deyga'), findP(/pillow spray/i)].filter(y => y && y.id !== x.id);
      else pair = sameBrand.filter(y => y.cat === x.cat).slice(0, 2);
      if (pair.length < 2) pair = [...pair, ...sameBrand].filter((y, i, a) => a.indexOf(y) === i).slice(0, 2);
      const bl = bullets(x), pr = paras(x);
      const howTo = bl.filter(y => /apply|massage|spray|rinse|before use|after|daily|how to use/i.test(y));
      const benefit = x.cat === 'fragrance' ? ((pr[0] || '').split('. ')[0] + '.').replace(/^\.$/, '') : (bl[0] || pr[0] || '').replace(/^[^:]{0,40}:\s*/, '');
      const short = summary(benefit);
      const similar = (x.cat === 'fragrance' ? sameCat.filter(y => family(y) === family(x)).concat(sameCat) : sameCat).filter((y, i, a) => a.indexOf(y) === i).slice(0, 4);
      const ks = kwFor(x);
      R[x.id] = { cat: x.cat, ben: short, more: benefit.length > short.length, chips: chipsOf(x), pair: pair.map(y => y.id), sim: similar.map(y => y.id),
        how: howTo, kw: ks.slice(0, 8).map(k => [k.k, 'k-' + k.s]), sb: sameBrand.slice(0, 4).map(y => y.id) };
    }
    return R;
  });
  require('fs').writeFileSync(out, JSON.stringify(data));
  console.log(Object.keys(data).length, 'products');
  await b.close();
})();
