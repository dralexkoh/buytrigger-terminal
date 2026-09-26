#!/usr/bin/env python3
"""check_lengths.py — platform rules for a draft, checked by code, not by eye.

Reads a JSON payload:
  {
    "layer": 1 | 2,
    "x": ["post 1", "post 2", ...],
    "threads": ["post 1", ...],          # Layer 1: exactly one post
    "substack": "note text"              # Layer 2 only
  }

Rules (rules/platforms.md is the human version):
  X        each post <= 280 chars; NO url and NO bare domain anywhere;
           Layer 1: 3-5 posts; Layer 2: 8-12 posts;
           if a stock is named ($TICKER), a not-advice line must be present.
  Threads  each post <= 450 chars; plain punctuation only (no arrows, em dashes,
           bullets, special symbols); the LAST post carries the tracked link
           with utm_content=...; Layer 1: 1 post; Layer 2: 3-5 posts.
  Substack Layer 2: 1,000-1,800 chars, tracked link present.

Usage: python3 tools/check_lengths.py payload.json
Exit 0 when clean, 1 when anything fails. Warnings never fail the run.
"""
import json
import re
import sys

DOMAIN_RE = re.compile(r'\b[a-z0-9-]+(?:\.[a-z0-9-]+)*\.(?:com|gov|club|net|org|io|co|uk|ai)\b', re.I)
URL_RE = re.compile(r'https?://', re.I)
TICKER_RE = re.compile(r'\$[A-Z]{1,5}\b')
BAD_CHARS = {'→': 'arrow', '←': 'arrow', '↑': 'arrow', '↓': 'arrow', '—': 'em dash', '–': 'en dash',
             '•': 'bullet', '·': 'middle dot', '…': 'ellipsis char', '–': 'en dash'}
NOT_ADVICE_RE = re.compile(r'not (financial )?advice', re.I)
UTM_RE = re.compile(r'utm_content=[A-Za-z0-9._-]+')
STALE_RE = re.compile(r'\b(today|tonight|yesterday|this morning|this afternoon)\b', re.I)


def main(path):
    p = json.load(open(path, encoding='utf-8'))
    layer = int(p.get('layer', 1))
    x = p.get('x') or []
    th = p.get('threads') or []
    sub = p.get('substack') or ''
    fails, warns = [], []

    # ---- X ----
    lo, hi = (3, 5) if layer == 1 else (8, 12)
    if not (lo <= len(x) <= hi):
        fails.append(f"X: {len(x)} posts; Layer {layer} needs {lo}-{hi}")
    stock = False
    for i, post in enumerate(x, 1):
        n = len(post)
        if n > 280:
            fails.append(f"X post {i}: {n} chars (limit 280)")
        if URL_RE.search(post) or DOMAIN_RE.search(post):
            fails.append(f"X post {i}: contains a URL or bare domain; X refuses app-published posts with links")
        if TICKER_RE.search(post):
            stock = True
        if STALE_RE.search(post):
            warns.append(f"X post {i}: says 'today/yesterday'; marketing may send it tomorrow")
    if stock and not any(NOT_ADVICE_RE.search(post) for post in x):
        fails.append("X: a stock is named ($TICKER) but no post carries a not-advice line")

    # ---- Threads ----
    lo, hi = (1, 1) if layer == 1 else (3, 5)
    if not (lo <= len(th) <= hi):
        fails.append(f"Threads: {len(th)} posts; Layer {layer} needs {lo}-{hi}")
    for i, post in enumerate(th, 1):
        n = len(post)
        if n > 450:
            fails.append(f"Threads post {i}: {n} chars (limit 450)")
        for ch, name in BAD_CHARS.items():
            if ch in post:
                fails.append(f"Threads post {i}: contains {name} ({ch!r}); plain punctuation only")
        if STALE_RE.search(post):
            warns.append(f"Threads post {i}: says 'today/yesterday'")
    if th:
        last = th[-1]
        if not UTM_RE.search(last):
            fails.append("Threads: last post has no tracked link (utm_content=...)")
        if any(TICKER_RE.search(t) for t in th) and not any(NOT_ADVICE_RE.search(t) for t in th):
            fails.append("Threads: a stock is named but no not-advice line")

    # ---- Substack ----
    if layer == 2:
        n = len(sub)
        if not (1000 <= n <= 1800):
            fails.append(f"Substack note: {n} chars (Layer 2 wants 1,000-1,800)")
        if not UTM_RE.search(sub):
            fails.append("Substack note: no tracked link (utm_content=...)")
    elif sub:
        warns.append("Layer 1 payload carries a substack note; Layer 1 is X + Threads only")

    print(f"Layer {layer}: X {len(x)} posts ({', '.join(str(len(s)) for s in x)}), "
          f"Threads {len(th)} posts ({', '.join(str(len(s)) for s in th)}), Substack {len(sub)} chars, stock named: {stock}")
    for w in warns:
        print("  warn:", w)
    if fails:
        for f in fails:
            print("  FAIL:", f)
        sys.exit(1)
    print("OK — platform rules pass")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    main(sys.argv[1])
