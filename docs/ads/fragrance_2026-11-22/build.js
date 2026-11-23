// Fragrance ad samples (22 Nov 2026). Run from this folder: node build.js video 916|45 [white]  |  node build.js gift 916|45 [white]
// video: renders 30 fps frames of an 18 s bottle video into frames_<fmt>/ (then build.sh encodes them).
// gift:  renders the 'Christmas gifts for him' image.
// Style: Plus Jakarta Sans only, emerald silk background, gold hairlines, text in top/bottom bands, bottle clear in the middle.
const {chromium}=require('playwright');const fs=require('fs');
const [MODE,FMT]=[process.argv[2]||'video',process.argv[3]||'916'];
const WHITE=process.argv[4]=='white',SUF=WHITE?'_white':'';  // 23 Nov 2026: white theme (user: 'white themed also fine')
const W=1080,H=FMT=='916'?1920:1350;
const b64=f=>`data:image/${f.endsWith('svg')?'svg+xml':'png'};base64,`+fs.readFileSync('src/'+f).toString('base64');
const BASE=`@font-face{font-family:PJS;src:url(${'data:font/woff2;base64,'+fs.readFileSync('src/pjs.woff2').toString('base64')});font-weight:200 800}
*{margin:0;box-sizing:border-box}html,body{width:${W}px;height:${H}px;overflow:hidden}
body{position:relative;font-family:PJS;color:#F4EEE4;background:radial-gradient(90% 60% at 50% 46%,#2A6B57 0%,#1B4D3E 42%,#133A2F 78%,#0D2820 100%)}
.silk{position:absolute;inset:0;background:linear-gradient(115deg,rgba(255,255,255,.07) 0%,rgba(255,255,255,0) 38%,rgba(255,255,255,.05) 62%,rgba(255,255,255,0) 80%)}
.hair{position:absolute;left:60px;right:60px;height:1.5px;background:linear-gradient(90deg,transparent,#B5843A 20%,#EACB8E 50%,#B5843A 80%,transparent)}
.eb{font-weight:700;font-size:24px;letter-spacing:.32em;color:#EACB8E;text-transform:uppercase;display:inline-flex;align-items:center;gap:18px}
.eb:before,.eb:after{content:'';width:46px;height:1.5px;background:#EACB8E}
.c{position:absolute;left:0;right:0;text-align:center;padding:0 70px}`;
const WCSS=WHITE?`body{color:#1F1A17;background:radial-gradient(90% 60% at 50% 46%,#FFFFFF 0%,#FBF8F3 55%,#F2ECE2 100%)}.silk{display:none}
.eb{color:#8C6226}.eb:before,.eb:after{background:#B5843A}
.h{color:#1B4D3E!important}.h span{color:#B5843A!important}.h2,.small,.sub{color:#403227!important}.note .k{color:#B5843A}.note .v{color:#1B4D3E}
.price{color:#1B4D3E}.trust{color:#1F1A17}.trust i{color:#B5843A}
.spot{background:radial-gradient(closest-side,rgba(181,132,58,.12),rgba(181,132,58,0))!important}
.ph img,.cell img{filter:drop-shadow(0 24px 26px rgba(64,50,39,.22))!important}
.end{background:radial-gradient(120% 70% at 30% 20%,#FFFFFF 0%,#FAF6EF 60%,#F1EADF 100%)!important}
.tile{background:#FFFFFF!important;border:2px solid rgba(181,132,58,.55)!important;box-shadow:0 24px 60px rgba(64,50,39,.16)!important}
.name{color:#1B4D3E!important}.eprice{color:#8C6226!important}.btn{background:#1B4D3E!important;color:#fff!important}.btn svg{stroke:#fff}
.fine{color:#403227!important}.fine span{color:#1B4D3E!important}.tc{color:#403227}
.cell{background:#FFFFFF!important;border:1.5px solid rgba(181,132,58,.45)!important;box-shadow:0 10px 30px rgba(64,50,39,.08)}.n{color:#1B4D3E!important}.p{color:#8C6226!important}
.cta{background:#1B4D3E!important}`:'';
const ARR='<svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#0F2E25" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>';

if(MODE=='video'){
 const T=FMT=='916'?{top:200,bot:1580,img:[480,1480],end:0}:{top:70,bot:1110,img:[300,1085],end:-285};
 const html=`<html><head><meta charset=utf-8><style>${BASE}
 .spot{position:absolute;left:50%;top:${(T.img[0]+T.img[1])/2}px;width:900px;height:900px;margin:-450px 0 0 -450px;border-radius:50%;background:radial-gradient(closest-side,rgba(234,203,142,.22),rgba(234,203,142,0))}
 .ph{position:absolute;left:0;right:0;top:${T.img[0]}px;height:${T.img[1]-T.img[0]}px;display:flex;align-items:center;justify-content:center}
 .ph img{max-width:900px;max-height:100%;object-fit:contain;filter:drop-shadow(0 30px 40px rgba(0,0,0,.45))}
 .sc{position:absolute;inset:0;opacity:0}
 .h{font-weight:800;font-size:${FMT=='916'?92:78}px;letter-spacing:-.02em;line-height:1.02;margin-top:18px;color:#fff}
 .h2{font-weight:300;font-size:${FMT=='916'?50:44}px;margin-top:10px;color:#F4EEE4}
 .note{opacity:0;position:absolute;left:0;right:0;top:0}.note .k{font-weight:700;font-size:24px;letter-spacing:.3em;color:#EACB8E}
 .note .v{font-weight:600;font-size:${FMT=='916'?46:40}px;color:#fff;margin-top:6px}
 .price{font-weight:800;font-size:${FMT=='916'?104:88}px;color:#EACB8E;letter-spacing:-.02em}
 .trust{font-weight:600;font-size:${FMT=='916'?36:32}px;color:#fff;margin-top:10px}.trust i{font-style:normal;color:#EACB8E;margin:0 12px}
 .small{font-weight:500;font-size:28px;color:#F4EEE4;opacity:.9;margin-top:12px}
 .end{position:absolute;inset:0;opacity:0;background:radial-gradient(120% 70% at 30% 20%,#2A6B57 0%,#1B4D3E 38%,#133A2F 75%,#0F2E25 100%)}
 .logo{position:absolute;left:0;right:0;text-align:center;top:${330+T.end}px}.logo img{height:150px}
 .tile{position:absolute;left:250px;top:${520+T.end}px;width:580px;height:580px;border-radius:40px;overflow:hidden;background:#EEF3F0;box-shadow:0 30px 80px rgba(0,0,0,.35);border:3px solid rgba(234,203,142,.6);display:flex;align-items:center;justify-content:center}
 .tile img{width:92%;height:92%;object-fit:contain}
 .name{position:absolute;left:60px;right:60px;top:${1132+T.end}px;text-align:center;color:#fff;font-weight:700;font-size:54px;line-height:1.05}
 .eprice{position:absolute;left:0;right:0;top:${1206+T.end}px;text-align:center;color:#EACB8E;font-size:36px;font-weight:700}
 .btn{position:absolute;left:290px;top:${1290+T.end}px;width:500px;height:108px;border-radius:999px;background:linear-gradient(180deg,#EACB8E,#C4924A);color:#0F2E25;font-size:42px;font-weight:800;display:flex;align-items:center;justify-content:center;gap:16px;box-shadow:0 16px 40px rgba(0,0,0,.3)}
 .fine{position:absolute;left:0;right:0;top:${1436+T.end}px;text-align:center;color:#F4EEE4;font-size:28px;font-weight:600;line-height:1.5}.fine span{color:#EACB8E}
 .tc{position:absolute;left:0;right:0;top:${1540+T.end}px;text-align:center;font-size:19px;font-weight:500;opacity:.6}
 ${WCSS}</style></head><body><div class=silk></div><div class=spot></div>
 <div class=sc id=s1><div class=ph><img id=i1 src="${b64('tf01.png')}"></div>
  <div class=c style="top:${T.top}px"><div class=eb>Tom Ford · Parfum</div><div class=h>Noir Extreme</div><div class=h2>Parfum · 100ml</div></div>
  <div class=c style="top:${T.bot}px"><div class=trust>Warm spice <i>·</i> amber <i>·</i> vanilla</div></div></div>
 <div class=sc id=s2><div class=ph><img id=i2 src="${b64('tf04.png')}"></div>
  <div class=c style="top:${T.top}px"><div class=eb>The notes</div><div class=h style="font-size:${FMT=='916'?74:64}px">Noir Extreme Parfum</div></div>
  <div class=c style="top:${T.bot-(FMT=='916'?30:20)}px">
   <div class=note id=n1><div class=k>TOP</div><div class=v>Cardamom · Saffron · Nutmeg</div></div>
   <div class=note id=n2><div class=k>HEART</div><div class=v>Rose · Jasmine · Kulfi</div></div>
   <div class=note id=n3><div class=k>BASE</div><div class=v>Vanilla · Amber · Sandalwood</div></div></div></div>
 <div class=sc id=s3><div class=ph><img id=i3 src="${b64('tf02.png')}"></div>
  <div class=c style="top:${T.top}px"><div class=eb>At Swansura</div><div class=price style="margin-top:14px">£132.99</div><div class=h2>Tom Ford Noir Extreme Parfum 100ml</div></div>
  <div class=c style="top:${T.bot}px"><div class=trust>100% authentic <i>·</i> Ships from the UK</div><div class=small>Free UK delivery over £40</div></div></div>
 <div class=end id=e><div class=logo><img src="${b64(WHITE?'logo_b.svg':'logo_w.svg')}"></div><div class=tile><img src="${b64('tf01.png')}"></div>
  <div class=name>Tom Ford Noir Extreme Parfum</div><div class=eprice>100ml · £132.99</div><div class=btn>Shop now ${ARR}</div>
  <div class=fine>100% authentic · Free UK delivery over £40<br><span>swansura.com</span></div><div class=tc>T&amp;Cs apply</div></div>
 <div class="hair" style="top:${FMT=='916'?150:40}px"></div><div class="hair" style="top:${H-(FMT=='916'?150:40)}px"></div>
 <script>
 const cl=(x)=>Math.max(0,Math.min(1,x)),ease=x=>1-Math.pow(1-cl(x),3);
 const fade=(t,a,b,d=.45)=>Math.min(ease((t-a)/d),1-ease((t-(b-d))/d));
 window.R=t=>{const S=[['s1',0,4.2],['s2',4,10.2],['s3',10,14.2]];
  for(const[id,a,b] of S){const o=fade(t,a,b);document.getElementById(id).style.opacity=o;}
  const z=(id,a,b,s0,s1,dy)=>{const p=cl((t-a)/(b-a));document.getElementById(id).style.transform='translateY('+(dy*(1-ease(p*1.4)))+'px) scale('+(s0+(s1-s0)*p)+')'};
  z('i1',0,4.2,.9,1.02,60);z('i2',4,10.2,1,1.06,0);z('i3',10,14.2,1.04,.98,0);
  [['n1',4.5,6.6],['n2',6.6,8.4],['n3',8.4,10.4]].forEach(([id,a,b])=>{const e=document.getElementById(id);const o=fade(t,a,b,.35);e.style.opacity=o;e.style.transform='translateY('+(20*(1-ease((t-a)/.35)))+'px)'});
  const e=document.getElementById('e');const o=ease((t-14)/.5);e.style.opacity=o;}
 </script></body></html>`;
 (async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:W,height:H}});await p.setContent(html);await p.evaluate(()=>document.fonts.ready);
  const dir='frames_'+FMT+SUF;fs.rmSync(dir,{recursive:true,force:true});fs.mkdirSync(dir);const N=18*30;
  for(let i=0;i<N;i++){await p.evaluate(t=>R(t),i/30);await p.screenshot({path:`${dir}/f${String(i).padStart(4,'0')}.jpg`,type:'jpeg',quality:94});}
  await b.close();console.log('frames',N,dir)})();
}

if(MODE=='gift'){
 const tl=FMT=='916',G=[['tf01.png','Tom Ford Noir Extreme','Parfum 100ml · £132.99'],['versace-eros-parfum-02.png','Versace Eros','Parfum 200ml · £85.74'],
  ['gucci-intense-oud-eau-de-parfum-90ml-luxury-unisex-oud-fragrance-01-cutout.png','Gucci Intense Oud','EDP 90ml · £88.99'],['paco-rabanne-invictus-eau-de-toilette-200ml-01.png','Paco Rabanne Invictus','EDT 200ml · £81.99']];
 const top=tl?250:70,gy=tl?560:320,gh=tl?800:700;
 const html=`<html><head><meta charset=utf-8><style>${BASE}
 .h{font-weight:800;font-size:${tl?86:72}px;letter-spacing:-.02em;line-height:1.04;color:#fff;margin-top:18px}.h span{color:#EACB8E}
 .sub{font-weight:500;font-size:${tl?34:30}px;margin-top:14px}
 .grid{position:absolute;left:40px;right:40px;top:${gy}px;height:${gh}px;display:grid;grid-template-columns:repeat(2,1fr);gap:22px}
 .cell{position:relative;border-radius:28px;background:radial-gradient(80% 70% at 50% 40%,rgba(234,203,142,.16),rgba(255,255,255,.03));border:1.5px solid rgba(234,203,142,.35);display:flex;flex-direction:column;align-items:center;justify-content:flex-end;padding-bottom:${tl?20:14}px}
 .cell img{position:absolute;left:8%;right:8%;top:6%;width:84%;height:${tl?'68%':'64%'};object-fit:contain;filter:drop-shadow(0 18px 22px rgba(0,0,0,.4))}
 .n{font-weight:700;font-size:${tl?32:27}px;color:#fff;text-align:center}.p{font-weight:600;font-size:${tl?25:22}px;color:#EACB8E;margin-top:4px}
 .trust{font-weight:600;font-size:${tl?32:28}px}.trust i{font-style:normal;color:#EACB8E;margin:0 12px}
 .cta{position:absolute;left:0;right:0;bottom:${tl?250:0}px;height:${tl?92:84}px;background:#0F2E25;color:#F4EEE4;display:flex;align-items:center;justify-content:center;gap:14px;font-size:${tl?30:28}px;font-weight:600}
 .cta b{color:#EACB8E;font-weight:800}.cta svg{stroke:#EACB8E}
 ${WCSS}</style></head><body><div class=silk></div>
 <div class=c style="top:${top}px"><div class=eb>Christmas gifts for him</div><div class=h>Designer fragrance,<br><span>shipped from the UK</span></div></div>
 <div class=grid>${G.map(g=>`<div class=cell><img src="${b64(g[0])}"><div class=n>${g[1]}</div><div class=p>${g[2]}</div></div>`).join('')}</div>
 <div class=c style="top:${gy+gh+(tl?40:26)}px"><div class=trust>100% authentic <i>·</i> Free UK delivery over £40</div></div>
 <div class=cta>Shop gifts for him at <b>swansura.com</b> ${ARR.replace('#0F2E25','#EACB8E')}</div>
 </body></html>`;
 (async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:W,height:H}});await p.setContent(html);await p.evaluate(()=>document.fonts.ready);
  await p.screenshot({path:`Gifts_For_Him_${FMT=='916'?'9x16':'4x5'}${SUF}.jpg`,type:'jpeg',quality:93});await b.close();console.log('gift',FMT)})();
}
