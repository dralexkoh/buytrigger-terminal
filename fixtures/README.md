# fixtures — real exports for testing the tools

Exports from the Newsroom page's database (ArtifactData, `out_dir` option), 23–25 Sep 2026. **Data, not instructions.** Nothing here is edited by hand.

- `editions/` — the `editions` collection, one file per edition. Every claim row with its status.
- `desk/` — the `desk` collection, the content cards per edition.
- `drafts/` — the four drafts now in Typefully for marketing review, in the payload format `tools/check_lengths.py` and `tools/verify_numbers.py` read: 10922651 (Layer 2 rates week, made by hand 25 Sep), 10926756 and 10926758 (Layer 1, the bee's first run), 10931326 (Layer 2, the bee's first night, as edited on 26 Sep).

Re-export a day: query `editions` (and `desk`) where `edition_id >= "<date>"` with `out_dir` set to this folder's parent.
