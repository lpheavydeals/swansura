# Keyword research build

```bash
python3 -I tools/keywords/build_kw.py docs/data/Swansura_Product_Data_Sheet_2026-10-18.xlsm /tmp/kw.json   # keyword sets per product
python3 -I tools/keywords/autocomplete.py /tmp/kw.json /tmp/ac.json                                    # Google UK autocomplete (~6 min, needs network)
python3 -I tools/keywords/make_xlsx.py /tmp/kw.json /tmp/ac.json seo/Swansura_Keyword_Research.xlsx    # workbook
```
Then recalculate formulas (LibreOffice) before reading values. Volumes come from Semrush exports pasted into the "Semrush Data" tab.
