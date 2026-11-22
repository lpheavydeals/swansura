# 22 Nov 2026 (user): retargeting campaign. Audience = Engagement campaign video ThruPlay viewers (custom audience
# 120249508222170240, 365 days, video_view_15s on the 20 Engagement videos linked to the Page) + website visitors 30d
# (added once the Custom Audience terms are accepted). £2/day, PURCHASE, the 3 USP image ads (same v5 creatives), all PAUSED.
# Usage: python3 retargeting_2026-11-22.py            -> builds campaign, ad set, 3 ads (idempotent, ids in the .json)
#        python3 retargeting_2026-11-22.py visitors   -> creates 'SW | Website visitors 30d' + 'SW | Purchasers 180d'
#                                                         and puts them on the ad set (include visitors, exclude buyers)
import json,subprocess,os,sys
HERE=os.path.dirname(os.path.abspath(__file__))
G='https://graph.facebook.com/v23.0';ACT='act_1614052623400872';PIX='1593636862064099'
TP='120249508222170240'
F=HERE+'/retargeting_2026-11-22.json';out=json.load(open(F)) if os.path.exists(F) else {}
ADS=[('Retargeting | Next-day, no import | Image','4041959056099428'),
     ('Retargeting | Skip the overseas delay | Image','1622551932956110'),
     ('Retargeting | Next-day price list | Image','1676710674008468')]
def post(path,**kw):
    a=['curl','-s','-X','POST',f'{G}/{path}']
    for k,v in kw.items(): a+=['--data-urlencode',f'{k}={v}']
    r=json.loads(subprocess.run(a,capture_output=True,text=True).stdout)
    if 'error' in r: print(path,r['error']);raise SystemExit(1)
    return r
def save(): json.dump(out,open(F,'w'),indent=1)
def targeting(inc,exc=()):
    t={"geo_locations":{"countries":["GB"],"location_types":["home","recent"]},"age_min":18,"age_max":65,
       "custom_audiences":[{"id":i} for i in inc],
       "targeting_automation":{"advantage_audience":0},
       "publisher_platforms":["facebook","instagram"],
       "facebook_positions":["feed","marketplace","story","search","facebook_reels","profile_feed"],
       "instagram_positions":["stream","story","reels","explore_home","profile_feed"],"device_platforms":["mobile","desktop"]}
    if exc: t["excluded_custom_audiences"]=[{"id":i} for i in exc]
    return t
def aud(name,desc,rule):
    return post(f'{ACT}/customaudiences',name=name,description=desc,prefill='true',rule=json.dumps(rule))['id']

if len(sys.argv)>1 and sys.argv[1]=='visitors':
    if 'visitors' not in out:
        out['visitors']=aud('SW | Website visitors 30d','All swansura.com visitors, last 30 days (pixel)',
          {"inclusions":{"operator":"or","rules":[{"event_sources":[{"id":PIX,"type":"pixel"}],"retention_seconds":2592000,
           "filter":{"operator":"and","filters":[{"field":"url","operator":"i_contains","value":"swansura.com"}]}}]}});save()
    if 'buyers' not in out:
        out['buyers']=aud('SW | Purchasers 180d','Bought on swansura.com, last 180 days (pixel Purchase)',
          {"inclusions":{"operator":"or","rules":[{"event_sources":[{"id":PIX,"type":"pixel"}],"retention_seconds":15552000,
           "filter":{"operator":"and","filters":[{"field":"event","operator":"eq","value":"Purchase"}]}}]}});save()
    post(out['adset'],targeting=json.dumps(targeting([TP,out['visitors']],[out['buyers']])))
    print('ad set now: ThruPlay + website visitors 30d, purchasers 180d excluded');raise SystemExit

if 'campaign' not in out:
    out['campaign']=post(f'{ACT}/campaigns',name='SW | Retargeting | Warm UK',objective='OUTCOME_SALES',
        special_ad_categories='[]',status='PAUSED',is_adset_budget_sharing_enabled='false')['id'];save()
if 'adset' not in out:
    out['adset']=post(f'{ACT}/adsets',name='ThruPlay viewers + site visitors | Purchase',campaign_id=out['campaign'],
        daily_budget='200',billing_event='IMPRESSIONS',optimization_goal='OFFSITE_CONVERSIONS',bid_strategy='LOWEST_COST_WITHOUT_CAP',
        promoted_object=json.dumps({"pixel_id":PIX,"custom_event_type":"PURCHASE"}),
        attribution_spec=json.dumps([{"event_type":"CLICK_THROUGH","window_days":7},{"event_type":"VIEW_THROUGH","window_days":1}]),
        targeting=json.dumps(targeting([TP])),status='PAUSED')['id'];save()
for nm,cr in ADS:
    if nm not in out:
        out[nm]=post(f'{ACT}/ads',name=nm,adset_id=out['adset'],creative=json.dumps({"creative_id":cr}),status='PAUSED',
            tracking_specs=json.dumps([{"action.type":["offsite_conversion"],"fb_pixel":[PIX]}]))['id'];save()
print(json.dumps(out,indent=1))
