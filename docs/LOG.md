# LOG — dated record of the swarm

Newest first. Times are UK.

## 3 Oct 2026 (Sat) — stop switches on the control room (phase 3)

- Alex: "approve — i am going out so push as much as you can". Control room (artifact `MGGZNGHSGWtAGwo3kZNxZn`) is now **version 12** with a **SWITCHES** panel under the top row: **The wire** (`journalism/config.wire_autopost`) and **L1 fast posts** (`l1_autopost`), each with a STOP / ALLOW button behind a one-line confirm, plus **STOP ALL PUBLISHING**. Each write stamps `<lane>_set_at` / `<lane>_set_by`. These two fields are the only thing the page writes. **Neither switch was flipped** — `l1_autopost` is still `true`, `wire_autopost` still `false`; the `how_to_stop` note in the document now mentions the page.
- The wire's second lock is shown honestly: when the switch is on but the task's MODE line is still DRAFTS ONLY the row reads ALLOWED · TASK STILL ON TEST and nothing publishes. STOP always works regardless of MODE. The page reads MODE from the newest wire ledger entry, so it is known at weekends too. Not covered by any switch: the newsroom editions and the Lisa draft desk — the panel says so.
- Write path proven on the real document at access level `admin` (same-value update, version 2 → 3). Confirm / cancel / STOP ALL tested on a 390 px phone; no-database case shows "NOT SAVED" and changes nothing; Monday clock and Saturday both checked; NEWS, CONTENT and OS unaffected, no console errors. Page pinned to Alex's Claude sidebar.
- **APPROVE on the CONTENT tab is now WANT THIS.** Checked the code and every bee prompt: it only ever wrote a timestamp on the card and no bee reads it. Label and footer now say so; the data field is unchanged. Making bees prefer wanted cards would be a prompt change — Alex's call.
- Also: countdown to the next writer and wire slot on the tiles; a five-weekday strip of headlines cleared in THE WIRE section.
- Records: project `claude/control-room-phase1.md` (now carries a phone how-to and the phase-3 record), `claude/START-HERE.md` rule 5. Push still needs Alex's token.

## 2 Oct 2026 (Fri, late) — London time put back on three crons; the control room learns the wire

- **Clock-change defect found and fixed.** When L1, L2 and L3 were re-created earlier tonight they lost their `CRON_TZ=Europe/London` prefix (the Lisa desk kept it). They fire at the right UK time today only because BST is UTC+1; from Sunday 25 October they would have run an hour early — L1 06:25/15:25, L2 22:10 (before the 22:45 edition exists), L3 07:40. Alex: "Yeah London time prefix of course". Put back at 23:45 UK with `update_trigger`, schedule only, no prompt sent. Next runs unchanged and verified: L1 Mon 07:25, L2 Mon 23:10, L3 Sun 08:40. `bees/SCHEDULE.md` and `docs/START-HERE.md` updated; the standing rule is now written down — every cron carries the prefix.
- **Control room (artifact `MGGZNGHSGWtAGwo3kZNxZn`, version 11)** now knows about the wire, which it could not see at all: a wire machine tile with its own 13 slots and a LIVE / DRAFTS ONLY badge; a THE WIRE section listing every headline with its form, full text, Typefully id, who cleared it, and the skip reasons; a fourth number on the top row (wire headlines today, separate from the 5-a-day lane); alerts when a wire run leaves no record, when a headline errors, or when the kill switch and the task's MODE line disagree. `journalism/wire-<date>` is read in its own shape and kept out of the card ledger. Still read-only; no capability or access rule changed.
- Checked against tonight's real test run: 4 headlines, DRAFTS ONLY, 13 editions seen, backlog note and all 4 skip reasons shown; a faked Monday clock gives amber at one missed wire run and red at three; NEWS, CONTENT and OS all still render with no console errors.
- `docs/START-HERE.md` carried the four deleted task ids until now; replaced with the live seven, including the wire.

## 2 Oct 2026 (Fri) — L1, L2, L3 and the Lisa desk re-homed to the Terminal project

- Scheduled tasks stay with the chat that created them and the app would not move them, so L1 and L2 were re-created from a Terminal-project chat with the exact live prompts (verified character-for-character against `bees/`), same crons, push notifications, automatic approval. Then, on Alex's "i just want all the lightning L1/2/3 and schedule moved", L3 and the Lisa draft desk the same way. New ids: L1 `trig_01KzwXrQ8gm6nk1bdabZhXXe`, L2 `trig_01Jts5fS2SfSGMYw2ud4QRLK`, L3 `trig_01EWz1aFEbhX9YpLZNACDF8o`, Lisa desk `trig_01RFFUjtxUnUxuGoAczQH39z`. All four run on Fable 5.1 (old L1 and Lisa were Opus 5.5 — Alex to say if he wants them back on Opus). All four old tasks deleted (22:57 UK).
- The watchdog was NOT copied: its prompt carries the filing token, which this chat never prints or moves. It stays live under the Dashboard project. The writer stays there too, same reason.
- First runs: new L2 tonight 23:10 UK; Lisa desk Sat 09:05 UK; L3 Sun 08:40 UK; L1 Mon 07:25 UK.
- Still open: `bees/lisa-desk.md` refresh.
- Evening: the old L1 published almost nothing all week (16 of 28 cards binned by the INTRADAY EXPLAINER class rule, 7 duplicates, 1 approved then blocked by the 5-a-day ceiling). Alex: "turn L1 into breaking news … like Walter Bloomberg", "factual only and no opinion", "no CTA", "why ceiling - if there are 20 that day go for it", "if the headline is stale don't post", "X and Threads only, no Substack". Built `bees/L1-wire.md` as task `trig_015H5pc8hi8a49npJEmpAA8T` (13 runs a weekday, 30 min after each edition, DRAFTS ONLY). Test run 1 at 23:15 UK on the 22:45 edition: 4 headlines cleared by Colette and Lisa (Snowflake $3.75bn convertibles, Eurostat flash inflation, USO and GLD weekly closes), 4 skipped correctly (S&P wrap, VIX, two mid-confidence stories). Goes live on Alex's "go"; the old L1 is then disabled. Record: project doc `claude/newsroom-l1-wire.md`.
- Folder reconnected as `buytrigger-terminal`. GitHub push still blocked (403 with a fresh fine-grained token — repo name or Contents permission; parked for another day).

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
