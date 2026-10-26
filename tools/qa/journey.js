const { chromium } = require('playwright');
const BASE='https://www.swansura.com', PDP='/products/milk-drops-brightening-serum-40-ml-rice-milk-alpha-arbutin-skin-brightening-treatment-for-dark-spots-uneven-skin-tone';
(async()=>{
  const b=await chromium.launch(); const res=[];
  for (const vp of [{n:'mobile',w:390,h:844,m:true},{n:'desktop',w:1366,h:900,m:false}]) {
    const ctx=await b.newContext({viewport:{width:vp.w,height:vp.h},isMobile:vp.m,hasTouch:vp.m});
    const p=await ctx.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(String(e).slice(0,150)));
    await p.goto(BASE+'/?preview_theme_id=200301314435'); 
    const step=async(name,fn)=>{try{const r=await fn();res.push([vp.n,name,'OK',r||''])}catch(e){res.push([vp.n,name,'FAIL',e.message.slice(0,150)]);await p.screenshot({path:`jfail_${vp.n}_${name.replace(/\W/g,'')}.png`})}};
    if (vp.m) await step('mobile menu opens', async()=>{ await p.click('header-drawer summary'); await p.waitForSelector('#menu-drawer',{state:'visible',timeout:5000}); const n=await p.locator('#menu-drawer a').count(); await p.keyboard.press('Escape'); await p.click('header-drawer summary').catch(()=>{}); return n+' links'; });
    await step('search', async()=>{ await p.goto(BASE+'/search?q=vilvah&type=product'); const n=await p.locator('.product-grid .grid__item').count(); if(!n) throw Error('no results'); return n+' results'; });
    await step('PDP loads + brand/ingredients', async()=>{ await p.goto(BASE+PDP); await p.waitForSelector('h1'); const h1=await p.textContent('h1'); const ing=await p.locator('text=Ingredients').count(); const pay=await p.locator('text=Pay in 3').count(); return h1.trim()+' | ingredients:'+ing+' paylater:'+pay; });
    await step('add to bag opens drawer', async()=>{ await p.click('product-form button[name="add"]'); await p.waitForSelector('cart-drawer.active, cart-drawer[class*="active"]',{timeout:10000}); const goal=await p.locator('cart-drawer .sw-goal, cart-drawer [class*="sw-cart-goal"], cart-drawer [class*="goal"]').count(); const cnt=await p.locator('#cart-icon-bubble .cart-count-bubble, #cart-icon-bubble [class*="count"]').first().textContent().catch(()=>''); return 'goal bar:'+goal+' count:'+String(cnt).trim(); });
    await step('drawer checkout button', async()=>{ const c=await p.locator('cart-drawer button[name="checkout"], cart-drawer [name="checkout"]').count(); if(!c) throw Error('no checkout'); return 'checkout present'; });
    await step('cart page totals', async()=>{ await p.goto(BASE+'/cart'); const t=await p.locator('.totals__total-value').first().textContent(); if(/GBP/.test(t)) throw Error('GBP shown '+t); return t.trim(); });
    await step('checkout reachable', async()=>{ await p.click('button[name="checkout"]'); await p.waitForURL(/checkouts|checkout/,{timeout:20000}); return p.url().split('?')[0].slice(0,60); });
    await step('collection filter/sort', async()=>{ await p.goto(BASE+'/collections/gucci?sort_by=price-ascending'); const n=await p.locator('.product-grid .grid__item').count(); return n+' items sorted'; });
    res.push([vp.n,'page errors',errs.length?'FAIL':'OK',errs.join(' | ')]);
    await ctx.close();
  }
  console.log(res.map(r=>r.join(' | ')).join('\n')); await b.close();
})();
