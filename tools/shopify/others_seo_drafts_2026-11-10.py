"""SEO drafts for the top 15 'Others' products by Semrush volume (user, 10 Nov 2026: 'Go ahead and draft them for the
top 15'). Puts the busier general search term (peptide serum, pillow spray, bakuchiol serum …) into the SEO title,
meta description and custom.h1. Coach Green Shower Gel (#12) is skipped: 'coach green' 480 most likely means the
Coach Green perfume; #16 Ultimate Day & Night Moisture Set takes its place.
Facts only from the product's own description and variants; no skin, sleep or mood claims (ASA).
argv[1] = Admin read of the 15 ({data:{pN:{id,handle,title,seo,h1,variants}}}). Writes
docs/seo/others_seo_drafts_2026-11-10.{json,md} (before/after per product = undo once written).
"""
import json, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
A = {p['handle']: p for p in json.load(open(sys.argv[1]))['data'].values()}
D = [  # handle, keyword (UK/mo), new H1 (None = keep), SEO title, meta description
 ('youthboost-anti-ageing-peptide-serum', 'peptide serum (4,400)', None,
  'Peptide Serum: Highborn London YOUTHBOOST | Swansura',
  'Highborn London YOUTHBOOST peptide serum with Matrixyl 3000, Argireline and copper peptides. Vegan, £94. 100% authentic, free UK delivery over £40.'),
 ('sleep-pillow-spray-roman-chamomile-28-botanical-extracts-anatome', 'pillow spray (2,400)', 'anatomē Roman Chamomile Sleep Pillow Spray',
  'Pillow Spray: anatomē Roman Chamomile | Swansura',
  'anatomē Roman Chamomile pillow spray with lavender, clary sage and 28 botanical extracts, to mist on pillows and linen. 30ml or 50ml, from £25.'),
 ('bakuchiol-youth-elixir', 'bakuchiol serum (2,400)', 'Highborn London Bakuchiol Serum: Youth Elixir',
  'Bakuchiol Serum: Highborn London Youth Elixir | Swansura',
  'Highborn London Bakuchiol Youth Elixir, a plant-based bakuchiol serum for day or night use, made in England. £99. Free UK delivery over £40.'),
 ('imperial-eye-gel', 'eye gel (1,300)', None,
  'Highborn London Imperial Eye Gel, 10ml to 30ml | Swansura',
  'A lightweight, cooling eye gel with glycerin, hyaluronic acid and argan oil, in 10ml, 15ml or 30ml jars. From £31, free UK delivery over £40.'),
 ('superior-lip-butter-large-50ml', 'lip butter (1,300)', 'Highborn London Superior Lip Butter 50ml',
  'Lip Butter: Highborn London Superior 50ml | Swansura',
  'Highborn London Superior Lip Butter in a large 50ml jar, a rich natural lip butter for soft, conditioned lips. £29, free UK delivery over £40.'),
 ('somali-frankincense-sleep-pillow-spray-overactive-mind-anatome', 'sleep pillow spray (1,300)', None,
  'Sleep Pillow Spray: anatomē Somali Frankincense | Swansura',
  'anatomē Somali Frankincense sleep pillow spray with lavender, clary sage and 28 botanical extracts, for pillows and linen. 30ml or 50ml, from £25.'),
 ('superior-lip-butter-15ml', 'lip butter (1,300)', 'Highborn London Superior Lip Butter 15ml',
  'Lip Butter: Highborn London Superior 15ml | Swansura',
  'Highborn London Superior Lip Butter in a 15ml jar, a natural lip butter to keep in your bag. £22.50, free UK delivery over £40.'),
 ('moistureburst-hydrating-glow-ceramide-serum', 'ceramide serum (1,000)', None,
  'Ceramide Serum: Highborn London MOISTUREBURST | Swansura',
  'Highborn London MOISTUREBURST, a lightweight hydrating ceramide serum to layer under moisturiser. Vegan, 30ml or 50ml, from £57.'),
 ('shiseido-ultimune-power-infusing-concentrate-face-serum-30ml-anti-aging-hydrating-serum', 'shiseido ultimune power infusing concentrate (720)', 'Shiseido Ultimune Power Infusing Concentrate 30ml',
  'Shiseido Ultimune Power Infusing Concentrate 30ml | Swansura',
  'Shiseido Ultimune Power Infusing Concentrate, a lightweight daily face serum, 30ml for £35.99. 100% authentic, free UK delivery over £40.'),
 ('the-gift-of-good-sleep-somali-frankincense', 'sleep gift set (720)', 'anatomē The Gift of Good Sleep: Somali Frankincense Sleep Gift Set',
  'Sleep Gift Set: anatomē The Gift of Good Sleep | Swansura',
  'anatomē sleep gift set: Somali Frankincense pillow spray and sleep oil, 50ml + 30ml, for a bedtime ritual. £68, free UK delivery over £40.'),
 ('natural-luminosity-scrub', 'natural body scrub (590)', 'Highborn London Natural Luminosity Body Scrub',
  'Natural Body Scrub: Highborn London Luminosity | Swansura',
  'Highborn London Natural Luminosity Scrub, a natural body scrub to exfoliate, in a large 220ml glass jar. Paraben and sulphate free, £50.'),
 ('24k-gold-hydrating-face-mask', 'gold face mask (480)', None,
  'Gold Face Mask: 24K Gold Hydrating Face Mask | Swansura',
  'A 24K gold face mask with hyaluronic acid, ceramides and shea butter for a hydrating treat. Swansura Selection, £34.99, free UK delivery over £40.'),
 ('illuminating-rose-hip-grape-seed-avocado-face-oil', 'rosehip face oil (480)', 'anatomē Rosehip Face Oil with Grape Seed & Avocado',
  'Rosehip Face Oil: anatomē Illuminating Face Oil | Swansura',
  'anatomē Illuminating rosehip face oil with grape seed, avocado, jojoba and mandarin oils, for evening use. 30ml, £52, free UK delivery over £40.'),
 ('bath-shower-oil-with-roman-chamomile-cornish-lavender', 'lavender bath oil (390)', 'anatomē Roman Chamomile & Cornish Lavender Bath Oil and Shower Oil',
  'Lavender Bath Oil: anatomē Bath & Shower Oil | Swansura',
  'anatomē lavender bath oil and shower oil with Roman Chamomile, jojoba, coconut and sunflower oils. 150ml, £68, free UK delivery over £40.'),
 ('ultimate-day-night-moisture-set', 'moisturiser gift set (390)', None,
  'Moisturiser Gift Set: Highborn Day & Night Set | Swansura',
  'Highborn London moisturiser gift set: Imperial Moisturiser and Night Elixir, both 50ml jars, made in England. £95, free UK delivery over £40.'),
]
out, md = [], ['# SEO drafts: top 15 Others products (10 Nov 2026)\n',
               'Coach Green Shower Gel left out: "coach green" (480/mo) most likely means the Coach Green perfume. #16 Ultimate Day & Night Moisture Set takes its place.\n']
for h, kw, h1, t, d in D:
    p = A[h]
    assert len(t) <= 60 and len(d) <= 150 and "'" not in d, (h, len(t), len(d))
    k = kw.split(' (')[0]
    hh = h1 or p['h1']['value']
    hits = [x for x, s in (('title', t), ('description', d), ('H1', hh)) if k in s.lower()]
    out.append(dict(id=p['id'], handle=h, keyword=kw, before=dict(seo_title=p['seo']['title'], seo_description=p['seo']['description'], h1=p['h1']['value']),
                    after=dict(seo_title=t, seo_description=d, h1=hh)))
    md += [f'## {p["title"]}\n', f'Keyword: **{kw}** · in: {", ".join(hits)} · https://www.swansura.com/products/{h}\n',
           f'- H1: {p["h1"]["value"]}' + (f'  →  **{h1}**' if h1 else ' (unchanged)'),
           f'- Title: {p["seo"]["title"]}  →  **{t}** ({len(t)})', f'- Description: {p["seo"]["description"]}', f'  → **{d}** ({len(d)})\n']
json.dump(out, open(ROOT / 'docs/seo/others_seo_drafts_2026-11-10.json', 'w'), ensure_ascii=False, indent=1)
open(ROOT / 'docs/seo/others_seo_drafts_2026-11-10.md', 'w').write('\n'.join(md))
for o in out: print(o['keyword'][:30].ljust(30), len(o['after']['seo_title']), len(o['after']['seo_description']))
