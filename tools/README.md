# tools — the checks, by code

Python 3, standard library only. Run from the repo root.

## `verify_numbers.py` — every number traces to a claim row

```bash
python3 tools/verify_numbers.py \
  --editions fixtures/editions/2026-09-25-*.json \
  --text fixtures/drafts/10931326-L2-hood.json \
  --story Robinhood
```

Builds the bag of numbers from every claim row at status `ok`/`sec` (optionally only the stories whose headline contains `--story`), pulls every number out of the draft, and lists any that are not in the bag. Tracked links are ignored; integers 0–31 are skipped unless `--strict`. Declared simple differences go in `--allow 16,14`. Exit 0 = clean.

Result on the three Friday 25 Sep drafts (26 Sep audit): 14, 11 and 49 numbers checked, all trace. A made-up `999,999` fails, as it should. On the rates-week shakedown draft (10922651) it flags `33` in "a 33-year high": that is 2026 − 1993 from the claim row "highest since 1993", a declared difference — `--allow 33` clears it. That is the check working: every derived number has to be declared.

## `check_lengths.py` — platform rules

```bash
python3 tools/check_lengths.py fixtures/drafts/10926756-L1-hood.json
```

Reads a payload `{layer, x[], threads[], substack}` and checks post counts, 280/450 limits, no URL or domain on X, plain punctuation on Threads, the tracked link on the last Threads post, the not-advice line when a stock is named, and the Substack note length for Layer 2. Warns on "today/yesterday". Exit 0 = clean.

Result on 26 Sep: the two Layer 1 drafts pass; the Layer 2 draft failed once (Threads named $HOOD with no not-advice line) and passes after the fix.

## `score_stories.py` — the Layer 2 selection, in the open

```bash
python3 tools/score_stories.py \
  --editions 'fixtures/editions/2026-09-25-*.json' \
  --desk 'fixtures/desk/2026-09-25-*.json' \
  --ledger ledger/journalism/2026-09-25-0630.json ledger/journalism/2026-09-25-1030.json ledger/journalism/2026-09-25-1430.json
```

Groups the day's stories into subjects, applies the gates, scores them, marks the ones Layer 1 already drafted, flags corrections and stale-risk wording, and prints the pick and the runner-up. On Friday 25 Sep it shows Oracle (nine editions, score 64, with a correction filed at 22:30 that the bee must honour) ahead of Micron (57), with Robinhood (40) marked as Layer 1's — which is why the cross-layer rule was added.

The grouping is a simple approximation (same tag, same lead company, or headline overlap); the bee groups by reading. The script is for checking the arithmetic, not for replacing the bee's judgement.

## Payload format

`fixtures/drafts/*.json` shows it. Copy a draft's posts out of Typefully (the MCP `get_draft` result has them under `platforms.x.posts[].text` etc.) into:

```json
{ "layer": 2, "typefully_draft_id": 10931326, "story": "Robinhood",
  "x": ["…"], "threads": ["…"], "substack": "…" }
```
