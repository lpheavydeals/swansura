// USP image ads (18 Nov 2026): 1 = UK prices / no customs, 2 = next-day UK delivery.
// node build.js  -> ../USP_<n>_<ratio>.jpg   (Plus Jakarta Sans only, Swansura emerald/brass)
const {chromium}=require('playwright');const fs=require('fs');
const b64=f=>`data:image/${f.endsWith('png')?'png':f.endsWith('svg')?'svg+xml':'webp'};base64,`+fs.readFileSync(f).toString('base64');
const TICK='<svg viewBox="0 0 24 24" width="1em" height="1em" fill="none" stroke="#EACB8E" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.2 4.2L19 7"/></svg>';
const ARR='<svg width="0.9em" height="0.9em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>';
const C={
 1:{h1:'Next-day delivery.',h2:'No import charges.',
    sub:'Vilvah &amp; Deyga from our UK stock. No overseas shipping fees, no customs or VAT to pay at your door.',
    ticks:['<b>Next-day</b> delivery £3.99','<b>VAT included</b> in every price','<b>100% genuine</b>, from the brands'],
    prods:[['p_milkdrops40.png',50,20,72],['p_betterageing.png',29,14,56],['lip_beet.png',71,14,50]],fine:'10% off Vilvah &amp; Deyga with code VD10 · Next-day: next working day after dispatch · T&amp;Cs apply'},
 2:{kind:'tiles',h1:'Skip the overseas delay',h2:'and import charges.',
    sub:'Genuine Vilvah &amp; Deyga, shipped from our UK stock.',
    tiles:[['truck','Next-day','UK delivery'],['shield','No customs','or import fees'],['tag','VAT included','UK prices']],
    prods:[['p_milkdrops40.png',50,20,74],['p_dg_vitc_wash.png',30,14,60],['p_dg_roseglow.png',72,14,50]],fine:'10% off Vilvah &amp; Deyga with code VD10 · Next-day: next working day after dispatch · T&amp;Cs apply'}};
const ICON={"truck": "<path d=\"M3 7h11v9H3zM14 10h4l3 3v3h-7z\"/><circle cx=\"7\" cy=\"17.5\" r=\"1.8\"/><circle cx=\"17\" cy=\"17.5\" r=\"1.8\"/>", "shield": "<path d=\"M12 3l7 3v5c0 4.5-3 8-7 10-4-2-7-5.5-7-10V6z\"/><path d=\"M8.5 12l2.4 2.4L15.5 10\"/>", "tag": "<path d=\"M3 12V4h8l10 10-8 8z\"/><circle cx=\"7.5\" cy=\"8.5\" r=\"1.4\"/>"};
const SZ={'4x5':[1080,1350],'1x1':[1080,1080],'9x16':[1080,1920]};
function html(c,W,H){const sq=W==H,tl=H>1500,k=sq?.86:1;
const padT=tl?250:sq?44:58, padB=tl?260:0;
return `<html><head><meta charset=utf-8><style>
@font-face{font-family:PJS;src:url(${b64('pjs.woff2')});font-weight:200 800}
*{margin:0;box-sizing:border-box}
body{width:${W}px;height:${H}px;overflow:hidden;font-family:PJS;color:#F4EEE4;
 background:radial-gradient(120% 75% at 25% 10%,#2A6B57 0%,#1B4D3E 38%,#133A2F 72%,#0F2E25 100%)}
.wrap{position:absolute;inset:${padT}px 0 ${padB}px 0;display:flex;flex-direction:column}
.top{display:flex;align-items:center;justify-content:space-between;padding:0 ${64*k}px}
.logo{height:${92*k}px}
.partner{display:flex;align-items:center;gap:${14*k}px}
.partner span{font-size:${17*k}px;font-weight:700;letter-spacing:.22em;text-transform:uppercase;color:#EACB8E;margin-right:${4*k}px;text-align:right;line-height:1.3}
.pill{background:#fff;border-radius:${14*k}px;height:${72*k}px;padding:0 ${18*k}px;display:flex;align-items:center;box-shadow:0 8px 22px rgba(0,0,0,.22)}
.pill img{height:${44*k}px}
.rule{height:2px;margin:${30*k}px ${64*k}px 0;background:linear-gradient(90deg,#B5843A,rgba(181,132,58,0))}
.head{position:relative;z-index:2;padding:${34*k}px ${64*k}px 0}
.h1{font-size:${(c.kind?80:86)*k}px;font-weight:800;letter-spacing:-.025em;line-height:1;color:#fff}
.h2{font-size:${(c.kind?80:86)*k}px;font-weight:800;letter-spacing:-.025em;line-height:1.05;color:#EACB8E}
.sub{margin-top:${22*k}px;max-width:${sq?900:880}px;font-size:${30*k}px;font-weight:500;line-height:1.35;color:#E6EFEA}
.stage{flex:1;position:relative;margin:${sq?10:24}px ${64*k}px 0;min-height:0}
.arch{position:absolute;left:50%;transform:translateX(-50%);top:0;bottom:16%;width:min(66%,calc((100% - 0px)*1));aspect-ratio:auto;border-radius:999px 999px 28px 28px;
 background:linear-gradient(180deg,rgba(244,248,245,.16),rgba(244,248,245,.05));border:1.5px solid rgba(234,203,142,.45)}
.plinth{position:absolute;left:50%;transform:translateX(-50%);bottom:3%;width:80%;height:22%}
.plinth .face{position:absolute;left:0;right:0;bottom:0;height:46%;border-radius:0 0 18px 18px;background:linear-gradient(180deg,#D9C3A0,#B5843A);box-shadow:0 26px 40px -14px rgba(0,0,0,.55)}
.plinth .top{position:absolute;left:0;right:0;top:0;height:76%;border-radius:50%;background:radial-gradient(120% 140% at 50% 30%,#FBF7F0 0%,#F1E7D6 55%,#E3D2B6 100%);box-shadow:inset 0 -6px 14px rgba(150,110,50,.25)}
.item{position:absolute;transform:translateX(-50%);object-fit:contain;filter:drop-shadow(0 14px 14px rgba(40,25,10,.28)) drop-shadow(0 3px 3px rgba(40,25,10,.22))}

.cmp{display:flex;gap:${18*k}px;margin:${sq?18:30}px ${64*k}px 0;position:relative;z-index:2}
.card{flex:1;border-radius:${20*k}px;padding:${24*k}px ${26*k}px}
.card h3{font-size:${21*k}px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;margin-bottom:${14*k}px}
.card li{list-style:none;display:flex;gap:${10*k}px;align-items:flex-start;font-size:${25*k}px;line-height:1.3;margin-top:${12*k}px}
.card li i{flex:none;font-style:normal;font-weight:800;width:1.1em;text-align:center}
.bad{background:rgba(15,46,37,.55);border:1.5px solid rgba(244,238,228,.18);color:rgba(244,238,228,.78)}
.bad h3{color:rgba(244,238,228,.6)}.bad i{color:#D98C7E}
.good{background:linear-gradient(180deg,#FBF7F0,#F1E7D6);color:#133A2F;border:2px solid #EACB8E;box-shadow:0 18px 40px -16px rgba(0,0,0,.6)}
.good h3{color:#8C6226}.good i{color:#1B4D3E}.good b{font-weight:800}
.tiles{display:flex;gap:${16*k}px;margin:${sq?18:28}px ${64*k}px 0;position:relative;z-index:2}
.tile{flex:1;display:flex;align-items:center;gap:${14*k}px;background:linear-gradient(180deg,#FBF7F0,#F1E7D6);border:1.5px solid #EACB8E;border-radius:${18*k}px;padding:${18*k}px ${18*k}px;color:#133A2F;box-shadow:0 14px 30px -14px rgba(0,0,0,.55)}
.tile .ic{flex:none;width:${54*k}px;height:${54*k}px;border-radius:50%;background:#1B4D3E;display:flex;align-items:center;justify-content:center}
.tile .ic svg{width:58%;height:58%;fill:none;stroke:#EACB8E;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round}
.tile b{display:block;font-size:${24*k}px;font-weight:800;line-height:1.15}
.tile span{display:block;font-size:${19*k}px;font-weight:600;color:#4B3E33;line-height:1.2}
.seal{position:absolute;z-index:3;right:${sq?2:0}%;top:${sq?2:4}%;width:${(tl?230:sq?175:205)}px;height:${(tl?230:sq?175:205)}px;border-radius:50%;
 background:radial-gradient(circle at 35% 30%,#F6E2B4,#EACB8E 45%,#C4924A 100%);color:#0F2E25;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;
 box-shadow:0 18px 36px -12px rgba(0,0,0,.6),inset 0 0 0 ${6*k}px rgba(255,255,255,.25);transform:rotate(-8deg)}
.seal::after{content:'';position:absolute;inset:${9*k}px;border-radius:50%;border:1.5px dashed rgba(15,46,37,.45)}
.seal .x{font-size:${(tl?17:sq?13:15)}px;font-weight:800;letter-spacing:.18em;text-transform:uppercase}
.seal .p{font-size:${(tl?76:sq?56:66)}px;font-weight:800;line-height:.95;letter-spacing:-.03em}
.seal .o{font-size:${(tl?22:sq?16:19)}px;font-weight:800;letter-spacing:.12em;text-transform:uppercase}
.seal .c{margin-top:${4*k}px;font-size:${(tl?16:sq?12:14)}px;font-weight:700;background:#0F2E25;color:#EACB8E;border-radius:999px;padding:${3*k}px ${10*k}px}
.ticks{display:flex;justify-content:space-between;gap:${14*k}px;padding:${sq?18:30}px ${64*k}px ${sq?20:30}px}
.ticks div{flex:1;display:flex;gap:${10*k}px;align-items:flex-start;font-size:${22*k}px;line-height:1.3;color:#F4EEE4}
.ticks svg{flex:none;font-size:${28*k}px;margin-top:-1px}
.ticks b{font-weight:800;color:#fff}
.bar{display:flex;align-items:center;justify-content:space-between;background:#F4EEE4;color:#133A2F;padding:${22*k}px ${64*k}px}
.bar .fine{font-size:${18*k}px;font-weight:600;color:#4B3E33;max-width:62%;line-height:1.3}
.btn{display:flex;align-items:center;gap:${12*k}px;background:linear-gradient(180deg,#EACB8E,#C4924A);color:#0F2E25;font-weight:800;font-size:${34*k}px;padding:${20*k}px ${38*k}px;border-radius:999px;box-shadow:0 10px 24px rgba(0,0,0,.18)}
${tl?'.bar{position:absolute;left:0;right:0;bottom:-'+(padB-40)+'px}':''}
</style></head><body><div class="wrap">
<div class="top"><img class="logo" src="${b64('swansura-logo-white.svg')}">
<div class="partner"><span>Official UK<br>partner of</span><div class="pill"><img src="${b64('vilvah.webp')}"></div><div class="pill"><img src="${b64('deyga.webp')}"></div></div></div>
<div class="rule"></div>
<div class="head"><div class="h1">${c.h1}</div><div class="h2">${c.h2}</div>${c.sub?`<div class="sub">${c.sub}</div>`:''}</div>
${c.kind=='tiles'?`<div class="tiles">${c.tiles.map(([i,b,t])=>`<div class="tile"><div class="ic"><svg viewBox="0 0 24 24">${ICON[i]}</svg></div><div><b>${b}</b><span>${t}</span></div></div>`).join('')}</div>`:''}${c.kind=='cmp'?`<div class="cmp"><div class="card bad"><h3>Ordered from overseas</h3><ul>${c.bad.map(t=>`<li><i>✕</i><span>${t}</span></li>`).join('')}</ul></div><div class="card good"><h3>With Swansura</h3><ul>${c.good.map(t=>`<li><i>✓</i><span>${t}</span></li>`).join('')}</ul></div></div>`:''}<div class="stage"><div class="arch"></div><div class="seal"><div class="x">Exclusive</div><div class="p">10%</div><div class="o">off</div><div class="c">Code VD10</div></div><div class="plinth"><div class="face"></div><div class="top"></div></div>${c.prods.map(([f,x,bo,h])=>`<img class="item" style="left:${x}%;bottom:${bo}%;height:${tl?Math.round(h*.72):h}%" src="${b64(f)}">`).join('')}</div>
${c.kind?'':`<div class="ticks">${c.ticks.map(t=>`<div>${TICK}<span>${t}</span></div>`).join('')}</div>`}
<div class="bar"><div class="fine">${c.fine}</div><div class="btn">Shop now ${ARR}</div></div>
</div></body></html>`}
(async()=>{const b=await chromium.launch();
for(const n of Object.keys(C))for(const [r,[W,H]] of Object.entries(SZ)){
 const p=await b.newPage({viewport:{width:W,height:H},deviceScaleFactor:1});
 await p.setContent(html(C[n],W,H));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
 await p.screenshot({path:`../USP_${n}_${r}.jpg`,type:'jpeg',quality:92});await p.close();console.log(n,r)}
await b.close()})();
