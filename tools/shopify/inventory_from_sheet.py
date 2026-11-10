"""Read the filled stock sheet and print inventorySetQuantities inputs.

Usage: python3 tools/shopify/inventory_from_sheet.py <filled.xlsx> [out.json]
Only rows with a number in 'NEW STOCK (fill in)' that differs from 'Stock now'
are sent; Shopify Collective (supplier) rows are skipped. Inventory item ids
come from docs/backups/inventory_before_2026-11-10.json (re-read live stock
before sending, and use changeFromQuantity = live quantity so a sale in
between is not overwritten).
"""
import json, sys, openpyxl
LOC = 'gid://shopify/Location/111879553411'
snap = {s['variant_id'].split('/')[-1]: s for s in
        json.load(open('docs/backups/inventory_before_2026-11-10.json'))['variants']}
ws = openpyxl.load_workbook(sys.argv[1], data_only=True)['Stock']
H = [c.value for c in ws[1]]
ix = {h: H.index(h) for h in H}
out = []
for r in ws.iter_rows(min_row=2, values_only=True):
    new = r[ix['NEW STOCK (fill in)']]
    if new in (None, '') or r[ix['Section']] == 'Collective supplier':
        continue
    new = int(new)
    s = snap[str(r[ix['Variant ID']])]
    if new == s['qty']:
        continue
    out.append(dict(inventoryItemId=s['inventory_item'], locationId=LOC, quantity=new,
                    changeFromQuantity=s['qty'], title=s['title'], variant=s['variant']))
batches = [out[i:i+250] for i in range(0, len(out), 250)]
json.dump(batches, open(sys.argv[2] if len(sys.argv) > 2 else '/dev/stdout', 'w'), ensure_ascii=False, indent=1)
print(f'{len(out)} changes in {len(batches)} batches', file=sys.stderr)
