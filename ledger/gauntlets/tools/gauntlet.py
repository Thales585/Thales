#!/usr/bin/env python3
"""Reusable gauntlet machinery: K3/K5 stats + anchor backtest.
Usage:
  gauntlet.py <run_dir> stats                 # K3 table + K5 correlation matrix
  gauntlet.py <run_dir> books '<json>'        # books: {"name":{"SYM":w,...},...}
Data: <run_dir>/data/<SYM>.json — Alpaca monthly bars (adjustment=all).
First bar (partial month) is dropped; all remaining points are src (real feed)."""
import json, csv, os, sys, glob
import numpy as np

def load(run_dir):
    # align all symbols on the intersection of available months (IEX can miss a bar)
    raw = {}
    for f in sorted(glob.glob(f"{run_dir}/data/*.json")):
        s = os.path.basename(f)[:-5]
        raw[s] = {b["t"][:7]: b["c"] for b in json.load(open(f))["bars"]}
    common = sorted(set.intersection(*[set(v) for v in raw.values()]))[1:]  # drop partial first month
    closes = {s: np.array([raw[s][m] for m in common]) for s in raw}
    return closes, common

def main():
    run_dir, mode = sys.argv[1], sys.argv[2]
    closes, months = load(run_dir)
    syms = list(closes); n = len(months)
    rets = {s: closes[s][1:]/closes[s][:-1]-1 for s in syms}

    if mode == "stats":
        print("=== K3: trailing TR / anchor maxDD / monthly vol ===")
        for s in syms:
            c = closes[s]; tr = c[-1]/c[0]-1
            pk = np.maximum.accumulate(c); mdd = ((c-pk)/pk).min()
            k3 = "PASS" if (tr > 0 and mdd > -0.60) else "KILL"
            print(f"{s:5s} TR={tr:+7.1%}  maxDD={mdd:+7.1%}  vol={np.std(rets[s],ddof=1):5.1%}  K3:{k3}")
        print("\n=== K5: monthly-return correlations ===")
        print("      " + "".join(f"{s:>7s}" for s in syms))
        for a in syms:
            print(f"{a:5s} " + "".join(f"{np.corrcoef(rets[a],rets[b])[0,1]:7.2f}" for b in syms))
        with open(f"{run_dir}/anchors.csv","w",newline="") as f:
            w = csv.writer(f); w.writerow(["month"]+[f"{s}(src)" for s in syms])
            for i,m in enumerate(months):
                w.writerow([m]+[round(float(closes[s][i]),2) for s in syms])
        print(f"\nwrote {run_dir}/anchors.csv")

    elif mode == "books":
        import matplotlib; matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        books = json.loads(sys.argv[3])
        fig,(ax1,ax2) = plt.subplots(2,1,figsize=(11,10))
        x = range(n)
        survivors = set().union(*[set(w) for w in books.values()])
        for s in syms:
            hot = s in survivors
            ax1.plot(x, closes[s]/closes[s][0]*100, "-o" if hot else "--o",
                     ms=4, lw=2 if hot else 1, label=s)
        ax1.set_title(f"{os.path.basename(run_dir)} — indexed 100 (src: Alpaca IEX monthly, adj=all)")
        ax1.set_xticks(x); ax1.set_xticklabels(months,rotation=45,fontsize=7)
        ax1.legend(fontsize=7); ax1.grid(alpha=.3)
        print("=== Books (T0 fixed weights, buy-and-hold) ===")
        for name,w in books.items():
            b = np.zeros(n)
            for s,wt in w.items(): b += wt*closes[s]/closes[s][0]
            b *= 100
            pk = np.maximum.accumulate(b)
            print(f"{name:40s} TR={b[-1]/100-1:+7.1%}  maxDD={((b-pk)/pk).min():+7.1%}")
            ax2.plot(x,b,marker="o",ms=4,label=name)
        ax2.set_title("Books"); ax2.set_xticks(x)
        ax2.set_xticklabels(months,rotation=45,fontsize=7); ax2.legend(fontsize=8); ax2.grid(alpha=.3)
        plt.tight_layout(); plt.savefig(f"{run_dir}/backtest.png",dpi=130)
        print(f"wrote {run_dir}/backtest.png")

if __name__ == "__main__":
    main()
