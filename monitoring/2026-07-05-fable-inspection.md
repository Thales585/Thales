# Alert reliability inspection — fable-model agent, 2026-07-05

*Independent inspection of monitoring/alert-rules.md v1.0, commissioned per the
standing invitation to attack the kill criteria hardest of all. Verdicts incorporated
into v1.1. Preserved verbatim below.*

## Per-sector grade table (1–5, 5 best)

| Sector | Detect | Ambig | FP risk | Lag | Worst rule in block |
|---|---|---|---|---|---|
| Uranium | 4 | 2 | 2 | 3 | NXE "dilutive raise announced → KILL" — fires on routine developer financing |
| Electrons | 4 | 2 | 2 | 3 | CATL "margin collapse + volume stall same print" — zero numeric thresholds; volume figure comes from SNE/CAIC installs, not the earnings print |
| Metals | 2 | 2 | 2 | 2 | Both rules. Stream renegotiations are buried in filings; `gold price real yields` is a commentary magnet for a condition that is pure price arithmetic |
| Procurement | 5 | 4 | 3 | 3 | None fatal. Best block in the file: numeric thresholds, press-released sources |
| Agriculture | 4 | 2 | 2 | 2 | CTVA "attributes concessions to farmer distress" — call-transcript exegesis, not a searchable event |
| Housing | 2 | 3 | 3 | 1 | ESNT default notices — the book's self-declared "true stop-loss" has the worst detection instrument in the file |
| GLP-1 | 4 | 2 | 2 | 3 | "Renal data strengthening / caseload erosion at scale" — a new GLP-1 kidney study appears weekly; "at scale" is pure judgment |
| Defense | 3 | 2 | 2 | 2 | "One member tables a cut" — diffuse across 27 national budget processes, mostly non-English sources, drowned in austerity op-eds |

**Systemic findings:** Ambiguity — 6/8 sectors quote doctrine prose instead of
mechanically decidable numbers. Lag — ~14/23 rules gated on quarterly/monthly releases
but specified as open-ended daily searches: 60–89 days of noise per genuine evaluation.

## Three weakest rules (rewrites adopted in v1.1)

1. **Housing/ESNT** — calendar-pin to earnings; WebFetch the investor-relations
   supplement directly; store the trailing-4Q new-notices average as a number in the
   rules file so 1.5×/2× is arithmetic. Weekly tripwire query is WATCH-only.
2. **Metals/WPM** — split: daily event leg naming actual counterparty mines
   (Salobo/Peñasquito/Antamina/Constancia + force-majeure terms); quarterly MD&A leg
   with "toll impairment" defined = impairment charge OR amended stream OR top-3
   stream guided down >15%.
3. **Uranium/NXE** — restore the distressed qualifier the v1.0 rule dropped: KILL only
   if (discount >10% AND size >5% of shares out) OR raise paired with milestone
   slip/going-concern; otherwise WATCH. As written it was a false-KILL machine, and
   kills are one-way doors.

## Cadence verdicts (adopted)

- Delete `gold price real yields` search — pure price arithmetic; compute from feed.
- Calendar-pin ~11 earnings-gated rules to report dates (+2 days).
- Monthly pins: uranium term price (Cameco UxC/TradeTech month-end page, first week);
  FAST monthly sales (6:00am CT, 4th business day); WASDE (published USDA calendar);
  delinquency = ICE First Look (~third week, prior month).
- EU defense budget rule → weekly (daily harvests austerity rhetoric → FP inflation).
- Keep genuinely daily: raises (NXE/FLNC/HEI), ADM new restatement, tariff enactment,
  legislation committee action, counterparty mine failures, renal outcome readouts.

## Missing alerts (adopted)

1. **ETF composition drift** (LIT CATL-weight, EUAD defense purity) — not a search; a
   monthly issuer-CSV holdings pull vs entry baseline; CATL weight <0.75× entry → WATCH.
2. **NGG/Ofgem** — RIIO determinations calendar; STRESSED on enacted allowed-return
   cut, WATCH on draft.

Gaps logged for v1.2 (beyond inspection budget): RBA auction-volumes rule, CCJ
Westinghouse guide-down, ADM crush-margin inversion. ADM query FP fix adopted:
require a dated company 8-K of a *new* restatement (`ADM "restatement" 8-K`).

Sources cited by inspector: Cameco uranium price page, UxC, TradeTech, Fastenal
investor news releases (May 2026 sales release verified).
