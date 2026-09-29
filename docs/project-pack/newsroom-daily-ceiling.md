# Newsroom — daily post ceiling (29 Sep 2026)

_Decision record. Adds to `claude/newsroom-l1-autopost.md`; the live prompt there is now one step longer (step 3b below)._

## The decision

Tue 29 Sep, the account had 5 posts out or booked before L1's 16:25 run (launch post 12:00, AMD explainer 13:33, Nvidia buyback explainer 15:26, L2 rates thread 19:30, Meta explainer 21:00), and L1 had 4 cards waiting. The Nvidia explainer repeated L1's Monday post on the same buyback. Alex: **"yeah add daily ceiling"**.

## What the L1 bee does now (live on `trig_01KFVJK2ZFogDj93EojbMFMs` from 15:54 UK, 29 Sep)

- Step 1 counts **every post on social set 273686** published earlier that UK day or scheduled for later that day — any source: L1, L2, explainers, launch posts, Alex's own. That is TODAY'S COUNT.
- **Step 3b — DAILY CEILING:** at most **5 posts a day** on the account. If TODAY'S COUNT is already 5 or more, the run publishes nothing; cards that passed the gates are left unfinished (not drafted, not in the ledger) so the next run can take them if their window is still open. Otherwise it publishes at most (5 − TODAY'S COUNT), best cards first. Never within **45 minutes** of another post.
- Step 8 (publish) now also requires the ceiling to allow it.
- Nothing else in the prompt changed. Kill switch, Colette + Lisa, dedupe and all platform rules are as in `claude/newsroom-l1-autopost.md`.

## Not covered (other chats' tasks)

The ceiling lives in L1 only. The Lisa draft desk (`trig_01P6oNEgwm31f8LhJJ8PmvFR`) has its own rule (fewer than 4 posts that day, 90 minutes apart) and the explainer posts come from another chat. Whoever owns those should count the same way — every post on the account, 5 a day — so the three schedulers agree.

## Where the record also lives

`buytrigger-swarm` repo: `bees/L1-fast.md` (exact live text), `rules/gates.md`, `docs/LOG.md` (29 Sep). Written to Alex's Mac; commit and push pending (the Mac disconnected mid-write, and the GitHub token does not yet cover the new repo).
