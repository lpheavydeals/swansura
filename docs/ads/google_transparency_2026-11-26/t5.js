const fs=require('fs');const {chromium}=require('playwright');
const d={...JSON.parse(fs.readFileSync('out1.json')),...JSON.parse(fs.readFileSync('out2.json'))};
const pick={"The Perfume Shop":0,"The Fragrance Shop":0,"Notino":1,"Perfume Click":0,"Jomashop":0,"FragranceNet":0,"Superdrug":0,"Vilvah":0,"Arabian Oud":0,"Boots UK":1};
(async()=>{const b=await chromium.launch();const p=await b.newPage({locale:'en-GB'});const out={};
for(const [n,i] of Object.entries(pick)){const a=d[n].advs[i];const now=Date.now()/1000;
 const cr=(a.creatives||[]).filter(c=>c.fmt==1&&now-c.last<7*86400).sort((x,y)=>y.first-x.first).slice(0,5);out[a.name]=[];
 for(const c of cr){try{await p.goto(`https://adstransparency.google.com/advertiser/${a.id}/creative/${c.cr}?region=GB`,{waitUntil:'networkidle',timeout:45000});await p.waitForTimeout(2500);
  let t=[];for(const f of p.frames()){try{const x=(await f.innerText('body')).trim();if(x&&f!==p.mainFrame())t.push(x)}catch(e){}}
  const main=(await p.innerText('body'));const m=main.match(/Last shown:?\s*([^\n]+)/);
  out[a.name].push({t:t.join(' / ').replace(/\s+/g,' ').slice(0,400),last:m&&m[1]});}catch(e){out[a.name].push({err:String(e).slice(0,80)})}}
 console.error(a.name,out[a.name].length);}
fs.writeFileSync('texts.json',JSON.stringify(out,null,1));await b.close();})();
