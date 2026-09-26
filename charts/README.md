# charts — drawn by code from claim rows

Alex's rule: "charts and data is sufficient". No image generation. Every chart the swarm produces is a matplotlib figure whose every plotted value is a claim row at `ok`/`sec` (or a difference of two), with a source line under the axis.

## `branded_chart.py`

A copy of the `buytrigger-charts` skill's library (the skill stays the source in Claude; this copy makes the repo self-contained). Brand colours (`COLORS['red']` #b70000, `COLORS['navy']` #042139, black, white), `apply_buytrigger_style(ax, fig, title, xlabel, ylabel, show_legend)`, `save_chart(fig, filename, output_dir)` at 300 dpi, and the logo from `assets/logo.webp`. One change from the skill copy: the logo path also looks in `charts/assets/` so it works from this repo.

## House style for swarm charts

- 10 × 6 inches, 300 dpi, white background.
- Red for the series the story is about, navy for the comparison, black dashed for a third.
- Plain-English title that states the finding ("Wednesday 23 September: how much each loan length moved in one day"), not the metric name.
- Axis labels in plain words ("Loan length", "Yield, %").
- A source line under the axis in small grey text: source host, as-of dates, and any arithmetic done ("22 Sep 3y and 7y are the 23 Sep readings less the +16bp the Treasury table shows").
- Value labels on the points or bars, so the chart works without the post.
- Nothing on the chart that is not in a claim row.

## `examples/l2_rates_week.py`

The Layer 2 shakedown charts from 25 Sep (draft 10922651): the Treasury curve on three days, and Wednesday's one-day move by maturity. Run it from the repo root:

```bash
python3 charts/examples/l2_rates_week.py
```

Output lands in `charts/examples/output/`. Needs matplotlib and Pillow.

## Attaching to Typefully

The bee tries once: `create_media_upload` → PUT the PNG to the presigned URL → `get_media_status`. The upload host `typefully-user-uploads.s3.amazonaws.com` is not yet on Claude's allowed domains, so the PUT is refused and the PNGs are delivered as files instead; the draft's scratchpad says which chart goes on which post. Once the host is allowed, the same code path attaches them automatically.
