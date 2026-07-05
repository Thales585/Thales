# The Ledger

Every position in the book gets a pre-registered entry **before or at enactment**: thesis,
seats, weights, kill criteria status, and a dated checkpoint. Grading happens against the
entry as written — the anti-goalpost rule applies (criteria amended only between runs,
never mid-run).

> Paper trading only. A calibration ledger, not financial advice.

## Structure

- `entries/` — one file per position/trio, named `YYYY-MM-DD-<slug>.md`
- Each entry is graded at its dated checkpoint: **mechanism alive / mechanism dead**,
  logged separately from P&L. Green P&L on a dead mechanism is a rejection that got lucky.

## Account

- Broker: Alpaca **paper** account `PA3AXI8V4TCX` (starting equity $100,000)
- Execution: `.claude/skills/alpaca-paper-trade/scripts/alpaca.sh`
- Constraint: **no leverage** — total book notional stays within cash.

## Current book (as of 2026-07-04)

| Entry | Tier | Notional | Status |
| --- | --- | --- | --- |
| [Uranium trio](entries/2026-07-04-uranium-trio.md) | 1 · Flagship | $5,000 | orders queued |
| [Electrons trio](entries/2026-07-04-electrons-trio.md) | 2 | $5,000 | orders queued |
| [Metals trio](entries/2026-07-04-metals-trio.md) | 3 | $5,000 | orders queued |
| [Procurement trio](entries/2026-07-04-procurement-trio.md) | 4 | $5,000 | orders queued |
| [Agriculture trio](entries/2026-07-04-agriculture-trio.md) | unranked (checkpoint 2026-08-15) | $5,000 | orders queued |
| [Housing trio](entries/2026-07-04-housing-trio.md) | unranked (checkpoint 2026-08-15) | $5,000 | orders queued |
| [GLP-1 trio](entries/2026-07-04-glp1-trio.md) | unranked (checkpoint 2026-08-15) | $5,000 | orders queued |
| [Defense trio](entries/2026-07-04-defense-trio.md) | unranked (checkpoint 2026-08-15) | $5,000 | orders queued |
| [AAPL road test](entries/2026-07-04-aapl-road-test.md) | — (plumbing) | ~$210 | order queued |

Deployed: ~$40,210 in trios + $45,000 control arm = ~$85,210 of $100,000 (~85%). Cicada sleeve: empty (cap <5%).

## Findings (sectors gauntleted, no position taken)

| Sector | Finding |
| --- | --- |
| [Space](gauntlets/2026-07-04-space/01-run.md) | The sector eats its own tollbooths — RKLB acquiring IRDM, Amazon absorbing GSAT's Apple toll; inverse claim (VSAT) emptied by a defense-boom rally. No valid trio. |
| [AI-datacenter power](gauntlets/2026-07-04-ai-datacenter/01-run.md) | Nothing tradable feeds on an AI-capex bust; all three pre-named inverse attempts killed. Engine and tollbooth clean but seatless. No valid trio. |
| Water (playbook) | Regime-inverse seat unfillable. |
| Shipping (playbook) | Killed on timing at a front-page high. |

Gauntlet runs live in `gauntlets/` — pre-registration, kill tables, anchor data, and
backtests for every sector put through the machinery, including the ones that produced
no position.
