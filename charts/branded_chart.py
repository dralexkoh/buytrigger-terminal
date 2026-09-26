#!/usr/bin/env python3
"""
BuyTrigger.Club Branded Chart Generator
All charts automatically styled with BuyTrigger branding.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image
import numpy as np
from pathlib import Path

# ============================================================
# BUYTRIGGER BRAND COLORS
# ============================================================
COLORS = {
    # Primary
    'red': '#b70000',
    'black': '#000000',
    'white': '#ffffff',
    # Secondary
    'navy': '#042139',
    'blue': '#6b8ca8',
    # Accent
    'yellow': '#d4a000',
    'green': '#2d8659',
    'dark_red': '#8b1538',
    # Utility
    'gray': '#e5e5e5',
}

# Data color palette (order of use for multi-series)
DATA_COLORS = [
    COLORS['red'],      # Primary series
    COLORS['navy'],     # Secondary series
    COLORS['black'],    # Tertiary
    COLORS['blue'],     # Fourth
    COLORS['yellow'],   # Fifth
    COLORS['green'],    # Sixth
]

# ============================================================
# SKILL DIRECTORY (for logo path)
# ============================================================
SKILL_DIR = Path(__file__).parent.parent
_CANDIDATES = [Path(__file__).parent / 'assets' / 'logo.webp',   # buytrigger-swarm/charts/assets
               SKILL_DIR / 'assets' / 'logo.webp']               # the buytrigger-charts skill layout
LOGO_PATH = next((p for p in _CANDIDATES if p.exists()), _CANDIDATES[0])

# ============================================================
# CORE STYLING FUNCTION
# ============================================================
def apply_buytrigger_style(ax, fig, title, xlabel='', ylabel='', show_legend=True, legend_labels=None):
    """Apply BuyTrigger branding to any matplotlib axes."""
    
    # Background
    fig.set_facecolor(COLORS['white'])
    ax.set_facecolor(COLORS['white'])
    
    # Title - Black, left-aligned
    ax.set_title(title, fontsize=18, fontweight='600', color=COLORS['black'],
                 pad=20, loc='left', fontfamily='sans-serif')
    
    # Axis labels - Black
    if xlabel:
        ax.set_xlabel(xlabel, fontsize=11, color=COLORS['black'], 
                      fontfamily='sans-serif', fontweight='600')
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=11, color=COLORS['black'],
                      fontfamily='sans-serif', fontweight='600')
    
    # Grid - subtle horizontal only
    ax.grid(True, axis='y', alpha=0.3, linestyle='-', linewidth=0.5, color=COLORS['gray'])
    ax.set_axisbelow(True)
    
    # Spines - black left and bottom only
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(COLORS['black'])
    ax.spines['left'].set_linewidth(1)
    ax.spines['bottom'].set_color(COLORS['black'])
    ax.spines['bottom'].set_linewidth(1)
    
    # Ticks - black
    ax.tick_params(colors=COLORS['black'], labelsize=10, length=4, width=0.8)
    
    # Legend
    if show_legend and legend_labels:
        legend = ax.legend(legend_labels, loc='upper left', frameon=True,
                          fontsize=10, edgecolor=COLORS['black'], 
                          framealpha=1, fancybox=False)
        legend.get_frame().set_linewidth(0.8)
        legend.get_frame().set_facecolor(COLORS['white'])
        for text in legend.get_texts():
            text.set_color(COLORS['black'])
    
    # Logo and branding
    _add_logo(ax)

def _add_logo(ax):
    """Add BuyTrigger logo and text to chart."""
    if LOGO_PATH.exists():
        logo = Image.open(LOGO_PATH)
        imagebox = OffsetImage(logo, zoom=0.04)
        ab = AnnotationBbox(imagebox, (0.45, 0.97), frameon=False,
                           xycoords='axes fraction', box_alignment=(0.5, 0.5))
        ax.add_artist(ab)
    
    ax.text(0.50, 0.97, 'BuyTrigger.Club', transform=ax.transAxes,
            fontsize=9, ha='left', va='center', color=COLORS['red'],
            fontweight='600', fontfamily='sans-serif')

# ============================================================
# CHART TYPES
# ============================================================

def bar_chart(data, labels, title, xlabel='', ylabel='', series_names=None, horizontal=False):
    """
    Create branded bar chart.
    
    Args:
        data: List of values (single series) or list of lists (multiple series)
        labels: Category labels
        title: Chart title
        xlabel, ylabel: Axis labels
        series_names: Names for legend (multi-series)
        horizontal: If True, creates horizontal bar chart
    """
    fig, ax = plt.subplots(figsize=(10, 6), facecolor=COLORS['white'])
    
    # Handle single vs multiple series
    if isinstance(data[0], (list, np.ndarray)):
        n_series = len(data)
        n_cats = len(labels)
        width = 0.8 / n_series
        x = np.arange(n_cats)
        
        for i, series in enumerate(data):
            offset = (i - n_series/2 + 0.5) * width
            color = DATA_COLORS[i % len(DATA_COLORS)]
            if horizontal:
                ax.barh(x + offset, series, width * 0.9, color=color, 
                       edgecolor=COLORS['black'], linewidth=0.5, alpha=0.9)
            else:
                ax.bar(x + offset, series, width * 0.9, color=color,
                      edgecolor=COLORS['black'], linewidth=0.5, alpha=0.9)
        
        if horizontal:
            ax.set_yticks(x)
            ax.set_yticklabels(labels)
        else:
            ax.set_xticks(x)
            ax.set_xticklabels(labels)
    else:
        x = np.arange(len(labels))
        color = DATA_COLORS[0]
        if horizontal:
            ax.barh(x, data, color=color, edgecolor=COLORS['black'], 
                   linewidth=0.5, alpha=0.9)
            ax.set_yticks(x)
            ax.set_yticklabels(labels)
        else:
            ax.bar(x, data, color=color, edgecolor=COLORS['black'],
                  linewidth=0.5, alpha=0.9)
            ax.set_xticks(x)
            ax.set_xticklabels(labels)
        series_names = None
    
    apply_buytrigger_style(ax, fig, title, xlabel, ylabel, 
                          show_legend=series_names is not None,
                          legend_labels=series_names)
    plt.tight_layout()
    return fig, ax


def line_chart(x_data, y_data, title, xlabel='', ylabel='', series_names=None, markers=True):
    """
    Create branded line chart.
    
    Args:
        x_data: X-axis values
        y_data: Y values (single list) or list of lists (multiple series)
        title: Chart title
        series_names: Names for legend
        markers: Whether to show markers on data points
    """
    fig, ax = plt.subplots(figsize=(10, 6), facecolor=COLORS['white'])
    
    marker = 'o' if markers else None
    markersize = 8 if markers else 0
    
    # Handle single vs multiple series
    if isinstance(y_data[0], (list, np.ndarray)):
        for i, series in enumerate(y_data):
            color = DATA_COLORS[i % len(DATA_COLORS)]
            ax.plot(x_data, series, marker=marker, linewidth=2.5, 
                   markersize=markersize, color=color, alpha=0.9)
    else:
        ax.plot(x_data, y_data, marker=marker, linewidth=2.5,
               markersize=markersize, color=DATA_COLORS[0], alpha=0.9)
        series_names = None
    
    apply_buytrigger_style(ax, fig, title, xlabel, ylabel,
                          show_legend=series_names is not None,
                          legend_labels=series_names)
    plt.tight_layout()
    return fig, ax


def area_chart(x_data, y_data, title, xlabel='', ylabel='', series_names=None, stacked=True):
    """
    Create branded area chart.
    
    Args:
        x_data: X-axis values
        y_data: Y values - list of lists for stacked areas
        title: Chart title
        stacked: If True, areas stack on top of each other
    """
    fig, ax = plt.subplots(figsize=(10, 6), facecolor=COLORS['white'])
    
    if isinstance(y_data[0], (list, np.ndarray)):
        colors = [DATA_COLORS[i % len(DATA_COLORS)] for i in range(len(y_data))]
        if stacked:
            ax.stackplot(x_data, *y_data, colors=colors, alpha=0.85)
        else:
            for i, series in enumerate(y_data):
                ax.fill_between(x_data, series, alpha=0.6, color=colors[i])
                ax.plot(x_data, series, color=colors[i], linewidth=1.5)
    else:
        ax.fill_between(x_data, y_data, alpha=0.85, color=DATA_COLORS[0])
        ax.plot(x_data, y_data, color=COLORS['black'], linewidth=1.5, alpha=0.3)
        series_names = None
    
    apply_buytrigger_style(ax, fig, title, xlabel, ylabel,
                          show_legend=series_names is not None,
                          legend_labels=series_names)
    plt.tight_layout()
    return fig, ax


def pie_chart(data, labels, title, explode=None, show_percentages=True):
    """
    Create branded pie chart.
    
    Args:
        data: Values for each slice
        labels: Labels for each slice
        title: Chart title
        explode: Tuple of explosion values (0.1 = explode slightly)
        show_percentages: Show percentage labels
    """
    fig, ax = plt.subplots(figsize=(10, 8), facecolor=COLORS['white'])
    
    colors = [DATA_COLORS[i % len(DATA_COLORS)] for i in range(len(data))]
    
    autopct = '%1.1f%%' if show_percentages else None
    wedges, texts, autotexts = ax.pie(data, labels=labels, colors=colors,
                                       explode=explode, autopct=autopct,
                                       startangle=90, 
                                       wedgeprops={'edgecolor': COLORS['white'], 'linewidth': 2})
    
    # Style percentage text
    if show_percentages:
        for autotext in autotexts:
            autotext.set_color(COLORS['white'])
            autotext.set_fontweight('600')
            autotext.set_fontsize(10)
    
    # Style labels
    for text in texts:
        text.set_color(COLORS['black'])
        text.set_fontsize(11)
    
    # Title
    ax.set_title(title, fontsize=18, fontweight='600', color=COLORS['black'],
                 pad=20, fontfamily='sans-serif')
    
    # Logo
    _add_logo(ax)
    
    plt.tight_layout()
    return fig, ax


def scatter_chart(x_data, y_data, title, xlabel='', ylabel='', series_names=None, sizes=None):
    """
    Create branded scatter plot.
    
    Args:
        x_data: X values (single list or list of lists for multiple series)
        y_data: Y values (single list or list of lists)
        title: Chart title
        sizes: Marker sizes (for bubble charts)
    """
    fig, ax = plt.subplots(figsize=(10, 6), facecolor=COLORS['white'])
    
    default_size = 80
    
    if isinstance(y_data[0], (list, np.ndarray)):
        for i, (x, y) in enumerate(zip(x_data, y_data)):
            color = DATA_COLORS[i % len(DATA_COLORS)]
            s = sizes[i] if sizes else default_size
            ax.scatter(x, y, s=s, color=color, alpha=0.7, 
                      edgecolor=COLORS['black'], linewidth=0.5)
    else:
        s = sizes if sizes else default_size
        ax.scatter(x_data, y_data, s=s, color=DATA_COLORS[0], alpha=0.7,
                  edgecolor=COLORS['black'], linewidth=0.5)
        series_names = None
    
    apply_buytrigger_style(ax, fig, title, xlabel, ylabel,
                          show_legend=series_names is not None,
                          legend_labels=series_names)
    plt.tight_layout()
    return fig, ax


def save_chart(fig, filename, output_dir='/mnt/user-data/outputs'):
    """Save chart with proper DPI and formatting."""
    output_path = Path(output_dir) / filename
    fig.savefig(output_path, dpi=300, bbox_inches='tight', 
                facecolor=COLORS['white'], edgecolor='none')
    plt.close(fig)
    return str(output_path)


# ============================================================
# QUICK USAGE EXAMPLES
# ============================================================
if __name__ == '__main__':
    # Example: Simple bar chart
    fig, ax = bar_chart(
        data=[45, 62, 38, 71, 55],
        labels=['Q1', 'Q2', 'Q3', 'Q4', 'Q5'],
        title='Quarterly Revenue Growth',
        xlabel='Quarter',
        ylabel='Revenue ($M)'
    )
    save_chart(fig, 'example_bar.png')
    print("Example chart saved!")
