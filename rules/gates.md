# The gates — which stories become drafts

"Garbage in, garbage out" is the risk with an automated feed. These gates are the filter. A story that fails any gate is recorded in the ledger with the reason and never drafted. The bees apply them in this order and stop at the first failure.

## Layer 1 (per desk card)

| Gate | Rule | Ledger reason |
|---|---|---|
| CLASS | card `klass` is `EVERGREEN PACK`, `BREAKING POST` or `CLOSING RECAP`. `INTRADAY EXPLAINER` is out of scope for posts. | `class filter` |
| WINDOW | `created_at + life_s` is still in the future; a `BREAKING POST` needs more than 15 minutes left | `window` |
| STORY | the card's story is `state` VERIFIED and `level` ok, and no later edition that day withdraws it in a `correction` | `story not verified` |
| CLAIMS | at least two claim rows at status `ok` or `sec` | `not enough usable claims` |
| DEDUPE | same angle as a card already drafted today → out. Same story, different angle → at most two per story per day. At most three Layer 1 drafts a day; beyond that keep the card with more `ok` rows, then the fresher one | `dedupe: same angle as …`, `dedupe: story cap`, `daily cap` |
| FCA | every post passes the fca-check standard standalone; AMBER is rewritten in Alex's voice; RED means no draft | `fca: <what>` |

## Layer 2 (per subject, one a night)

| Gate | Rule |
|---|---|
| STORY | VERIFIED and ok in at least one of today's editions |
| CORRECTIONS | not withdrawn by a later edition's `correction`; if a correction amends a figure, only the amended edition's rows are used |
| CLAIMS | at least three rows at `ok`/`sec` across the subject's editions |
| STALE | the story must not depend on an intraday quote that will be wrong by morning. Closes, filings, official releases and auction results are fine; a pre-market or mid-session quote is not a chartable number |
| SCORE | +2 per `ok` row, +1 per `sec` row, +3 if the subject appears in three or more of today's editions, +2 if an `EVERGREEN PACK` card points at it |
| CROSS-LAYER | prefer the highest-scoring subject that Layer 1 did **not** draft today. Only if nothing else passes may Layer 2 take a Layer 1 subject, and then the title says `· also L1 today` and the scratchpad warns marketing to send one or the other |
| NUMBER CHECK | every numeric token in the posts and chart labels is in the bag of `ok`/`sec` claim values, or is a declared simple difference of two of them |
| FCA | as Layer 1 |

`tools/score_stories.py` runs the SCORE and CROSS-LAYER arithmetic on a day's exports so it can be inspected.

## Layer 3 (per week)

| Gate | Rule |
|---|---|
| TREND | a subject that appears in at least three editions across at least two different days of the week just ended, VERIFIED/ok, not withdrawn |
| RANK | (days present × 3) + (editions present) + (count of `ok` rows); the top one is the article |
| FCA | whole piece and each chart's text |

## Claim status meanings (from the Newsroom)

- `ok` — verified against a primary source (a filing, an official table, an exchange close)
- `sec` — a secondary source (a market data page) that agreed with the story
- `single`, `warn`, `stale`, and anything else — never quoted, never charted

## Why "everything reads the feed"

The Newsroom's Daily Brief writer does the research and the verification, every two hours, and files claim rows with a status. If the bees researched too, a number could enter a post that nobody verified, and the two systems would drift. One source, many outputs.
