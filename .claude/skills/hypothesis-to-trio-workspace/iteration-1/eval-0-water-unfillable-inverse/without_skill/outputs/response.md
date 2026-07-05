# Municipal water trio — draft for the Thales ledger

- **Drafted:** 2026-07-05 (market closed — Saturday; orders would queue for Monday 2026-07-06 09:30 ET open)
- **Account state checked:** Alpaca paper `PA3AXI8V4TCX`, equity $100,000, no open positions
- **Proposed notional:** $5,000 · no leverage (house convention, matches prior trio entries)
- **Status:** DRAFT — not enacted. Orders specified below; place them only after you accept the amended thesis.

---

## 1. The hypothesis, stress-tested before structuring

Your claim has two parts. They grade very differently, and the ledger should record that
before any position exists.

**Part A — "critically underinvested": TRUE, well-anchored.** EPA's needs surveys put the
20-year drinking-water gap in the hundreds of billions; the mechanism (100-year-old pipe,
lead service lines, PFAS treatment) is physical, not narrative.

**Part B — "will be repriced upward over the next 24 months as federal funding lands":
PARTIALLY BACKWARDS, and this is the part that would have gotten the trade killed
mid-run.** The search-verified record:

- The IIJA/BIL water supplemental (~$55B including $15B for lead service lines) runs
  **FY2022–FY2026**. FY2026 is the *last* BIL year. The federal wave is **cresting, not
  arriving** — practitioners describe BIL lead-service-line funding as "sunsetting" in
  2026, with resources likely to *decrease* in 2027.
- The White House's FY2026 budget proposed a **$2.4–2.46B cut** to the State Revolving
  Funds. Congress held regular appropriations flat at ~$3.04B (P.L. 119-74), and EPA
  announced $7.2B in FY2026 SRF allotments — but "flat under a proposed 80% cut" is not
  a funding tailwind; it is appropriations risk.

**What actually forces repricing inside your 24-month window is not federal money — it is
federal *mandate*:**

- **Lead and Copper Rule Improvements (LCRI):** compliance date **November 1, 2027** —
  inside your window. Baseline inventories and replacement plans are due, and a mandatory
  **10-year replacement of all lead and galvanized service lines** begins, regardless of
  test results and regardless of whether grant money exists. This is a dated, mostly
  unfunded mandate: municipalities must spend.
- **PFAS National Primary Drinking Water Regulation** (final April 2024): treatment capex
  with compliance in the 2029–2031 horizon — planning and engineering dollars start now.

**Amended thesis for pre-registration:** *Municipal water capex is compelled upward
through 2027–2028 by dated regulatory mandates (LCRI Nov-2027, PFAS), with the tail of
BIL money as an accelerant. Suppliers of mandated hardware reprice as orders convert.
Federal appropriations are a **risk to the thesis, not its driver** — a rescission is a
kill trigger, not the catalyst.*

If you insist on the original framing ("repricing because new federal money lands"), the
honest recommendation is **do not structure it** — the funding calendar contradicts it.

---

## 2. Seat selection (Engine / Tollbooth / Regime-inverse)

Prices are live Alpaca snapshots as of 2026-07-05 (Friday 2026-07-03 close prints).

### Engine — Mueller Water Products (MWA) @ $24.96 — 42.5% / $2,125 (~85 sh)

The purest listed play on the mechanism: fire hydrants, iron gate valves, and **brass
service-line products** — the exact hardware the LCRI replacement wave consumes. ~90%+
municipal water end-market, so the thesis seat is authentic (K2). Mid-cap (~$3.9B),
liquid, profitable, investment-grade-ish balance sheet (K1/K3/K4 pass on inspection —
verify leverage in latest 10-Q before enactment).

- *Considered and passed over for the seat:* **XYL** ($118.14) — excellent company but a
  diversified global water-tech platform; the muni-mandate signal is diluted (~weaker K2
  authenticity for *this* thesis). **TTEK** ($29.91) — heavy direct federal-contract
  exposure makes it a bet *on* appropriations, the exact risk we just demoted.

### Tollbooth — Core & Main (CNM) @ $44.93 — 32.5% / $1,625 (~36 sh)

The largest US waterworks distributor. Whoever wins the manufacturing share fight — 
Mueller, McWane, Ford Meter Box, any meter vendor — the pipe, valve, meter, and service
line still ships through Core & Main's ~370 branches at a distribution margin. That is
the definition of the tollbooth seat: it collects on sector volume, not on picking the
winner.

- *Considered and passed over:* **BMI** ($146.00, Badger Meter) — good business, but
  meters are a *product* bet, not a toll on all flows. **AWK** ($136.89) — flagged on
  **K2 authenticity**: SRF/BIL dollars flow to *municipal* systems, not investor-owned
  rate base; AWK's actual thesis is muni-system acquisition, a different (and partly
  opposite) mechanism — see below.
- *Redundancy note (K5):* MWA and CNM are both muni-waterworks names and will correlate.
  They sit on different margin pools (manufacturer vs distributor) and different
  narratives (MWA = product cycle, CNM = volume/pricing), so expected correlation is
  high-but-tolerable (~0.7–0.8). Standing kill: trailing 90-day correlation > 0.9 →
  collapse the two seats into one and rebuild.

### Regime-inverse — **the seat cannot be filled honestly. Declare it, don't fake it.**

The failure regime is: FY2027 appropriations gut the SRFs / BIL tail is impounded, muni
budgets squeeze, LCRI enforcement slips, capex is deferred. What *profits* from that?
Every candidate fails on inspection:

| Candidate | Why it fails the seat |
| --- | --- |
| XLU ($45.75) | Same rate-sensitivity, same direction; correlated, not inverse. |
| MUB ($107.50) | Muni fiscal stress is *the failure mode itself* — muni credit gets hurt with the thesis, not by it. |
| TLT / duration | "Austerity → duration rally" is a macro guess, not a scenario-level inverse of *this* mechanism. |
| Short FIW ($108.99) | Pure negation of the book — redundant, and FIW is thin (238 shares traded Friday). |
| WTRG ($39.37) / AWK | The cleverest candidate: if public funding fails, distressed munis *sell systems* to investor-owned utilities, so privatization accelerates on thesis failure. But the mechanism is multi-year and both names still carry the same rate/sector beta week to week — it inverts on paper, not in the ledger. Rejected. |

**Resolution:** park the inverse seat's 25% in **SGOV ($100.43) — $1,250 (~12 sh)** and
record it in the entry as **declared ballast, not inversion**. The risk work that the
inverse seat normally does is transferred, explicitly, to the dated kill criteria below.
(Optional overlay if you want true convexity: the account has options level 3 — a small
Jan-2027 XYL put spread would be the liquid way to buy the failure scenario. XYL options
are the only liquid chain in the sector; FIW/MWA chains are too thin. Left out of the
base structure to keep the trio clean.)

This is the third-best outcome. The best would be a real inverse; the second-best is not
running the trio; faking an inverse with a correlated utility would be the worst.

---

## 3. Kill criteria (pre-registered — amend between runs, never mid-run)

1. **Funding kill (dated):** FY2027 appropriations enact an SRF cut ≥ 50% vs the FY2026
   $3.04B baseline, or BIL water funds are impounded/rescinded without judicial or
   congressional restoration within 90 days → thesis review; Engine trimmed to half.
2. **Mandate kill (dated, primary):** the **Nov 1, 2027 LCRI compliance date** is
   delayed > 12 months by rulemaking or court order → full kill. This is the thesis's
   load-bearing clock.
3. **Mechanism kill:** MWA reports two consecutive quarters of YoY declines in water
   infrastructure orders/backlog, or CNM reports two consecutive quarters of negative
   volume growth in municipal end-markets → the mandate is not converting to orders; kill.
4. **Standard kills:** any leg round-trips −75% (K3); any leg forced into a distressed
   dilutive raise (K4).
5. **Redundancy kill:** MWA/CNM 90-day correlation > 0.9 (K5) → restructure to one seat.

## 4. Grade dates

- **First checkpoint:** MWA fiscal Q3 earnings (early August 2026) + CNM Q2 earnings
  (early September 2026). Grade order/backlog *mechanism*, not the P&L line.
- **Mid-grade (hard clock):** **2027-11-01** — LCRI compliance date. Did the mandate
  hold? Did replacement plans convert to awarded work?
- **Final grade:** **2028-07-05** — the 24-month window closes. Grade the amended thesis
  as written, including the explicit prediction that mandates, not appropriations, drive
  the repricing.

---

## 5. Orders (ready to queue — NOT yet placed)

```bash
source ~/.config/alpaca/paper-trading.env
AUTH=(-H "APCA-API-KEY-ID: $ALPACA_API_KEY_ID" -H "APCA-API-SECRET-KEY: $ALPACA_API_SECRET_KEY")
B="https://paper-api.alpaca.markets/v2/orders"

# Engine — Mueller Water Products, 42.5%
curl -s "${AUTH[@]}" -X POST "$B" -d '{"symbol":"MWA","notional":"2125","side":"buy","type":"market","time_in_force":"day"}'
# Tollbooth — Core & Main, 32.5%
curl -s "${AUTH[@]}" -X POST "$B" -d '{"symbol":"CNM","notional":"1625","side":"buy","type":"market","time_in_force":"day"}'
# Inverse seat (declared ballast) — SGOV, 25%
curl -s "${AUTH[@]}" -X POST "$B" -d '{"symbol":"SGOV","notional":"1250","side":"buy","type":"market","time_in_force":"day"}'
```

Market opens Monday 2026-07-06 09:30 ET. After fills, copy this entry to
`/Users/Adam/thales/ledger/entries/2026-07-06-water-trio.md`, add the order IDs to the
seat table, and log the ballast declaration in the inversion-claim section.

## 6. Summary table

| Seat | Asset | Symbol | Last | Weight | Notional | Seat verdict |
| --- | --- | --- | --- | --- | --- | --- |
| Engine | Mueller Water Products | MWA | $24.96 | 42.5% | $2,125 | Filled — pure-play on mandated hardware |
| Tollbooth | Core & Main | CNM | $44.93 | 32.5% | $1,625 | Filled — distribution toll on all sector volume |
| Regime-inverse | *(unfillable — declared ballast)* | SGOV | $100.43 | 25.0% | $1,250 | **Not filled**; risk transferred to dated kills |

**Bottom line:** the underinvestment half of your hypothesis is solid; the "federal
funding lands" half is backwards — BIL water money sunsets in FY2026 and the FY2026
budget fight nearly cut the SRFs by $2.4B. The tradeable version is the **LCRI Nov-2027
unfunded mandate**, expressed through MWA (engine) and CNM (tollbooth), with the inverse
seat honestly declared unfillable and held as SGOV ballast under dated kill criteria.

Sources:
- [FY2026 Appropriations for EPA Water Infrastructure Programs (CRS IF13177)](https://www.congress.gov/crs-product/IF13177)
- [White House proposes $2.4B reduction for 2026 State Revolving Fund programs (WaterWorld)](https://www.waterworld.com/drinking-water-treatment/infrastructure-funding/news/55287774/white-house-proposes-24b-reduction-for-2026-state-revolving-fund-programs)
- [Drinking Water State Revolving Fund (EPA)](https://www.epa.gov/dwsrf)
- [EPA Issues Final Lead and Copper Rule Improvements (Beveridge & Diamond)](https://www.bdlaw.com/publications/epa-issues-final-lead-and-copper-rule-improvements-with-far-reaching-lead-pipe-replacement-mandates/)
- [What does LCRI require in 2025 and 2026? (BlueConduit)](https://blueconduit.com/post/what-does-lcri-require-in-2025-and-2026/)
- [Prioritizing Lead & Copper Rule compliance before 2027 (Arcadis)](https://www.arcadis.com/en-us/insights/blog/united-states/erica-walker/2024/insights-on-lead-and-copper-compliance-program)

*Paper trading only — a calibration exercise, not financial advice.*
