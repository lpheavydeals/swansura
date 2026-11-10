"""Replace supplier claim text in custom.pdp.ben (benefit line under the price) and
custom.sw.a[0] (first PDP FAQ answer) on Highborn London / anatomē products with the
opening sentence of the claim-free description (10 Nov 2026).

Usage: python3 collective_benefit_lines_2026-11-10.py <admin read: products{id handle sw pdp}> <focus travel body_html file>
Writes docs/seo/collective_benefit_lines_2026-11-10.json (before/after per product = undo).
"""
import json, re, html, sys
import importlib.util
ROOT = __file__.rsplit('/tools/', 1)[0]
spec = importlib.util.spec_from_file_location('ct', ROOT + '/tools/shopify/claim_titles_2026-11-10.py')
REP = None
src = open(ROOT + '/tools/shopify/claim_titles_2026-11-10.py').read()
REP = eval(src[src.index('REP = [') + 6: src.index(']\ndef rep') + 1])
def rep(s):
    for a, b in REP: s = s.replace(html.unescape(a), html.unescape(b))
    return s
desc = {x['id']: x['html'] for x in json.load(open(ROOT + '/docs/seo/collective_descriptions_2026-11-10.json'))}
for x in json.load(open(ROOT + '/docs/seo/claim_titles_2026-11-10.json'))['products']:
    desc[x['id']] = x['after']['html']
nodes = json.load(open(sys.argv[1]))['data']['products']['nodes']
focus = open(sys.argv[2]).read()
C = re.compile(r"wrinkle|fine line|collagen|firm|acne|pore|heal|sooth|calm|brighten|anti-?age|ageing|age-? ?defying|youthful|repair|restor|rejuven|plump|deeper sleep|stress|clarity|focus|endurance|overactive|relax|mind|redness|irritat|protect|energis|invigorat|harmony|breathing|tranquil", re.I)
def first(h):
    p = re.search(r'<p>(.*?)</p>', h, re.S).group(1)
    t = rep(html.unescape(re.sub('<[^>]+>', '', p)).strip())
    s = re.split(r'(?<=[.!?])\s+(?=[A-Z])', t)
    out = s[0]
    if len(out) < 70 and len(s) > 1: out += ' ' + s[1]
    return out
out = []
for p in nodes:
    sw = json.loads(p['sw']['value']) if p['sw'] else None
    pd = json.loads(p['pdp']['value']) if p['pdp'] else None
    hit_a = bool(sw and sw.get('a') and C.search(sw['a'][0]))
    hit_b = bool(pd and pd.get('ben') and C.search(pd['ben']))
    ben0 = (pd or {}).get('ben') or ''
    a0 = (sw or {}).get('a', [''])[0] if sw and sw.get('a') else ''
    stem = ben0.rstrip('.…')[:60]
    if hit_a and stem and a0.startswith(stem): hit_b = True   # ben is a cut-down copy of the claim answer
    if hit_b and stem and a0.startswith(stem): hit_a = True
    if not (hit_a or hit_b): continue
    h = focus if p['handle'] == 'focus-eau-de-parfum-travel-10ml' else desc[p['id']]
    n = first(h)
    left = [w for w in C.findall(n) if w.lower() != 'focus']  # Focus = product name
    assert not left, (p['handle'], n, left)
    sw2, pd2 = dict(sw), dict(pd)
    if hit_a: sw2['a'] = [n] + sw['a'][1:]
    if hit_b: pd2['ben'] = n
    if sw2 == sw: sw2 = None
    if pd2 == pd: pd2 = None
    out.append(dict(id=p['id'], handle=p['handle'], before=dict(sw=p['sw']['value'], pdp=p['pdp']['value']),
                    after=dict(sw=sw2 and json.dumps(sw2, ensure_ascii=False), pdp=pd2 and json.dumps(pd2, ensure_ascii=False)), line=n))
json.dump(out, open(ROOT + '/docs/seo/collective_benefit_lines_2026-11-10.json', 'w'), ensure_ascii=False, indent=1)
print(len(out))
for o in out: print(o['handle'][:45], '|', o['line'])
