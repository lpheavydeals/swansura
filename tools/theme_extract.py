"""Write theme files from a saved Shopify theme-files GraphQL result into theme/. Prints the next cursor."""
import json, sys, os, base64
src, out = sys.argv[1], sys.argv[2]
d = json.load(open(src))['data']['theme']['files']
n = 0
for f in d['nodes']:
    path = os.path.join(out, f['filename']); os.makedirs(os.path.dirname(path), exist_ok=True)
    b = f['body'] or {}
    if 'content' in b: open(path, 'w', encoding='utf-8').write(b['content'])
    elif 'contentBase64' in b: open(path, 'wb').write(base64.b64decode(b['contentBase64']))
    else: open(path + '.url', 'w').write(b.get('url', '')); 
    n += 1
print(n, d['pageInfo']['hasNextPage'], d['pageInfo']['endCursor'])
