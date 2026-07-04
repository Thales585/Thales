# Monitoring log — daily alert loop output

Newest entries at top. Format per run: date · price-backstop summary · event-trigger
firings (with sources) or "no firings" · actions taken. A kill is never executed by
the loop — it flags; the operator acts.

---

## 2026-07-05 — loop initialized (pre-fill baseline)

- Book: 25 orders `accepted`, awaiting 2026-07-06 09:30 ET open. No positions held yet;
  price backstops arm automatically once avg_entry_price exists.
- Event scan: not yet run (first scheduled run after first fill day).
- Alert rules v1.0 committed; fable reliability inspection in progress — rules may be
  amended to v1.1 on its verdicts (between-runs amendment, permitted).
