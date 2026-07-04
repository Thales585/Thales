# Thales

A falsifiable **paper-trading** method and calibration ledger — named for Thales of
Miletus, who read the winter sky, rented the olive presses cheap off-season, and let them
out at his price when the harvest came: *an edge of knowledge, expressed through structure,
executed on timing.*

> **Paper trading only.** This is a hypothetical learning ledger — not financial advice and
> not a solicitation. The product of the method is **calibration**, not profit: written
> hypotheses, pre-registered kills, and honestly graded predictions.

## The method

The core of the book (~95%+) is a **ranked list of flagship trios**. Each candidate sector
is put through a gauntlet of five kill criteria; survivors are graded into a probability
tier by the strength of the thesis, the cleanliness of all three seats, and the durability
of the mechanism.

Each trio has three seats:

| Seat | Role | Default weight |
| --- | --- | --- |
| **Engine** | The growth thesis itself | 40–45% |
| **Tollbooth** | Collects whatever wins in the sector | 30–35% |
| **Regime-inverse** | Does its job when the regime turns | 25–30% |

No single leg exceeds 60%. Inversion is claimed at the *scenario* level only — weekly prices
will not decorrelate.

### The five kill criteria

A leg dies when it fails any gate:

1. **Viability** — micro-float or a plausible bankruptcy candidate.
2. **Authenticity** — trades on an unrelated narrative, not the thesis seat.
3. **Survival** — round-tripped ~−75%; failed holders whatever the moat.
4. **Self-funding** — forced into a distressed dilutive raise in the window.
5. **Non-redundancy** — correlation above ~0.9 vs an already-filled seat.

*Anti-goalpost rule: criteria may be amended between runs, never mid-run. Every candidate
needs a search-verified anchor; nothing is recalled from memory.*

### The cicada hunt (< 5% sleeve)

A standing scan — a curiosity, not a foundation — for events whose date is already fixed by
a biological, astronomical, legal, software-epoch, demographic, or infrastructure clock:
dated certainties the market has forgotten to price. Survivors become small asymmetric
tickets that self-liquidate on the event date, hard-capped as an opportunistic sleeve.

### Grading

Grade the **mechanism**, not the P&L line. A macro move that lifts every leg at once is the
regime, not the thesis — log it as a P&L event, not a graded prediction. Green P&L on a dead
mechanism is a rejection that got lucky. Checkpoints are dated; a kill is a conscious, logged
act.

## Repository layout

```
thales/
├── README.md
├── docs/                           # Method card + playbook PDFs
├── ledger/                         # The calibration ledger (the product)
│   ├── README.md                   # Current book + rules
│   └── entries/                    # One pre-registered entry per position
└── .claude/
    └── skills/
        └── alpaca-paper-trade/    # Claude Code skill: paper-trade execution layer
            ├── SKILL.md
            └── scripts/alpaca.sh   # curl-based Alpaca paper-API helper
```

**Status: development stage.** Research is ongoing, but the book is now being road-tested
live on the Alpaca paper account — see [the ledger](ledger/README.md) for the current
positions ($5,000 per complete trio, no leverage).

## The execution layer

[`alpaca-paper-trade`](.claude/skills/alpaca-paper-trade/SKILL.md) is a
[Claude Code](https://claude.com/claude-code) skill that places and inspects orders on the
Alpaca **paper** API (`https://paper-api.alpaca.markets`). It is the bridge between the
ledger and live paper execution.

Guardrails:

- **Paper-only rail** — the helper refuses to run against any host that is not
  `paper-api.alpaca.markets`.
- **No keys in the repo** — credentials are read from `~/.config/alpaca/paper-trading.env`
  (outside version control, `chmod 600`). `.gitignore` also blocks any `*.env` / secret
  files as a backstop.

```sh
# read-only
scripts/alpaca.sh account         # balances, buying power
scripts/alpaca.sh clock           # market open? next open/close
scripts/alpaca.sh positions       # open positions
scripts/alpaca.sh orders open     # order list

# mutating (confirm first)
scripts/alpaca.sh buy  AAPL 1     # market buy, 1 share
scripts/alpaca.sh sell AAPL 1 195 # limit sell @ 195 (GTC)
scripts/alpaca.sh order <id>      # check fill status
```

## Reference

The method is distilled in [docs/Thales_Method_Card.pdf](docs/Thales_Method_Card.pdf) and
[docs/Thales_Playbook.pdf](docs/Thales_Playbook.pdf).

---

*Reviewers are invited to attack the kill criteria hardest of all — that is where the method
lives or dies.*
