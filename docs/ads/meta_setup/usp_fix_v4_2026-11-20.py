# 20 Nov 2026 (v4): 'Invalid asset count in dynamic creative target rule: Multiple descriptions'. Meta adds its shop
# destination + an extra description to every creative on a Sales ad, and the placement rules (image_label only)
# then see 2 descriptions. Fix: label our description (and body/title) and name those labels in every rule.
import json,subprocess,os
HERE=os.path.dirname(os.path.abspath(__file__));G='https://graph.facebook.com/v23.0';ACT='act_1614052623400872'
o=json.load(open(HERE+'/usp_adset_2026-11-20.json'))
DESC={'1':'Next-day UK delivery','2':'10% off with code VD10','4':'Extra 10% off with code VD10'}
def run(*a): return subprocess.run(list(a),capture_output=True,text=True).stdout
def jd(t): return json.JSONDecoder().raw_decode(t)[0]
out={}
for n in ('1','2','4'):
    old=jd(run('curl','-sg',f"{G}/{o[n]['creative']}?fields=asset_feed_spec,url_tags,name"))
    a=old['asset_feed_spec']
    rules=[]
    for r in a['asset_customization_rules']:
        cs={k:v for k,v in r['customization_spec'].items() if k not in('age_min','age_max')}
        rules.append({"customization_spec":cs,"image_label":{"name":r['image_label']['name']},"body_label":{"name":"b1"},"title_label":{"name":"t1"},
                      "description_label":{"name":"d1"},"link_url_label":{"name":"l1"},"priority":r['priority']})
    afs={"images":[{"hash":i['hash'],"adlabels":[{"name":i['adlabels'][0]['name']}]} for i in a['images']],
         "bodies":[{"text":a['bodies'][0]['text'],"adlabels":[{"name":"b1"}]}],"titles":[{"text":a['titles'][0]['text'],"adlabels":[{"name":"t1"}]}],
         "descriptions":[{"text":DESC[n],"adlabels":[{"name":"d1"}]}],
         "link_urls":[{"website_url":a['link_urls'][0]['website_url'],"display_url":"swansura.com","adlabels":[{"name":"l1"}]}],
         "call_to_action_types":["SHOP_NOW"],"ad_formats":["SINGLE_IMAGE"],"optimization_type":"PLACEMENT","asset_customization_rules":rules}
    c=jd(run('curl','-s','-X','POST',f'{G}/{ACT}/adcreatives','-F',f"name=SW Sales | USP {n} | 20 Nov v4",'-F','asset_feed_spec='+json.dumps(afs),
         '-F','object_story_spec='+json.dumps({"page_id":"788176181050418","instagram_user_id":"17841477741370196"}),'-F','url_tags='+old.get('url_tags','')))
    if 'id' not in c: print(n,c); continue
    r=jd(run('curl','-s','-X','POST',f"{G}/{o[n]['ad']}",'-F','creative='+json.dumps({"creative_id":c['id']})))
    out[n]={'ad':o[n]['ad'],'new_creative':c['id'],'swap':r}; print(n,c['id'],r,flush=True)
json.dump(out,open(HERE+'/usp_fix_v4_2026-11-20.json','w'),indent=1)
