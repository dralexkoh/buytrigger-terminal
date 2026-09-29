# The content desk — what it has been quietly doing, and what is missing

_Written by Claude (Marissa / OS Control), 24 September 2026, 20:30 UK, after Alex pointed out that the half of the Newsroom that turns news into content had been left out of a whole day of work. Work item BTRES-3.7.15. Evidence read live from the desk, not recalled._

---

## The finding

The content desk has been running since 15 September and **nobody has opened it**. Every Daily Brief run has been proposing content angles off its own stories, exactly as designed, and they have been piling up.

| | |
|---|---|
| Editions with a desk entry | **20** |
| Content cards proposed | **26** |
| Cards Alex has approved | **1** |
| Oldest card still on file | 22 September, 14:44 UTC |
| Cards still inside their window at 19:20 UTC on 24 Sep | **10** — nine EVERGREEN PACK, one INTRADAY EXPLAINER |

By type: 14 intraday explainers, 10 evergreen packs, 1 breaking post, 1 closing recap.

The intraday and breaking ones have expired by design — a 30-minute or 2-hour window is short on purpose. The **evergreen packs carry 48 hours**, which means nine of them are still usable right now and most will expire over the weekend.

A sample of what has been sitting there, in the run's own words:

- *"What a 5% government borrowing rate actually costs a family: the mortgage, the car loan, the savings account"* — Substack · YouTube · live segment
- *"Everyone quotes the 10-year. The 2-year moved 14bp and told you it was priced"* — Substack · YouTube · live segment
- *"How to tell a rates sell-off from a fear sell-off: check what isn't falling"* — chart · X thread · club explainer
- *"The headline said new home sales rose 6.4%. The same sentence said give or take 22%"* — Substack · YouTube · live segment
- *"Why good news for the economy is bad news for expensive shares"* — Substack · YouTube · live segment

These are usable. They are in his register, each one is tied to a story that already passed the evidence rules, and each names the formats it suits.

---

## Why it was missed

Not a build failure. Three things stacked up:

1. **The desk lives on the private Claude page**, and since the public build started on 23 September nobody has opened that page — all the attention went to `buytrigger.club`.
2. **Nothing announces a new card.** Cards appear silently in the CONTENT tab. There is no digest, no notification, nothing that reaches Alex where he actually is.
3. **The cards expire on their own.** A card nobody sees dies quietly and leaves no trace of having been missed, so the loss is invisible.

The run is not at fault and neither is the page. The gap is that the desk has an input and no output.

---

## What is actually missing

The design always ran: **news → card → Alex approves → something makes the post.** Only the first two links exist.

| Link | State |
|---|---|
| Run proposes a card off a sourced story | **built and working**, 26 cards' worth of proof |
| Card appears in the CONTENT tab for Alex to approve or ignore | **built**, unopened |
| Alex finds out a card exists without going to look | **missing** |
| Approved card becomes a draft post | **missing** |
| Draft reaches X / Threads / LinkedIn / Substack | rails exist (Typefully is connected), nothing wired |
| Video and graphics | Descript and Canva are connected, nothing wired |

This is where the "swarm" idea came from, and it stalls at the third row.

---

## Proposal — two pieces, in this order

**Piece one: the daily card digest.** A scheduled task at the end of each trading day that reads the desk, lists the cards still inside their window with their angle and formats, and sends it to Alex where he already is. He replies with the numbers he wants. Nothing else changes — the desk stays where it is, the run stays as it is. This alone rescues the value that is being lost every day, and it is small.

**Piece two: approved card becomes a draft.** When a card is approved, produce the actual first draft in Alex's voice — the `alex-voice` skill already exists for this — and put it in Typefully as an unscheduled draft for him to edit and send. Never auto-publish; the draft is the deliverable, posting stays his.

Deliberately not proposed yet: moving the desk into Supabase, video, graphics, or any autonomous posting. Those are worth doing after the first two prove the loop works end to end.

---

## Decisions for Alex

1. **The nine live evergreen cards.** They expire over the weekend. Worth a look tonight or tomorrow, or let them go and start clean from Monday with the digest in place.
2. **Digest timing and channel** — end of the US day at 22:30 UK is the natural slot, so the day's cards are all in. Where it should reach him is his call.
3. **Draft, never post.** Confirming the boundary before anything is built: Claude drafts, Alex sends. Nothing leaves for a public account without him pressing it.

---

## Note for the record

A whole day went into taking the Newsroom public — address switch, HTTPS, the live feed, four uploads — and the half of the system that turns that news into Alex's content was not mentioned once. The lesson is not "look at the desk"; it is that a feature with no output nobody sees will be forgotten by everyone, including the person who built it. Piece one exists to fix that property, not just today's backlog.
