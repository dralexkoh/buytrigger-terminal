# START HERE — BuyTrigger Newsroom Terminal (BTRES-3.7.15)

_The first read for every chat in this project. Written 29 Sep 2026; renamed from "Newsroom & Automation" to the **Terminal** the same day on Alex's decision. The master plan is `claude/terminal-blueprint.md`._

## What the Terminal is

One machine: **gather** market news once (Tim's research desk), **publish** it to buytrigger.club and the members' Desk, **broadcast** it in four sizes (L1 headline · L2 thread with graphics · L3 article · L4 video, plus Telegram), **measure** what worked, and **control** it all from one screen. Alex: "the automatic Walter Bloomberg, a mini Bloomberg terminal."

## Labels — every chat and task carries one

| Label | What |
|---|---|
| **3.7.15 Terminal · Newsroom** | the writer (13 editions a weekday), the watchdog, buytrigger.club, the feed |
| **3.7.15 Terminal · Broadcast** | L1, L2, L3 (and L4 later), Colette + Lisa review, the Lisa draft desk, Telegram |
| **3.7.15 Terminal · Control Room** | the private status page, alerts, measurement, the 3.19 CRM & Funnel join |
| **3.7.15 Terminal · Desk feed** | what the members' Desk reads from the feed (the Desk page itself is a Dashboard job) |

Not here: the members' app (`buytrigger-dashboard`, the BuyTrigger Dashboard project). CRM has its own chat (3.19).

## Where things live

| Thing | Where |
|---|---|
| Plans, briefs, status records | this project's `claude/…` docs |
| Engine: bee prompts, rules, tools, ledger snapshots, control-room records | repo **`buytrigger-terminal`** (GitHub `dralexkoh/buytrigger-terminal`, Mac `Desktop/GitHub Project/buytrigger-terminal`) |
| Public site | repo `buytrigger-newsroom` → buytrigger.club |
| Feed and filings | Research Supabase project `paoxcmxteemakhyvwihn` |
| Private Newsroom page (editions, desk cards, ledger, kill switch) | artifact `MGGZNGHSGWtAGwo3kZNxZn` |

## Live scheduled tasks (all named `3.7.15 Terminal · …`)

| Task | Id | When (UK) | Model |
|---|---|---|---|
| writer (Daily Brief) | `trig_01MnsDBLPFNiHguXRQjFPohq` | 06:45, 08:45, 10:45, then hourly 13:45–22:45, weekdays | Opus 5 |
| watchdog | `trig_016riCgZvbeVLBsUMpC5HoF9` | 50 min after each writer slot | Opus 5 |
| **L1 wire** (BREAKING / UPDATE / DATA headlines) — **LIVE since 5 Oct 2026** | `trig_015H5pc8hi8a49npJEmpAA8T` | 30 min after each writer slot, 13 runs weekdays | Fable 5.1 |
| L1 fast posts (cards → threads) | `trig_01KzwXrQ8gm6nk1bdabZhXXe` | 07:25, 16:25 weekdays | Fable 5.1 |
| L2 story thread | `trig_01Jts5fS2SfSGMYw2ud4QRLK` | 23:10 weekdays | Fable 5.1 |
| L3 weekly article | `trig_01EWz1aFEbhX9YpLZNACDF8o` | 08:40 Sunday | Fable 5.1 |
| Lisa draft desk | `trig_01RFFUjtxUnUxuGoAczQH39z` | 09:05 daily | Fable 5.1 |

Ids changed on 2 Oct when L1, L2, L3 and the Lisa desk were re-created from this project (`claude/terminal-tasks-rehoming.md`); the four old ids are deleted. The writer and the watchdog stay under the Dashboard project because their prompts carry the filing token. **Every cron is London-time** — see `bees/SCHEDULE.md`.

## Standing rules

1. **Everything reads the feed.** No bee researches; every number traces to a claim row at `ok`/`sec`.
2. **Change control for live tasks.** No model, schedule or publishing change without two good test runs of a copy that posts nothing public; then watch the first live run.
3. **The filing-token line** in the writer and watchdog prompts is never printed or changed except at a planned rotation.
4. **At most 5 posts a day on the whole account**, 45 minutes apart. Every scheduler counts the same way (L1 and the Lisa desk do since 29 Sep).
5. **Kill switches:** `journalism/config` → `l1_autopost` (L1 fast posts) and `wire_autopost` plus the wire task's own `MODE:` line (the wire; both must say live). Alex flips them from the SWITCHES panel on the control room. **Wire headlines carry no "Not advice." line** (Alex, 5 Oct 2026); they stay bare sourced facts.
6. **One job, one chat, one label, one branch.** Read this file and the blueprint before building.
7. **Alex decides** models, schedules, what publishes, new channels, and anything member-facing. Plain language, one decision at a time, outcome first.

## Status 5 Oct 2026

The wire is live and posts by itself (first one 14:26 UK, 5 Oct). The current open list is in the project doc `claude/START-HERE.md` and `claude/closeout-2026-10-05.md`; the list below is the 29 Sep one, kept for the record.

## Open items (29 Sep)

- Push the `buytrigger-terminal` repo to GitHub: the Mac's GitHub token must include the repo (github.com/settings/personal-access-tokens → Fine-grained tokens → Edit → Repository access), then `git push -u origin main`.
- Allow `typefully-user-uploads.s3.amazonaws.com` so L2/L3 charts attach automatically.
- Saturday 09:25 UK L1 run so Friday-evening stories don't expire (Alex to decide).
- Reach numbers: Typefully's analytics tools are not exposed to Claude at the moment; read X and Threads by browser weekly until they are.
- Blueprint decisions (§7 of `claude/terminal-blueprint.md`): X links, Telegram channel, breaking allowance, frequency.
