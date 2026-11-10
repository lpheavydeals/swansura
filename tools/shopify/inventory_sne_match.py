import json,glob,re,collections,unicodedata
S='/tmp/claude-0/-home-user-swansura/cb6ce7c1-c8b8-59d8-a1e3-4a95f6d9a400/scratchpad/'
rows=json.load(open(S+'stk/sne_rows.json'))
bc={}
for f in ['b1.json','b2.json']:
  for n in json.load(open(S+'stk/'+f))['data']['v']['nodes']:
    for b in n['barcodes']['nodes']: bc.setdefault(b['value'].lstrip('0'),[]).append(n['id'])
V=[]
for f in sorted(glob.glob(S+'inv/p*.json')):
  for p in json.load(open(f))['data']['products']['nodes']:
    for v in p['variants']['nodes']: V.append(dict(pid=p['id'],title=p['title'],vendor=p['vendor'],handle=p['handle'],vid=v['id'],vt=v['title'],qty=v['inventoryQuantity'],price=v['price'],inv=v['inventoryItem']['id']))
SKIP={'Vilvah','Deyga','Highborn London','anatomē'}
V=[v for v in V if v['vendor'] not in SKIP]
byvid={v['vid']:v for v in V}
def norm(s):
  s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()
  s=s.replace('&',' and ').replace("'",'').replace('’','')
  s=re.sub(r'eau de parfum|\bedp\b',' edp ',s); s=re.sub(r'eau de toilette|\bedt\b',' edt ',s); s=re.sub(r'eau de cologne|\bedc\b',' edc ',s)
  s=re.sub(r'extrait de parfum|extrait',' extrait ',s)
  s=re.sub(r'(\d+(?:\.\d+)?)\s*ml',r' \1ml ',s)
  return re.sub(r'[^a-z0-9.]+',' ',s).split()
def sizes(t): return set(x for x in t if re.fullmatch(r'\d+(\.\d+)?ml',x))
def conc(t):
  c={x for x in t if x in('edp','edt','edc','extrait')}
  if 'parfum' in t and not c: c={'parfum'}
  return c
def kind(t):
  k=set()
  if 'tester' in t: k.add('tester')
  if {'set','gift','giftset','coffret','x'}&set(t) : k.add('set')
  if {'deodorant','deo','stick'}&set(t): k.add('deo')
  if {'mist','body','lotion','shower','gel'}&set(t) and not {'edp','edt'}&set(t): k.add('body')
  return k
STOP=set('the for and pour of de la le eau spray perfume fragrance unisex women men woman man ml w m u him her luxury long lasting natural new packing pack purse travel vaporisateur natural intense_x edition limited special by in with a an tester gift set giftset coffret mini miniature version x oz fl'.split())|{'n'}
def gen(raw,t):
  raw=raw.lower(); g=set()
  if re.search(r'\(w\)|\bwomen|\bwoman|\bfor her\b|\bfemme\b|\bfeminin|\blady\b|\(f\)',raw): g.add('w')
  if re.search(r'\(m\)|\bmen\b|\bman\b|\bfor him\b|\bhomme\b|\bmasculin|\bmen\x27s|\bmen’s',raw): g.add('m')
  return g
def core(t): return set(x for x in t if x not in STOP and not re.fullmatch(r'\d+(\.\d+)?ml',x) and x not in('edp','edt','edc','extrait','parfum','tester','set','gift'))
for v in V:
  t=norm(v['title']+' '+('' if v['vt']=='Default Title' else v['vt']))
  v['t']=t; v['sz']=sizes(norm(v['vt'])) or sizes(norm(v['title'])); v['c']=conc(t); v['k']=kind(t); v['core']=core(t); v['b']=core(norm(v['vendor'])); v['g']=gen(v['title']+' '+v['vt'],t)
res=[]
for r in rows:
  t=norm(r['desc']+' '+(r['brand'] or '')); out=dict(r)
  ean=str(r['ean'] or '').split('.')[0].lstrip('0')
  isT = r['sheet']=='TESTERS' or 'tester' in t
  if ean in bc and not isT:
    vids=[x for x in bc[ean] if x in byvid]
    if len(vids)==1: out.update(m=vids[0],how='EAN',score=1.0); res.append(out); continue
  sz=sizes(t); c=conc(t); k=kind(t); cr=core(t); g=gen(r['desc'],t)
  if r['sheet']=='TESTERS': k.add('tester')
  best=[]
  for v in V:
    if v['b'] and not (v['b']&cr): continue
    if sz and v['sz'] and not (sz&v['sz']): continue
    if ('tester' in k)!=('tester' in v['k']): continue
    if ('set' in k)!=('set' in v['k']): continue
    if ('deo' in k)!=('deo' in v['k']): continue
    if len(g)==1 and len(v['g'])==1 and g!=v['g']: continue
    if c and v['c'] and not (c&v['c']): continue
    a=cr-v['b']; b=v['core']-v['b']
    if not a or a!=b: continue
    if not (sz and v['sz']) and not (sz==v['sz']): continue
    s=1.0
    best.append((s,v['vid']))
  best.sort(reverse=True)
  if len(best)==1:
    out.update(m=best[0][1],how='name',score=round(best[0][0],2))
  elif len(best)>1:
    out.update(m=None,how='unsure',score=round(best[0][0],2),cands=[b[1] for b in best[:3]])
  else: out.update(m=None,how='none',score=best[0][0] if best else 0)
  res.append(out)
json.dump(dict(res=res,V={v['vid']:{k:v[k] for k in('title','vt','vendor','qty','inv','handle','price')} for v in V}),open(S+'stk/match.json','w'),default=str)
C=collections.Counter(r['how'] for r in res); print(C)
mv=collections.Counter(r['m'] for r in res if r.get('m')); print('store variants matched',len(mv),'multi-hit',sum(1 for x in mv.values() if x>1),'of store',len(V))
print('qty>0 unmatched',sum(1 for r in res if not r.get('m') and (r['qty'] or 0)>0))
