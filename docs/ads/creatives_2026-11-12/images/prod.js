const {chromium}=require('playwright');const fs=require('fs');
const b64=(f,t)=>`data:${t};base64,`+fs.readFileSync(f).toString('base64');
const ADS={
 lip:{img:'lip.jpg',font:'SAT',w:400,hs:82,bg:'linear-gradient(170deg,#F7E9EC 0%,#F1DCE1 55%,#E9CDD4 100%)',ink:'#4A1626',acc:'#9B2F4A',eb:'DEYGA · NOW SHIPPED FROM THE UK',h:'The beetroot lip balm<br>you know <span class="s">from home</span>',line:['beetroot','almond &amp; avocado oil','shea butter','a sheer, rosy tint'],name:'Deyga Beetroot Lip Balm',price:'Classic 10 g · £10.99'},
 milk:{img:'milk.jpg',font:'DAN',w:600,hs:88,bg:'linear-gradient(170deg,#FAF6EE 0%,#F4ECDD 60%,#ECE0CB 100%)',ink:'#3E2F22',acc:'#B5843A',eb:'VILVAH · NOW SHIPPED FROM THE UK',h:'Milk Drops,<br>your daily <span class="s">milk serum</span>',line:['rice milk extract','hyaluronic acid','fragrance-free'],name:'Vilvah Milk Drops Serum',price:'20 ml £21.99 · 40 ml £30.99'},
 hair:{img:'hair.jpg',font:'KAU',w:400,hs:76,bg:'linear-gradient(170deg,#F0F4E8 0%,#E4ECD8 60%,#D7E3C8 100%)',ink:'#1F3A1C',acc:'#5E8A2C',eb:'DEYGA HAIR CARE KIT · SHIPPED FROM THE UK',h:'Your Sunday <span class="s">champi</span>,<br>in three easy steps',line:['1 · pre-wash oil','2 · rice water shampoo','3 · soy milk conditioner'],name:'Deyga Hair Care Kit',price:'50 ml £18.99 · 220 ml £36.99'},
};
const SZ={'4x5':{W:1080,H:1350,top:62,ph:780,pt:318,gap:26},'9x16':{W:1080,H:1920,top:240,ph:900,pt:560,gap:34},'1x1':{W:1080,H:1080,top:44,ph:600,pt:250,gap:18}};
const html=(a,z,zn)=>`<html><head><meta charset="utf-8"><style>
@font-face{font-family:PJS;src:url(pjs.woff2)}@font-face{font-family:SAT;src:url(Satisfy-Regular.ttf)}@font-face{font-family:DAN;src:url(dancing.ttf);font-weight:400 700}@font-face{font-family:KAU;src:url(kaushan.ttf)}
*{margin:0;box-sizing:border-box}body{width:${z.W}px;height:${z.H}px;overflow:hidden;position:relative;font-family:PJS;background:${a.bg}}
body:before{content:'';position:absolute;inset:0;background:radial-gradient(60% 40% at 50% ${Math.round((z.pt+z.ph/2)/z.H*100)}%,rgba(255,255,255,.75),transparent 70%)}
.top{position:absolute;left:0;right:0;top:${z.top}px;text-align:center;padding:0 60px}
.eb{font-weight:700;font-size:${zn=='1x1'?19:21}px;letter-spacing:.3em;color:#695541;display:inline-flex;align-items:center;gap:16px}
.eb:before,.eb:after{content:'';width:40px;height:1.5px;background:#B5843A}
.h{font-family:${a.font};font-weight:${a.w};font-size:${zn=='1x1'?a.hs*0.82:a.hs}px;line-height:1.08;color:${a.ink};margin-top:14px}
.s{color:${a.acc}}
.ph{position:absolute;left:${(z.W-z.ph)/2}px;top:${z.pt}px;width:${z.ph}px;height:${z.ph}px;border-radius:40px;overflow:hidden;box-shadow:0 30px 70px rgba(40,30,20,.18),0 0 0 6px rgba(255,255,255,.7)}
.ph img{width:100%;height:100%;object-fit:cover}
.line{position:absolute;left:0;right:0;top:${z.pt+z.ph+z.gap}px;text-align:center;color:${a.ink};font-weight:600;font-size:${zn=='1x1'?22:26}px;letter-spacing:.04em}
.line b{color:#B5843A;margin:0 10px}
.row{position:absolute;left:${(z.W-z.ph)/2}px;right:${(z.W-z.ph)/2}px;top:${z.pt+z.ph+z.gap+(zn=='1x1'?44:56)}px;display:flex;align-items:center;justify-content:space-between;gap:20px}
.nm{font-family:${a.font};font-weight:${a.w};font-size:${zn=='1x1'?34:40}px;color:${a.ink};line-height:1.05}.pr{font-weight:700;font-size:${zn=='1x1'?21:25}px;color:#695541;margin-top:6px}
.fine{font-size:${zn=='1x1'?16:18}px;color:#5C4A39;margin-top:5px;font-weight:600}
.btn{flex:none;height:${zn=='1x1'?70:84}px;padding:0 32px;border-radius:999px;background:linear-gradient(180deg,#1E5A47,#133A2F);color:#fff;font-weight:800;font-size:${zn=='1x1'?24:28}px;display:flex;align-items:center;gap:10px;box-shadow:0 12px 30px rgba(19,58,47,.3)}
.logo{position:absolute;right:${(z.W-z.ph)/2+22}px;top:${z.pt+22}px;height:54px;padding:8px 14px;background:rgba(255,255,255,.88);border-radius:14px}.logo img{height:38px}
</style></head><body>
<div class="top"><div class="eb">${a.eb}</div><div class="h">${a.h}</div></div>
<div class="ph"><img src="${b64(a.img,'image/jpeg')}"></div>
<div class="logo"><img src="${b64('logob.svg','image/svg+xml')}"></div>
<div class="line">${a.line.join('<b>·</b>')}</div>
<div class="row"><div><div class="nm">${a.name}</div><div class="pr">${a.price}</div><div class="fine">Official UK partner · Free UK delivery over £40</div></div>
<div class="btn">Shop now <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></div></div>
</body></html>`;
(async()=>{const br=await chromium.launch();
for(const [k,a] of Object.entries(ADS))for(const [zn,z] of Object.entries(SZ)){const p=await br.newPage({viewport:{width:z.W,height:z.H}});fs.writeFileSync('t.html',html(a,z,zn));await p.goto('file://'+process.cwd()+'/t.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(250);await p.screenshot({path:`${k}_${zn}.png`});await p.close();}
await br.close()})();
