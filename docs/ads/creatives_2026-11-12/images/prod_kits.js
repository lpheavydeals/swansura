const {chromium}=require('playwright');const fs=require('fs');
const b64=(f,t)=>`data:${t};base64,`+fs.readFileSync(f).toString('base64');
const ADS={
 apm:{img:'apm.jpg',t:'#e9ecf3',b:'#d9dce4',acc:'#55508A',eb:'Vilvah · Official UK partner',h:'Two serums,<br><i>one simple routine</i>',sub:'Morning: Milk Drops · Night: Better Ageing Serum',name:'AM PM Serum Kit',price:'2 serums · £47.99',fine:'Shipped from the UK · Free UK delivery on this kit'},
 bhk:{img:'bhk.jpg',t:'#eceded',b:'#dcdcdd',acc:'#2F5596',eb:'Vilvah · Official UK partner',h:'Your wash-day <i>duo</i>',sub:'Goat Milk Shampoo · Cream Conditioner · light jasmine scent',name:'Bestseller Hair Kit',price:'Shampoo + conditioner · £27.99'},
 abc:{img:'abc.jpg',t:'#efefef',b:'#e0e0e0',acc:'#4E8A2C',eb:'Deyga · Official UK partner',h:'Your everyday <i>A, B, C</i>',sub:'Aloe vera gel · Beetroot lip balm · Charcoal bath bar',sc:0.86,name:'ABC Kit',price:'3 products · £22.99'},
 clr:{img:'clr.jpg',t:'#efefef',b:'#e0e0e0',acc:'#4E8A2C',eb:'Deyga · Official UK partner',h:'Wash, then <i>hydrate</i>',sub:'Charcoal bath bar, then aloe vera gel',sc:0.86,name:'Clear Skin Kit',price:'2 products · £14.99'},
};
const SZ={'4x5':{W:1080,H:1350,top:64,hs:74,pw:940,pt:300,bar:1218},'9x16':{W:1080,H:1920,top:250,hs:84,pw:1080,pt:540,bar:1610},'1x1':{W:1080,H:1080,top:44,hs:60,pw:700,pt:250,bar:958}};
const html=(a,z0,zn)=>{const z={...z0,pw:a.full&&zn=='9x16'?z0.W:z0.pw*(a.full?0.98:1)*(a.sc||1),pt:z0.pt};return `<html><head><meta charset="utf-8"><style>
@font-face{font-family:PJS;src:url(pjs.woff2)}@font-face{font-family:DMS;src:url(dmserif.ttf)}@font-face{font-family:DMS;src:url(dmserif-i.ttf);font-style:italic}
*{margin:0;box-sizing:border-box}body{width:${z.W}px;height:${z.H}px;overflow:hidden;position:relative;font-family:PJS;background:linear-gradient(${a.t},${a.t} ${z.pt}px,${a.b})}
.ph{position:absolute;left:${(z.W-z.pw)/2}px;top:${z.pt}px;width:${z.pw}px;-webkit-mask-image:${a.full?'linear-gradient(transparent,#000 110px,#000 calc(100% - 90px),transparent),linear-gradient(90deg,transparent,#000 28px,#000 calc(100% - 28px),transparent)':'radial-gradient(closest-side,#000 72%,transparent 100%)'};-webkit-mask-composite:source-in;mask-composite:intersect}
.top{position:absolute;left:0;right:0;top:${z.top}px;text-align:center;padding:0 70px}
.eb{font-weight:700;font-size:${zn=='1x1'?17:20}px;letter-spacing:.28em;text-transform:uppercase;color:#695541}
.h{font-family:DMS;font-size:${z.hs}px;line-height:1.04;color:#1F1A17;margin-top:14px;letter-spacing:-.005em}
.h i{color:${a.acc}}
.sub{font-weight:500;font-size:${zn=='1x1'?19:23}px;color:#4B3E33;margin-top:16px;letter-spacing:.01em}
.bar{position:absolute;left:${zn=='1x1'?70:60}px;right:${zn=='1x1'?70:60}px;top:${z.bar}px;height:${zn=='1x1'?92:108}px;background:#fff;border-radius:999px;display:flex;align-items:center;justify-content:space-between;padding:0 10px 0 34px;box-shadow:0 14px 40px rgba(30,25,20,.16)}
.nm{font-family:DMS;font-size:${zn=='1x1'?27:32}px;color:#1F1A17;line-height:1}.pr{font-weight:700;font-size:${zn=='1x1'?17:19}px;color:#695541;margin-top:5px}
.fine{font-size:${zn=='1x1'?13:15}px;font-weight:600;color:#7A6A5A;margin-top:4px}.btn{height:${zn=='1x1'?64:76}px;padding:0 30px;border-radius:999px;background:#133A2F;color:#fff;font-weight:800;font-size:${zn=='1x1'?21:24}px;display:flex;align-items:center;gap:10px;letter-spacing:.02em}
.foot{position:absolute;left:0;right:0;top:${z.bar+(zn=='1x1'?92:108)}px;text-align:center;font-size:${zn=='1x1'?15:18}px;font-weight:600;color:#5C4A39;letter-spacing:.04em}
</style></head><body>
<img class="ph" src="${b64(a.img,'image/jpeg')}">
<div class="top"><div class="eb">${a.eb}</div><div class="h">${a.h}</div><div class="sub">${a.sub}</div></div>
<div class="bar"><div><div class="nm">${a.name}</div><div class="pr">${a.price}</div><div class="fine">${a.fine||'Shipped from the UK · Free UK delivery over £40'}</div></div><div class="btn">Shop now <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></div></div>

</body></html>`};
(async()=>{const br=await chromium.launch();
for(const [k,a] of Object.entries(ADS))for(const [zn,z] of Object.entries(SZ)){const p=await br.newPage({viewport:{width:z.W,height:z.H}});fs.writeFileSync('t.html',html(a,z,zn));await p.goto('file://'+process.cwd()+'/t.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(250);await p.screenshot({path:`${k}_${zn}.png`});await p.close();}
await br.close()})();
