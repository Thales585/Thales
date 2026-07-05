---
name: hypothesis-to-trio
description: Convert a market hypothesis or thesis into a gauntlet-ready three-seat trio (engine / tollbooth / regime-inverse) for the Thales paper-trading ledger. Use this whenever the user states a hypothesis, thesis, prediction, or "what if" about a sector, technology, commodity, policy, or macro regime and wants tradable structure around it — even if they don't say "trio" (phrases like "how would I trade this idea", "build something around this thesis", "turn this into positions" all qualify). Also use when a seat looks unfillable and the user wants proxy or synthetic-short alternatives. Output is a seat proposal that feeds INTO the trio-gauntlet; it never declares survivors.
---

# Hypothesis → Trio

Turn a falsifiable hypothesis into a **seat structure** the gauntlet can then try to
kill. This skill does the *mapping*, not the judging: no kill verdicts, no backtests,
no survivor claims. Its product is a well-formed candidate slate.

**Standing frame:** paper trading only; a calibration exercise, not financial advice.

## The contract

**Input:** a hypothesis — one sentence to a paragraph. If the user gives only a vibe
("water is going to matter"), sharpen it into a falsifiable mechanism *with* them
before mapping seats; a hypothesis that can't fail can't be traded.

**Output:** the template at the bottom, always. Every candidate ticker must be
**verified tradable on Alpaca** before it appears — run
`~/thales/.claude/skills/alpaca-paper-trade/scripts/alpaca.sh` (read-only) or
`GET /v2/assets/{symbol}` on the paper API. Never assume a listing; Rheinmetall and
CATL taught us that. Never cite prices, returns, or valuations from memory — seat
mapping needs none of them, and the gauntlet will fetch real anchors later.

## Mapping the three seats

Work from the hypothesis's *mechanism*, not its sector label:

1. **ENGINE — who IS the thesis?** The asset whose economics are the hypothesis
   happening. Test: if the hypothesis is true, this name's revenue line must show it
   within the horizon, via dated catalysts. Prefer pure-plays over conglomerates
   (the RTX lesson: adjacency is not identity).
2. **TOLLBOOTH — who collects no matter which competitor wins?** Look for fee-per-unit,
   rent, royalty, stream, or regulated-return economics. Ask the flow-vs-stock
   question from the housing run: a toll on *flow* starves when volume is the regime
   casualty; a toll on the *stock* (in-force books, installed base) survives a freeze.
   Presses, not pickaxes.
3. **REGIME-INVERSE — who feeds when the hypothesis fails?** Not who *dodges* (the SRE
   lesson — regulated utilities dodge; they don't feed). The seat needs a mechanism
   that converts the hypothesis's failure mode into someone's margin. Inversion is
   claimed at scenario level only; weekly prices won't decorrelate and that's fine.

Offer 2–3 candidates per seat where they exist, with one line of seat-logic each.

## When a seat won't fill — the proxy ladder

Walk down in order; label which rung you're on, and log the cost of each rung
honestly (every rung is a wart the gauntlet pre-registration must carry):

1. **Listed proxy (ETF or carrier).** The LIT-for-CATL / EUAD-for-Rheinmetall pattern:
   a basket or related listing that carries the exposure diluted. Cost: K2
   authenticity erosion — grading must reference the true asset, not the proxy price.
   A carrier equity (CCJ carrying Westinghouse) is the stronger form of this rung.
2. **Synthetic seat via short.** Notate as **short(N)** where N is the Alpaca-tradable
   asset that *thrives* in the scenario the seat is meant to monetize the failure of.
   Most useful for an unfillable regime-inverse: if nothing *feeds* on the thesis
   failing, shorting the most thesis-levered pure-play converts its collapse into the
   seat's payoff. Be honest about the three structural costs, in the output, always:
   - it is a **hedge, not a feeder** — non-cannibalization dies by construction (the
     three seats can no longer all win together in a sector-wide bull);
   - **do not short the engine itself** — that is not an inverse seat, it is just
     less engine (redundancy in mirror form; K5 at correlation −1);
   - carry and borrow costs decay the seat; in live markets loss is unbounded. On
     the Alpaca paper account shorting is enabled, so it is testable — paper only.
3. **Declare the seat unfillable.** Sometimes that is the finding (Water; AI-DC's
   inverse; Space's tollbooth). Recommend "expect no-valid-trio" and say what future
   listing or structure would reopen the sector. A forced weak occupant is worse
   than an honest hole.

## What this skill must never do

- Declare a trio "surviving," "valid," or "passing" — only the gauntlet
  (`trio-gauntlet` skill, or `~/thales/ledger/gauntlets/` machinery) kills or spares.
- Quote prices, returns, drawdowns, correlations, or market caps from memory.
- Skip tradability verification, or bury a proxy rung's cost.

## Output template (always this shape)

```
## Hypothesis (restated, falsifiable)
<one sentence: mechanism + horizon + what would prove it wrong>

## Seat map
| Seat | Candidates (Alpaca-verified) | Seat logic (one line each) |
| Engine | ... | ... |
| Tollbooth | ... | ... |
| Regime-inverse | ... | ... |

## Proxy rungs used (if any)
<rung number, what it substitutes for, and its logged cost — or "none">

## Uninsured quadrant (first guess)
<the scenario that hurts all three seats at once>

## Hand-off
Feed to trio-gauntlet: pre-register kills BEFORE pulling data. This slate is
unjudged — expect candidates to die there.
```

**Example (compressed).** Input: *"Grid-scale storage will beat peaker plants on cost
in 3 years."* → Engine: FLNC (storage pure-play; quarterly deployments are dated).
Tollbooth: NGG (transmission collects on every electron, storage or peaker). Inverse:
a peaker-heavy IPP if one lists cleanly; else rung 2 — **short(FLNC-competitor)** is
wrong (that's intra-engine), so the honest rung-2 is short a name whose margins
*require* peaker scarcity pricing; if none is tradable, rung 3: declare and log what
listing would reopen it.
