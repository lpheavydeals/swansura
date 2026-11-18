# 18 Nov 2026: 4 more Deyga/Vilvah video ads for the Purchase ad sets (all PAUSED).
# Videos re-cut in the PJS-only style with the T&Cs line (scratchpad ads/ed build3.py + ov3.js keys r/g/p, build2.py key n).
# Copy is neutral: no 'you know from home' (Meta personal-attributes rule, the ad sets now target areas, not people).
# usage: python3 new_ads_2026-11-18.py <video dir>  -> new_ads_ampm_v2_2026-11-18.json
import json,subprocess,sys,os,time
D=sys.argv[1];HERE=os.path.dirname(os.path.abspath(__file__))
G='https://graph.facebook.com/v23.0';ACT='act_1614052623400872'
KITS='120249456165350240';LIPS='120249456165580240'
P='Official UK partner of {} · Free UK delivery over £40.'
ADS={
 'Vilvah_AMPMSerumKit_v2':(KITS,'Vilvah AM PM Serum Kit (hands)','https://www.swansura.com/products/vilvah-am-pm-serum-kit',
   "A day serum and a night serum from Vilvah, shipped from the UK.\n\nMorning: Milk Drops, with rice milk extract, hyaluronic acid and aloe.\nNight: Better Ageing Serum, with bakuchiol, blue pea flower and peptides.\n\nLight layers you pat in, morning and night. "+P.format('Vilvah'),
   'Vilvah AM PM Serum Kit, £46.99','Milk Drops + Better Ageing Serum'),
}
def run(*a): return subprocess.run(list(a),capture_output=True,text=True).stdout
def jd(t): return json.JSONDecoder().raw_decode(t)[0]
out={}
for k in ADS:
    vid={};th={}
    for z in ('4x5','9x16'):
        f=f'{D}/{k}_{z}.mp4';tj=f'{D}/{k}_{z}_thumb.jpg'
        run('ffmpeg','-v','error','-y','-ss','1.2','-i',f,'-frames:v','1','-q:v','2',tj)
        v=jd(run('curl','-s','-X','POST',f'{G}/{ACT}/advideos','-F',f'name=SW {k} {z} 18Nov','-F',f'source=@{f}'));vid[z]=v['id']
        im=jd(run('curl','-s','-X','POST',f'{G}/{ACT}/adimages','-F',f'filename=@{tj}'));th[z]=list(im['images'].values())[0]['hash']
    out[k]={'videos':vid,'thumbs':th};print(k,'uploaded',vid,flush=True)
for k,o in out.items():
    for _ in range(80):
        st=[jd(run('curl','-s',f"{G}/{v}?fields=status"))['status']['video_status'] for v in o['videos'].values()]
        if all(s=='ready' for s in st): break
        time.sleep(15)
    adset,nm,url,body,head,desc=ADS[k]
    afs={"videos":[{"video_id":o['videos']['4x5'],"thumbnail_hash":o['thumbs']['4x5'],"adlabels":[{"name":"feed45"}]},
                   {"video_id":o['videos']['9x16'],"thumbnail_hash":o['thumbs']['9x16'],"adlabels":[{"name":"vert916"}]}],
         "bodies":[{"text":body}],"titles":[{"text":head}],"descriptions":[{"text":desc}],"link_urls":[{"website_url":url}],
         "call_to_action_types":["SHOP_NOW"],"ad_formats":["SINGLE_VIDEO"],"optimization_type":"PLACEMENT","onsite_destinations":[],
         "asset_customization_rules":[
          {"customization_spec":{"publisher_platforms":["facebook","instagram"],"facebook_positions":["feed","marketplace","profile_feed","search"],"instagram_positions":["stream","explore_home","profile_feed"]},"video_label":{"name":"feed45"},"priority":1},
          {"customization_spec":{"publisher_platforms":["facebook","instagram"],"facebook_positions":["story","facebook_reels"],"instagram_positions":["story","reels"]},"video_label":{"name":"vert916"},"priority":2},
          {"customization_spec":{},"video_label":{"name":"vert916"},"priority":3}]}
    oss={"page_id":"788176181050418","instagram_user_id":"17841477741370196"}
    c=jd(run('curl','-s','-X','POST',f'{G}/{ACT}/adcreatives','-F',f'name=SW Sales | {nm} | 18 Nov','-F','asset_feed_spec='+json.dumps(afs),'-F','object_story_spec='+json.dumps(oss),
         '-F','url_tags=utm_source=meta&utm_medium=paid_social&utm_campaign={{campaign.name}}&utm_content={{ad.name}}'))
    o['creative']=c.get('id') or c
    if c.get('id'):
        a=jd(run('curl','-s','-X','POST',f'{G}/{ACT}/ads','-F',f'name={nm} | Video 4x5+9x16 | Swansura','-F',f'adset_id={adset}',
             '-F','creative='+json.dumps({"creative_id":c['id']}),'-F','status=PAUSED'))
        o['ad']=a.get('id') or a;o['adset']=adset
    print(k,o.get('creative'),o.get('ad'),flush=True)
json.dump(out,open(f'{HERE}/new_ads_ampm_v2_2026-11-18.json','w'),indent=1,ensure_ascii=False)
