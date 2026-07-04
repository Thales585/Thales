#!/usr/bin/env python3
"""Agriculture gauntlet — kill execution + anchor backtest.
Data: Alpaca IEX monthly bars (adjustment=all), Jun 2025 - Jul 2026.
All bars are real feed data (flag: src); nothing interpolated."""
import json, csv, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

D = os.path.dirname(os.path.abspath(__file__))
SYMS = ["DE", "CTVA", "ADM", "BG", "FPI", "LAND", "TSN"]

closes, months = {}, None
for s in SYMS:
    bars = json.load(open(f"{D}/data/{s}.json"))["bars"]
    # drop the partial first bar (Jun 2025) -> 13 points Jul'25..Jul'26
    bars = bars[1:]
    closes[s] = np.array([b["c"] for b in bars])
    months = [b["t"][:7] for b in bars]

n = len(months)
rets = {s: closes[s][1:] / closes[s][:-1] - 1 for s in SYMS}

print("=== K3: window survival (trailing TR, anchor maxDD) ===")
stats = {}
for s in SYMS:
    c = closes[s]
    tr = c[-1] / c[0] - 1
    peak = np.maximum.accumulate(c)
    mdd = ((c - peak) / peak).min()
    vol = np.std(rets[s], ddof=1)
    stats[s] = (tr, mdd, vol)
    k3 = "PASS" if (tr > 0 and mdd > -0.60) else "KILL"
    print(f"{s:5s} TR={tr:+7.1%}  maxDD={mdd:+7.1%}  vol(m)={vol:5.1%}  K3:{k3}")

print("\n=== K5: monthly-return correlation matrix ===")
print("      " + "".join(f"{s:>7s}" for s in SYMS))
corr = {}
for a in SYMS:
    row = ""
    for b in SYMS:
        c_ = np.corrcoef(rets[a], rets[b])[0, 1]
        corr[(a, b)] = c_
        row += f"{c_:7.2f}"
    print(f"{a:5s} {row}")

# ---- books (weights fixed at T0, buy-and-hold) ----
def book(weights):
    idx = np.zeros(n)
    for s, w in weights.items():
        idx += w * closes[s] / closes[s][0]
    return idx * 100

trio      = book({"CTVA": 0.425, "FPI": 0.325, "TSN": 0.25})
trio_alt  = book({"DE": 0.425, "FPI": 0.325, "TSN": 0.25})
naive_de  = book({"DE": 1.0})                      # obvious single-asset benchmark
naive_pair= book({"DE": 0.5, "ADM": 0.5})          # obvious pair benchmark

def bstats(x):
    peak = np.maximum.accumulate(x)
    return x[-1] / 100 - 1, ((x - peak) / peak).min()

print("\n=== Books (T0=Jul 2025, buy-and-hold 12m) ===")
for name, b in [("Trio CTVA/FPI/TSN 42.5/32.5/25", trio),
                ("Alt  DE/FPI/TSN   42.5/32.5/25", trio_alt),
                ("Naive DE 100%", naive_de),
                ("Naive DE/ADM 50/50", naive_pair)]:
    tr, mdd = bstats(b)
    print(f"{name:34s} TR={tr:+7.1%}  maxDD={mdd:+7.1%}")

# ---- outputs ----
with open(f"{D}/anchors.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["month"] + [f"{s}(src)" for s in SYMS])
    for i, m in enumerate(months):
        w.writerow([m] + [round(float(closes[s][i]), 2) for s in SYMS])

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 10))
x = range(n)
for s in SYMS:
    idx = closes[s] / closes[s][0] * 100
    ax1.plot(x, idx, marker="o", ms=4, label=s)
ax1.set_title("Agriculture candidates — indexed to 100 at Jul 2025 (all points src: Alpaca IEX monthly, adj=all)")
ax1.set_xticks(x); ax1.set_xticklabels(months, rotation=45, fontsize=7)
ax1.legend(fontsize=8); ax1.grid(alpha=0.3)
for name, b, lw in [("Trio CTVA/FPI/TSN", trio, 2.5),
                    ("Alt DE/FPI/TSN", trio_alt, 1.5),
                    ("Naive DE 100%", naive_de, 1.5),
                    ("Naive DE/ADM 50/50", naive_pair, 1.5)]:
    ax2.plot(x, b, marker="o", ms=4, lw=lw, label=name)
ax2.set_title("Books — buy-and-hold, weights fixed at T0")
ax2.set_xticks(x); ax2.set_xticklabels(months, rotation=45, fontsize=7)
ax2.legend(fontsize=9); ax2.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(f"{D}/backtest.png", dpi=130)
print(f"\nSaved {D}/anchors.csv and {D}/backtest.png")
