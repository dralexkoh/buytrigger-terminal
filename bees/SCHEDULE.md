# The bees as scheduled tasks

Each bee runs as a Claude scheduled task. The prompt files in this folder are the source of truth; the scheduled task carries a copy. When a prompt changes here, the same text is pasted into the task (ask the swarm chat: "push bees/L2-story.md to the L2 task").

| Bee | File | Task id | Schedule (UTC cron) | UK time | Status 29 Sep 2026 |
|---|---|---|---|---|---|
| `3.7.15 Terminal · L1 fast posts` | `L1-fast.md` | `trig_01KFVJK2ZFogDj93EojbMFMs` | `25 6,15 * * 1-5` | 07:25 and 16:25, Mon–Fri | enabled; auto-publishes after Colette + Lisa since 28 Sep; 5-a-day ceiling added 29 Sep 15:54 UK |
| `3.7.15 Terminal · L2 story thread` | `L2-story.md` | `trig_01MXnELxXcAqhEg9ffUBqnA8` | `10 22 * * 1-5` | 23:10, Mon–Fri | enabled; prompt as of 26 Sep 07:26 UK |
| `3.7.15 Terminal · Lisa draft desk` | `lisa-desk.md` | `trig_01P6oNEgwm31f8LhJJ8PmvFR` | `CRON_TZ=Europe/London 5 9 * * *` | 09:05 daily | enabled; reviews L2 drafts, schedules the good ones (weekdays 19:30, weekends 10:00), deletes expired and held L1 drafts. Owned by another chat; copied here for the record |
| `3.7.15 Terminal · L3 weekly article` | `L3-article.md` | `trig_018ybEdaU9BaHRYu2yFDWgRh` | `40 7 * * 0` | 08:40 Sunday | enabled; first run 27 Sep (VIX article, 3 charts, draft); prompt updated 29 Sep for 13 editions a day |

UTC crons read as UK time + 1 hour while British Summer Time lasts (until 25 Oct 2026). After the clocks change, the UK times above become 06:25/15:25, 22:10 and 07:40 unless the crons are moved an hour later.

## Notes

- Layer 1 runs twice a weekday (renamed "2x weekdays" on 26 Sep). It never sees the 16:30–22:30 editions until the next morning; Friday evening's evergreens can expire before Monday. A Saturday 09:25 UK run would close that gap (Alex to decide).
- Kill switch: `journalism/config` on the Newsroom page, `l1_autopost`. Anything but `true` → drafts only.
- All three tasks run with automatic approval, which is what lets them finish unattended. They can only create Typefully drafts and write the `journalism` ledger; the prompts forbid everything else.
- The writer (`3.7.15 Terminal · writer`, `trig_01MnsDBLPFNiHguXRQjFPohq`, 13 runs a weekday) and the watchdog (`trig_016riCgZvbeVLBsUMpC5HoF9`) are the Newsroom part of the Terminal. Never edit them without the change-control rule; both prompts carry the filing token.
- All tasks were renamed `3.7.15 Terminal · …` on 29 Sep 2026 (names only).
- Version history of each prompt is this repo's git history. The first versions (24–25 Sep) lived only in the tasks; `docs/LOG.md` records what changed and when.

## Changing a prompt safely

1. Edit the file here. Keep the "Never" section intact.
2. Run the day's fixtures through `tools/score_stories.py` if the change touches selection, so you can see what the bee would have picked.
3. Push the text to the task (update the prompt only; leave the schedule and name alone unless that is the change).
4. Watch the next run's report. The report format is fixed at the bottom of each prompt so it is easy to scan.
5. Record the change in `docs/LOG.md` with the date.
