import docx, json, re, sys
d = docx.Document(sys.argv[1])
L = [(ln.strip(), any(r.bold for r in p.runs if r.text.strip()), p.style.name) for p in d.paragraphs for ln in p.text.split('\n') if ln.strip()]
SECT = {'cleanser','toner','serum','moisturiser','kit','hair care','lip care','body care','mask','soap'}
items = []; cur = None; mode = None; sect = None
def is_prod(t, b, st):
    return b and st == 'Normal' and len(t) < 130 and not re.match(r'(?i)^(benefits|ingredients)\b', t) and not re.match(r'^[^:]{2,40}:\s', t) and t.lower() not in SECT
for t, b, st in L:
    tl = t.lower().rstrip(':')
    if b and tl in SECT: sect = t; mode = None; continue
    if mode == 'ing' and not b and st == 'Normal' and t.count(',') >= 1 and cur and not cur['inci']: cur['inci'] = t; continue
    if is_prod(t, b, st):
        cur = {'name': t, 'sect': sect, 'inci': '', 'legend': '', 'key': []}; items.append(cur); mode = 'desc'; continue
    if cur is None: continue
    if re.match(r'(?i)^ingredients\b', t):
        mode = 'ing'; rest = re.sub(r'(?i)^ingredients\s*:?\s*', '', t)
        if rest: cur['inci'] += rest
        continue
    if re.match(r'(?i)^benefits', t): mode = 'ben'; continue
    if mode == 'ing':
        if t.startswith('*') and t.count(',') < 2 and re.search(r'(?i)organic|derived|grown|certified', t): cur['legend'] += ' ' + t; continue
        if re.match(r'(?i)^in\b', t) and t.count(',') < 2: continue
        m = re.match(r'^([^:,]{2,40}):\s*(.+)$', t)
        if m and t.count(',') < 3: cur['key'].append([m.group(1).strip(), m.group(2).strip()]); continue
        if t.count(',') >= 1 or len(t) < 60: cur['inci'] += (', ' if cur['inci'] else '') + t
print(len(items), sum(1 for i in items if i['inci']), sum(1 for i in items if i['key']))
json.dump(items, open(sys.argv[2], 'w'), ensure_ascii=False, indent=1)
for i in items: print(f"{i['sect'][:9]:9} | {i['name'][:60]:60} | inci {len(i['inci'])} | key {len(i['key'])} | {i['legend'][:30]}")
