#!/usr/bin/env python3
"""score_stories.py — the Layer 2 "which story tonight" algorithm, in the open.

The STORY bee (bees/L2-story.md, step 3-4) picks one subject a night. This is
the same arithmetic as a script, so anyone can run it on a day's exports and
see why a subject won, what the runner-up was, and which subjects were skipped
because Layer 1 already drafted them that day.

Inputs are ArtifactData exports (JSON files, one per document):
  --editions  edition docs for the day      (fixtures/editions/2026-09-25-*.json)
  --desk      desk docs for the day         (fixtures/desk/2026-09-25-*.json)
  --ledger    journalism docs for the day   (ledger/journalism/2026-09-25-*.json)

Gates (stop at first failure):
  STORY        VERIFIED and level ok in at least one edition
  CORRECTIONS  not withdrawn by a later edition's `correction`
  CLAIMS       at least 3 claim rows at ok/sec across the subject's editions
Score:
  +2 per ok row, +1 per sec row, +3 if in 3+ editions, +2 if an EVERGREEN PACK card points at it
Cross-layer:
  prefer the top subject NOT in the Layer 1 set for the day

Subject grouping is deliberately simple: stories share a subject when they share
a tag and their headlines overlap enough in meaningful words (Jaccard >= 0.34)
or share a company/instrument name. The bee groups by reading; this script
approximates that so the numbers can be checked.

Usage:
  python3 tools/score_stories.py --editions fixtures/editions/2026-09-25-*.json \
      --desk fixtures/desk/2026-09-25-*.json --ledger ledger/journalism/2026-09-25-*.json
"""
import argparse
import glob
import json
import re
from collections import defaultdict

STOP = set('''a an the of to in on for and or as at by with from is are was were be been its it this that these those
after before over under up down out off into than then there here who what which when where why how not no yes
his her their our your my we you they he she one two three first third again still just more most less very
day days week today tonight yesterday morning afternoon evening new news us'''.split())


def words(s: str):
    return {w for w in re.findall(r"[a-z0-9$&.'-]+", (s or '').lower()) if w not in STOP and len(w) > 2}


def jaccard(a, b):
    return len(a & b) / len(a | b) if (a | b) else 0.0


def entity(headline: str, tag: str):
    """The thing a headline is about, for the tags where that is one name."""
    t = (tag or '').upper()
    h = headline or ''
    if t == 'VIX':
        return 'fear gauge'
    if t == 'COMMODITY':
        return 'oil' if 'oil' in h.lower() else None
    if t == 'STOCK':
        m = re.match(r"([A-Z][A-Za-z&.]+)(?:'s)?(?:\s+([A-Z][A-Za-z&.]+))?", h)
        if not m:
            return None
        first, second = m.group(1), m.group(2)
        # "Bloom Energy", "Blue Owl": keep a capitalised second word unless it starts the verb phrase
        if second and second.lower() not in {'the', 'and', 'or'} and first.lower() not in {'the'}:
            return f"{first} {second}".lower()
        return first.lower()
    return None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--editions', nargs='+', required=True)
    ap.add_argument('--desk', nargs='*', default=[])
    ap.add_argument('--ledger', nargs='*', default=[])
    ap.add_argument('--threshold', type=float, default=0.34)
    a = ap.parse_args()

    def expand(paths):
        out = []
        for p in paths:
            out.extend(sorted(glob.glob(p)) or [p])
        return out

    editions = [json.load(open(f, encoding='utf-8')) for f in expand(a.editions)]
    editions.sort(key=lambda e: e.get('edition_id', ''))
    desks = {d.get('edition_id'): d for d in (json.load(open(f, encoding='utf-8')) for f in expand(a.desk))}
    ledgers = {}
    for f in expand(a.ledger):
        doc = json.load(open(f, encoding='utf-8'))
        eid = doc.get('edition_id') or re.sub(r'\.json$', '', f.split('/')[-1])
        ledgers[eid] = doc

    # withdrawn stories: any later edition's correction naming a headline
    withdrawn = set()
    for e in editions:
        c = e.get('correction')
        if isinstance(c, dict):
            for key in ('withdrawn', 'stories', 'headline', 'headlines'):
                v = c.get(key)
                if isinstance(v, str):
                    withdrawn.add(v.lower())
                elif isinstance(v, list):
                    withdrawn.update(str(x).lower() for x in v)

    # flatten stories
    items = []
    for e in editions:
        eid = e.get('edition_id')
        for idx, s in enumerate(e.get('stories', [])):
            items.append({'edition': eid, 'idx': idx, 'tag': s.get('tag'), 'headline': s.get('headline', ''),
                          'verified': s.get('state') == 'VERIFIED' and s.get('level') == 'ok',
                          'ok': sum(1 for c in s.get('claims', []) if c.get('status') == 'ok'),
                          'sec': sum(1 for c in s.get('claims', []) if c.get('status') == 'sec'),
                          'words': words(s.get('headline', ''))})

    # corrections filed as stories (tag CORRECTION) attach to the subject they name
    corrections = [it for it in items if (it['tag'] or '').upper() == 'CORRECTION']
    items = [it for it in items if (it['tag'] or '').upper() != 'CORRECTION']

    # group into subjects: same tag, and either the same lead entity or enough headline overlap
    subjects = []
    for it in items:
        it['entity'] = entity(it['headline'], it['tag'])
        home = None
        for sub in subjects:
            if sub['tag'] != it['tag']:
                continue
            if it['entity'] and sub['entity'] == it['entity']:
                home = sub
                break
            if not it['entity'] and any(jaccard(it['words'], m['words']) >= a.threshold for m in sub['members']):
                home = sub
                break
        if home is None:
            home = {'tag': it['tag'], 'entity': it['entity'], 'members': [], 'label': it['headline'], 'corrections': []}
            subjects.append(home)
        home['members'].append(it)
    for c in corrections:
        cw = c['words']
        for sub in subjects:
            hit = (sub['entity'] and sub['entity'] in c['headline'].lower()) or any(jaccard(cw, m['words']) >= 0.25 for m in sub['members'])
            if hit:
                sub['corrections'].append(f"{c['edition']}: {c['headline']}")

    # Layer 1 set for the day: (edition, story index) of every drafted card
    l1 = set()
    l1_ids = {}
    for eid, doc in ledgers.items():
        for card_id, entry in (doc.get('drafted') or {}).items():
            if not isinstance(entry, dict) or entry.get('layer', 1) != 1:
                continue
            desk = desks.get(eid) or {}
            for card in desk.get('cards', []):
                if card.get('id') == card_id:
                    l1.add((eid, card.get('story')))
                    l1_ids[(eid, card.get('story'))] = entry.get('typefully_draft_id')

    evergreen = set()
    for eid, d in desks.items():
        for card in d.get('cards', []):
            if card.get('klass') == 'EVERGREEN PACK':
                evergreen.add((eid, card.get('story')))

    rows = []
    for sub in subjects:
        m = sub['members']
        keys = {(x['edition'], x['idx']) for x in m}
        gate = None
        if not any(x['verified'] for x in m):
            gate = 'STORY: never VERIFIED/ok'
        elif any(x['headline'].lower() in withdrawn for x in m):
            gate = 'CORRECTIONS: withdrawn'
        ok = sum(x['ok'] for x in m)
        sec = sum(x['sec'] for x in m)
        if gate is None and ok + sec < 3:
            gate = f'CLAIMS: {ok + sec} usable rows (<3)'
        eds = len({x['edition'] for x in m})
        score = 2 * ok + sec + (3 if eds >= 3 else 0) + (2 if keys & evergreen else 0)
        in_l1 = keys & l1
        stale = any(re.search(r'\b(futures|pre-market|before the open|overnight|opening bell)\b', x['headline'], re.I) for x in m)
        rows.append({'subject': sub['label'][:70], 'tag': sub['tag'], 'editions': eds, 'ok': ok, 'sec': sec,
                     'score': score, 'gate': gate, 'l1': sorted(str(l1_ids.get(k)) for k in in_l1),
                     'stale': stale, 'corrections': sub['corrections'], 'n': len(m)})

    rows.sort(key=lambda r: (r['gate'] is not None, -r['score']))
    print(f"{len(editions)} editions, {len(items)} stories + {len(corrections)} corrections, {len(subjects)} subjects, Layer 1 set: {len(l1)} story(ies)\n")
    print(f"{'score':>5} {'eds':>3} {'sto':>3} {'ok':>3} {'sec':>3}  {'tag':<9} {'L1?':<12} subject / gate")
    for r in rows:
        flag = ('L1 ' + ','.join(r['l1'])) if r['l1'] else ''
        gate = f"   [skipped: {r['gate']}]" if r['gate'] else ''
        stale = '   [stale-risk: intraday/futures wording; chart closes and filings only]' if r['stale'] and not r['gate'] else ''
        print(f"{r['score']:>5} {r['editions']:>3} {r['n']:>3} {r['ok']:>3} {r['sec']:>3}  {str(r['tag']):<9} {flag:<12} {r['subject']}{gate}{stale}")
        for c in r['corrections']:
            print(f"{'':>34}  correction -> {c}")

    passing = [r for r in rows if r['gate'] is None]
    if not passing:
        print("\nRESULT: no subject qualified tonight")
        return
    pick = next((r for r in passing if not r['l1']), None)
    if pick:
        print(f"\nRESULT: {pick['subject']}  (score {pick['score']}, no Layer 1 draft today)")
    else:
        pick = passing[0]
        print(f"\nRESULT: {pick['subject']}  (score {pick['score']}) — ALSO L1 TODAY (draft {','.join(pick['l1'])}); title gets ' · also L1 today' and marketing is warned")
    others = [r for r in passing if r is not pick]
    if others:
        print(f"runner-up: {others[0]['subject']} (score {others[0]['score']})")


if __name__ == '__main__':
    main()
