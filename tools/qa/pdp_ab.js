const {chromium,devices}=require('playwright');
const T={old:'200858009987',fix:'200907620739'};const H=['vilvah-goat-milk-shampoo-250ml','tom-ford-noir-extreme-parfum-100ml-for-men','100-plant-based-hair-color-black-natural-henna-indigo-dye-kit-grey-coverage-sensitive-scalp-deygas'];
(async()=>{const b=await chromium.launch();const R={old:[],fix:[]};
for(let run=0;run<4;run++)for(const h of H)for(const k of (run%2?['fix','old']:['old','fix'])){
 const c=await b.newContext(devices['Moto G4']);const p=await c.newPage();
 // set preview cookie first (unthrottled), then measure a throttled load of the product page
 await p.goto(`https://www.swansura.com/?preview_theme_id=${T[k]}`,{waitUntil:'domcontentloaded',timeout:90000});
 const cdp=await c.newCDPSession(p);await cdp.send('Network.enable');await cdp.send('Network.setCacheDisabled',{cacheDisabled:true});
 await cdp.send('Network.emulateNetworkConditions',{offline:false,latency:150,downloadThroughput:1.6e6/8,uploadThroughput:750e3/8});await cdp.send('Emulation.setCPUThrottlingRate',{rate:4});
 await p.addInitScript(()=>{window.__lcp=0;window.__lt=0;new PerformanceObserver(l=>{for(const e of l.getEntries())window.__lcp=e.startTime}).observe({type:'largest-contentful-paint',buffered:true});new PerformanceObserver(l=>{for(const e of l.getEntries())window.__lt+=e.duration-50}).observe({type:'longtask',buffered:true});});
 await p.goto(`https://www.swansura.com/products/${h}`,{waitUntil:'load',timeout:120000});await p.waitForTimeout(2000);
 const r=await p.evaluate(()=>{const n=performance.getEntriesByType('navigation')[0];const f=performance.getEntriesByName('first-contentful-paint')[0];return{theme:Shopify.theme.id,fcp:f?f.startTime|0:0,lcp:window.__lcp|0,dcl:n.domContentLoadedEventEnd|0,load:n.loadEventEnd|0,lt:window.__lt|0,html:n.transferSize>>10}});
 if(String(r.theme)!==T[k])console.log('WRONG THEME',k,r.theme);R[k].push(r);await c.close();}
const med=a=>{a=[...a].sort((x,y)=>x-y);return a[a.length>>1]};
for(const k of ['old','fix'])console.log(k.padEnd(4),Object.fromEntries(['fcp','lcp','dcl','load','lt','html'].map(m=>[m,med(R[k].map(r=>r[m]))])),'n='+R[k].length);
require('fs').writeFileSync('ab_raw.json',JSON.stringify(R));await b.close()})();
