# The Newsroom, mirrored — three surfaces, one source

_Alex's architecture, described by him on 24 September 2026 and written down by Claude before it gets lost again. This supersedes the narrower "content desk" framing in `claude/content-desk-state.md`: the desk is not a feature bolted onto the Newsroom, it is the seed of the second surface. Work item BTRES-3.7.15._

_**Update, 24 Sep 20:45 UK:** surface 2 is built — see `claude/newsroom-journalism.md` for the decisions, the gates and the shakedown. The status rows below are updated; the rest of this doc is as first written._

---

## The shape

One verified source of news. Three surfaces reading the same source. Nothing downstream does its own research.

```
                    newsroom_editions   ← the single source of truth
                  (Supabase, every edition, every story, every claim
                   with its source and its status — already built)
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
  1 · NEWSROOM          2 · JOURNALISM        3 · JOURNAL MEDIA
  the news channel      X · Threads ·         shorts · Instagram ·
  buytrigger.club       Substack notes        video
  LIVE                  BUILT · OFF           not built
```

**1 · Newsroom** — live at `buytrigger.club` since 24 September. Free, no login, nine editions a weekday, filing itself.

**2 · Newsroom Journalism** — the written social surface. X, Threads, Substack notes. Takes a story that already passed the evidence rules and renders it for each platform. **Built 24 September as a flow into Typefully; scheduled task exists and is switched off until Alex reviews the first five drafts.** Record: `claude/newsroom-journalism.md`.

**3 · Newsroom Journal Media** — the visual surface. Shorts, Instagram, video.

2 and 3 are the platforms the swarm works on.

## The swarm, in Alex's terms

| | Role | State |
|---|---|---|
| **Gathering bees** | find and verify the news | **working** — the Daily Brief run, nine a weekday, every number sourced and re-proved before it ships |
| **Honey-making bees** | turn a verified story into written posts for surface 2 | **built 24 Sep** — scheduled task `trig_01KFVJK2ZFogDj93EojbMFMs`, disabled until the shakedown review. Reads the desk cards, applies seven gates, writes Typefully drafts, keeps a ledger |
| **Video-making bee** | turn a verified story into a short for surface 3 | not built. Descript and Canva are connected; nothing is wired |
| **Queen bee** | Alex. Picks what gets made, approves what goes out | approval now happens in Typefully: he edits and sends, or deletes. Five drafts waiting as of 24 Sep 20:45 |

## The two rules that make it work

**Everything reads the feed. Nothing re-researches.** A short that quotes a number must trace to the same claim row as the edition it came from. The moment a bee goes and finds its own facts, the evidence chain breaks and the whole thing becomes ordinary content. This is the rule that makes three surfaces safe rather than three times the risk.

**Bees draft. The queen sends.** Nothing reaches a public account without Alex pressing it. Drafts land where he already works — Typefully for written, Descript for video — and he edits and publishes. No autonomous posting, not at any stage.

## What is already true, and it is more than it feels

The hard part is done. A verified, timestamped, source-backed feed of market stories, updating itself nine times a weekday, with every number carrying its provenance and a withdrawal path if one is wrong. That is the expensive thing to build and it exists. Surfaces 2 and 3 are renderers on top of it, not new newsrooms.

The desk has also been proving the concept quietly: 26 angles proposed off real stories, each already naming which formats it suits — `X POST · THREADS`, `CHART · X THREAD · CLUB EXPLAINER`, `SUBSTACK · YOUTUBE · LIVE SEGMENT`. The classification surface 2 and 3 need is already being produced.

## The one decision that shapes everything else

**Are surfaces 2 and 3 places Alex opens, or flows that deliver into the tools he already uses?**

*Places* — each surface is its own page, like the Newsroom: he opens Journalism, sees today's stories rendered as ready posts, picks, and sends from there. Consistent with how he thinks about it ("platforms"), more to build, and one more thing to keep open.

*Flows* — no new page. A digest reaches him, he picks, and the drafts appear in Typefully and Descript where he already edits and publishes. Much less to build, and it meets him where the work actually happens.

*Both, in order* — flows first, because the value is in the drafts existing, and a page later if the volume justifies one.

Claude's recommendation is the third, and to start with surface 2 only: written posts are cheaper to draft, easier to judge, and the feedback comes back in a day. Video is the right second step, not the first.

**Decided 24 Sep: flows.** Typefully drafts, no page, no digest step — every qualifying card becomes a draft and Alex sends or deletes in the app.

## Decided on 24 September (were "not yet decided")

- Platforms in the first cut of surface 2 — **X, Threads and Substack notes, all three.**
- Honey bees draft from the **approved desk card**, not the raw edition; the card carries the angle and the formats, the story behind it carries the claims.
- How many drafts a day — **Evergreen, Breaking and Close cards only; hard cap three a day, two per story.** Intraday Explainers are out. The ledger's rejection reasons will show whether the caps are right.
- Where the queen approves from — **Typefully on the phone.**

## Why this doc exists

On 24 September a full day went into taking surface 1 public, and surfaces 2 and 3 were not mentioned once — by Alex or by Claude — until he raised it at the end of the day. The plan was always three surfaces off one source. Writing it down here so that the next session starts from the whole shape rather than the part that happens to be live.
