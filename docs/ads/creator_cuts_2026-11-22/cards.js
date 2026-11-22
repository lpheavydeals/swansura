// End card + top pill for the creator cuts (22 Nov 2026). node cards.js -> end.png (1080x1920), pill.png (transparent)
const {chromium}=require('playwright');const fs=require('fs');const S='../usp_2026-11-18/src/';
const b64=f=>`data:image/${f.endsWith('png')?'png':f.endsWith('svg')?'svg+xml':'webp'};base64,`+fs.readFileSync(S+f).toString('base64');
const font=`@font-face{font-family:PJS;src:url(${b64('pjs.woff2')});font-weight:200 800}*{margin:0;box-sizing:border-box}`;
const end=`<html><head><style>${font}body{width:1080px;height:1920px;font-family:PJS;color:#F4EEE4;background:radial-gradient(110% 70% at 50% 30%,#245F4D,#133A2F 60%,#0F2E25);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:250px 64px 330px}
.logo{height:150px}h2{margin-top:44px;font-size:64px;font-weight:800;letter-spacing:-.02em;line-height:1.1;color:#fff}h2 em{font-style:normal;color:#EACB8E}
.row{margin-top:34px;display:flex;gap:16px;align-items:center}.row span{font-size:17px;font-weight:700;letter-spacing:.22em;color:#EACB8E;margin-right:6px}
.pill{background:#fff;border-radius:14px;height:72px;padding:0 18px;display:flex;align-items:center}.pill img{height:44px}
.code{margin-top:40px;font-size:38px;font-weight:700}.code b{color:#0F2E25;background:linear-gradient(180deg,#EACB8E,#C4924A);padding:4px 16px;border-radius:10px;font-weight:800}
.btn{margin-top:40px;background:linear-gradient(180deg,#EACB8E,#C4924A);color:#0F2E25;font-weight:800;font-size:40px;padding:22px 52px;border-radius:999px}
.url{margin-top:20px;font-size:30px;font-weight:700}.fine{margin-top:28px;font-size:20px;color:rgba(244,238,228,.75);line-height:1.4}</style></head><body>
<img class="logo" src="${b64('swansura-logo-white.svg')}"><h2>Vilvah &amp; Deyga<br><em>with next-day UK delivery</em></h2>
<div class="row"><span>OFFICIAL UK<br>PARTNER OF</span><div class="pill"><img src="${b64('vilvah.webp')}"></div><div class="pill"><img src="${b64('deyga.webp')}"></div></div>
<div class="code">Extra 10% off with <b>VD10</b></div><div class="btn">Shop now &rarr;</div><div class="url">swansura.com</div>
<div class="fine">10% off Vilvah &amp; Deyga with code VD10 · one code per order<br>Next-day: next working day after dispatch · T&amp;Cs apply</div></body></html>`;
const pill=`<html><head><style>${font}body{width:1080px;height:200px;background:transparent;display:flex;justify-content:center;align-items:center;font-family:PJS}
.p{display:flex;align-items:center;gap:14px;background:rgba(15,46,37,.88);border:1.5px solid rgba(234,203,142,.7);border-radius:999px;padding:12px 26px 12px 16px;color:#F4EEE4;font-size:28px;font-weight:600}
.p img{height:46px}.p b{color:#EACB8E;font-weight:800}</style></head><body><div class="p"><img src="${b64('swansura-logo-white.svg')}"><span>At Swansura · <b>next-day UK delivery</b></span></div></body></html>`;
(async()=>{const b=await chromium.launch();
let p=await b.newPage({viewport:{width:1080,height:1920}});await p.setContent(end);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);await p.screenshot({path:'end.png'});
p=await b.newPage({viewport:{width:1080,height:200}});await p.setContent(pill);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);await p.screenshot({path:'pill.png',omitBackground:true});
await b.close()})();
