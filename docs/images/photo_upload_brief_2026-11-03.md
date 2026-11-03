# Photo upload brief (3 Nov 2026) — new products, client Drive folder

The user approved this work ("do everything"). Products are already LIVE (sold out) with no photos. You add photos only.
Tools: Shopify MCP (`ToolSearch "select:mcp__Shopify__graphql_mutation,mcp__Shopify__graphql_query"`), Read (views images), Bash.
Work only on the products in your batch file. Never delete products or touch other products. No medical/performance claims in alt text.

Batch file: JSON list of {handle, id (Shopify product gid), title, confidence, note, folder, images:[local webp paths, Drive order], sheet}.
`sheet` = contact sheet JPG with every image numbered (#1, #2 … = images[0], images[1] …).

For EACH product:
1. Read the `sheet` image (Read tool). Open single images (Read the .webp path) only when the sheet is unclear (box label, size, name).
2. Check the photos really show THIS product (brand + perfume name on bottle/box; for sets, the set). If the folder is the wrong product
   (common for confidence medium/low — see note), upload NOTHING for it and record status "wrong_folder" + what the photos show.
3. Choose the gallery: first = a clear shot of the bottle alone (or bottle + box) on a plain background; then the rest.
   Drop near-duplicates (same shot twice), images of a different product/size, screenshots with UI, blank/broken images.
   Keep lifestyle / ingredient / AI-styled shots of the right product (the store has used them before). Max 8 images.
4. Alt text per image, unique: "<product title> – <what the image shows>" (e.g. "Lattafa Khamrah Qahwa Eau de Parfum 100ml – bottle
   with coffee beans and dates"). Describe only what is visible. No claims ("long-lasting", "best"), no notes you can't see.
5. Copy chosen files in gallery order to /tmp/claude-0/-home-user-swansura/29c675fb-6e77-57c8-9687-33182e9bfb9b/scratchpad/up/<handle>/<handle>-01.webp, -02 … (exact names; they become Shopify file names).
6. Upload (do several products per round to save calls, e.g. 4–6 products):
   a. `python3 /home/user/swansura/tools/shopify/stage_images.py input <files…>` → JSON input.
   b. stagedUploadsCreate(input:$input){stagedTargets{url resourceUrl parameters{name value}} userErrors{field message}} with that input.
   c. `python3 /home/user/swansura/tools/shopify/stage_images.py post <same files…>` → finds the targets in your transcript, POSTs, prints resourceUrl + code (must be 201). If "no staged target found", wait 10 s and retry once (transcript flush).
   d. For each product: productUpdate(product:{id:<id>}, media:[{mediaContentType:IMAGE, originalSource:<resourceUrl>, alt:<alt>} … in gallery order]){product{id media(first:10){nodes{alt status}}} userErrors{field message}}. Alias several products in one mutation (variables $p0:ProductUpdateInput!, $m0:[CreateMediaInput!] …).
   e. Remove the 'Photo pending' tag: tagsRemove(id:<id>, tags:["Photo pending"]){userErrors{field message}} (aliased).
   Before uploading, query the product's media count: if it already has media, skip it (status "already_has_media") — never upload twice.
7. After all uploads, query your products' media (first:10){nodes{status alt}} and confirm every product you uploaded has >0 media and none with status FAILED (retry a FAILED one once).

Result file (path given in your prompt): JSON list of {handle, id, status: "uploaded"|"wrong_folder"|"no_usable_images"|"already_has_media"|"error",
n_uploaded, dropped:[{n, reason}], order:[image numbers in gallery order], alts:[…], note}. Also note anything the client should check
(e.g. box says a different size, AI-generated look, mismatched name).

Report back in under 15 lines: counts by status, wrong-folder products with what the photos showed, anything odd.
