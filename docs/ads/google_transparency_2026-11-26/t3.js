const {chromium}=require('playwright');const fs=require('fs');
const names=process.argv.slice(2);
(async()=>{const b=await chromium.launch();const p=await b.newPage({locale:'en-GB'});
await p.goto('https://adstransparency.google.com/?region=GB',{waitUntil:'networkidle',timeout:60000});
const rpc=async(svc,req)=>p.evaluate(async([svc,req])=>{const r=await fetch('/anji/_/rpc/'+svc+'?authuser=',{method:'POST',headers:{'content-type':'application/x-www-form-urlencoded'},body:'f.req='+encodeURIComponent(JSON.stringify(req))});return r.text()},[svc,req]);
const out={};
for(const n of names){
  const s=JSON.parse(await rpc('SearchService/SearchSuggestions',{"1":n,"2":10,"3":10,"4":[2826],"5":{"1":1}}));
  const advs=(s["1"]||[]).filter(x=>x["1"]).map(x=>({name:x["1"]["1"],id:x["1"]["2"],ctry:x["1"]["3"],n:x["1"]["4"]}));
  const sites=(s["1"]||[]).filter(x=>x["2"]).map(x=>x["2"]["1"]);
  out[n]={advs,sites};
  for(const a of advs.slice(0,3)){
    let all=[],tok=null;
    for(let i=0;i<5;i++){
      const req={"2":100,"3":{"8":[2826],"12":{"1":"","2":true},"13":{"1":[a.id]}},"7":{"1":1,"2":0,"3":-1}};
      if(tok)req["4"]=tok;
      const r=JSON.parse(await rpc('SearchService/SearchCreatives',req));
      all=all.concat(r["1"]||[]);tok=r["2"];if(!tok)break;}
    a.creatives=all.map(c=>({cr:c["2"],fmt:c["4"],first:+c["6"]["1"],last:+c["7"]["1"],days:c["13"],url:(c["3"]["1"]||{})["4"],img:(c["3"]["3"]||{})["2"]}));
  }
  console.error(n,advs.map(a=>a.name+':'+(a.creatives||[]).length).join(' | '));
}
fs.writeFileSync('out.json',JSON.stringify(out));await b.close();})();
