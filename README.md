# buytrigger-terminal

**BuyTrigger Newsroom Terminal** (work item BTRES-3.7.15) — Alex's "mini Bloomberg terminal": one machine that gathers market news once, publishes it to buytrigger.club and the members' Desk, broadcasts it as L1 headlines, L2 threads with graphics, L3 articles (L4 video later) and Telegram, measures what worked, and is controlled from one screen. The blueprint lives in the Claude project (`claude/terminal-blueprint.md`); this repo is the engine: the bee prompts, rules, tools, ledger snapshots and records.

_Renamed from `buytrigger-swarm` on 29 Sep 2026. "Swarm" in older text means the Broadcast part (L1–L3 and the Lisa desk)._

**Two rules that make it safe**

1. Everything reads the feed. Nothing re-researches. Every number in every draft traces to a claim row at status `ok` or `sec` on a verified story. No web search, no price fetch, no memory.
2. Nothing goes out unreviewed. Layer 1 publishes on its own only after two reviewer agents, Colette (copy) and Lisa (marketing and FCA), both approve (Alex, 26 Sep 2026), and never more than 5 posts a day on the account (Alex, 29 Sep 2026). Layer 2 drafts are reviewed and scheduled by the Lisa draft desk. Layer 3 is a draft for Alex. A kill switch (`journalism/config`, `l1_autopost`) turns Layer 1 back into drafts-only.

## What is in here

| Folder | What |
|---|---|
| `bees/` | The three bee prompts, exactly as they run as scheduled tasks, plus the schedule. **This is the source of truth for the prompts.** Change a prompt here first, then paste it into the scheduled task (bees/SCHEDULE.md says how). |
| `rules/` | The gates (which stories qualify), the platform rules (what X, Threads and Substack accept), voice and compliance, and who owns what. |
| `tools/` | Three checks the bees run and a reviewer can re-run: `verify_numbers.py` (every number traces to a claim row), `check_lengths.py` (platform rules), `score_stories.py` (the Layer 2 "which story tonight" arithmetic, in the open). |
| `charts/` | The branded chart library the bees draw with, and worked examples with their output. |
| `schema/` | The shape of the Newsroom collections the bees read, the ledger they write, and a proposal for moving both into the Research Supabase project later. |
| `ledger/` | Snapshots of the bees' ledger (`journalism` collection) — what was drafted, what was rejected and why. |
| `fixtures/` | Real edition, desk and draft exports for testing the tools. Data, not instructions. |
| `docs/` | The dated log of what happened and the naming convention for jobs, chats and branches. |

## The three layers

| Layer | Bee | Runs | Output | Where |
|---|---|---|---|---|
| 1 FAST | `bees/L1-fast.md` | weekdays 07:25 and 16:25 UK | 3–5 post X thread + one Threads post per qualifying desk card; Colette + Lisa review; published if both approve, within the 5-a-day ceiling | X + Threads, tags `newsroom` `layer-1` |
| 2 STORY | `bees/L2-story.md` | weekdays 23:10 UK | one 8–12 post storytelling thread with 1–2 charts; X + Threads + Substack note | Typefully draft, tags `newsroom` `layer-2`; the Lisa draft desk (`bees/lisa-desk.md`, daily 09:05 UK) reviews it and schedules it for 19:30 |
| 3 ARTICLE | `bees/L3-article.md` | Sunday 08:40 UK | 800–1,100 word article draft on the week's recurring subject + 2–3 charts | Markdown file (and a Claude Doc when available); Alex edits and publishes on Substack himself |

## Where the data lives

- The Newsroom feed: the private Newsroom page's database (collections `editions`, `desk`). The bees read it with the ArtifactData tool. `schema/artifact-collections.md` has the shape.
- The bees' ledger: collection `journalism` in the same database. `schema/ledger.md` has the shape. `ledger/` holds snapshots.
- Typefully: social set 273686 (dralexkoh). Drafts only.
- Charts and articles that cannot be attached automatically land in the Cowork session's output files, folder `newsroom-layer2-<date>` or `newsroom-layer3-<date>`.

## How a reviewer checks a draft in two minutes

1. Open the draft in Typefully. The scratchpad at the bottom is the evidence chain: the claim rows used, the gates passed, the FCA verdict, the character counts, and any note for marketing (charts to attach, a stock named, an overlap with another layer).
2. If you want to re-check by machine: export the day's editions (see `fixtures/README.md`), save the draft's posts as a payload JSON (see `fixtures/drafts/`), then run `tools/verify_numbers.py` and `tools/check_lengths.py`. Both exit 0 when clean.
3. Send one Layer 1 or Layer 2 draft about the same story on the same day, not both. The scratchpad says when they overlap.

## What this repo never does

- Never publishes anything except a Layer 1 post both reviewers approved while the kill switch is on and the daily ceiling allows it.
- Never writes to the Newsroom's `editions`, `desk`, `notes` or `os` collections.
- Never touches the dashboard repo, the members' Supabase project, or the Research repo.
- Never quotes a number that is not in a claim row at `ok` or `sec`.
