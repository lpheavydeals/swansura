import json,subprocess,sys
G="https://graph.facebook.com/v23.0"; ACT="act_1614052623400872"
def post(path,data):
    args=["curl","-sS","-X","POST",f"{G}/{path}"]
    for k,v in data.items():
        args+=["--data-urlencode",f"{k}={v if isinstance(v,str) else json.dumps(v)}"]
    r=json.loads(subprocess.run(args,capture_output=True,text=True).stdout)
    if "error" in r: print(path,json.dumps(r["error"],indent=1)); sys.exit(1)
    return r
out={}
camp=post(f"{ACT}/campaigns",{"name":"SW | Sales | Prospecting | UK","objective":"OUTCOME_SALES",
  "status":"PAUSED","special_ad_categories":[],"is_adset_budget_sharing_enabled":"false"})
out["campaign"]=camp["id"]
tgt={"geo_locations":{"countries":["GB"],"location_types":["home","recent"]},
 "age_min":20,"age_max":65,"age_range":[22,55],"genders":[2],
 "flexible_spec":[{"interests":[{"id":i} for i in ["6003157824284","6003423248519","6003494675627","6003875393160","6810084906985"]]}],
 "targeting_automation":{"advantage_audience":1}}
ads=post(f"{ACT}/adsets",{"name":"Adv+ W22-55 | Purchase","campaign_id":out["campaign"],"status":"PAUSED",
 "daily_budget":"1500","billing_event":"IMPRESSIONS","optimization_goal":"OFFSITE_CONVERSIONS",
 "bid_strategy":"LOWEST_COST_WITHOUT_CAP",
 "promoted_object":{"pixel_id":"1593636862064099","custom_event_type":"PURCHASE"},"targeting":tgt})
out["adset"]=ads["id"]
names={"Vilvah_AMPMSerumKit":"Vilvah AM PM Serum Kit","Vilvah_FaceBrighteningKitLarge":"Vilvah Face Brightening Kit Large",
 "Vilvah_MilkFaceKit":"Vilvah Milk Face Kit","Deyga_LipBalmStick":"Deyga Beetroot Lip Balm Stick",
 "Vilvah_FaceLiftKit":"Vilvah Face Lift Kit","Vilvah_MilkBodyKit":"Vilvah Milk Body Kit"}
sw=json.load(open("swap_tc.json")); out["ads"]={}
for k,n in names.items():
    a=post(f"{ACT}/ads",{"name":f"{n} | Video 4x5+9x16 | From home","adset_id":out["adset"],
      "creative":{"creative_id":sw[k]["creative"]},"status":"PAUSED"})
    out["ads"][k]=a["id"]; print(k,a["id"])
json.dump(out,open("sales.json","w"),indent=1); print(out)
