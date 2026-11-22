# 22 Nov 2026 (user): the 5 Deyga videos the user uploaded to the ad library are made into plain single-video ads,
# PAUSED, in 'Lip balm W21-50 | Purchase' (120249456165580240); headline = next-day delivery USP + price,
# links via /discount/VD10?redirect=… . Videos used as uploaded (user: no edits). The 3 older paused ads are kept.
import json,subprocess,os,urllib.parse
HERE=os.path.dirname(os.path.abspath(__file__))
G='https://graph.facebook.com/v23.0';ACT='act_1614052623400872';ADSET='120249456165580240'
L=lambda p:'https://www.swansura.com/discount/VD10?redirect='+urllib.parse.quote(p,safe='')
P='Official UK partner of Deyga · Free UK delivery over £40.'
U="Next-day UK delivery, no customs or import fees, VAT included. Extra 10% off Deyga with code VD10.\n\n"+P
def T(a): return a+"\n\n"+U
ADS=[('1894983298355849','Deyga Beetroot Lip Balm Stick | Creator','/products/beetroot-lip-balm-stick-natural-tinted-balm-for-dry-lips-100-organic-ingredients-plant-based-cruelty-free-5-5-g',
      T("Deyga's Beetroot Lip Balm Stick, shipped from our UK stock 🌿 A tinted beetroot lip balm in an easy twist-up stick."),'Next-day UK delivery · £13.99'),
     ('1861015078386242','Deyga Beetroot Lip Balm Classic | Creator','/products/deygas-beetroot-lip-balm-classic-10-g-100-natural-no-harsh-chemicals',
      T("Deyga's Beetroot Lip Balm Classic, shipped from our UK stock 🌿 The original tinted beetroot lip balm, 10 g."),'Next-day UK delivery · £10.99'),
     ('2189394721686902','Deyga Hair Care Kit | Creator','/products/hair-care-set-deygas-rice-water-shampoo-soy-milk-conditioner-hair-growth-oil-set-for-strong-smooth-frizz-tamed-hair',
      T("Deyga's Hair Care Kit, shipped from our UK stock 🌿 Rice Water Shampoo, Soy Milk Conditioner and Hair Growth Oil in one set."),'Next-day UK delivery · £36.99'),
     ('1461008032254744','Deyga Rice Water Shampoo | Creator','/products/deygas-rice-water-shampoo-220ml-natural-hair-care-for-smooth-nourished-hair',
      T("Deyga's Rice Water Shampoo, shipped from our UK stock 🌿 A rice water shampoo for regular use, 220 ml."),'Next-day UK delivery · £13.99'),
     ('1476686071301494','Deyga Plant Based Hair Colour | Creator','/products/100-plant-based-hair-color-black-natural-henna-indigo-dye-kit-grey-coverage-sensitive-scalp-deygas',
      T("Deyga's Plant Based Hair Colour in Black, shipped from our UK stock 🌿 A henna and indigo hair colour kit."),'Next-day UK delivery · £16.99')]
def run(*a): return subprocess.run(list(a),capture_output=True,text=True).stdout
def jd(t): return json.JSONDecoder().raw_decode(t)[0]
F=HERE+'/deyga_creator_2026-11-22.json';out=json.load(open(F)) if os.path.exists(F) else {}
def save(): json.dump(out,open(F,'w'),indent=1)
for vid,nm,path,body,hl in ADS:
    o=out.setdefault(vid,{})
    if 'thumb_url' not in o:
        th=jd(run('curl','-sg',f'{G}/{vid}/thumbnails?fields=uri,is_preferred'))['data']
        o['thumb_url']=(next((t for t in th if t.get('is_preferred')),th[0]))['uri'];save()
    if 'creative' not in o:
        vd={"video_id":vid,"image_url":o['thumb_url'],"message":body,"title":hl,"link_description":"Extra 10% off Deyga with code VD10",
            "call_to_action":{"type":"SHOP_NOW","value":{"link":L(path),"link_caption":"swansura.com"}}}
        c=jd(run('curl','-s','-X','POST',f'{G}/{ACT}/adcreatives','--data-urlencode',f'name=SW Deyga | {nm} | 22 Nov',
           '--data-urlencode','object_story_spec='+json.dumps({"page_id":"788176181050418","instagram_user_id":"17841477741370196","video_data":vd}),
           '--data-urlencode','url_tags=utm_source=meta&utm_medium=paid_social&utm_campaign={{campaign.name}}&utm_content={{ad.name}}'))
        if 'id' not in c: print(nm,c);continue
        o['creative']=c['id'];save()
    if 'ad' not in o:
        a=jd(run('curl','-s','-X','POST',f'{G}/{ACT}/ads','--data-urlencode',f'name={nm}','-d',f'adset_id={ADSET}',
           '--data-urlencode','creative='+json.dumps({"creative_id":o['creative']}),'-d','status=PAUSED',
           '--data-urlencode','tracking_specs='+json.dumps([{"action.type":["offsite_conversion"],"fb_pixel":["1593636862064099"]}])))
        if 'id' not in a: print(nm,a);continue
        o['ad']=a['id'];save()
    print(nm,o['creative'],o['ad'],flush=True)
