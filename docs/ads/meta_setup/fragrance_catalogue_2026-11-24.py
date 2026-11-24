# 24 Nov 2026 (user: 'Go ahead, build them as draft. Budget as 8 Pounds'): brand-by-brand fragrance catalogue ads.
# Every product set has the filter 'brand = X AND in stock', so sold-out items fall out on their own whenever
# Shopify syncs stock to the catalogue. Paco Rabanne Fame EDP Refillable 80ml (dearer than other UK shops) is left out.
# Campaign budget £8/day (CBO) with ONE ad set per brand (Meta refuses an ad whose product set is not the ad set's own
# product set, error 1885054, so a shared ad set with brand ads is not possible); each ad set: PURCHASE on the pixel,
# GB 25-55, all genders, same placements as the fragrance ad set; one emerald-framed carousel ad in each. Everything PAUSED: nothing spends until the user switches it on.
import json,subprocess,os,sys
G='https://graph.facebook.com/v23.0';ACT='act_1614052623400872';CAT='2794613394240386'
PAGE='788176181050418';IG='17841477741370196';PIXEL='1593636862064099'
FRAME='52ec2ca6493e95062dd7e0511d58fcc2'  # docs/ads/catalogue_frames_2026-11-24/frame_emerald.png
F=os.path.dirname(os.path.abspath(__file__))+'/fragrance_catalogue_2026-11-24.json'
out=json.load(open(F)) if os.path.exists(F) else {}
def call(method,path,**kw):
    a=['curl','-s','-X',method,f'{G}/{path}']
    for k,v in kw.items(): a+=['--data-urlencode',f'{k}={v if isinstance(v,str) else json.dumps(v)}']
    r=json.loads(subprocess.run(a,capture_output=True,text=True).stdout);print(path,json.dumps(r)[:300]);
    if 'error' in r: json.dump(out,open(F,'w'),indent=1);sys.exit(1)
    return r
INS={'availability':{'eq':'in stock'}}
BRANDS=[ # brand, collection, message
 ('Tom Ford','tom-ford','Tom Ford perfume, in stock in the UK: Oud Wood, Black Orchid, Noir Extreme and Neroli Portofino.'),
 ('Chopard','chopard','Chopard Malaki perfumes and the Gardens of Paradise discovery set, in stock in the UK.'),
 ('Gucci','gucci','Gucci perfume from UK stock: Intense Oud, Guilty, Bloom and Flora, plus minis and gift sets.'),
 ('Al Haramain','al-haramain','Al Haramain perfume from UK stock: the Amber Oud editions and the L’Aventure range.'),
 ('Tiziana Terenzi','tiziana-terenzi','Tiziana Terenzi extrait de parfum from UK stock: Kirke, Borelli, Draconis, Caput Mundi and more.'),
 ('Versace','versace','Versace perfume from UK stock: Eros, Eros Pour Femme and Yellow Diamond, plus 5ml minis.'),
 ('Paco Rabanne','paco-rabanne','Paco Rabanne perfume from UK stock: 1 Million, Invictus, Phantom, Lady Million and Fame, plus mini sets.'),
]
TAIL='\n\n100% authentic, shipped from the UK. Free UK delivery over £40.'
EXCL={'Paco Rabanne':[{'retailer_id':{'neq':'63257659736451'}}]}
sets=out.setdefault('product_sets',{});sets.setdefault('Tom Ford','1671141295054261')
for b,_,_ in BRANDS:
    if b not in sets:
        flt={'and':[{'brand':{'eq':b}},INS]+EXCL.get(b,[])}
        sets[b]=call('POST',f'{CAT}/product_sets',name=f'SW Ads | {b} in stock',filter=flt)['id']
if 'all' not in out:
    flt={'and':[{'or':[{'brand':{'eq':b}} for b,_,_ in BRANDS]},INS,{'retailer_id':{'neq':'63257659736451'}}]}
    out['all']=call('POST',f'{CAT}/product_sets',name='SW Ads | Fragrance catalogue brands in stock',filter=flt)['id']
if 'campaign' not in out:
    out['campaign']=call('POST',f'{ACT}/campaigns',name='SW | Sales | Fragrance Catalogue | UK',objective='OUTCOME_SALES',
        status='PAUSED',special_ad_categories=[],is_adset_budget_sharing_enabled='false',
        promoted_object={'product_catalog_id':CAT})['id']
ads=out.setdefault('ads',{})
LAY=[{'layer_type':'image','image_source':'catalog'},
     {'layer_type':'frame_overlay','frame_source':'custom','frame_image_hash':FRAME,'opacity':100,
      'overlay_position':'center','scale':100,'blending_mode':'normal'}]
T={'geo_locations':{'countries':['GB'],'location_types':['home','recent']},'age_min':25,'age_max':55,
   'targeting_automation':{'advantage_audience':0},'publisher_platforms':['facebook','instagram'],
   'facebook_positions':['feed','story','profile_feed'],
   'instagram_positions':['stream','story','reels','explore_home','profile_feed'],'device_platforms':['mobile','desktop']}
for b,h,msg in BRANDS:
    e=ads.setdefault(b,{'product_set':sets[b]})
    if 'ad' in e: continue
    slug=h.replace('-','_')
    if 'adset' not in e:
        e['adset']=call('POST',f'{ACT}/adsets',name=f'{b} | Catalogue UK 25-55 | Purchase',campaign_id=out['campaign'],
            status='PAUSED',billing_event='IMPRESSIONS',optimization_goal='OFFSITE_CONVERSIONS',
            promoted_object={'product_set_id':sets[b],'custom_event_type':'PURCHASE'},
            attribution_spec=[{'event_type':'CLICK_THROUGH','window_days':7},{'event_type':'VIEW_THROUGH','window_days':1}],
            targeting=T)['id']
        json.dump(out,open(F,'w'),indent=1)
    if 'creative' not in e: e['creative']=call('POST',f'{ACT}/adcreatives',name=f'SW Catalogue | {b} | emerald frame',product_set_id=sets[b],
        object_story_spec={'page_id':PAGE,'instagram_user_id':IG,'template_data':{
            'message':msg+TAIL,'link':f'https://www.swansura.com/collections/{h}','name':'{{product.name}}',
            'description':'{{product.price}}','call_to_action':{'type':'SHOP_NOW'},'multi_share_end_card':False,
            'image_layer_specs':LAY}},
        url_tags=f'utm_source=facebook&utm_medium=paid_social&utm_campaign=fragrance_catalogue&utm_content={slug}')['id']
    e['ad']=call('POST',f'{ACT}/ads',name=f'{b} | Catalogue carousel | Emerald frame',adset_id=e['adset'],status='PAUSED',
        creative={'creative_id':e['creative']},tracking_specs=[{'action.type':['offsite_conversion'],'fb_pixel':[PIXEL]}])['id']
    json.dump(out,open(F,'w'),indent=1)
json.dump(out,open(F,'w'),indent=1)
