# The Newsroom collections the bees read

The private Newsroom page keeps a small database (read with the ArtifactData tool, url `https://claude.ai/artifact/MGGZNGHSGWtAGwo3kZNxZn`). The swarm reads two collections and writes one.

## `editions` (read only)

One document per edition, id `YYYY-MM-DD-HHMM` in UK time (e.g. `2026-09-25-1630`). Nine editions on a weekday: 06:30, 08:30, 10:30, 12:30, 14:30, 16:30, 18:30, 20:30, 22:30.

```
edition_id   "2026-09-25-1630"
title        edition headline
as_of        ISO timestamp of the data
as_of_label  human label
checked      what was verified
markets      the market table (levels, changes)
catalysts    upcoming events
origin       who filed it
schema       schema version
stories[]    the stories
  headline   one line
  dek        one sentence under it
  tag        MARKET | STOCK | MACRO | RATES | VIX | COMMODITY | CORRECTION | …
  state      VERIFIED | STALE FEED | …
  level      ok | mid | …
  conf       confidence label
  asof       as-of label
  sources    list of source hosts
  claims[]   the claim rows — the ONLY place a number may come from
    claim    what was measured ("S&P 500 change on the day")
    value    the figure as a string ("+0.28%", "$30.2m", "47,794,572")
    source   host ("sec.gov", "finance.yahoo.com", "treasury.gov")
    asof     when ("25 SEP 15:34Z", "22 SEP 2026", "FILING TEXT")
    status   ok | sec | single | warn | stale
  callouts[] boxed notes
correction   optional: names a story withdrawn or amended by this edition
```

Corrections also appear as stories with `tag: CORRECTION` (e.g. "Correction: Oracle did file with the SEC on Friday"). The bees treat both forms the same: the corrected story's earlier rows are not used.

## `desk` (read only)

One document per edition. The desk turns stories into content cards.

```
edition_id   "2026-09-25-0630"
cards[]
  id         "k1", "k2", …
  rank       "#1"
  klass      EVERGREEN PACK | BREAKING POST | CLOSING RECAP | INTRADAY EXPLAINER
  title      the card's angle
  why        why it matters (may cite figures from OTHER stories — the bee only uses this card's story's rows)
  formats    "CHART · X THREAD · CLUB EXPLAINER"
  window     "48 H WINDOW"
  life_s     seconds the card lives, from created_at
  story      index into the edition's stories[]
  created_at ISO timestamp
approvals{}  the Newsroom's own approvals; the bees do not read or write it
```

## `journalism` (the swarm's ledger — read and write)

See `ledger.md`.

## Exporting for the tools

The ArtifactData tool's `out_dir` option writes each document as `<out_dir>/<collection>/<doc_id>.json`. That is how `fixtures/` and `ledger/` were produced. A query by `edition_id >= "2026-09-25"` gets a day.
