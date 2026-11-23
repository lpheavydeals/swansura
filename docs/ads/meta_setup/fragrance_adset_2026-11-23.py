# 23 Nov 2026 (user: 'build the fragrance ad set as draft, before we'll confirm the ad creatives'):
# new campaign + ad set, both PAUSED, no ads yet (ads come after the user confirms the creatives).
# Broad UK 25-55, all genders, no interests or postcodes (the narrow skincare audience cost £28.63 CPM),
# PURCHASE on the pixel, £10/day, same placements as the Vilvah ad set (no FB Marketplace / Reels).
import json,subprocess,os
G='https://graph.facebook.com/v23.0';ACT='act_1614052623400872'
F=os.path.dirname(os.path.abspath(__file__))+'/fragrance_adset_2026-11-23.json'
out=json.load(open(F)) if os.path.exists(F) else {}
def post(path,**kw):
    a=['curl','-s','-X','POST',f'{G}/{path}']
    for k,v in kw.items(): a+=['--data-urlencode',f'{k}={v if isinstance(v,str) else json.dumps(v)}']
    r=json.loads(subprocess.run(a,capture_output=True,text=True).stdout);print(path,r);return r
if 'campaign' not in out:
    out['campaign']=post(f'{ACT}/campaigns',name='SW | Sales | Fragrance | UK',objective='OUTCOME_SALES',status='PAUSED',
        special_ad_categories=[],is_adset_budget_sharing_enabled='false')['id']
if 'adset' not in out:
    T={'geo_locations':{'countries':['GB'],'location_types':['home','recent']},'age_min':25,'age_max':55,
       'targeting_automation':{'advantage_audience':0},'publisher_platforms':['facebook','instagram'],
       'facebook_positions':['feed','story','profile_feed'],
       'instagram_positions':['stream','story','reels','explore_home','profile_feed'],'device_platforms':['mobile','desktop']}
    out['adset']=post(f'{ACT}/adsets',name='Fragrance UK 25-55 | Purchase',campaign_id=out['campaign'],status='PAUSED',
        daily_budget='1000',billing_event='IMPRESSIONS',optimization_goal='OFFSITE_CONVERSIONS',bid_strategy='LOWEST_COST_WITHOUT_CAP',
        promoted_object={'pixel_id':'1593636862064099','custom_event_type':'PURCHASE'},
        attribution_spec=[{'event_type':'CLICK_THROUGH','window_days':7},{'event_type':'VIEW_THROUGH','window_days':1}],
        targeting=T)['id']
json.dump(out,open(F,'w'),indent=1)
