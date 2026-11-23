# 23 Nov 2026 (user: 'Go with a and b'): (a) ad links go straight to the product/collection page instead of
# /discount/VD10?redirect=… (the redirect added ~1–1.5 s before the page started loading; the bag already offers VD10).
# Applies to the Vilvah, Engagement and Retargeting ads Claude built (the user's own Deyga creatives are left alone).
# Each creative is copied with only the link changed (headline/text/thumbnail/UTMs kept) and swapped onto the same ad id.
import json,subprocess,urllib.parse,re,os
G='https://graph.facebook.com/v23.0';ACT='act_1614052623400872'
ADSETS={'120249456165350240':'Vilvah','120249382199750240':'Engagement','120249508225430240':'Retargeting'}
HERE=os.path.dirname(os.path.abspath(__file__));F=HERE+'/direct_links_2026-11-23.json'
out=json.load(open(F)) if os.path.exists(F) else {}
def run(*a): return json.JSONDecoder().raw_decode(subprocess.run(list(a),capture_output=True,text=True).stdout)[0]
R=re.compile(r'https://www\.swansura\.com/discount/VD10\?redirect=([^"&\s]+)')
fix=lambda s:R.sub(lambda m:'https://www.swansura.com'+urllib.parse.unquote(m.group(1)),s)
for s,lab in ADSETS.items():
    for a in run('curl','-sg',f'{G}/{s}/ads?fields=id,name,effective_status,creative{{id,name,url_tags,object_story_spec}}&limit=50')['data']:
        if a['id'] in out or a['effective_status'] in ('ARCHIVED','DELETED'): continue
        c=a['creative'];oss=c.get('object_story_spec')
        if not oss or not R.search(json.dumps(oss)): continue
        new=json.loads(fix(json.dumps(oss)))
        vd=new.get('video_data')
        if vd and vd.get('image_url') and vd.get('image_hash'): vd.pop('image_hash')
        new={k:new[k] for k in ('page_id','instagram_user_id','video_data','link_data') if k in new}
        cr=run('curl','-s','-X','POST',f'{G}/{ACT}/adcreatives','--data-urlencode',f"name={c.get('name','')} | direct link",
               '--data-urlencode','object_story_spec='+json.dumps(new),'--data-urlencode','url_tags='+(c.get('url_tags') or ''))
        if 'id' not in cr: print('ERR',a['name'],cr);continue
        r=run('curl','-s','-X','POST',f"{G}/{a['id']}",'--data-urlencode','creative='+json.dumps({'creative_id':cr['id']}))
        out[a['id']]={'set':lab,'name':a['name'],'old_creative':c['id'],'new_creative':cr['id'],'ok':r.get('success')}
        json.dump(out,open(F,'w'),indent=1);print(lab,'|',a['name'],'|',c['id'],'->',cr['id'],r)
