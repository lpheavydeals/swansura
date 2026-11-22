# 22 Nov 2026 (user): add the newly uploaded creator videos to the Engagement ad set 'Adv+ UK 22-55 | ThruPlay'
# (120249382199750240): Vilvah Milk Drops & Face Wash, AM PM Kit, Milk Powder Kit; Deyga Lip Balm Classic, Hair Care Kit.
# Plain single-video ads, PAUSED, with their OWN creatives (a creative shared with a Sales ad gets the shop destination,
# which the Engagement objective refuses). Same copy/headline/links as the Sales creator ads. Videos used as uploaded.
import json,subprocess,os,urllib.parse
HERE=os.path.dirname(os.path.abspath(__file__))
G='https://graph.facebook.com/v23.0';ACT='act_1614052623400872';ADSET='120249382199750240'
L=lambda p:'https://www.swansura.com/discount/VD10?redirect='+urllib.parse.quote(p,safe='')
HL="Next-day UK delivery. UK's Official Partner"
def U(b): return ("Next-day UK delivery, no customs or import fees, VAT included. Extra 10% off "+b+" with code VD10.\n\n"
                  "Official UK partner of "+b+" · Free UK delivery over £40.")
AMPM='/products/vilvah-am-pm-serum-kit'
FBK='/products/vilvah-face-brightening-kit-milk-powder-face-wash-milk-drops-brightening-serum-duo-milky-cleanse-radiance-boost-evens-skin-tone-fades-dark-spots'
ADS=[('1643892144100116','Vilvah Face Brightening Kit | Creator 2 | Engagement','Vilvah',FBK,
      "Vilvah's Face Brightening Kit, shipped from our UK stock ✨ Milk Powder Face Wash, then a few drops of Milk Drops serum."),
     ('990666766968753','Vilvah AM PM Serum Kit | Creator 1 | Engagement','Vilvah',AMPM,
      "Vilvah's AM PM Serum Kit, shipped from our UK stock 🌿 Milk Drops serum for the morning, Better Ageing Serum for the evening."),
     ('1883744626141972','Vilvah Face Brightening Kit | Creator 1 | Engagement','Vilvah',FBK,
      "Vilvah's Face Brightening Kit, shipped from our UK stock ✨ Milk Powder Face Wash, then a few drops of Milk Drops serum."),
     ('1861015078386242','Deyga Beetroot Lip Balm Classic | Creator | Engagement','Deyga','/products/deygas-beetroot-lip-balm-classic-10-g-100-natural-no-harsh-chemicals',
      "Deyga's Beetroot Lip Balm Classic, shipped from our UK stock 🌿 The original tinted beetroot lip balm, 10 g."),
     ('2189394721686902','Deyga Hair Care Kit | Creator | Engagement','Deyga','/products/hair-care-set-deygas-rice-water-shampoo-soy-milk-conditioner-hair-growth-oil-set-for-strong-smooth-frizz-tamed-hair',
      "Deyga's Hair Care Kit, shipped from our UK stock 🌿 Rice Water Shampoo, Soy Milk Conditioner and Hair Growth Oil in one set.")]
def run(*a): return json.JSONDecoder().raw_decode(subprocess.run(list(a),capture_output=True,text=True).stdout)[0]
F=HERE+'/engagement_creator_2026-11-22.json';out=json.load(open(F)) if os.path.exists(F) else {}
def save(): json.dump(out,open(F,'w'),indent=1)
for vid,nm,b,path,line in ADS:
    o=out.setdefault(vid,{})
    if 'thumb_url' not in o:
        th=run('curl','-sg',f'{G}/{vid}/thumbnails?fields=uri,is_preferred')['data']
        o['thumb_url']=(next((t for t in th if t.get('is_preferred')),th[0]))['uri'];save()
    if 'creative' not in o:
        vd={"video_id":vid,"image_url":o['thumb_url'],"message":line+"\n\n"+U(b),"title":HL,
            "link_description":"Extra 10% off "+b+" with code VD10",
            "call_to_action":{"type":"SHOP_NOW","value":{"link":L(path),"link_caption":"swansura.com"}}}
        c=run('curl','-s','-X','POST',f'{G}/{ACT}/adcreatives','--data-urlencode',f'name=SW Eng | {nm} | 22 Nov',
           '--data-urlencode','object_story_spec='+json.dumps({"page_id":"788176181050418","instagram_user_id":"17841477741370196","video_data":vd}),
           '--data-urlencode','url_tags=utm_source=meta&utm_medium=paid_social&utm_campaign={{campaign.name}}&utm_content={{ad.name}}')
        if 'id' not in c: print(nm,c);continue
        o['creative']=c['id'];save()
    if 'ad' not in o:
        a=run('curl','-s','-X','POST',f'{G}/{ACT}/ads','--data-urlencode',f'name={nm}','-d',f'adset_id={ADSET}',
           '--data-urlencode','creative='+json.dumps({"creative_id":o['creative']}),'-d','status=PAUSED')
        if 'id' not in a: print(nm,a);continue
        o['ad']=a['id'];save()
    print(nm,o['creative'],o['ad'],flush=True)
