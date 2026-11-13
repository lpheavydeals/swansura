# New creatives for the AM PM + Face Brightening video ads with today's prices; swapped onto the ads in both campaigns.
import json,subprocess
G='https://graph.facebook.com/v23.0';ACT='act_1614052623400872'
sw=json.load(open('swap_tc.json'));sales=json.load(open('sales.json'))['ads']
def run(*a): return subprocess.run(list(a),capture_output=True,text=True).stdout
def jd(t): return json.JSONDecoder().raw_decode(t)[0]
out={};import sys;TEST=len(sys.argv)>1
for k,old,fix in [('Vilvah_AMPMSerumKit','2367835133980266',[('£47.99','£46.99')]),
                  ('Vilvah_FaceBrighteningKitLarge','1632705141672112',[('£42.99','£39.99'),('Free UK delivery on this kit','Free UK delivery over £40')])]:
    c=json.load(open(f'cr_{old}.json'));a=c['asset_feed_spec']
    def f(t):
        for x,y in fix: t=t.replace(x,y)
        return t
    o=sw[k]
    afs={"videos":[{"video_id":o['videos']['4x5'],"thumbnail_hash":o['thumbs']['4x5'],"adlabels":[{"name":"feed45"}]},
                   {"video_id":o['videos']['9x16'],"thumbnail_hash":o['thumbs']['9x16'],"adlabels":[{"name":"vert916"}]}],
         "bodies":[{"text":f(b['text'])} for b in a['bodies']],"titles":[{"text":f(b['text'])} for b in a['titles']],
         "descriptions":[{"text":f(b['text'])} for b in a['descriptions']],"link_urls":[{"website_url":a['link_urls'][0]['website_url']}],
         "call_to_action_types":["SHOP_NOW"],"ad_formats":["SINGLE_VIDEO"],"optimization_type":"PLACEMENT","onsite_destinations":[],
         "asset_customization_rules":[
          {"customization_spec":{"publisher_platforms":["facebook","instagram"],"facebook_positions":["feed","marketplace","profile_feed","search"],"instagram_positions":["stream","explore_home","profile_feed"]},"video_label":{"name":"feed45"},"priority":1},
          {"customization_spec":{"publisher_platforms":["facebook","instagram"],"facebook_positions":["story","facebook_reels"],"instagram_positions":["story","reels"]},"video_label":{"name":"vert916"},"priority":2},
          {"customization_spec":{},"video_label":{"name":"vert916"},"priority":3}]}
    print(k,'\n TITLE',afs['titles'],'\n BODY',afs['bodies'][0]['text'][-90:])
    r=jd(run('curl','-s','-X','POST',f'{G}/{ACT}/adcreatives','-F',f'name=SW | {k} | price fix 13 Nov','-F','asset_feed_spec='+json.dumps(afs),
      '-F','object_story_spec='+json.dumps(c['object_story_spec']),'-F','url_tags='+c['url_tags']))
    if 'id' not in r: print(r);break
    out[k]={'old':old,'new':r['id'],'ads':{}}
    if TEST:
        print(run('curl','-sSg',f"{G}/{r['id']}?fields=asset_feed_spec{{onsite_destinations}}"));break
    for ad in (o['ad'],sales[k]):
        out[k]['ads'][ad]=jd(run('curl','-s','-X','POST',f'{G}/{ad}','-F','creative='+json.dumps({"creative_id":r['id']})))
    print(k,out[k])
json.dump(out,open('price_fix2.json','w'),indent=1)
