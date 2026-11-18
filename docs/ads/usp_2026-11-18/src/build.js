// USP image ads (18 Nov 2026): 1 = UK prices / no customs, 2 = next-day UK delivery.
// node build.js  -> ../USP_<n>_<ratio>.jpg   (Plus Jakarta Sans only, Swansura emerald/brass)
const {chromium}=require('playwright');const fs=require('fs');
const b64=f=>`data:image/${f.endsWith('png')?'png':f.endsWith('svg')?'svg+xml':'webp'};base64,`+fs.readFileSync(f).toString('base64');
const TICK='<svg viewBox="0 0 24 24" width="1em" height="1em" fill="none" stroke="#EACB8E" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.2 4.2L19 7"/></svg>';
const ARR='<svg width="0.9em" height="0.9em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>';
const C={
 1:{eb:'Official UK partner of',h1:'Vilvah &amp; Deyga',h2:'at UK prices',
    sub:'No customs charges. No import fees at your door.<br>VAT already included.',
    ticks:['<b>100% genuine</b>, straight from the brands','<b>Dispatched from the UK</b>','<b>Free UK delivery</b> over £40'],
    prods:['fbk.png','lip.png'],fine:'swansura.com · T&amp;Cs apply'},
 2:{eb:'Official UK partner of',h1:'Next-day',h2:'UK delivery',
    sub:'Genuine Vilvah &amp; Deyga, dispatched from<br>our UK stock. No waiting on overseas parcels.',
    ticks:['<b>Next-day</b> delivery £3.99','<b>Free UK delivery</b> over £40','<b>100% genuine</b>, from the brands'],
    prods:['apm.png','lip_beet.png'],fine:'Next working day after dispatch · swansura.com · T&amp;Cs apply'}};
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
.h1{font-size:${92*k}px;font-weight:800;letter-spacing:-.025em;line-height:1;color:#fff}
.h2{font-size:${92*k}px;font-weight:800;letter-spacing:-.025em;line-height:1.05;color:#EACB8E}
.sub{margin-top:${22*k}px;font-size:${30*k}px;font-weight:500;line-height:1.35;color:#E6EFEA}
.stage{flex:1;position:relative;margin:${sq?14:30}px ${64*k}px 0;min-height:0}
.disc{position:absolute;left:50%;top:2%;height:96%;aspect-ratio:1;transform:translateX(-50%);border-radius:50%;
 background:radial-gradient(circle at 50% 45%,#F4F8F5 0%,#E4EEE9 62%,rgba(228,238,233,0) 63%)}
.prods{position:absolute;inset:0;display:flex;align-items:flex-end;justify-content:center;gap:${10*k}px;padding-bottom:${sq?4:12}px}
.prods img{max-height:92%;max-width:56%;object-fit:contain;filter:drop-shadow(0 22px 24px rgba(0,0,0,.35))}
.prods img+img{max-height:74%;max-width:40%}
.ticks{display:flex;justify-content:space-between;gap:${14*k}px;padding:${sq?18:30}px ${64*k}px ${sq?20:30}px}
.ticks div{flex:1;display:flex;gap:${10*k}px;align-items:flex-start;font-size:${22*k}px;line-height:1.3;color:#F4EEE4}
.ticks svg{flex:none;font-size:${28*k}px;margin-top:-1px}
.ticks b{font-weight:800;color:#fff}
.bar{display:flex;align-items:center;justify-content:space-between;background:#F4EEE4;color:#133A2F;padding:${22*k}px ${64*k}px}
.bar .fine{font-size:${21*k}px;font-weight:600;color:#4B3E33;max-width:62%;line-height:1.3}
.btn{display:flex;align-items:center;gap:${12*k}px;background:linear-gradient(180deg,#EACB8E,#C4924A);color:#0F2E25;font-weight:800;font-size:${34*k}px;padding:${20*k}px ${38*k}px;border-radius:999px;box-shadow:0 10px 24px rgba(0,0,0,.18)}
${tl?'.bar{position:absolute;left:0;right:0;bottom:-'+(padB-40)+'px}':''}
</style></head><body><div class="wrap">
<div class="top"><img class="logo" src="${b64('swansura-logo-white.svg')}">
<div class="partner"><span>${c.eb.replace('UK partner','UK<br>partner')}</span><div class="pill"><img src="${b64('vilvah.webp')}"></div><div class="pill"><img src="${b64('deyga.webp')}"></div></div></div>
<div class="rule"></div>
<div class="head"><div class="h1">${c.h1}</div><div class="h2">${c.h2}</div><div class="sub">${c.sub}</div></div>
<div class="stage"><div class="disc"></div><div class="prods">${c.prods.map(p=>`<img src="${b64(p)}">`).join('')}</div></div>
<div class="ticks">${c.ticks.map(t=>`<div>${TICK}<span>${t}</span></div>`).join('')}</div>
<div class="bar"><div class="fine">${c.fine}</div><div class="btn">Shop now ${ARR}</div></div>
</div></body></html>`}
(async()=>{const b=await chromium.launch();
for(const n of Object.keys(C))for(const [r,[W,H]] of Object.entries(SZ)){
 const p=await b.newPage({viewport:{width:W,height:H},deviceScaleFactor:1});
 await p.setContent(html(C[n],W,H));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
 await p.screenshot({path:`../USP_${n}_${r}.jpg`,type:'jpeg',quality:92});await p.close();console.log(n,r)}
await b.close()})();
