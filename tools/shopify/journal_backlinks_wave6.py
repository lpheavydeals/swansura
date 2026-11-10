"""Back-links to the 4 guides of 9-10 Nov 2026 (best-perfume-gift-sets-uk-2026, stocking-fillers-for-her-under-25,
goat-milk-soap-guide, indian-skincare-uk-guide) + cross-links between them (user, 10 Nov 2026: 'Published all four,
add the back-links'). One short sentence or clause per anchor, nothing else changed; every anchor must occur once.

Input: JSON {key: current stored text}; key = article handle, or 'col:<handle>' for a collection's custom.seo_copy.
Build it from the Admin (article.body / metafield value) right before applying, so 'before' is the exact stored text.
Output: docs/seo/journal_backlinks_wave6_2026-11-10.json ({key: {id, before, after}} = update + undo list).
DO NOT APPLY until all 4 guides are published (isPublished true, pages 200): on 10 Nov they were still unpublished.

Usage: python3 tools/shopify/journal_backlinks_wave6.py <current.json>
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
PG = '<a href="/blogs/journal/best-perfume-gift-sets-uk-2026">'
SF = '<a href="/blogs/journal/stocking-fillers-for-her-under-25">'
GM = '<a href="/blogs/journal/goat-milk-soap-guide">'
IN = '<a href="/blogs/journal/indian-skincare-uk-guide">'

EDITS = {
    # published articles -> new guides
    "christmas-gift-guide": ("gid://shopify/Article/1005324665219", [
        ('<a href="/collections/perfume-gift-sets">perfume gift sets</a>.</p>\n<h2>Perfume gift sets for him</h2>',
         f'<a href="/collections/perfume-gift-sets">perfume gift sets</a>, or read our {PG}perfume gift sets guide</a>.</p>\n<h2>Perfume gift sets for him</h2>'),
        ('<h2>Stocking fillers under £25</h2>\n<ul>',
         f'<h2>Stocking fillers under £25</h2>\n<p>More small gifts in our {SF}stocking fillers for her guide</a>.</p>\n<ul>'),
    ]),
    "how-to-use-lip-scrub": ("gid://shopify/Article/1005468221827", [
        ('For more small gifts, see our <a href="/blogs/journal/christmas-gift-guide">Christmas gift guide</a>.</p>',
         f'For more small gifts, see our <a href="/blogs/journal/christmas-gift-guide">Christmas gift guide</a> or {SF}stocking fillers for her under £25</a>.</p>'),
    ]),
    "natural-shampoo-guide": ("gid://shopify/Article/1005503283587", [
        ('Vilvah makes it for dry, frizzy or chemically treated hair.</li>',
         f'Vilvah makes it for dry, frizzy or chemically treated hair. Our {GM}goat milk soap guide</a> covers Vilvah’s other goat milk products.</li>'),
    ]),
    "deyga-or-vilvah": ("gid://shopify/Article/1005307822467", [
        ('Here is how to tell which one suits your skin, and where to start.</p>',
         f'Here is how to tell which one suits your skin, and where to start. For the ingredients behind both, read our {IN}Indian skincare guide</a>.</p>'),
    ]),
    "hair-oil-guide": ("gid://shopify/Article/1005324861827", [
        ('the dried fruit is steeped in a base oil such as coconut.</li>',
         f'the dried fruit is steeped in a base oil such as coconut. Our {IN}Indian skincare guide</a> covers amla and other Indian ingredients.</li>'),
    ]),
    # the 4 new guides, cross-links
    "best-perfume-gift-sets-uk-2026": ("gid://shopify/Article/1005550928259", [
        ('or our <a href="/blogs/journal/christmas-gift-guide">Christmas gift guide</a> for skincare and stocking fillers too.</p>',
         f'or our <a href="/blogs/journal/christmas-gift-guide">Christmas gift guide</a> for skincare too. For small gifts, read {SF}stocking fillers for her under £25</a>.</p>'),
    ]),
    "stocking-fillers-for-her-under-25": ("gid://shopify/Article/1005550993795", [
        ('see them all in <a href="/collections/goat-milk-soap">goat milk soap</a>.',
         f'see them all in <a href="/collections/goat-milk-soap">goat milk soap</a>, or read our {GM}goat milk soap guide</a>.'),
    ]),
    "goat-milk-soap-guide": ("gid://shopify/Article/1005551059331", [
        ('see our <a href="/collections/stocking-fillers">stocking fillers</a>.</li>',
         f'see our <a href="/collections/stocking-fillers">stocking fillers</a> and {SF}stocking fillers guide</a>.</li>'),
    ]),
    "indian-skincare-uk-guide": ("gid://shopify/Article/1005560562051", [
        ('(see <a href="/collections/goat-milk-soap">goat milk soap</a>).',
         f'(see our {GM}goat milk soap guide</a>).'),
    ]),
    # collection copy
    "col:goat-milk-soap": ("gid://shopify/Collection/714711892355", [
        ('Patch test before first use.</p>',
         f'Patch test before first use. Our {GM}goat milk soap guide</a> explains how to choose and use a bar.</p>'),
    ]),
    "col:range-goat-milk": ("gid://shopify/Collection/714071441795", [
        ('(see <a href="/collections/goat-milk-soap">goat milk soap</a>).',
         f'(see <a href="/collections/goat-milk-soap">goat milk soap</a> and our {GM}goat milk soap guide</a>).'),
    ]),
}

cur = json.load(open(sys.argv[1]))
out = {}
for k, (gid, edits) in EDITS.items():
    before = cur[k]
    after = before
    for old, new in edits:
        assert after.count(old) == 1, (k, old, after.count(old))
        after = after.replace(old, new)
    out[k] = {"id": gid, "before": before, "after": after}
    print(k, len(before), "->", len(after))
json.dump(out, open(ROOT / "docs/seo/journal_backlinks_wave6_2026-11-10.json", "w"), ensure_ascii=False, indent=1)
