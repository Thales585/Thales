# Alert Rules — machine-checkable daily monitor spec (v1.0, 2026-07-05)

Executed daily by the monitoring loop. Two check classes:

**A. Price backstops (computed from Alpaca positions API, no judgment):**
For every leg: unrealized P&L% from avg_entry_price.
- ≤ −30% → WATCH · ≤ −45% → STRESSED · ≤ −60% → KILL
- Trio-level: weighted book ≤ −25% → STRESSED review.
- Correlation-collapse flag: all 24 legs same-direction move >5% in 5 sessions → freeze-and-attribute.

**B. Event triggers (daily web search, one query set per sector).**
Each rule: search query → firing condition → tier. A rule FIRES only on a dated,
sourced report matching the condition — rumor/opinion pieces log as WATCH-notes only.

## Uranium
- Q: `uranium term price monthly <current month>` → two consecutive soft prints → WATCH
- Q: `NexGen Rook I delay OR financing OR offering` → dilutive raise announced → KILL; milestone slip → WATCH
- Q: `uranium producer restart expansion announcement` → top-3 producer closing >10% of deficit → STRESSED

## Electrons
- Q: `CATL quarterly results volume margin` → margin collapse + volume stall same print → KILL; deceleration → WATCH
- Q: `US EU tariff Chinese batteries exclusion` → structural exclusion enacted → STRESSED
- Q: `Fluence Energy offering OR raise OR going concern` → dilutive raise → KILL

## Metals
- Q: `Wheaton stream renegotiation OR counterparty mine failure` → toll impairment → STRESSED
- Q: `gold price real yields` → gold −20% from entry AND platinum flat → KILL check (needs price confirm from feed)

## Procurement
- Q: `Xometry earnings guidance` → growth <15% y/y → WATCH; margin compression + cut → STRESSED; raise → KILL
- Q: `Fastenal daily sales monthly` → negative growth → WATCH; two negative comps → KILL

## Agriculture
- Q: `WASDE report surprise grain prices` → >5% grain move + no leg differential → WATCH
- Q: `Corteva pricing farmer distress concessions` → first attribution → STRESSED; second consecutive quarter → KILL
- Q: `ADM restatement OR SEC OR accounting` → any new restatement → **KILL immediate**
- Q: `Tyson feed costs protein margins` → demand collapse w/ high feed → KILL

## Housing
- Q: `mortgage delinquency data monthly` → two months rising → WATCH
- Q: `Essent default notices quarterly results` → >1.5× trailing → STRESSED; >2× → **KILL (true stop-loss)**
- Q: `DR Horton incentives gross margin` → erosion attributed to incentives → STRESSED (×2 quarters → KILL)
- Q: `Invitation Homes occupancy rent growth` → negative once → STRESSED; twice → KILL

## GLP-1
- Q: `drug pricing legislation distribution fees committee` → clears committee → STRESSED; passes → KILL (MCK)
- Q: `Lilly obesity revenue scripts` → below prior-year comp → STRESSED (×2 → KILL)
- Q: `GLP-1 kidney renal outcomes data` → strengthening → WATCH (DVA asymmetry); caseload erosion at scale → KILL (DVA)

## Defense
- Q: `European defense budget cut proposal` → one member tables cut → WATCH; two members or enacted reversal → STRESSED/KILL
- Q: `HEICO organic revenue results` → negative once → STRESSED; twice or dilutive raise → KILL
- Q: `jet fuel price airline margins` → shock compressing DAL margins → STRESSED (×2 quarters → KILL)

## Standing findings (weekly cadence sufficient)
- Space reopen: `space launch insurance IPO OR ground station public listing` → standalone toll lists → reopen sector run
- AI-DC reopen: `distressed data center REIT OR power arbitrage listing` → bust-monetizer lists → reopen sector run

## Output contract for the daily run
Append one dated block to `monitoring/log.md`: prices summary, any tier firings with
source URLs, "no firings" otherwise. STRESSED or KILL → flag loudly at top of response.
Never execute an exit automatically — a kill is a conscious, logged act by the operator.
