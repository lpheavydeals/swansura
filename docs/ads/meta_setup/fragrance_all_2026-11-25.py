# 25 Nov 2026 (user: 'retargeting is too early … use the 12 pounds for the fragrances campaign alone'):
# one broad catalogue ad set with ALL in-stock fragrance (every brand except the skincare ones) in the
# Fragrance Catalogue campaign (CBO £12/day); the 7 brand ad sets are paused (not deleted) so Meta learns on one ad set.
import json,subprocess,os,sys
G='https://graph.facebook.com/v23.0';ACT='act_1614052623400872';CAT='2794613394240386'
PAGE='788176181050418';IG='17841477741370196';PIXEL='1593636862064099'
FRAME='52ec2ca6493e95062dd7e0511d58fcc2';CAMP='120249535916100240'
F=os.path.dirname(os.path.abspath(__file__))+'/fragrance_all_2026-11-25.json'
out=json.load(open(F)) if os.path.exists(F) else {}
def call(method,path,**kw):
    a=['curl','-s','-X',method,f'{G}/{path}']
    for k,v in kw.items(): a+=['--data-urlencode',f'{k}={v if isinstance(v,str) else json.dumps(v)}']
    r=json.loads(subprocess.run(a,capture_output=True,text=True).stdout);print(path,json.dumps(r)[:300])
    if 'error' in r: json.dump(out,open(F,'w'),indent=1);sys.exit(1)
    return r
SKIN=['Vilvah','Deyga','Highborn London','anatomē','Shiseido','Swansura - The Body Studio']
if 'product_set' not in out:
    flt={'and':[{'availability':{'eq':'in stock'}},{'retailer_id':{'neq':'63257659736451'}},{'retailer_id':{'neq':'y18oi6oxge'}}]+[{'brand':{'neq':b}} for b in SKIN]}
    out['product_set']=call('POST',f'{CAT}/product_sets',name='SW Ads | All fragrance in stock',filter=flt)['id']
T={'geo_locations':{'countries':['GB'],'location_types':['home','recent']},'age_min':25,'age_max':55,
   'targeting_automation':{'advantage_audience':0},'publisher_platforms':['facebook','instagram'],
   'facebook_positions':['feed','story','profile_feed'],
   'instagram_positions':['stream','story','reels','explore_home','profile_feed'],'device_platforms':['mobile','desktop']}
if 'adset' not in out:
    out['adset']=call('POST',f'{ACT}/adsets',name='All fragrance | Catalogue UK 25-55 | Purchase',campaign_id=CAMP,
        status='PAUSED',billing_event='IMPRESSIONS',optimization_goal='OFFSITE_CONVERSIONS',
        promoted_object={'product_set_id':out['product_set'],'custom_event_type':'PURCHASE'},
        attribution_spec=[{'event_type':'CLICK_THROUGH','window_days':7},{'event_type':'VIEW_THROUGH','window_days':1}],
        targeting=T)['id']; json.dump(out,open(F,'w'),indent=1)
LAY=[{'layer_type':'image','image_source':'catalog'},
     {'layer_type':'frame_overlay','frame_source':'custom','frame_image_hash':FRAME,'opacity':100,
      'overlay_position':'center','scale':100,'blending_mode':'normal'}]
MSG=('Designer, niche and Arabian perfume from UK stock: Tom Ford, Gucci, Versace, Paco Rabanne, Al Haramain, Franck Olivier and more.'
     '\n\n100% authentic, shipped from the UK. Free UK delivery over £40.')
if 'creative' not in out:
    out['creative']=call('POST',f'{ACT}/adcreatives',name='SW Catalogue | All fragrance | emerald frame',product_set_id=out['product_set'],
        object_story_spec={'page_id':PAGE,'instagram_user_id':IG,'template_data':{
            'message':MSG,'link':'https://www.swansura.com/collections/fragrance','name':'{{product.name}}',
            'description':'{{product.price}}','call_to_action':{'type':'SHOP_NOW'},'multi_share_end_card':False,
            'image_layer_specs':LAY}},
        url_tags='utm_source=facebook&utm_medium=paid_social&utm_campaign=fragrance_catalogue&utm_content=all_fragrance')['id']
if 'ad' not in out:
    out['ad']=call('POST',f'{ACT}/ads',name='All fragrance | Catalogue carousel | Emerald frame',adset_id=out['adset'],status='PAUSED',
        creative={'creative_id':out['creative']},tracking_specs=[{'action.type':['offsite_conversion'],'fb_pixel':[PIXEL]}])['id']
json.dump(out,open(F,'w'),indent=1)
