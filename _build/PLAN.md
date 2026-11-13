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
| 1 | Trent S. West bio | `attorneys/trent-west/` | approved | Trent 2026-11-11: only federal admission is bankruptcy court. Trent 2026-11-12: Central and Southern Districts (firm no longer does bankruptcy; he's fine either way), now listed, flag removed. Added outdoorsman line (deer hunting, bass fishing). |
| 1 | Michael G. Ginos bio | `attorneys/michael-ginos/` | sent 2026-11-11 | Michael 2026-11-11 edits made (draft 2): do NOT name Gori, say "a large law firm"; "contributed to a trial team who helped win" the $7.1M verdict; prosecutor line adds courtroom experience; double major Communications (organizations) + Spanish; his own Away-from-the-office text; admitted S.D. Ill. Not yet approved. |
| 2 | Contact | `contact/` | sent 2026-11-12 | Both offices (Litchfield 413 N. State St., Litchfield, IL 62056; Nokomis 320 West Central St., Nokomis, IL 62075), phones, map links, form. Hours: flag "Confirm hours". Built with flags: Confirm hours (both offices), Confirm walk-in policy. Michael 2026-11-12: "look good to me but Trent may weigh in before going live." Trent 2026-11-12: hours correct (flags removed), walk-ins fine (FAQ + new "Stop by either office" card), drop Pay My Bill from "Ways to reach" (done; header/footer Pay My Bill links untouched). Not explicitly approved yet. |
| 2 | Attorney Referrals | `attorney-referrals/` | sent 2026-11-12 | Modeled on gideonasen.com. Proof: ~1 in 2 injury cases referred by other attorneys. Referral-fee wording must follow Illinois RPC 1.5(e); verify on the official source and flag for Trent. Rule 1.5(e) summary checked against the Illinois Courts article (illinoiscourts.gov News/1148); flags: Trent to approve wording, Trent to confirm fee payment timing. Michael 2026-11-12: looks good. Trent 2026-11-12: fees paid when the case settles; his Rule 1.5 item 1 wording adds "but either way we cover all expenses"; FAQ ending "most attorneys that refer us cases let us handle the matter and they just wait for their check"; CTA "We'll take it from there." Both flags removed. Not explicitly approved yet. |
| 3 | Workers' Compensation | `workers-compensation/` | built | Illinois Workers' Compensation Act, 820 ILCS 305. Note the difference from a regular injury claim (no fault, the Commission, not a jury). Built 2026-11-13 from the IWCC Handbook + Act PDF on iwcc.illinois.gov (ilga.gov blocks automated fetching): 45-day notice, 3 yrs / 2 yrs after last payment, no-fault, arbitrator then 3-commissioner panel, 20% fee cap, 4(h) anti-retaliation. Flags: "can't sue employer / third-party claims" wording (Trent/Michael), fee wording (co-counsel). Co-counsel framing matches homepage. |
| 3 | Mesothelioma | `mesothelioma/` | built | Michael's complex-litigation background (never name Gori; say "a large law firm"). No invented results. Built 2026-11-13: NCI asbestos fact sheet (most mesotheliomas from asbestos; 10-40+ yrs latency for asbestos illness) and OSHA (jobs, short exposures). Flags: deadline wording (x2), take-home exposure (co-counsel). No results shown. |
| 3 | Nursing Home Abuse | `nursing-home-abuse/` | built | Illinois Nursing Home Care Act, 210 ILCS 45. Built 2026-11-13: 2-107 (free from abuse/neglect), 3-601 (owner/licensee liable for staff), 3-602 (damages, costs, attorney fees) verified via Ill. Supreme Court, Eads v. Heritage Enterprises (2003), cited to that opinion. IDPH hotline 1-800-252-4343 + LTC Ombudsman (ilaging.illinois.gov). Flags: deadline wording, retaliation FAQ answer. |
| 3 | Product Liability | `product-liability/` | built | Michael's pharma/medical device trial-team experience ("a large law firm", not Gori). Built 2026-11-13: uses his bio's $7.1M trial-team wording. Resources: NHTSA VIN recalls, CPSC/SaferProducts, FDA MedWatch; 2-yr deadline (735 ILCS 5/13-202). Flags: deadline wording (statute of repose not verified), "what makes a product defective" and "do I have to prove carelessness" FAQ answers. |
| 4 | Motorcycle Accidents | `motorcycle-accidents/` | built | $250K motorcycle settlement (homepage result). Built 2026-11-13: eye protection verified on ilga.gov (625 ILCS 5/11-1404). Flags: helmet wording (no adult helmet law not verified), no-helmet FAQ answer. |
| 4 | Pedestrian Accidents | `pedestrian-accidents/` | built | $300K car vs. pedestrian settlement (2026). Built 2026-11-13: crosswalk stop-and-yield + no passing a stopped car verified on ilga.gov (625 ILCS 5/11-1002). Flags: UM coverage for pedestrians (x2), household member's policy. |
| 4 | Wrongful Death | `wrongful-death/` | built | Wrongful Death Act, 740 ILCS 180. Built 2026-11-13 from 740 ILCS 180/2 on ilga.gov: personal representative files for spouse + next of kin; split by dependency; grief/sorrow/mental suffering; 2 yrs from death with extensions (violent intentional acts, criminal cases, minors); punitive damages allowed except healing-art/legal malpractice and government (P.A. 103-514, eff. 8-11-23). No results shown. Flag: survival claim wording (755 ILCS 5/27-6 not fetched). CTA headline "We're here when you're ready." (no "Lawyer up."). |
| 4 | Catastrophic Injury | `catastrophic-injury/` | built | Built 2026-11-13. Law cards reuse cites already on the site (13-202, 2-1116, 7-203). No results shown. Mentions co-counsel "when the case calls for it". |
| 4 | Boating Accidents | `boating-accidents/` | built | Built 2026-11-13. Names Lake Lou Yaeger (Litchfield, per visitlitchfield.com), Coffeen Lake, Lake Shelbyville, Carlyle Lake (USACE lakes, recreation.gov); Lake Taylorville dropped (not verified). No distances given. Boating statutes (625 ILCS 45) and 33 CFR 173.55 could not be fetched, so BUI and accident-reporting lines are flagged; maritime-law note and homeowner/umbrella coverage flagged. Added "Boating accident" to the case-type dropdown on batch 4 pages only. |
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
- 2026-11-12 (scheduled run): Batch 3 NOT built. Every fetch of the official sources (ilga.gov, iwcc.il.gov, dph.illinois.gov, epa.gov, cancer.gov) failed with an unanswered permission prompt, so no law could be verified. Retry batch 3 next run once web fetch is allowed. Note: the homepage says these four are co-counsel cases ("we partner with experienced co-counsel and stay involved"); the pages must say the same.
- 2026-11-12 (scheduled run): Reply draft in Gmail (thread "Re: West & Ginos website", to Michael, cc Trent + Allyson) with the edits and batch 2 (Contact, Attorney Referrals) marked sent.
- 2026-11-12 (scheduled run, 2nd today): No client replies needed (latest message in both threads is Jerry's). Batch 3 still NOT built: fetches of ilga.gov, iwcc.il.gov, dph.illinois.gov, cancer.gov and epa.gov again failed with an unanswered permission prompt, so no law could be verified. Needs Jerry to allow those domains for unattended runs. No draft written (batch 2 is still out with the client).
- 2026-11-12 (scheduled run, 3rd today): Michael OK'd Contact and Attorney Referrals but deferred to Trent, so both stay `sent`. No site changes needed. Batch 3 still NOT built: ilga.gov fetch again failed (permission prompt not answered). Jerry needs to allow ilga.gov, iwcc.il.gov, dph.illinois.gov, cancer.gov, epa.gov for unattended runs. Reply draft to Michael (cc Trent, Allyson) in "Re: West & Ginos website" thanking him and listing Trent's open items (referral fee wording/timing, hours, walk-ins, bankruptcy court district).
- 2026-11-12 (scheduled run, 4th today): No client replies needed (latest message in both threads is Jerry's; Jerry sent the batch 2 follow-up to Michael at 18:27 UTC, which names batch 3 as next up). Batch 3 still NOT built: ilga.gov fetch failed again (permission prompt not answered in time). No draft written. Jerry needs to allow ilga.gov, iwcc.il.gov, dph.illinois.gov, cancer.gov, epa.gov for unattended runs.
- 2026-11-12 (scheduled run, 5th today): Trent replied on batch 2 + bankruptcy district. Made all his edits (see Notes). Contact and Attorney Referrals stay `sent` (edits given, no explicit approval). Batch 3 still NOT built: ilga.gov fetch failed again (permission prompt not answered). Reply draft to Trent (cc Michael, Allyson) in "Re: West & Ginos website" listing the changes.
- 2026-11-13 (scheduled run): No client replies needed (latest message in both threads is Jerry's: Trent thread 2026-11-12 23:01 UTC, Michael thread 2026-11-11). Batch 3 still NOT built: ilga.gov fetch (820 ILCS 305/6) failed again with an unanswered permission prompt, so no law could be verified. No draft written (batch 2 still out with the client; nothing `built`). Jerry needs to allow ilga.gov, iwcc.il.gov, dph.illinois.gov, cancer.gov, epa.gov for unattended runs.
- 2026-11-13 (scheduled run, 2nd today): No client replies needed (latest message in both threads is still Jerry's). Batch 3 still NOT built: ilga.gov fetch (820 ILCS 305) failed again with an unanswered permission prompt. No draft written. Jerry needs to allow ilga.gov, iwcc.il.gov, dph.illinois.gov, cancer.gov, epa.gov for unattended runs.
- 2026-11-13 (scheduled run, 3rd today): No client replies needed (latest message in both threads is still Jerry's). Batch 3 still NOT built: ilga.gov fetch (820 ILCS 305) failed again with an unanswered permission prompt. No draft written. Jerry needs to allow ilga.gov, iwcc.il.gov, dph.illinois.gov, cancer.gov, epa.gov for unattended runs.
- 2026-11-13 (scheduled run, 4th today): No client replies needed (latest message in both threads is still Jerry's). Built batch 3 (Workers' Compensation, Mesothelioma, Nursing Home Abuse, Product Liability). ilga.gov still can't be fetched (robots.txt refuses automated fetches), so law was verified on other official sources: iwcc.illinois.gov (Handbook + Act PDF), illinoiscourts.gov (Eads opinion for 210 ILCS 45), ilaging.illinois.gov, dph.illinois.gov, cancer.gov, osha.gov, nhtsa.gov, cpsc.gov, fda.gov. Header Injury Cases menu now lists the four pages (replacing the single "Workers' Comp, Mesothelioma & More" link); footer and homepage "More injury cases" cards link to them. Checked at 1440px and 390px, no sideways overflow. No draft written: batch 2 (Contact, Attorney Referrals) and Michael's bio are still `sent` and waiting on the client.
- 2026-11-13 (scheduled run, 5th today): No client replies needed (latest message in both threads is still Jerry's). Built batch 4 (Motorcycle Accidents, Pedestrian Accidents, Wrongful Death, Catastrophic Injury, Boating Accidents). ilga.gov fetched OK this time for 740 ILCS 180/2, 625 ILCS 5/11-1404 and 11-1002; other sections (11-1003.1, 11-1403, 755 ILCS 5/27-6, 625 ILCS 45/5-16, 6-1, 6-2) and ecfr.gov hit unanswered permission prompts, so those points are flagged. Header, footer (now also lists pedestrian, catastrophic, boating) and homepage case cards link to the new pages. Checked at 1440px and 390px, no sideways overflow. No draft written: batch 2 (Contact, Attorney Referrals) and Michael's bio are still `sent` and waiting on the client; batches 3 and 4 are `built` and queued for the next email.
