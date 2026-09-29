# Newsroom surface 2 — Journalism (X · Threads · Substack)

_Built 24–26 September 2026. Work item BTRES-3.7.15. Standing record for surface 2 — update in place. The plan it implements is `claude/newsroom-three-surfaces.md`._

**State at 10:20 UK, Sat 26 Sep: Layer 1 is now AUTONOMOUS — from Mon 28 Sep it drafts, sends each draft through the Colette (copy) and Lisa (marketing director) reviewer agents, and publishes what both approve; kill switch `journalism/config.l1_autopost`. Record: `claude/newsroom-l1-autopost.md`. Layers 2 and 3 stay drafts-only. The two Friday L1 drafts were published Sat 08:43 UK on Alex's instruction (X and Threads, all four live). Two L2 drafts still wait for marketing. The swarm repo package is built and delivered; Alex creates `buytrigger-swarm` and drops it in (`SETUP.md` inside). The CRM counter belongs to the CRM chat — `claude/crm-stage1-handover.md`.**

---

## 0 · The operating rule (Alex, 25 Sep, after the shakedown)

*"a lot of failed posts — you didn't do your homework properly — I am asking marketing team to check — for you if you can come up with creative post put in draft — marketing can review."*

So, on 25 Sep: **Claude drafts into Typefully. Marketing reviews, edits and sends.** No layer auto-posts.

**Revised for Layer 1 only (Alex, Sat 26 Sep, 09:50 UK):** *"yes L1 needs to be autonomous and make sure colette and lisa agent approves before auto post ok."* Layer 1 now publishes on its own after two agent reviewers — Colette (copy chief) then Lisa (marketing director) — both approve; anything either of them does not approve stays a draft for a human with their notes in the scratchpad. Layers 2 and 3 keep the 25 Sep rule. Full record and the live prompt: `claude/newsroom-l1-autopost.md`.

**Ownership rule (Alex, 25 Sep, "we spin off and don't disturb"):** the swarm is its own project. One job = one chat = one branch, named `<job>-<stage>`. A chat reads the project docs list before building; a handover doc with the job's name means the job is taken. The Newsroom chat owns surfaces 2 and 3 only. It does not touch the CRM, the dashboard, member data or the Newsroom site.

## 1 · The three layers

| Layer | What | Platforms | Bee | Schedule |
|---|---|---|---|---|
| **1 · FAST** | a post or 3–5 post thread off a fresh story; **auto-publishes after Colette + Lisa approve (from 28 Sep)** | X + Threads | `trig_01KFVJK2ZFogDj93EojbMFMs` | weekdays 07:25 and 16:25 UK (Alex's setting) |
| **2 · STORY** | one long thread a night, 8–12 posts, with 1–2 charts drawn from claim rows | X + Threads + Substack note | `trig_01MXnELxXcAqhEg9ffUBqnA8` | weekdays 23:10 UK |
| **3 · ARTICLE** | the week's trend as an 800–1,100 word Substack draft with 2–3 charts | file + doc for Alex to edit | `trig_018ybEdaU9BaHRYu2yFDWgRh` | Sundays 08:40 UK |

Typefully tags: `newsroom` on everything, plus `layer-1` / `layer-2`. Draft titles start `L1 ·` or `L2 ·`, with `[STOCK]` when a ticker is named so the reviewer looks harder, and `· also L1 today` when Layer 2 had to take a story Layer 1 already drafted.

**Graphics decision (Alex, 24 Sep): charts and data only.** Number graphics are drawn by code from claim rows. Pictures with no numbers are a hand tool, not a bee.

**The prompts are files.** `bees/L1-fast.md`, `bees/L2-story.md`, `bees/L3-article.md` in the swarm package are the exact text of the three tasks (L2 as updated 26 Sep). **The L1 file in the package is now out of date:** the live L1 prompt (autopost version, 26 Sep 10:10) is in `claude/newsroom-l1-autopost.md` and must replace `bees/L1-fast.md` when the swarm repo is populated. Change the file, then push it to the task.

## 2 · The gates every bee applies

1. **Class** (Layer 1) — Evergreen Pack, Breaking Post, Closing Recap. Intraday Explainers out.
2. **Window** — still inside `created_at + life_s`; a Breaking Post needs 15 minutes left.
3. **Story** — `VERIFIED` at level `ok`; later editions read for a `correction` that withdraws it.
4. **Claims only** — no number in a post or on a chart unless it is a claim row at `ok` or `sec`. Nothing researched, fetched or recalled. Layer 2 now runs a number check by code before creating the draft; the same check is `tools/verify_numbers.py` in the package.
5. **Dedupe** — same angle → freshest wins; two per story per day; three drafts a day (Layer 1); one a night (Layer 2); one a week (Layer 3). **Cross-layer (added 26 Sep):** Layer 2 prefers a story Layer 1 did not draft that day; if it must take one, the title says so and the scratchpad tells marketing to send one or the other.
6. **Voice** — `alex-voice`; free tier; never a BuyTrigger/ValueTrigger level; never an invented position.
7. **FCA** — `fca-check` on every post standalone; RED → no draft. A stock named → a not-advice line in the same rendering (Layer 2 X: last post; Threads: before the link).
8. **Platform rules learned 24 Sep** — X text carries **no URL and no bare domain** (X refuses app-published posts with links; sources named in words, "on the BuyTrigger Newsroom"). Threads posts **≤ 450 characters, plain punctuation** (two 494-character posts with arrows and em dashes failed; cause not confirmed by Typefully). Threads and Substack links carry `utm_content=<edition>-<card>` or `l2-<date>` so each post gets its own line in the CRM once its counter is live.
9. **Publishing.** Layers 2 and 3: never — no `publish_at`, `plan_at` or `confirm_publish`. Layer 1 (from 28 Sep): publishes only a draft it created in that run, only after Colette APPROVE and Lisa APPROVE, only while `journalism/config.l1_autopost` is `true`; never `plan_at`, never a retry after a one-platform failure, never another draft.
10. **Review desk (Layer 1, added 26 Sep)** — Colette checks voice, hook, reader clarity and every hard rule, and may FIX once (numbers untouched) or REJECT; Lisa makes the send decision: FCA standalone (RED or AMBER → HOLD), stricter bar for a named stock, nothing about Alex, dedupe against the last 48 hours, freshness, tags, brand risk. Reviewers get the text and the claim rows; they use no tools and do no research.

## 3 · Where things live

| Piece | Where |
|---|---|
| Ledger | private page `MGGZNGHSGWtAGwo3kZNxZn`, collection `journalism`: one doc per edition (`drafted{}`, `rejected{}` per card, with reasons and draft ids), plus `<date>-L2` and `<date>-L3` docs. Snapshots in the package under `ledger/` |
| Drafts | Typefully set `dralexkoh` (273686), tag `newsroom` |
| Charts | `/mnt/user-data/outputs/newsroom-layer2-<date>/` in the run's chat; shakedown charts also in the dashboard repo `Claude outputs/newsroom-layer2-2026-09-25/` |
| The swarm repo package | `buytrigger-swarm-package-2026-09-26.tar.gz` — in the chat and in the dashboard folder under `Claude outputs/` (untracked). Contents: README, SETUP, `bees/` (three prompts + schedule), `rules/` (gates, platforms, voice and compliance, ownership), `tools/` (verify_numbers, check_lengths, score_stories), `charts/` (branded library + worked example), `schema/` (collections, ledger, a one-source SQL proposal for the Research project), `ledger/` and `fixtures/` (real exports), `docs/LOG.md` |
| Counter | **not this project's.** The CRM chat's package: `claude/crm-stage1-handover.md`. The Newsroom chat's duplicate sits in the dashboard repo under `_to_delete/crm-stage1-withdrawn-2026-09-25/` for Alex to delete; local branch `crm-stage1` — `git branch -D crm-stage1` in Terminal |

## 4 · What happened (the record)

**Shakedown, 20:45 UK 24 Sep.** Five Layer 1 drafts from the eight live evergreen cards; three cards collapsed as duplicates; one held ($SCHW).

**Sent, 23:38 UK 24 Sep**, on Alex's "anything layer 1 start shooting them out": four macro threads to X and Threads. X: 4 of 4 live. Threads: 2 of 4 live, 2 failed with no reason from Typefully, one retry also failed. Alex's verdict the next morning: too many failures, marketing reviews from now on.

**Layer 2 shakedown, 12:20 UK 25 Sep.** Draft 10922651 — "The cost of money reset this week" — 11-post X thread, 4-post Threads thread, Substack note, two charts. Charts delivered as files because the upload host is blocked.

**CRM duplicate, 12:30–13:00 UK 25 Sep.** Built without noticing the CRM chat had already filed its handover at 12:12. Withdrawn; the CRM chat's stands.

**First unattended runs, Fri 25 Sep.** Layer 1 at 16:25: two drafts — 10926756 (Robinhood CEO Form 4, `[STOCK]`) and 10926758 (AI capex beat) — with full evidence chains, FCA logged, ledger written. Layer 2 at 23:11: one draft — 10931326 (Robinhood, insider sale: divide, don't read) — two charts as files, ledger `2026-09-25-L2` written.

**Audit, Sat 26 Sep 07:00–07:45 UK.** Every number in the three bee drafts checked by script against the `ok`/`sec` claim rows: 14, 11 and 49 numbers, all trace; no correction in the 22:30 edition touches those stories. Two compliance edits to 10931326: X post 10 ends "Not advice, not a view on the stock."; Threads post 4 carries "Not advice." before the link. Its scratchpad says so and warns marketing that 10926756 covers the same filing. Layer 2 picked the same story as Layer 1 → cross-layer rule added to the L2 prompt (live from Monday's run). The selection arithmetic run on Friday's exports (`tools/score_stories.py`) shows Oracle would have scored 64 across nine editions — with a correction filed at 22:30 that the bee must honour — ahead of Micron 57 and Robinhood 40: the bee's grouping under-counted recurring subjects; the prompt's "group by subject across editions" wording is now explicit.

**Sent, 08:43 UK Sat 26 Sep**, on Alex's "Publish both now" in the Cowork chat (he had asked why the L1 drafts sat unsent): 10926756 (Robinhood Form 4) → X 2103752150849601790, Threads DdvhlhPG-YX; 10926758 (AI capex beat) → X 2103752190217355470, Threads Ddvhmm6mxR0. Threads accepted both cleanly — four in a row under the 450/ASCII rule. Ledger updated with URLs and "published by Claude on Alex's instruction".

**Policy change, 09:50–10:20 UK Sat 26 Sep.** Alex: "L1 needs to be autonomous and make sure colette and lisa agent approves before auto post." Task `trig_01KFVJK2ZFogDj93EojbMFMs` re-prompted and renamed; kill switch doc `journalism/config` created (`l1_autopost: true`); decision record `claude/newsroom-l1-autopost.md`. First autonomous run: Mon 28 Sep 07:25 UK.

**Still in Typefully as drafts:** 10922651 (L2, rates week) and 10931326 (L2, Robinhood — now a duplicate of the published L1 thread; marketing should pull or hold it). 10913768 and 10915651 were deleted by someone.

## 5 · Alex's actions

| # | Action | Why |
|---|---|---|
| 1 | **Create the repo `buytrigger-swarm`**, clone it next to the dashboard, drop the package in, connect the folder to the swarm chat — `SETUP.md` in the package, five steps | Claude cannot create repos; once the folder is connected the swarm chat works there directly |
| 2 | **Allow the domain `typefully-user-uploads.s3.amazonaws.com`** in Claude's allowed domains | until then no bee can attach a chart; marketing attaches the PNGs by hand from the scratchpad's instructions |
| 3 | Put the tagged links in the X and Threads bios (`utm_source=x|threads&utm_medium=bio`) | X posts can't carry links, so the bio is X's only measurable door |
| 4 | Tell marketing: L1 now publishes itself after the Colette + Lisa desk; marketing's job on L1 is the HELD drafts (notes in the scratchpad) and the morning check that L2's draft does not repeat what L1 sent. L2 drafts still need a human send: 10922651 (rates week) is ageing; 10931326 (Robinhood) duplicates the L1 thread sent Sat 08:43 — pull or hold it. Charts for both are files in the chat / repo folder | |
| 5 | In Terminal, in the dashboard repo: `git branch -D crm-stage1`, delete `_to_delete/crm-stage1-withdrawn-2026-09-25/` | tidy-up of the withdrawn duplicate |
| 6 | CRM Stage 1 go-live — with the CRM chat | conversion is uncounted until it runs |
| 7 | Confirm the Layer 1 schedule: two runs a day (07:25, 16:25) is what is set; the task is still named "4x" | changed by someone other than the Newsroom chat on 25 Sep |

## 6 · Open items

| # | Item | Owner |
|---|---|---|
| 1 | First Layer 3 run, Sun 27 Sep 08:40 UK — read its report; the rates week or Oracle are the candidates | Claude → Alex |
| 2 | Monday's runs: **Layer 1 07:25 — first autonomous run: did Colette and Lisa both run, what was published, what was held and why** (notification + ledger `reviews{}`); Layer 2 23:10 with the new prompt — check the cross-layer rule fired and the number check ran | Claude → marketing |
| 3 | Populate `buytrigger-swarm` directly once the folder is connected; from then on prompt changes go file → task | Claude |
| 4 | One source: move the desk cards and the `journalism` ledger into the Research Supabase project (`schema/supabase/swarm_one_source.sql` in the package, not yet run), then repoint the bees | Claude → Alex |
| 5 | Threads failure cause: watch whether the ≤450/plain rule holds over a week | Claude |
| 6 | Weekly numbers note from the CRM's daily view once the counter is live | Claude |
| 7 | Cadence and caps review alongside the trial-week counts | Claude → Alex, Sunday |
| 8 | Surface 3 (shorts, Instagram, video) not started | — |

## 7 · Standing rules for surface 2

- **Layer 1 publishes after Colette and Lisa both approve; Layers 2 and 3 are drafts, marketing sends.** No bee sets `plan_at`. L1's `confirm_publish` rests on Alex's standing authorisation of 26 Sep and is switched off by `journalism/config.l1_autopost: false`.
- **The ledger is the truth.** A card under `drafted` or `rejected` is finished. Every reason is written down so the algo is tuned from evidence.
- **Claims only.** Not in a claim row at `ok` or `sec` → not in a post, not on a chart. Derived numbers are declared.
- **Corrections first.** Later editions are read before anything is drafted.
- **No URLs in X text. Threads ≤ 450, plain.** Links on Threads and Substack carry `utm_content`.
- **One story, one layer, one day.** Layer 2 avoids Layer 1's stories; when it can't, it says so.
- **Bees write to `journalism` only.** Never `desk`, `editions`, `notes`, `os`, never the Daily Brief task.
- **Nothing about Alex** — positions, trades, holdings, subscribers, revenue — in any post.
- **Stay in lane.** The swarm never touches the dashboard repo's `src/`, member tables, the CRM or the Newsroom site. One job, one chat, one branch. Prompts are files in the swarm repo.
