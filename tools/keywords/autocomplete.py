import json, sys, time, urllib.request, urllib.parse, re
KW, OUT = sys.argv[1], sys.argv[2]
d = json.load(open(KW))
seeds = {p['core'] for p in d['products']} | {'vilvah','deyga','vilvah uk','deyga uk','buy vilvah','buy deyga'} | {k['kw'] for k in d['keywords'] if k['kind']=='Brand / family' and k['kw'].endswith(' perfume')}
try: res = json.load(open(OUT))
except Exception: res = {}
for i, q in enumerate(sorted(seeds)):
    if q in res: continue
    url = 'https://suggestqueries.google.com/complete/search?' + urllib.parse.urlencode({'client':'firefox','gl':'uk','hl':'en-GB','q':q})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'}), timeout=15) as r:
                res[q] = json.loads(r.read().decode('utf-8','replace'))[1]; break
        except Exception as e:
            time.sleep(3*(attempt+1)); res[q] = []
    if i % 25 == 0: json.dump(res, open(OUT,'w'), ensure_ascii=False); print(i, len(seeds), flush=True)
    time.sleep(0.35)
json.dump(res, open(OUT,'w'), ensure_ascii=False, indent=0); print('done', len(res))
