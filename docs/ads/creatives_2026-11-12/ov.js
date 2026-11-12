const {chromium}=require('playwright');const fs=require('fs');
const CSS=`@font-face{font-family:PJS;src:url(pjs.woff2) format('woff2');font-weight:200 800}
*{margin:0;box-sizing:border-box}html,body{width:1080px;height:1920px;background:transparent;font-family:PJS,sans-serif;overflow:hidden}
.abs{position:absolute;left:0;right:0}
.topscrim{position:absolute;top:0;left:0;right:0;height:1000px;background:linear-gradient(rgba(10,20,16,.55),rgba(10,20,16,.25) 45%,transparent)}
.botscrim{position:absolute;bottom:0;left:0;right:0;height:1050px;background:linear-gradient(transparent,rgba(10,20,16,.35) 40%,rgba(10,20,16,.62))}
.eyebrow{display:inline-block;background:rgba(15,46,37,.82);color:#EACB8E;font-size:25px;font-weight:700;letter-spacing:.2em;padding:14px 28px;border-radius:999px;border:1.5px solid rgba(234,203,142,.55)}
.h{color:#fff;font-weight:800;font-size:82px;line-height:1.04;letter-spacing:-.025em;text-shadow:0 4px 28px rgba(0,0,0,.35)}
.sub{color:#F4EEE4;font-weight:600;font-size:38px;line-height:1.25;text-shadow:0 2px 16px rgba(0,0,0,.4)}
.c{text-align:center;padding:0 80px}
.chip{display:inline-flex;align-items:center;gap:18px;background:rgba(255,255,255,.94);color:#133A2F;font-size:40px;font-weight:700;padding:20px 36px;border-radius:999px;box-shadow:0 10px 30px rgba(0,0,0,.18);margin:9px 0}
.chip i{width:16px;height:16px;border-radius:50%;background:#B5843A;display:block}
.cap{color:#fff;font-weight:800;font-size:66px;line-height:1.08;letter-spacing:-.02em;text-shadow:0 4px 24px rgba(0,0,0,.45)}
.panel{position:absolute;left:110px;top:850px;width:860px;height:440px;border-radius:36px;background:rgba(255,250,244,.58);border:2px solid rgba(255,255,255,.7);box-shadow:0 20px 60px rgba(0,0,0,.12);display:flex;flex-direction:column;justify-content:center;padding:0 56px}
.panel b{color:#B5843A;font-size:30px;letter-spacing:.22em;font-weight:800}
.panel p{color:#133A2F;font-size:62px;font-weight:800;line-height:1.08;letter-spacing:-.02em;margin-top:14px}
.card{position:absolute;inset:0;background:radial-gradient(120% 70% at 30% 20%,#2A6B57 0%,#1B4D3E 38%,#133A2F 75%,#0F2E25 100%)}
.card:after{content:'';position:absolute;inset:0;background:linear-gradient(115deg,transparent 30%,rgba(255,255,255,.06) 45%,transparent 60%)}
.logo{position:absolute;top:320px;left:0;right:0;text-align:center}.logo img{height:150px}
.hair{position:absolute;top:492px;left:390px;width:300px;height:2px;background:linear-gradient(90deg,transparent,#B5843A,transparent)}
.tile{position:absolute;top:520px;left:250px;width:580px;height:580px;border-radius:40px;overflow:hidden;background:#fff;box-shadow:0 30px 80px rgba(0,0,0,.35);border:3px solid rgba(234,203,142,.6)}
.tile img{width:100%;height:100%;object-fit:cover}
.name{position:absolute;top:1140px;left:60px;right:60px;text-align:center;color:#fff;font-size:54px;font-weight:800;letter-spacing:-.02em;line-height:1.1}
.price{position:absolute;top:1218px;left:0;right:0;text-align:center;color:#EACB8E;font-size:40px;font-weight:700}
.btn{position:absolute;top:1300px;left:290px;width:500px;height:112px;border-radius:999px;background:linear-gradient(180deg,#EACB8E,#C4924A);color:#0F2E25;font-size:44px;font-weight:800;display:flex;align-items:center;justify-content:center;gap:16px;box-shadow:0 16px 40px rgba(0,0,0,.3)}
.fine{position:absolute;top:1450px;left:0;right:0;text-align:center;color:#F4EEE4;font-size:30px;font-weight:600;line-height:1.5}
.fine span{color:#EACB8E}`;
const logo=fs.readFileSync('logo.svg','utf8');const logoUri='data:image/svg+xml;base64,'+Buffer.from(logo).toString('base64');
const img=f=>'data:image/jpeg;base64,'+fs.readFileSync(f).toString('base64');
const hook=(eb,h,sub)=>`<div class="topscrim"></div><div class="abs c" style="top:330px"><div class="eyebrow">${eb}</div><div class="h" style="margin-top:34px">${h}</div>${sub?`<div class="sub" style="margin-top:24px">${sub}</div>`:''}</div>`;
const chips=(arr)=>`<div class="abs c" style="top:1180px">${arr.map(t=>`<div><span class="chip"><i></i>${t}</span></div>`).join('')}</div>`;
const cap=(t,s)=>`<div class="botscrim"></div><div class="abs c" style="top:1240px"><div class="cap">${t}</div>${s?`<div class="sub" style="margin-top:20px">${s}</div>`:''}</div>`;
const panel=(b,p)=>`<div class="panel"><b>${b}</b><p>${p}</p></div>`;
const end=(im,name,price,fine)=>`<div class="card"></div><div class="logo"><img src="${logoUri}"></div><div class="hair"></div><div class="tile"><img src="${img(im)}"></div><div class="name">${name}</div><div class="price">${price}</div><div class="btn">Shop now <svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#0F2E25" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></div><div class="fine">${fine}</div>`;
const O={
 d1:hook('DEYGA · NOW SHIPPED FROM THE UK','The beetroot lip balm<br>you know from home.'),
 d2a:chips(['Beetroot extract']), d2b:chips(['Beetroot extract','Almond &amp; avocado oil']), d2c:chips(['Beetroot extract','Almond &amp; avocado oil','Shea butter']),
 d3a:cap('A sheer, rosy tint.'), d3b:cap('Lips feel soft<br>and supple.'),
 d4:cap('Official UK partner<br>of Deyga.','Dispatched from the UK · Free delivery over £40'),
 dend:end('deyga1.jpg','Deyga Beetroot Lip Balm','Classic 10 g · £10.99','Free UK delivery over £40<br><span>swansura.com</span>'),
 v1:hook('VILVAH · NOW SHIPPED FROM THE UK','Milk Drops.<br>Your daily milk serum.'),
 v2:chips(['Rice milk extract']), v3:chips(['Rice milk extract','Hyaluronic acid']),
 v3b:cap('Light, milky and<br>quick to absorb.'),
 vp1:panel('STEP 1','A few drops on<br>clean skin'), vp2:panel('STEP 2','Gently pat<br>it in'), vp3:panel('STEP 3','Follow with<br>moisturiser &amp; SPF'),
 v5:'<div class="topscrim"></div><div class="abs c" style="top:340px"><div class="cap">Fragrance-free.<br>For every skin type.</div><div class="sub" style="margin-top:20px">Official UK partner of Vilvah</div></div>',
 vend:end('vil0.jpg','Vilvah Milk Drops Serum','20 ml £21.99 · 40 ml £30.99','Free UK delivery over £40<br><span>swansura.com</span>'),
 mask:`<div style="position:absolute;inset:0;background:#000"></div><div style="position:absolute;left:110px;top:850px;width:860px;height:440px;border-radius:36px;background:#fff"></div>`
};
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
for(const [k,v] of Object.entries(O)){fs.writeFileSync('t.html',`<html><head><meta charset="utf-8"><style>${CSS}</style></head><body>${v}</body></html>`);
await p.goto('file://'+process.cwd()+'/t.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(150);
await p.screenshot({path:'ov/'+k+'.png',omitBackground:!(k.endsWith('end')||k=='mask')});}
await b.close()})();
