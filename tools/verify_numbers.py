#!/usr/bin/env python3
"""verify_numbers.py — does every number in a draft trace to a claim row?

The rule of the swarm: nothing re-researches. A draft may only carry numbers that
sit in a claim row with status `ok` or `sec` on the day's editions. This script
is the mechanical check the bees run (and the reviewer can re-run) before a
draft goes to Typefully.

Usage
  python3 tools/verify_numbers.py --editions fixtures/editions/2026-09-25-*.json \
      --text draft.txt [--story "Robinhood"] [--allow 16,14,11]

  --editions   one or more edition JSON files (ArtifactData exports of the
               `editions` collection). Every claim row at status ok/sec across
               them goes into the "bag" of permitted numbers.
  --text       one or more files holding the draft text (plain text or the
               JSON payload format used by check_lengths.py). Use "-" for stdin.
  --story      optional substring; only stories whose headline contains it
               feed the bag (case-insensitive). Tighter = safer.
  --allow      comma list of extra numbers you have declared as simple
               differences of two claim values (say so in the scratchpad).

Exit code 0 when every number traces, 1 when any does not.
Small tokens (integers 0-31, used for dates, ordinals and post counts) are
skipped; pass --strict to check them too.
"""
import argparse
import json
import re
import sys

NUM_RE = re.compile(r'(?<![A-Za-z])[-+]?\$?\d[\d,]*(?:\.\d+)?')
URL_RE = re.compile(r'(?:https?://\S+|\b[a-z0-9.-]+\.(?:club|com|gov|net|org)/\S*)', re.I)


def norm(tok: str) -> str:
    t = tok.strip().lstrip('+-$').replace(',', '')
    if '.' in t:
        t = t.rstrip('0').rstrip('.')
    return t


def numbers_in(text: str):
    out = []
    text = URL_RE.sub(' ', text)  # a tracked link's utm_content is not a figure
    for m in NUM_RE.finditer(text):
        raw = m.group(0)
        n = norm(raw)
        if n:
            out.append((n, raw, m.start()))
    return out


def load_text(path: str) -> str:
    data = sys.stdin.read() if path == '-' else open(path, encoding='utf-8').read()
    # Accept the JSON payload format {x: [...], threads: [...], substack: "..."}
    try:
        obj = json.loads(data)
    except Exception:
        return data
    parts = []
    for k in ('x', 'threads'):
        for p in obj.get(k, []) or []:
            parts.append(p)
    if obj.get('substack'):
        parts.append(obj['substack'])
    for k in ('chart_labels', 'labels'):
        for p in obj.get(k, []) or []:
            parts.append(p)
    return '\n\n'.join(parts) if parts else data


def build_bag(edition_files, story_filter=None):
    bag = {}
    rows = 0
    for f in edition_files:
        ed = json.load(open(f, encoding='utf-8'))
        eid = ed.get('edition_id', f)
        for s in ed.get('stories', []):
            if story_filter and story_filter.lower() not in (s.get('headline') or '').lower():
                continue
            for c in s.get('claims', []):
                if c.get('status') not in ('ok', 'sec'):
                    continue
                rows += 1
                blob = ' '.join(str(c.get(k, '')) for k in ('claim', 'value', 'asof'))
                for n, raw, _ in numbers_in(blob):
                    bag.setdefault(n, []).append(f"{eid} · {s.get('headline','')[:50]} · {c.get('claim','')} = {c.get('value','')}")
    return bag, rows


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--editions', nargs='+', required=True)
    ap.add_argument('--text', nargs='+', required=True)
    ap.add_argument('--story', default=None)
    ap.add_argument('--allow', default='')
    ap.add_argument('--strict', action='store_true')
    a = ap.parse_args()

    bag, rows = build_bag(a.editions, a.story)
    allowed = {norm(x) for x in a.allow.split(',') if x.strip()}
    text = '\n\n'.join(load_text(p) for p in a.text)

    checked = 0
    bad = []
    for n, raw, pos in numbers_in(text):
        if not a.strict:
            try:
                if '.' not in n and 0 <= int(n) <= 31:
                    continue
            except ValueError:
                pass
        checked += 1
        if n in bag or n in allowed:
            continue
        ctx = text[max(0, pos - 40):pos + 40].replace('\n', ' ')
        bad.append((raw, ctx))

    print(f"bag: {len(bag)} distinct numbers from {rows} ok/sec claim rows in {len(a.editions)} edition file(s)"
          + (f" (story filter: {a.story!r})" if a.story else ''))
    print(f"draft: {checked} numbers checked")
    if bad:
        print(f"UNMATCHED: {len(bad)}")
        for raw, ctx in bad:
            print(f"  {raw!r:>10}  …{ctx}…")
        sys.exit(1)
    print("OK — every number traces to an ok/sec claim row" + (" or the --allow list" if allowed else ''))


if __name__ == '__main__':
    main()
