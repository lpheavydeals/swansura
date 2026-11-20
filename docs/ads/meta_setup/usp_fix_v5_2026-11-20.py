# 20 Nov 2026 (v5): Ads Manager still refused edits on the 3 USP ads ('Invalid asset count in dynamic creative target
# rule: Multiple descriptions') because Meta keeps adding a 2nd description to placement-customised Sales creatives.
# v5 = plain single-image link ads (4:5 image, no asset_feed_spec / placement rules), same text, link and UTMs.
import json,subprocess,os
HERE=os.path.dirname(os.path.abspath(__file__));G='https://graph.facebook.com/v23.0';ACT='act_1614052623400872'
o=json.load(open(HERE+'/usp_adset_2026-11-20.json'))
DESC={'1':'Next-day UK delivery','2':'10% off with code VD10','4':'Extra 10% off with code VD10'}
def run(*a): return subprocess.run(list(a),capture_output=True,text=True).stdout
def jd(t): return json.JSONDecoder().raw_decode(t)[0]
out={}
for n in ('1','2','4'):
    old=jd(run('curl','-sg',f"{G}/{o[n]['creative']}?fields=asset_feed_spec,url_tags"))
    a=old['asset_feed_spec']
    ld={"image_hash":o[n]['hashes']['4x5'],"link":a['link_urls'][0]['website_url'],"message":a['bodies'][0]['text'],"name":a['titles'][0]['text'],
        "description":DESC[n],"caption":"swansura.com","call_to_action":{"type":"SHOP_NOW","value":{"link":a['link_urls'][0]['website_url']}}}
    oss={"page_id":"788176181050418","instagram_user_id":"17841477741370196","link_data":ld}
    c=jd(run('curl','-s','-X','POST',f'{G}/{ACT}/adcreatives','-F',f"name=SW Sales | USP {n} | 20 Nov v5 single image",'-F','object_story_spec='+json.dumps(oss),'-F','url_tags='+old.get('url_tags','')))
    if 'id' not in c: print(n,c); continue
    r=jd(run('curl','-s','-X','POST',f"{G}/{o[n]['ad']}",'-F','creative='+json.dumps({"creative_id":c['id']})))
    out[n]={'ad':o[n]['ad'],'new_creative':c['id'],'swap':r}; print(n,c['id'],r,flush=True)
json.dump(out,open(HERE+'/usp_fix_v5_2026-11-20.json','w'),indent=1)
