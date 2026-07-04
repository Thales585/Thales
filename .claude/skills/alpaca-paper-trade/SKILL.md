---
name: alpaca-paper-trade
description: Execute and inspect PAPER trades on Alpaca as the execution layer for the Thales ledger. Use when the user wants to place a paper buy/sell order, check account/buying power, list positions or open orders, check an order's fill status, cancel an order, or record a fill against a Thales trio or cicada ticket. Paper trading only — no real money is at stake.
---

# Alpaca paper trade

Execution layer for the **Thales Playbook** — a paper-only calibration ledger. This
skill places and inspects orders on the Alpaca **paper** endpoint
(`https://paper-api.alpaca.markets`). No real money is ever at stake; this is road-testing
and calibration only.

## Guardrails

- **Paper only.** The helper refuses to run against any host that is not
  `paper-api.alpaca.markets`. Never point it at the live trading API.
- **Never hard-code keys.** Credentials live outside the repo in
  `~/.config/alpaca/paper-trading.env` (`chmod 600`). The script sources that file.
  If it's missing, ask the user to provide keys and write them there — never commit keys.
- **Confirm before writing.** Placing, canceling, or otherwise mutating orders is an
  action the user should approve. Show the intended order (symbol, side, qty, type,
  price) and confirm before submitting, unless the user already said to just do it.
- **Reads are free.** `account`, `clock`, `positions`, `orders`, `order` are read-only —
  run them freely to answer questions.

## The helper

All calls go through `scripts/alpaca.sh` (uses `curl`; pretty-prints with `jq` if present).

```
scripts/alpaca.sh account                       # balances, buying power, status
scripts/alpaca.sh clock                          # is the market open? next open/close
scripts/alpaca.sh positions                      # current open positions
scripts/alpaca.sh orders [open|closed|all]       # order list (default: open)
scripts/alpaca.sh order <order_id>               # one order's status / fill
scripts/alpaca.sh buy  <SYMBOL> <QTY> [limit]    # market (no price) or limit+GTC
scripts/alpaca.sh sell <SYMBOL> <QTY> [limit]    # market (no price) or limit+GTC
scripts/alpaca.sh buy-notional  <SYMBOL> <USD>   # dollar-based fractional order
scripts/alpaca.sh sell-notional <SYMBOL> <USD>   # (market, day; asset must be fractionable)
scripts/alpaca.sh cancel <order_id>              # cancel an open order
```

Notes:
- A market order placed while the market is closed is **accepted** and queued for the
  next open (status `accepted`, not `filled`). Check `clock` first if timing matters.
- Market orders use `time_in_force=day`; limit orders use `gtc`. If the user needs
  different TIF/bracket/extended-hours behavior, extend the helper rather than
  hand-rolling a raw curl.

## Typical flows

**"Buy 1 share of AAPL"** → confirm the order → `scripts/alpaca.sh buy AAPL 1` →
report the returned order id and status.

**"Did my order fill?"** → `scripts/alpaca.sh order <id>` (or `orders closed`) → report
`filled_qty` and `filled_avg_price`.

**"What do I hold / how much dry powder?"** → `scripts/alpaca.sh positions` and
`scripts/alpaca.sh account`.

## Tying trades back to the ledger

Thales grades the **mechanism**, not the P&L line. When a trade corresponds to a trio leg
(engine / tollbooth / regime-inverse) or a cicada ticket, note the pre-registered thesis and
the next dated checkpoint alongside the fill so the position can be graded later. Default trio
weights: Engine 40–45 / Tollbooth 30–35 / Inverse 25–30, no leg over 60%. Cicada tickets are a
hard-capped sleeve (<5% of book) and self-liquidate on their event date.
