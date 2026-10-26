// Journey check on the draft theme: card Add -> bag, qty, search overlay, phone drawer, help panel, wishlist.
// node tools/qa/proto_journey.js THEME_ID OUTDIR
const { chromium } = require('playwright');
const [theme, out] = process.argv.slice(2);
(async () => {
  const b = await chromium.launch(); const res = [];
  const ok = (n, v, extra = '') => res.push(`${v ? 'PASS' : 'FAIL'} ${n} ${extra}`);
  for (const w of [1366, 390]) {
    const ctx = await b.newContext({ viewport: { width: w, height: 900 } }); const p = await ctx.newPage();
    const errs = []; p.on('pageerror', e => errs.push(e.message));
    await p.goto(`https://www.swansura.com/?preview_theme_id=${theme}`, { waitUntil: 'load', timeout: 60000 });
    await p.addStyleTag({ content: '#preview-bar-iframe,#PBarNextFrameWrapper,#shopify-pc__banner{display:none!important}' });
    await p.waitForTimeout(1500);
    await p.locator('.p-card .add').first().click(); await p.waitForSelector('#layer .bag', { timeout: 15000 }).catch(() => {});
    const lines = await p.locator('#layer .bag .line').count(); ok(`${w} add -> bag`, lines > 0, `lines=${lines}`);
    await p.screenshot({ path: `${out}/j_${w}_bag.png` });
    const cnt = await p.locator('#bagCount').textContent(); ok(`${w} bag count`, +cnt >= 1, cnt);
    await p.locator('#layer [data-bq]').filter({ hasText: '+' }).first().click(); await p.waitForTimeout(1500);
    const q = await p.locator('#layer .bag .qty span').first().textContent(); ok(`${w} qty +`, +q >= 2, q);
    await p.locator('#layer .rm').first().click(); await p.waitForTimeout(1500);
    ok(`${w} remove`, await p.locator('#layer .bag-empty').count() > 0);
    await p.keyboard.press('Escape');
    await p.locator('#openSearch').click(); await p.fill('#q', 'oud'); await p.waitForSelector('#qres .p-card', { timeout: 15000 }).catch(() => {});
    const sr = await p.locator('#qres .p-card').count(); ok(`${w} search`, sr > 0, `cards=${sr}`);
    await p.screenshot({ path: `${out}/j_${w}_search.png` }); await p.keyboard.press('Escape');
    if (w < 900) { await p.locator('#burger').click(); await p.waitForTimeout(400); ok(`${w} drawer`, await p.locator('#layer .drawer-nav').count() > 0); await p.screenshot({ path: `${out}/j_${w}_drawer.png` }); await p.keyboard.press('Escape'); }
    else { await p.locator('nav.main .item').first().hover(); await p.waitForTimeout(400); ok(`${w} mega`, await p.locator('nav.main .item').first().locator('.mega').isVisible()); await p.screenshot({ path: `${out}/j_${w}_mega.png` }); }
    await p.locator('#chatBtn').click(); ok(`${w} help`, await p.locator('#chatPanel').isVisible()); await p.keyboard.press('Escape');
    await p.locator('.p-card .heart').first().click(); await p.waitForTimeout(300);
    ok(`${w} wishlist`, (await p.locator('#wishCount').textContent()) === '1');
    ok(`${w} no JS errors`, errs.length === 0, errs.join(' | '));
    await ctx.close();
  }
  console.log(res.join('\n')); await b.close();
})();
