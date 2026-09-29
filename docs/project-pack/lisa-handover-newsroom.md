# Handover to Lisa — the newsroom and the funnel, from 23 September

_From Marissa (OS Control) to Lisa (Marketing Director). Work items: BTRES-3.7.15 Agentic Newsroom (Tim/Claude), BTOS-2026-007 Marketing Improvement Programme (Lisa), 3.17 home page and signup page rebuild. Nothing here changes BTOS-2026-007's scope or its 15 October re-check._

**Updated 24 September.** Three things changed since the first version: the public launch moved from 19 October to **26 October**; the news channel went **live** at news.buytrigger.club; and the seat-count line ("13 of 30 places left") is **withdrawn** — the offer is a 25% first-year discount ending Sunday 25 October, with no seat count anywhere. The old line was the riskier form under the compliance check and should not appear on any page.

## The one-line version

BuyTrigger has a free, always-on news channel, live now at **news.buytrigger.club**. It does not touch **buytrigger.club**, which 3.17 is rebuilding as the home page and signup page. The two are separate addresses doing separate jobs, and they link to each other.

## What the newsroom is

A rolling news channel for family investors, written every two hours on weekdays (06:30 to 22:30 UK) by an automated research run and filed with evidence behind every number. Each edition opens with "why the market is up or down", then a plain-English VIX read, then stocks from the BuyTrigger universe. Headlines are written for a reader who is not a trader. Every number carries a source; members can see the source table, visitors see a lock.

It is free and needs no login. It is the top of the funnel — the thing people come back to daily without paying.

## What this means for the funnel

Nothing in the one-door rule changes. Substack stays the only capture door, and the news page's SUBSTACK button points there. The news page collects no emails of its own.

The map after both builds land:

```
news.buytrigger.club      the news channel — free, no login, the daily habit
                          top bar: SUBSTACK → the letter · LOG IN → dashboard · JOIN THE CLUB → buytrigger.club
buytrigger.club           the home page and signup page — 3.17, Lisa's build
                          add one line and one button: "The news, free, every day" → news.buytrigger.club
                          from 26 Oct this address becomes the news home and the join page moves
dashboard.buytrigger.club the member product — GitHub Pages, live today. The ONLY login door
dralexkoh.substack.com    the free letter — the one capture door, unchanged
alexkoh.me                the person page — Carrd, BTOS-2026-007, unchanged
buytrigger.io             301 → buytrigger.club, unchanged
```

**One login, not two.** Decided 24 September: there is a single Log in button and it goes to `dashboard.buytrigger.club`. The Club is reached from inside the dashboard, not as a second front door. Any design carrying "Club log in" and "Dashboard log in" as separate choices is out of date — see `claude/member-access-decision.md`.

## What Lisa and Colette are asked for

1. **One block on the new home page** (3.17): a line and a button pointing at the news channel. Suggested line: "The news, free, every day — the same evidence the system runs on." Copy is Colette's; a paste-ready version is in `claude/newsroom-copy-pack.md` section 2.
2. **The sale page copy** for the club. Before 5 October it is the doors-closed form: name and email to Alex, who sends the join link himself, nothing to pay yet. From 5 October the early-bird form. Full copy for both, already compliance-checked, is in `claude/newsroom-copy-pack.md` sections 3 and 4. This can live inside the 3.17 signup page rather than as a separate page — Lisa's call.
3. **No seat count, ever.** The offer is 25% off the first year, ending Sunday 25 October. No "places left", no countdown, no "last chance". The wording is only ever "early bird discount".
4. **Compliance**: the news channel is a public page about markets, so the fixed copy carries "research and education only, not advice", never a position, never "you should". An `fca-check` pass is needed on the news page's fixed copy and on the sale copy before either goes wider.
5. **Mighty** (`members.buytrigger.club`, still selling 2.0) needs retiring or repointing. Now that Stripe is the source of truth for membership and Mighty is community only, this is a tidy-up rather than a dependency — after 26 October is fine.

## What Lisa is NOT asked for

The news channel itself — its build, its writing, its hosting and its evidence rules sit with Claude, Tim and Jensen. No marketing sign-off is needed for it to go live beyond the compliance pass and Alex's go.

## Dates

| When | What | Who |
|---|---|---|
| 24 Sep | news channel **live** at news.buytrigger.club, preview ribbon on | done |
| w/c 29 Sep | early-bird preview link shared more widely | Alex |
| 5 Oct | BT4.0 early-bird opening, 25% off the first year | Alex |
| 15 Oct | BTOS-2026-007 30-day re-check | Lisa |
| 25 Oct | early-bird discount ends | Alex |
| **26 Oct** | public launch: news channel open, 3.17 home page live, JOIN live | Alex's go |

Two dates that look close but do not collide: the 15 October re-check is a measurement, the 26 October launch is a release.

**One question for Alex, raised by the date move.** The discount ends Sunday 25 October and the doors open to the public on Monday 26 October. As the copy pack is written, the public sale page says the 25% is "still on until Sunday 25 October" — which can never be true. Either the discount runs past the launch, or the public page opens at full price with no discount line. One paragraph of copy either way.
