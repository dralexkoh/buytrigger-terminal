# Close-out — Newsroom go-live, 24 September 2026

_Dated close-out for the chat that took the Newsroom public. Written 26 September. Work item `BTRES-3.7.15` stays OPEN — surfaces 2 and 3 and the 4.0 release run on. This records what that session delivered, what is still true, and where the live records are._

## Delivered

- **`buytrigger.club` is the Newsroom.** Moved off Carrd onto GitHub Pages (repo `dralexkoh/buytrigger-newsroom`), four apex A records at Porkbun, Let's Encrypt certificate, Enforce HTTPS on. No Cloudflare in the path.
- **It updates itself.** The Daily Brief run files each edition to Supabase (`newsroom_editions`, Research project) and the page polls every 60 seconds. First unattended filing 24 Sep, 11:43 UTC. No rebuild, no upload, no session needed.
- **Never goes blank.** 18 editions are baked into the page; if the feed is empty or unreachable they stay on screen.
- **One login door.** `SUBSTACK · LOG IN · JOIN THE CLUB`, with LOG IN going to `dashboard.buytrigger.club`. Decided the same day: Stripe is the source of truth for membership, Mighty is community only (`claude/member-access-decision.md`).
- **`news.buytrigger.club` deleted.** JOIN points at `buytrigger.carrd.co` until 3.17's page becomes `/join`.
- **Page work:** five lines of story text on phones, round logo, one-line preview and legal strips, three-second edition notice queued for the next build.

## Still true on 26 September

| | |
|---|---|
| Daily Brief | nine runs a weekday, Opus 5, `trig_01MnsDBLPFNiHguXRQjFPohq` |
| THE WIRE | **still paused in the run's prompt.** Armed by the Sunday task before Monday's first run |
| Sunday review | `trig_01Sh2kPm19mAnstkAnNwgmjK`, fires 27 Sep 07:30 UTC — measures the trial, arms the wire, recommends frequency |
| Frequency | unchanged, by Alex's instruction. Proposal on the table: hourly through the US session, 13 runs against 9 |
| Content desk | 26 cards proposed, 1 approved. Now superseded by the L1/L2/L3 bees built since |

## Open, and nothing scheduled covers it

**The early-bird discount ends Sunday 25 October; the public launch is Monday 26 October.** The sale copy in `claude/newsroom-copy-pack.md` section 4 says the 25% is "still on until Sunday 25 October" on a page that does not go up until the 26th. That sentence can never be true. Either the discount runs past the launch, or the public page opens at full price. One paragraph, Alex's call, needed before the 5 October early-bird opening. A reminder is set for 2 October.

## Three things learned, kept because they cost time

1. **Committing a file by staged path can write a stale copy** when the container's clock has not ticked. Deliver the file, commit by its delivered id, then read the destination back and compare checksums before saying it is there. This bit twice in one day.
2. **GitHub Pages does not redirect an old custom domain.** Changing the repo's domain left the old address answering "Site not found". Plan the redirect before the switch, never assume it.
3. **A page can be right on the server and wrong in the browser** for ten minutes — `Cache-Control: max-age=600`. Fetch with the cache bypassed and read `last-modified` before diagnosing a failed deploy.

## Where the live records are

`claude/newsroom-live-status.md` — the standing record, kept current
`claude/newsroom-three-surfaces.md` — the plan: one source, three surfaces
`claude/apex-switch-runbook.md` — how the address move was done
`claude/member-access-decision.md` — Stripe-first, one login door
`RUN_SHEET.md` on the Mac, in `BuyTrigger-Research/Project/active/3.7.15 Agentic Newsroom/web/` — commands and failure table
