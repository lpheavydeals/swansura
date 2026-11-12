const {chromium}=require('playwright');const fs=require('fs');
const b64=(f,t)=>`data:${t};base64,`+fs.readFileSync(f).toString('base64');
const ADS={
 lip:{bg:'lipC.png',pos:'50% 45%',font:'SAT',w:400,hs:88,eb:'DEYGA · NOW SHIPPED FROM THE UK',h:'The beetroot lip balm<br>you know <span class="s">from home</span>',line:['beetroot','almond &amp; avocado oil','shea butter','a sheer, rosy tint'],tile:'deyga1.jpg',name:'Deyga Beetroot Lip Balm',price:'Classic 10 g · £10.99'},
 milk:{bg:'milkA.png',pos:'50% 50%',font:'DAN',w:600,hs:90,eb:'VILVAH · NOW SHIPPED FROM THE UK',h:'Milk Drops,<br>your daily <span class="s">milk serum</span>',line:['rice milk extract','hyaluronic acid','fragrance-free'],tile:'vil0.jpg',name:'Vilvah Milk Drops Serum',price:'20 ml £21.99 · 40 ml £30.99'},
 hair:{bg:'h4.png',pos:'50% 0%',drop:{'4x5':300,'9x16':470},sc:0.78,font:'KAU',w:400,hs:78,eb:'DEYGA HAIR CARE KIT · SHIPPED FROM THE UK',h:'Your Sunday <span class="s">champi</span>,<br>in three easy steps',line:['1 · pre-wash oil','2 · rice water shampoo','3 · soy milk conditioner'],tile:'hk1.jpg',name:'Deyga Hair Care Kit',price:'50 ml £18.99 · 220 ml £36.99'},
};
const SIZES={'4x5':{W:1080,H:1350,top:70,bot:60},'9x16':{W:1080,H:1920,top:250,bot:330}};
const html=(a,z,zn)=>`<html><head><meta charset="utf-8"><style>
@font-face{font-family:PJS;src:url(pjs.woff2)}@font-face{font-family:SAT;src:url(Satisfy-Regular.ttf)}@font-face{font-family:DAN;src:url(dancing.ttf);font-weight:400 700}@font-face{font-family:KAU;src:url(kaushan.ttf)}
*{margin:0;box-sizing:border-box}body{width:${z.W}px;height:${z.H}px;overflow:hidden;position:relative;font-family:PJS}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:${a.pos}}
.ts{position:absolute;left:0;right:0;top:0;height:${z.top+430}px;background:linear-gradient(rgba(12,18,15,.62),rgba(12,18,15,.25) 65%,transparent)}
.bs{position:absolute;left:0;right:0;bottom:0;height:${z.bot+520}px;background:linear-gradient(transparent,rgba(12,18,15,.35) 40%,rgba(12,18,15,.7))}
.top{position:absolute;left:0;right:0;top:${z.top}px;text-align:center;padding:0 60px}
.eb{font-weight:700;font-size:22px;letter-spacing:.3em;color:#F4EEE4;display:inline-flex;align-items:center;gap:16px;text-shadow:0 1px 10px rgba(0,0,0,.4)}
.eb:before,.eb:after{content:'';width:40px;height:1.5px;background:#EACB8E}
.h{font-family:${a.font};font-weight:${a.w};font-size:${a.hs}px;line-height:1.1;color:#fff;margin-top:18px;text-shadow:0 3px 22px rgba(0,0,0,.4)}
.s{color:#F6D58E;text-shadow:0 1px 3px rgba(40,25,10,.55),0 3px 20px rgba(0,0,0,.5)}
.bot{position:absolute;left:44px;right:44px;bottom:${z.bot}px}
.line{text-align:center;color:#fff;font-weight:600;font-size:28px;letter-spacing:.04em;text-shadow:0 2px 14px rgba(0,0,0,.6);margin-bottom:22px}
.line b{color:#EACB8E;margin:0 12px}
.card{display:flex;align-items:center;gap:22px;background:rgba(255,255,255,.95);border-radius:28px;padding:18px 20px;box-shadow:0 20px 50px rgba(0,0,0,.28)}
.tile{width:150px;height:150px;border-radius:18px;overflow:hidden;flex:none;border:2px solid #EAD9B8}.tile img{width:100%;height:100%;object-fit:cover}
.info{flex:1;min-width:0}.nm{font-family:${a.font};font-weight:${a.w};font-size:40px;color:#133A2F;line-height:1.1}
.pr{font-weight:700;font-size:25px;color:#695541;margin-top:8px}.fine{font-size:19px;color:#5C4A39;margin-top:8px;font-weight:600}
.btn{flex:none;height:84px;padding:0 30px;border-radius:999px;background:linear-gradient(180deg,#1E5A47,#133A2F);color:#fff;font-weight:800;font-size:28px;display:flex;align-items:center;gap:10px}
</style></head><body>${a.drop?`<img class="bg" style="filter:blur(38px) brightness(.85);transform:scale(1.15)" src="${b64(a.bg,'image/png')}"><img style="position:absolute;left:${(z.W-z.W*a.sc)/2}px;top:${a.drop[zn]}px;width:${z.W*a.sc}px;-webkit-mask-image:linear-gradient(transparent,#000 140px),linear-gradient(90deg,transparent,#000 90px,#000 calc(100% - 90px),transparent);-webkit-mask-composite:source-in;mask-composite:intersect" src="${b64(a.bg,'image/png')}">`:`<img class="bg" src="${b64(a.bg,'image/png')}">`}<div class="ts"></div><div class="bs"></div>
<div class="top"><div class="eb">${a.eb}</div><div class="h">${a.h}</div></div>
<div class="bot"><div class="line">${a.line.join('<b>·</b>')}</div><div class="card"><div class="tile"><img src="${b64(a.tile,'image/jpeg')}"></div><div class="info"><div class="nm">${a.name}</div><div class="pr">${a.price}</div><div class="fine">Official UK partner · Free UK delivery over £40</div></div><div class="btn">Shop now <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></div></div></div></body></html>`;
(async()=>{const br=await chromium.launch();
for(const [k,a] of Object.entries(ADS))for(const [zn,z] of Object.entries(SIZES)){const p=await br.newPage({viewport:{width:z.W,height:z.H}});fs.writeFileSync('t.html',html(a,z,zn));await p.goto('file://'+process.cwd()+'/t.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(250);await p.screenshot({path:`${k}_${zn}.png`});await p.close();}
await br.close()})();
