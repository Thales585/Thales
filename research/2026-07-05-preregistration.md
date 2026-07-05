# Pre-Registration — SIGNED / BINDING

**Written 2026-07-05, before any post-entry data exists. Paper trading only; a calibration
study, not financial advice.**

> **Status: SIGNED / BINDING as of 2026-07-05. Control arm ENACTED 2026-07-05; study
> T0 = 2026-07-06.** v1 was audited by an independent model (Fable) and graded
> *not-yet-sound*; v2 adopted every fix; v3 settled the three operator decisions —
> **Electrons → ICLN**, **Defense → ITA report-only**, **breadth → hard gate at 6 of 7**.
> The 9-ETF control arm ($45k) was enacted 2026-07-05 to fill the same 2026-07-06 open as
> the trios, so **T0 = 2026-07-06** (the clean common start of §8). Positions and order IDs
> in [ledger/entries/2026-07-05-control-arm.md](../ledger/entries/2026-07-05-control-arm.md).
> The study clock now runs; the single verdict is due ~2027-07-06.

---

## 0. Why this document exists

Every integrity failure so far came from deciding what counted as success *after* seeing
results. This fixes the question, benchmark, metric, thresholds, **and the handling of
every foreseeable edge case** before the forward data exists — so the answer cannot be
reverse-engineered. Written for a skeptical, non-technical broker desk whose first
question is *"why not just buy the sector fund?"*

## 1. The primary research question

> **Over a fixed 12-month hold (entered 2026-07-06, one verdict at 12 months), does the
> Thales *structure* — a concentrated three-seat re-weighting of a sector plus an internal
> regime-inverse hedge — deliver a better pain-adjusted return (§4) than the
> market-preferred sector fund a retail client would otherwise buy to express the same
> theme, held the same way, over the same window?**

**This is a test of structure, not stock-picking.** The trios deliberately re-weight
(mostly) the same names the sector fund already holds, then add a hedge leg. High overlap
between a trio and its benchmark is therefore *expected and fair* — the question is
whether the deliberate concentration-plus-hedge beats owning the cap-weighted fund. Framing
it this way (rather than as stock selection) is what makes the overlapping pairs legitimate
rather than circular.

## 2. The baseline

**Series of record: a computed total-return series** — daily closing values, dividends
reinvested, both arms from the same data source — reconciled against the Alpaca paper
fills at entry. The live paper positions are the desk-facing exhibit you can pull up and
eyeball; the *scored* number is the computed total-return series, because Alpaca paper
dividend/corporate-action handling is unreliable and the two arms have very different
yields (this alone is worth 1–3 pp against an 8 pp guardrail).

**Benchmark selection rule (operationalized, uniform):** the **largest-AUM US-listed ETF
in the theme's category as of 2026-07-05**; any deviation logged with a reason.

| Trio (legs) | Theme | Benchmark | Overlap with trio legs | Note |
|---|---|---|---|---|
| Uranium (NXE/CCJ/EQT) | uranium | **URA** | high (CCJ, NXE are top URA holdings; ~75% of trio) | pair mostly tests weighting + the EQT hedge |
| Electrons (LIT/NGG/FLNC) | electrification | **ICLN** | low–moderate | no clean single-fund analog; ICLN chosen for recognizability, solar/wind tilt logged |
| Metals (GLD/WPM/PPLT) | precious metals | **GLD** *(was GDX)* | GLD = the engine leg | swapped per audit: GLD is the fund a client actually buys, and harder to beat than miners |
| Procurement (XMTR/FAST/RBA) | industrials | **XLI** | low (names are small in XLI) | broad benchmark, logged |
| Agriculture (CTVA/ADM/TSN) | agribusiness | **MOO** | high (CTVA, ADM top-10 MOO) | tests weighting + TSN hedge |
| Housing (DHI/ESNT/INVH) | homebuilding | **XHB** | moderate (DHI in XHB; ESNT/INVH outside) | ITB is the alternative |
| GLP-1 (LLY/MCK/DVA) | healthcare | **XLV** | very high (all 3 legs are XLV names; LLY is #1) | most circular — explicitly a concentration+hedge test |
| Defense (EUAD/HEI/DAL) | aerospace & defense | **ITA — report-only** | low | Europe-vs-US confound; excluded from binding count, reported for context |

**Whole-market anchor:** a **$5,000 SPY** position, same day, as the "do nothing clever"
reference. Role is defined in §5 (it is context, not a success gate).

### Decisions locked (2026-07-05)

- **Electrons → ICLN.** No dominant fund matches "batteries + grid + storage"; ICLN is the
  recognizable large-AUM clean-energy fund a retail client would actually buy. Its
  solar/wind tilt is a logged imperfection, not corrected for.
- **Defense → ITA, report-only.** ITA (US primes) vs the Europe-tilted trio is a
  geography confound the thesis itself predicts, so the pair is **excluded from the binding
  verdict** and reported for context only. This keeps every *scored* benchmark a true
  "sector fund a client would buy." **Scored pairs therefore N = 7** (Uranium, Electrons,
  Metals, Procurement, Agriculture, Housing, GLP-1).

## 3. What is compared

Per pair (trio vs its benchmark) and at book level (equal-weight 8 trios vs equal-weight
8 benchmarks vs SPY). Fixed weights, no rebalancing, full window.

## 4. Metrics (pre-declared, edge cases pinned)

1. **Primary — pain-adjusted return:** total return ÷ |max drawdown|, where **max
   drawdown is computed on daily closing values** (not monthly — monthly understates it,
   and the choice must be fixed now). Plain-English: *dollars made per dollar of
   worst-case loss.*
   - **Negative-return rule:** if *both* arms of a comparison have negative total return
     over the window, the ratio is not meaningful (it can rank a bigger loss higher), so
     the pair is judged on **max drawdown alone** — smaller drawdown wins.
   - **Near-zero-drawdown rule:** if an arm's max drawdown is smaller than 2%, the
     denominator is floored at 2% to avoid an unbounded ratio.
2. **Always reported alongside — raw total return.** So a win bought by hiding in cash-like
   names cannot pass silently.
3. **Report-only (no verdict weight):** return ÷ volatility (Sharpe-like), and the
   mechanism-confirmation rate (calibration count, graded independently of P&L).

## 5. Verdict rule (all conditions joint; committed now)

The 12-month verdict is **one of three labels — success / mixed / failure** — decided
mechanically over the **7 scored pairs** (Defense report-only, excluded):

- **SUCCESS requires *all four*:** (i) the trio book beats the benchmark book on
  pain-adjusted return; **and** (ii) the trio book's raw total return is **no more than 8 pp
  below** the benchmark book; **and** (iii) the trio book also beats **SPY** on
  pain-adjusted return; **and** (iv) **breadth ≥ 6 of 7** scored pairs beat their own
  benchmark on pain-adjusted return. Miss any one → not a success.
- **FAILURE:** the trio book loses the pain-adjusted comparison to the benchmark book, **or**
  breaches the 8 pp return guardrail, **or** breadth ≤ 3 of 7 (worse than a coin flip).
- **MIXED:** anything else. Pre-labeled now so no in-between result can be dressed as a win.

**Breadth is a hard gate (operator's choice, eyes open).** With N = 7 correlated long-only
pairs in one regime, the binding bar is **6 of 7** — the proportional equivalent of the
requested "7 of 8," and ~6.25% likely by chance (vs the ~36% of a 5/8 majority), so a pass
means something. This is a demanding gate that a single unlucky pair can sink; that risk is
accepted deliberately, because a *failure here is itself informative* (see §5b). *(If you
want the absolute strictest, 7 of 7 is available — ~0.8% by chance — say the word.)*

## 5b. What each outcome is pre-committed to teach

Declaring the lessons in advance stops us from inventing a flattering moral after the fact:

- **Success** (all four gates): weak evidence the structure adds value *in this regime* —
  still not a validation of the hedge, which needs a stress event (§7.2).
- **Failure via breadth** with mechanisms mostly *confirmed*: the theses were right but the
  *construction* underperformed cap-weighting → the lesson points to execution — better
  entry timing / technical analysis, and **reducing proxy reliance** (the LIT-for-CATL and
  EUAD engine substitutions are prime suspects), not to abandoning the ideas.
- **Failure via the return guardrail**: the hedge cost too much for the protection it gave
  in a calm tape → re-examine inverse-leg sizing (the 25% weight) and whether "pre-paid"
  inverses (DVA, DAL) ever had asymmetry left to give.
- **Failure with mechanisms mostly *rejected***: the ideas were wrong, cleanly → the
  gauntlet's kill criteria need sharpening, and this is the honest, valuable negative
  result the whole ledger exists to produce.
- **Mixed**: report exactly which gate failed and why; no rounding toward either verdict.

**Why 8 pp (guardrail derivation, written ex-ante):** each trio holds ~25% in a
regime-inverse leg expected to lag the theme by ~20–30 pp in a bull market; 0.25 × ~25 pp
≈ 6 pp of expected hedge drag, plus a ~2 pp margin → 8 pp. It is expected-hedge-cost
arithmetic, not a tuned dial.

## 6. Mid-window exit protocol (the fix that makes this a real experiment)

The trios carry live kill-lines; some will likely fire. **Pre-committed, uniform rule:**
if any trio leg is killed by its pre-registered kill-line, acquired for cash, or delisted,
its proceeds sit as **flat cash inside that trio's sleeve** for the remainder of the
window. The pair **stays in all scoring**. Nothing is dropped, substituted, rebalanced, or
redeployed into a new winner (redeployment would be the survivorship machine a critic would
rightly attack). The event and date are logged at the checkpoint.

**The asymmetry is intentional and disclosed:** the benchmark ETFs have no kill-lines and
simply buy-and-hold. That is *by design* — the method being tested *includes* its exit
discipline, so "the method (with disciplined exits) vs buy-and-hold the fund" is the honest
comparison, provided exited cash is never redeployed. Stated here so it can't be called a
hidden thumb on the scale later.

## 7. Honesty clauses committed in advance

1. **The hedge is supposed to drag in a bull** — in a calm up-market the plain fund may win
   on raw return; the trio is judged on pain-adjusted return. Stated so a calm-market fund
   win is neither spun as failure nor hidden.
2. **A calm window cannot confirm the method** — the hedge's whole promise is untestable
   without a stress event; a benign window can only fail to reject.
3. **N≈8, one regime, 12 months = underpowered.** No outcome is statistically conclusive;
   this is one calibration data point.
4. **Paper flatters** — no slippage, borrow cost, liquidity limit, or client behaviour.
5. **Total-return convention is fixed** (dividends reinvested, both arms, computed series of
   record) precisely so the different yields can't distort the guardrail.
6. **All trios included, dogs and all**; benchmark imperfections logged, not optimized away.

## 8. Sign-off, T0, and the enactment contingency

- **Signed and committed 2026-07-05**, in its own pushed commit *before* the control arm
  exists — so the pre-registration is tamper-evident by construction (the standing rule
  from the review). Decisions locked; nothing about the design may now change without a
  logged, dated amendment.
- **The control arm is deferred, not cancelled.** Because the trios were already enacted
  and fill 2026-07-06, they cannot reset — so the study's start is defined by the *control
  arm's* enactment, not the trios':
  - **If the control arm is enacted before the 2026-07-06 open** (recommended): **T0 =
    2026-07-06**, both arms share a clean common start, and the trios' study window matches
    their live fills exactly.
  - **If enactment is deferred past Monday:** **T0 = the control arm's actual fill date.**
    Both arms are then scored on the **computed total-return series (§2) from that common
    T0** — the trios' live ledger keeps running from their Monday fills, but any trio P&L
    *before* T0 sits outside the study window. This keeps the comparison honest (a shared
    starting line) at the cost of discarding the trios' first stretch of live data.
  - The study never proceeds with the two arms measured from *different* start dates.
- **Consequence to accept with the deferral:** every day the control arm waits past Monday
  is a day of trio performance excluded from the study. Enacting before Monday's open is
  the only way to capture the full 12 months on both arms.

---

*Decisions locked 2026-07-05: Electrons → ICLN, Defense → ITA report-only, breadth → hard
gate 6/7. Awaiting operator sign-off to (1) commit this as the binding pre-registration in
its own pushed commit and (2) enact the 9-ETF control arm ($45k) to fill the same
2026-07-06 open as the trios.*
