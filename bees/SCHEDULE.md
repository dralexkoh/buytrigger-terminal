# The bees as scheduled tasks

Each bee runs as a Claude scheduled task. The prompt files in this folder are the source of truth; the scheduled task carries a copy. When a prompt changes here, the same text is pasted into the task (ask the swarm chat: "push bees/L2-story.md to the L2 task").

| Bee | File | Task id | Schedule (cron) | UK time | Status (wire row: 5 Oct 2026; others 29 Sep) |
|---|---|---|---|---|---|
| Layer 1 FAST | `L1-fast.md` | `trig_01KzwXrQ8gm6nk1bdabZhXXe` (Terminal project copy, 2 Oct; old `trig_01KFVJK2ZFogDj93EojbMFMs` retired) | `CRON_TZ=Europe/London 25 7,16 * * 1-5` | 07:25 and 16:25, Mon–Fri | enabled; auto-publishes after Colette + Lisa since 28 Sep; 5-a-day ceiling added 29 Sep 15:54 UK |
| Layer 1 WIRE | `L1-wire.md` | `trig_015H5pc8hi8a49npJEmpAA8T` | `CRON_TZ=Europe/London 15 7,9,11,14,15,16,17,18,19,20,21,22,23 * * 1-5` | 30 min after each writer slot, 13 runs a weekday | created 2 Oct; **LIVE from 5 Oct 2026, 10:57 UK** (`wire_autopost` true and MODE LIVE). First headline posted by a run itself 5 Oct 14:26 UK. No "Not advice." line (Alex, 5 Oct). Publish now, with a schedule-2-minutes-ahead fallback if that is refused. No daily cap; 4 min apart; shelf life by kind of news |
| Layer 2 STORY | `L2-story.md` | `trig_01Jts5fS2SfSGMYw2ud4QRLK` (Terminal project copy, 2 Oct; old `trig_01MXnELxXcAqhEg9ffUBqnA8` retired) | `CRON_TZ=Europe/London 10 23 * * 1-5` | 23:10, Mon–Fri | enabled; prompt as of 26 Sep 07:26 UK |
| Lisa draft desk | `lisa-desk.md` | `trig_01RFFUjtxUnUxuGoAczQH39z` (Terminal project copy, 2 Oct; old `trig_01P6oNEgwm31f8LhJJ8PmvFR` deleted) | `CRON_TZ=Europe/London 5 9 * * *` | 09:05 daily | enabled; reviews L2 drafts, schedules the good ones (weekdays 19:30, weekends 10:00), deletes expired and held L1 drafts. Owned by another chat; copied here for the record |
| Layer 3 ARTICLE | `L3-article.md` | `trig_01EWz1aFEbhX9YpLZNACDF8o` (Terminal project copy, 2 Oct; old `trig_018ybEdaU9BaHRYu2yFDWgRh` deleted) | `CRON_TZ=Europe/London 40 8 * * 0` | 08:40 Sunday | enabled; first run 27 Sep (VIX article, 3 charts, draft); prompt updated 29 Sep for 13 editions a day |

**Every cron here is London-time** (`CRON_TZ=Europe/London`), so the UK times above hold through the clock change on 25 October. Three of them lost that prefix when the tasks were re-created on 2 Oct and would have fired an hour early from 25 Oct; put back 2 Oct 23:45 UK (schedule only, prompts untouched, next runs unchanged). Any new or re-created task carries the prefix.

## Notes

- Layer 1 runs twice a weekday (renamed "2x weekdays" on 26 Sep). It never sees the 16:30–22:30 editions until the next morning; Friday evening's evergreens can expire before Monday. A Saturday 09:25 UK run would close that gap (Alex to decide).
- Kill switch: `journalism/config` on the Newsroom page, `l1_autopost`. Anything but `true` → drafts only.
- All three tasks run with automatic approval, which is what lets them finish unattended. They can only create Typefully drafts and write the `journalism` ledger; the prompts forbid everything else.
- The Daily Brief writer (`trig_01MnsDBLPFNiHguXRQjFPohq`, every two hours weekdays) is the Newsroom's, not the swarm's. Never edit it from here; its prompt carries a filing token.
- Version history of each prompt is this repo's git history. The first versions (24–25 Sep) lived only in the tasks; `docs/LOG.md` records what changed and when.

## Changing a prompt safely

1. Edit the file here. Keep the "Never" section intact.
2. Run the day's fixtures through `tools/score_stories.py` if the change touches selection, so you can see what the bee would have picked.
3. Push the text to the task (update the prompt only; leave the schedule and name alone unless that is the change).
4. Watch the next run's report. The report format is fixed at the bottom of each prompt so it is easy to scan.
5. Record the change in `docs/LOG.md` with the date.
