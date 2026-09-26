# The bees as scheduled tasks

Each bee runs as a Claude scheduled task. The prompt files in this folder are the source of truth; the scheduled task carries a copy. When a prompt changes here, the same text is pasted into the task (ask the swarm chat: "push bees/L2-story.md to the L2 task").

| Bee | File | Task id | Schedule (UTC cron) | UK time | Status 26 Sep 2026 |
|---|---|---|---|---|---|
| Layer 1 FAST | `L1-fast.md` | `trig_01KFVJK2ZFogDj93EojbMFMs` | `25 6,15 * * 1-5` | 07:25 and 16:25, Mon–Fri | enabled; last run 25 Sep 16:25 UK succeeded (2 drafts) |
| Layer 2 STORY | `L2-story.md` | `trig_01MXnELxXcAqhEg9ffUBqnA8` | `10 22 * * 1-5` | 23:10, Mon–Fri | enabled; last run 25 Sep 23:11 UK succeeded (1 draft); prompt updated 26 Sep 07:26 UK to this file |
| Layer 3 ARTICLE | `L3-article.md` | `trig_018ybEdaU9BaHRYu2yFDWgRh` | `40 7 * * 0` | 08:40 Sunday | enabled; first run due Sun 27 Sep |

UTC crons read as UK time + 1 hour while British Summer Time lasts (until 25 Oct 2026). After the clocks change, the UK times above become 06:25/15:25, 22:10 and 07:40 unless the crons are moved an hour later.

## Notes

- The Layer 1 task is named "4x weekdays" but its schedule is two runs a day. It was changed from the original four-run schedule by someone other than the swarm chat on 25 Sep. Left as found; Alex to confirm. Four runs would be `25 6,9,12,15 * * 1-5` (07:25, 10:25, 13:25, 16:25 UK).
- All three tasks run with automatic approval, which is what lets them finish unattended. They can only create Typefully drafts and write the `journalism` ledger; the prompts forbid everything else.
- The Daily Brief writer (`trig_01MnsDBLPFNiHguXRQjFPohq`, every two hours weekdays) is the Newsroom's, not the swarm's. Never edit it from here; its prompt carries a filing token.
- Version history of each prompt is this repo's git history. The first versions (24–25 Sep) lived only in the tasks; `docs/LOG.md` records what changed and when.

## Changing a prompt safely

1. Edit the file here. Keep the "Never" section intact.
2. Run the day's fixtures through `tools/score_stories.py` if the change touches selection, so you can see what the bee would have picked.
3. Push the text to the task (update the prompt only; leave the schedule and name alone unless that is the change).
4. Watch the next run's report. The report format is fixed at the bottom of each prompt so it is easy to scan.
5. Record the change in `docs/LOG.md` with the date.
