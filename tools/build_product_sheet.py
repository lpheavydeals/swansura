import sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import FormulaRule

out = sys.argv[1]
F = "Arial"
GREEN = "1F6B4F"
CLAY = "B4532A"
thin = Side(style="thin", color="D6DCE3")
border = Border(left=thin, right=thin, top=thin, bottom=thin)
input_fill = PatternFill("solid", fgColor="FFF8E1")
auto_fill = PatternFill("solid", fgColor="E3EEE8")
ex_fill = PatternFill("solid", fgColor="EDEFF2")

wb = Workbook()

# ---------- Instructions ----------
ins = wb.active
ins.title = "Instructions"
ins.sheet_view.showGridLines = False
ins.column_dimensions["A"].width = 3
ins.column_dimensions["B"].width = 24
ins.column_dimensions["C"].width = 95
ins["B2"] = "Swansura · Product Data Sheet"
ins["B2"].font = Font(name=F, size=18, bold=True, color=GREEN)
ins["B3"] = "Please fill in one row per product on the 'Products' tab and send the file back to us."
ins["B3"].font = Font(name=F, size=11, color="545C6B")

rows = [
    ("How to fill", None, None),
    ("Yellow cells", "Fill these in: Brand, Category, Product Name, SKU, MRP, Selling Price, H1, Meta Title, Meta Description.", input_fill),
    ("Green cells", "Calculated automatically (S.No, Discount %, character counts). Please don't edit them.", auto_fill),
    ("Row 3 (grey, italic)", "An example row showing the expected format. Overwrite it with a real product or delete it.", ex_fill),
    ("SKU", "Your stock code for the product, exactly as used in your inventory. Each SKU must be unique (duplicates turn red). No SKUs yet? Leave blank and we'll create them.", None),
    ("Prices", "In GBP (£), numbers only, e.g. 18.99. Selling Price should not be higher than MRP.", None),
    ("Category", "Pick from the dropdown. If none fits, type your own category.", None),
    ("Variants", "If a product comes in sizes or shades, add one row per variant and put the size/shade in the Product Name.", None),
    ("", "", None),
    ("SEO guidance", None, None),
    ("H1", "Main heading on the product page: brand + product + key benefit, e.g. 'Vilvah Milk Drop Brightening Serum'.", None),
    ("Meta Title", "Shown as the blue link in Google. Aim for 50–60 characters, keyword first, brand once. Count turns red above 60.", None),
    ("Meta Description", "Shown under the title in Google. Aim for 140–160 characters: benefit + UK delivery/offer. Count turns red above 160.", None),
    ("Not sure?", "Leave the SEO columns blank and we'll write them for you.", None),
]
r = 5
for k, v, fill in rows:
    c = ins.cell(row=r, column=2, value=k or None)
    if v is None:
        c.font = Font(name=F, size=12, bold=True, color=CLAY)
    else:
        c.font = Font(name=F, size=11, bold=True, color="1B1F2A")
        c.alignment = Alignment(vertical="top")
        if fill:
            c.fill = fill
            c.border = border
        if v:
            d = ins.cell(row=r, column=3, value=v)
            d.font = Font(name=F, size=11, color="1B1F2A")
            d.alignment = Alignment(wrap_text=True, vertical="top")
    r += 1
foot = ins.cell(row=r + 1, column=2, value="Prepared by Lokesh · www.thebilliongame.com")
foot.font = Font(name=F, size=10, italic=True, color="636B7A")

# ---------- Lists (hidden, feeds the Category dropdown) ----------
ls = wb.create_sheet("Lists")
cats = ["Skincare", "Haircare", "Body Care", "Bath & Shower", "Lip Care",
        "Fragrance – Perfume", "Fragrance – Attar / Oil", "Fragrance – Bakhoor & Home",
        "Men's Grooming", "Gift Sets & Combos", "Wellness"]
ls["A1"] = "Category"
ls["A1"].font = Font(name=F, bold=True)
for i, cname in enumerate(cats, start=2):
    ls.cell(row=i, column=1, value=cname).font = Font(name=F)
ls.column_dimensions["A"].width = 30
ls.sheet_state = "hidden"
CAT_END = len(cats) + 1

# ---------- Products ----------
ws = wb.create_sheet("Products", 1)
headers = [
    ("S.No", 7, "auto"),
    ("Brand", 22, "in"),
    ("Category", 26, "in"),
    ("Product Name", 42, "in"),
    ("MRP (£)", 12, "in"),
    ("Selling Price (£)", 15, "in"),
    ("Discount %", 11, "auto"),
    ("H1", 40, "in"),
    ("Meta Title", 46, "in"),
    ("Meta Title Length (50–60)", 13, "auto"),
    ("Meta Description", 62, "in"),
    ("Meta Description Length (140–160)", 15, "auto"),
]
ws["A1"] = "Swansura · Product Data Sheet  —  fill the yellow columns; green columns calculate automatically"
ws["A1"].font = Font(name=F, size=12, bold=True, color=GREEN)
ws.merge_cells("A1:L1")
ws.row_dimensions[1].height = 24
for i, (h, w, kind) in enumerate(headers, start=1):
    c = ws.cell(row=2, column=i, value=h)
    c.font = Font(name=F, size=10, bold=True, color="FFFFFF")
    c.fill = PatternFill("solid", fgColor=GREEN if kind == "in" else "636B7A")
    c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    c.border = border
    ws.column_dimensions[c.column_letter].width = w
ws.row_dimensions[2].height = 40

example = {
    2: "Vilvah",
    3: "Skincare",
    4: "Vilvah Milk Drop Brightening Serum 30ml (EXAMPLE)",
    5: 24.99,
    6: 19.99,
    8: "Vilvah Milk Drop Brightening Serum",
    9: "Milk Drop Brightening Serum UK | Vilvah | Swansura",
    11: "Vilvah Milk Drop Serum for brighter, even-toned skin. Gentle, natural formula. Shop the official range at Swansura with fast UK delivery. Order today.",
}
FIRST, LAST = 3, 602  # room for 600 products
for row in range(FIRST, LAST + 1):
    is_ex = row == FIRST
    ws.cell(row=row, column=1, value=f'=IF(COUNTA(B{row},D{row})=0,"",ROW()-{FIRST - 1})')
    ws.cell(row=row, column=7, value=f'=IF(OR(E{row}="",F{row}="",E{row}=0),"",(E{row}-F{row})/E{row})')
    ws.cell(row=row, column=10, value=f'=IF(I{row}="","",LEN(I{row}))')
    ws.cell(row=row, column=12, value=f'=IF(K{row}="","",LEN(K{row}))')
    if is_ex:
        for col, val in example.items():
            ws.cell(row=row, column=col, value=val)
    for col in range(1, 13):
        c = ws.cell(row=row, column=col)
        c.border = border
        kind = headers[col - 1][2]
        c.fill = ex_fill if is_ex else (input_fill if kind == "in" else auto_fill)
        c.font = Font(name=F, size=10, italic=is_ex, color="636B7A" if is_ex else "1B1F2A")
        c.alignment = Alignment(vertical="top", wrap_text=col in (4, 8, 9, 11),
                                horizontal="center" if col in (1, 7, 10, 12) else None)
        if col in (5, 6):
            c.number_format = '£#,##0.00'
        if col == 7:
            c.number_format = '0%'

dv_cat = DataValidation(type="list", formula1=f"=Lists!$A$2:$A${CAT_END}", allow_blank=True,
                        showErrorMessage=True, errorStyle="information",
                        errorTitle="New category",
                        error="This category isn't in the list. Click OK to keep it.")
dv_cat.add(f"C{FIRST}:C{LAST}")
dv_mrp = DataValidation(type="decimal", operator="greaterThanOrEqual", formula1="0", allow_blank=True,
                        showErrorMessage=True, errorTitle="MRP", error="Enter a number in £, e.g. 24.99")
dv_mrp.add(f"E{FIRST}:E{LAST}")
dv_sell = DataValidation(type="custom", formula1=f'=OR(E{FIRST}="",F{FIRST}<=E{FIRST})', allow_blank=True,
                         showErrorMessage=True, errorStyle="warning",
                         errorTitle="Selling price",
                         error="Selling Price is higher than MRP. Please check.")
dv_sell.add(f"F{FIRST}:F{LAST}")
for dv in (dv_cat, dv_mrp, dv_sell):
    ws.add_data_validation(dv)

red = Font(name=F, size=10, bold=True, color="C0392B")
redfill = PatternFill("solid", fgColor="FDECEA")
ws.conditional_formatting.add(f"J{FIRST}:J{LAST}",
                              FormulaRule(formula=[f'AND(J{FIRST}<>"",J{FIRST}>60)'], font=red, fill=redfill))
ws.conditional_formatting.add(f"L{FIRST}:L{LAST}",
                              FormulaRule(formula=[f'AND(L{FIRST}<>"",L{FIRST}>160)'], font=red, fill=redfill))

ws.freeze_panes = "E3"
ws.auto_filter.ref = f"A2:L{LAST}"
wb.active = wb.index(ws)
for s in wb.worksheets:
    s.sheet_view.tabSelected = s is ws
wb.calculation.fullCalcOnLoad = True
wb.save(out)
print("saved", out)
