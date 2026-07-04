# Housing gauntlet — run verdict (v1.0)

- **Run:** 2026-07-04, after [pre-registration](00-preregistration.md). Data: Alpaca IEX
  monthly bars adj=all, Jul 2025→Jul 2026, all `src` — [anchors.csv](anchors.csv),
  [backtest.png](backtest.png).

**Standing frame:** hypothetical constructions for a paper learning ledger, not
financial advice; the falsification conditions do the work; grade the mechanism, not
the luck.

## Kill table

| Candidate | Seat | Verdict | Criterion |
| --- | --- | --- | --- |
| **BLDR** | Tollbooth | **KILLED** | **K3** — TR −33.4%, maxDD −45.0%. The pre-registered tollbooth-vs-pickaxe debate was settled by data before K2 could be argued. |
| **FNF** | Tollbooth (widen 1) | **KILLED** | **K3** — TR −6.8%. Title fees need transactions; the freeze starved them. |
| **HD** | Tollbooth (widen 1) | **KILLED** | **K3** — TR −0.1%. Repair-and-remodel did not offset. |
| **ICE** | Tollbooth (widen 2) | **KILLED** | **K3** — TR −27.2%. |
| **LEN** | Engine | **KILLED** | **K3** — TR −20.2%, maxDD −34.2%. Engine contention resolved by kill, not choice. |
| **MTG** | Tollbooth (widen 2) | **Lost contention** | Passed K3 (+11.5%/−12.7%) but 0.91 corr to ESNT (K5 tangle); ESNT wins on TR and DD. |
| **AMH** | Inverse | **Lost contention** | Passed K3 (+2.1%); 0.97 corr to INVH — one bet, two wrappers; INVH wins on TR. |

**The run's finding, worth the whole exercise:** in a frozen-transaction housing
regime, every toll on *flow* (materials, title, remodel, mortgage tech) starved —
K3 killed the entire first tollbooth pool. The seat was only fillable by a toll on the
*stock*: mortgage insurance premiums on $247.9B in force (ESNT Q1 2026 — StockTitan),
which collect whether or not a single house trades.

## Survivor trio + weights

| Seat | Asset | Weight | Notes |
| --- | --- | --- | --- |
| Engine | **DHI** | 42.5% | +12.3% TR / −18.6% maxDD; the only engine to survive K3 |
| Tollbooth | **ESNT** | 32.5% | +18.3% / −10.4%; in-force premiums; K4 emphatic pass (buybacks + 7yr dividend growth). **Wart:** an MI tollbooth *pays claims* in a foreclosure wave — its tail risk deepens the uninsured quadrant. |
| Regime-inverse | **INVH** | 25.0% | +4.0% / −17.9%; rents from the priced-out; 0.54 corr vs DHI |

Flip conditions: ESNT to ~25% if MI pricing war erodes premium yield two quarters;
engine weight down if DHI margin guidance confirms incentive-driven erosion.

## Backtest as evidence

Survivor +12.2% / −14.3% vs naive DHI +12.3% / −18.6% — identical return, four points
less drawdown; the inverse seat cost nothing this regime. Dead-pool benchmark DHI/HD
50/50: +6.1%.

## Scenario grid

| Regime | DHI | ESNT | INVH |
| --- | --- | --- | --- |
| Rates cut, thaw | feeds | feeds (NIW grows) | cap-rate relief, mild feed |
| High-for-longer freeze | starves | collects in-force | **feeds** |
| Foreclosure wave (rates high + job losses) | starves | **pays claims — wart** | mixed (demand up, tenant credit down) |
| Rents soft + rates high | starves | collects | starves — **uninsured quadrant, named** |

## Log entry

- T0 (Alpaca IEX 2026-07-01 adj close): DHI $135.34-region, ESNT/INVH per anchors.csv.
- **Enacted:** $5,000 paper, no leverage — DHI $2,125 / ESNT $1,625 / INVH $1,250.
- **Kill-lines:** DHI — two consecutive quarters of gross-margin erosion attributed to
  incentives, or −60% DD. ESNT — default notice inflection >2x trailing average
  (tollbooth turning into claims-payer), or any dilutive raise. INVH — occupancy or
  blended rent growth negative two quarters (the seat's claim failing), or −60% DD.
- **Attribution warnings:** a Fed cut lifting all three at once is the regime, not the
  thesis; INVH rallying on a REIT-wide yield trade is noise; no FX leg.
- **First scheduled loop checkpoint: 2026-08-15** (aligned with the Agriculture
  checkpoint; DHI reports mid-July — early re-verify if the print is extreme).

## Limits + standing caveat

IEX monthly anchors, one regime of history, drawdowns understated, dividend-adjusted
series. Hypothetical paper learning ledger, not financial advice; the kill criteria do
the work.
