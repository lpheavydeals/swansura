"""Journal guide 'Perfume gift sets under £30: what is in each box'
(user, 28 Nov 2026: 'Go ahead with the two guides', the next budget guides after oud under £60 / aftershave under £50).

Why: Christmas gift searches are budget searches ('perfume gift sets under £30', 'cheap perfume gift sets uk'),
and AI assistants answer them with short lists. Every set below was in stock and £30 or less on the storefront
on 28 Nov 2026. Facts = each product's own description (notes list, set contents). NO PRICES in the text (band only).

Usage: python3 tools/shopify/guide_gift_sets_under_30.py <storefront products dump dir>
Output: docs/seo/guide_gift_sets_under_30_2026-11-28.jsonl
"""
import glob
import json
import sys

from journal_lib import build

A = {
    "title": "Perfume gift sets under £30: what is in each box",
    "handle": "perfume-gift-sets-under-30",
    "tag": "Gift guide",
    "summary": "Boxed perfume gift sets for £30 or less, with what is in each box and the notes in each scent: sets for her, sets for him, and sets with several scents to try.",
    "mt": "Perfume Gift Sets Under £30: What Is in Each Box | Swansura",
    "md": "Perfume gift sets under £30 in the UK: Trussardi, Grès, Guess, Armaf, Korloff, Paco Rabanne, Jaguar and Franck Olivier sets, with contents and notes.",
    "pick": {
        "pj": "trussardi-pure-jasmine-lifestyle-mini-gift-set-eau-de-parfum-60ml-10ml-7ml",
        "rr": "trussardi-ruby-red-eau-de-parfum-gift-set-60ml-stardust-body-emulsion-125ml-women-s-fragrance-set",
        "gres": "gres-cabotine-rose-eau-de-toilette-body-lotion-gift-set-100ml-200ml",
        "bella": "franck-olivier-bella-women-eau-de-parfum-deodorant-gift-set-75ml-250ml",
        "armaf": "armaf-club-de-nuit-woman-eau-de-parfum-travel-set-2-x-12ml",
        "guess": "guess-seductive-eau-de-toilette-gift-set-seductive-noir-red-blue-4-x-15ml",
        "korloff": "korloff-paris-discovery-set-eau-de-parfum-3x10ml",
        "paco": "paco-rabanne-mens-miniature-eau-de-toilette-set-1-million-invictus-phantom-3-x-4ml",
        "jaguar": "jaguar-classic-eau-de-toilette-shower-gel-gift-set-100ml-200ml",
        "black": "franck-olivier-black-touch-eau-de-toilette-deodorant-gift-set-100ml-250ml",
    },
    "titles": {},
    "shop": ["pj", "rr", "gres", "guess", "armaf", "korloff", "paco", "jaguar"],
    "body": """<p><strong>A boxed perfume set makes a ready-to-give present, and it does not have to cost much.</strong> Every set below was £30 or less at Swansura at the time of writing. Most hold a full bottle plus a matching body lotion, shower gel, deodorant or travel spray; a few hold several small sprays, which is a good choice when you are not sure which scent they would like. We list what is in each box and the notes in each scent, so you can match the set to the person.</p>
<h2>How to choose a gift set</h2>
<ul>
<li><strong>You know their style:</strong> pick a set with a full bottle and a matching body product. The lotion or gel uses the same scent, so they can layer it.</li>
<li><strong>You are not sure:</strong> pick a set with several small sprays, so they can try more than one scent.</li>
<li><strong>For a bag or a trip:</strong> pick a travel set with small bottles.</li>
</ul>
<h2>Gift sets for her</h2>
<ul>
<li>[[pj|Trussardi Pure Jasmine Lifestyle Mini Gift Set]]: a 60ml eau de parfum plus 10ml and 7ml sprays of the same scent. Bergamot, pistachio and neroli, then jasmine and champaca, over vanilla, sandalwood and patchouli. Three sizes means one for home, one for the bag and one for travel.</li>
<li>[[rr|Trussardi Ruby Red Eau de Parfum Gift Set]]: a 60ml eau de parfum with a 125ml Stardust body emulsion. Citrus and fruit, then rose and jasmine, over amber, vanilla, musk and woods. Warm and polished, a good pick for evenings and the cooler months.</li>
<li>[[gres|Grès Cabotine Rose Gift Set]]: a 100ml eau de toilette with a 200ml perfumed body lotion. Cherry blossom, pear and green leaves, then peony and mimosa, over plumeria, sandalwood, vetiver and musk. Light and pretty for daytime.</li>
<li>[[bella|Franck Olivier Bella Women Gift Set]]: a 75ml eau de parfum with a 250ml deodorant. Lemon, lychee and raspberry, then lily and rose, over ambergris, vetiver, cedar and musk.</li>
<li>[[armaf|Armaf Club de Nuit Woman Travel Set]]: two 12ml sprays of the same eau de parfum. Bergamot, grapefruit, peach and orange, then geranium, jasmine, litchi and rose, over musk, patchouli, vanilla and vetiver. One spray for the handbag, one for home. Our <a href="/blogs/journal/armaf-club-de-nuit-guide">Armaf Club de Nuit guide</a> covers the whole line.</li>
</ul>
<h2>Sets with several scents to try</h2>
<ul>
<li>[[guess|Guess Seductive Gift Set]]: four 15ml eau de toilette sprays, Seductive, Seductive Noir, Seductive Red and Seductive Blue. Seductive is pear and jasmine over vanilla; Noir is iris and lily of the valley over white suede; Red is cherry and almond over tonka; Blue is citrus, cardamom and marine notes over cedarwood and musk.</li>
<li>[[korloff|Korloff Paris Discovery Set]]: three 10ml eau de parfum sprays. The brand describes Miss as fresh and fruity, Lady as floral and elegant, and Korlove as soft and warm.</li>
<li>[[paco|Paco Rabanne Men's Miniature Set]]: three 4ml eau de toilette minis, 1 Million, Invictus and Phantom. 1 Million is blood mandarin, cinnamon and leather; Invictus is sea notes, grapefruit and bay leaf; Phantom is lemon, lavender and apple over vanilla. Our <a href="/blogs/journal/paco-rabanne-perfume-guide">Paco Rabanne perfume guide</a> compares the full bottles.</li>
</ul>
<h2>Gift sets for him, or for anyone</h2>
<ul>
<li>[[jaguar|Jaguar Classic Gift Set]]: a 100ml eau de toilette with a 200ml shower gel. Basil, lavender, mandarin and bergamot, then lotus, orange blossom and ginger, over sandalwood, benzoin and white musk. Listed for men and women.</li>
<li>[[black|Franck Olivier Black Touch Gift Set]]: a 100ml eau de toilette with a 250ml deodorant. Cardamom, spices, bergamot and grapefruit, then orange blossom, jasmine and magnolia, over vetiver, patchouli, musk, vanilla and cedar. Also listed for men and women.</li>
</ul>
<p>For a bigger budget, our <a href="/blogs/journal/best-perfume-gift-sets-uk-2026">perfume gift sets guide</a> covers the designer sets, and our <a href="/blogs/journal/aftershave-under-50">aftershave under £50 guide</a> lists single bottles for him.</p>
<h2>Smaller gifts and stocking fillers</h2>
<p>A single miniature spray is a lighter present for a stocking. Our <a href="/blogs/journal/mini-perfume-sets-guide">mini perfume sets guide</a> lists what is inside each miniature set, and our <a href="/blogs/journal/stocking-fillers-for-her-under-25">stocking fillers for her guide</a> adds lip care and soaps.</p>
<h2>Delivery</h2>
<p>Browse every <a href="/collections/perfume-gift-sets">perfume gift set</a>, or see <a href="/collections/perfume-gift-sets-for-her">gift sets for her</a>, <a href="/collections/aftershave-gift-sets-for-him">aftershave gift sets for him</a> and <a href="/collections/gifts-under-50">gifts under £50</a>. All are 100% authentic and ship from the UK, with free UK delivery over £40, so two sets in one order usually ship free. Order early in December so gifts arrive in time; see our <a href="/policies/shipping-policy">shipping policy</a> for delivery options.</p>""",
    "faq": [
        ["What is a good perfume gift set under £30?",
         "For her, the Trussardi Pure Jasmine Lifestyle set (three sizes of one eau de parfum) or the Trussardi Ruby Red set with body emulsion. To try several scents, the Guess Seductive set of four 15ml sprays. For him, the Paco Rabanne miniature set or the Jaguar Classic set."],
        ["Which set is best if I do not know their perfume?",
         "A set with several scents: the Guess Seductive set (four scents), the Korloff Paris Discovery Set (three scents) or the Paco Rabanne men's miniature set (three scents)."],
        ["What is the difference between a body lotion set and a deodorant set?",
         "Both hold a full bottle of the fragrance. In a body lotion or body emulsion set the second item is scented skincare in the same scent; in a deodorant set it is a body spray. Shower gel sets add a scented wash."],
        ["Are these perfume gift sets authentic?",
         "Yes. Every gift set at Swansura is 100% authentic and ships from the UK, with free UK delivery over £40."],
    ],
}

if __name__ == "__main__":
    ALL = {}
    for f in glob.glob(sys.argv[1] + "/*.json"):
        d = json.load(open(f))
        if isinstance(d, dict) and "products" in d:
            for p in d["products"]:
                ALL[p["handle"]] = p
    build(A, ALL, "guide_gift_sets_under_30_2026-11-28.jsonl")
