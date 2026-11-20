// USP videos (20 Nov 2026): 2 x 20 s, 9:16 + 4:5. Frames rendered with Playwright, encoded with ffmpeg.
// node vid.js <1|2> <916|45>   -> frames in ./fr_<n>_<r>/ ; then enc.sh
const {chromium}=require('playwright');const fs=require('fs');const S='../usp_2026-11-18/src/';
const b64=f=>`data:image/${f.endsWith('png')?'png':f.endsWith('svg')?'svg+xml':'webp'};base64,`+fs.readFileSync(S+f).toString('base64');
const FPS=25,DUR=20;
const V={
 1:{prods:[['p_milkdrops40.png',50,20,72],['p_betterageing.png',29,14,56],['lip_beet.png',71,14,50]],
   cards:[[0,3,'Love <em>Vilvah</em> &amp; <em>Deyga</em>?','Official UK partner'],
          [3,6,'<em>Next-day</em> UK delivery','Dispatched from our UK stock'],
          [6,9,'<em>No import</em> charges','No customs or VAT at your door'],
          [9,12,'<em>VAT included</em> UK prices','100% genuine, from the brands'],
          [12,14,'<em>Exclusive</em> 10% off','On Vilvah &amp; Deyga'],
          [14,16,'Use code <em>VD10</em>','In your bag or at checkout']],seal:12.2},
 2:{prods:[['p_milkdrops40.png',50,20,74],['p_dg_vitc_wash.png',30,14,60],['p_dg_roseglow.png',72,14,50]],
   cards:[[0,3,'Skip the <em>overseas delay</em>','Genuine Vilvah &amp; Deyga'],
          [3,6,'&hellip;and the <em>import charges</em>','Shipped from our UK stock'],
          [6,8.5,'<em>Next-day</em> UK delivery','Order in the UK, delivered in the UK'],
          [8.5,11,'<em>No customs</em> or import fees','Nothing extra at your door'],
          [11,13.5,'<em>VAT included</em> in every price','The price you see is the price you pay'],
          [13.5,16,'<em>Exclusive</em> 10% off','Vilvah &amp; Deyga with code VD10']],seal:13.7}};
const n=+process.argv[2],r=process.argv[3],[W,H]=r=='916'?[1080,1920]:[1080,1350],tl=H>1500,c=V[n];
const top=tl?250:50, bot=tl?330:60;
const html=`<html><head><meta charset=utf-8><style>
@font-face{font-family:PJS;src:url(${b64('pjs.woff2')});font-weight:200 800}
*{margin:0;box-sizing:border-box}body{width:${W}px;height:${H}px;overflow:hidden;font-family:PJS;color:#F4EEE4;position:relative;
 background:radial-gradient(120% 75% at 25% 10%,#2A6B57 0%,#1B4D3E 38%,#133A2F 72%,#0F2E25 100%)}
#glow{position:absolute;width:900px;height:900px;border-radius:50%;background:radial-gradient(circle,rgba(234,203,142,.16),rgba(234,203,142,0) 65%);left:90px;top:${tl?700:380}px}
.hdr{position:absolute;left:64px;right:64px;top:${top}px;display:flex;align-items:center;justify-content:space-between}
.hdr .logo{height:92px}.partner{display:flex;align-items:center;gap:14px}
.partner span{font-size:17px;font-weight:700;letter-spacing:.22em;text-transform:uppercase;color:#EACB8E;text-align:right;line-height:1.3}
.pill{background:#fff;border-radius:14px;height:72px;padding:0 18px;display:flex;align-items:center;box-shadow:0 8px 22px rgba(0,0,0,.22)}.pill img{height:44px}
.rule{position:absolute;left:64px;right:64px;top:${top+122}px;height:2px;background:linear-gradient(90deg,#B5843A,rgba(181,132,58,0))}
.card{position:absolute;left:64px;right:64px;top:${top+160}px;opacity:0}
.card h1{font-size:${tl?98:76}px;font-weight:800;letter-spacing:-.025em;line-height:1.02;color:#fff}.card h1 em{font-style:normal;color:#EACB8E}
.card p{margin-top:${tl?20:14}px;font-size:${tl?34:30}px;font-weight:600;color:#E6EFEA}
.stage{position:absolute;left:64px;right:64px;top:${tl?760:500}px;bottom:${tl?bot+110:110}px}
.arch{position:absolute;left:50%;transform:translateX(-50%);top:0;bottom:16%;width:66%;border-radius:999px 999px 28px 28px;background:linear-gradient(180deg,rgba(244,248,245,.16),rgba(244,248,245,.05));border:1.5px solid rgba(234,203,142,.45)}
.plinth{position:absolute;left:50%;transform:translateX(-50%);bottom:3%;width:80%;height:22%}
.plinth .face{position:absolute;left:0;right:0;bottom:0;height:46%;border-radius:0 0 18px 18px;background:linear-gradient(180deg,#D9C3A0,#B5843A);box-shadow:0 26px 40px -14px rgba(0,0,0,.55)}
.plinth .tp{position:absolute;left:0;right:0;top:0;height:76%;border-radius:50%;background:radial-gradient(120% 140% at 50% 30%,#FBF7F0 0%,#F1E7D6 55%,#E3D2B6 100%);box-shadow:inset 0 -6px 14px rgba(150,110,50,.25)}
.item{position:absolute;object-fit:contain;filter:drop-shadow(0 14px 14px rgba(40,25,10,.28)) drop-shadow(0 3px 3px rgba(40,25,10,.22))}
.sweep{position:absolute;inset:0;overflow:hidden;pointer-events:none}.sweep i{position:absolute;top:-20%;bottom:-20%;width:18%;background:linear-gradient(90deg,rgba(255,255,255,0),rgba(255,255,255,.18),rgba(255,255,255,0));transform:skewX(-18deg)}
.seal{position:absolute;z-index:3;right:0;top:2%;width:230px;height:230px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#F6E2B4,#EACB8E 45%,#C4924A 100%);color:#0F2E25;display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:0 18px 36px -12px rgba(0,0,0,.6);opacity:0}
.seal::after{content:'';position:absolute;inset:10px;border-radius:50%;border:1.5px dashed rgba(15,46,37,.45)}
.seal .x{font-size:17px;font-weight:800;letter-spacing:.18em}.seal .p{font-size:76px;font-weight:800;line-height:.95;letter-spacing:-.03em}.seal .o{font-size:22px;font-weight:800;letter-spacing:.12em}
.seal .c{margin-top:4px;font-size:16px;font-weight:700;background:#0F2E25;color:#EACB8E;border-radius:999px;padding:3px 12px}
.dots{position:absolute;left:0;right:0;bottom:${bot+40}px;display:flex;justify-content:center;gap:10px}.dots i{width:10px;height:10px;border-radius:50%;background:rgba(244,238,228,.3)}.dots i.on{background:#EACB8E;width:30px;border-radius:6px}
.end{position:absolute;inset:0;background:radial-gradient(110% 70% at 50% 30%,#245F4D,#133A2F 60%,#0F2E25);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;opacity:0;padding:${top}px 64px ${bot}px}
.end .logo{height:150px}.end h2{margin-top:44px;font-size:64px;font-weight:800;letter-spacing:-.02em;line-height:1.08;color:#fff}.end h2 em{font-style:normal;color:#EACB8E}
.end .row{margin-top:34px;display:flex;gap:16px;align-items:center}.end .row span{font-size:17px;font-weight:700;letter-spacing:.22em;color:#EACB8E;margin-right:6px}
.end .btn{margin-top:46px;background:linear-gradient(180deg,#EACB8E,#C4924A);color:#0F2E25;font-weight:800;font-size:40px;padding:22px 52px;border-radius:999px}
.end .url{margin-top:22px;font-size:30px;font-weight:700;color:#F4EEE4}
.end .fine{margin-top:30px;font-size:20px;font-weight:500;color:rgba(244,238,228,.75);line-height:1.4}
</style></head><body><div id="glow"></div>
<div class="hdr"><img class="logo" src="${b64('swansura-logo-white.svg')}"><div class="partner"><span>Official UK<br>partner of</span><div class="pill"><img src="${b64('vilvah.webp')}"></div><div class="pill"><img src="${b64('deyga.webp')}"></div></div></div><div class="rule"></div>
${c.cards.map((k,i)=>`<div class="card" id="c${i}"><h1>${k[2]}</h1><p>${k[3]}</p></div>`).join('')}
<div class="stage" id="stage"><div class="arch"></div><div class="plinth"><div class="face"></div><div class="tp"></div></div>
${c.prods.map(([f,x,bo,h],i)=>`<img class="item" id="p${i}" style="left:${x}%;bottom:${bo}%;height:${h}%" src="${b64(f)}">`).join('')}
<div class="sweep"><i id="sw"></i></div>
<div class="seal" id="seal"><div class="x">EXCLUSIVE</div><div class="p">10%</div><div class="o">OFF</div><div class="c">Code VD10</div></div></div>
<div class="dots">${c.cards.map((k,i)=>`<i id="d${i}"></i>`).join('')}</div>
<div class="end" id="end"><img class="logo" src="${b64('swansura-logo-white.svg')}">
<h2>${n==1?'Next-day delivery.<br><em>No import charges.</em>':'Genuine Vilvah &amp; Deyga,<br><em>from our UK stock.</em>'}</h2>
<div class="row"><span>OFFICIAL UK<br>PARTNER OF</span><div class="pill"><img src="${b64('vilvah.webp')}"></div><div class="pill"><img src="${b64('deyga.webp')}"></div></div>
<div class="btn">Shop now &rarr;</div><div class="url">swansura.com</div>
<div class="fine">10% off Vilvah &amp; Deyga with code VD10 · one code per order<br>Next-day: next working day after dispatch · T&amp;Cs apply</div></div>
<script>
const C=${JSON.stringify(c.cards.map(k=>[k[0],k[1]]))},SEAL=${c.seal},P=${c.prods.length};
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x)),ease=x=>1-Math.pow(1-cl(x),3),back=x=>{x=cl(x);const s=1.7;return 1+(s+1)*Math.pow(x-1,3)+s*Math.pow(x-1,2)};
window.render=t=>{
 C.forEach(([a,b],i)=>{const e=document.getElementById('c'+i),fi=ease((t-a)/.4),fo=b>=16?1:1-cl((t-(b-.25))/.25);e.style.opacity=Math.min(fi,fo);e.style.transform='translateY('+(1-fi)*40+'px)';
  document.getElementById('d'+i).className=t>=a&&t<b?'on':''});
 for(let i=0;i<P;i++){const d=i==0?0:.15+.12*i,k=back((t-d)/.8),e=document.getElementById('p'+i);e.style.opacity=cl((t-d)/.3);e.style.transform='translateX(-50%) translateY('+(1-k)*120+'px) scale('+(1+.04*cl(t/16))+')'}
 document.getElementById('stage').style.transform='scale('+(1+.03*Math.sin(t*.35))+')';
 const sw=document.getElementById('sw'),st=((t-1.2)%4)/1.1;sw.style.left=(-25+st*150)+'%';sw.style.opacity=st>=0&&st<=1?1:0;
 const se=document.getElementById('seal'),sk=back((t-SEAL)/.5);se.style.opacity=cl((t-SEAL)/.2);se.style.transform='rotate('+(-8+(1-cl((t-SEAL)/.5))*-30)+'deg) scale('+(t<SEAL?0:sk+.04*Math.sin((t-SEAL)*4)*cl(t-SEAL-0.6))+')';
 document.getElementById('glow').style.transform='translate('+(Math.sin(t*.4)*80)+'px,'+(Math.cos(t*.3)*40)+'px)';
 const en=document.getElementById('end'),ek=ease((t-16)/.5);en.style.opacity=ek;en.style.transform='scale('+(1.04-.04*ek)+')';
};render(0);
</script></body></html>`;
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:W,height:H}});await p.setContent(html);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(400);
const dir=`fr_${n}_${r}`;fs.rmSync(dir,{recursive:true,force:true});fs.mkdirSync(dir);
const only=process.argv[4]?process.argv[4].split(',').map(Number):null;
for(let f=0;f<FPS*DUR;f++){const t=f/FPS;if(only&&!only.some(x=>Math.abs(x-t)<1e-6))continue;await p.evaluate(t=>render(t),t);await p.screenshot({path:`${dir}/${String(f).padStart(4,'0')}.jpg`,type:'jpeg',quality:92});}
await b.close();console.log('done',dir)})();
