# Catalogue ad frames (24 Nov 2026)

Transparent 1080x1080 frames laid over Meta catalogue product photos (white 1:1, bottle in the middle).
Band at the top (the bottles reach almost to the bottom edge of the catalogue photos).

- `frame_emerald.png` – emerald border + band, white logo, gold text. Ad image hash 52ec2ca6493e95062dd7e0511d58fcc2
- `frame_white.png` – white border, brass hairline, ivory band, brown logo. Ad image hash c45347a43bcf8404ffe1fe1ea4c0e8c8
- Rebuild: `node build.js` (fonts/logos from ../fragrance_2026-11-22/src/)

Applied through the creative's `template_data.image_layer_specs`:
`[{layer_type:image, image_source:catalog}, {layer_type:frame_overlay, frame_source:custom, frame_image_hash:<hash>, opacity:100, overlay_position:center, scale:100, blending_mode:normal}]`
(blending_mode is required). Facebook feed previews show the frame; Meta's Instagram feed preview did not.
