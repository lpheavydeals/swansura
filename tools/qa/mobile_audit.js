// Phone audit of the draft theme, same checks as the prototype's mobile passes (CLAUDE.md, preview v36/v56):
// sideways scroll, text under 11px, tap targets under 24px (links inside sentences excepted), JS errors.
// node tools/qa/mobile_audit.js THEME_ID OUT.json [widths=390,360,320]
const { chromium } = require('playwright');
const curlRoute = require('./curl_route.js'); // pages via curl while Shopify's bot check blocks the browser
const [theme, out, ws = '390,360,320', only] = process.argv.slice(2);
const PAGES = ['/', '/collections/skincare', '/collections/concern-acne', '/collections/fragrance', '/collections/scent-oud',
  '/collections/moisturiser-for-dry-skin', '/collections/milk-drop-brightening-serum-1', '/collections/dior',
  '/products/milk-drops-brightening-serum-40-ml-rice-milk-alpha-arbutin-skin-brightening-treatment-for-dark-spots-uneven-skin-tone',
  '/products/dior-sauvage-eau-de-parfum-100ml-10ml-men-s-gift-set', '/products/vilvah-goat-milk-hair-kit',
  '/blogs/journal', '/blogs/journal/deyga-or-vilvah', '/pages/rituals', '/collections', '/pages/advent', '/pages/sitemap',
  '/pages/offers', '/pages/wishlist', '/pages/about', '/pages/contact', '/pages/faq', '/cart', '/search?q=rose', '/pages/nope'];
(async () => {
  const b = await chromium.launch(); const res = [];
  for (const w of ws.split(',').map(Number)) {
    const ctx = await b.newContext({ viewport: { width: w, height: 800 }, deviceScaleFactor: 1, isMobile: true, hasTouch: true }); await curlRoute(ctx, theme);
    const p = await ctx.newPage(); let errs = []; p.on('pageerror', e => errs.push((/sw-proto|swansura|assets\//.test(e.stack || '') ? 'theme: ' : 'other: ') + e.message));
    await p.goto(`https://www.swansura.com/?preview_theme_id=${theme}`, { waitUntil: 'load', timeout: 60000 });
    for (const path of only ? only.split(',') : PAGES) {
      errs = [];
      try { await p.goto('https://www.swansura.com' + path, { waitUntil: 'load', timeout: 60000 }); } catch (e) { res.push({ w, path, error: 'load ' + e.message.slice(0, 60) }); continue; }
      await p.addStyleTag({ content: '#preview-bar-iframe,#PBarNextFrameWrapper,#shopify-pc__banner,.shopify-pc__banner__dialog{display:none!important}' });
      await p.waitForTimeout(1200);
      const r = await p.evaluate(() => {
        const vw = document.documentElement.clientWidth, out = { title: document.title, challenge: document.title.includes('Just a moment') };
        out.scroll = document.documentElement.scrollWidth - vw;
        const wide = []; document.querySelectorAll('.swp *').forEach(el => { const b = el.getBoundingClientRect(); if (b.width && b.right > vw + 1 && getComputedStyle(el).position !== 'fixed' && !el.closest('.rail,.grid-p,.thumbs,.typechips,.kwchips,.tabs,.chips,.advent-strip,.journal,.extras,[style*="overflow"]')) wide.push(`${el.tagName.toLowerCase()}.${(el.className || '').toString().slice(0, 30)} w${Math.round(b.width)} r${Math.round(b.right)} min:${getComputedStyle(el).minWidth}`); });
        out.wide = [...new Set(wide)].slice(0, 6);
        const small = new Set(); const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
        while (walker.nextNode()) { const t = walker.currentNode; if (!t.textContent.trim()) continue; const el = t.parentElement; if (!el.closest('.swp') || el.closest('[hidden],template,script,style,.visually-hidden')) continue; const cs = getComputedStyle(el); if (cs.display === 'none' || cs.visibility === 'hidden' || el.getClientRects().length === 0) continue; if (parseFloat(cs.fontSize) < 11) small.add(`${el.tagName.toLowerCase()}.${el.className}`.slice(0, 50) + ' ' + cs.fontSize); }
        out.small = [...small].slice(0, 8);
        const tiny = new Set(); document.querySelectorAll('.swp a, .swp button, .swp input, .swp select, .swp summary, .swp label').forEach(el => {
          const b = el.getBoundingClientRect(); if (!b.width || el.closest('[hidden],.sr-only,.visually-hidden') || getComputedStyle(el).visibility === 'hidden') return;
          if (el.closest('p, li, .pagebody, .abody, .lede, .txt, .smprod, .dt')) return; // inline links in sentences (WCAG 2.5.8 exception)
          if (el.tagName === 'INPUT' && (el.type === 'radio' || el.type === 'checkbox') && el.closest('label')) return;
          if (b.width < 24 || b.height < 24) tiny.add(`${el.tagName.toLowerCase()}.${(el.className || '').toString().slice(0, 30)} ${Math.round(b.width)}x${Math.round(b.height)} "${(el.textContent || el.getAttribute('aria-label') || '').trim().slice(0, 20)}"`);
        });
        out.tiny = [...tiny].slice(0, 8);
        return out;
      });
      res.push({ w, path, ...r, errs: errs.slice(0, 3) });
    }
    await ctx.close();
  }
  require('fs').writeFileSync(out, JSON.stringify(res, null, 1));
  for (const r of res) { const bad = r.error || r.challenge || r.scroll > 0 || r.small?.length || r.tiny?.length || r.errs?.some(x => x.startsWith('theme')); console.log(`${bad ? 'CHECK' : 'OK   '} ${r.w} ${r.path}${r.error ? ' ' + r.error : ''}${r.challenge ? ' BOT-CHECK' : ''}${r.scroll > 0 ? ' scroll+' + r.scroll + ' ' + r.wide.join(',') : ''}${r.small?.length ? ' small:' + r.small.join(' | ') : ''}${r.tiny?.length ? ' tiny:' + r.tiny.join(' | ') : ''}${r.errs?.length ? ' js:' + r.errs.join(' | ') : ''}`); }
  await b.close();
})();
