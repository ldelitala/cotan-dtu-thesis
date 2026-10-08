#!/usr/bin/env python3
"""Regenerate the tau-sweep figures for the thesis from the pipeline CSV data.

The pipeline's own plots (src/analysis/R/09_sweep_tau.R) are exported at
11x8 in / 300 dpi; shrunk into a ~3.4 in thesis panel the text scales to ~3 pt
and becomes unreadable. This script re-plots the same data at the final panel
size, so the fonts are authored for the size they are printed at.

Run:  python3 english/scripts/make_tau_sweep_figures.py
Deps: matplotlib, numpy
"""
from __future__ import annotations

import csv
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

HERE = Path(__file__).resolve().parent          # english/scripts
ENGLISH = HERE.parent                            # english/
ROOT = ENGLISH.parent                            # repo root
PIPE = ROOT / "pipeline" / "results"
IMG = ENGLISH / "images"

# One entry per figure: (csv, out, title, x-ticks, published tau, zoom)
FIGURES = [
    ("arrigoni/plots/arrigoni_tau_sweep.csv", "arrigoni_tau_sweep.png",
     "Human cell-line mixture", np.arange(0.05, 0.3001, 0.05), 0.20, None),
    ("arrigoni/plots/arrigoni_tau_sweep.csv", "arrigoni_tau_sweep_zoom.png",
     "Human cell-line mixture (zoom)", np.arange(0.16, 0.2801, 0.02), 0.20, (0.15, 0.28)),
    ("ding_cortex_2/plots/ding_merged_tau_sweep.csv", "ding_tau_sweep.png",
     "Mouse cortex (transcript clusters)", np.arange(0.05, 0.3001, 0.05), 0.09, None),
    ("ding_cortex_2/plots/ding_gene_cluster_tau_sweep.csv", "ding_gene_tau_sweep.png",
     "Mouse cortex (gene clusters)", np.arange(0.05, 0.3001, 0.05), 0.09, None),
]

plt.rcParams.update({
    "font.size": 7, "axes.titlesize": 7.5, "axes.labelsize": 7,
    "xtick.labelsize": 6.5, "ytick.labelsize": 6.5, "legend.fontsize": 6,
    "axes.grid": True, "grid.color": "0.85", "grid.linewidth": 0.5,
    "axes.spines.top": False, "axes.spines.right": False,
    "figure.dpi": 300, "savefig.bbox": "tight", "savefig.pad_inches": 0.02,
})
C_EV, C_PUB = "#F8766D", "0.35"


def load(path: Path) -> tuple[np.ndarray, np.ndarray]:
    with path.open() as fh:
        rows = list(csv.DictReader(fh))
    tau = np.array([float(r["tau"]) for r in rows])
    ev = np.array([int(float(r["events"])) for r in rows])
    return tau, ev


def make(csv_rel, out, title, xticks, published, zoom):
    tau, ev = load(PIPE / csv_rel)
    if zoom is not None:
        m = (tau >= zoom[0]) & (tau <= zoom[1])
        tau, ev = tau[m], ev[m]
    fig, ax = plt.subplots(figsize=(3.5, 2.7))
    ax.axvline(published, ls=(0, (4, 3)), lw=0.8, color=C_PUB,
               label=r"published $\tau$=%.2g" % published)
    ax.plot(tau, ev, color=C_EV, lw=1.0, marker="o", ms=2.2, label="DTU events")
    ax.set_xlabel(r"$\tau$ (min DEA contrast)")
    ax.set_ylabel("candidate count")
    ax.set_title(title)
    ax.set_xticks(xticks)
    ax.set_xticklabels(["%.2f" % t for t in xticks])
    ax.yaxis.set_major_locator(MaxNLocator(nbins=5, integer=True))
    ax.margins(x=0.02)
    ax.legend(loc="upper right", frameon=False, handlelength=1.6, borderpad=0.2)
    fig.savefig(IMG / out)
    plt.close(fig)
    print("wrote", IMG / out)


if __name__ == "__main__":
    for args in FIGURES:
        make(*args)
