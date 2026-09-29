# START HERE — BuyTrigger Newsroom & Automation (BTRES-3.7.15)

_For the first chat in the new Claude project. Written 29 Sep 2026 by the swarm chat, which moved out of the "BuyTrigger Dashboard" project so that project stays pure dashboard engineering._

## What this project covers

Work item **BTRES-3.7.15 — Agentic Newsroom**. Every chat carries one of these labels in its name:

| Label | What | Main record |
|---|---|---|
| **3.7.15 Newsroom** | the writer (Daily Brief task, 13 runs a weekday), the watchdog, buytrigger.club, the feed in the Research Supabase project | Dashboard project doc `claude/newsroom-live-status.md` (to be copied here) |
| **3.7.15 Swarm** | L1 fast posts (auto-publish after Colette + Lisa), L2 story threads, L3 weekly article, the Lisa draft desk, the 5-a-day ceiling | this repo: `bees/`, `rules/`, `docs/LOG.md` |
| **3.7.15 Desk feed** | what the member Desk reads from the feed | Dashboard project doc `claude/member-desk-phase1-status.md` (the Desk page itself stays a dashboard job) |

Not here: the dashboard app (`src/`, member access, releases) — that stays in the **BuyTrigger Dashboard** project with its plain numbers (3.9, 3.17, 3.18 …). CRM keeps its own chat.

## Live scheduled tasks (do not edit without the change-control rule below)

| Task | Id | When (UK) | Model |
|---|---|---|---|
| Newsroom writer (Daily Brief) | `trig_01MnsDBLPFNiHguXRQjFPohq` | 06:45, 08:45, 10:45, then hourly 13:45–22:45, weekdays | Opus 5 |
| Newsroom watchdog | `trig_016riCgZvbeVLBsUMpC5HoF9` | 50 min after each writer slot | Opus 5 |
| L1 fast posts | `trig_01KFVJK2ZFogDj93EojbMFMs` | 07:25, 16:25 weekdays | Opus 5.5 |
| L2 story thread | `trig_01MXnELxXcAqhEg9ffUBqnA8` | 23:10 weekdays | Fable 5.1 |
| L3 weekly article | `trig_018ybEdaU9BaHRYu2yFDWgRh` | 08:40 Sunday | Fable 5.1 |
| Lisa draft desk | `trig_01P6oNEgwm31f8LhJJ8PmvFR` | 09:05 daily | Opus 5.5 |

## Standing rules

1. **Everything reads the feed.** No bee researches; every number traces to a claim row at `ok`/`sec`.
2. **Change control for live tasks.** No model, schedule or publishing change without two good test runs of a copy that posts nothing public; then watch the first live run.
3. **The writer's and watchdog's filing-token line is never printed or changed** except at a planned rotation.
4. **At most 5 posts a day on the whole account**, 45 minutes apart (29 Sep). Any new scheduler must count the same way.
5. **Kill switch for L1:** `journalism/config` → `l1_autopost` on the private Newsroom page.
6. **One job, one chat, one label, one branch.** Read this file and the docs before building.
7. **Alex decides** models, schedules, what publishes, and anything member-facing. Plain language, one decision at a time, outcome first.

## Open items carried over (29 Sep)

- Push this repo to GitHub: the Mac's GitHub token must include `buytrigger-swarm` (github.com/settings/personal-access-tokens → Fine-grained tokens → Edit → add repo), then `git push -u origin main`.
- Allow `typefully-user-uploads.s3.amazonaws.com` so L2/L3 charts attach automatically.
- Saturday 09:25 UK L1 run so Friday evening stories don't expire (Alex to decide).
- Same 5-a-day ceiling for the Lisa draft desk and the explainer posts (Alex to OK).
- Weekly reach numbers: Typefully's analytics tools are not exposed to Claude at the moment; read X and Threads by browser once a week until they are.
- Copy the Newsroom docs from the Dashboard project into this one (list below).

## Docs to bring across from the BuyTrigger Dashboard project

`claude/newsroom-live-status.md` · `claude/newsroom-journalism.md` · `claude/newsroom-l1-autopost.md` · `claude/newsroom-daily-ceiling.md` · `claude/newsroom-three-surfaces.md` · `claude/newsroom-golive-closeout.md` · `claude/lisa-handover-newsroom.md` · `claude/newsroom-copy-pack.md` · `claude/newsroom-web-build-brief.md` · `claude/content-desk-state.md`
