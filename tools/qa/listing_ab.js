const {chromium,devices}=require('playwright');
(async()=>{const b=await chromium.launch();const out={};
for(let r=0;r<5;r++) for(const t of ['200857125251','200858009987']){
 const c=await b.newContext({...devices['Moto G4']});const p=await c.newPage();
 const s=await c.newCDPSession(p);await s.send('Network.enable');await s.send('Network.emulateNetworkConditions',{offline:false,latency:150,downloadThroughput:1.6*1024*1024/8,uploadThroughput:750*1024/8});await s.send('Emulation.setCPUThrottlingRate',{rate:4});
 await p.addInitScript(()=>{window.__lt=0;window.__lcp=0;new PerformanceObserver(l=>{for(const e of l.getEntries())window.__lcp=e.startTime}).observe({type:'largest-contentful-paint',buffered:true});new PerformanceObserver(l=>{for(const e of l.getEntries())if(e.startTime<8000)window.__lt+=Math.max(0,e.duration-50)}).observe({type:'longtask',buffered:true});});
 // warm preview cookie
 await p.goto(`https://www.swansura.com/?preview_theme_id=${t}`,{waitUntil:'domcontentloaded'}).catch(()=>{});
 await p.goto(`https://www.swansura.com/collections/natural-skincare?fbclid=r${r}`,{waitUntil:'load',timeout:90000}).catch(()=>{});
 await p.waitForTimeout(3000);
 const m=await p.evaluate(()=>({fcp:performance.getEntriesByName('first-contentful-paint')[0]?.startTime|0,lcp:window.__lcp|0,dcl:performance.getEntriesByType('navigation')[0].domContentLoadedEventEnd|0,load:performance.getEntriesByType('navigation')[0].loadEventEnd|0,tbt:window.__lt|0,title:document.title.slice(0,20)}));
 (out[t]=out[t]||[]).push(m);console.log(t,r,JSON.stringify(m));await c.close();}
const med=a=>{a=[...a].sort((x,y)=>x-y);return a[a.length>>1]};
for(const t in out){console.log(t,'median',['fcp','lcp','dcl','load','tbt'].map(k=>k+' '+med(out[t].map(x=>x[k]))).join(', '))}
await b.close()})();
