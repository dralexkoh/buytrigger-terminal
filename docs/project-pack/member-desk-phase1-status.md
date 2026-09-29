# 3.18 Member Desk — CLOSED · live as v3.9.0 (25 Sept 2026) · follow-up v3.9.1 live (26 Sept)

_Closed 25 Sept 2026, evening; follow-up v3.9.1 closed 26 Sept. The close-out of record is in the repo: `Project/closeouts/CLOSEOUT_3.18_Member_Desk_2026-09-25.md` (§6 covers v3.9.1). The build record with every addendum: `Project/active/3.18 Member Desk/BUILD_RECORD_phase1_2026-09-25.md`. This doc is the pointer and the open list. The chat that built 3.18 is archived — start the next Desk work from this list._

## What is live

- **`dashboard.buytrigger.club/desk` is the members' home** since 25 Sept 2026 (v3.9.0). Login and the bare address land there; the Daily Summary is out of the members' nav (route kept for bookmarks; the Free product still lands on `/free/summary`). Desk is the centre tab on the phone bar, first in the sidebar, the only NEW badge; the installed app opens on it and has a "The Desk" shortcut.
- The page: rotating Newsroom lead (nine seconds a story, pause/step/jump) with the **evidence** members-only; rundown + Coming up (member's names first); **Your Portfolio with a tracking strip per saved slot** (live since save vs S&P, weights only) above the stock rows; watchlist; the Board; macro desk with **VIX zones 22 / 24 / 28** (Alex); club strip.
- Built in one day from the approved canvas; 416 tests; zero AI tokens at runtime; the feed is a one-row check per minute with editions pulled only on change.

## Follow-up — v3.9.1, 26 Sept 2026 (close-out §6, build record addendum 5) — LIVE

**Member space link.** Alex: a link to members.buytrigger.club from inside the dashboard, without cluttering it. Two places, nothing else moved: the Desk's club strip (`MEMBER SPACE →` next to `NEWSROOM →`) and one **Member space** row, last under MORE in the desktop sidebar and the phone hamburger menu. Both come from one setting, `links.memberSpace` in `src/data/deskClub.json` (`https://members.buytrigger.club/`); null hides both. Outside link, new tab, members only, never a bottom tab; the member space keeps its own sign-in — no auth, Supabase, entitlement or data change. Commit `0604fcfd`, pushed by Alex 26 Sept (GitHub `main` `5951fa67`); **verified in the live bundle** on dashboard.buytrigger.club (v3.9.1 + the link). Tests 416 (3 new), build clean, screenshots `.qa/shots/member-space-*.png`.

This is item 5 of `claude/member-access-decision.md` ("Club item in the dashboard nav, opening Mighty") — marked done there. `members.buytrigger.club` stays: Mighty remains the paying home (that doc, item 9). Do not add a second "Community" item.

## Follow-up — 28–29 Sept 2026: Newsroom coverage and the Desk's edition times — LIVE

- **Why members saw no Meta or Nu news (Alex, 28 Sept):** the Newsroom writer only researched a handful of names. Fixed upstream in the writer's prompt (whole 119-name universe, top ten every run, news sweep, fair share); no Desk code change was needed. The Desk's name matching was tested against Meta / Nu stories and works. Record: `claude/newsroom-live-status.md` §00–00d.
- **`tickers` per story (item 6 below) — done 28 Sept.** Every edition since 20:30 UK, 28 Sept carries `tickers`; the Desk uses it in preference to name matching.
- **Next-edition label:** the Newsroom moved to 13 editions a weekday (06:45, 08:45, 10:45, then hourly 13:45 → 22:45 UK) on 29 Sept. `EDITION_SLOTS_UK` in `src/utils/desk.js` and the two tests updated; 416 tests pass, build clean (cloud copy); commit `192690cba`, pushed by Alex 29 Sept; **verified live** 16:24 UK (the Desk chunk carries the new slots and none of the old).
- The Desk shows whatever the public feed holds. On 29 Sept two editions reached the private Newsroom page but not the feed for about an hour each; a watchdog task now checks the feed after every edition (`claude/newsroom-live-status.md` §00d).

## Still open (close-out §4) — future scopes, none blocking

1. **Free-tier Desk** — `/free/desk`, levels blurred, portfolio locked. Alex to schedule.
2. **NEAR SELLTRIGGER band** — placeholder 10 % (`NEAR_SELLTRIGGER_PCT` in `src/utils/desk.js`).
3. **Club strip config** — `src/data/deskClub.json`: member space link set (26 Sept); next live session and Telegram link still null.
4. **PU flag** — shows only where the sheet writes "(PU)"; one-line sync change if exact PU is wanted.
5. **Phase 2 remainder** — since-you-last-looked + recent moves (detector built and tested), last-visit key, **Alex's desk note** (Sheet `Desk` tab recommended, or a table — Alex to choose), earnings dates in Coming up.
6. ~~Newsroom chat: add `tickers: []` per story.~~ — done 28 Sept (see follow-up above).
7. Footer under the dark page — keep or restyle.
8. Rotation speed (9 s) — one constant.
9. Retire `/summary` once page views show nobody lands there.
10. First-day watch on Monday: feed load and `closes.json` cache on phones.
11. The loop back — a link from the member space to the dashboard lives on the community side (Alex).

## Mac device-bridge lessons (for any chat committing in this repo — also in the repo's `CLAUDE.md` → Git Workflow)

- `git checkout <branch>` cannot rewrite files on the Mac VM (no unlink): switch with `git symbolic-ref HEAD refs/heads/<branch> && git reset -q` only when the working tree already matches; fast-forward with `git branch -f <branch> <tip>` needs no file writes.
- Stale `.git/*.lock` and `.git/refs/heads/<branch>.lock` files block the next commit; move them into `.git/_stale/`.
- **iCloud-style duplicates inside `.git`** (26 Sept): files named `refs/heads/main 2`, `index 2`, `AUTO_MERGE 2` appeared and broke Alex's `git pull` with `fatal: bad object refs/heads/main 2`. Fix: move every `* 2` file under `.git` into `.git/_stale/` (`find .git -name "* 2" -o -name "* 2.*"`). Likely cause: the repo lives on the Desktop, which iCloud syncs; moving the GitHub Project folder off the Desktop would stop it.
- Other chats leave uncommitted edits in the same tree (e.g. 3.17 website files, the 4.0 checklist): stage files by name, never `git add -A`.
- A branch checked out in the shared tree catches other chats' "commit on main" — it happened once on 25 Sept and was fast-forwarded onto `main`. The tree is left on `main`. The `the-desk` branch is fully merged and can be deleted any time.
- The data bot commits to `main` on GitHub through the day: Alex pushes with `git pull --no-rebase --no-edit && git push origin main`.
- **29 Sept:** the Mac can drop off the bridge mid-command. A commit reported as sent may not have landed — check `git log -3` and `git status -sb` ("ahead 1") before telling Alex to push.
