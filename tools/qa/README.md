# Theme QA scripts (Day 5)

- `crawl.py PATHS.txt OUT.json` – fetches each path from the draft theme preview (cookie set via `?preview_theme_id=`), records status, Liquid errors, H1s, title, meta description, canonical, robots, JSON-LD validity, images without alt and internal links.
- `browse.js PAGES.json OUT.json` – Playwright at 390 px and 1366 px: console errors, sideways scroll, text < 11 px, tap targets < 24 px, LCP, CLS, axe WCAG 2.1 AA (needs `axe.min.js` from the `axe-core` package next to the script or in `$AXE`), screenshots.
- `journey.js` – menu, search, product page, add to bag, drawer, bag page, checkout, sort.

Change `THEME` / the preview ID at the top of each script for another theme.
