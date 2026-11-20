// USP image 3 (20 Nov 2026): light 'UK price list' look, 4 products with real prices + VD10 price. node build3.js
const {chromium}=require('playwright');const fs=require('fs');
const b64=f=>`data:image/${f.endsWith('png')?'png':f.endsWith('svg')?'svg+xml':'webp'};base64,`+fs.readFileSync(f).toString('base64');
const P=[['p_milkdrops40.png','Vilvah','Milk Drops Serum 40 ml',30.99],['p_facewash.png','Vilvah','Milk Powder Face Wash 50 g',13.99],
         ['p_dg_vitc_wash.png','Deyga','Vitamin C Foaming Face Wash',15.99],['p_dg_roseglow.png','Deyga','Rose Glow Serum 30 ml',17.99]];
const vd=p=>(p-Math.round(p*10)/100).toFixed(2);
const SZ={'4x5':[1080,1350],'1x1':[1080,1080],'9x16':[1080,1920]};
const TICK='<svg viewBox="0 0 24 24" width="1em" height="1em" fill="none" stroke="#B5843A" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.2 4.2L19 7"/></svg>';
function html(W,H){const sq=W==H,tl=H>1500,cols=sq?4:2,padT=tl?250:sq?40:52,padB=tl?250:0;
return `<html><head><meta charset=utf-8><style>
@font-face{font-family:PJS;src:url(${b64('pjs.woff2')});font-weight:200 800}
*{margin:0;box-sizing:border-box}body{width:${W}px;height:${H}px;overflow:hidden;font-family:PJS;color:#1F1A17;background:linear-gradient(180deg,#FBF8F3,#F3ECE1)}
.wrap{position:absolute;inset:${padT}px 0 ${padB}px 0;display:flex;flex-direction:column}
.top{display:flex;align-items:center;justify-content:space-between;padding:0 60px}.logo{height:${sq?78:92}px}
.partner{display:flex;align-items:center;gap:12px}.partner span{font-size:16px;font-weight:700;letter-spacing:.22em;color:#695541;text-align:right;line-height:1.3}
.pill{background:#fff;border:1px solid #E3DACD;border-radius:14px;height:${sq?60:70}px;padding:0 16px;display:flex;align-items:center}.pill img{height:${sq?36:42}px}
.rule{height:2px;margin:${sq?22:28}px 60px 0;background:linear-gradient(90deg,#B5843A,rgba(181,132,58,0))}
.head{padding:${sq?20:tl?30:22}px 60px 0}.h1{font-size:${sq?70:tl?84:74}px;font-weight:800;letter-spacing:-.025em;line-height:1.02;color:#1B4D3E}.h1 em{font-style:normal;color:#B5843A}
.ticks{margin-top:${sq?14:20}px;display:flex;gap:26px;flex-wrap:wrap;font-size:${sq?23:26}px;font-weight:700;color:#133A2F}.ticks span{display:flex;align-items:center;gap:8px}
.grid{flex:1;min-height:0;display:grid;grid-template-columns:repeat(${cols},1fr);gap:${sq?14:20}px;padding:${sq?20:tl?30:22}px 60px ${sq?20:tl?30:22}px}
.card{background:#fff;border:1.5px solid #E8DCC6;border-radius:20px;display:flex;flex-direction:column;overflow:hidden;box-shadow:0 14px 30px -18px rgba(60,40,10,.35)}
.ph{flex:1;min-height:0;background:radial-gradient(90% 80% at 50% 45%,#F4F8F5,#E3EDE7);display:flex;align-items:flex-end;justify-content:center;padding:${sq?10:18}px 10px 6px}
.ph img{max-height:100%;max-width:92%;object-fit:contain;filter:drop-shadow(0 10px 10px rgba(40,25,10,.22))}
.info{padding:${sq?10:14}px ${sq?12:18}px ${sq?12:16}px}.br{font-size:${sq?13:15}px;font-weight:800;letter-spacing:.2em;text-transform:uppercase;color:#695541}
.nm{font-size:${sq?16:21}px;font-weight:700;line-height:1.2;margin-top:3px;min-height:${sq?2.4:1.2}em}
.pr{display:flex;align-items:center;justify-content:space-between;gap:8px;margin-top:${sq?8:10}px;flex-wrap:wrap}.was{font-size:${sq?20:26}px;font-weight:800;color:#1F1A17}
.now{background:#1B4D3E;color:#fff;border-radius:999px;padding:${sq?4:6}px ${sq?10:14}px;font-size:${sq?14:18}px;font-weight:700}.now b{color:#EACB8E;font-weight:800}
.bar{display:flex;align-items:center;justify-content:space-between;gap:20px;background:radial-gradient(120% 140% at 20% 0%,#2A6B57,#1B4D3E 50%,#133A2F);color:#F4EEE4;padding:${sq?20:26}px 60px}
.bar .t{font-size:${sq?26:30}px;font-weight:800;line-height:1.15}.bar .t em{font-style:normal;color:#EACB8E}.bar .f{font-size:${sq?14:16}px;font-weight:500;color:rgba(244,238,228,.75);margin-top:6px}
.btn{flex:none;background:linear-gradient(180deg,#EACB8E,#C4924A);color:#0F2E25;font-weight:800;font-size:${sq?28:32}px;padding:${sq?16:18}px ${sq?28:34}px;border-radius:999px}
${tl?`.bar{position:absolute;left:0;right:0;bottom:-${padB-40}px}`:''}
</style></head><body><div class="wrap">
<div class="top"><img class="logo" src="${b64('swansura-logo-brown.svg')}"><div class="partner"><span>OFFICIAL UK<br>PARTNER OF</span><div class="pill"><img src="${b64('vilvah.webp')}"></div><div class="pill"><img src="${b64('deyga.webp')}"></div></div></div>
<div class="rule"></div>
<div class="head"><div class="h1">Vilvah &amp; Deyga<br><em>at UK prices</em></div>
<div class="ticks"><span>${TICK}VAT included</span><span>${TICK}No customs</span><span>${TICK}Next-day delivery</span></div></div>
<div class="grid">${P.map(([f,b,n,p])=>`<div class="card"><div class="ph"><img src="${b64(f)}"></div><div class="info"><div class="br">${b}</div><div class="nm">${n}</div><div class="pr"><span class="was">£${p.toFixed(2)}</span><span class="now"><b>£${vd(p)}</b> with VD10</span></div></div></div>`).join('')}</div>
<div class="bar"><div><div class="t">Extra <em>10% off</em> Vilvah &amp; Deyga<br>with code <em>VD10</em></div><div class="f">One code per order · Next-day: next working day after dispatch · T&amp;Cs apply</div></div><div class="btn">Shop now &rarr;</div></div>
</div></body></html>`}
(async()=>{const b=await chromium.launch();for(const [r,[W,H]] of Object.entries(SZ)){const p=await b.newPage({viewport:{width:W,height:H}});await p.setContent(html(W,H));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);await p.screenshot({path:`../USP_3_${r}.jpg`,type:'jpeg',quality:92});await p.close();console.log(r)}await b.close()})();
