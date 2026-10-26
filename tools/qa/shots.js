// Side-by-side screenshots: prototype (local server) vs draft theme preview.
// node tools/qa/shots.js OUTDIR THEME_ID "protoRoute|storePath" ...  (widths 1366 and 390)
const { chromium } = require('playwright');
const [out, theme, ...pairs] = process.argv.slice(2);
(async () => {
  const b = await chromium.launch();
  for (const w of [1366, 390]) {
    const ctx = await b.newContext({ viewport: { width: w, height: 900 }, deviceScaleFactor: 1 });
    const p = await ctx.newPage();
    await p.goto(`https://www.swansura.com/?preview_theme_id=${theme}`, { waitUntil: 'domcontentloaded' });
    for (const pair of pairs) {
      const [route, path] = pair.split('|');
      const name = route.replace(/[^a-z0-9-]/gi, '_') || 'home';
      await p.goto('http://localhost:8765/#' + route, { waitUntil: 'networkidle' });
      await p.waitForTimeout(1500);
      await p.screenshot({ path: `${out}/${name}_${w}_proto.png`, fullPage: true });
      await p.goto('https://www.swansura.com' + path, { waitUntil: 'networkidle' }).catch(() => {});
      await p.addStyleTag({ content: '#preview-bar-iframe,#PBarNextFrameWrapper{display:none!important}' }).catch(() => {});
      await p.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 600) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 60)); } window.scrollTo(0, 0); });
      await p.waitForTimeout(800);
      await p.screenshot({ path: `${out}/${name}_${w}_store.png`, fullPage: true });
      console.log(w, route, 'ok');
    }
    await ctx.close();
  }
  await b.close();
})();
