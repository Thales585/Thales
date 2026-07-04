# Agriculture trio — first gauntlet-born position (v1.0)

- **Enacted:** 2026-07-04 22:28 UTC (orders queued; fills expected 2026-07-06 09:30 ET)
- **Notional:** $5,000 · no leverage
- **Source:** full gauntlet run 2026-07-04 — see
  [gauntlets/2026-07-04-agriculture/](../gauntlets/2026-07-04-agriculture/01-run.md)
  (pre-registration, kill table, anchors.csv, backtest.png). This is the first position
  in the book born from a from-scratch gauntlet rather than inherited from the playbook.
- **Tier:** unranked pending first checkpoint; enters below Procurement until graded.

## Pre-registered thesis

Bumper-crop glut is the scenario axis: a glut starves the engine (seed/chem pricing
power), the presses keep collecting on volume (tollbooth), and cheap feed expands
protein margins (inverse feeds).

## Seats

| Seat | Asset | Symbol | Weight | Notional | Order ID |
| --- | --- | --- | --- | --- | --- |
| Engine | Corteva | CTVA | 42.5% | $2,125 | `2f1486c4-1772-4749-b189-5d7806ffbd50` |
| Tollbooth | Archer-Daniels-Midland | ADM | 32.5% | $1,625 | `c45bf5c8-64f6-4f4d-a4fd-4fd6c39f9b5b` |
| Regime-inverse | Tyson Foods | TSN | 25.0% | $1,250 | `989dd13b-6f2b-4b98-9024-35f5a584db45` |

## Gauntlet lineage (what died to make this)

FPI and LAND — the pre-registered tollbooth favorites — killed at K3 (negative trailing
returns) and mutually redundant at 0.93 correlation. DE and BG passed all kills but lost
seat contention to CTVA (K2 purity) and ADM (drawdown + K2). Backtest: survivor book
+27.7% / −10.3% vs naive DE/ADM pair +33.0% / −5.1% — trio upheld against a winning
naive benchmark on forward-mechanism grounds (funded inverse seat; no all-time-high
concentration). Full argument in the run file.

## Kill-lines (execution only until next run)

- **CTVA:** guidance cut attributing seed-price concessions to farmer distress, two
  quarters running; or −60% DD.
- **ADM:** any new accounting restatement (scar reopening = kill, not flag); or crush
  margins inverted two consecutive quarters.
- **TSN:** protein-demand collapse with feed costs still high; or −60% DD.

## Checkpoint

- **First grade date: 2026-08-15** — after the CTVA/ADM/TSN earnings cluster and the
  August WASDE. Attribution before amendment; avian-flu-driven TSN moves are noise for
  this mechanism, not thesis confirmation.

## Fill log

- 2026-07-04 — all three orders `accepted`, awaiting Monday open. Fills TBD.
