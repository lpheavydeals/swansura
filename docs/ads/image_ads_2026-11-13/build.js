const {chromium}=require('playwright');const fs=require('fs');
const b64=f=>`data:image/${f.endsWith('png')?'png':'jpeg'};base64,`+fs.readFileSync(f).toString('base64');
const K=JSON.parse(fs.readFileSync('kits.json'));
const ARR='<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>';
const base=(W,H)=>`@font-face{font-family:PJS;src:url(pjs.woff2);font-weight:200 800}*{margin:0;box-sizing:border-box}body{width:${W}px;height:${H}px;overflow:hidden;position:relative;font-family:PJS;color:#1F1A17}`;
// Style A: product on stone plinth, scene backdrop
function A(k,W,H){const sq=H==W;const ph=sq?540:760,pTop=sq?300:330;const pb=pTop+ph-(sq?20:30);
return `<html><head><meta charset=utf-8><style>${base(W,H)}
body{background:radial-gradient(120% 80% at 50% 38%,${k.bgA1} 0%,${k.bgA2} 70%,${k.bgA3} 100%)}
.tex{position:absolute;inset:0;background:url(${b64(k.prop)}) center/cover;filter:blur(38px) saturate(.9);opacity:.18;transform:scale(1.2)}
.shaft{position:absolute;inset:0;background:linear-gradient(115deg,rgba(255,255,255,.45) 0%,rgba(255,255,255,0) 45%)}
.top{position:absolute;left:0;right:0;top:${sq?48:64}px;text-align:center}
.eb{font-weight:700;font-size:${sq?18:20}px;letter-spacing:.3em;text-transform:uppercase;color:#695541}
.eb span{display:inline-block;width:46px;height:2px;background:#B5843A;vertical-align:middle;margin:0 14px 5px}
.h1{font-weight:300;font-size:${sq?50:60}px;letter-spacing:-.01em;margin-top:${sq?18:26}px;line-height:1.05}
.h2{font-weight:800;font-size:${sq?64:78}px;letter-spacing:-.02em;color:${k.acc};line-height:1.05}
.plinth{position:absolute;left:50%;transform:translateX(-50%);top:${pb-(sq?16:20)}px;width:${sq?700:820}px;height:${sq?120:150}px}
.slab{position:absolute;border-radius:22px;box-shadow:inset 0 3px 0 rgba(255,255,255,.55),inset 0 -6px 14px rgba(90,60,30,.12)}
.slab{background-blend-mode:multiply}.s1{left:0;right:0;bottom:0;height:55%;background:url(${b64('noise.jpg')}) center/cover,linear-gradient(180deg,${k.stone1},${k.stone2});box-shadow:0 30px 50px -20px rgba(60,40,20,.35)}
.s2{left:10%;right:10%;top:0;height:52%;background:url(${b64('noise.jpg')}) center/cover,linear-gradient(180deg,${k.stone0},${k.stone1})}
.prod{position:absolute;left:50%;transform:translateX(-50%);bottom:${H-pb}px;max-height:${ph-(sq?20:30)}px;max-width:${sq?680:820}px;z-index:2;object-fit:contain;filter:drop-shadow(0 22px 22px rgba(40,25,10,.28))}
.chip{z-index:3;position:absolute;right:${sq?54:60}px;top:${pTop+(sq?10:40)}px;width:${sq?150:176}px;height:${sq?150:176}px;border-radius:50%;background:${k.acc};color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;box-shadow:0 12px 30px rgba(0,0,0,.18);transform:rotate(-8deg)}
.chip b{font-size:${sq?36:42}px;font-weight:800;line-height:1}.chip small{font-size:${sq?14:16}px;font-weight:600;letter-spacing:.06em;margin-top:6px;text-transform:uppercase}
.trust{position:absolute;left:0;right:0;bottom:${sq?82:96}px;text-align:center;font-weight:600;font-size:${sq?19:22}px;color:#4B3E33;letter-spacing:.02em}
.trust i{font-style:normal;color:#B5843A;margin:0 10px}
.url{position:absolute;left:0;right:0;bottom:0;height:${sq?64:74}px;background:#133A2F;color:#F4EEE4;display:flex;align-items:center;justify-content:center;gap:16px;font-size:${sq?22:25}px;font-weight:600;letter-spacing:.04em}
.url b{color:#EACB8E;font-weight:800}
</style></head><body><svg width=0 height=0><filter id=stone><feTurbulence type=fractalNoise baseFrequency=.9 numOctaves=3 result=n/><feColorMatrix in=n type=saturate values=0 result=g/><feComponentTransfer in=g result=g2><feFuncA type=linear slope=.18/></feComponentTransfer><feComposite in=g2 in2=SourceGraphic operator=in result=t/><feBlend in=SourceGraphic in2=t mode=multiply/></filter></svg>
<div class=tex></div><div class=shaft></div>
<div class=top><div class=eb><span></span>${k.brand} · Official UK partner<span></span></div><div class=h1>${k.a1}</div><div class=h2>${k.a2}</div></div>
<div class=plinth><div class="slab s1"></div><div class="slab s2"></div></div>
<img class=prod src="${b64(k.cut)}">
<div class=chip><b>${k.chip}</b><small>${k.chipS}</small></div>
<div class=trust>${k.trust.join('<i>·</i>')}</div>
<div class=url>${k.name} <b>Shop now at swansura.com</b> ${ARR}</div>
</body></html>`}
// Style B: photo top + hook, white panel bullets, packshot
function B(k,W,H){const sq=H==W;const th=sq?470:620,bar=sq?84:96;
return `<html><head><meta charset=utf-8><style>${base(W,H)}
body{background:#fff}
.ph{position:absolute;left:0;top:0;width:${W}px;height:${th}px;object-fit:cover;object-position:${k.pos||'center'}}
.shade{position:absolute;left:0;top:0;width:${W}px;height:${th}px;background:linear-gradient(90deg,rgba(0,0,0,.55),rgba(0,0,0,.15) 45%,rgba(0,0,0,0) 65%)}
.hook{position:absolute;left:${sq?54:64}px;top:${th*(k.hy||.42)}px;transform:translateY(-50%);color:#fff;font-weight:800;font-size:${sq?62:74}px;line-height:1.02;letter-spacing:-.02em;text-shadow:0 2px 18px rgba(0,0,0,.25)}
.hook em{font-style:normal;font-weight:300;display:block;font-size:.62em;margin:2px 0 4px}.hook em.ne{font-weight:800;font-size:1em;line-height:.9}
.logo{position:absolute;right:${sq?40:48}px;top:${sq?34:42}px;color:#fff;font-weight:700;font-size:${sq?16:18}px;letter-spacing:.28em;text-transform:uppercase;text-shadow:0 1px 10px rgba(0,0,0,.6),0 0 2px rgba(0,0,0,.4)}
.pan{position:absolute;left:${sq?54:64}px;top:${th+(sq?40:56)}px;width:${sq?500:530}px}
.nm{font-size:${sq?40:48}px;line-height:1.08;font-weight:500;letter-spacing:-.01em}.nm b{color:${k.acc};font-weight:800}
.sub{font-size:${sq?20:23}px;color:#695541;font-weight:600;margin-top:8px}
ul{list-style:none;margin-top:${sq?22:34}px;border-left:2px solid #1F1A17;padding-left:0}
li{position:relative;padding:0 0 ${sq?14:22}px 26px;font-size:${sq?22:26}px;font-weight:400;line-height:1.25}
li:before{content:'';position:absolute;left:-6px;top:${sq?9:11}px;width:10px;height:10px;border-radius:50%;background:${k.acc}}
li b{font-weight:800}
.pack{position:absolute;right:${sq?30:36}px;bottom:${bar+(sq?20:30)}px;max-height:${(sq?H-th-bar+120:H-th-bar+170)}px;max-width:${(k.pw||470)*(sq?.9:1)}px;filter:drop-shadow(0 26px 26px rgba(40,25,10,.25))}
.bar{position:absolute;left:0;right:0;bottom:0;height:${bar}px;background:${k.bar||'#133A2F'};color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 ${sq?46:56}px;font-weight:700;font-size:${sq?26:30}px}
.bar span{font-weight:500;font-size:.72em;opacity:.9;margin-left:14px}
</style></head><body>
<img class=ph src="${b64(k.top)}"><div class=shade></div>
<div class=logo>${k.brand} × Swansura</div>
<div class=hook>${k.hook}</div>
<div class=pan><div class=nm>${k.nm}</div><div class=sub>${k.sub}</div><ul>${k.b.map(x=>'<li>'+x+'</li>').join('')}</ul></div>
<img class=pack src="${b64(k.cut)}">
<div class=bar><div>${k.price}<span>${k.priceS}</span></div><div style="display:flex;align-items:center;gap:10px">Shop now ${ARR}</div></div>
</body></html>`}
(async()=>{const br=await chromium.launch();const only=process.argv[2];
for(const [id,k] of Object.entries(K)){if(only&&!only.split(',').includes(id))continue;
 for(const [st,fn] of [['A',A],['B',B]])for(const [zn,W,H] of [['4x5',1080,1350],['1x1',1080,1080]]){
  const p=await br.newPage({viewport:{width:W,height:H}});fs.writeFileSync('t.html',fn(k,W,H));await p.goto('file://'+process.cwd()+'/t.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(200);
  await p.screenshot({path:`out/${id}_${st}_${zn}.jpg`,type:'jpeg',quality:92});await p.close();}}
await br.close()})();
