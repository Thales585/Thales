# Audit — `hypothesis-to-trio` skill (v1.0)

**Auditor:** Claude (Opus 4.8) · **Date:** 2026-07-05 · **Verdict:** ship, with two
follow-ups logged for v1.1. Paper trading only; a calibration exercise, not financial
advice.

---

## 1. Scope and method

Audited the skill at `~/thales/.claude/skills/hypothesis-to-trio/` against four axes:
purpose fit, protocol consistency with the Thales method, safety/guardrails, and
empirical behaviour. Empirical evidence comes from four test runs on the **fable** model
(two hypotheses × with-skill/baseline), graded against pre-registered assertions written
*before* any output was seen — the same anti-goalpost discipline the ledger uses.
Artifacts: `../hypothesis-to-trio-workspace/iteration-1/`.

## 2. What the skill is supposed to do

Input a hypothesis; output a gauntlet-ready three-seat slate (engine / tollbooth /
regime-inverse). When a seat won't fill, walk a proxy ladder — listed proxy → synthetic
`short(N)` → declare unfillable. Critically, it is a **mapping** tool, not a **judging**
tool: it must never declare a trio surviving/valid (that is the gauntlet's job) and must
never quote prices from memory.

## 3. Empirical results

| Test (trap it probes) | With skill | Baseline |
|---|---|---|
| Eval 0 — Water: inverse seat historically unfillable | **6/6** | 4/6 |
| Eval 1 — AI bust: engine itself is the unfillable seat | **5/5** | 1/5 |
| **Total** | **11/11 (100%)** | **5/11 (45%)** |

Mean cost with-skill: ~34k tokens / ~159s. Baseline: ~35k / ~256s (baselines ran
*longer* — without the seat frame they wandered into live-quote pulls and options-chain
analysis).

**Behavioural highlights (with skill):**
- *Eval 1* recognised the bust as the **mirror** of the ledger's AI-DC finding, moved
  the unfillable seat to the engine, built it from `short(SMCI)`/`short(VRT)`, and
  proactively **excluded `short(NVDA)`** so the long-NVDA inverse wouldn't be a K5
  mirror at correlation −1. This is the skill's hardest intended manoeuvre, executed
  unprompted.
- *Eval 0* honoured the prior "Water inverse unfillable" finding, surfaced PRMB as the
  one genuine decay-driven feeder, and backed it with rung-2 `short(TTEK)` — all three
  synthetic-seat costs logged.
- Zero prices quoted from memory in either with-skill run; all tickers Alpaca-verified.

## 4. Findings

### F1 — Baseline contamination on Eval 0 (evidence limitation, not a skill defect)
The Eval-0 baseline scored 4/6 because the subagent **read the house method out of the
repo** and reproduced it unprompted. "No skill" was therefore not a clean control on the
water case. Consequence: the skill's measured lift is understated on Eval 0 and the
*honest* signal is Eval 1 (1/5 baseline), where no in-repo anchor existed and the model
defaulted to a generic options plan. **Action:** future eval baselines for repo-resident
skills should run in a scratch dir with no ledger access. Logged, not blocking.

### F2 — Two assertions are strong discriminators (positive finding)
"Gauntlet hand-off / no survivor claim" and "uninsured quadrant named" failed for
*both* baselines and passed for *both* with-skill runs. These are exactly the
method-specific behaviours the skill injects — good evidence it is teaching the
discipline (mapping ≠ judging; name the quadrant that kills all three) rather than
generic competence. Keep them in the regression set.

### F3 — Protocol consistency: clean
The skill's seat definitions, the flow-vs-stock tollbooth test, the "dodge ≠ feed"
inverse rule, and the proxy ladder all match the live gauntlet method and the exit
doctrine verbatim. The `short(N)` guardrails (never short the engine; hedge-not-feeder
breaks non-cannibalization; carry decay) are correct and were reproduced faithfully by
both with-skill runs. No drift from the playbook.

### F4 — Safety: within guardrails
The skill is read-only by construction: it verifies tradability via the read-only assets
API and hands off; it places no orders. It correctly frames shorting as paper-only and
notes unbounded live loss. It cannot itself enact anything — enactment stays with the
operator via the separate `alpaca-paper-trade` skill. No surprise-of-intent issues.

### F5 — Minor: price-hygiene rule is stricter than the assertion caught
The Eval-0 baseline quoted 16 live prices (sourced, not memory) — permitted by the
assertion but contrary to the skill's "seat mapping needs no prices" principle. The
with-skill runs correctly quoted none. Not a defect, but v1.1 could state explicitly
that *even live-sourced* prices are out of scope for the mapping step, to keep the
hand-off clean.

## 5. Recommendations (v1.1 backlog, none blocking)

1. **Add a third test: a natively-fillable, bullish sector** (e.g. a clean
   engine/tollbooth/inverse with no proxy needed) to confirm the skill doesn't
   *over-reach* for `short(N)` when a seat fills natively — the current two tests both
   probe unfillable seats, so the skill's restraint is unmeasured.
2. **State the price-hygiene rule at hand-off** (F5).
3. **Run description-triggering optimisation** — the current description is untested for
   over/under-triggering against near-miss prompts (e.g. "should I buy water stocks?"
   which should *not* trigger a full trio build).
4. Re-run Eval-0 baseline in an isolated dir to get an uncontaminated delta (F1).

## 6. Verdict

**Ship v1.0.** The skill does what it claims, stays inside its guardrails, is faithful
to the method, and shows a clear, mechanism-level lift on the case that matters most
(synthetic-seat construction, 5/5 vs 1/5). The failures it prevents are real and were
observed live in the baselines — an off-method options plan, and a mapping step that
silently did the gauntlet's judging job. Follow-ups are enhancements, not fixes.

*Reviewers are invited to attack the proxy ladder hardest of all — the `short(N)` rung
is where this skill most risks manufacturing a seat that shouldn't exist.*
