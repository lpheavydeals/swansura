# 20 Nov 2026: the 3 USP ads showed 'Invalid asset count in dynamic creative target rule: Multiple descriptions':
# Meta had stored an extra empty description next to ours. Meta re-adds the shop destination + an empty
# description whenever a creative goes onto a Sales ad, so v3 sends NO description (Meta's empty one = 1 description). New creatives (same images/text, one description,
# no shop destination so every click uses the VD10 website link) are swapped onto the same ad ids.
import json,subprocess,os
HERE=os.path.dirname(os.path.abspath(__file__));G='https://graph.facebook.com/v23.0';ACT='act_1614052623400872'
o=json.load(open(HERE+'/usp_adset_2026-11-20.json'))
def run(*a): return subprocess.run(list(a),capture_output=True,text=True).stdout
def jd(t): return json.JSONDecoder().raw_decode(t)[0]
out={}
for n in ('1','2','4'):
    old=jd(run('curl','-sg',f"{G}/{o[n]['creative']}?fields=asset_feed_spec,object_story_spec,url_tags,name"))
    a=old['asset_feed_spec']
    afs={"images":[{"hash":i['hash'],"adlabels":[{"name":i['adlabels'][0]['name']}]} for i in a['images']],
         "bodies":[{"text":a['bodies'][0]['text']}],"titles":[{"text":a['titles'][0]['text']}],
         "link_urls":[{"website_url":a['link_urls'][0]['website_url'],"display_url":"swansura.com"}],
         "call_to_action_types":["SHOP_NOW"],"ad_formats":["SINGLE_IMAGE"],"optimization_type":"PLACEMENT","onsite_destinations":[],
         "asset_customization_rules":[{"customization_spec":{k:v for k,v in r['customization_spec'].items() if k not in('age_min','age_max')},"image_label":{"name":r['image_label']['name']},"priority":r['priority']} for r in a['asset_customization_rules']]}
    c=jd(run('curl','-s','-X','POST',f'{G}/{ACT}/adcreatives','-F',f"name={old['name']} v3",'-F','asset_feed_spec='+json.dumps(afs),
         '-F','object_story_spec='+json.dumps({"page_id":"788176181050418","instagram_user_id":"17841477741370196"}),'-F','url_tags='+old.get('url_tags','')))
    if 'id' not in c: print(n,c); continue
    r=jd(run('curl','-s','-X','POST',f"{G}/{o[n]['ad']}",'-F','creative='+json.dumps({"creative_id":c['id']})))
    out[n]={'ad':o[n]['ad'],'old_creative':o[n]['creative'],'new_creative':c['id'],'swap':r}
    print(n,c['id'],r,flush=True)
json.dump(out,open(HERE+'/usp_fix_v3_2026-11-20.json','w'),indent=1)
