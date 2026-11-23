# 23 Nov 2026 (user: 'Go with a and b'): (b) drop Facebook Marketplace + Facebook Reels placements from the
# Vilvah, Deyga and Retargeting ad sets (Reels 7 clicks -> 1 visit, Marketplace 5 -> 0 lifetime). Before-state kept = undo.
import json,subprocess,os
G='https://graph.facebook.com/v23.0'
SETS=['120249456165350240','120249456165580240','120249508225430240']
F=os.path.dirname(os.path.abspath(__file__))+'/no_reels_marketplace_2026-11-23.json'
out=json.load(open(F)) if os.path.exists(F) else {}
def run(*a): return json.loads(subprocess.run(list(a),capture_output=True,text=True).stdout)
for s in SETS:
    a=run('curl','-s',f'{G}/{s}?fields=name,targeting')
    t=a['targeting']; out.setdefault(s,{'name':a['name'],'before':json.loads(json.dumps(t))})
    fp=t.get('facebook_positions',[])
    t['facebook_positions']=[p for p in fp if p not in ('marketplace','facebook_reels')]
    if t['facebook_positions']==fp: print(a['name'],'already clean',fp);continue
    r=run('curl','-s','-X','POST',f'{G}/{s}','--data-urlencode','targeting='+json.dumps(t))
    out[s]['after']=t['facebook_positions'];out[s]['result']=r
    print(a['name'],fp,'->',t['facebook_positions'],r)
json.dump(out,open(F,'w'),indent=1)
