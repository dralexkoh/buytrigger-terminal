# LOG — dated record of the swarm

Newest first. Times are UK.

## 26 Sep 2026 (Sat) — audit, two fixes, the repo package

- Audited the bees' first unattended runs (Fri 25 Sep). Layer 1 made two drafts (10926756 Robinhood Form 4, stock named; 10926758 AI capex). Layer 2 made one (10931326 Robinhood, with two charts as files). Every number in all three checked by script against the `ok`/`sec` claim rows: 14, 11 and 49 numbers, all trace. The 22:30 edition carried no correction touching those stories.
- Two compliance edits to draft 10931326: X post 10 now ends "Not advice, not a view on the stock." and Threads post 4 carries "Not advice." before the link. The scratchpad says so, and warns marketing that Layer 1 draft 10926756 covers the same filing — send one or the other on the same day.
- Layer 2 prompt updated in the live task at 07:26: cross-layer rule (prefer a subject Layer 1 did not draft today; otherwise title `· also L1 today` plus a warning), not-advice line on X when a stock is named, the number check as a step, `overlaps_l1` in the ledger. `bees/L2-story.md` is that text.
- Layer 1 and Layer 3 prompts copied from the live tasks into `bees/` unchanged.
- Tools written and run on the real Friday data: `verify_numbers.py`, `check_lengths.py` (caught the Threads not-advice gap), `score_stories.py` (shows Oracle at 64 across nine editions with a 22:30 correction, Micron 57, Robinhood 40 marked as Layer 1's).
- Package delivered as a tarball for Alex to drop into the new `buytrigger-swarm` repo (`SETUP.md`).
- Found and left alone: the Layer 1 task's schedule is two runs a day (07:25, 16:25) though it is named "4x"; changed by someone else on 25 Sep.
- Nothing published. Marketing has not yet sent any of the four drafts (10922651, 10926756, 10926758, 10931326).

## 25 Sep 2026 (Fri) — marketing sends; three bees live; CRM clash resolved

- After the 24 Sep failures, Alex's rule: bees draft, marketing reviews and sends. All prompts changed to drafts-only; Threads ≤ 450 plain punctuation; no URL or domain on X.
- Layer 2 shakedown by hand (rates week, draft 10922651, two charts). Typefully media upload blocked by network policy (upload host not allowed); charts delivered as files.
- Three scheduled tasks created: L1 (four runs a day, later changed to two by someone else), L2 nightly 23:10, L3 Sunday 08:40.
- Built a CRM Stage 1 package in the dashboard repo without checking the Project first; the CRM chat had filed its own handover at 13:12. Package withdrawn to `_to_delete/crm-stage1-withdrawn-2026-09-25/` in the dashboard repo (Alex deletes the folder and the local branch `crm-stage1`). Naming convention adopted: one job = one chat = one branch `<job>-<stage>`. Decision: spin the swarm off into its own repo.
- Layer 1 first unattended run 16:25: two drafts, evidence chains complete, FCA logged. Layer 2 first run 23:11: one draft, ledger written.

## 24 Sep 2026 (Thu) — surface 2 built and shaken down

- Surface 2 defined: three layers (FAST, STORY, ARTICLE), everything reads the feed, gates as the "algo".
- Five Layer 1 drafts made by hand from the day's cards. Four published through Typefully at Alex's "start shooting them out": 10913777 and 10913771 live on X and Threads; 10913772 and 10913774 live on X, failed on Threads (no reason given); one retry failed. $SCHW draft 10913768 deleted by someone.
- X refused posts containing a URL or bare domain. Threads refused 494-character posts with arrows and em dashes (cause unconfirmed).
- Alex: "a lot of failed posts, you didn't do your homework properly" — owned: no end-to-end test before publishing. Fix: one end-to-end test first, then marketing review, always.
