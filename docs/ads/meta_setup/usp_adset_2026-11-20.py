# 20 Nov 2026 (user): new ad set 'Vilvah Deyga USP' in the Sales campaign, same targeting as the Kits Purchase ad set
# (women 21-50, 243 postcode sectors, 5 interests, same placements, Advantage+ audience off), PURCHASE, PAUSED.
# 3 image ads (USP 1, 2, 4; 4x5 feeds / 9x16 stories+reels / 1x1 default) -> natural-skincare (only Vilvah + Deyga) with VD10 auto-applied.
import json,subprocess,os
HERE=os.path.dirname(os.path.abspath(__file__));D=HERE+'/../usp_2026-11-18'
G='https://graph.facebook.com/v23.0';ACT='act_1614052623400872';CAMP='120249389743960240';SRC='120249456165350240'
URL='https://www.swansura.com/discount/VD10?redirect=%2Fcollections%2Fnatural-skincare'
P='Official UK partner of Vilvah & Deyga · Free UK delivery over £40.'
ADS=[('1','Vilvah Deyga USP | Next-day, no import | Image',
  "Vilvah & Deyga, shipped from our UK stock. 🌿\n\nNext-day UK delivery, no customs or import fees, and VAT already in the price. Use code VD10 for an extra 10% off Vilvah and Deyga.\n\n"+P,
  'Extra 10% off with code VD10','Next-day UK delivery'),
 ('2','Vilvah Deyga USP | Skip the overseas delay | Image',
  "Skip the overseas wait and the import charges. 📦\n\nGenuine Vilvah & Deyga from our UK stock: next-day delivery available, prices include VAT, nothing extra to pay at your door. Extra 10% off with code VD10.\n\n"+P,
  'Vilvah & Deyga, from UK stock','10% off with code VD10'),
 ('4','Vilvah Deyga USP | Next-day price list | Image',
  "Better Ageing Serum, Milk Body Lotion, Chocolate Body Butter, Rice Water Shampoo and more from Vilvah & Deyga, with next-day UK delivery. ✨\n\nPrices include VAT, no customs charges. Extra 10% off Vilvah and Deyga with code VD10.\n\n"+P,
  'Vilvah & Deyga with next-day delivery','Extra 10% off with code VD10')]
def run(*a): return subprocess.run(list(a),capture_output=True,text=True).stdout
def jd(t): return json.JSONDecoder().raw_decode(t)[0]
F=HERE+'/usp_adset_2026-11-20.json';out=json.load(open(F)) if os.path.exists(F) else {}
if 'adset' not in out:
    src=jd(run('curl','-s',f'{G}/{SRC}?fields=targeting,attribution_spec,promoted_object'))
    a=jd(run('curl','-s','-X','POST',f'{G}/{ACT}/adsets','-F','name=Vilvah Deyga USP W21-50 | Purchase','-F',f'campaign_id={CAMP}','-F','daily_budget=500',
      '-F','billing_event=IMPRESSIONS','-F','optimization_goal=OFFSITE_CONVERSIONS','-F','bid_strategy=LOWEST_COST_WITHOUT_CAP',
      '-F','promoted_object='+json.dumps({"pixel_id":"1593636862064099","custom_event_type":"PURCHASE"}),
      '-F','attribution_spec='+json.dumps(src['attribution_spec']),'-F','targeting='+json.dumps(src['targeting']),'-F','status=PAUSED'))
    if 'id' not in a: print(a);raise SystemExit
    out['adset']=a['id'];json.dump(out,open(F,'w'),indent=1)
print('adset',out['adset'])
for n,nm,body,hl,ds in ADS:
    o=out.setdefault(n,{})
    if 'hashes' not in o:
        o['hashes']={z:list(jd(run('curl','-s','-X','POST',f'{G}/{ACT}/adimages','-F',f'filename=@{D}/USP_{n}_{z}.jpg'))['images'].values())[0]['hash'] for z in ('4x5','1x1','9x16')}
    afs={"images":[{"hash":o['hashes']['4x5'],"adlabels":[{"name":"i45"}]},{"hash":o['hashes']['9x16'],"adlabels":[{"name":"i916"}]},{"hash":o['hashes']['1x1'],"adlabels":[{"name":"i11"}]}],
      "bodies":[{"text":body}],"titles":[{"text":hl}],"descriptions":[{"text":ds}],"link_urls":[{"website_url":URL,"display_url":"swansura.com"}],
      "call_to_action_types":["SHOP_NOW"],"ad_formats":["SINGLE_IMAGE"],"optimization_type":"PLACEMENT",
      "asset_customization_rules":[
       {"customization_spec":{"publisher_platforms":["facebook","instagram"],"facebook_positions":["feed","marketplace","profile_feed","search"],"instagram_positions":["stream","explore_home","profile_feed"]},"image_label":{"name":"i45"},"priority":1},
       {"customization_spec":{"publisher_platforms":["facebook","instagram"],"facebook_positions":["story","facebook_reels"],"instagram_positions":["story","reels"]},"image_label":{"name":"i916"},"priority":2},
       {"customization_spec":{},"image_label":{"name":"i11"},"priority":3}]}
    if 'creative' not in o:
        c=jd(run('curl','-s','-X','POST',f'{G}/{ACT}/adcreatives','-F',f'name=SW Sales | USP {n} | 20 Nov','-F','asset_feed_spec='+json.dumps(afs),
          '-F','object_story_spec='+json.dumps({"page_id":"788176181050418","instagram_user_id":"17841477741370196"}),
          '-F','url_tags=utm_source=meta&utm_medium=paid_social&utm_campaign={{campaign.name}}&utm_content={{ad.name}}'))
        if 'id' not in c: print(n,c);break
        o['creative']=c['id']
    if 'ad' not in o:
        a=jd(run('curl','-s','-X','POST',f'{G}/{ACT}/ads','-F',f'name={nm}','-F',f'adset_id={out["adset"]}','-F','creative='+json.dumps({"creative_id":o['creative']}),'-F','status=PAUSED'))
        if 'id' not in a: print(n,a);break
        o['ad']=a['id']
    print(n,o['creative'],o['ad'],flush=True);json.dump(out,open(F,'w'),indent=1)
