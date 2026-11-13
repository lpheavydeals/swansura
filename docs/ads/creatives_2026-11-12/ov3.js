const {chromium}=require('playwright');const fs=require('fs');
const MODE=process.argv[2]||'916';
// band positions (px in the 1080x1920 frame)
const P=MODE=='916'?{top:120,bot:1800,ts:0,tsh:430,bsh:520}:{top:315,bot:1600,ts:285,tsh:620,bsh:620};
const CSS=`@font-face{font-family:PJS;src:url(pjs.woff2) format('woff2');font-weight:200 800}
@font-face{font-family:Fr;src:url(fraunces-italic.ttf);font-style:italic;font-weight:100 900}
@font-face{font-family:FrR;src:url(fraunces.ttf);font-weight:100 900}
@font-face{font-family:GV;src:url(greatvibes.ttf)}
@font-face{font-family:SAT;src:url(Satisfy-Regular.ttf)}
@font-face{font-family:DAN;src:url(dancing.ttf);font-weight:400 700}
@font-face{font-family:KAU;src:url(kaushan.ttf)}@font-face{font-family:PAR;src:url(parisienne.woff2)}@font-face{font-family:YT;src:url(Yellowtail-Regular.ttf)}@font-face{font-family:PAC;src:url(pacifico.woff2)}@font-face{font-family:COU;src:url(courgette.woff2)}
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
.ing{font-family:PJS;font-weight:600;font-size:36px;letter-spacing:.06em;color:#fff;text-shadow:0 2px 14px rgba(0,0,0,.55)}.ing b{color:#EACB8E;margin:0 14px}
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
const line=(arr)=>bot(`<div class="ing">${arr.join('<b>·</b>')}</div>`);
const capb=(t,s)=>bot(`<div class="l cap2" style="font-size:56px">${t}</div>${s?`<div class="small">${s}</div>`:''}`);
const arrow='<svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#0F2E25" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>';
const end=(im,name,price)=>{const o=MODE=='916'?0:-20;return `<div class="card"></div><div class="logo" style="top:${330+o}px"><img src="${logoUri}"></div><div class="tile" style="top:${520+o}px"><img src="${img(im)}"></div><div class="name" style="top:${1132+o}px">${name}</div><div class="price" style="top:${1222+o}px">${price}</div><div class="btn" style="top:${1300+o}px">Shop now ${arrow}</div><div class="fine" style="top:${1446+o}px">Free UK delivery over £40<br><span>swansura.com</span></div><div class="fine" style="top:${(MODE=='916'?1545:1560)}px;font-size:19px;font-weight:500;opacity:.6">T&amp;Cs apply</div>`};
const TH={f:{},n:{},a:{f:'PAR',w:400,h:100,c:80,n:76},b:{f:'YT',w:400,h:86,c:68,n:66},c:{f:'PAC',w:400,h:74,c:58,n:58},k:{f:'COU',w:400,h:72,c:58,n:58},s:{},m:{},y:{},l:{}};
const thcss=k=>{if(!TH[k[0]])return '';return `.h,.cap2,.l,.name{font-family:PJS!important;font-style:normal!important;font-variation-settings:normal!important;font-weight:500!important;letter-spacing:-.01em!important}.h{font-size:68px!important;line-height:1.12}.cap2{font-size:54px!important;line-height:1.15}.name{font-size:56px!important;font-weight:700!important}.s{font-family:PJS!important;font-size:1em!important;font-weight:800!important;color:inherit!important;line-height:1.12}`};
const thx=k=>(k=='a1'?`.ts{display:none}.h{color:#163F33!important;text-shadow:0 1px 18px rgba(255,255,255,.6)!important}.eb{color:#163F33!important;text-shadow:none!important}`:'')+(k[0]=='a'&&k!='a1'?`.bs{height:620px!important;background:linear-gradient(transparent,rgba(10,20,30,.25) 35%,rgba(10,20,30,.7))!important}`:'')+(k[0]=='a'?``:'');
const lab=(l,t)=>top(`<div class="eb">${l}</div><div class="h" style="margin-top:14px">${t}</div>`);
const end2=(im,name,price,fine)=>end(im,name,price).replace('Free UK delivery over £40',fine);
const P1='Official UK partner of Vilvah',P2='Official UK partner of Deyga',SH='Dispatched from the UK · Free delivery over £40';
const O={
 a1:hook('VILVAH · AM TO PM SERUM KIT','Two serums,<br><span class="s">one routine</span>'),
 a2:lab('MORNING','Milk Drops'), a2b:line(['rice milk extract','hyaluronic acid','aloe']),
 a3:lab('NIGHT','Better Ageing Serum'), a3b:line(['bakuchiol','blue pea flower','peptides']),
 a4:capb('light layers, <span class="s">morning &amp; night</span>'),
 a5:bot(`<div class="ing">${P1}</div><div class="small">Dispatched from the UK · Free UK delivery on this kit</div>`),
 aend:end2('aend.jpg','Vilvah AM PM Serum Kit','Milk Drops + Better Ageing Serum · £47.99','Free UK delivery on this kit'),
 b1:hook('VILVAH · SHIPPED FROM THE UK','Your <span class="s">wash-day</span> duo'),
 b2:lab('STEP 1','Goat Milk Shampoo'), b2b:line(['goat milk','jasmine flower water','pea protein']),
 b3:capb('a <span class="s">creamy, gentle</span> wash'),
 b4:lab('STEP 2','Cream Conditioner'), b4b:line(['tucuma butter','broccoli seed oil','aloe']),
 bend:end2('bend.jpg','Vilvah Bestseller Hair Kit','Shampoo + Conditioner · £27.99','Add one more item for free UK delivery'),
 c1:hook('DEYGA · SHIPPED FROM THE UK','Your everyday <span class="s">ABC</span>'),
 c2:lab('A','Aloe Vera Gel'), c2b:line(['aloe vera','glycerin']),
 c3:lab('B','Beetroot Lip Balm'), c3b:line(['beetroot','almond oil','shea butter']),
 c4:lab('C','Charcoal Bath Bar'), c4b:line(['activated charcoal','coconut oil','tea tree']),
 c5:capb('face, lips &amp; body, <span class="s">one kit</span>',P2+' · Dispatched from the UK'),
 cend:end2('cend.jpg','Deyga ABC Kit','Aloe · Beetroot · Charcoal · £22.99','Free UK delivery over £40'),
 k1:hook('DEYGA · SHIPPED FROM THE UK','Wash, then <span class="s">hydrate</span>'),
 k2:lab('STEP 1','Charcoal Bath Bar'), k2b:line(['activated charcoal','coconut oil','tea tree oil']),
 k3:lab('STEP 2','Aloe Vera Gel'), k3b:line(['aloe vera','glycerin']),
 k4:capb('two steps, <span class="s">morning &amp; night</span>',P2+' · Dispatched from the UK'),
 kend:end2('kend.jpg','Deyga Clear Skin Kit','Bath bar + aloe gel · £14.99','Free UK delivery over £40'),
f1:hook('VILVAH · SHIPPED FROM THE UK','Your <span class="s">milk</span> routine,<br>in two steps'),
 f2:lab('STEP 1','Milk Powder Face Wash'), f2b:line(['rice milk','papain','hyaluronic acid']),
 f3:capb('<span class="s">powder to foam</span>, just add water'),
 f4:lab('STEP 2','Milk Drops Serum 40 ml'), f4b:line(['rice milk extract','aloe vera','hyaluronic acid']),
 f5:capb('morning <span class="s">&amp;</span> evening',P1+' · Free UK delivery on this kit'),
 fend:end2('fend.jpg','Vilvah Face Brightening Kit (Large)','Face wash + Milk Drops 40 ml · £42.99','Free UK delivery on this kit'),
 n1:hook('DEYGA · SHIPPED FROM THE UK','Scrub, then <span class="s">balm</span>'),
 n2:lab('STEP 1','Strawberry Lip Scrub'), n2b:line(['sugar','avocado oil','shea butter']),
 n3:capb('gently, <span class="s">once or twice</span> a week'),
 n4:lab('STEP 2','Beetroot Lip Balm'), n4b:line(['beetroot','almond oil','jojoba oil']),
 n5:capb('a <span class="s">sheer, rosy</span> tint'),
 n6:capb('your <span class="s">two-step</span> lip routine',P2+' · Dispatched from the UK'),
 nend:end2('nend.jpg','Deyga Nourished Lip Care Kit','Lip scrub + beetroot balm · £25.99','Free UK delivery over £40'),
 s1:hook('DEYGA · SHIPPED FROM THE UK','Beetroot balm,<br><span class="s">in a stick</span>'),
 s2:lab('TWIST UP','Beetroot Lip Balm Stick'), s2b:line(['beetroot extract','shea butter','jojoba oil']),
 s3:capb('a <span class="s">sheer, rosy</span> tint'),
 s4:capb('slips into <span class="s">any pocket</span>',P2+' · Dispatched from the UK'),
 send:end2('send.jpg','Deyga Beetroot Lip Balm Stick','5.5 g · £13.99','Free UK delivery over £40'),
 m1:hook('VILVAH · SHIPPED FROM THE UK','Mask, then <span class="s">serum</span>'),
 m2:lab('STEP 1 · ONCE OR TWICE A WEEK','Milk Mud Mask'), m2b:line(['kaolin clay','oat milk extract','saffron extract']),
 m3:lab('STEP 2 · MORNING &amp; EVENING','Milk Drops Serum'), m3b:line(['aloe vera juice','hyaluronic acid','rice milk extract']),
 m4:capb('a <span class="s">light, water-based</span> gel'),
 m5:capb('your <span class="s">two-step</span> milk routine',P1+' · Free UK delivery on this kit'),
 mend:end2('mend.jpg','Vilvah Milk Face Kit','Milk Mud Mask + Milk Drops · £44.99','Free UK delivery on this kit'),
 y1:hook('VILVAH · SHIPPED FROM THE UK','Shower, then <span class="s">moisturise</span>'),
 y2:lab('STEP 1','Goat Milk Body Wash'), y2b:line(['goat milk','coconut oil','vanilla scent']),
 y3:lab('STEP 2','Milk Body Lotion'), y3b:line(['oat milk','ceramide NP','olive squalane']),
 y3c:capb('<span class="s">creamy</span> oat milk lotion'),
 y3d:capb('for arms, legs <span class="s">&amp; body</span>'),
 y4:capb('made for <span class="s">dry skin</span>'),
 y5:capb('shower to moisturiser, <span class="s">every day</span>',P1+' · Free UK delivery on this kit'),
 yend:end2('yend.jpg','Vilvah Milk Body Kit','Body wash + lotion · £41.99','Free UK delivery on this kit'),
 l1:hook('VILVAH · SHIPPED FROM THE UK','Two jars,<br><span class="s">one routine</span>'),
 l2:lab('STEP 1','Under Eye Cream'), l2b:line(['shea butter','bakuchiol','bamboo extract']),
 l3:capb('<span class="s">dot, then pat</span> gently'),
 l4:lab('STEP 2','Ultra Moisturising Cream'), l4b:line(['olive squalane','white lily oil','shea butter']),
 l5:capb('<span class="s">eyes first</span>, then face',P1+' · Free UK delivery over £40'),
 lend:end2('lend.jpg','Vilvah Face Lift Kit','Under eye cream + moisturiser · £35.99','Free UK delivery over £40'),
};
const ONLY=process.argv[3]?process.argv[3].split(','):null;
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});const dir='ov'+MODE;fs.mkdirSync(dir,{recursive:true});
for(const [k,v] of Object.entries(O)){if(ONLY&&!ONLY.includes(k[0]))continue;fs.writeFileSync('t.html',`<html><head><meta charset="utf-8"><style>${CSS}${thcss(k)}${thx(k)}</style></head><body>${v}</body></html>`);
await p.goto('file://'+process.cwd()+'/t.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(200);
await p.screenshot({path:dir+'/'+k+'.png',omitBackground:!k.endsWith('end')});}
await b.close()})();
