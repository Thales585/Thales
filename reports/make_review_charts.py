#!/usr/bin/env python3
"""Charts for the 2026-07-05 project review.
Chart 1: all 8 enacted trio-books indexed to 100 at 2026-01 (YTD), pre-trade.
Chart 2: trailing-12m return vs anchor maxDD scatter, one dot per trio-book.
Data: Alpaca IEX monthly bars adj=all (data-2026-07-05/), all src.
Weights: Engine 42.5 / Tollbooth 32.5 / Inverse 25 (book convention)."""
import json, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data-2026-07-05")

# trio: (engine, tollbooth, inverse), display name, playbook vs gauntlet
TRIOS = [
    (("NXE","CCJ","EQT"),   "Uranium",     "playbook"),
    (("LIT","NGG","FLNC"),  "Electrons",   "playbook"),
    (("GLD","WPM","PPLT"),  "Metals",      "playbook"),
    (("XMTR","FAST","RBA"), "Procurement", "playbook"),
    (("CTVA","ADM","TSN"),  "Agriculture", "gauntlet"),
    (("DHI","ESNT","INVH"), "Housing",     "gauntlet"),
    (("LLY","MCK","DVA"),   "GLP-1",       "gauntlet"),
    (("EUAD","HEI","DAL"),  "Defense",     "gauntlet"),
]
W = np.array([0.425, 0.325, 0.25])

def load(sym):
    bars = json.load(open(f"{D}/{sym}.json"))["bars"][1:]  # drop partial first month
    months = [b["t"][:7] for b in bars]
    return months, np.array([b["c"] for b in bars])

months, _ = load("NXE")
n = len(months)
ytd0 = months.index("2026-01")  # YTD index base

def book(legs):
    idx = np.zeros(n)
    for s, w in zip(legs, W):
        _, c = load(s)
        idx += w * c / c[0]
    return idx * 100  # indexed to full-series start

# ---- Chart 1: YTD book curves (re-based to Jan 2026 = 100) ----
fig, ax = plt.subplots(figsize=(11, 6.2))
cmap = plt.cm.tab10
stats = {}
for i, (legs, name, kind) in enumerate(TRIOS):
    b = book(legs)
    ytd = b / b[ytd0] * 100
    ls = "-" if kind == "gauntlet" else "--"
    ax.plot(range(ytd0, n), ytd[ytd0:], ls, marker="o", ms=4, color=cmap(i),
            label=f"{name} ({kind})")
    # full-window stats for chart 2
    tr = b[-1]/b[0] - 1
    peak = np.maximum.accumulate(b); mdd = ((b-peak)/peak).min()
    ytd_ret = ytd[-1]/100 - 1
    stats[name] = (tr, mdd, ytd_ret, kind)
ax.axhline(100, color="gray", lw=0.8, alpha=0.6)
ax.set_title("Enacted trio-books, YTD 2026 (indexed to Jan 2026 = 100) — pre-trade, through 2026-07-01\n"
             "Weights 42.5/32.5/25 · Alpaca IEX monthly adj close · solid = gauntlet-born, dashed = playbook",
             fontsize=10)
ax.set_xticks(range(ytd0, n)); ax.set_xticklabels(months[ytd0:], rotation=45, fontsize=8)
ax.set_ylabel("Index (Jan 2026 = 100)")
ax.legend(fontsize=8, ncol=2); ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(f"{os.path.dirname(D)}/chart1-trios-ytd.png", dpi=130)

# ---- Chart 2: trailing-12m TR vs maxDD scatter ----
fig, ax = plt.subplots(figsize=(9, 6.2))
for name, (tr, mdd, ytd_ret, kind) in stats.items():
    m = "o" if kind == "gauntlet" else "s"
    col = "#1f77b4" if kind == "gauntlet" else "#7f7f7f"
    ax.scatter(mdd*100, tr*100, s=120, marker=m, color=col, zorder=3)
    ax.annotate(name, (mdd*100, tr*100), textcoords="offset points",
                xytext=(7, 4), fontsize=9)
ax.axhline(0, color="gray", lw=0.8); ax.set_xlabel("Anchor max drawdown, trailing 12m (%)")
ax.set_ylabel("Total return, trailing 12m (%)")
ax.set_title("Trio-book risk/return, trailing 12 months (pre-trade)\n"
             "circle = gauntlet-born · square = playbook · anchor maxDD understated vs daily",
             fontsize=10)
ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(f"{os.path.dirname(D)}/chart2-risk-return.png", dpi=130)

# ---- print a table for the report ----
print(f"{'Trio':12s} {'kind':9s} {'YTD':>8s} {'12mTR':>8s} {'maxDD':>8s}")
for name, (tr, mdd, ytd_ret, kind) in stats.items():
    print(f"{name:12s} {kind:9s} {ytd_ret:+7.1%} {tr:+7.1%} {mdd:+7.1%}")
