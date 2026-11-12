# West & Ginos — page plan

The scheduled email check reads this file every run. It builds the next batch marked `todo`, and presents built batches to the client in its reply drafts. Keep it up to date: change a status when it changes, and add a dated note to the log at the bottom.

Statuses:
- `todo`: not built yet
- `built`: live on the preview site, not shown to the client yet
- `sent`: presented in an email (note the date)
- `approved`: the client OK'd it
- `blocked`: needs something from the client first (say what)

Preview base: https://mockups.clickgiant.com/west-ginos/

## Done
| Page | Path | Status |
|---|---|---|
| Homepage | `/` | approved |
| Car Accidents | `car-accidents/` | approved |
| Truck Accidents | `truck-accidents/` | approved |
| Dog Bites | `dog-bites/` | approved |
| Slip, Trip & Fall | `slip-trip-fall/` | approved |

## Batches, in order
| # | Page | Path | Status | Notes |
|---|---|---|---|---|
| 1 | Why Choose Us | `why-choose-us/` | approved | Trent 2026-11-11: "rest looks good"; compare intro now "Clients have come to us after a big firm made them feel unimportant." |
| 1 | Trent S. West bio | `attorneys/trent-west/` | approved | Trent 2026-11-11: only federal admission is bankruptcy court (flag: which district?). Added outdoorsman line (deer hunting, bass fishing). |
| 1 | Michael G. Ginos bio | `attorneys/michael-ginos/` | sent 2026-11-11 | Michael 2026-11-11 edits made (draft 2): do NOT name Gori, say "a large law firm"; "contributed to a trial team who helped win" the $7.1M verdict; prosecutor line adds courtroom experience; double major Communications (organizations) + Spanish; his own Away-from-the-office text; admitted S.D. Ill. Not yet approved. |
| 2 | Contact | `contact/` | built | Both offices (Litchfield 413 N. State St., Litchfield, IL 62056; Nokomis 320 West Central St., Nokomis, IL 62075), phones, map links, form. Hours: flag "Confirm hours". Built with flags: Confirm hours (both offices), Confirm walk-in policy. |
| 2 | Attorney Referrals | `attorney-referrals/` | built | Modeled on gideonasen.com. Proof: ~1 in 2 injury cases referred by other attorneys. Referral-fee wording must follow Illinois RPC 1.5(e); verify on the official source and flag for Trent. Rule 1.5(e) summary checked against the Illinois Courts article (illinoiscourts.gov News/1148); flags: Trent to approve wording, Trent to confirm fee payment timing. |
| 3 | Workers' Compensation | `workers-compensation/` | todo | Illinois Workers' Compensation Act, 820 ILCS 305. Note the difference from a regular injury claim (no fault, the Commission, not a jury). |
| 3 | Mesothelioma | `mesothelioma/` | todo | Michael's complex-litigation background (never name Gori; say "a large law firm"). No invented results. |
| 3 | Nursing Home Abuse | `nursing-home-abuse/` | todo | Illinois Nursing Home Care Act, 210 ILCS 45. |
| 3 | Product Liability | `product-liability/` | todo | Michael's pharma/medical device trial-team experience ("a large law firm", not Gori). |
| 4 | Motorcycle Accidents | `motorcycle-accidents/` | todo | $250K motorcycle settlement (homepage result). |
| 4 | Pedestrian Accidents | `pedestrian-accidents/` | todo | $300K car vs. pedestrian settlement (2026). |
| 4 | Wrongful Death | `wrongful-death/` | todo | Wrongful Death Act, 740 ILCS 180. |
| 4 | Catastrophic Injury | `catastrophic-injury/` | todo | |
| 4 | Boating Accidents | `boating-accidents/` | todo | Lake Lou Yaeger, Lake Shelbyville, Carlyle Lake, Lake Taylorville: verify which are near before naming. |
| 5 | Traffic & Criminal Defense | `traffic-criminal/` | todo | Both partners are former prosecutors; Trent is in the National College for DUI Defense. |
| 5 | Estate Planning | `estate-planning/` | todo | Wills for Warriors (free wills for veterans). |
| 5 | Probate | `probate/` | todo | |
| 6 | Litchfield | `litchfield-il/` | todo | Office town. Unique content per town page. |
| 6 | Nokomis | `nokomis-il/` | todo | Office town. Trent's hometown. |
| 6 | Hillsboro | `hillsboro-il/` | todo | Michael's hometown; Montgomery County courthouse. |
| 6 | Carlinville | `carlinville-il/` | todo | Macoupin County seat. |
| 7 | Springfield | `springfield-il/` | todo | Sangamon County. |
| 7 | Edwardsville | `edwardsville-il/` | todo | Madison County seat. |
| 7 | Taylorville | `taylorville-il/` | todo | Christian County seat. |
| 7 | Vandalia | `vandalia-il/` | todo | Fayette County seat; I-70. |
| 8 | Effingham | `effingham-il/` | todo | I-57/I-70 interchange. |
| 8 | Greenville | `greenville-il/` | todo | Bond County seat. |
| 8 | Staunton | `staunton-il/` | todo | Macoupin County. |
| 8 | Mt. Olive | `mt-olive-il/` | todo | Macoupin County. |

## Waiting on the client (don't build until they send it)
| Page | Path | Status | Needs |
|---|---|---|---|
| Meet Our Team | `meet-our-team/` | blocked | Staff names, titles, photos |
| Reviews | `reviews/` | blocked | Permission to use real Google reviews |

## Rules for new pages
- Follow `CLAUDE.md`. Use the Car Accidents layout for injury pages and the bio/Why Choose Us styles where they fit. Add each page to `PAGES` in `build.py`, and replace the matching `href="#"` links in the header, footer and homepage.
- Client copy uses the full firm name "Law Offices of West & Ginos, LLC". Every page stays noindex.
- Law: only state rules you've checked against an official source (ilga.gov for Illinois statutes, ecfr.gov for federal rules), cited with the `.cite` component. Mark anything uncertain with a yellow `<span class="flag">` instead of guessing.
- Results: only amounts already on the site or confirmed by the client. Never client names. Never invent a result, quote or review.
- Photo ideas ("Example: photo shoot" frames) must be things the firm can shoot with staff or willing clients. No accident or injury scenes.
- Never mention LSAs, FindLaw or ask4sam.
- Town pages: each one gets unique local content (courthouse, main roads, hospitals, distance from our offices), verified by search. No copy-paste between towns.
- Check every page at 1440px and 390px with Playwright before pushing. Nothing may overflow sideways.

## Log
- 2026-11-11: Batch 1 (Why Choose Us + both bios) built and sent to Trent and Michael.
- 2026-11-11 (scheduled run): No client replies needed (latest messages in both threads are Jerry's). Built batch 2 (Contact, Attorney Referrals); nav, footer and homepage links now point to them. Not sent yet: batch 1 is still waiting on the client.
- 2026-11-12 (scheduled run): Trent and Michael replied on batch 1. Made their bio and Why Choose Us edits. Why Choose Us and Trent's bio approved; Michael's bio at draft 2. Litchfield address (413 N. State St.) already correct everywhere.
