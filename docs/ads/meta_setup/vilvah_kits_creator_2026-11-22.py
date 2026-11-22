# 22 Nov 2026 (user): the 5 Vilvah videos the user uploaded to the ad library are made into plain single-video ads,
# PAUSED, in the Vilvah kits ad set 'Kits W21-50 | Purchase' (120249456165350240); headline = next-day delivery USP,
# links via /discount/VD10?redirect=… . Then (`delete`) every other ad in that ad set is deleted (before-state saved).
# The videos are used as uploaded (user: no edits); they still carry Vilvah's own claims / '20% OFF' / 'comment for link'.
import json,subprocess,os,sys,time,urllib.parse
HERE=os.path.dirname(os.path.abspath(__file__))
G='https://graph.facebook.com/v23.0';ACT='act_1614052623400872';ADSET='120249456165350240'
L=lambda p:'https://www.swansura.com/discount/VD10?redirect='+urllib.parse.quote(p,safe='')
P='Official UK partner of Vilvah · Free UK delivery over £40.'
AMPM='/products/vilvah-am-pm-serum-kit'
FBK='/products/vilvah-face-brightening-kit-milk-powder-face-wash-milk-drops-brightening-serum-duo-milky-cleanse-radiance-boost-evens-skin-tone-fades-dark-spots'
GMS='/products/vilvah-goat-milk-shampoo-250ml'
AMPM_T=("Vilvah's AM PM Serum Kit, shipped from our UK stock 🌿 Milk Drops serum for the morning, Better Ageing Serum for the evening.\n\n"
        "Next-day UK delivery, no customs or import fees, VAT included. Extra 10% off Vilvah with code VD10.\n\n"+P)
FBK_T=("Vilvah's Face Brightening Kit, shipped from our UK stock ✨ Milk Powder Face Wash, then a few drops of Milk Drops serum.\n\n"
       "Next-day UK delivery, no customs or import fees, VAT included. Extra 10% off Vilvah with code VD10.\n\n"+P)
GMS_T=("Vilvah Goat Milk Shampoo, shipped from our UK stock 🥛 A creamy goat milk shampoo for regular use.\n\n"
       "Next-day UK delivery, no customs or import fees, VAT included. Extra 10% off Vilvah with code VD10.\n\n"+P)
ADS=[('990666766968753','Vilvah AM PM Serum Kit | Creator 1',AMPM,AMPM_T,'Next-day UK delivery · £46.99'),
     ('1490945759637105','Vilvah AM PM Serum Kit | Creator 2',AMPM,AMPM_T,'Next-day UK delivery · £46.99'),
     ('1883744626141972','Vilvah Face Brightening Kit | Creator 1',FBK,FBK_T,'Next-day UK delivery · £31.99'),
     ('1643892144100116','Vilvah Face Brightening Kit | Creator 2',FBK,FBK_T,'Next-day UK delivery · £31.99'),
     ('1606193371308107','Vilvah Goat Milk Shampoo | Creator',GMS,GMS_T,'Next-day UK delivery · £15.99')]
def run(*a): return subprocess.run(list(a),capture_output=True,text=True).stdout
def jd(t): return json.JSONDecoder().raw_decode(t)[0]
F=HERE+'/vilvah_kits_creator_2026-11-22.json';out=json.load(open(F)) if os.path.exists(F) else {}
def save(): json.dump(out,open(F,'w'),indent=1)

if len(sys.argv)>1 and sys.argv[1]=='delete':
    keep={out[v]['ad'] for v,*_ in ADS}
    ads=jd(run('curl','-sg',f'{G}/{ADSET}/ads?fields=id,name,effective_status,creative{{id}}&limit=200'))['data']
    out.setdefault('deleted_before',[a for a in ads if a['id'] not in keep]);save()
    for a in ads:
        if a['id'] in keep: continue
        r=jd(run('curl','-s','-X','DELETE',f"{G}/{a['id']}"));print('delete',a['id'],a['name'],r)
    raise SystemExit

for vid,nm,path,body,hl in ADS:
    o=out.setdefault(vid,{})
    if 'thumb' not in o:
        th=jd(run('curl','-sg',f'{G}/{vid}/thumbnails?fields=uri,is_preferred'))['data']
        o['thumb_url']=(next((t for t in th if t.get('is_preferred')),th[0]))['uri'];save()
    if 'creative' not in o:
        vd={"video_id":vid,"image_url":o['thumb_url'],"message":body,"title":hl,"link_description":"Extra 10% off Vilvah with code VD10",
            "call_to_action":{"type":"SHOP_NOW","value":{"link":L(path),"link_caption":"swansura.com"}}}
        c=jd(run('curl','-s','-X','POST',f'{G}/{ACT}/adcreatives','--data-urlencode',f'name=SW Kits | {nm} | 22 Nov',
           '--data-urlencode','object_story_spec='+json.dumps({"page_id":"788176181050418","instagram_user_id":"17841477741370196","video_data":vd}),
           '--data-urlencode','url_tags=utm_source=meta&utm_medium=paid_social&utm_campaign={{campaign.name}}&utm_content={{ad.name}}'))
        if 'id' not in c: print(nm,c);continue
        o['creative']=c['id'];save()
    if 'ad' not in o:
        a=jd(run('curl','-s','-X','POST',f'{G}/{ACT}/ads','--data-urlencode',f'name={nm}','-d',f'adset_id={ADSET}',
           '--data-urlencode','creative='+json.dumps({"creative_id":o['creative']}),'-d','status=PAUSED',
           '--data-urlencode','tracking_specs='+json.dumps([{"action.type":["offsite_conversion"],"fb_pixel":["1593636862064099"]}])))
        if 'id' not in a: print(nm,a);continue
        o['ad']=a['id'];save()
    print(nm,o['creative'],o['ad'],flush=True)
