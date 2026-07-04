# Alert Rules — machine-checkable monitor spec (v1.1, 2026-07-05)

v1.1 incorporates the [fable reliability inspection](2026-07-05-fable-inspection.md)
(between-runs amendment, logged). Rules are grouped by **cadence class** — the daily
runner executes only what its day calls for:

- **[D]** daily — genuinely event-driven, press-released, fire-capable any day
- **[W]** weekly (Mondays) — slow-moving or FP-prone if run daily; WATCH-capable
- **[M]** monthly-pinned — evaluate only in the named window
- **[Q]** calendar-pinned to report dates (+2 days) — the only genuine evaluation days;
  between dates these rules are dormant, not searched
- **[P]** price/data computation — no search; computed from Alpaca feed or issuer data

## A. Price backstops [P] (every run)

Per leg vs avg_entry_price: ≤−30% WATCH · ≤−45% STRESSED · ≤−60% KILL.
Trio weighted book ≤−25% → STRESSED. Correlation collapse (all legs same-direction
>5% in 5 sessions) → freeze-and-attribute, 72h.

## Uranium
- **[M]** Term price: first week of month, Cameco uranium-price page (UxC/TradeTech
  month-end averages) — two consecutive soft prints → WATCH.
- **[D]** `"NexGen" offering OR "bought deal" OR "private placement"` — **KILL only if**
  (discount >10% to prior close AND size >5% of shares outstanding) OR paired with
  milestone slip / going-concern language in the same filing; **any other raise →
  WATCH**. (v1.1 fix: v1.0 dropped the distressed qualifier — false-KILL machine.)
- **[W]** `"Rook I" delay OR schedule OR permit` → WATCH-only.
- **[W]** `uranium producer restart expansion announcement` → dated announcement by a
  top-3 producer closing >10% of deficit → STRESSED. Reference deficit: record the
  figure used at next checkpoint (currently unstored — v1.2 item).

## Electrons
- **[Q]** CATL report dates: KILL = gross margin down >400bp y/y (or <15%) AND
  shipment growth <5% y/y (shipments per SNE/CAIC monthly install data). Deceleration
  short of both → WATCH.
- **[D]** `US EU tariff Chinese batteries exclusion enacted` → enacted structural
  exclusion → STRESSED (proposals → WATCH-note).
- **[D]** `Fluence Energy offering OR raise OR going concern` → dilutive raise → KILL.
- **[M]** LIT holdings CSV (issuer site): CATL weight <0.75× entry-date weight →
  WATCH (proxy decay). Entry baseline: record at first monthly pull.
- **[W]** `Ofgem RIIO allowed returns determination National Grid` → enacted cut to
  allowed equity returns → STRESSED; draft → WATCH.

## Metals
- **[P]** Gold/platinum rule is arithmetic, not search: GLD ≤0.80× entry AND PPLT
  within ±5% of entry → KILL check flag. (v1.1: deleted the `gold price real yields`
  search — commentary magnet.)
- **[D]** `Salobo OR Peñasquito OR Antamina OR Constancia suspension OR strike OR
  "force majeure"` → dated operator announcement → STRESSED (WPM counterparty leg).
- **[Q]** WPM report dates: "toll impairment" = recognized impairment charge OR amended
  precious-metal purchase agreement OR top-3 stream guided down >15% → STRESSED.

## Procurement (inspection: best block, kept)
- **[Q]** XMTR report dates: growth <15% y/y → WATCH; margin compression + guidance cut
  → STRESSED; capital raise → KILL.
- **[M]** FAST monthly sales (6:00am CT, 4th business day): negative growth → WATCH;
  two consecutive negative comps → KILL.
- v1.2 gap (logged): RBA auction-volume rule — inverse currently uncovered by events.

## Agriculture
- **[M]** WASDE per published USDA calendar: >5% grain move + no leg differential
  within 5 sessions → WATCH.
- **[Q]** CTVA report dates (+transcript): pricing concessions attributed to farmer
  distress → STRESSED once, KILL on second consecutive quarter.
- **[D]** `ADM "restatement" 8-K` → **KILL immediate** on a dated company filing of a
  *new* restatement (v1.1: query rephrased; 2024-scandal recirculation is not a firing).
- **[Q]** ADM report dates: crush margin inverted → STRESSED (×2 → KILL). TSN report
  dates: protein demand collapse with feed still high → KILL.

## Housing
- **[M]** Delinquency = ICE Mortgage First Look (~third week, prior month): two months
  rising → WATCH.
- **[Q]** **ESNT earnings dates (~early Feb/May/Aug/Nov): WebFetch the earnings release
  + portfolio supplement from investor.essentgroup.com directly; extract new notices of
  default. Trailing-4Q average: RECORD HERE at first print (currently unset — arms at
  first report). >1.5× → STRESSED; >2× → KILL (the book's true stop-loss).**
- **[W]** `private mortgage insurance defaults claims rising` → WATCH-notes only, never
  fire-capable.
- **[Q]** DHI report dates: incentive-attributed margin erosion → STRESSED (×2 → KILL).
  INVH report dates: occupancy or blended rent growth negative → STRESSED (×2 → KILL).

## GLP-1
- **[D]** `drug pricing legislation distribution fees committee` → clears committee →
  STRESSED; enacted → KILL (MCK).
- **[Q]** LLY report dates: obesity revenue below prior-year comp → STRESSED (×2 → KILL).
- **[D]** `GLP-1 kidney renal outcomes trial results` → fire-capable only on a named
  phase-3/registry readout with quantified caseload effect; weekly-study noise →
  WATCH-note at most. Strengthening readout → WATCH (DVA asymmetry); erosion at scale
  (quantified, named trial) → KILL (DVA).
- v1.2 gap (logged): CCJ Westinghouse guide-down (Uranium block, cross-listed).

## Defense
- **[W]** `European defense budget cut proposal enacted` → one member tables → WATCH;
  two members or enacted reversal → STRESSED/KILL. (v1.1: daily → weekly; daily runs
  harvest austerity rhetoric.)
- **[Q]** HEI report dates: organic parts revenue negative → STRESSED (×2 or dilutive
  raise → KILL). DAL report dates: fuel-shock margin compression unhedged → STRESSED
  (×2 → KILL).
- **[M]** EUAD holdings CSV: non-defense drift materially above entry baseline → WATCH.

## Standing findings [W]
- Space reopen: `space launch insurance IPO OR ground station public listing`.
- AI-DC reopen: `distressed data center REIT OR power arbitrage listing`.

## Output contract (unchanged)
Append dated block to `monitoring/log.md`; STRESSED/KILL flagged loudly with sources;
"no firings" otherwise; commit + push. **The loop never executes an exit** — a kill is
a conscious, logged act by the operator.
