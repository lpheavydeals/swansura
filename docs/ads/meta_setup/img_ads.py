# Upload Style B image ads (4x5/1x1/9x16) and create one PAUSED image ad per kit in the Sales ad set.
import json,re,subprocess,os
HERE=os.path.dirname(os.path.abspath(__file__));D=HERE+'/../image_ads_2026-11-13'
G='https://graph.facebook.com/v23.0';ACT='act_1614052623400872';ADSET='120249389744460240'
MD=open(D+'/Image_Ad_Copy_2026-11-13.md').read()
U='https://www.swansura.com/products/'
K=[('Vilvah_AMPMSerumKit','## 1.','Vilvah AM PM Serum Kit','vilvah-am-pm-serum-kit'),
('Vilvah_FaceBrighteningKitLarge','## 2.','Vilvah Face Brightening Kit Large','vilvah-face-brightening-kit-large'),
('Vilvah_MilkFaceKit','## 3.','Vilvah Milk Face Kit','vilvah-milk-face-kit-milk-mud-mask-milk-drops-brightening-serum-de-tans-brightens-clears-skin-oatmilk-saffron-rice-milk-extracts'),
('Deyga_LipBalmStick','## 4.','Deyga Beetroot Lip Balm Stick','beetroot-lip-balm-stick-natural-tinted-balm-for-dry-lips-100-organic-ingredients-plant-based-cruelty-free-5-5-g'),
('Vilvah_FaceLiftKit','## 5.','Vilvah Face Lift Kit','vilvah-face-lift-kit'),
('Vilvah_MilkBodyKit','## 6.','Vilvah Milk Body Kit','vilvah-milk-body-kit-goat-milk-body-wash-milk-body-lotion-deep-hydration-skin-softening-nourishment-oat-milk-olive-squalane-coconut-oil-vanilla-scent')]
def run(*a): return subprocess.run(list(a),capture_output=True,text=True).stdout
def jd(t): return json.JSONDecoder().raw_decode(t)[0]
out=json.load(open(HERE+'/img_ads.json')) if os.path.exists(HERE+'/img_ads.json') else {}
for k,hd,nm,h in K:
    o=out.setdefault(k,{})
    if 'hashes' not in o:
        o['hashes']={}
        for z in ('4x5','1x1','9x16'):
            im=jd(run('curl','-s','-X','POST',f'{G}/{ACT}/adimages','-F',f'filename=@{D}/{k}_B_{z}.jpg'))
            o['hashes'][z]=list(im['images'].values())[0]['hash']
    i=MD.index(hd);j=MD.find('\n## ',i+5);sec=MD[i:j if j>0 else len(MD)]
    body=re.search(r'\*\*Primary text:\*\*\n(.*?)\n\*\*Headline',sec,re.S).group(1).strip()
    hl=re.search(r'\*\*Headline:\*\* (.*)',sec).group(1).strip();ds=re.search(r'\*\*Description:\*\* (.*)',sec).group(1).strip()
    afs={"images":[{"hash":o['hashes']['4x5'],"adlabels":[{"name":"i45"}]},{"hash":o['hashes']['9x16'],"adlabels":[{"name":"i916"}]},{"hash":o['hashes']['1x1'],"adlabels":[{"name":"i11"}]}],
      "bodies":[{"text":body}],"titles":[{"text":hl}],"descriptions":[{"text":ds}],"link_urls":[{"website_url":U+h}],
      "call_to_action_types":["SHOP_NOW"],"ad_formats":["SINGLE_IMAGE"],"optimization_type":"PLACEMENT",
      "asset_customization_rules":[
       {"customization_spec":{"publisher_platforms":["facebook","instagram"],"facebook_positions":["feed","marketplace","profile_feed"],"instagram_positions":["stream","explore_home","profile_feed"]},"image_label":{"name":"i45"},"priority":1},
       {"customization_spec":{"publisher_platforms":["facebook","instagram"],"facebook_positions":["story","facebook_reels"],"instagram_positions":["story","reels"]},"image_label":{"name":"i916"},"priority":2},
       {"customization_spec":{},"image_label":{"name":"i11"},"priority":3}]}
    if 'creative' not in o:
        c=jd(run('curl','-s','-X','POST',f'{G}/{ACT}/adcreatives','-F',f'name=SW Sales | {nm} | Image B','-F','asset_feed_spec='+json.dumps(afs),
          '-F','object_story_spec='+json.dumps({"page_id":"788176181050418","instagram_user_id":"17841477741370196"}),
          '-F','url_tags=utm_source=meta&utm_medium=paid_social&utm_campaign={{campaign.name}}&utm_content={{ad.name}}'))
        if 'id' not in c: print(k,c);break
        o['creative']=c['id']
    if 'ad' not in o:
        a=jd(run('curl','-s','-X','POST',f'{G}/{ACT}/ads','-F',f'name={nm.split(" ",1)[1] if False else nm} | Image 4x5+1x1+9x16 | Swansura','-F',f'adset_id={ADSET}','-F','creative='+json.dumps({"creative_id":o['creative']}),'-F','status=PAUSED'))
        if 'id' not in a: print(k,a);break
        o['ad']=a['id']
    print(k,o['creative'],o['ad'],flush=True)
    json.dump(out,open(HERE+'/img_ads.json','w'),indent=1)
