"""Client confirmation sheet for the 9 Hemel duplicate pairs (7 Nov 2026).
Data: Shopify admin export of vendor:Hemel on 7 Nov 2026 (prices, stock, created dates) and
docs/seo/price_updates_2026-11-03.json (the price from the client's 3 Nov sheet).
Output: docs/Swansura_Hemel_Duplicates_Client_Check_2026-11-07.xlsx
"""
import pathlib
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.comments import Comment

ROOT = pathlib.Path(__file__).resolve().parents[2]
U = "https://www.swansura.com/products/"
# scent, A = Oct 2026 listing (title, handle, price, stock), B = May 2026 listing, price on client's 3 Nov sheet, done?
PAIRS = [
 ("Dorado", ("Hemel Dorado Eau de Parfum 100ml – Luxury Unisex Leather Amber Fragrance", "hemel-dorado-eau-de-parfum-100ml-luxury-unisex-leather-amber-fragrance", 54.99, 3),
  ("Hemel Paris Dorado EDP Unisex 100ML", "hemel-dorado-eau-de-parfum-100ml", 87.95, 10), 54.99, True),
 ("Gris", ("Hemel Gris Eau de Parfum 100ml – Luxury Unisex Citrus Woody Fragrance", "hemel-gris-eau-de-parfum-100ml-luxury-unisex-citrus-woody-fragrance", 53.99, 3),
  ("Hemel Paris Gris Eau De Parfum for all 100ML", "hemel-gris-eau-de-parfum-100ml", 87.95, 10), 53.99, True),
 ("Amethyst Dream", ("Hemel Amethyst Dream Eau de Parfum 100ml – Luxury Unisex Floral Fruity Fragrance", "hemel-amethyst-dream-eau-de-parfum-100ml-luxury-unisex-floral-fruity-fragrance", 61.99, 5),
  ("Hemel Amethyst Dream Unisex EDP 100ML", "hemel-amethyst-dream-unisex-eau-de-parfum-100ml", 69.99, 10), 69.99, False),
 ("Favourite Black", ("Hemel Favourite Black Eau de Parfum 100ml – Luxury Unisex Leather Amber Fragrance", "hemel-favourite-black-eau-de-parfum-100ml-luxury-unisex-leather-amber-fragrance", 61.99, 5),
  ("Hemel Favourite Black Unisex Eau De Parfum 100ML", "hemel-favourite-black-unisex-eau-de-parfum-100ml", 69.99, 10), 69.99, False),
 ("Fragrance Affair", ("Hemel Fragrance Affair Eau de Parfum 100ml – Luxury Unisex Floral Spicy Fragrance", "hemel-fragrance-affair-eau-de-parfum-100ml-luxury-unisex-floral-spicy-fragrance", 61.99, 5),
  ("Hemel Fragrance Affair Unisex Eau De Parfum 100ML", "hemel-fragrance-affair-unisex-eau-de-parfum-100ml", 63.99, 10), 63.99, False),
 ("Patchouli For All", ("Hemel Patchouli For All Eau de Parfum 100ml – Luxury Unisex Woody Patchouli Fragrance", "hemel-patchouli-for-all-eau-de-parfum-100ml-luxury-unisex-woody-patchouli-fragrance", 61.99, 5),
  ("Hemel Patchouli For All Eau De Parfum 100ML", "hemel-patchouli-for-all-eau-de-parfum-100ml", 60.99, 10), 60.99, False),
 ("Plateado", ("Hemel Plateado Eau de Parfum 100ml – Luxury Unisex Spicy Woody Fragrance", "hemel-plateado-eau-de-parfum-100ml-luxury-unisex-spicy-woody-fragrance", 49.99, 3),
  ("Hemel Plateado Eau De Parfum Unisex 100ML", "hemel-plateado-eau-de-parfum-100ml", 53.99, 10), 53.99, False),
 ("Rosado", ("Hemel Rosado Eau de Parfum 100ml – Luxury Unisex Floral Amber Long lasting Fragrance", "hemel-rosado-eau-de-parfum-100ml-luxury-unisex-floral-amber-fragrance", 49.99, 3),
  ("Hemel Rosado Eau De Parfum Unisex 100ML", "hemel-rosado-eau-de-parfum-100ml", 53.99, 10), 53.99, False),
 ("Valley of Diamond", ("Hemel Valley of Diamond Eau de Parfum 100ml – Luxury Unisex Floral Woody Fragrance", "hemel-valley-of-diamond-eau-de-parfum-100ml-luxury-unisex-floral-woody-fragran", 61.99, 5),
  ("Hemel Valley Of Diamond Unisex Eau De Parfum 100ML", "hemel-valley-of-diamond-unisex-eau-de-parfum-100ml", 60.99, 10), 60.99, False),
]

F = "Arial"
EMER, GOLD, INPUT, DONE, GREY = "1B4D3E", "F4EADA", "FFF2CC", "E4EEE9", "F5F2ED"
thin = Side(style="thin", color="D9CFC0")
BOX = Border(left=thin, right=thin, top=thin, bottom=thin)
WRAP = Alignment(wrap_text=True, vertical="top")
GBP = '£#,##0.00;-£#,##0.00;"-"'

wb = Workbook()
ws = wb.active
ws.title = "Hemel duplicates"
ws["A1"] = "Hemel: each scent is listed twice in the store – please confirm"
ws["A1"].font = Font(name=F, size=14, bold=True, color=EMER)
ws["A2"] = ("Every Hemel scent has two live product pages, one from May 2026 and one from October 2026, usually at different prices. "
            "Customers and Google see both. We suggest keeping ONE page per scent (the October one: clearer name, SEO title and photo descriptions) "
            "and hiding the other (set to Draft, nothing deleted, old link sends visitors to the kept page). "
            "Please fill in the yellow columns. Rows 1–2 (Dorado, Gris) are already done; please just confirm price and stock.")
ws["A2"].font = Font(name=F, size=10)
ws["A2"].alignment = WRAP
ws.merge_cells("A2:R2")
ws.row_dimensions[2].height = 58

H = ["#", "Scent", "Status (7 Nov 2026)",
     "Listing A – Oct 2026 (we suggest KEEP)", "A price £", "A stock", "A link",
     "Listing B – May 2026 (we suggest HIDE)", "B price £", "B stock", "B link",
     "Price on your 3 Nov sheet £", "Price gap A vs B £", "Stock if combined (A + B)",
     "YOUR CHOICE: which page to keep", "YOUR CHOICE: correct price £", "YOUR CHOICE: real stock (units)", "Your notes"]
HR = 4
for c, h in enumerate(H, 1):
    x = ws.cell(HR, c, h)
    x.font = Font(name=F, size=10, bold=True, color="FFFFFF")
    x.fill = PatternFill("solid", fgColor=EMER if c < 15 else "B5843A")
    x.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
    x.border = BOX
ws.row_dimensions[HR].height = 44

for i, (scent, a, b, sheet_price, done) in enumerate(PAIRS, 1):
    r = HR + i
    status = ("DONE: B hidden (Draft) + link redirected to A. Please confirm price and stock."
              if done else "Waiting for your choice. Both pages are live.")
    vals = [i, scent, status, a[0], a[2], a[3], U + a[1], b[0], b[2], b[3], U + b[1], sheet_price,
            f"=ABS(E{r}-I{r})", f"=F{r}+J{r}", "Keep A (Oct) – hide B" if done else None, None, None, None]
    for c, v in enumerate(vals, 1):
        x = ws.cell(r, c, v)
        x.font = Font(name=F, size=10, color="0000FF" if c in (5, 6, 9, 10, 12) else "000000")
        x.alignment = WRAP
        x.border = BOX
        if c in (5, 9, 12, 13, 16):
            x.number_format = GBP
        if c in (7, 11):
            x.hyperlink = v
            x.value = "Open page" if not (done and c == 11) else "Open (now redirects to A)"
            x.font = Font(name=F, size=10, color="0563C1", underline="single")
        if c >= 15:
            x.fill = PatternFill("solid", fgColor=INPUT)
        elif done:
            x.fill = PatternFill("solid", fgColor=DONE)
    ws.row_dimensions[r].height = 48
last = HR + len(PAIRS)

tr = last + 1
ws.cell(tr, 2, "Total").font = Font(name=F, size=10, bold=True)
for col in ("F", "J", "N", "Q"):
    x = ws[f"{col}{tr}"]
    x.value = f"=SUM({col}{HR+1}:{col}{last})"
    x.font = Font(name=F, size=10, bold=True)
    x.border = BOX

dv = DataValidation(type="list", formula1='"Keep A (Oct) – hide B,Keep B (May) – hide A,Keep both (they are different products),Not sure – let\'s discuss"', allow_blank=True)
ws.add_data_validation(dv)
dv.add(f"O{HR+1}:O{last}")
dvp = DataValidation(type="decimal", operator="between", formula1="0", formula2="1000", allow_blank=True,
                     error="Please enter a price in £, e.g. 54.99")
ws.add_data_validation(dvp)
dvp.add(f"P{HR+1}:P{last}")
dvs = DataValidation(type="whole", operator="between", formula1="0", formula2="10000", allow_blank=True,
                     error="Please enter a whole number of units")
ws.add_data_validation(dvs)
dvs.add(f"Q{HR+1}:Q{last}")

ws["L4"].comment = Comment("From the client's product sheet of 3 Nov 2026 (applied to the store that day). "
                           "It gave one price per scent; for 7 scents it matched the May page, for Dorado and Gris the October page.", "Swansura team")
ws["F4"].comment = Comment("Units in stock in Shopify on 7 Nov 2026.", "Swansura team")
ws["N4"].comment = Comment("If both pages' stock is real, the kept page should get the combined number.", "Swansura team")

n = last + 3
notes = [
 ("How to fill this in", True),
 ("1. Column O: pick which page to keep from the drop-down. Rows 1–2 are pre-filled because they are already done.", False),
 ("2. Column P: the correct selling price in £ (e.g. 54.99). Leave blank to use the 'Price on your 3 Nov sheet' (column L).", False),
 ("3. Column Q: how many bottles you really have of that scent in total (e.g. 13). The two pages currently show different stock: "
  "are the May page's units (column J) extra bottles, or the same bottles counted twice?", False),
 ("Example: Dorado → O 'Keep A (Oct) – hide B', P 54.99, Q 13.", False),
 ("Blue numbers are taken from the store on 7 Nov 2026. Black cells are calculated. Yellow cells are yours to fill.", False),
 ("Nothing is deleted: the hidden page keeps its photos and history and can be switched back on.", False),
]
for k, (t, bold) in enumerate(notes):
    x = ws.cell(n + k, 1, t)
    x.font = Font(name=F, size=10, bold=bold, color=EMER if bold else "000000")
    ws.merge_cells(start_row=n + k, start_column=1, end_row=n + k, end_column=18)

widths = [4, 16, 26, 38, 10, 8, 12, 34, 10, 8, 14, 12, 11, 12, 26, 13, 14, 28]
for c, w in enumerate(widths, 1):
    ws.column_dimensions[chr(64 + c)].width = w
ws.freeze_panes = "C5"
ws.sheet_view.zoomScale = 90
ws.page_setup.orientation = "landscape"
ws.page_setup.fitToWidth = 1
ws.sheet_properties.pageSetUpPr.fitToPage = True
ws.page_setup.fitToHeight = 0

out = ROOT / "docs/Swansura_Hemel_Duplicates_Client_Check_2026-11-07.xlsx"
wb.save(out)
print(out)
