"""
enhanced_plt_utils.py

Author: Hamza Abdelhedi

Last Updated: December 2023

Tested on:
- Python 3.10.12
- Matplotlib 3.8.1

## Contents:

- `plt_enhanced()`: Sets plotting parameters to improve figure readability. Call it before you start plotting. Note: This update modifies defaults, allowing custom settings in your scripts.

---

This utility script provides convenient function for enhancing Matplotlib plots and improved readability.
"""

import matplotlib.pyplot as plt
import numpy as np

def plt_enhancing(
    label_size="x-large",
    line_width=1.5,
    spines_right=False,
    spines_top=False,
    title_size="x-large",
    cap_size=4,
    figure_title_size="xx-large",
    figure_title_weight="bold",
    auto_layout=True,
    font_size=12,
    legend_size="large",
    dashed_pattern=[8.0, 4.0],
    line_width_global=2.5,
    marker_edge_width=2.5,
    marker_size=10,
    patch_line_width=2.5,
    savefig_format="svg",
    savefig_bbox="tight",
    xtick_label_size="x-large",
    xtick_major_size=3.0,
    xtick_major_width=2.0,
    ytick_label_size="x-large",
    ytick_major_size=5.0,
    ytick_major_width=2.0,
):
    """
    Enhance pyplot defaults to become publication-ready.

    Args:
        label_size (str): Size of labels. Default: "x-large"
        line_width (float): Width of lines. Default: 1.5
        spines_right (bool): Whether to show right spines. Default: False
        spines_top (bool): Whether to show top spines. Default: False
        title_size (str): Size of titles. Default: "x-large"
        cap_size (float): Size of error bar caps. Default: 4
        figure_title_size (str): Size of figure titles. Default: "xx-large"
        figure_title_weight (str): Weight of figure titles. Default: "bold"
        auto_layout (bool): Whether to use figure autolayout. Default: True
        font_size (int): Font size. Default: 12
        legend_size (str): Font size of legends. Default: "large"
        dashed_pattern (list): Pattern for dashed lines. Default: [8.0, 4.0]
        line_width_global (float): Global line width. Default: 2.5
        marker_edge_width (float): Marker edge width. Default: 2.5
        marker_size (int): Marker size. Default: 10
        patch_line_width (float): Width of patch lines. Default: 2.5
        savefig_format (str): Format for saving figures. Default: "svg"
        savefig_bbox (str): Bbox parameter for saving figures. Default: "tight"
        xtick_label_size (str): Size of x-axis tick labels. Default: "x-large"
        xtick_major_size (float): Size of x-axis major ticks. Default: 8.0
        xtick_major_width (float): Width of x-axis major ticks. Default: 2.0
        ytick_label_size (str): Size of y-axis tick labels. Default: "x-large"
        ytick_major_size (float): Size of y-axis major ticks. Default: 8.0
        ytick_major_width (float): Width of y-axis major ticks. Default: 2.0

    Returns:
        None
    """

    params = {
        "axes.labelsize": label_size,
        "axes.linewidth": line_width,
        "axes.spines.right": spines_right,
        "axes.spines.top": spines_top,
        "axes.titlesize": title_size,
        "errorbar.capsize": cap_size,
        "figure.titlesize": figure_title_size,
        "figure.titleweight": figure_title_weight,
        "figure.autolayout": auto_layout,
        "font.size": font_size,
        "legend.fontsize": legend_size,
        "lines.dashed_pattern": dashed_pattern,
        "lines.linewidth": line_width_global,
        "lines.markeredgewidth": marker_edge_width,
        "lines.markersize": marker_size,
        "patch.linewidth": patch_line_width,
        "savefig.format": savefig_format,
        "savefig.bbox": savefig_bbox,
        "xtick.labelsize": xtick_label_size,
        "xtick.major.size": xtick_major_size,
        "xtick.major.width": xtick_major_width,
        "ytick.labelsize": ytick_label_size,
        "ytick.major.size": ytick_major_size,
        "ytick.major.width": ytick_major_width,

    }

    plt.rcParams.update(params)