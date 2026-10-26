const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1400,height:900}});
await p.goto('http://localhost:8765/#home');await p.waitForTimeout(2500);
const r=await p.evaluate(()=>{
 const items=[...document.querySelectorAll('header .item')].map(it=>{const a=it.querySelector(':scope>a');
  const cols=[...it.querySelectorAll('.mega>div')].map(c=>({h:c.querySelector('h4')?.textContent.trim(),links:[...c.querySelectorAll('a')].map(x=>[x.textContent.trim(),x.getAttribute('href')])}));
  return {t:a.textContent.trim(),h:a.getAttribute('href'),cols}});
 const foot=[...document.querySelectorAll('footer h4, footer summary')].map(h=>{const box=h.closest('div,details');return {h:h.textContent.trim(),links:[...box.querySelectorAll('a')].map(x=>[x.textContent.trim(),x.getAttribute('href')])}});
 const legal=[...document.querySelectorAll('footer .legal a, footer .bar a')].map(x=>[x.textContent.trim(),x.getAttribute('href')]);
 return {items,foot,legal};});
console.log(JSON.stringify(r));await b.close();})();
