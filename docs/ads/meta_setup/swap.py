# Upload re-cut kit videos, build new creatives (same copy/placements as mk.py) and point the existing ads at them.
# usage: python3 swap.py <video dir> <tag>   -> writes videos_<tag>.tsv, thumbs_<tag>.tsv, swap_<tag>.json
import json,re,subprocess,sys,os
D,TAG=sys.argv[1],sys.argv[2];HERE=os.path.dirname(os.path.abspath(__file__))
G='https://graph.facebook.com/v23.0';ACT='act_1614052623400872'
MD=open(HERE+'/../creatives_2026-11-12/Meta_Ad_Copy_2026-11-12.md').read()
ADS={'Vilvah_AMPMSerumKit':('120249382770680240','## 4. Vilvah AM PM Serum Kit','Vilvah AM PM Serum Kit','https://www.swansura.com/products/vilvah-am-pm-serum-kit'),
'Vilvah_FaceBrighteningKitLarge':('120249382771140240','## 8. Vilvah Face Brightening Kit (Large)','Vilvah Face Brightening Kit Large','https://www.swansura.com/products/vilvah-face-brightening-kit-large')}
a2=json.load(open(HERE+'/ads2.json'))
for k,h,nm,url in [('Vilvah_MilkFaceKit','## 10. Vilvah Milk Face Kit','Vilvah Milk Face Kit','https://www.swansura.com/products/vilvah-milk-face-kit-milk-mud-mask-milk-drops-brightening-serum-de-tans-brightens-clears-skin-oatmilk-saffron-rice-milk-extracts'),
('Deyga_LipBalmStick','## 11. Deyga Beetroot Lip Balm Stick','Deyga Beetroot Lip Balm Stick','https://www.swansura.com/products/beetroot-lip-balm-stick-natural-tinted-balm-for-dry-lips-100-organic-ingredients-plant-based-cruelty-free-5-5-g'),
('Vilvah_FaceLiftKit','## 12. Vilvah Face Lift Kit','Vilvah Face Lift Kit','https://www.swansura.com/products/vilvah-face-lift-kit'),
('Vilvah_MilkBodyKit','## 13. Vilvah Milk Body Kit','Vilvah Milk Body Kit','https://www.swansura.com/products/vilvah-milk-body-kit-goat-milk-body-wash-milk-body-lotion-deep-hydration-skin-softening-nourishment-oat-milk-olive-squalane-coconut-oil-vanilla-scent')]:
    ADS[k]=(a2[k]['ad'],h,nm,url)
def run(*a): return subprocess.run(list(a),capture_output=True,text=True).stdout
def jd(t): return json.JSONDecoder().raw_decode(t)[0]
out={}
for k,(ad,hd,nm,url) in ADS.items():
    vid={};th={}
    for z in ('4x5','9x16'):
        f=f'{D}/{k}_{z}.mp4';tj=f'{D}/{k}_{z}_thumb.jpg'
        run('ffmpeg','-v','error','-y','-ss','1.2','-i',f,'-frames:v','1','-q:v','2',tj)
        v=jd(run('curl','-s','-X','POST',f'{G}/{ACT}/advideos','-F',f'name=SW kit {k} {z} {TAG}','-F',f'source=@{f}'))
        vid[z]=v['id'];open(f'{HERE}/videos_{TAG}.tsv','a').write(f'{k}\t{z}\t{json.dumps(v)}\n')
        im=jd(run('curl','-s','-X','POST',f'{G}/{ACT}/adimages','-F',f'filename=@{tj}'))
        th[z]=list(im['images'].values())[0]['hash'];open(f'{HERE}/thumbs_{TAG}.tsv','a').write(f'{k}\t{z}\t{th[z]}\n')
    out[k]={'ad':ad,'videos':vid,'thumbs':th};print(k,'uploaded',vid,flush=True)
import time
for k,o in out.items():
    for _ in range(80):
        st=[jd(run('curl','-s',f"{G}/{v}?fields=status"))['status']['video_status'] for v in o['videos'].values()]
        if all(s=='ready' for s in st): break
        time.sleep(15)
    ad,hd,nm,url=ADS[k]
    i=MD.index(hd);j=MD.find('\n## ',i+5);sec=MD[i:j if j>0 else len(MD)]
    a=re.search(r'\*\*Primary text \(A[^\n]*\*\*\n(.*?)\n\n\*\*Primary text \(B',sec,re.S).group(1).strip()
    h=re.search(r'\*\*Headline:\*\* (.*)',sec).group(1).strip();d=re.search(r'\*\*Description:\*\* (.*)',sec).group(1).strip()
    afs={"videos":[{"video_id":o['videos']['4x5'],"thumbnail_hash":o['thumbs']['4x5'],"adlabels":[{"name":"feed45"}]},
                   {"video_id":o['videos']['9x16'],"thumbnail_hash":o['thumbs']['9x16'],"adlabels":[{"name":"vert916"}]}],
         "bodies":[{"text":a}],"titles":[{"text":h}],"descriptions":[{"text":d}],"link_urls":[{"website_url":url}],
         "call_to_action_types":["SHOP_NOW"],"ad_formats":["SINGLE_VIDEO"],"optimization_type":"PLACEMENT",
         "asset_customization_rules":[
          {"customization_spec":{"publisher_platforms":["facebook","instagram"],"facebook_positions":["feed","video_feeds","marketplace","profile_feed","search"],"instagram_positions":["stream","explore","explore_home","profile_feed"]},"video_label":{"name":"feed45"},"priority":1},
          {"customization_spec":{"publisher_platforms":["facebook","instagram"],"facebook_positions":["story","facebook_reels"],"instagram_positions":["story","reels"]},"video_label":{"name":"vert916"},"priority":2},
          {"customization_spec":{},"video_label":{"name":"vert916"},"priority":3}]}
    oss={"page_id":"788176181050418","instagram_user_id":"17841477741370196"}
    c=jd(run('curl','-s','-X','POST',f'{G}/{ACT}/adcreatives','-F',f'name=SW Eng | {nm} | {TAG}','-F','asset_feed_spec='+json.dumps(afs),'-F','object_story_spec='+json.dumps(oss),
         '-F','url_tags=utm_source=meta&utm_medium=paid_social&utm_campaign={{campaign.name}}&utm_content={{ad.name}}'))
    o['creative']=c.get('id');o['creative_err']=c.get('error')
    if c.get('id'):
        r=jd(run('curl','-s','-X','POST',f'{G}/{ad}','-F','creative='+json.dumps({"creative_id":c['id']})));o['swap']=r
    print(k,'creative',c.get('id') or c,'swap',o.get('swap'),flush=True)
json.dump(out,open(f'{HERE}/swap_{TAG}.json','w'),indent=1)
