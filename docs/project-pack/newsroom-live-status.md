# BuyTrigger Newsroom — live status, trial week and frequency plan

_Standing record, opened 24 September 2026. Last updated 29 September, 16:30 UK (§00d outage review, watchdog, writer self-check, change-control rule). Before that 12:20 UK (§00c thirteen runs, Opus 5.5, shorter corrections, Fable for L3; §00b the corrections and the RISKY CLAIMS rule; §00a the AMD miss and the news sweep). Before that: 28 September evening (§00 coverage fix and wire on; §2; §5 items 2, 14, 15; §6 lesson 7) and 27 September, Sunday review. Work item `BTRES-3.7.15 — Agentic Newsroom`. Written by Claude (Marissa / OS Control). Not a close-out: the work item stays open through the 4.0 release and the frequency decision. This doc carries what is true right now — update it in place._

---

## 00 · Coverage fix and wire on — 28 September (Alex present)

**Alex, 28 Sep, 18:30 UK:** *"the dashboard and desk is not giving news on meta and nu — we need to tweak what's being researched, not just nvidia and hood — fix it."*

**Cause.** Not the dashboard. The writer (the Daily Brief task) only ever researched a handful of names: every edition from 24 to 28 September played Micron, Oracle, Bloom Energy, Nvidia and Robinhood, often with filler ("has filed nothing", "no news behind it"). Meta and Nu never appeared, so the Desk had nothing to put on members' Meta or Nu rows. The Desk's matching code was tested against stories naming Meta, Meta Platforms, Facebook, Nu Holdings, Nubank and $NU — all match, with or without a `tickers` field. The stock-page Research Desk (weekly filings briefs) already covers all 119 names and was not the cause.

**The change** — the writer's prompt, edited with `update_trigger` at 17:42 UTC, read back byte-identical, schedule and filing-token line untouched. Task renamed "BuyTrigger Daily Brief (Claude) — every 2h weekdays, files to the Newsroom (whole universe + wire on, 28 Sep)".
1. **COVERAGE** — the watchlist is now the whole BuyTrigger universe (119 tickers, snapshot 28 Sep, listed in the prompt). It overrides any shorter watchlist in the HQ doc `claude/daily-brief-profile.md` (not editable from this project).
2. **Top ten every run** — NVDA NU CRDO JPM META UBER NFLX ADBE AAPL GEV (snapshot 28 Sep, from the free-tier top ten): price move, releases, EDGAR including 6-K/20-F for foreign filers, dated catalysts.
3. **Rotation** — the other names in turn: slot n of the day checks universe positions with remainder n mod 9 (about 13 names a run), so every name is checked once each weekday. Plus any universe name moving 3% or more.
4. **FAIR SHARE** — a name is a story only when something new happened; "filed nothing" / "no news" stories are out except once a day before results; no name more than three editions in a row without a new number.
5. **`tickers` on every story** — universe tickers only, main one first; [] for stories naming no universe stock. Closes item 14.
6. **THE WIRE switched on** — Alex's 22–26 Sep pause had ended but the prompt still said PAUSED (item 2). Wording as prepared in §0.
7. Step 5's heading now says `buytrigger.club` (half of item 15).

**Result — the 20:30 UK edition, filed 19:47 UTC (first run on the new prompt).** 12 stories, every one carrying `tickers`. Lead: *Meta's new business software sends the market to its low of the day*. Stock stories: **Nubank falls 10% on reports it may buy Britain's Monzo** (NU), **Meta launches business AI tools and hires a rival's chief executive** (META, NOW), Boeing −6% (BA), Credo −8% after a co-founder sale (CRDO), Apple's $5.7bn award (AAPL), chip and laser makers (AMD, COHR, SNDK). Four WIRE stories. No Micron, Oracle, Bloom Energy or Robinhood filler. Numbers check: 34 re-fetched, 16 changed, 5 dropped. Levels: 10 stories `ok`, 2 `mid` (Boeing wire-sourced, Credo single source). Desk matching on this edition lights up META, NOW, BA, JPM, WFC, NU, CRDO, AAPL, AMD, COHR, SNDK.

**No dashboard code changed; nothing to push.**

**Watch next:** Tuesday's full day — does the rotation reach the whole universe, does the run time grow (20:30 took ~17 minutes, fire to file), and does the pre-open `mid` rate (§3b) get better or worse with more names to check. The universe and top-ten lists are snapshots: update the prompt's COVERAGE lines when the sheet adds or drops names or the top ten changes (§6).

## 00a · The AMD miss and the news sweep — 29 September (Alex present)

**Alex, 29 Sep, ~10:20 UK:** *"AMD buying another company — did you capture that big news? If not, why did the algo not pick it up?"*

**What was missed.** AMD announced an $8.2bn all-stock deal to buy World Labs (Fei-Fei Li's AI lab) at **16:05 ET / 21:05 UK on Mon 28 Sep**, after the US close (company release on GlobeNewswire and ir.amd.com). The 22:30, 06:30 and 08:30 editions all missed it. The 20:30 edition, filed 20:47 UK, had said AMD fell "with no news behind it" — true at the time, 18 minutes before the release.

**Why.** The 28 Sep rules found company news three ways only: the top ten every run, the rotation (each name once a day), and 3%+ movers. AMD fell through all three: not in the top ten; its rotation slot (slot 7 = the 20:30 run) had already passed; after hours the shares moved about +0.1%. A big announcement that does not move the price was invisible outside the name's rotation turn.

**The fix** — prompt edited with `update_trigger` at 09:25:58 UTC, 4½ minutes before the 10:30 run; read back byte-identical, schedule and token line untouched. Two additions:
1. **(0) NEWS SWEEP, first, every run, the whole universe** — the SEC latest-filings list (8-K and 6-K since the previous edition) plus the press-release wires and the day's news, for MATERIAL EVENTS: buying or being bought, merger, stake, spin-off; results, guidance, results date; CEO/CFO change; large contract won or lost; buyback, share or debt raise; regulator, court or government decision; a wire-carried product launch. A material event is a story whatever the price did, and outranks a "no news" price move. The 22:30 and 06:30 runs sweep the whole after-hours window from 21:00 UK.
2. **Late catches count** — a material event from the last 24 hours that no edition has carried is still new; carry it and say when it was announced.

**Result — the 10:30 UK edition, filed 10:50 UK (first run on the new rules).** Story: *AMD is buying Fei-Fei Li's World Labs for $8.2 billion in shares*, `tickers: ["AMD"]`, level `ok`, sourced to ir.amd.com (status `ok`, "28 September 2026, 4:05pm EDT") plus Yahoo Finance for price, and the dek says plainly "This page did not carry it yesterday and should have." The sweep also caught two other material events no price screen would have: **Snowflake's $3.75bn zero-coupon bond raise** (SNOW) and **Raytheon's $20.7bn missile order** (RTX). 13 stories, every one with `tickers`; four WIRE stories; a correction leading (Nubank and Credo, not Meta, fell hardest on Monday). Numbers check: 14 re-fetched, 3 changed, 4 dropped.

**Watch next:** whether the sweep stretches run time (10:30 ran ~19 minutes, fire to file) and whether the edition grows too long (13 stories, against 7–9 before 28 Sep) — if so, cap stock stories per edition rather than drop the sweep.

## 00d · Outage review and safeguards — 29 September, 16:30 UK (Alex present)

**Alex, 16:20 UK:** *"did the newsroom and desk die? this is business critical and make sure this doesn't happen again … if it's opus or fable — give me recommendation so this doesn't ping out."*

**What happened.** Neither site went down — buytrigger.club and the dashboard stayed up and showed their last good edition throughout (the dashboard was checked live at 16:24 UK: login page up; Alex's push of `192690cba` deployed at 16:23 UK, the Desk chunk carries the new slot times). **The news stopped updating twice:** 13:50–14:26 UK (13:45 edition stuck on the private page until posted by hand) and 14:50–15:57 UK (14:45 edition, same). About 1 h 40 min of stale news in total, on top of the planned 10:45 → 13:45 gap in the new schedule. **Cause:** the writer was moved to Opus 5.5 at 12:11 UK without a test run; both Opus 5.5 runs ended in under 5 minutes, wrote thin editions to the private page and skipped step 5. The change process was the failure, not the site.

**Safeguards now live:**
1. **Writer back on Opus 5** (14:57 UTC) — 40+ runs last week and today, every one posted. 15:45 UK edition posted by itself.
2. **Writer self-check** (prompt edited 15:26 UTC, read back byte-identical): step 5 is marked REQUIRED; after posting, the run reads the public feed back with the public read key, retries once if its edition is missing, and its final reply starts "PUBLIC: OK <id>" or "PUBLIC: FAILED <id> — …".
3. **Watchdog task** `trig_016riCgZvbeVLBsUMpC5HoF9`, created 15:27 UTC — `CRON_TZ=Europe/London 35 7,9,11,14,15,16,17,18,19,20,21,22,23 * * 1-5` (50 minutes after each writer slot). Each run: reads the public feed, the withdrawn list and the private page; posts any of today's editions that are on the private page but not public (unchanged document, never a withdrawn one); checks the due slot produced an edition at all; replies OK / FIXED / ALERT in one line. **Push notifications on** — FIXED and ALERT lines reach Alex's phone. Carries the filing token (rotate it here too at the public push). Created on the account default (Opus 5.5); **moved to Opus 5 at 15:31 UTC, before its first run (16:35 UK)**, on Alex's "go — accepted your recommendations".

**Model recommendation — accepted by Alex, 29 Sep 16:30 UK:** anything that publishes live on a schedule — the Newsroom writer and the watchdog — stays on **Opus 5**, the proven model. **Fable 5.1** for the big, non-live work: the weekly article (L3), builds, reviews. **Opus 5.5** is not used for the writer until a test copy shows it completes the run and posts. L1 (Opus 5.5) has published correctly since 26 Sep and is left as is.

**New standing rule — change control for live automations:** never change the model, schedule or publishing step of a live Newsroom task without a test first: run a copy of the task with step 5 removed (it posts nothing public), read its private-page edition and run length, and switch the live task only after two good test runs. Then watch the first live run end to end (private page AND public feed).

---

## 00c · Thirteen runs, Opus 5.5, shorter corrections — 29 September (Alex present)

**Alex, 29 Sep, ~12:10 UK:** *"ok we are increasing frequency — i want opus 5.5 … I want fable for bigger things like build or article."* Earlier the same hour: *"honesty is good, but it takes up space."* (He overrode the §4 recommendation to keep nine runs; frequency is his call.)

**Changed at 11:11 UTC**, one `update_trigger` call, read back byte-identical, token line untouched:
- **Schedule** — `CRON_TZ=Europe/London 45 6,8,10,13,14,15,16,17,18,19,20,21,22 * * 1-5`: **13 runs a weekday** — 06:45, 08:45, 10:45, then hourly 13:45 → 22:45 UK. London-time cron, so the times hold through the 25 Oct clock change. The 13:45 run lands 15 minutes after the 13:30 UK US data releases (the §3c miss). First run: 13:45 UK, 29 Sep.
- **Model** — Opus 5 → **Opus 5.5** (`claude-opus-5-5`). There is no effort (high/extra) setting on scheduled tasks from this tool; it runs at the default.
- **Prompt** — run times, Morning baseline 06:45, catalysts at 22:45, after-hours sweep at 22:45 and 06:45; ROTATION now mod **13** (about nine names a run, each name still once a weekday); hourly runs must file within 40 minutes and file short rather than pad; **CORRECTIONS are now the third story (after MARKET and VIX), two sentences** — still tagged CORRECTION, still honest, less space.
- Task renamed "BuyTrigger Daily Brief (Claude, Opus 5.5) — 13 runs weekdays 06:45–22:45 UK, files to the Newsroom".

**Fable for the bigger work (Alex):** L3 weekly article bee `trig_018ybEdaU9BaHRYu2yFDWgRh` moved Opus 5.5 → **Fable 5.1**, and its read limit raised from 45 to 70 editions a week. L2 story bee was already on Fable 5.1. L1 fast posts and Lisa stay on Opus 5.5.

**Dashboard follow-up (Desk "next edition" label):** `EDITION_SLOTS_UK` in `src/utils/desk.js` → the 13 new slots; `desk.test.js` and `desk.test.jsx` updated (fixture 17:33 BST → "NEXT EDITION 17:45"). Cloud copy: **416 tests pass, build clean**. Committed on local `main` on the Mac as **`192690cba`** at 14:58 UTC (the first attempt at 11:15 UTC was lost when the Mac dropped off the bridge; redone after Alex's Mac had pulled the data bot's 11:52 commit). Alex pushes: `cd "$HOME/Desktop/GitHub Project/buytrigger-dashboard" && git pull --no-rebase --no-edit && git push origin main`. Until pushed, the Desk's "next edition" shows the old times; nothing else is affected.

**Usage:** 13 runs on Opus 5.5 instead of 9 on Opus 5 — clearly more usage per day. Alex: "tokens ok usage ok". Levers if it bites: cap stock stories and wire items per edition before cutting runs.

**First run on Opus 5.5 — 13:45 UK, 29 Sep: problem.** Fired 12:46 UTC, finished 12:50 UTC (4½ minutes, against ~20 on Opus 5). It wrote a thin edition to the private page (6 stories: MARKET, VIX, one stock story — Novo Nordisk's $300m obesity-pill licence — and three WIRE; numbers check refetched only 3) and **did not post it to the public feed** (step 5). The token and the endpoint are fine: Claude posted the same document by hand at 13:26 UTC → 200 `{"ok":true}`, live on buytrigger.club and the Desk. Cause not known — the run's transcript is not readable from here, and `newsroom_filings` is not publicly readable. Only the model changed on step 5's path, so the model is the first suspect. **14:45 UK repeated it**: fired 13:46, finished 13:50 UTC (under 5 minutes), 7 stories, 6 numbers re-fetched, private page only — posted by hand at 14:57 UTC (200). **Model reverted to Opus 5 at 14:57 UTC** on Alex's "ok" (he had been asked: if 14:45 repeats, switch back to Opus 5 while the cause is found). Schedule, prompt and token unchanged. Task renamed "… (Claude, Opus 5) — 13 runs …".

**Correction (16:35 UK): the 15:45 run did NOT post by itself.** The scheduled run (fired 15:00, finished 15:06 UTC) also held step 5. The 15:45 edition (as_of 15:20 UTC on both the private page and the feed) was filed by that run's session after Alex opened it in the app and talked to it — the "BuyTrigger Daily Brief" chat Alex asked about. So the fault was not only Opus 5.5.

**Likely root cause (found by that run's own session):** the prompt ended with the hard rule "You never publish, post, message, schedule or trade", which contradicts step 5 "PUBLISH IT TO THE PUBLIC SITE". Runs resolved the conflict by holding step 5; a held run could also record a "proxy-blocked" blocker in `daily-brief-latest.md` that the next run believed. It worked all last week on Opus 5 — the new model and the 29 Sep edits tipped runs into the stricter reading. The run's session could not edit its own task (guardrail); **edited from this session at 15:34 UTC** (read back byte-identical, 10 minutes before the 16:45 run): the last sentence now says steps 4 and 5 are the configured, authorised output of every run and only other publishing is forbidden; a new paragraph "STEP 5 IS AUTHORISED AND NOT OPTIONAL … never record a blocker you did not actually hit this run"; and setup step 2 now says a previous edition's "step 5 blocked / proxy-blocked" note is to be ignored. Model stays Opus 5.

**To try Opus 5.5 again later:** the cause must be found first — read one Opus 5.5 run's transcript (sessions `cse_01TMfRLArVdrBJwkSfmjThXA` 13:45 and `cse_01XtxsZ2oNDB7GJamLhhB8Lc` 14:45, from the scheduled task's run history) to see whether it refused the step-5 POST, lost network, or ended early. Both runs were also far shallower (under 5 minutes against ~20), so the sweep and rotation were not being done either.

**Knock-ons checked:** L1/L2/L3 and Lisa prompts have no hard-coded edition times; L2 at 23:10 UK may start before the 22:45 edition has filed (22:45 run + ~20 min) — it then works from the 21:45 edition; acceptable, watch it.

---

## 00b · Why so many corrections — 29 September (Alex present)

**Alex, 29 Sep, ~12:00 UK:** *"why is there a lot of correction type posts?"*

**The count.** 5 corrections in 27 editions (24 Sep 12:30 → 29 Sep 10:30) — about one edition in five leads with one. **None was a wrong price.** All five were claims about WHEN, NOTHING or MOST:
1. 25 Sep 14:30 — August new home sales listed as "still to come" when Census had published them the day before (WHEN, from habit).
2. 25 Sep 22:30 — "Oracle has filed nothing since 23 Sep", read from a stale SEC copy (NOTHING).
3. 28 Sep 08:30 — "the VIX will not print until 14:30 UK"; it is published from 08:00 UK. Second time in eight days (WHEN, fixed fact).
4. 28 Sep 22:30 — "Robinhood's September figures due tonight at 21:05"; no such release had been announced (WHEN, invented time).
5. 29 Sep 10:30 — "Meta's fall was the biggest among the top ten"; Nubank and Credo fell further (MOST, set not fully checked).

**The fix** — prompt edited with `update_trigger` at 10:59 UTC, read back byte-identical, schedule and token line untouched. New section **RISKY CLAIMS** before the numbers check: every WHEN claim needs the official calendar or the company's own announcement fetched that run (no times from habit, memory or earlier editions; none on unannounced releases); every NOTHING claim needs two EDGAR routes to agree (submissions JSON and the filing list) or is reworded to "the latest filing I can see is…"; every MOST claim needs the whole named set checked and named; FIXED FACTS for the VIX hours and company monthly figures. Corrections stay first when a mistake does get through — the honesty rule is unchanged; the aim is fewer mistakes.

**Measure:** corrections per edition over the next full week (baseline 5 in 27). Open item 4, the second independent checker, is still the stronger fix if the rate does not fall.

---

## 0 · Sunday review — 27 September

_Superseded in part on 28 September: the wire edit below was made by Claude with Alex present (§00). The frequency recommendation stands._

**The wire is still paused, and I could not switch it on.** Editing the Daily Brief task's prompt was refused by this session's permission settings — twice, on two different routes. Monday's 06:30 editions will ship without wire stories unless you make one edit yourself. It takes two minutes. Open the task, find the paragraph beginning `THE WIRE — PAUSED`, and replace that whole first sentence with:

> THE WIRE — ACTIVE. The 22–26 September pause is over, lifted 27 September. Every edition carries wire stories under the rules below:

Then delete two leftover qualifiers further down: `only while the wire is active: ` in the output template's "The wire" line, and `(only when the wire is active) ` in the story-order rule. **Leave the `NEWSROOM_FILE_TOKEN` line exactly as it stands, and change nothing else — not the schedule, not the model, not step 5.**

**What the week showed.** The feed only began recording at 11:43 UTC Thursday, so this is one and a half trading days — 15 editions — and the wire was off for all of it. Every scheduled slot filed: 9 of 9 on Friday, 6 of 6 on Thursday after step 5 went live. No run came back empty. Errors: two corrections in 15 editions, 12 stories at `mid` confidence, 25 of 661 claims flagged. They cluster in the quiet hours — pre-open editions run 18% mid-level stories against 8% in the US session, and the 10:30 edition alone shipped 3 of its 7 stories at mid. The real gap is timing: the 13:30 UK data print was caught 73 minutes late on Thursday and 87 minutes late on Friday.

**Frequency — I recommend against going to thirteen runs.** Coverage was not what failed. Nothing was missed for want of a run, and the largest index move on each day already had a run at the end of it. What failed was accuracy when there was little to report, and four more runs a day add four more thin editions, which is exactly where the errors live. Both of your own pre-conditions are also unmet: the error count is not low, and the second checker is not built. Move one run instead — to 13:45 UK, fifteen minutes after the print.

**Yours to decide:** ~~the wire edit above~~ (done 28 Sep, §00), and whether to take nine runs with the 13:45 move now, or hold the cadence untouched until a full wire-on week has been measured.

---

**The address moved on 24 September.** The Newsroom is now the main site at **`buytrigger.club`**. `news.buytrigger.club` has been **deleted** and no longer resolves. Any earlier doc saying the channel lives at `news.buytrigger.club`, or that the address switch happens on 19 or 26 October, is superseded by this line.

**Surface 2 (the posts) has its own record:** `claude/newsroom-journalism.md` — three bees, drafts only, marketing sends. The swarm is spinning off into its own repo.

**The member-side twin:** the dashboard's Desk (`dashboard.buytrigger.club/desk`, 3.18, live 25 Sep as v3.9.0) reads this feed read-only and shows members the evidence the public page withholds. Record: `claude/member-desk-phase1-status.md`.

---

## 1 · The address map as it stands

| Address | What it serves | Host |
|---|---|---|
| **`buytrigger.club`** | the Newsroom — free, no login, the front page | GitHub Pages, repo `dralexkoh/buytrigger-newsroom` |
| `www.buytrigger.club` | follows the bare domain | CNAME → `buytrigger.club` |
| **`buytrigger.club/join/`** | the sales page (3.17, live 24 Sep ~17:50) — form to Alex's inbox via Formspree | same repo, `join/index.html` |
| ~~`buytrigger.carrd.co`~~ | retired 24 Sep (3.17 close-out) | — |
| `dashboard.buytrigger.club` | the member product — the only login door | GitHub Pages, repo `buytrigger-dashboard` |
| `dralexkoh.substack.com` | the free letter — the one capture door | Substack |
| ~~`news.buytrigger.club`~~ | **deleted 24 Sep** | — |

DNS is at **Porkbun**. The apex carries four A records — `185.199.108.153`, `.109.153`, `.110.153`, `.111.153` — replacing Carrd's `172.66.0.70`. No Cloudflare anywhere in this path.

**Top bar:** `SUBSTACK` → the letter · `LOG IN` → `dashboard.buytrigger.club` · `JOIN THE CLUB` → `buytrigger.club/join/` (repointed 24 Sep by 3.17; Carrd retired).

**Enforce HTTPS is now on** (Alex, by 26 Sep). The 24 September note about the greyed-out tick is closed.

---

## 2 · What is live

| Piece | Where | State |
|---|---|---|
| The page | `buytrigger.club`, GitHub Pages | live over HTTPS, Enforce HTTPS on |
| The feed | Supabase **Research** project `paoxcmxteemakhyvwihn`, table `newsroom_editions` | live, RLS on, public read where `withdrawn = false` — **verified by read, 28 Sep** |
| The write door | Edge Function `newsroom-file`, Verify JWT off, bearer token | live — file · checked · withdraw |
| The writer | Scheduled task `trig_01MnsDBLPFNiHguXRQjFPohq`, cron `CRON_TZ=Europe/London 45 6,8,10,13,14,15,16,17,18,19,20,21,22 * * 1-5`, **thirteen runs a weekday, Opus 5.5** (from 29 Sep, §00c) | live; whole-universe coverage, news sweep, `tickers` per story, wire on, RISKY CLAIMS check, short corrections (§00–00c) |
| Network permission | `supabase.co` and `*.supabase.co` in Claude's allowed domains | done |
| The private page | Claude artifact `MGGZNGHSGWtAGwo3kZNxZn` | Alex's desk. A version behind on cosmetics only |

### The chain

```
scheduled run (every 2h, weekdays)
  → writes the edition to the Claude page          (step 4)
  → POSTs the same document to newsroom-file        (step 5)
      → upserts newsroom_editions, logs newsroom_filings
buytrigger.club
  → renders the baked snapshot instantly
  → fetches the feed every 60s and on tab focus
  → replaces the snapshot when rows come back; keeps it when they do not
```

**First unattended filing: 24 September, 11:43 UTC**, edition `2026-09-24-1230`, live on the public page within a minute. No human involved between the run writing and the page updating.

### 2a · Phone header change — 25 Sep, 22:00 UK (Alex, from his phone: "five lines before the headline")

Committed on the newsroom repo's `main` as `c8f502a` by the Desk chat (Alex to push; a fast-forward on top of GitHub's `2f1b01a`). At ≤620px only: the rolling pill and filed time sit on the brand row (date and age hidden there, kept wider); the three buttons share one row; the PREVIEW ribbon folds into the legal line at the foot ("Preview · 4.0 opens 5 Oct."); the new-edition toast is one line; the check label shows its first word (VERIFIED / CORRECTED). The headline starts about 115 px higher on a 390 px phone. Desktop and tablet unchanged; both inline scripts parse. Before/after render in the Desk chat's outputs. **Whoever next edits `index.html` (the writer's snapshot bake or the Newsroom chat): pull first — this commit changes `renderFresh`, `renderStory`'s `.conf` span, the `.legal .narrow` text and appends a phone `@media` block before `</style>`.**

---

## 3 · The trial week — measured 27 September

**Mon 24 Sep → Wed 1 Oct.** Review 1 Oct, changes effective 2 Oct, settled before the 5 October early-bird opening. **Note (28 Sep):** from the 20:30 UK run on 28 Sep the editions carry the wire and whole-universe coverage, so the 1 Oct review compares two different products; measure the wire-on editions separately.

**How much evidence there actually is.** Step 5 went live at 11:43 UTC on Thursday 24 September, so the feed holds **Thursday midday onwards only — 15 editions across one and a half trading days**, not a week. Monday 21 to Wednesday 23 September ran but could not post and are not measurable from the feed. **THE WIRE was off for every one of these 15 editions**, so these numbers describe a product that is about to change shape. Read everything below as an early indication, not a settled trial result.

Read 27 September from `newsroom_editions` (`withdrawn = false`, newest 60). Newest row: `2026-09-25-2230`, filed Friday 25 September 21:40 UTC — **about 40 hours old at the time of reading, which is correct**: the cron is weekdays only, so Friday 22:30 UK is the last run before Monday. The public page `buytrigger.club` could not be fetched from this session (403 at the proxy — an allowlist limit, not a fault with the site).

### 3a · Signal rate

| Day | Slots with a row | New edition filed | Re-stamped an existing one |
|---|---|---|---|
| Thu 24 Sep (from 12:30) | 6 of 6 | 6 | 0 |
| Fri 25 Sep | 9 of 9 | 9 | 0 |

**Every run filed its own edition. Not one run came back with "no material change."** 15 distinct `edition_id`s across 15 rows. The writer rewrites every edition from scratch rather than carrying stories forward, so there is no repeated text to discount. This is the finding that most bears on frequency, and it cuts **for** the proposal, not against it: the argument "most runs come back with nothing" is not true on this evidence.

One defect found: the top-level `checked_at` column is **null on all 15 rows**. The per-edition numbers check lives inside `doc.checked` and is populated, so nothing is lost, but the column the page reads for its "CHECKED <time>" label is never written. Worth a look before 4.0. (Still null on every 28 Sep row, including 20:30.)

### 3b · Error rate

| Measure | Count |
|---|---|
| Editions | 15 |
| Stories | 109 |
| Stories at `level` **mid** | **12** (11%) |
| Stories at `level` **low** | **0** |
| Editions leading with a CORRECTION | **2** (Fri 14:30, Fri 22:30) |
| Claims total | 661 |
| Claims flagged `single` | 17 |
| Claims flagged `stale` | 7 |
| Claims flagged `unconf` | 1 |
| Claims flagged `disc` | 0 |
| **Flagged claims total** | **25** (3.8%) |

**Where the errors are is more useful than the total.** By slot:

| Slot | Editions | Stories | mid | Claims | Flagged | Flagged % |
|---|---|---|---|---|---|---|
| 06:30 | 1 | 6 | 1 | 51 | 1 | 2.0% |
| 08:30 | 1 | 6 | 1 | 40 | 1 | 2.5% |
| 10:30 | 1 | 7 | **3** | 48 | **7** | **14.6%** |
| 12:30 | 2 | 14 | 1 | 79 | 1 | 1.3% |
| 14:30 | 2 | 16 | 0 | 88 | 0 | 0.0% |
| 16:30 | 2 | 15 | **3** | 82 | **8** | **9.8%** |
| 18:30 | 2 | 15 | 2 | 94 | 2 | 2.1% |
| 20:30 | 2 | 15 | 1 | 88 | 4 | 4.5% |
| 22:30 | 2 | 15 | 0 | 91 | 1 | 1.1% |

Grouped: **pre-open 06:30–12:30 — 18% of stories at mid, 4.6% of claims flagged. US session 14:30–22:30 — 8% of stories at mid, 3.4% flagged.** The thinner the news, the weaker the sourcing. The 10:30 edition is the worst single edition in the set.

The two corrections both matter, and one more than the other. Friday 22:30 corrected an **absence claim** — the 20:30 edition said Oracle had filed nothing since 23 September when it had filed twice that afternoon, because the SEC feed returned a stale copy. Friday 14:30 corrected a **staleness error**: Thursday's new home sales data re-reported as if it were Friday's. Both are the exact failure the FRESH DATA rules were written to prevent, and both happened anyway. The rules are not yet self-enforcing; that is what open item 4, the second independent checker, is for.

### 3c · Timing fit

Reconstructed from the editions' own MARKET stories. The editions are the only view of the day available, so the largest move can only be located to the window between two editions — itself a limit worth stating.

| Day | Largest inter-edition S&P 500 move | Window | Was a run within 30 min of it? |
|---|---|---|---|
| Thu 24 Sep | +0.39 pp day-change (7,671.46 → 7,701.14) | 16:30 → 18:30 UK | Yes — the 18:30 run closes the window |
| Fri 25 Sep | +0.19 pp day-change (7,725.43 → 7,740.34) | 16:30 → 18:30 UK | Yes — the 18:30 run closes the window |

Friday's whole intraday range was +0.29% to +0.51% day-change — a drift, not a move. **No large index move went uncovered on either day.**

**The genuine miss is the 13:30 UK data print, on both days:**

| Day | Print | Landed | First edition carrying it | Late by |
|---|---|---|---|---|
| Thu 24 Sep | Jobless claims 197,000 (DOL) | 13:30 UK | 14:30 edition, filed 14:43 UK | **73 min** |
| Fri 25 Sep | Factory / AI equipment orders (Census) | 13:30 UK | 14:30 edition, filed 14:57 UK | **87 min** |

The Friday 06:30 edition even flagged "US factory orders due 13:30 UK" in advance, and then no run was near it. Separately, Thursday's new home sales (15:00 UK) first appeared in the 16:30 edition filed 17:04 UK — 124 minutes late.

### 3d · Filing reliability

| Day | Scheduled slots | Rows | Gaps |
|---|---|---|---|
| Thu 24 Sep | 9 | 6 | 06:30, 08:30, 10:30 — **step 5 was not live yet**, not failures |
| Fri 25 Sep | 9 | 9 | none |

**Of every slot that ran with step 5 live, 15 of 15 produced a row. No gaps, no missed slots, no partial filings.** On this evidence the chain is reliable; open item 5 (the heartbeat alert) is still worth building, but nothing has yet needed it.

No reader analytics exist yet; GitHub Pages serves none. The privacy-respecting counter is **built** by the CRM chat (item 6 below) and goes live on Alex's clicks.

---

## 4 · Frequency — recommendation, 27 September

**Recommendation: do NOT go to thirteen runs yet. Keep nine, and move one run to 13:45 UK. Re-review after one full week with the wire on.** Frequency is Alex's decision; nothing has been changed (the 28 Sep edit left the schedule untouched).

### Why the increase is not earned yet

The proposal's case was coverage. The measurement does not support a coverage problem:

- Every run filed. No run was wasted on "nothing new" — so the usual argument against more runs does not apply either.
- The largest index move on both days was already covered by an existing run.
- Nothing was missed for want of a run.

What the measurement does show is an **accuracy** problem concentrated in the thin hours: pre-open editions carry more than double the mid-level rate of US-session editions, the 10:30 edition flagged 14.6% of its claims, and two corrections landed in 15 editions. Thirteen runs adds four more editions into exactly that thin-news band. It buys coverage that is not short and pays for it in the failure mode that is.

The doc's own **two conditions before any increase** are also both unmet: the error count is not low, and the second independent checker (open item 4) is not built.

And the decisive point: **the wire was off for all 15 editions.** The wire adds three to five verified headlines to every edition. Judging cadence on wire-off editions and then turning the wire on measures the wrong product. One week with the wire on is worth more than any cron change.

(28 Sep: the coverage problem Alex found was one of breadth across names, not of timing — fixed in the prompt, not the clock. See §00.)

### What to do instead — the 13:45 print-catcher

The one real, repeated miss is the 13:30 UK release, 73 and 87 minutes late on consecutive days. That is fixed by moving a run, not by adding four.

### The cron — and a conflict in the proposal as written

Worked out for BST (UK = UTC+1 until 25 October); cron fields are UTC. **I could not test these against the platform: creating or editing a scheduled task was refused in this session (see §0). The interval arithmetic below is verified by hand, not by the scheduler accepting it.**

**The standing proposal cannot run as written.** 06:30 · 08:30 · 10:30 · 13:45, then hourly 14:30 → 22:30 has two problems:

1. It needs two different minute values (`:30` and `:45`). A 5-field cron takes the cross-product of its minute and hour lists, so `30,45 5,7,9,12-21 * * 1-5` fires **twice** in every listed hour — 26 runs, not 13.
2. **13:45 → 14:30 is a 45-minute gap, under the platform's one-hour minimum, and would be refused.** The same flaw sits in Stage B below as originally written: moving the 12:30 run to 13:45 while keeping 14:30 leaves the same 45-minute gap.

Both are solved by putting every run at `:45`:

| Option | Cron (UTC) | Runs | UK times | Min gap |
|---|---|---|---|---|
| **Recommended** — nine runs, print-catcher | `45 5,7,9,12,13,15,17,19,21 * * 1-5` | 9 | 06:45 · 08:45 · 10:45 · **13:45** · 14:45 · 16:45 · 18:45 · 20:45 · 22:45 | 60 min ✓ |
| Prepared, not recommended yet — the thirteen | `45 5,7,9,12,13,14,15,16,17,18,19,20,21 * * 1-5` | 13 | 06:45 · 08:45 · 10:45 · **13:45** · then hourly 14:45 → 22:45 | 60 min ✓ |

Both sit exactly on the one-hour floor at the 12:45 → 13:45 UTC step. If the platform rejects an exactly-60-minute gap, drop the `13` hour from the recommended option and accept 13:45 followed by 16:45.

Note both shift all runs from `:30` to `:45`, which changes every edition's label and `edition_id` minute. That is cosmetic but visible on the page, and it is the price of one expression. Moving only the midday run is not expressible as a single cron. **If the cron changes, the prompt's ROTATION rule already says to count the day's runs in order from 0, so the rotation survives; the slot times listed beside it should be updated in the same edit.**

**Stage C, unchanged and still the better ceiling:** event-driven bursts — nine base, plus two or three on CPI, jobs, Fed and big-earnings days, roughly +15% usage — in preference to flat hourly through the US session, which is thirteen runs and roughly +45% for filler on quiet days. The audience is family investors who open the page once or twice a day; the value of frequency to them is that the page is right when they look, not that there are more editions.

**The real capacity gain is still not the clock.** The wire returning adds three to five verified headlines per edition at no cost. The X collector (paid API, official company and CEO accounts, each post filed as a claim) is the next step up in first-hand sourcing and needs Alex's approval with the cost in front of him.

---

## 5 · Open items

| # | Item | Owner |
|---|---|---|
| 1 | ~~Tick **Enforce HTTPS**~~ — **done by 26 Sep** | — |
| 2 | ~~THE WIRE switched back on~~ — **done 28 Sep, 17:42 UTC**, by Claude with Alex present (§00); first wire-on edition 20:30 UK, four WIRE stories | — |
| 3 | Trial measurement — **done 27 Sep, §3**. Frequency decision | **Alex**, see §4 |
| 4 | Second independent checker run — both of the week's corrections are the failure this would catch | Claude |
| 5 | Heartbeat alert when two runs in a row are missed | Claude |
| 6 | Reader counter — **built 25 Sep by the CRM chat as CRM Stage 1**: `claude/crm-stage1-handover.md` carries the package and Alex's clicks. (A duplicate built the same morning by the Newsroom chat was withdrawn; see `claude/newsroom-journalism.md` §3.) | **Alex**, with the CRM chat |
| 7 | `fca-check` pass on the page's fixed copy, recorded | Claude |
| 8 | Sync the private Claude page with the public build | Claude |
| 9 | ~~3.17 landing page → `buytrigger.club/join`, repoint JOIN, retire Carrd~~ — **done 24 Sep** | — |
| 10 | Sweep the build brief and copy pack for the old address and the 19 Oct date | Claude |
| 11 | Token rotation at the public push | **Alex** |
| 12 | Allow `typefully-user-uploads.s3.amazonaws.com` in Claude's allowed domains so the bees can attach charts to drafts | **Alex** |
| 13 | **Push the phone header commit** `c8f502a` (`cd "$HOME/Desktop/GitHub Project/buytrigger-newsroom" && git pull --no-rebase --no-edit && git push origin main`) | **Alex** |
| 14 | ~~Add `tickers: []` per story in the writer's output~~ — **done 28 Sep** (§00); all 12 stories in the 20:30 edition carry it | — |
| 15 | The `newsroom_editions.checked_at` column is null on every row — the per-edition `doc.checked` object is populated but the column the page's "CHECKED <time>" label reads is never written. ~~Step 5's heading still names `news.buytrigger.club`~~ — **fixed 28 Sep**. The `checked_at` half is still open (the edge function or the writer's `file` action should set it from `doc.checked.at`) | Claude |
| 16 | **New, 27 Sep:** the Sunday refresh of `web/site/index.html` (3-second notice, and the shorter notice text) was **not built** — this review ran in the cloud with no access to Alex's Mac | Claude, next session with the Mac |
| 17 | **New, 28 Sep:** watch the first full day on the widened prompt (Tue 29 Sep) — rotation reaching the whole universe, run time, pre-open `mid` rate; refresh the COVERAGE snapshot when the universe or top ten changes | Claude |
| 18 | **New, 29 Sep:** first full day on the fixed prompt (Wed 30 Sep, 06:45 → 22:45) — every edition on the public feed by itself (watchdog replies OK, no FIXED); run lengths; corrections count against the 5-in-27 baseline | Claude |
| 19 | **New, 29 Sep:** the public page's title and share text still say "the market, every two hours" (`<title>`, `og:title`, `twitter:title`, meta description in the newsroom repo's `index.html`) — now hourly from 13:45. Copy change via GitHub web upload (the newsroom repo cannot be pushed from Alex's Mac) | Claude prepares → **Alex** uploads |
| 20 | **New, 29 Sep:** the HQ project's `claude/daily-brief-profile.md` still lists the old short watchlist, and `claude/daily-brief-latest.md` may carry a "step 5 blocked" note. The writer's prompt now overrides both, so nothing breaks, but they should be tidied from a chat in the BuyTrigger HQ project (this project cannot write there) | **Alex** / HQ chat |
| 21 | **New, 29 Sep:** the filing token now lives in two task prompts — the writer and the watchdog `trig_016riCgZvbeVLBsUMpC5HoF9`. Rotate both together (item 11) | **Alex** + Claude |

### The open copy question

The early-bird discount ends **Sunday 25 October**; the public launch is **Monday 26 October**. The sale copy cannot say the offer is still running on a page that goes up the day after it expires. Either the discount extends past the launch, or the public page opens at full price. One paragraph in `claude/newsroom-copy-pack.md` section 4. Alex's call.

---

## 6 · Standing rules

- **The filing token lives in the scheduled task's prompt**, on the `NEWSROOM_FILE_TOKEN =` line. Anyone editing that task reads the live prompt first and carries that line through untouched. Never printed anywhere. Rotate at the public push.
- **The writer covers the whole BuyTrigger universe** (Alex, 28 Sep: "not just Nvidia and Hood"). The universe and top-ten lists in the prompt's COVERAGE section are snapshots dated 28 September. When the sheet adds or drops a name, or the top ten changes, edit those two lines (read the live prompt first; token line untouched; read the saved prompt back and compare). Every story carries `tickers` — the Desk reads it to put stories on members' names.
- **Change control for live Newsroom tasks** (29 Sep, after the Opus 5.5 outage): no model, schedule or step-5 change goes live without two good test runs of a copy that posts nothing public; then watch the first live run on both the private page and the public feed. The watchdog `trig_016riCgZvbeVLBsUMpC5HoF9` is the backstop, not the plan.
- **Company news is found by a sweep, not only by rotation or price** (29 Sep, after the AMD–World Labs miss). Every run starts with the NEWS SWEEP across the whole universe; a material event is a story even at a 0% move. Never remove the sweep to save run time — cap stories per edition instead.
- **Supabase project discipline.** Newsroom work belongs to the Research project `paoxcmxteemakhyvwihn`. The production members' project `brzawmbpwkdundruicca` is off limits for Newsroom tables. (The CRM's `crm` schema is the CRM chat's planned exception, per `claude/crm-funnel-brief.md`; it touches no existing table.)
- **A wrong number comes off the page first and is corrected second.** `{"action":"withdraw","edition_id":"…"}` drops it within a minute; the correction leads the next edition. Never edit or delete an earlier edition.
- **Nothing about Alex goes in an edition** — no positions, trades, entry prices, holdings, subscriber identities or revenue.
- **Class names.** The source page owns a `.login` class from the old owner login. The public top bar uses `.signin`; reusing `.login` inherits the old sizing and a phone-only `order:2` that reshuffles the buttons.
- **One job, one chat, one branch** (Alex, 25 Sep). A chat reads the project docs list before building; a handover doc with the job's name means it is taken.
- **The newsroom repo's local `main` had a commit (`575c92d`) that GitHub already held as `2f1b01a` ("Add files via upload", same content). Reset to `origin/main` on 25 Sep before the header commit; nothing was lost.**
- **A cron change to the writer has to be expressible as ONE 5-field expression with every gap at 60 minutes or more** (27 Sep). Mixed minute values multiply out into extra runs, and anything tighter than an hour is refused by the platform. Work the UK→UTC arithmetic and the gaps before proposing times.

### Three things learned the hard way on 24 September

1. **Committing a file by staged path can write a stale copy** when the container's timestamp has not changed. Deliver the file, commit it by its delivered id, then read the destination back and compare checksums before saying it is there. Twice a file was reported saved when the copy on the Mac was the previous version.
2. **GitHub Pages does not redirect an old custom domain.** Changing the repo's custom domain from `news.buytrigger.club` to `buytrigger.club` left the old address answering "Site not found", not redirecting. It was deleted at Porkbun rather than rescued. Any future address move needs a redirect planned before the switch, not assumed.
3. **A page can be correct on the server and wrong in the browser** for up to ten minutes — `Cache-Control: max-age=600`. Before diagnosing a failed deploy, fetch the file with the cache bypassed and read `last-modified`.

### Three more from 24–25 September

4. **X refuses app-published posts that contain any link**, including bare domains like `treasury.gov`. Posts sent through Typefully name sources in words.
5. **Both sandboxes sit behind the same allowed-domains list.** `supabase.co` reaches; `amazonaws.com` does not. A new host used by a bee (Typefully's upload bucket) has to be allowed by Alex before the bee can use it — test the host with one request before building on it.
6. **Two chats built the same counter on the same morning.** The project docs list is the lock: read it before building, and file the handover doc the moment a job starts, not when it ends.

### Two from the 27 September review

7. **A scheduled Cowork run cannot edit a scheduled task's prompt.** The permission classifier refuses it, and there is no way round it from inside an unattended run — correctly, since it is a live automation. **Any change to a running automation has to be either done by Alex, or done in a session where he is present to approve it.** Plan wire switches, schedule changes and prompt fixes for an attended session; a Sunday routine can measure and prepare, but it cannot arm. **Confirmed 28 Sep:** in an attended session, `update_trigger` with the full prompt worked first time; the task list (`list_triggers`) returns the live prompt under `derived_state.prompt`, which is how to read it first and verify it after.
8. **The feed is the only record of the trial, so the trial began when step 5 went live, not when the runs did.** Three Thursday runs and all of Monday to Wednesday happened and are simply not measurable from `newsroom_editions`. When a measurement window matters, check when the recording started before counting.
