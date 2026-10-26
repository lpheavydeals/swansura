// Journeys on the ported product / listing / advent / wishlist pages of the draft theme.
// node tools/qa/proto_journey2.js THEME_ID
const { chromium } = require('playwright');
const curlRoute = require('./curl_route.js'); // pages via curl while Shopify's bot check blocks the browser
const theme = process.argv[2];
const PDP = '/products/milk-drops-brightening-serum-40-ml-rice-milk-alpha-arbutin-skin-brightening-treatment-for-dark-spots-uneven-skin-tone';
const KIT = '/products/vilvah-goat-milk-hair-kit';
(async () => {
  const b = await chromium.launch(); const res = [];
  const ok = (n, v, extra = '') => { const l = `${v ? 'PASS' : 'FAIL'} ${n} ${extra}`; res.push(l); console.log(l); }; // printed at once so a later bot-check stop keeps earlier results
  for (const w of (process.env.WIDTHS || '1366,390').split(',').map(Number)) { // WIDTHS=390 runs the phone pass alone
    const ctx = await b.newContext({ viewport: { width: w, height: 900 } }); await ctx.route(/\.(png|jpe?g|webp|gif|svg|woff2?|mp4)(\?|$)/i, r => r.abort()); // photos/fonts aren't needed and every request counts toward Shopify's bot limit
    await curlRoute(ctx, theme); const p = await ctx.newPage();
    const errs = []; p.on('pageerror', e => errs.push(e.message));
    const SLOW = +(process.env.SLOW || 0); // ms pause before each page load, to stay under Shopify's rate limit
    const go = async u => { if (SLOW) await p.waitForTimeout(SLOW); for (let t = 0; t < 6; t++) { const r = await p.goto('https://www.swansura.com' + u, { waitUntil: 'load', timeout: 60000 }); if (r && r.status() !== 429) break; console.error(`429 on ${u}, waiting 90 s`); await p.waitForTimeout(90000); } // Shopify's bot check clears after a minute or two
    await p.addStyleTag({ content: '#preview-bar-iframe,#PBarNextFrameWrapper,#shopify-pc__banner,#shopify-pc__banner__dialog{display:none!important}' }); await p.waitForTimeout(800); };
    const bagLines = async () => { await p.waitForSelector('#layer .bag', { timeout: 15000 }).catch(() => {}); return p.evaluate(() => [...document.querySelectorAll('#layer .bag .line')].map(l => l.querySelector('.qty span')?.textContent)); };
    const clear = async () => { await p.evaluate(() => fetch('/cart/clear.js', { method: 'POST' })); await p.evaluate(() => document.querySelector('#layer') && (document.querySelector('#layer').innerHTML = '')); };
    await go(`/?preview_theme_id=${theme}`); await clear();
    // product page
    await go(PDP);
    const p0 = await p.textContent('#pdpPrice');
    const radios = await p.locator('input[name="variant"]').count();
    if (radios > 1) { await p.locator('input[name="variant"]').nth(1).check({ force: true }); await p.waitForTimeout(300); }
    const p1 = await p.textContent('#pdpPrice'); ok(`${w} pdp variant switch`, radios < 2 || p0 !== p1, `${p0.trim()} -> ${p1.trim()}`);
    if (radios > 1) await p.locator('input[name="variant"]').nth(0).check({ force: true });
    const thumbs = await p.locator('.thumbs button').count();
    if (thumbs > 1) { const s0 = await p.getAttribute('#mainImg img', 'src'); await p.locator('.thumbs button').nth(1).click(); const s1 = await p.getAttribute('#mainImg img', 'src'); ok(`${w} pdp gallery`, s0 !== s1); }
    ok(`${w} pdp ingredients`, await p.locator('#ingredients .inci-flow').count() > 0);
    await p.locator('input[name="pack"][value="duo"]').check({ force: true }); await p.locator('[data-addq]').click();
    let l = await bagLines(); ok(`${w} pdp duo -> bag`, l.length === 1 && l[0] === '2', JSON.stringify(l));
    await clear(); await go(PDP);
    if (await p.locator('.fbt [data-addall]').count()) { await p.locator('.fbt [data-addall]').click(); l = await bagLines(); ok(`${w} pdp add both`, l.length === 2, JSON.stringify(l)); }
    await clear(); await go(PDP);
    if (await p.locator('input[name="pack"][value="routine"]').count()) { await p.locator('input[name="pack"][value="routine"]').check({ force: true }); await p.locator('[data-addq]').click(); l = await bagLines(); ok(`${w} pdp routine pack`, l.length === 3, JSON.stringify(l)); }
    await clear(); await go(PDP);
    await Promise.all([p.waitForURL(/checkout|checkouts/, { timeout: 30000 }).catch(() => {}), p.locator('[data-buynow]').click()]);
    ok(`${w} pdp buy it now -> checkout`, /checkout/.test(p.url()), p.url().slice(0, 60));
    await clear();
    await go(KIT); const tabs = await p.locator('[data-incitab]').count();
    if (tabs > 1) { await p.locator('#ingredients summary').click(); await p.locator('[data-incitab]').nth(1).click(); const vis = await p.evaluate(() => [...document.querySelectorAll('.inci-panel')].map(x => !x.hidden)); ok(`${w} kit ingredient tabs`, vis[1] && !vis[0], JSON.stringify(vis)); }
    await p.locator('.heart.big').click();
    // wishlist page + recently viewed
    await go('/pages/wishlist'); await p.waitForTimeout(2500); ok(`${w} wishlist page`, await p.locator('#wishGrid .p-card').count() > 0);
    await go('/'); await p.waitForTimeout(2500); ok(`${w} home recently viewed`, await p.locator('#seenGrid .p-card').count() > 0, String(await p.locator('#seenGrid .p-card').count()));
    // listing filters
    await go('/collections/fragrance'); await p.waitForTimeout(1500);
    const c0 = Number(await p.textContent('#count'));
    const box = p.locator('#filters input[type="checkbox"]').first();
    if (w < 900) await p.locator('#ftoggle').click().catch(() => {});
    await box.check({ force: true }); await p.waitForTimeout(500);
    const c1 = Number(await p.textContent('#count')); ok(`${w} listing filter`, c1 > 0 && c1 < c0, `${c0} -> ${c1}`);
    // advent doors
    await go('/pages/advent'); await p.locator('[data-door]').first().click(); ok(`${w} advent door opens`, await p.locator('.door.open').count() === 1);
    await p.locator('[data-revealall]').first().click(); ok(`${w} advent reveal all`, await p.locator('.door.open').count() >= 12, String(await p.locator('.door.open').count()));
    // bag page
    await go(PDP); await p.locator('[data-addq]').click(); await bagLines(); await go('/cart'); await p.waitForTimeout(1500); ok(`${w} bag page`, await p.locator('#bagPage .line').count() === 1);
    await clear();
    ok(`${w} no JS errors`, errs.length === 0, errs.slice(0, 3).join(' | '));
    await ctx.close();
  }
  console.log(`done: ${res.filter(l => l.startsWith('PASS')).length} pass, ${res.filter(l => l.startsWith('FAIL')).length} fail`); await b.close();
})();
