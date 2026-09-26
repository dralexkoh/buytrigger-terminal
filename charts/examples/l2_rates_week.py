"""Layer 2 shakedown charts (25 Sep 2026, Typefully draft 10922651) — every number below is a treasury.gov claim row
(status ok) from the Newsroom editions 2026-09-24-0630, -0830 and -2230.
22 Sep values for 3y/7y are the 23 Sep row minus the +16bp the same row states."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))  # charts/branded_chart.py
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from branded_chart import COLORS, apply_buytrigger_style, save_chart

OUT = str(HERE / 'output')

mats = ['2y', '3y', '5y', '7y', '10y', '30y']
d22 = [4.71, 4.81, 4.83, 4.89, 4.96, 5.29]
d23 = [4.85, 4.97, 4.99, 5.05, 5.11, 5.40]
d24 = {'2y': 4.87, '10y': 5.18, '30y': 5.47}

# ---- chart 1: the curve, three days -------------------------------------
fig, ax = plt.subplots(figsize=(10, 6))
x = list(range(len(mats)))
ax.plot(x, d22, marker='o', color=COLORS['navy'], linewidth=2.2, label='Mon 22 Sep')
ax.plot(x, d23, marker='o', color=COLORS['red'], linewidth=2.6, label='Wed 23 Sep')
x24 = [mats.index(k) for k in d24]
ax.plot(x24, list(d24.values()), marker='s', color=COLORS['black'], linewidth=2.2, linestyle='--', label='Thu 24 Sep (2y, 10y, 30y)')
for xi, v in zip(x, d23):
    ax.annotate(f'{v:.2f}%', (xi, v), textcoords='offset points', xytext=(0, -17), ha='center', fontsize=9, color=COLORS['red'], fontweight='600')
for xi, v in zip(x, d22):
    ax.annotate(f'{v:.2f}%', (xi, v), textcoords='offset points', xytext=(0, -17), ha='center', fontsize=8.5, color=COLORS['navy'])
for xi, (k, v) in zip(x24, d24.items()):
    ax.annotate(f'{v:.2f}%', (xi, v), textcoords='offset points', xytext=(0, 9), ha='center', fontsize=9, color=COLORS['black'], fontweight='600')
ax.set_xticks(x); ax.set_xticklabels(mats)
ax.set_ylim(4.5, 5.7)
apply_buytrigger_style(ax, fig, 'What the US government pays to borrow, by loan length', xlabel='Loan length', ylabel='Yield, %', show_legend=False)
ax.legend(loc='upper left', frameon=True, edgecolor=COLORS['black'], fontsize=10)
fig.text(0.01, 0.01, 'Source: US Treasury daily par yield curve, treasury.gov. 22 Sep 3y and 7y are the 23 Sep readings less the +16bp the Treasury table shows. Thursday rows published for 2y, 10y and 30y.', fontsize=7.5, color='#555555', ha='left')
save_chart(fig, 'l2_curve_three_days.png', output_dir=OUT)

# ---- chart 2: Wednesday's one-day change by maturity --------------------
chg = [round((b - a) * 100) for a, b in zip(d22, d23)]  # 14, 16, 16, 16, 15, 11
fig, ax = plt.subplots(figsize=(10, 6))
cols = [COLORS['red'] if c == max(chg) else COLORS['navy'] for c in chg]
bars = ax.bar(mats, chg, color=cols, width=0.62)
for b, c in zip(bars, chg):
    ax.annotate(f'+{c}bp', (b.get_x() + b.get_width() / 2, c), textcoords='offset points', xytext=(0, 5), ha='center', fontsize=11, fontweight='600', color=COLORS['black'])
ax.set_ylim(0, 20)
apply_buytrigger_style(ax, fig, 'Wednesday 23 September: how much each loan length moved in one day', xlabel='Loan length', ylabel='Change in yield, basis points', show_legend=False)
fig.text(0.01, 0.01, 'Source: US Treasury daily par yield curve, treasury.gov, 22 and 23 Sep 2026. One basis point = 0.01 of a percentage point.', fontsize=7.5, color='#555555', ha='left')
save_chart(fig, 'l2_wednesday_change.png', output_dir=OUT)
print('charts written', chg)
