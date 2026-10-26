// Day 5 browser QA of the draft theme: phone + desktop, console errors, sideways scroll, small text,
// small tap targets, LCP/CLS, axe WCAG 2.1 AA, screenshots.
const { chromium } = require('playwright');
const fs = require('fs');
const BASE = 'https://www.swansura.com';
const THEME = '200301314435';
const pages = JSON.parse(fs.readFileSync(process.argv[2]));
const axeSrc = fs.readFileSync(process.env.AXE || (__dirname + '/axe.min.js'), 'utf8');
(async () => {
  const browser = await chromium.launch();
  const out = [];
  for (const vp of [{ name: 'mobile', width: 390, height: 844, mobile: true }, { name: 'desktop', width: 1366, height: 900, mobile: false }]) {
    const ctx = await browser.newContext({ viewport: { width: vp.width, height: vp.height }, isMobile: vp.mobile, hasTouch: vp.mobile, deviceScaleFactor: 1, userAgent: vp.mobile ? 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148' : undefined });
    await ctx.addInitScript(() => {
      window.__lcp = 0; window.__cls = 0;
      new PerformanceObserver(l => { for (const e of l.getEntries()) window.__lcp = e.startTime; }).observe({ type: 'largest-contentful-paint', buffered: true });
      new PerformanceObserver(l => { for (const e of l.getEntries()) if (!e.hadRecentInput) window.__cls += e.value; }).observe({ type: 'layout-shift', buffered: true });
    });
    const p0 = await ctx.newPage();
    await p0.goto(`${BASE}/?preview_theme_id=${THEME}`, { waitUntil: 'domcontentloaded' });
    for (const [i, path] of pages.entries()) {
      const page = await ctx.newPage();
      const errors = [];
      page.on('console', m => { if (m.type() === 'error') errors.push(m.text().slice(0, 200)); });
      page.on('pageerror', e => errors.push('PAGEERROR ' + String(e).slice(0, 200)));
      const t0 = Date.now();
      let status = 0;
      try { const r = await page.goto(BASE + path, { waitUntil: 'load', timeout: 60000 }); status = r.status(); } catch (e) { errors.push('NAV ' + e.message.slice(0, 100)); }
      const loadMs = Date.now() - t0;
      await page.waitForTimeout(1500);
      const m = await page.evaluate(() => {
        const vw = document.documentElement.clientWidth;
        const sideways = document.documentElement.scrollWidth > vw + 1;
        const wide = [...document.querySelectorAll('body *')].filter(e => { const r = e.getBoundingClientRect(); return r.width && r.right > vw + 2 && getComputedStyle(e).position !== 'fixed' && !e.closest('[class*="slider"],[class*="rail"],.sw-chips,.sw-tabs,ul.slider,[class*="scroll"]'); }).slice(0, 5).map(e => e.tagName + '.' + (e.className || '').toString().slice(0, 40));
        const vis = e => { const s = getComputedStyle(e); const r = e.getBoundingClientRect(); return r.width > 0 && r.height > 0 && s.visibility !== 'hidden' && s.display !== 'none' && s.opacity !== '0'; };
        let small = [];
        for (const e of document.querySelectorAll('body *')) {
          if (![...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim())) continue;
          if (!vis(e) || e.closest('.visually-hidden,[aria-hidden="true"]')) continue;
          const fs = parseFloat(getComputedStyle(e).fontSize); if (fs < 11) small.push(e.tagName + ':' + fs + ':' + e.textContent.trim().slice(0, 30));
        }
        let taps = [];
        for (const e of document.querySelectorAll('a[href],button,input:not([type=hidden]),select,summary,[role=button]')) {
          if (!vis(e) || e.closest('.visually-hidden')) continue;
          const r = e.getBoundingClientRect();
          if (r.width < 24 || r.height < 24) {
            const inline = e.tagName === 'A' && e.closest('p,li,.rte') && getComputedStyle(e).display === 'inline';
            if (!inline) taps.push(e.tagName + ':' + Math.round(r.width) + 'x' + Math.round(r.height) + ':' + (e.getAttribute('aria-label') || e.textContent.trim()).slice(0, 25));
          }
        }
        const imgsNoAlt = [...document.images].filter(i => !i.hasAttribute('alt')).length;
        const brokenImgs = [...document.images].filter(i => i.complete && i.naturalWidth === 0 && i.src && !i.src.startsWith('data:') && i.loading !== 'lazy').length;
        return { sideways, wide, small: small.slice(0, 6), smallN: small.length, taps: taps.slice(0, 6), tapsN: taps.length, imgsNoAlt, brokenImgs, lcp: Math.round(window.__lcp), cls: +window.__cls.toFixed(3), h1: [...document.querySelectorAll('h1')].map(h => h.textContent.trim().slice(0, 60)) };
      });
      await page.addScriptTag({ content: axeSrc });
      const axe = await page.evaluate(async () => { const r = await axe.run(document, { runOnly: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'] }); return r.violations.map(v => ({ id: v.id, impact: v.impact, n: v.nodes.length, ex: v.nodes.slice(0, 2).map(n => n.target.join(' ').slice(0, 80)) })); });
      const shot = `shot_${vp.name}_${i}.png`;
      await page.screenshot({ path: shot });
      out.push({ vp: vp.name, path, status, loadMs, errors: [...new Set(errors)].slice(0, 5), ...m, axe, shot });
      console.log(vp.name, path, status, 'lcp', m.lcp, 'cls', m.cls, 'side', m.sideways, 'axe', axe.length, 'err', errors.length);
      await page.close();
    }
    await ctx.close();
  }
  fs.writeFileSync(process.argv[3], JSON.stringify(out, null, 1));
  await browser.close();
})();
