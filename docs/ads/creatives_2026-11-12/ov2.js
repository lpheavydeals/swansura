const {chromium}=require('playwright');const fs=require('fs');
const MODE=process.argv[2]||'916';
// band positions (px in the 1080x1920 frame)
const P=MODE=='916'?{top:120,bot:1800,ts:0,tsh:430,bsh:520}:{top:315,bot:1600,ts:285,tsh:620,bsh:620};
const CSS=`@font-face{font-family:PJS;src:url(pjs.woff2) format('woff2');font-weight:200 800}
@font-face{font-family:Fr;src:url(fraunces-italic.ttf);font-style:italic;font-weight:100 900}
@font-face{font-family:FrR;src:url(fraunces.ttf);font-weight:100 900}
@font-face{font-family:GV;src:url(greatvibes.ttf)}
*{margin:0;box-sizing:border-box}html,body{width:1080px;height:1920px;background:transparent;overflow:hidden}
.abs{position:absolute;left:0;right:0;text-align:center;padding:0 70px}
.ts{position:absolute;left:0;right:0;top:${P.ts}px;height:${P.tsh}px;background:linear-gradient(rgba(12,18,15,.5),rgba(12,18,15,.16) 70%,transparent)}
.bs{position:absolute;left:0;right:0;bottom:${1920-(MODE=='916'?1920:1635)}px;height:${P.bsh}px;background:linear-gradient(transparent,rgba(12,18,15,.14) 35%,rgba(12,18,15,.45))}
.eb{font-family:PJS;font-weight:700;font-size:22px;letter-spacing:.32em;color:#F4EEE4;text-shadow:0 1px 10px rgba(0,0,0,.4);display:inline-flex;align-items:center;gap:18px}
.eb:before,.eb:after{content:'';width:46px;height:1.5px;background:#EACB8E}
.h{font-family:Fr;font-style:italic;font-weight:420;font-variation-settings:'SOFT' 100,'WONK' 1,'opsz' 96;color:#fff;font-size:74px;line-height:1.02;letter-spacing:-.01em;text-shadow:0 3px 22px rgba(0,0,0,.35)}
.s{font-family:GV;color:#F6D58E;font-size:1.45em;font-style:normal;font-weight:400;letter-spacing:0;line-height:.9;text-shadow:0 1px 3px rgba(40,25,10,.55),0 3px 20px rgba(0,0,0,.5)}
.l{font-family:Fr;font-style:italic;font-weight:400;font-variation-settings:'SOFT' 100,'opsz' 72;color:#fff;font-size:50px;line-height:1.12;text-shadow:0 2px 18px rgba(0,0,0,.45)}
.l b{font-family:PJS;font-style:normal;color:#EACB8E;font-weight:700;margin:0 14px}
.small{font-family:PJS;font-weight:600;font-size:26px;letter-spacing:.06em;color:#F4EEE4;text-shadow:0 1px 10px rgba(0,0,0,.5);margin-top:16px}
.card{position:absolute;inset:0;background:radial-gradient(120% 70% at 30% 20%,#2A6B57 0%,#1B4D3E 38%,#133A2F 75%,#0F2E25 100%)}
.logo{position:absolute;left:0;right:0;text-align:center}.logo img{height:150px}
.tile{position:absolute;left:250px;width:580px;height:580px;border-radius:40px;overflow:hidden;background:#fff;box-shadow:0 30px 80px rgba(0,0,0,.35);border:3px solid rgba(234,203,142,.6)}
.tile img{width:100%;height:100%;object-fit:cover}
.name{position:absolute;left:60px;right:60px;text-align:center;color:#fff;font-family:Fr;font-style:italic;font-variation-settings:'SOFT' 100,'opsz' 96;font-weight:450;font-size:62px;line-height:1.05}
.price{position:absolute;left:0;right:0;text-align:center;color:#EACB8E;font-family:PJS;font-size:36px;font-weight:700}
.btn{position:absolute;left:290px;width:500px;height:108px;border-radius:999px;background:linear-gradient(180deg,#EACB8E,#C4924A);color:#0F2E25;font-family:PJS;font-size:42px;font-weight:800;display:flex;align-items:center;justify-content:center;gap:16px;box-shadow:0 16px 40px rgba(0,0,0,.3)}
.fine{position:absolute;left:0;right:0;text-align:center;color:#F4EEE4;font-family:PJS;font-size:28px;font-weight:600;line-height:1.5}.fine span{color:#EACB8E}`;
const logoUri='data:image/svg+xml;base64,'+Buffer.from(fs.readFileSync('logo.svg','utf8')).toString('base64');
const img=f=>'data:image/jpeg;base64,'+fs.readFileSync(f).toString('base64');
const top=(inner)=>`<div class="ts"></div><div class="abs" style="top:${P.top}px">${inner}</div>`;
const bot=(inner)=>`<div class="bs"></div><div class="abs" style="bottom:${1920-P.bot}px">${inner}</div>`;
const hook=(eb,h)=>top(`<div class="eb">${eb}</div><div class="h" style="margin-top:22px">${h}</div>`);
const step=(n,t)=>top(`<div class="h"><span class="s" style="font-size:1.05em">Step ${n}</span></div><div class="h" style="font-size:62px;margin-top:6px">${t}</div>`);
const line=(arr)=>bot(`<div class="l">${arr.join('<b>·</b>')}</div>`);
const capb=(t,s)=>bot(`<div class="l" style="font-size:56px">${t}</div>${s?`<div class="small">${s}</div>`:''}`);
const arrow='<svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#0F2E25" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>';
const end=(im,name,price)=>{const o=MODE=='916'?0:-20;return `<div class="card"></div><div class="logo" style="top:${330+o}px"><img src="${logoUri}"></div><div class="tile" style="top:${520+o}px"><img src="${img(im)}"></div><div class="name" style="top:${1132+o}px">${name}</div><div class="price" style="top:${1222+o}px">${price}</div><div class="btn" style="top:${1300+o}px">Shop now ${arrow}</div><div class="fine" style="top:${1446+o}px">Free UK delivery over £40<br><span>swansura.com</span></div>`};
const O={
 d1:hook('DEYGA · NOW SHIPPED FROM THE UK','The beetroot lip balm<br>you know <span class="s">from home</span>'),
 d2a:line(['beetroot extract']), d2b:line(['beetroot extract','almond &amp; avocado oil']), d2c:line(['beetroot','almond &amp; avocado oil','shea butter']),
 d3a:capb('a <span class="s" style="font-size:1.4em">sheer, rosy</span> tint'), d3b:capb('lips feel <span class="s" style="font-size:1.4em">soft &amp; supple</span>'),
 d4:capb('Official UK partner of Deyga','Dispatched from the UK · Free delivery over £40'),
 dend:end('deyga1.jpg','Deyga Beetroot Lip Balm','Classic 10 g · £10.99'),
 v1:hook('VILVAH · NOW SHIPPED FROM THE UK','Milk Drops,<br>your daily <span class="s">milk serum</span>'),
 v2:line(['rice milk extract']), v3:line(['rice milk extract','hyaluronic acid']),
 vs1:step(1,'a few drops on clean skin'), vs2:step(2,'gently pat it in'), vs3:step(3,'follow with moisturiser &amp; SPF'),
 v5:capb('fragrance-free','Official UK partner of Vilvah · Dispatched from the UK'),
 vend:end('vil0.jpg','Vilvah Milk Drops Serum','20 ml £21.99 · 40 ml £30.99'),
};
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});const dir='ov'+MODE;fs.mkdirSync(dir,{recursive:true});
for(const [k,v] of Object.entries(O)){fs.writeFileSync('t.html',`<html><head><meta charset="utf-8"><style>${CSS}</style></head><body>${v}</body></html>`);
await p.goto('file://'+process.cwd()+'/t.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(200);
await p.screenshot({path:dir+'/'+k+'.png',omitBackground:!k.endsWith('end')});}
await b.close()})();
