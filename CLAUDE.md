# ClickGiant client previews

Static design mockups for ClickGiant clients, published with GitHub Pages at https://mockups.clickgiant.com/ (custom domain via the CNAME file; DNS is a Cloudflare CNAME `mockups` -> jerrycahalan.github.io, DNS only).

## West & Ginos (`west-ginos/`)
- Never edit `west-ginos/**/index.html` by hand. Edit the sources in `_build/` and run `python3 _build/build.py` from the repo root.
  - `_build/partials/` — shared header (topbar, nav, mobile menu), footer, review bar, icons, script
  - `_build/pages/` — page bodies (`home.html`, `car-accidents.html`, ...). Add new pages to `PAGES` in `build.py`.
  - `{{ROOT}}` is replaced with the relative path back to `west-ginos/`.
- Shared styles: `west-ginos/assets/site.css`. Images: `west-ginos/assets/img/`.
- Client copy rule: use the full firm name "Law Offices of West & Ginos, LLC" (never just "West & Ginos" in body copy).
- Keep yellow `<span class="flag">` tags on anything the client still needs to approve.
- Every page carries `<meta name="robots" content="noindex, nofollow, noarchive">`.
- The page plan and its status live in `_build/PLAN.md`. Read it before building, and update it after.
- After pushing, GitHub Pages republishes in about a minute.
