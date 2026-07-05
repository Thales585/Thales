# Control arm — sector-fund benchmark (research study)

- **Enacted:** 2026-07-05 ~12:15 UTC · $45,000 ($5,000 × 9) · no leverage · fills expected
  2026-07-06 09:30 ET, the **same open as the trios** → **study T0 = 2026-07-06** (clean
  common start; §8 of the pre-registration).
- **Purpose:** the live parallel benchmark for the binding study in
  [research/2026-07-05-preregistration.md](../../research/2026-07-05-preregistration.md).
  This is a *control*, not a trio — it takes no thesis and is never graded on mechanism.
- **Series of record:** a computed total-return series (dividends reinvested, daily-close
  drawdowns) per §2 — these live paper fills are the desk-facing exhibit, reconciled at T0.

## Positions

| Benchmark for | ETF | Notional | Scored? | Order ID |
| --- | --- | --- | --- | --- |
| Uranium | URA | $5,000 | yes | `da0836b0-b8df-4b13-b39f-068ad55bb1c2` |
| Electrons | ICLN | $5,000 | yes | `1406e1a9-4905-42b2-86c1-cdf8a0062da7` |
| Metals | GLD | $5,000 | yes | `5709eb2e-e1ec-447d-a092-2486f3c8f395` |
| Procurement | XLI | $5,000 | yes | `84ae0624-1af3-4842-8bd6-d742ff3dea34` |
| Agriculture | MOO | $5,000 | yes | `9a5aec9a-a85f-4ee0-9c8d-607563cb37eb` |
| Housing | XHB | $5,000 | yes | `3aa1508d-8fe6-45ea-ba5d-9c9ee2151d2c` |
| GLP-1 | XLV | $5,000 | yes | `1705e9a2-b053-439b-a7e3-b2e0433fe7dd` |
| Defense | ITA | $5,000 | **report-only** | `434ccf96-198e-4b95-b016-9d425f1a0d48` |
| whole-market anchor | SPY | $5,000 | anchor | `a50ccf06-fb3c-43ca-a84a-6d024c13f3a5` |

**Scored pairs: N = 7** (Defense report-only, SPY is the anchor gate).

## Notes

- **GLD overlap:** GLD is both this arm's Metals benchmark *and* the Metals-trio engine
  leg ($2,125). On Alpaca the positions aggregate into one GLD holding; the scored study
  uses the computed series, so the overlap is a bookkeeping detail, not a measurement one.
- **No kill-lines:** the control arm buys-and-holds for the full window. The trios' exit
  discipline is asymmetric by design (§6 of the pre-registration) — that asymmetry *is*
  part of what the study tests.

## Fill log

- 2026-07-05 — all 9 orders `accepted`, awaiting Monday open. Fills TBD.
