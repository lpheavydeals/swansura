// Dump the prototype's rendered parts (announce, header, each main section, footer) to HTML files.
// Serve prototype/ on :8765 first. node tools/proto/dump_sections.js ROUTE OUTDIR [WIDTH]
const {chromium}=require('playwright');const fs=require('fs');
const [route,dir,w]=process.argv.slice(2);
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:+(w||1366),height:900}});
await p.goto('http://localhost:8765/#'+route,{waitUntil:'networkidle'});await p.waitForTimeout(1500);
const parts=await p.evaluate(()=>{const L=[];const add=(n,el)=>el&&L.push([n,el.outerHTML]);
add('announce',document.querySelector('aside.announce'));add('header',document.querySelector('header.site'));
document.querySelectorAll('main#app > *').forEach((s,i)=>{const h=s.querySelector('h1,h2');add(String(i).padStart(2,'0')+'_'+(s.className||s.tagName).toString().replace(/\s+/g,'.')+'_'+(h?h.textContent.trim().slice(0,30).replace(/[^a-z0-9]+/gi,'-'):''),s)});
add('faqslot',document.querySelector('#faqslot'));add('footer',document.querySelector('footer.site'));add('chat',document.querySelector('#chatBtn'));return L});
fs.mkdirSync(dir,{recursive:true});for(const [n,h] of parts){fs.writeFileSync(dir+'/'+n+'.html',h)}console.log(parts.map(([n,h])=>n+' '+h.length).join('\n'));await b.close();})();
