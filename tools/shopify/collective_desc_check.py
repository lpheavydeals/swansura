"""Check the Highborn London + anatomē description rewrites (10 Nov 2026) against the brief:
banned claim / wellbeing / testimonial / superlative words outside the product's own title, 90–230 words, allowed tags only,
no prices, one or more links and every link in the product's link_options, keyword in the first sentence when given.
argv[1] = facts json, argv[2..] = writer output files. Prints problems; exit 1 if any."""
import json, re, sys, html
F = {f['id']: f for f in json.load(open(sys.argv[1]))}
O = [o for p in sys.argv[2:] for o in json.load(open(p))]
BAN = re.compile(r"wrinkle|fine line|ageing|aging|age-defying|youthful|ageless|collagen|firm(?:ing|er)\b|lift(?:ing|s)?\b|tighten|plump|repair|rebuild|restor|renew|rejuven|\bheal|sooth|\bcalm|inflamm|microbial|bacteri|acne|blemish|\bspots?\b|\bpores?\b|sebum|oil control|brighten|pigment|dark circle|puff|radian|\bglow(?:ing)?\b|boost|clinical|proven|guarantee|eczema|"
                 r"helps? you sleep|deeper sleep|restful|better sleep|quiet(?:s|en)? (?:the|your) mind|anxi|stress|overstimulat|\bmood|wellbeing|well-being|endurance|clarity|confidence|aromachology|science of scent|"
                 r"best-selling|bestselling|\bbest\b|most luxurious|ultimate|subscribe|customer|review|£", re.I)
TAGS = {'p', 'h3', 'ul', 'li', 'a', 'strong', 'em', 'br'}
bad = 0
assert len(O) == len(F), (len(O), len(F))
for o in O:
    f = F[o['id']]; h = o['html']; errs = []
    text = html.unescape(re.sub('<[^>]+>', ' ', h)); words = len(text.split())
    if not 90 <= words <= 230: errs.append(f'{words} words')
    tags = set(re.findall(r'</?([a-z0-9]+)', h)) - TAGS
    if tags: errs.append(f'tags {tags}')
    if re.search(r'style=|<h[12]', h): errs.append('style/h1/h2')
    ttl = f['title'].lower()
    for m in BAN.finditer(text):
        w = m.group(0).lower()
        if w in ttl and text.lower().count(w) <= ttl.count(w) + 0 and w not in ('£', 'best'):  # the product's own name, used once
            continue
        ctx = text[max(0, m.start() - 40):m.end() + 30].replace('\n', ' ')
        errs.append(f'banned "{m.group(0)}" …{ctx}…')
    links = re.findall(r'href="([^"]+)"', h)
    ok = {'/products/' + l['handle'] for l in f['link_options']}
    if not links: errs.append('no link')
    for l in links:
        if l not in ok: errs.append(f'link not allowed {l}')
    if f.get('keyword'):
        first = re.split(r'(?<=[.!?])\s', text.strip(), 1)[0].lower()
        if f['keyword'] not in first: errs.append(f'keyword "{f["keyword"]}" not in first sentence')
    if errs:
        bad += 1; print('##', f['title'][:70]); [print('  -', e) for e in errs]
print(len(O), 'checked,', bad, 'with problems')
sys.exit(1 if bad else 0)
