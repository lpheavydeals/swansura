// Runs the prototype (prototype/index.html, served on :8765) in Chromium and exports, straight from its own code:
// every listing route (membership in the prototype's ranked order, title, H1, intro, eyebrow, FAQs) and the
// derived data per product (type, scent family, for, key ingredients, skin types, notes, studio pick, product FAQs).
// Usage: (cd prototype && python3 -m http.server 8765) & node tools/proto/extract_data.js docs/data/prototype_export.json
const { chromium } = require('playwright'); const fs = require('fs');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('http://localhost:8765/index.html#home', { waitUntil: 'networkidle' });
  await p.waitForFunction(() => typeof P !== 'undefined' && P.length > 500);
  const data = await p.evaluate(() => {
    const out = { listings: {}, products: {}, kw: KW, ranges: Object.fromEntries(Object.entries(RANGES).map(([k, r]) => [k, [r[0], r[1], String(r[2])]])),
      families: FAMILIES, concerns: CONCERNS, cats: Object.fromEntries(Object.entries(CATS).map(([k, c]) => [k, { name: c.name, intro: c.intro, world: c.world, faq: c.faq }])),
      priceBands: PRICE_BANDS, listH1: LIST_H1 };
    const rank = p => (p.available ? 0 : 8) + (isPick(p) ? 0 : 4) + (BR[p.brand]?.partner ? 0 : 2) + (p.compare ? 0 : 1);
    const routes = [];
    Object.keys(CATS).forEach(k => routes.push(['c', k, CATS[k].name, P.filter(p => inCat(p, k))]));
    Object.keys(CONCERNS).forEach(k => routes.push(['concern', k, CONCERNS[k][0], P.filter(p => p.cat !== 'fragrance' && p.tags.includes(k))]));
    PRICE_BANDS.forEach(b => routes.push(['price', b[0], b[1], P.filter(p => inBand(p, b[0]))]));
    KW.forEach(k => routes.push(['k', k.s, k.k, kwList(k)]));
    Object.keys(RANGES).forEach(k => routes.push(['range', k, RANGES[k][0] + ' range', rangeList(k)]));
    Object.keys(FAMILIES).forEach(k => routes.push(['scent', k, FAMILIES[k][0] + ' fragrances', P.filter(p => p.cat === 'fragrance' && family(p) === k)]));
    for (const [kind, key, title, list] of routes) {
      const sorted = [...list].sort((a, b) => rank(a) - rank(b));
      const k = kind === 'k' ? KWBY[key] : null;
      const base = kind === 'c' ? (CATS[key].faq || []) : k ? (k.faq || []) : [];
      let faq = []; try { const auto = listingFaq(kind, key, title, sorted); faq = auto.length ? auto : topUpFaq(base, sorted); } catch (e) {}
      out.listings[kind + '-' + key] = { kind, key, title, h1: LIST_H1[kind + '-' + key] || title, ids: sorted.map(p => p.id),
        live: kind === 'k' ? kwLive().some(x => x.s === key) : true, grp: k ? k.grp : null, d: k ? k.d : null, faq, faqTitle: title + ' questions' };
    }
    for (const x of P) {
      let pf = [];
      out.products[x.id] = { sub: subtype(x), fam: x.cat === 'fragrance' ? family(x) : null, for: x.cat === 'fragrance' ? forWho(x) : null,
        ings: ingsOf(x).map(i => i[1]), skin: skinTypes(x), pick: isPick(x), concerns: x.tags.filter(t => CONCERNS[t]), tags: x.tags, cat: x.cat,
        notes: (() => { try { return notes(x); } catch (e) { return null; } })(),
        faq: (() => { const d = document.createElement('div'); d.innerHTML = productPage(x.id); return [...d.querySelectorAll('.pfaq details')].map(e => [e.querySelector('summary').textContent, e.querySelector('p').textContent]); })() };
    }
    out.brands = Object.fromEntries(Object.entries(BR).map(([name, B]) => [name, { ...B, h1: (() => { try { return brandH1(name, B.slug); } catch (e) { return null; } })(), faq: (() => { try { return brandFaq(name); } catch (e) { return []; } })() }]));
    out.rituals = ritualsData(); out.ritualGroups = RITUAL_GROUPS; out.journal = JOURNAL; out.advent = ADVENT; out.offers = OFFERS;
    return out;
  });
  // Page header as rendered (eyebrow + intro line) for every listing route.
  for (const r of Object.keys(data.listings)) {
    await p.evaluate(r => { location.hash = r; }, r);
    await p.waitForFunction(r => document.querySelector('.pagehead h1') && location.hash === '#' + r, r);
    Object.assign(data.listings[r], await p.evaluate(() => ({
      eyebrow: document.querySelector('.pagehead .eyebrow')?.textContent.trim() || '',
      intro: document.querySelector('.pagehead .lede')?.textContent.trim() || '' })));
  }
  fs.writeFileSync(process.argv[2], JSON.stringify(data));
  console.log(Object.keys(data.listings).length, 'listings', Object.keys(data.products).length, 'products');
  await b.close();
})();
