# LOG — dated record of the swarm

Newest first. Times are UK.

## 29 Sep 2026 (Tue, later) — control room phase 1 on the private Newsroom page

- Built the **CONTROL** view inside the private Newsroom page (artifact `MGGZNGHSGWtAGwo3kZNxZn`, version 10) to `claude/control-room-brief.md`. Read only. No scheduled task touched, no capability or access rule changed, kill switch only read.
- Checked first what the page can reach: its capability is `db` only, so it reads `editions`, `desk`, `journalism` and `os`, and cannot reach the public feed, Typefully or the task list. Those three show grey lamps with the reason rather than a guess.
- The ledger alone undercounts posts, because explainer and launch posts are made in other chats and never write to `journalism`. The view instead reads back the count L1 itself makes of the whole account at the start of each run, and shows when it was counted.
- Finding on the day: L1's 16:36 run counted **8 posts on the account (5 published, 3 scheduled)** against the 5-a-day ceiling. L1 obeyed the ceiling and published nothing; the other chats' posts do not count themselves. This puts a number on the open item "same 5-a-day ceiling for the Lisa draft desk and the explainer posts".
- Verified: three numbers recounted from the raw documents (7 editions today; 8 posts from L1's own run note; 6 corrections / 43 mid stories / 307 stories over 40 editions); stale cases (Monday 06:30, Saturday 10:00) show amber with the reason, two missing slots show red; NEWS, CONTENT and OS all still render with no console errors.
- Record: Newsroom project doc `claude/control-room-phase1.md`.
- Next, on Alex's word: phase 2 heartbeats — every task writes one row to `ops/heartbeats`, watchdog first, writer last, under the two-test-runs change-control rule.

## 29 Sep 2026 (Tue, evening) — the Terminal

- Alex named the whole thing the **BuyTrigger Newsroom Terminal** ("the automatic Walter Bloomberg"): gather (Tim) → publish → broadcast (L1 headlines with story links, L2 threads with graphics, L3 articles, L4 video later, Telegram) → measure (control room + 3.19 CRM & Funnel) → control. Blueprint in the Claude project: `claude/terminal-blueprint.md`.
- Project moved out of the Dashboard project into its own ("BuyTrigger Newsroom & Automation", renamed to the Terminal the same evening). All 11 Newsroom docs copied across word for word (`docs/project-pack/`), plus `docs/START-HERE.md`.
- All six scheduled tasks renamed `3.7.15 Terminal · …`; schedules, prompts and models untouched. The Lisa draft desk prompt now counts the same 5-a-day ceiling as L1 and runs on London time (another chat, 29 Sep afternoon).
- Repo renamed `buytrigger-swarm` → `buytrigger-terminal` (steps in `docs/RENAME-STEPS.md`; Alex does the GitHub and Mac steps). Control-room brief written (`claude/control-room-brief.md`).

## 29 Sep 2026 (Tue) — daily ceiling; repo brought up to date with the live bees

- State found: L1 publishing on its own since Mon 28 Sep after Colette + Lisa approve (2 posts Monday, both live). Tue 07:25 run could not reach Typefully; 4 cards waited for 16:25. L2 drafting nightly; the Lisa draft desk schedules it for 19:30. L3's first article (VIX week) delivered Sun 27 Sep as a draft. The Newsroom now files 13 editions a weekday.
- Another chat's explainer posts (AMD, Nvidia buyback, Meta) went out alongside; the Nvidia one repeated Monday's L1 story within 24 hours. With the launch post, 5 posts were out or booked for Tuesday before L1's 16:25 run.
- Alex: "add daily ceiling". L1 prompt now counts every post on the account for the UK day (any source) and publishes nothing once 5 are out or booked; 45-minute gap from any other post; cards over the ceiling wait for the next run. Live on the task at 15:54 UK.
- Repo: `bees/L1-fast.md`, `bees/L3-article.md` replaced with the live prompts; `bees/lisa-desk.md` added (the other chat's task, for the record); README, SCHEDULE, gates updated; ledger snapshot refreshed (28 documents).
- Still open: Typefully analytics tools are not exposed to Claude right now, so reach numbers can't be read automatically; charts still can't attach (upload host); GitHub push blocked by the Mac's token scope.

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
