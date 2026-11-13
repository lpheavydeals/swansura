import json,re,subprocess,sys
S=sys.argv[1];MD=open('/home/user/swansura/docs/ads/creatives_2026-11-12/Meta_Ad_Copy_2026-11-12.md').read()
vid={};th={}
for l in open(S+'/videos.tsv'):
    k,z,r=l.rstrip('\n').split('\t');vid[(k,z)]=json.loads(r)['id']
for l in open(S+'/thumbs.tsv'):
    k,z,h=l.rstrip('\n').split('\t');th[(k,z)]=h
KITS=[('Vilvah_AMPMSerumKit','## 4. Vilvah AM PM Serum Kit','Vilvah AM PM Serum Kit','https://www.swansura.com/products/vilvah-am-pm-serum-kit'),
('Vilvah_FaceBrighteningKitLarge','## 8. Vilvah Face Brightening Kit (Large)','Vilvah Face Brightening Kit Large','https://www.swansura.com/products/vilvah-face-brightening-kit-large'),
('Vilvah_BestsellerHairKit','## 5. Vilvah Bestseller Hair Kit','Vilvah Bestseller Hair Kit','https://www.swansura.com/products/vilvah-bestseller-hair-kit-goat-milk-shampoo-200ml-cream-conditioner-200ml-nourishing-frizz-control-sulfate-free-hair-care-set'),
('Deyga_ABCKit','## 6. Deyga ABC Kit','Deyga ABC Kit','https://www.swansura.com/products/natural-skincare-set-deygas-aloe-vera-gel-beetroot-lip-balm-charcoal-bath-bar-for-hydrated-skin-soft-lips-clean-body'),
('Deyga_NourishedLipsKit','## 9. Deyga Nourished Lip Care Kit','Deyga Nourished Lip Care Kit','https://www.swansura.com/products/nourished-lip-care-kit-deygas-strawberry-lip-scrub-beetroot-lip-balm-set-for-soft-smooth-hydrated-lips'),
('Deyga_ClearSkinKit','## 7. Deyga Clear Skin Kit','Deyga Clear Skin Kit','https://www.swansura.com/products/deyga-clear-skin-kit')]
out={}
for k,hd,nm,url in KITS:
    i=MD.index(hd);sec=MD[i:MD.find('\n## ',i+5) if MD.find('\n## ',i+5)>0 else len(MD)]
    a=re.search(r'\*\*Primary text \(A[^\n]*\*\*\n(.*?)\n\n\*\*Primary text \(B',sec,re.S).group(1).strip()
    h=re.search(r'\*\*Headline:\*\* (.*)',sec).group(1).strip();d=re.search(r'\*\*Description:\*\* (.*)',sec).group(1).strip()
    afs={"videos":[{"video_id":vid[(k,'4x5')],"thumbnail_hash":th[(k,'4x5')],"adlabels":[{"name":"feed45"}]},
                   {"video_id":vid[(k,'9x16')],"thumbnail_hash":th[(k,'9x16')],"adlabels":[{"name":"vert916"}]}],
         "bodies":[{"text":a}],"titles":[{"text":h}],"descriptions":[{"text":d}],"link_urls":[{"website_url":url}],
         "call_to_action_types":["SHOP_NOW"],"ad_formats":["SINGLE_VIDEO"],"optimization_type":"PLACEMENT",
         "asset_customization_rules":[
          {"customization_spec":{"publisher_platforms":["facebook","instagram"],"facebook_positions":["feed","video_feeds","marketplace","profile_feed","search"],"instagram_positions":["stream","explore","explore_home","profile_feed"]},"video_label":{"name":"feed45"},"priority":1},
          {"customization_spec":{"publisher_platforms":["facebook","instagram"],"facebook_positions":["story","facebook_reels"],"instagram_positions":["story","reels"]},"video_label":{"name":"vert916"},"priority":2},
          {"customization_spec":{},"video_label":{"name":"vert916"},"priority":3}]}
    oss={"page_id":"788176181050418","instagram_user_id":"17841477741370196"}
    cmd=['curl','-s','-X','POST','https://graph.facebook.com/v23.0/act_1614052623400872/adcreatives','-F','name=SW Eng | '+nm,'-F','asset_feed_spec='+json.dumps(afs),'-F','object_story_spec='+json.dumps(oss),
         '-F','url_tags=utm_source=meta&utm_medium=paid_social&utm_campaign={{campaign.name}}&utm_content={{ad.name}}']
    r=json.loads(subprocess.run(cmd,capture_output=True,text=True).stdout);print(k,'creative',r);
    if 'id' not in r: break
    ad=['curl','-s','-X','POST','https://graph.facebook.com/v23.0/act_1614052623400872/ads','-F','name='+nm+' | Video 4x5+9x16 | From home','-F','adset_id=120249382199750240','-F','creative='+json.dumps({"creative_id":r['id']}),'-F','status=PAUSED']
    r2=json.loads(subprocess.run(ad,capture_output=True,text=True).stdout);print(k,'ad',r2);out[k]={'creative':r['id'],'ad':r2.get('id'),'err':r2.get('error')}
    if 'id' not in r2: break
json.dump(out,open(S+'/ads.json','w'),indent=1)
