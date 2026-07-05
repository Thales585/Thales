# Thesis Trade Plan: AI Datacenter Capex Cycle Cracks Within 18 Months

**Ledger:** Thales (Alpaca paper) · **Date opened:** 2026-07-04 · **Account state checked:** $100,000 equity, flat book, options level 3, shorting enabled — clean slate.

---

## 1. The thesis, restated so it can be wrong

> **H:** Between now and **January 21, 2028**, hyperscaler/neocloud AI infrastructure orders get cancelled or materially pushed out, GPU lead times collapse toward normal (<10 weeks), and the market reprices the AI supply chain down at least 30% from July 2026 levels.

That date isn't arbitrary — it's the Jan-2028 LEAPS expiry, which is 18.5 months out. The trade is time-boxed by construction: if nothing has cracked by then, the thesis was wrong and the position self-liquidates. That's the discipline the ledger exists to enforce.

**What "crack" observably looks like (any two of):**
- A top-5 hyperscaler guides capex *down* year-over-year
- NVDA data-center revenue declines sequentially for 2 quarters
- GPU lead times < 10 weeks / used H100-H200 rental prices down >50%
- A major neocloud (CoreWeave-class) credit event or covenant breach
- Vertiv/Eaton book-to-bill < 1.0

## 2. What the market is already telling us (pulled live from Alpaca, Jan-2028 chain)

| Underlying | Spot | Jan-28 ~20Δ put IV | Read |
|---|---|---|---|
| NVDA | $194.51 | **~44%** | Cheapest crash insurance in the complex |
| SMH | $591.93 | ~52% | Middling |
| VRT | $300.50 | **~71%** | Market *already* prices cancellation risk here |

This is the single most important input to structuring: **the market agrees with you most where Vertiv is concerned and least where Nvidia is concerned.** So you buy convexity where it's cheap (NVDA), and express the second-order leg (VRT) in a vol-neutral way (short stock), because buying 71%-IV puts means paying up for your own idea.

Also note the tape: yesterday SMH was −4.6%, DELL −7.3%, VRT −3.5%, ANET −4.0% while GLD rose +2%. The theme is already wobbling. Good for conviction, bad for entry prices on vol — hence the scale-in schedule below.

## 3. Structure — three legs, one budget

Total risk budget: **~$7,500 (7.5% of ledger)**. A "the-whole-cycle-cracks" thesis is a low-probability/high-payoff bet; it gets lottery-ticket sizing, not core sizing. In the Thales spirit: small fixed premium, large convexity — rent the olive presses, don't buy the grove.

### Leg A — The engine, via cheap convexity: NVDA Jan-2028 $150 puts

- **Ticket:** BUY 3 × `NVDA280121P00150000` (Jan-21-2028 $150P), limit ~$15.75 (quoted 15.54/15.73, delta −0.20, IV 44%)
- **Cost:** ~$4,725. Max loss = premium.
- Strike ≈ 23% OTM. If the cycle cracks, NVDA doesn't fall 23% — it falls 50-70% (see Cisco 2000-01: −88%). At NVDA $100, these are worth ≥$50 → ~3.2x. At $70, ~$80 → ~5x. Vol expansion in a crack adds more.
- **Why not short the stock:** unbounded upside risk against a name that can rally 40% on one earnings print. Puts convert "right eventually" into a survivable position.
- **Cheaper variant if you want more contracts:** the 150/100 put spread (~$10 net) caps payoff at ~5x but cuts theta. For a "crack" thesis I prefer outright puts — the whole point is the fat left tail.

### Leg B — The second-order casualty, vol-neutral: short VRT stock

Cooling/power equipment is where order cancellations show up *first and hardest* — it's the pure capex-flow business with no software cushion. But its options already price this (71% IV), so:

- **Ticket:** SELL SHORT 30 × VRT @ market (~$300.50) → ~$9,015 notional
- **Hard stop:** buy-to-cover at **$375** (+25%) → max loss ~$2,250
- No theta bleed, no IV overpay, and VRT's beta to a capex crack is higher than NVDA's (it fell ~65% peak-to-trough in the early-2025 DeepSeek scare vs NVDA's ~40%).

### Leg C — The "wrong-for-the-right-reasons" hedge: TLT

Two failure modes for legs A+B: (1) the boom keeps going — premium budget already caps that; (2) the crack happens *because of* a broad recession, in which case you're right but want a second payer. A capex bust of this size is disinflationary and forces cuts:

- **Ticket:** BUY 6 × TLT @ ~$85.53 → ~$513. Token size — this is a placeholder/diversifier, and it also hedges the scenario where the Fed cuts hard and *reflates* the bubble (TLT up cushions put decay).
- Optional upgrade: TLT Jan-2028 $95 calls instead, same logic, more convexity.

**Total at risk: $4,725 (A) + $2,250 (B stop) + ~$100 (C drawdown tolerance) ≈ $7,075.** Cash remaining ~$85k stays in the ledger untouched.

### Entry schedule
Vol is elevated after yesterday's selloff. Enter **1/3 now, 1/3 on 2026-08-01, 1/3 after NVDA's Aug-2026 earnings** (whichever way it breaks — if it rips, you get cheaper strikes; if it cracks, the first tranche pays).

## 4. Pre-registered kill criteria (write these in the ledger *now*, argue with them never)

| Date | Checkpoint | Kill trigger | Action |
|---|---|---|---|
| **2026-11-30** | Q3 hyperscaler + NVDA earnings | All top-4 hyperscalers guide 2027 capex UP y/y **and** NVDA DC revenue growth ≥ +40% y/y | Cut all legs by 50% |
| **2027-04-30** | Supply-chain check | TSMC CoWoS still sold out through 2028 **and** GB/Rubin lead times still > 30 weeks | Exit Leg B entirely, halve Leg A |
| **2027-10-01** | Time-value salvage | No crack signal (Section 1 list) has fired | Close everything, log thesis as falsified |
| Any time | Leg B stop | VRT ≥ $375 | Cover short (automatic stop order) |
| Any time | Thesis-breaker | NVDA announces demand visibility via new $100B+ multi-year committed orders that are *prepaid or take-or-pay* | Full exit — cancellable backlog is your thesis; non-cancellable backlog kills it |

**Profit-taking rules (pre-registered too):** NVDA < $150 → sell 1 of 3 puts (recoup ~full premium), trail the rest. VRT < $200 → cover half the short. Never let a >2x winner round-trip to zero.

## 5. Monitoring dashboard (weekly, 10 minutes)

1. **GPU lead times** — Nvidia earnings-call commentary + TSMC monthly revenue (a y/y decel below +15% is your canary)
2. **Vertiv orders/backlog** — quarterly; book-to-bill is the purest cancellation gauge in the market
3. **Neocloud credit** — CoreWeave bond prices / any GPU-backed-loan distress headlines; the crack likely starts in leveraged buyers, not hyperscalers
4. **Used-GPU rental spot prices** (e.g., H200 $/hr on open marketplaces) — collapsing rental rates precede cancelled orders by ~2 quarters
5. **Depreciation-schedule changes** — any hyperscaler *shortening* GPU useful life is a pre-writedown tell

## 6. Why this structure and not the obvious alternatives

- **SOXS or other levered inverse ETFs:** ruinous decay over an 18-month horizon; they're day-trading tools. (It was +15% yesterday — and still down enormously over any long window.)
- **Shorting SMCI/DELL:** already crushed (SMCI $27, DELL −7.3% yesterday); worst-house-in-a-bad-neighborhood shorts get squeezed hardest on relief rallies.
- **SMH puts:** fine, but at 52% IV vs NVDA's 44% you pay index prices for less convexity than the epicenter name offers.
- **Just waiting:** the whole point of the ledger — a thesis without a dated, falsifiable, costed position is a vibe.

## 7. Ledger entry (copy into Thales log)

```
2026-07-04 | THESIS-011 "AI capex crack" | horizon 2028-01-21 | budget $7.5k (7.5%)
  A: +3 NVDA280121P00150000  @ ~15.75  (risk $4,725)
  B: -30 VRT @ ~300.50, stop $375      (risk $2,250)
  C: +6 TLT @ ~85.53                   (diversifier)
  Kill: 2026-11-30 capex-guide check / 2027-04-30 lead-time check / 2027-10-01 hard exit
  Falsified if: hyperscaler capex guided up through 2027 AND lead times stay >30wk
  Payoff if right: Leg A 3-5x, Leg B ~+40-60%, est. +$18-28k on $7k risked
```

One honest caveat to log alongside it: capex cycles crack later than bears expect far more often than earlier. The 18-month clock and the fixed premium are what make being early survivable — respect them more than the thesis itself.
