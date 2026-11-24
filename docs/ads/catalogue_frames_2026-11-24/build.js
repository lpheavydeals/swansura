// Catalogue ad frames (24 Nov 2026): transparent 1080x1080 PNGs laid over Meta catalogue product photos
// (white 1:1, bottle in the middle). Plus Jakarta Sans only. node build.js -> frame_emerald.png, frame_white.png
const {chromium}=require('playwright');const fs=require('fs');const S='../fragrance_2026-11-22/src/';
const b64=(f,t)=>`data:${t};base64,`+fs.readFileSync(S+f).toString('base64');
const FONT=b64('pjs.woff2','font/woff2');
const T={emerald:{edge:'#1B4D3E',band:'linear-gradient(180deg,#1F5646,#133A2F)',hair:'#EACB8E',txt:'#F4EEE4',acc:'#EACB8E',logo:b64('logo_w.svg','image/svg+xml')},
         white:{edge:'#FFFFFF',band:'#FBF8F3',hair:'#B5843A',txt:'#1B4D3E',acc:'#8C6226',logo:b64('logo_b.svg','image/svg+xml')}};
(async()=>{const b=await chromium.launch();
for(const [k,c] of Object.entries(T)){
 const html=`<html><head><style>@font-face{font-family:PJS;src:url(${FONT});font-weight:200 800}
 *{margin:0;box-sizing:border-box}html,body{width:1080px;height:1080px;background:transparent;font-family:PJS}
 .edge{position:absolute;inset:0;border:22px solid ${c.edge}}
 .hair{position:absolute;inset:132px 34px 34px 34px;border:2px solid ${c.hair};border-top:none}
 .band{position:absolute;left:0;right:0;top:0;height:120px;background:${c.band};display:flex;align-items:center;justify-content:space-between;padding:0 46px;border-bottom:2px solid ${c.hair}}
 .band img{height:78px}
 .t{text-align:right;color:${c.txt};font-weight:700;font-size:25px;letter-spacing:.14em;text-transform:uppercase;line-height:1.35}
 .t i{font-style:normal;color:${c.acc}}
 </style></head><body><div class=edge></div><div class=hair></div>
 <div class=band><img src="${c.logo}"><div class=t>100% authentic<br><i>Shipped from the UK</i></div></div></body></html>`;
 const p=await b.newPage({viewport:{width:1080,height:1080}});await p.setContent(html);await p.evaluate(()=>document.fonts.ready);
 await p.screenshot({path:`frame_${k}.png`,omitBackground:true});await p.close();console.log('frame',k);}
await b.close()})();
