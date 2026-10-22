import json, re, collections
import sys
S=sys.argv[1] if len(sys.argv)>1 else 'inci.json'
doc={i['name']:i for i in json.load(open(S))}
def D(prefix):
    m=[k for k in doc if k.lower().startswith(prefix.lower())]; assert len(m)==1,(prefix,m); return doc[m[0]]
K={'MPFW':'Milk powder face wash','HFFW':'Honey fix','CFW':'Cream face wash','MFT':'Milk face toner','RWT':'Rosewater facial','TTT':'Tea tree water','MDS':'Milk drops brightening','BS':'Beautifying serum','BAS':'Better ageing serum','UEC':'Under eye cream','AVG':'Aloa vera gel','UMC':'Ultra moisturiser','GMS':'Goat milk shampoo','AFS':'Anti frizz hair serum','CC':'Cream conditioner','HGO':'Hair growth oil','ADO':'Anti-dandruff Hair oil','HS':'Herbal shampoo','GMHM':'Goat milk hair mask','LBG':'Lip balm –grapefruit','MLB':'Milk lip balm','LS':'Lip scrub','LBL':'Lip balm-lemon','FC':'Foot cream (treat','MBL':'Milk body lotion','DSR':'Deo shot (vanilla','CBP':'Cookie n cream body polish','GMBW':'Goat milk body wash','DSL':'Deo shot- lavender','SPF':'Melt-in-Milk Sunscreen','MMM':'Milk mud mask','CFM':'Charcoal face mask','WRM':'Wild rose face mask','CBM':'Cookie n cream body mask'}
NAME={'MPFW':'Milk Powder Face Wash','HFFW':'Honey Face Wash','CFW':'Fragrance-Free Cream Face Wash','MFT':'Milk Face Toner','RWT':'Rosewater Facial Toner','TTT':'Tea Tree Water Toner','MDS':'Milk Drops Serum','BS':'Beautifying Serum','BAS':'Better Ageing Serum','UEC':'Under Eye Cream','AVG':'Aloe Vera Gel','UMC':'Ultra Moisturising Cream','GMS':'Goat Milk Shampoo','AFS':'Anti-Frizz Hair Serum','CC':'Cream Conditioner','HGO':'Hair Growth Oil','ADO':'Anti-Dandruff Hair Oil','HS':'Herbal Shampoo','GMHM':'Goat Milk Hair Mask','LBG':'Grapefruit Lip Balm','MLB':'Milk Lip Balm SPF 30','LS':'Lip Scrub','LBL':'Lemon Lip Balm','FC':'Foot Care Cream','MBL':'Milk Body Lotion','DSR':'Rose & Vanilla Deo Shot','CBP':'Cookie N Cream Body Polish','GMBW':'Goat Milk Body Wash','DSL':'Lavender & Sage Deo Shot','SPF':'Melt-in-Milk Sunscreen SPF 50','MMM':'Milk Mud Mask','CFM':'Charcoal Face Mask','WRM':'Wild Rose Face Mask','CBM':'Cookie N Cream Body Mask'}
MAP={'15976621080963':'SPF MDS MFT','15976344125827':'BAS MDS','15976121139587':'AFS GMS','15976115470723':'GMHM GMS','15976112062851':'ADO HS','15976102953347':'CC AFS GMS','15976076083587':'HS','15976069693827':'CC','15976062452099':'GMS','15415429955971':'RWT AVG','15415431266691':'DSR DSL','15415431463299':'BAS UEC','15415431692675':'HFFW AVG RWT','15415431856515':'BAS UMC','15415432872323':'AVG HFFW','15415434346883':'MMM MDS','15415434903939':'MFT MDS','15415435854211':'SPF MDS','15415436640643':'MPFW MDS','15415430578563':'WRM','15415432839555':'CFM','15415430414723':'CFW','15415432675715':'MPFW','15415430054275':'HFFW','15415432708483':'DSL','15415433003395':'DSR','15415432085891':'LS','15415431758211':'LS LBL','15415431037315':'LS LBG','15415430316419':'SPF MLB','15415430611331':'LBL','15415431299459':'LBG','15415432642947':'MLB','15415430775171':'CBM CBP','15415432216963':'GMBW MBL','15415430447491':'HGO GMS','15415431201155':'GMS CC','15415431954819':'HGO HS','15415432937859':'FC','15415432446339':'MBL','15415431627139':'CBM','15415431233923':'CBP','15415430840707':'GMBW','15415430185347':'MMM','15415430676867':'AVG','15415431332227':'UEC','15415432348035':'UMC','15415432282499':'AFS','15415431987587':'GMHM','15415430087043':'CC','15415430873475':'GMS','15415431594371':'HS','15415432118659':'ADO','15415430152579':'HGO','15415430349187':'BAS','15415432380803':'BS','15415435067779':'MDS','15415430218115':'MFT','15415431004547':'RWT'}
def split_items(s):
    out=[];depth=0;cur=''
    for ch in s:
        if ch=='(': depth+=1
        if ch==')': depth=max(0,depth-1)
        if ch==',' and depth==0: out.append(cur);cur=''
        else: cur+=ch
    out.append(cur); res=[]
    for x in out:
        x=re.sub(r'\s+',' ',x).strip().rstrip('.').strip('"').strip()
        if not x: continue
        m=re.match(r'^(\*+)\s*(.*)$',x); mk=len(m.group(1)) if m else 0; nm=m.group(2) if m else x
        nm=re.sub(r'\s*\(\s*',' (',nm).replace(' )',')').strip()
        res.append([nm,mk])
    return res
def legend(t):
    labs=[re.sub(r'\s+',' ',l).strip(' |"') for l in re.split(r'\*+',t) if l.strip(' |"')]
    return {str(i+1):l[0].upper()+l[1:].lower() for i,l in enumerate(labs[:2])}
def comp(k):
    e=D(K[k]); return {'n':NAME[k],'l':split_items(e['inci']),'g':legend(e['legend']) if e['legend'] else {}}
P=json.load(open('prototype/products.json')); n=0
for p in P:
    p.pop('inci',None)
    if p['id'] in MAP: p['inci']=[comp(k) for k in MAP[p['id']].split()]; n+=1
json.dump(P,open('prototype/products.json','w'),ensure_ascii=False,separators=(',',':'))
print('products with lists',n)
for pid in ['15415430054275','15415430873475','15415432380803','15415431004547']:
    x=[p for p in P if p['id']==pid][0]['inci'][0]; print(x['n'],x['g'],len(x['l']),x['l'][:5])
print(collections.Counter(len(c['l']) for p in P if p.get('inci') for c in p['inci']).most_common(15))
