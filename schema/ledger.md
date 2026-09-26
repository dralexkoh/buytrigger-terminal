# The ledger — collection `journalism`

The bees' own record. One document per Layer 1 edition, plus one per night for Layer 2 and one per week for Layer 3. It answers "what did the swarm do, and why" without opening Typefully, and it is what stops a bee drafting the same card twice.

## Layer 1: document id = edition id

```json
{
  "edition_id": "2026-09-25-0630",
  "drafted": {
    "k1": {
      "typefully_draft_id": 10926756,
      "at": "2026-09-25T15:31:41Z",
      "run": "2026-09-25T15:26:00Z",
      "layer": 1,
      "platforms": ["x", "threads"],
      "angle": "insider sale is a number you divide (HOOD Form 4, story 2)",
      "stock_named": true,
      "fca": "6 green, 0 amber, 0 red",
      "note": "optional: what was left out and why"
    }
  },
  "rejected": {
    "k2": { "reason": "class filter", "at": "…", "run": "…" }
  }
}
```

A card in `drafted` or `rejected` is finished; the next run skips it.

## Layer 2: document id = `<date>-L2`

```json
{
  "drafted": {
    "typefully_draft_id": 10931326,
    "at": "2026-09-25T22:19:42Z",
    "run": "2026-09-25T22:10:00Z",
    "layer": 2,
    "story": "Robinhood's boss sold $30m of shares under a year-old plan",
    "angle": "Insider sale: divide, don't read",
    "editions": ["2026-09-25-0630", "2026-09-25-1230", "2026-09-25-1430", "2026-09-25-1630"],
    "score": 25,
    "stock_named": true,
    "charts": ["newsroom-layer2-2026-09-25/chart1-hood-sold-vs-kept.png", "…"],
    "charts_attached": "delivered as files; attach by hand (upload host refused by network policy)",
    "fca": "CLEAN 17 green 0 amber 0 red",
    "status": "draft",
    "published": false,
    "scheduled": false,
    "overlaps_l1": 10926756
  }
}
```

If nothing qualified: `{ "skipped": { "reason": "…", "at": "…", "candidates_considered": n } }`.
If FCA RED: `{ "rejected": { "reason": "fca: …", "at": "…" } }`.

`overlaps_l1` was added on 26 Sep 2026 with the cross-layer rule; earlier documents do not carry it.

## Layer 3: document id = `<Sunday date>-L3`

```json
{ "drafted": { "at": "…", "subject": "…", "editions": ["…"], "files": ["…"], "layer": 3 } }
```
or `{ "rejected": "no subject recurred across two days" }`.

## Writing rules

- ArtifactData `update` (merge), pinned with the version read. On a version mismatch, re-read and retry once.
- The bees never write any other collection.
- `published` and `scheduled` are always `false` when a bee writes them. If marketing later sends a draft, that shows in Typefully, not here — until the "one source" move (`supabase/swarm_one_source.sql`) gives the ledger a `sent_at` column that a weekly job fills from Typefully.

## Snapshots

`ledger/journalism/` holds JSON exports of every document as of 26 Sep 2026 07:20 UK. Re-export with ArtifactData `list` on `journalism` with `out_dir`.
