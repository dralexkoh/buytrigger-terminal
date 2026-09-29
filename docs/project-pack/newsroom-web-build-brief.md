# BuyTrigger Newsroom — web build brief (buytrigger.club)

_Version 6, 23 September 2026, 12:40 UK (v5 12:20, v4 11:50) (v3 22 Sep 18:30, v2 17:40, v1 16:10). Written by Claude (as Marissa / OS Control) from Alex's decisions of 21–22 September. Work item `BTRES-3.7.15 — Agentic Newsroom` (feed, Tim) plus a new dashboard scope to be opened in `buytrigger-dashboard` (build, Jensen) through the scope flow. Nothing in this brief is built or deployed. Approval to host and to open the public door is Alex's, at the end._

## Alex's decisions (22 Sep, 16:00 UK)

1. **The news channel is the new landing page** at `buytrigger.club`. Free, no login.
2. **JOIN → the sales page** ($599 / $60), then checkout, then the dashboard.
3. **A demo of ten stocks** is available free.
4. **Tapping the header goes back to the news** from anywhere.
5. **Alex's content desk and OS board stay on a private link only he can open** — no admin door on the public site. ("So it doesn't confuse users, or welcome hackers.")

Recommended shape for 3 (Claude's call, for Alex to overrule): the demo is **the real dashboard in a ten-stock mode**, not a separate page. A visitor who taps DASHBOARD in the top bar gets the Daily Summary with ten stocks and a JOIN banner; a member gets all 111+. One codebase, one flag. On the news page's bottom strip the ten demo names show their levels; every other active name shows its name only. Which ten: Lisa and Tim pick, never the member watchlist names, reviewed monthly.

## The map

```
buytrigger.club                 NEWS — the channel. Free. The landing page.
buytrigger.club/app             DASHBOARD — Daily Summary · Macro · Portfolio
                                 visitor: ten-stock demo + JOIN banner · member: everything
buytrigger.club/join            the sales page → Stripe checkout → /app
buytrigger.club/login           member log in (the dashboard's existing 4.0 login)
dralexkoh.substack.com          the free letter — stays the door in social bios
<private Claude page>           Alex's CONTENT desk and OS board — today's page, unchanged
```

Top bar on every public page: **BUYTRIGGER** (wordmark = home = news) · NEWS · DASHBOARD · right side: FREE LETTER · JOIN THE CLUB · LOG IN (visitor) or the member's name (logged in). Phone: bottom tabs NEWS · SUMMARY · MACRO · PORTFOLIO.

`buytrigger.io` → 301 → `buytrigger.club` (already the roadmap's rule). `members.buytrigger.club` (Mighty, still selling 2.0) retires at launch.

## Security shape

- The public site carries **no admin code and no admin route**. There is nothing to find. Alex's desk (CONTENT, OS, tweak notes, approvals) stays on the private Claude page, where his Claude identity is the login and the server enforces owner-only data. If the desk ever moves to the web it gets its own private address behind the dashboard's auth with an admin role, never a hidden door on the public site.
- Member login is the dashboard's existing Supabase auth. The news channel reads a public feed; the evidence table and the archive are member reads behind row-level security.
- The feed is filed by one authenticated endpoint the scheduled run calls. No browser ever holds a write key.
- Public page about markets = financial promotion surface: compliance pass (`fca-check`) on the channel's fixed copy, the JOIN pitch and the demo before the door opens. Research and education only; no advice; never Alex's positions.

## What gets built, by owner

**Tim / Research (feed and archive)**
1. `newsroom_editions`, `newsroom_stories`, `newsroom_claims` tables in the isolated Research Supabase (`paoxcmxteemakhyvwihn`), append-only, hashed like the Desk ledger. Schema = `bt-newsroom-feed/0.1` as filed today (`claude/newsroom-app-feed-contract.md`), one row per edition, per story, per claim.
2. One authenticated filing endpoint; the Daily Brief run files there as well as to the Claude page during the changeover, then only there.
3. Two read views: public (headline, short, dek, callouts, level, source names, markets, catalysts, time chip) and member (adds claims with status, plus the archive).
4. Backfill from the editions already filed and the weekly archive docs.
5. `newsroom_cards` / `newsroom_approvals` later, with the private-preview build flow from the Phase 1 review. Not for launch.

**Jensen / Technology (the site)**
6. New scope in `buytrigger-dashboard`: a Newsroom page = today's page with the Claude-only parts removed (NEWS only; no CONTENT, no OS, no tweak notes, no login of Alex's). Same one-screen fit, today-so-far, rundown sheet on phone, EVIDENCE button (locked for visitors, evidence table for members).
7. The shared top bar and the phone tab bar across the news page and the dashboard; wordmark → news.
8. THE DAY SO FAR block on the Daily Summary (top three stories, time chips, WATCH THE CHANNEL).
9. Ten-stock demo mode of the dashboard for visitors, JOIN banner, member view unchanged.
10. The bottom strip on the news page: active BuyTriggers today (ten demo names with levels; other names only) and today's picks — a small read-only daily feed from the BuyTrigger database (Database Manager owns the query).
11. Routing and hosting: `buytrigger.club` → news; `/app`, `/join`, `/login`; redirects above. Cloudflare, where the Command Centre already runs.

**Lisa / Colette (words and the sale)**
12. The sales page at `/join` (launch set, w/c 29 Sep). JOIN copy on the news page, the EVIDENCE pitch line, the demo banner. Same closing line as every free piece: "My system's exact levels are for members. The thinking is free, forever."
13. Which ten demo stocks (with Tim).

**Marissa / OS Control**
14. Writer handoff for the newsroom feed work (BTRES-3.7.15) — Claude has the page, the feed and the design; Codex reviews. Recorded through a written handoff before any repo write.
15. Registry: AUT-2026-016 schedule and outputs; the decision record for "merge into 4.0" and "news is the landing page".

## Sequence

| When | What | Gate |
|---|---|---|
| Now → Fri 26 Sep | Trial week on the private page continues; this brief is the scope | — |
| Sun 27 / Mon 28 Sep | Trial review: keep, change, stop. If keep: open the dashboard scope (Jensen) and the Research scope (Tim); writer handoff recorded | Alex: keep |
| w/c 28 Sep | Lane 1 stays first: the five 5-October items only Alex can do are not displaced by this | — |
| 28 Sep → 10 Oct | Tables, endpoint, read views (Tim); Newsroom page + top bar + day-so-far block (Jensen); sales page (Colette) | none needed to build |
| 5 Oct | BT4.0 early-bird opening as planned — news page not required for it | — |
| 10–16 Oct | Demo mode, bottom strip, phone tabs; compliance pass; private preview at a staging address | Alex: preview OK |
| 19 Oct | Public launch: buytrigger.club → news; JOIN live | Alex: go |

Two to three working days of build in total, spread across the fortnight so it never competes with Lane 1.

## Acceptance (what "done" means)

- A visitor at buytrigger.club sees the channel within one second, one screen, on phone and desktop; no admin control exists on the page.
- Tapping the wordmark from any dashboard page returns to the news; tapping DASHBOARD as a visitor opens the ten-stock demo with a JOIN banner; as a member, the full Daily Summary.
- THE DAY SO FAR on the Daily Summary matches the channel's top three stories at the same minute.
- Every number on the public channel resolves to a claim row with a source; the member evidence table shows it; a visitor cannot read claim rows from the network.
- The scheduled run files one edition per run to the endpoint; a bad edition can be withdrawn by an owner action without editing history.
- Compliance pass recorded; fixed copy carries the research-and-education line.

## Open

- The exact demo rule (ten fixed names vs a rotating ten) and whether the demo shows live or delayed levels — Lisa and Tim.
- Whether JOIN goes straight to checkout or via the free letter first — Lisa, against the one-door rule in `claude/marketing-brand-roadmap.md`.
- Hosting address for the dashboard (`/app` vs `app.`) — Jensen.

---

## Version 2 additions — 22 Sep, 17:40 UK

### Alex's decisions (22 Sep, 17:20 UK)

6. **JOIN → the sales landing.** For now the One Club is **on hold until [OPENING DATE]**; the page carries an early-bird line: email **hello@alexkoh.me**, **13 spots left of 30**. When the doors open the email button becomes checkout and nothing else on the page changes.
7. **LOG IN → the members' login** (the dashboard's existing 4.0 login).
8. **The ten-stock demo is reachable by accident** — DASHBOARD · DEMO in the top bar, a TRY THE DEMO button on the sales page, and the UNLOCK ALL banner inside the demo lead back to JOIN.
9. **A mirrored private login for Alex** — his content-creation desk and OS board stay on a private link only he can open; that link is where Claude / OS / CRM automation (the marketing agent swarm) hangs off. No admin door on the public site.
10. **Order of work: 3.7.9 first.** The web build starts **Saturday night, 26 Sep** (moved from Mon 28 Sep). Trial review folds into that Saturday session.

Mocked on the design canvas as boards **G · The sale** and **H · The demo**; the public door (C) now links JOIN → G, DASHBOARD · DEMO → H, LOG IN → D.

### Sequence, revised

| When | What | Gate |
|---|---|---|
| Tue 22 → Fri 26 Sep | 3.7.9 Live Research Packs runs first: Thursday 24 Sep Live pack (Tim), drawing on the newsroom's day-so-far archive. Trial week on the private page continues; daily spot checks | — |
| **Sat 26 Sep, night** | Web build starts: trial review (keep / change / stop) + open the dashboard scope (Jensen) and the Research scope (Tim); writer handoff recorded | Alex: keep |
| 26 Sep → 10 Oct | Tables, endpoint, read views (Tim); Newsroom page + top bar + day-so-far block (Jensen); sales page on-hold version (Colette) | none needed to build |
| 5 Oct | BT4.0 early-bird opening as planned — not dependent on the site | — |
| 10–16 Oct | Demo mode, bottom strip, phone tabs; compliance pass; staging preview | Alex: preview OK |
| 19 Oct | Public launch: buytrigger.club → news; JOIN live (on-hold page until the opening date) | Alex: go |

Lane 1 (the five 5-October items only Alex can do) is not displaced by any of this.

### Colour audit — the black channel next to the white dashboard

Method: WCAG 2 contrast ratios computed from the brand tokens in the Research repo (`research/config/brand_tokens.json`, `BRAND.md`): primary #B70000, black #000000, white #FFFFFF, navy #042139, gold #FFD700, green #22C55E, red #EF4444, light grey #F5F5F5, body text #374151. The channel uses ground #04121F, which is the same navy family (1.15:1 against #042139 — the eye reads them as one colour).

**Verdict: they do not clash.** The channel is the brand's dark face, the dashboard its light face; both come from one palette and one font set (Barlow Condensed / IBM Plex Sans / IBM Plex Mono). Three things make the join feel deliberate rather than two products stapled together:

1. **One top bar on both, in navy #042139** with white wordmark and gold JOIN. The bar is the constant; the page below it changes colour.
2. **The navy "THE DAY SO FAR" block on the white Daily Summary** is the bridge — a piece of the channel living inside the dashboard, with the WATCH THE CHANNEL button in brand red.
3. **Red #B70000 is the only saturated accent shared by both**; gold stays a fill (badge, button) with navy text, never text on white.

Pairs that pass (text at 4.5:1, large text 3:1):

| Surface | Pair | Ratio | |
|---|---|---|---|
| Channel #04121F | white text | 17.6 | pass |
| Channel | soft #C5D3DF | 12.4 | pass |
| Channel | muted #9FB3C4 | 8.7 | pass |
| Channel | gold #FFD700 | 13.5 | pass |
| Channel | green #22C55E | 8.3 | pass |
| Channel | red #EF4444 | 5.0 | pass |
| Red #B70000 fill | white text | 7.0 | pass |
| Gold #FFD700 fill | navy text | 13.5 | pass |
| White dashboard | navy #042139 | 16.4 | pass |
| White | body #374151 | 10.3 | pass |
| White | brand red #B70000 | 7.0 | pass |
| Navy bar #042139 | white | 16.4 | pass |
| Navy bar | gold | 11.7 | pass |

Pairs that fail on the white dashboard — for Jensen's checklist, not blockers:

| Pair | Ratio | Rule |
|---|---|---|
| gold #FFD700 text on white | 1.4 | never gold text on white; gold is a fill with navy text |
| green #22C55E text on white | 2.3 | use #15803D (5.0) for "up" / positive small text |
| red #EF4444 text on white | 3.8 | large text only; use #B70000 (7.0) for small "down" text |

The demo mock (board H) already uses the darker green/red for its bars and labels.

### Documents to get ready — status and owner

| Document | Status | Owner | Where |
|---|---|---|---|
| This build brief (scope, map, security, sequence, acceptance) | ready, v2 | Marissa | `claude/newsroom-web-build-brief.md` |
| Feed contract (`bt-newsroom-feed/0.1`, OS `os/*` schemas) | ready | Tim / Claude | `claude/newsroom-app-feed-contract.md` |
| Rollout plan (decisions log) | ready, needs v8 with decisions 6–10 | Marissa | `claude/newsroom-rollout-plan.md` |
| Mockups (A–H + phones) | ready | Claude | design canvas |
| Writer handoff, Newsroom page + feed → dashboard scope | **draft below**, to be recorded before any repo write | Marissa → Codex (OS registry) | this doc |
| Sales page copy, on-hold + early-bird version | **brief below**; copy to write | Lisa / Colette | BUYTRIGGER CONTENT |
| Demo rules (which ten, live or delayed, rotation) | open | Lisa + Tim | Research |
| Dashboard scope brief for `buytrigger-dashboard` | to open Sat 26 Sep from this doc | Jensen | dashboard repo scope flow |
| Research scope (tables, endpoint, views) | to open Sat 26 Sep | Tim | Research repo `Project/active/` |
| Compliance checklist for the public surface | **draft below** | Marissa → compliance owner | this doc |
| OS registry: AUT-2026-016 status, decisions "news is the landing page", "3.7.9 first, build from 26 Sep" | outstanding | Codex | `claude/os-board-handoff-for-codex.md` |

#### Draft — writer handoff (for the OS registry, Sat 26 Sep)

Work: BTRES-3.7.15 Agentic Newsroom, Phase 2 — public web page. From: Claude (page, feed, design mocks, this brief). To: Jensen (dashboard scope: page, top bar, day-so-far block, demo mode, routing) and Tim (Research scope: tables, endpoint, read views). Claude keeps the private Claude page and the scheduled Daily Brief run until the endpoint files cleanly for five straight runs, then the run files only to Research. Codex reviews read-only and records the handoff. Evidence: this brief, the feed contract, the design canvas, the trial spot-check log. Approval state: build approved by Alex 22 Sep; hosting and public door approval still Alex's at 19 Oct.

#### Brief — sales page copy (Colette, under Lisa)

One page at `/join`, dark, same top bar. Headline "Don't guess. Measure." (placeholder). Three tiles: 111+ stocks with BuyTrigger and ValueTrigger levels · 13 of 30 early-bird spots · $599 a year or $60 a month. Aside: ON HOLD — One Club opens [OPENING DATE]; hold a place by email to hello@alexkoh.me, subject "Early bird", reply within a day; pay nothing until the doors open. Two secondary buttons: TRY THE TEN-STOCK DEMO, WATCH THE NEWS. Closing line, as every free piece: "My system's exact levels are for members. The thinking is free, forever." Research and education only; no advice; never Alex's positions. Second version for opening day: the email button becomes checkout, nothing else changes. Keep the one-door rule: the free letter stays the door in social bios; the Club link only appears in the letter/welcome flow and on buytrigger.club itself.

#### Draft — compliance checklist (before 19 Oct)

- Fixed copy on the channel, the sales page and the demo banner carries "research and education only, not advice".
- No performance claims, no returns figures, no "13 spots" urgency line without the real count behind it (count kept by Lisa; page updated by hand until checkout goes live).
- Demo shows levels for the ten demo names only; never the member watchlist; never Alex's positions, entry prices or holdings.
- Every number on the public channel resolves to a claim row with a source; withdrawn stories stay withdrawn in the archive.
- Early-bird email goes to hello@alexkoh.me only; no address list is built on the public site.
- Compliance pass (`fca-check`) recorded on the fixed copy before the public door opens; Alex's go recorded.

### Open (added)

- The opening date for the One Club — Alex.
- Who keeps the "spots left" count current on the page until checkout exists — Lisa (proposed).
- The private link for Alex's desk: stays the Claude page for now; a CRM / agent-swarm hook is a separate scope once the marketing automation lane is defined.

---

## Version 3 additions — 22 Sep, 18:30 UK: the editorial spec (what the news must be)

### Alex's decisions (22 Sep, 18:00 UK)

11. **3.7.9 first; the web build starts Saturday night 26 Sep** (confirmed). Fable 5.1 drives the build session.
12. **The news is written for family investors.** Every edition carries: WHY THE MARKET IS UP / DOWN, a VIX UPDATE, and stock stories biased to the BuyTrigger database (the universe and its elements: BuyTrigger, ValueTrigger, triggered / near / far).
13. **Members preview mocked** — board I on the design canvas: the channel as a member sees it, EVIDENCE panel open, the family-investor slots, and the ACTIVE TODAY strip with levels visible to members and words only to visitors.

### The family-investor lens — live in the run from the next edition

Applied today to the run's standing profile (`claude/daily-brief-profile.md`, section "The family investor lens") and flagged to the next run with an OS CONTROL NOTE in `claude/daily-brief-latest.md`. The scheduled prompt itself is re-issued with the lens baked in at the Saturday build session (the prompt's exact text is not in this session's log after compaction; the profile doc and the note are the working channel until then).

| Slot | Tag | Rule |
|---|---|---|
| WHY THE MARKET IS UP / DOWN / FLAT | `MARKET` | one per edition, first; headline names the cause; index moves with exact numbers; two or three causes each with a number and a primary source; breadth or leadership when it explains the day; never a bare recap |
| VIX UPDATE | `VIX` | one per edition, second; level, change, and the ladder band in plain words: under 15 calm · 15–20 normal · 20–30 nervous · over 30 the system's buy window; dips are windows, not warnings; never "you should" |
| Stock stories | `STOCK` | BuyTrigger-universe names first; every stock story ends with the element it touches: near a BuyTrigger · triggered today · far from trigger · ValueTrigger zone · level: members; a word, never an invented level |
| THE WIRE | `WIRE` | unchanged: three to five verified general headlines after the watchlist stories |

Feed contract change for the build (Tim): `story.element` (enum above, optional) and `story.slot` values `WHY THE MARKET IS UP` / `WHY THE MARKET IS DOWN` / `WHY THE MARKET IS FLAT` / `VIX UPDATE`. The page renders `element` as the chip on the ACTIVE TODAY strip and on the story card. Public view: element word only. Member view: element word plus the level from the read-only levels feed (Database Manager; item 10 in "What gets built").

### First-hand sources and X — where we stand

- **Today:** the run reads company press releases, SEC filings (EDGAR), earnings-call transcripts, exchange and regulator notices, central banks, and the wires. Those are "first mouth" for a filing-grade newsroom, and they pass the evidence table as `ok`.
- **X is not linked.** The run cannot read X (no API, and X blocks anonymous reads). A CEO's post reaches an edition only when a wire or the company carries it; it is cited as the wire with status `sec`. The run is told never to quote a social post from memory.
- **To link X properly** (for the build, not before): a small collector in the Research repo (Tim) on the X API — Basic tier is a paid plan — reading a curated list of official company and CEO accounts for the BuyTrigger universe, filing each post as a claim with the post's own timestamp and URL, status `single` until a second source confirms. Paid API use and a new automation: Alex's approval, requested at the Saturday session with the cost in front of him. Until then, wires carry the CEO quotes.

### Documents-ready table — additions

| Document | Status | Owner |
|---|---|---|
| Editorial spec (this section) | ready | Marissa; Tim applies to the run and the feed contract |
| Members preview mock (board I) | ready | Claude |
| X collector scope (cost, account list, claim rules) | to draft for Saturday | Tim |
| Prompt re-issue with the lens baked in | Saturday session | Claude (writer of AUT-2026-016) |

---

## Version 4 — 23 Sep: the go-live plan, pulled forward

Alex, 23 Sep: "we are not waiting till later now" — the newsroom is the new buytrigger.club segment; it runs in parallel with 4.0 (the overall run) and 3.17 (the website funnel). This section replaces the "Sequence, revised" table above where they differ.

### Three stages, each one usable on its own

| Stage | When | What people see | What has to exist | Gate |
|---|---|---|---|---|
| **0 · Preview door** | this week → 5 Oct | the Claude page itself, shared by link with early birds and a few trusted readers | the page's feed opened to anyone with the link (read only, no admin) — Claude checks feasibility Sat; a `news.buytrigger.club` forward to it if Alex wants the address early | Alex: OK to share; compliance line on the page |
| **1 · Own address** | Sat 26 Sep → 10 Oct | `news.buytrigger.club` — the same page, BuyTrigger address, no Claude branding | (a) `newsroom_editions` table in the Research Supabase with public read, (b) one filing endpoint with a scoped write token the run calls (never in the page), (c) the page fetching that feed instead of the Claude store, (d) Cloudflare Pages hosting, (e) WITHDRAW action for the owner, (f) the CONTENT/OS desk stays on the private Claude page | Alex: hosting + Supabase approval (Sat); compliance pass before the link goes out |
| **2 · The landing page** | 10 → 19 Oct | `buytrigger.club` = the channel; JOIN → sale; DASHBOARD · DEMO; LOG IN → members; THE DAY SO FAR in the dashboard | the 3.17 funnel wiring (Lisa/Colette copy, Jensen routing), ten-stock demo mode, bottom strip from the database | Alex: go, 19 Oct |

Two to three build days across the fortnight; Lane 1 (the five 5-Oct items only Alex can do) is not displaced.

### Risks and what we do about them (before anything is public)

| Risk | What could happen | Prepared answer |
|---|---|---|
| A wrong number goes public | a stale-cache story like 21 Sep, now in front of readers | FRESH DATA + NUMBERS CHECK rules already in the run; WITHDRAWN state on the page; CORRECTION leads the next edition; owner WITHDRAW button in stage 1; a second checker (separate run, 15 min after each edition) added before stage 1 |
| The run stops and nobody notices | a silent page all afternoon | the page already shows FEED QUIET after 3 hours with no filing; add a heartbeat check-in that pings Alex if two runs in a row are missing (the 22 Sep 12:30 gap is the case) |
| Compliance | a public financial page reads like advice | fixed copy carries "research and education only, not advice"; no positions, no "you should"; `fca-check` pass on the page copy before stage 0 sharing; Alex's name on the page only as publisher |
| A key leaks | the filing token ends up in page code or a prompt | the page only ever reads; the run calls one endpoint with a token stored in the task's secrets, never pasted in the prompt; rotate at launch |
| Usage limits | Opus every two hours plus the build eats the plan | stays at nine runs a day; wire returns only when the plumbing is code; review 26 Oct |
| 4.0 attention | the newsroom pulls Alex off the launch | the build is Claude's and Jensen's time, not Alex's; his only actions are the three gates above |
| Domain plumbing | `buytrigger.club` DNS not on Cloudflare, or Mighty still answering | check on Sat; stage 1 uses a sub-address so nothing live moves until 19 Oct |
| Readers judge it by one edition | first impression on a quiet day | the "today so far" mode plays the whole day; early birds get the link after a full trading day is on the page, not at 07:00 |

### Alex's decisions needed

1. Stage 0: share the preview link with early birds from the week of 29 Sep (yes / not yet).
2. Stage 1: approve hosting on Cloudflare Pages and the feed table in the Research Supabase (Sat 26 Sep session).
3. The address: `news.buytrigger.club` for stage 1 (recommended) or straight to `buytrigger.club` at stage 2 only.

---

## Version 5 — 23 Sep: hosting and addresses, checked against the OS files

Checked on Alex's Mac (00_OS work records and the 4.0 decision pack, read only):

- **Member dashboard** = `dashboard.buytrigger.club`, React/Vite/Supabase, **hosted on GitHub Pages**, auto-deploys from `main` of `buytrigger-dashboard`.
- **Cloudflare** only ran the retired Command Centre (`os.alexkoh.me` / `os.buytrigger.club`, a Worker). Nothing the members use depends on it.
- Old OS memory notes say `dashboard.buytrigger.club` once carried a **free ten-stock preview with email capture**. Jensen to confirm on Sat whether that code is still in the repo — if so, the demo mode is largely built.

Changes to the plan (supersede the map and the stage-1 row above):

| Item | Was | Now |
|---|---|---|
| Hosting | Cloudflare Pages | **GitHub Pages, same as the dashboard** — no new provider. The newsroom is one static page. |
| Dashboard address | `buytrigger.club/app` | **`dashboard.buytrigger.club`** — already live; keep it |
| Stage 1 address | `news.buytrigger.club` | unchanged: a temporary side door so `buytrigger.club` is not touched before the 5 Oct early-bird opening |
| Stage 2 | `buytrigger.club` = the channel | unchanged; on 19 Oct `news.buytrigger.club` forwards to `buytrigger.club` so every shared link keeps working |
| DNS | — | one CNAME for `news` at whoever holds the `buytrigger.club` DNS; check Sat |

Final map at 19 Oct: `buytrigger.club` (news, free) → JOIN → sale · DASHBOARD → `dashboard.buytrigger.club` (demo for visitors, everything for members) · LOG IN → the dashboard's login.

---

## Version 6 — 23 Sep: flow triple-check, and who owns what

### The flow, walked end to end

| # | The move | Lands on | Status |
|---|---|---|---|
| 1 | Someone opens `buytrigger.club` | the news channel, free, no login, one screen | ready (page built) |
| 2 | Taps JOIN THE CLUB | the sale at `/join` — on hold, early bird by email, 13 of 30 | copy to write (Colette) |
| 3 | Taps DASHBOARD · DEMO | `dashboard.buytrigger.club` — ten stocks, JOIN banner | demo mode to build (Jensen); may already exist |
| 4 | Taps LOG IN | the dashboard's existing login → full dashboard | live today |
| 5 | Taps the wordmark from anywhere | back to the news | one shared top bar (Jensen) |
| 6 | A member opens the dashboard | Daily Summary with THE DAY SO FAR → WATCH THE CHANNEL | to build (Jensen) |
| 7 | Alex opens his private link | CONTENT and OS desk | live today, stays private |

### Five things the walk-through turned up

1. **`buytrigger.club` changes job.** The marketing roadmap has it as the shop, reached only from inside the letter ("one door" = Substack). From 19 Oct it becomes the free front page. The one-door rule still holds because the news page's FREE LETTER button points at Substack and nothing else captures email — but the roadmap line and the CLOSED copy must be rewritten. **Lisa's call, needed before 19 Oct.**
2. **`buytrigger.io` 301.** It points at `buytrigger.club`, which will be the news. The product name should land on the product: repoint it to `buytrigger.club/join`. **Lisa, one line.**
3. **Two hosts, one bar.** News on `buytrigger.club`, dashboard on `dashboard.buytrigger.club`. A logged-in member will still see "LOG IN" on the news page unless a small shared sign-in cookie is set on `.buytrigger.club`. Accept it for launch, or Jensen adds the cookie later. **Not a blocker.**
4. **Mighty.** `members.buytrigger.club` still sells 2.0. Retire or repoint at launch. **Lisa + Jensen.**
5. **"13 spots left" is updated by hand** until checkout exists. **Lisa owns the count.**

Nothing in the walk-through breaks. Items 1 and 2 are decisions, not build work.

### The website funnel work — stop or continue

There is no `3.17` in the OS registry. The live website-and-funnel work order is **BTOS-2026-007, Marketing Improvement Programme (Lisa, due 15 Oct)**: one door on Substack, `alexkoh.me` rebuilt in Carrd, the `buytrigger.io` 301, bios, YouTube slate, the Monday letter.

**It should not stop.** Only two of its items touch this build, and they are handed over rather than duplicated:

| Stays with Lisa (BTOS-2026-007) | Moves to the newsroom build |
|---|---|
| Substack as the one capture door | `buytrigger.club` front page = the news |
| `alexkoh.me` rebuild (Carrd) | the `/join` sale page (Colette writes the copy, Jensen builds it) |
| `buytrigger.io` 301 (repointed per item 2) | `dashboard.buytrigger.club` demo mode and the day-so-far block |
| bios, YouTube, Threads, the Monday letter | the shared top bar and routing |
| the 15 Oct 30-day re-check | |

Two dates to keep apart: BTOS-2026-007 re-checks on 15 Oct; the newsroom goes public on 19 Oct. Nothing collides.

---

## Version 7 — 23 Sep, 13:10 UK: no conflict, and we start today

Alex, 23 Sep: the newsroom lives at **news.buytrigger.club**; **3.17 is rebuilding `buytrigger.club` as the home page and soon the signup page**. That settles the two items Version 6 raised.

**Version 6 items 1 and 2 are closed, not escalated:**
- `buytrigger.club` keeps its job. It stays the shop / home page and 3.17 rebuilds it. The one-door rule is untouched: Substack stays the only capture door, and the news page's FREE LETTER button points there.
- The `buytrigger.io` 301 stays exactly as it is — it lands on `buytrigger.club`, which is still the product page. No change needed.
- `news.buytrigger.club` is now the **permanent** home of the channel, not a stage-1 side door. There is no 19 October address switch and no forwarding to set up. Every link shared from day one stays correct forever.

**What the two builds owe each other:** one block on the new home page pointing at the news, and one JOIN button on the news pointing back. That is the whole interface between them. Handover written: `claude/lisa-handover-newsroom.md`.

### DNS, checked live (23 Sep, 13:05 UK)

| Host | Answer | Reading |
|---|---|---|
| `buytrigger.club` | 172.66.0.70 | Cloudflare (proxied) — the DNS is already there |
| `dashboard.buytrigger.club` | 185.199.108–111.153 | GitHub Pages |
| `members.buytrigger.club` | 162.159.128.53 | Cloudflare — the old Mighty site |
| `buytrigger.io` | 207.207.210.x | elsewhere; 301 to the club |
| `news.buytrigger.club` | no record | to be added |

So: **hosting is GitHub Pages** (what the dashboard already uses, no Workers, no Pages build pipeline — none of what cost three days last time). The only Cloudflare touch is **one CNAME row** in the DNS panel, `news` → the GitHub Pages host. Five minutes, no build settings, no Workers.

### Revised schedule — starts today, not Saturday

Saturday was Alex's own date from 22 Sep, set when the plan was to finish 3.7.9 first. 3.7.9's Thursday pack does not need Claude's hands, so the build starts now.

| When | What | Needs Alex |
|---|---|---|
| **today** | repo scaffold for the static news page; the page reads a public feed instead of the Claude store; Lisa's handover (done) | no |
| **Wed–Thu** | feed table in the Research Supabase + one filing endpoint; the run files to both places during changeover | **yes — approve the Supabase table (read-only public) and the filing token** |
| **Thu–Fri** | page deployed to GitHub Pages at a `github.io` address; second checker added; heartbeat alert for missed runs | **yes — GitHub repo (new, public or private) created** |
| **Fri/Sat** | `news` CNAME added; compliance pass on fixed copy | **yes — one DNS row; fca-check** |
| **w/c 29 Sep** | early-bird preview link | **yes — go** |
| **19 Oct** | public: news channel + 3.17 home page + JOIN live | **yes — go** |

Nothing above competes with Lane 1 or with 4.0. Alex's actions are four short approvals, no build time.

---

## Version 8 — 23 Sep, 17:30 UK: the address map Alex set, and the feed is built

### Addresses, final

| Address | Job | When |
|---|---|---|
| `news.buytrigger.club` | the news channel | now → 19 Oct |
| `buytrigger.club` | **becomes the news home** at 19 Oct; today's home page moves to a join page | 19 Oct |
| `buytrigger.club/join` (or `join.buytrigger.club`) | the sale — today's Carrd home page, moved | 19 Oct |
| `dashboard.buytrigger.club` | **the member door.** LOG IN lands here. Bookmarked or saved to an iPhone home screen it opens straight into the member's session | live today |
| `members.buytrigger.club` | Mighty, the 2.0 community. Untouched by this build; retire or repoint when Mighty retires | — |

**Settled 23 Sep:** the member door is `dashboard.buytrigger.club`, which is already live on GitHub Pages with its own
Supabase login. Nothing to move, no DNS change, and no clash with Mighty. `members.buytrigger.club` stays where it is.

**On auto-login, honestly:** it works, with one caveat. The dashboard signs in through Supabase, which keeps the
session in the browser's own storage. Saved to an iPhone home screen the site gets its own storage container, so it
reopens signed in — that is the PWA behaviour Alex is describing and it is real. The caveat: the sign-in refreshes
itself while the member visits, but if nobody opens it for a long stretch the token finally expires and they sign in
once more. So "add to home screen and you are in" is true for anyone who uses it weekly.

### Built today, waiting on Alex's keys

In the Research repo, `Project/active/3.7.15 Agentic Newsroom/web/`:

- `supabase/migrations/20260923_newsroom_feed.sql` — `newsroom_editions` (public read, no public write, row-level
  security on) and `newsroom_filings` (private append-only log of every filing).
- `supabase/functions/newsroom-file/index.ts` — the only door into the feed. One bearer token. Three actions:
  file, checked, withdraw. The service key never leaves Supabase.
- `RUN_SHEET.md` — five commands for Alex, with a test before the run touches anything, and a table of what breaks.

Claude cannot run these from here: the keys live on Alex's Mac and are never read by Claude. What comes back to
Claude is the **anon key only** — designed to be public, sits in the page source.

### Live now

The public teaser page is published as its own artifact: today's editions baked in, no login button, no OS or
CONTENT tab in the source, PREVIEW ribbon, FREE LETTER and JOIN buttons, compliance footer on every screen.
Alex shares it when he flips it to "anyone with the link". It is a preview, not the live channel — the editions
are a snapshot until the feed above is switched on.
