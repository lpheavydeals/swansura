"""Remove product prices from collection page text (18 Nov 2026; user: prices now change weekly).

Usage: python3 tools/shopify/collection_price_strip_2026-11-18.py <admin_collections.json> <out plan.json>
Input = Admin read of all collections: id, handle, seo{title description}, copy=custom.seo_copy, faq=custom.faq.
Keeps thresholds (free delivery over £40, £5 off over £70 with SAVE5, under/over £X, £X to £Y bands).
Cost FAQ answers become "Each product page shows its current price."; stock FAQ answers keep counts.
MAN / RMAN = hand rewrites of sentences the rules cannot fix cleanly.
"""
import json,re,sys
P=r'£\d{1,3}(?:,\d{3})*(?:\.\d{2})?(?![\d.,]\d)'
PROT=[r'£\d+(?!\.\d) (?:to|and|-|–) £\d+(?!\.\d)(?! (?:for|each))',
      r'(?:[Uu]nder|[Oo]ver|above|below|[Pp]ass|past the|reach the|[Cc]lears? the|the|[Ss]pend|[Bb]udget of|within|delivery starts at|[Oo]rders of) £\d+(?!\.\d)',
      r'£\d+(?!\.\d) (?:off|free|and over|or more|budget|threshold|mark|line|edit|range|band)',
      r'[Gg]ifts? (?:under|over) £\d+', r'£\d+-£\d+']
def protect(t):
    store=[]
    def sub(m):
        store.append(m.group(0)); return '\u00a7%d\u00a7'%(len(store)-1)
    for p in PROT: t=re.sub(p,sub,t)
    return t,store
def restore(t,store):
    for i,v in enumerate(store): t=t.replace('\u00a7%d\u00a7'%i,v)
    return t
GEN='Each product page shows its current price.'
def faq_answer(q,a):
    o=a
    # range answers for cost questions
    if has(a) and re.match(r'(?i)(how much|what do .* cost|what does .* cost|what is the price|what are the prices|what can i buy)',q):
        # keep any non-price sentences
        sents=re.split(r'(?<=[.!?])\s+',a)
        keep=[s for s in sents if not has(s)]
        a=' '.join([GEN]+keep) if not keep or GEN not in keep else ' '.join(keep)
    a=re.sub(r'(\d+ products?), from '+P+' to '+P+r'(?=[:.,])',r'\1',a)
    a=re.sub(r'\bProducts from '+P+' to '+P+': ','Products by type: ',a)
    a=re.sub(r'\bProducts from '+P+' to '+P+r'\.','',a)
    return a.strip(),o
def text(t0):
    t,store=protect(t0)
    PP=P+r'(?: for \d+ ?ml)?'
    t=re.sub(r' \(((?:'+P+r'(?: for \d+\s?ML| for \d+ml)?)(?:,? (?:or|and) )?)+\)','',t)
    t=re.sub(r',? (?:at|for|from|priced at|priced from|between|are|is|cost) '+PP+' (?:or|and|to) '+PP+r'(?: each)?(?=[ .,;:)<])','',t)
    t=re.sub(r',? (?:at|are|is|cost|costs) '+P+r' each(?=[ .,;:)<])','',t)
    t=re.sub(r',? (?:both|each|also) '+P+r'(?=[ .,;:)<])','',t)
    t=re.sub(r' \((?:both |each |from |all |only )?'+P+r'(?: each)?\)','',t)
    t=re.sub(r'\('+P+r', ([^)]+)\)',r'(\1)',t)
    t=re.sub(r'\(([^)£]+), '+P+r'\)',r'(\1)',t)
    t=re.sub(r',? (?:priced )?from '+P+' to '+P+r'(?=[ ,.;:)])','',t)
    t=re.sub(r', (?:at|for|from|starting at|priced at) '+P+r',(?= (?:is|are|has|have|pairs|uses|gives|makes|adds|brings|combines|offers|sits|comes|was)\b)','',t)
    t=re.sub(r', (?:at|for|from|starting at|priced at) '+P+',',',',t)
    t=re.sub(r',? (?:at|for|from|starting at|priced at|costs?|is) '+P+r'(?=[.,;:)<]|\s*$)','',t)
    t=re.sub(r' (?:at|for) '+P+r'(?= (?:and|or|is|with|it|makes|gives|sits|in|this)\b)','',t)
    return restore(t,store)
def has(x):
    t,_=protect(x); return bool(re.search(P,t))
def run(nodes):
    out=[]
    for n in nodes:
        rec={'id':n['id'],'handle':n['handle']}
        d=(n['seo'] or {}).get('description') or ''
        if has(d):
            rec['desc']=[d,text(d)]; rec['seo_title']=(n['seo'] or {}).get('title')
        c=(n['copy'] or {}).get('value') or ''
        if has(c): rec['copy']=[c,text(c)]
        f=(n['faq'] or {}).get('value') or ''
        if has(f):
            arr=json.loads(f); new=[]
            for q,a in arr:
                a2,_=faq_answer(q,a); new.append([q,text(a2)])
            rec['faq']=[f,json.dumps(new,ensure_ascii=False)]
        if len(rec)>2: out.append(rec)
    for r in out:  # hand fix: a 'what can I buy' answer needs content, not just the price note
        if r['handle']=='gifts-under-50' and 'faq' in r:
            a=json.loads(r['faq'][1]); a[0][1]='Perfume minis and gift sets, natural skincare kits and stocking fillers, all priced under £50. Each product page shows its current price.'
            r['faq'][1]=json.dumps(a,ensure_ascii=False)
    return out
# (handle, original text, replacement) applied to desc/copy/faq BEFORE the generic rules
MAN=[
('fragrance','357 authentic scents, from minis at £14.99 to rare extraits,','357 authentic scents, from minis to rare extraits,'),
('the-woods-collection','each in a 100ml bottle at £39.99 or £40.99.','each in a 100ml bottle.'),
('the-woods-collection',' One fixed price makes it easy to pick by mood rather than budget.',' Pick by mood: the range runs from fresh and green to warm and amber.'),
('the-woods-collection','At £39.99 to £40.99 each, they also suit','They also suit'),
('signature-dorient','Aura, Paradiso and Charm (£63.99 to £66.99) come with','Aura, Paradiso and Charm come with'),
('signature-dorient',' Diamond is £65.99, Jade £66.99, and Opal and Rose £63.99.',''),
('hugo-boss','Eau de Parfum Intense 100ml at £70.99 puts','Eau de Parfum Intense 100ml puts'),
('acqua-di-parma','Most of our nine pieces are 20ml sprays at £40.99, with sets and grooming from £32.99, so','Most of our nine pieces are 20ml sprays, with sets and grooming too, so'),
('dolce-gabbana','holds five scents, at £39.99 for women and £34.99 for men.','holds five scents, one for women and one for men.'),
('gucci','from pen sprays and miniatures at £16.95 to a full gift set at £84.99.','from pen sprays and miniatures to a full gift set.'),
('guerlain','from £44.99 for a miniature set to £94.99 for a 125ml bottle,','from a miniature set to a 125ml bottle,'),
('skincare','Prices start at £6.99, so you can try a single cleanser or build a full routine.','You can try a single cleanser or build a full routine.'),
('bodycare',', and each bath bar costs £15.99 or less.','.'),
('bodycare','a body scrub at £16.99 made with','a body scrub made with'),
('john-varvatos',' The John Varvatos Artisan Eau de Toilette 75ml is priced at £32.99.',''),
('burberry','It is also £48.99 for 50ml and £58.99 for 90ml, so you can choose the size that suits you.','It comes in 50ml and 90ml, so you can choose the size that suits you.'),
('chloe','Perfume Set 4x5ml at £45.99 lets you try','Perfume Set 4x5ml lets you try'),
('calvin-klein','with suede and warm woods, at £22.99 for the full bottle or £18.99 as a mini.','with suede and warm woods, as a full bottle or a mini.'),
('carolina-herrera','We stock seven, from £19.99 for the 10ml Bad Boy Le Parfum up to £76.99 for the 150ml bottle.','We stock seven, from the 10ml Bad Boy Le Parfum up to the 150ml bottle.'),
('elie-saab','from £31.99 for Elixir to £52.99 for the Le Parfum gift set.','from Elixir to the Le Parfum gift set.'),
('elizabeth-arden','At £16.99 for a full 100ml, it makes a generous present,','As a full 100ml, it makes a generous present,'),
('dunhill',' The four Desire eaux de toilette are £28.99 each, and the ten Signature Collection eaux de parfum are £45.99.',''),
('lancome','The 25ml Idôle Nectar Eau de Parfum is £39.99 and a handy size for your bag.','The 25ml Idôle Nectar Eau de Parfum is a handy size for your bag.'),
('trussardi','from 7ml miniatures at £14.99 to the 90ml Pure Jasmine at £42.99.','from 7ml miniatures to the 90ml Pure Jasmine.'),
('price-0-15','Small kits such as Deyga Hydro Boosting Skin Care Kit and Clear Skin Kit are £14.99.','Small kits such as Deyga Hydro Boosting Skin Care Kit and Clear Skin Kit sit here too.'),
('price-0-15','For the bath, Swansura Selection goat milk soap bars are £9.99, and Deyga Charcoal Bath Bar is £10.99.','For the bath, there are goat milk soap bars and Deyga Charcoal Bath Bar.'),
('price-15-25','Gucci Bloom Parfum 10ml Miniature Spray and Gucci Guilty Pour Femme 10ml are £19.99, and Calvin Klein Eternity, Defy and My Euphoria 10ml minis are £18.99 each.','Gucci Bloom Parfum 10ml Miniature Spray, Gucci Guilty Pour Femme 10ml and the Calvin Klein Eternity, Defy and My Euphoria 10ml minis all sit here.'),
('price-15-25','Highborn London Crystal Cleanser at £24 and Superior Lip Butter (15ml) at £22.50 bring','Highborn London Crystal Cleanser and Superior Lip Butter (15ml) bring'),
('price-25-50','Calvin Klein Eternity Eau de Parfum is £28.99 and Eternity for Men Eau de Toilette 100ml is £38.99.','Calvin Klein Eternity Eau de Parfum and Eternity for Men Eau de Toilette 100ml both sit here.'),
('price-25-50','Highborn London Imperial Moisturiser is £46, its Cleanse and Tone Pack is £44 and Diamond Toner is £25.','Highborn London Imperial Moisturiser, its Cleanse and Tone Pack and Diamond Toner sit here too.'),
('price-25-50',"anatomē's sleep range fits neatly here: each sleep oil is £28, the pillow sprays are £34, and The Little Gift of Good Sleep is £35.","anatomē's sleep range fits neatly here: the sleep oils, the pillow sprays and The Little Gift of Good Sleep."),
('price-50-9999',' Pre-Eminent Beauty Serum is £66, Night Elixir £56 and Imperial Eye Gel £59.',' Pre-Eminent Beauty Serum, Night Elixir and Imperial Eye Gel sit here too.'),
('price-50-9999','For a complete set, Four Phase Day and Night is £145 and the Seven Phase Collection is £185.','For a complete set, there are Four Phase Day and Night and the Seven Phase Collection.'),
('price-50-9999','anatomē Rose-hip, Grape Seed &amp; Avocado Face Oil is £52, and its Bath &amp; Shower Oils are £68.','anatomē Rose-hip, Grape Seed &amp; Avocado Face Oil and its Bath &amp; Shower Oils sit here too.'),
('price-50-9999','anatomē Eau de Parfum options at £125 include','anatomē Eau de Parfum options here include'),
('body-butter','natural oils, priced from £12.99.','natural oils.'),
('lip-balm-for-dry-lips',', and the Grape Fruit Lip Balm 10g is also £6.99.',', and the Grape Fruit Lip Balm 10g is another option.'),
('niche-perfume',"anatomē's eaux de parfum start at £28 for a smaller size, with larger bottles at £125.","anatomē's eaux de parfum come in a smaller size as well as larger bottles."),
('perfume-gift-sets','Calvin Klein My Euphoria (10 ml, £18.99) and Gucci Flora Gorgeous Orchid (10 ml, £17.99) both start under £20.','Calvin Klein My Euphoria (10 ml) and Gucci Flora Gorgeous Orchid (10 ml) both sit under £20.'),
('gifts-under-25','Trussardi Pure Jasmine and Jimmy Choo I Want Choo Forever cost £14.99 each, and three Hermès Un Jardin minis, all unisex, are £24.99.','Trussardi Pure Jasmine, Jimmy Choo I Want Choo Forever and three unisex Hermès Un Jardin minis all sit here.'),
("gifts-under-25","and Deyga's £19.99 glow kit brings","and Deyga's glow kit brings"),
('gifts-25-to-50',"anatomē's eaux de parfum cost £28 in the smaller size, and","anatomē's eaux de parfum fit here in the smaller size, and"),
('scent-oud','resinous agarwood, up to £299.99.','resinous agarwood.'),
('swansura-selection','Each handmade soap here weighs 115G or 125G and costs £9.99.','Each handmade soap here weighs 115G or 125G.'),
('highborn-london','from a £22.50 lip butter to full regimen collections.','from a lip butter to full regimen collections.'),
('highborn-london','Imperial Moisturiser at £46 helps','Imperial Moisturiser helps'),
('highborn-london','while Night Elixir at £56 gives','while Night Elixir gives'),
('anatome',' Most come in a £28 size and a £125 size.',' Most come in a small and a large size.'),
('anatome','The Chamomile Bath Salts, at £30, blend','The Chamomile Bath Salts blend'),
('anatome','Bath &amp; Shower Oils at £68 add','Bath &amp; Shower Oils add'),
('anatome','The Little Gift of Good Sleep at £35 and The Gift of Good Sleep at £68 make','The Little Gift of Good Sleep and The Gift of Good Sleep make'),
('lalique','Prices start from £28.99, so most sit in our','Most sit in our'),
('michael-kors','</a> is from £13.99.','</a> is the miniature for men.'),
('narciso-rodriguez','The 10ml sprays start from £25.99 and suit','The 10ml sprays suit'),

]
X=r'£\d+(?:\.\d{2})?(?![.\d]\d)'
MAN+=[
('sap',', each at £43.99, so choosing comes down to mood rather than budget.',', so choosing comes down to mood.'),
('hermes','Our pieces start at £24.99, so they are an affordable way into a famous house.','Our pieces are an easy way into a famous house.'),
('hermes','You will find it at £24.99, or at £25.99 in a second listing.','You will find it in two listings.'),
('calvin-klein','Prices start at £18.99, so it is an easy place','The miniatures make it an easy place'),
('body-butter','Body Butter 40G, also £15.99, uses','Body Butter 40G uses'),
('paco-rabanne','</a> starts from £27.99, and a women','</a> is one option, and a women'),
]
RMAN=[
('*',r',? with prices (?:from|starting at|start at) '+X+r'(?: to '+X+r')?',''),
('chloe',r'Prices start (?:at|from) '+X+r', and every piece','Every piece'),
('dkny',r'Prices start (?:at|from) '+X+r', with full 100ml bottles','There are full 100ml bottles'),
('*',r' ?Prices start (?:at|from) '+X+r'\.',''),
('deyga',r'(bath bars such as Shea Saffron and Rose Pink Clay) start at '+X+r'\.',r'\1 round it off.'),
('bvlgari',r'our edit of eight pieces runs from '+X+' to '+X+r'\.','our edit has eight pieces.'),
('jean-paul-gaultier',r' ?The 80ml Eau de Parfum is '+X+r'\.',''),
('s-t-dupont',r', each at '+X+r'\.','.'),
('givenchy',r'the Amarige Eau de Toilette is '+X+r'\.','choose the Amarige Eau de Toilette.'),
('hollister',r' ?The 100ml bottle is '+X+r'\.',''),
('escada',r'The 25ml Magnetism Eau de Parfum is '+X+r'\.','The 25ml Magnetism Eau de Parfum is a handy size.'),
('juicy-couture',r' ?We stock it at '+X+r'\.',''),
('price-25-50',r'(anatomē Balance and Focus Eau de Parfum) start at '+X+r'\.',r'\1 sit here too.'),
('sensitive-skin',r'(Swansura Selection) starts at '+X+r'\.',r'\1 is a gentle place to start.'),
('anatome',r' ?Sleep oils start at '+X+r'\.',''),
]
# POST = hand fixes on the finished page copy, where removing prices left a broken sentence
POST=[
('tom-ford','Prices run, so these are bottles for a special purchase or a gift.','These are bottles for a special purchase or a gift.'),
('giorgio-armani','The Giorgio Armani Code Refillable Eau de Toilette 125ml. Bright','Our pick is the Giorgio Armani Code Refillable Eau de Toilette 125ml. Bright'),
('serge-lutens','Serge Lutens La Fille de Berlin Eau de Parfum 50ml. It is built','Our pick is Serge Lutens La Fille de Berlin Eau de Parfum 50ml. It is built'),
('antonio-banderas',' Each.</p>','</p>'),
('antonio-banderas','Our edit includes bottles from the range.','Our edit includes four bottles from the range.'),
('price-25-50',"DKNY Be Tempted 100ml, and Chloé Rose Naturelle Intense and Nomade Jasmin Naturel Intense. Burberry My Burberry Eau de Parfum 50ml. Bentley's men's range, including Infinite, Momentum Unlimited and Become, sits.","So do DKNY Be Tempted 100ml, Chloé Rose Naturelle Intense, Nomade Jasmin Naturel Intense and Burberry My Burberry Eau de Parfum 50ml, along with Bentley's men's range, including Infinite, Momentum Unlimited and Become."),
('price-25-50','For a skincare gift set, Deyga Vitamin C Daily Glow Combo.','For a skincare gift set, try Deyga Vitamin C Daily Glow Combo.'),
('price-0-15','Vilvah Fragrance-Free Cream Face Wash, and Vilvah Honey Face Wash and Deyga Oat Milk Face Wash. Vilvah Milk Powder Face Wash is a milk face wash. Deyga Pure Rose Water Toner, while Vilvah Wild Rose and Charcoal face masks.','Vilvah Fragrance-Free Cream Face Wash, Vilvah Honey Face Wash and Deyga Oat Milk Face Wash all sit here, and Vilvah Milk Powder Face Wash is a milk face wash. So do Deyga Pure Rose Water Toner and the Vilvah Wild Rose and Charcoal face masks.'),
('price-0-15','Vilvah Natural Lip Scrub, a lip scrub with lemon oil, and Natural Lemon Lip Balm. Deyga Natural Lip Balm is a natural lip balm, and Deyga Beetroot Lip Balm Classic.','Vilvah Natural Lip Scrub, a lip scrub with lemon oil, and Natural Lemon Lip Balm both sit here, as do Deyga Natural Lip Balm and Deyga Beetroot Lip Balm Classic.'),
('price-15-25','Hermès Un Jardin 15ml miniatures, make','Hermès Un Jardin 15ml miniatures make'),
('price-15-25','Deyga Chocolate Body Butter is a chocolate body butter, and Deyga Body Scrub, a fruit-based body scrub. Deyga Charcoal Detox Face Mask and Activated Charcoal Body Wash.','Deyga Chocolate Body Butter, Deyga Body Scrub (a fruit-based body scrub), Deyga Charcoal Detox Face Mask and Activated Charcoal Body Wash all sit here.'),
('price-50-9999','YOUTHBOOST Peptide Serum and Organic Facial Oil, and Bakuchiol Youth Elixir.','So do YOUTHBOOST Peptide Serum, Organic Facial Oil and Bakuchiol Youth Elixir.'),
('price-50-9999','Hemel Valley of Diamond, Fragrance Affair and Patchouli For All.','Hemel Valley of Diamond, Fragrance Affair and Patchouli For All sit here too.'),
('yves-saint-laurent','Yves Saint Laurent Yvresse Eau de Toilette 80ml for Women. Inspired','Our pick is Yves Saint Laurent Yvresse Eau de Toilette 80ml for Women. Inspired'),
('chloe','keeps the finish warm. It.</p>','keeps the finish warm.</p>'),
('chloe','Nomade Eau de Parfum 50ml, blends','Nomade Eau de Parfum 50ml blends'),
('etienne-aigner','masculine finish. It. Its warm','masculine finish. Its warm'),
('etienne-aigner','round it off. It. It is the lighter','round it off. It is the lighter'),
('body-butter-for-dry-skin','with a gentle floral note. Both. For','with a gentle floral note. For'),
('anatome','Most come in a small and a large size. Parfum Travel, a perfume discovery set of six scents.','Most come in a small and a large size, and Parfum Travel is a perfume discovery set of six scents.'),
('anatome','Face Oil, nourishes','Face Oil nourishes'),
('bentley','Unlimited Eau de Toilette, mixes','Unlimited Eau de Toilette mixes'),
('shower-gel-body-wash','free from sulphates and parabens for 115G or 125G.','free from sulphates and parabens, in 115G or 125G sizes.'),
('concern-lips','and Vilvah Natural Lip Scrub with lemon essential oil.','and Vilvah Natural Lip Scrub uses lemon essential oil.'),
('stocking-fillers',"Vilvah's Grape Fruit Lip Balm, and the Strawberry","Vilvah's Grape Fruit Lip Balm is another easy pick, and the Strawberry"),
('range-beetroot','Beetroot Lip Balm Classic 10 g, blends','Beetroot Lip Balm Classic 10 g blends'),
('range-vitamin-c','If you would like both steps together, the Vitamin C Daily Glow Combo.','If you would like both steps together, choose the Vitamin C Daily Glow Combo.'),
('highborn-london','Natural Luminosity Body Butter, smooth','Natural Luminosity Body Butter smooth'),
('hair-fall','from Vilvah and Deyga, focuses on','from Vilvah and Deyga focuses on'),
('scent-floral','Prices start with miniatures under £20, and every bottle','The range runs from miniatures to full bottles, and every bottle'),
('perfume-gift-sets','Gucci Flora Gorgeous Orchid (10 ml) both sit under £20.','Gucci Flora Gorgeous Orchid (10 ml) are two good examples.'),
('anatome','Roman Chamomile Sleep Pillow Spray, made to mist','Roman Chamomile Sleep Pillow Spray are made to mist'),
('fun-basics','At under £20 for a full 100ml, these sit','As full 100ml bottles at everyday prices, these sit'),
('maison-de-milan','With most bottles under £20, these sit','As friendly-priced 100ml bottles, these sit'),
('chris-adams','two 100ml bottles for men, both under £15, making them some of the best-value','two 100ml bottles for men, among the best-value'),
('chris-adams','At these prices, both sit in our','Both sit in our'),
]
def build(orig_nodes):
    import copy as _c
    nodes=_c.deepcopy(orig_nodes); by={n['handle']:n for n in nodes}
    for h,o,nw in MAN:
        n=by[h]
        for k in ('copy','faq'):
            if n[k] and o in n[k]['value']: n[k]['value']=n[k]['value'].replace(o,nw)
        if n['seo'] and o in (n['seo'].get('description') or ''): n['seo']['description']=n['seo']['description'].replace(o,nw)
    for h,p,rp in RMAN:
        for n in (nodes if h=='*' else [by[h]]):
            if n['copy']: n['copy']['value']=re.sub(r'<p>\s*</p>','',re.sub(p,rp,n['copy']['value']))
            if n['seo'] and n['seo'].get('description'): n['seo']['description']=re.sub(p,rp,n['seo']['description'])
    man={n['id']:n for n in nodes}; out=[]
    for n in orig_nodes:
        m=man[n['id']]; rec={'id':n['id'],'handle':n['handle']}
        d0=(n['seo'] or {}).get('description') or ''; d1=text((m['seo'] or {}).get('description') or '')
        if d0!=d1: rec['desc']=[d0,d1]; rec['seo_title']=n['seo']['title']
        c0=(n['copy'] or {}).get('value') or ''; c1=text((m['copy'] or {}).get('value') or '')
        if c0!=c1: rec['copy']=[c0,c1]
        f0=(n['faq'] or {}).get('value') or ''
        if f0:
            new=[[q,text(faq_answer(q,a)[0])] for q,a in json.loads(m['faq']['value'])]
            if json.loads(f0)!=new: rec['faq']=[f0,json.dumps(new,ensure_ascii=False)]
        if len(rec)>2: out.append(rec)
    for r in out:
        for h,o,nw in POST:
            if r['handle']==h and 'copy' in r:
                assert o in r['copy'][1],(h,o); r['copy'][1]=r['copy'][1].replace(o,nw)
    for r in out:  # hand fix: a 'what can I buy' answer needs content, not just the price note
        if r['handle']=='gifts-under-50' and 'faq' in r:
            a=json.loads(r['faq'][1]); a[0][1]='Perfume minis and gift sets, natural skincare kits and stocking fillers, all priced under £50. Each product page shows its current price.'
            r['faq'][1]=json.dumps(a,ensure_ascii=False)
    return out
if __name__=='__main__':
    out=build(json.load(open(sys.argv[1]))); json.dump(out,open(sys.argv[2],'w'),ensure_ascii=False,indent=1); print(len(out))
