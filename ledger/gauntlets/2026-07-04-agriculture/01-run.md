# Agriculture gauntlet — run verdict (v1.0)

- **Run executed:** 2026-07-04, after pre-registration was committed (see
  [00-preregistration.md](00-preregistration.md))
- **Data:** Alpaca IEX monthly bars, dividend-adjusted, Jul 2025 → Jul 2026, 13 points
  per asset, all flagged `src` (real feed, zero interpolation) — [anchors.csv](anchors.csv).
  Cross-checked against web quotes (Yahoo/StockAnalysis/MacroTrends, 2026-07-02 marks):
  DE ~$627, ADM $76.87, TSN $58.89, CTVA ~$85 — consistent with feed closes.
- **Chart:** [backtest.png](backtest.png)

**Standing frame:** hypothetical constructions for a paper learning ledger, not
financial advice; the falsification conditions do the work; grade the mechanism, not
the luck.

## Kill table

| Candidate | Seat sought | Verdict | Criterion fired |
| --- | --- | --- | --- |
| **FPI** | Tollbooth | **KILLED** | **K3** — trailing TR −2.8% (positive required); maxDD −25.2% survivable but moot. The pre-registered favorite died on contact with data. |
| **LAND** | Tollbooth | **KILLED** | **K3** — trailing TR −0.7%. Also flagged: 0.93 correlation to FPI (K5) — the two farmland REITs were one bet in two wrappers; K1 was borderline (~$400M cap) but never reached. |
| **BG** | Tollbooth | **Lost seat contention** (not killed) | Passed K3 (+37.3%, −15.8%). Lost to ADM on drawdown (−15.8% vs −7.4%) and on K2 purity: post-Viterra, BG is more trading-desk than press. Remains a valid widening candidate. |
| **DE** | Engine | **Lost seat contention** (not killed) | Passed K3 (+19.8%, −13.6%). Lost to CTVA on K2: ag+construction conglomerate vs pure-play ag science; and DE sits just off its Feb 2026 all-time high ($660.56 — MacroTrends) — the rich-entry scar the Procurement trio taught us to respect. |

## Survivor trio + weights

| Seat | Asset | Weight | Rationale |
| --- | --- | --- | --- |
| **Engine** | **CTVA** (Corteva) | **42.5%** | Pure-play seed science + crop protection; +20.1% TR, −17.0% maxDD, lowest engine vol (6.8%/mo). Dated catalysts: quarterly earnings (next expected early Aug 2026 — verify at checkpoint) plus USDA WASDE monthly prints. |
| **Tollbooth** | **ADM** | **32.5%** | Owns the processing layer between harvest and consumer — literally presses (oilseed crush). Collects on volume whichever crop or farmer wins. +46.2% TR, −7.4% maxDD. **Warts logged:** crush spreads are cyclical (economics are not purely fee-like), and the intersegment-sales accounting scar — SEC settled 2026-01-27 for $40M, DOJ closed with no action (SEC 8-K). K4 pass: settlement paid from operations, no dilutive raise in window. |
| **Regime-inverse** | **TSN** (Tyson) | **25.0%** | Cheap-feed beneficiary: a grain glut that starves the engine feeds the protein margin. +16.6% TR, −11.2% maxDD. K5 clean: 0.56 corr vs CTVA, 0.54 vs ADM. |

No leg exceeds 60%; weights are the book defaults — catalyst density did not justify
deviation. **Flip conditions:** ADM weight drops to ~25% if crush margins invert for two
consecutive quarters (tollbooth behaving like a trading book); CTVA/TSN rebalance flips
if farm income prints force seed-pricing concessions (engine weakening confirmed).

## Backtest as evidence, not oracle

The survivor book returned **+27.7% / −10.3% maxDD** vs naive DE 100% (+19.8% / −13.6%)
and naive DE/ADM 50/50 (**+33.0% / −5.1%**). The naive pair won the backtest. The trio
stands anyway, argued as follows: the pair concentrates 50% in an engine at its all-time
high with zero regime insurance; its edge is one regime of history (a benign ag year).
The trio pays ~5 points of trailing return for a funded inverse seat and a pure engine.
That is the same argument that upheld the silver kill in Metals — redundancy and
forward mechanism over rear-view P&L. Killing the farmland REITs also *cost* nothing:
the dead-favorite book (CTVA/FPI/TSN) backtests at just +11.8%.

## Scenario grid

| Regime | CTVA | ADM | TSN |
| --- | --- | --- | --- |
| Ag bull (strong farm income) | feeds | feeds (volume) | neutral–squeezed (feed costs up) |
| Bumper glut (grain prices crash) | starves | mixed (cheap input, volume holds) | **feeds** |
| Food-demand recession + high inputs | starves | starves | starves — **the uninsured quadrant, named** |
| Trade war / export shock | mixed | starves (flows reroute) | mixed (export protein hit) |

Non-cannibalization holds: in a broad ag bull all three can win together.

## Log entry — T0 marks (Alpaca IEX adj close, 2026-07-01 monthly bar)

- CTVA $85.79 · ADM $76.80 · TSN $58.92 · USD base, no FX leg.
- **Enactment:** $5,000 paper, no leverage — CTVA $2,125 / ADM $1,625 / TSN $1,250
  (order IDs in the ledger entry).
- **Kill-lines per leg (mid-run, execution only):**
  - CTVA: kill on forced guidance cut attributing seed-price concessions to farmer
    distress two quarters running, or −60% drawdown.
  - ADM: kill on any new accounting restatement (the scar reopening is a K2/K4 kill,
    not a flag), or crush-margin inversion two consecutive quarters.
  - TSN: kill on protein-demand collapse with feed costs still high (inverse without
    its regime), or −60% drawdown.
- **Attribution warnings, standing:** a rate cut or dollar move lifting all three at
  once is the Fed, not the thesis; TSN rallying on an avian-flu supply shock is
  *noise* for our mechanism (it's not a feed-cost story) — log WHY before crediting
  the seat; no FX leg, so FX flattery is not available as an excuse.
- **Grader calendar:** earnings cluster (CTVA, ADM, TSN — late Jul/early Aug 2026,
  dates to verify at checkpoint); USDA WASDE monthly; August crop production report.
- **First scheduled loop checkpoint: 2026-08-15** — after the earnings cluster and the
  August WASDE. Re-verify prices, re-test every kill-line, verdict-in-progress per leg.

## Limits + standing caveat

Monthly anchors from a single feed (IEX — thinner volume than SIP, closes may differ
marginally from consolidated tape); one regime of history (a benign-to-strong ag year);
anchor drawdowns understated vs daily reality; dividend-adjusted series flatter
raw-price optics for the yield names. Hypothetical constructions for a paper learning
ledger, not financial advice; the kill criteria do the work.
