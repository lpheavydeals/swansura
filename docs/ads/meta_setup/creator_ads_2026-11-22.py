# 22 Nov 2026: 5 creator videos (permission confirmed by the user 21 Nov), cut in docs/ads/creator_cuts_2026-11-22/,
# uploaded as plain single-video ads (no placement rules: see the USP 'multiple descriptions' lesson), PAUSED,
# in the Vilvah Deyga USP ad set. Each link sets VD10 via /discount/VD10?redirect=…
import json,subprocess,os,time,urllib.parse
HERE=os.path.dirname(os.path.abspath(__file__));D=HERE+'/../creator_cuts_2026-11-22'
G='https://graph.facebook.com/v23.0';ACT='act_1614052623400872';ADSET='120249494273770240'
L=lambda p:'https://www.swansura.com/discount/VD10?redirect='+urllib.parse.quote(p,safe='')
P='Official UK partner of Vilvah & Deyga · Next-day UK delivery · Free UK delivery over £40.'
ADS={
 'Deyga_LipBalmStick_Creator':('Deyga Beetroot Lip Balm Stick | Creator','/products/beetroot-lip-balm-stick-natural-tinted-balm-for-dry-lips-100-organic-ingredients-plant-based-cruelty-free-5-5-g',
   "Dry, chapped lips this winter? 💋 Deyga's Beetroot Lip Balm Stick: a soft twist-up balm with a sheer rosy tint from beetroot.\n\n£13.99, or 10% off with code VD10.\n\n"+P,'Deyga Beetroot Lip Balm Stick','Extra 10% off with code VD10'),
 'Deyga_RiceWaterDuo_Creator':('Deyga Rice Water Shampoo + Soy Milk Conditioner | Creator','/products/deygas-rice-water-shampoo-220ml-natural-hair-care-for-smooth-nourished-hair',
   "Wash day for curls 🌾 Deyga's Rice Water Shampoo with the Soy Milk Conditioner: a gentle lather, then plenty of slip for easy detangling.\n\nShampoo £13.99 · Conditioner £14.99 · 10% off with code VD10.\n\n"+P,'Deyga Rice Water Shampoo','Extra 10% off with code VD10'),
 'Vilvah_FaceBrightening_Creator':('Vilvah Face Brightening Kit | Creator','/products/vilvah-face-brightening-kit-milk-powder-face-wash-milk-drops-brightening-serum-duo-milky-cleanse-radiance-boost-evens-skin-tone-fades-dark-spots',
   "A simple two-step routine ✨ Vilvah Milk Powder Face Wash, then a few drops of Milk Drops serum.\n\nVilvah Face Brightening Kit £31.99, or 10% off with code VD10.\n\n"+P,'Vilvah Face Brightening Kit','Extra 10% off with code VD10'),
 'Deyga_Unboxing_Creator':('Deyga Unboxing | Creator','/collections/deyga',
   "Unboxing Deyga 📦 The 10% Vitamin C Face Serum, the Beetroot Lip Balm and more, now shipped from our UK stock.\n\nExtra 10% off Deyga with code VD10.\n\n"+P,'Deyga, from UK stock','Extra 10% off with code VD10'),
 'Deyga_LipBalmMaking_Creator':('Deyga Beetroot Lip Balm Making | Creator','/products/beetroot-lip-balm-stick-natural-tinted-balm-for-dry-lips-100-organic-ingredients-plant-based-cruelty-free-5-5-g',
   "How Deyga's Beetroot Lip Balm is made 🌱 Butters and oils with beetroot for a mild, rosy tint.\n\nShipped from our UK stock. 10% off with code VD10.\n\n"+P,'Deyga Beetroot Lip Balm','Extra 10% off with code VD10'),
}
def run(*a): return subprocess.run(list(a),capture_output=True,text=True).stdout
def jd(t): return json.JSONDecoder().raw_decode(t)[0]
F=HERE+'/creator_ads_2026-11-22.json';out=json.load(open(F)) if os.path.exists(F) else {}
for k in ADS:
    o=out.setdefault(k,{})
    if 'video' not in o:
        f=f'{D}/{k}_9x16.mp4';tj=f'{D}/{k}_thumb.jpg'
        run('ffmpeg','-v','error','-y','-ss','1.2','-i',f,'-frames:v','1','-q:v','2',tj)
        o['video']=jd(run('curl','-s','-X','POST',f'{G}/{ACT}/advideos','-F',f'name=SW {k} 22Nov','-F',f'source=@{f}'))['id']
        o['thumb']=list(jd(run('curl','-s','-X','POST',f'{G}/{ACT}/adimages','-F',f'filename=@{tj}'))['images'].values())[0]['hash']
        json.dump(out,open(F,'w'),indent=1);print(k,'uploaded',o['video'],flush=True)
for k,(nm,path,body,hl,ds) in ADS.items():
    o=out[k]
    for _ in range(80):
        if jd(run('curl','-sg',f"{G}/{o['video']}?fields=status"))['status']['video_status']=='ready': break
        time.sleep(15)
    if 'creative' not in o:
        vd={"video_id":o['video'],"image_hash":o['thumb'],"message":body,"title":hl,"link_description":ds,
            "call_to_action":{"type":"SHOP_NOW","value":{"link":L(path),"link_caption":"swansura.com"}}}
        c=jd(run('curl','-s','-X','POST',f'{G}/{ACT}/adcreatives','-F',f'name=SW USP | {nm} | 22 Nov',
           '-F','object_story_spec='+json.dumps({"page_id":"788176181050418","instagram_user_id":"17841477741370196","video_data":vd}),
           '-F','url_tags=utm_source=meta&utm_medium=paid_social&utm_campaign={{campaign.name}}&utm_content={{ad.name}}'))
        if 'id' not in c: print(k,c);continue
        o['creative']=c['id']
    if 'ad' not in o:
        a=jd(run('curl','-s','-X','POST',f'{G}/{ACT}/ads','-F',f'name={nm}','-F',f'adset_id={ADSET}','-F','creative='+json.dumps({"creative_id":o['creative']}),'-F','status=PAUSED'))
        if 'id' not in a: print(k,a);continue
        o['ad']=a['id']
    json.dump(out,open(F,'w'),indent=1);print(k,o['creative'],o['ad'],flush=True)
