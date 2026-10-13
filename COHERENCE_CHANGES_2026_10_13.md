# Coherence corrections, 13 October 2026
The existing family v4 is updated in place. Original regressions and sample definitions are retained. Added deterministic price-screen and ten-year ownership tables; no depreciation forecast is introduced.

## persona
Name and print the fixed payment-rate assumption.
```diff
--- before review
+++ after review
@@ -5,6 +5,7 @@
               cpf_refund=350_000,     # assumed: CPF used for the flat (plus accrued interest), refunded to their CPF accounts on sale
               sell_costs=20_000,      # assumed: agent, legal and moving costs
               age=38, want_sqft=1050) # about 1,050 sqft (typical 3-bedroom size); both Singapore citizens, flat past its minimum occupation period
+PAYMENT_RATE = 0.016  # Fixed route-comparison assumption, separate from monthly SORA illustrations.
 TENURE = min(30, 65 - PERSON['age'])
 def budget_for(income, hdb_value, loan_left=PERSON['hdb_loan_left']):
     net = hdb_value - loan_left - PERSON['sell_costs']; cpf = min(PERSON['cpf_refund'], net); cash = net - cpf
@@ -43,4 +44,6 @@
 MRTPREM_TITLE = 'Family-size resales within 5 minutes of MRT sell for {near:+.0f}% more per sqft than those over 15 minutes away'
 print(f"Net proceeds {sgm(NET_PROCEEDS)} (cash {sgm(NET_PROCEEDS - PERSON['cpf_refund'])}, CPF {sgm(PERSON['cpf_refund'])}). Budget {sgm(BUDGET)}, limited by {BINDING}: "
       f"their funds alone would allow {sgm(CASH_CAP)}, the loan alone {sgm(LOAN_CAP)}. "
-      f"ABSD if they buy before selling: {sgd(0.2 * BUDGET)} (refund subject to IRAS conditions).")+      f"ABSD if they buy before selling: {sgd(0.2 * BUDGET)} (refund subject to IRAS conditions).")
+print('Fixed option payment assumption (%):',100*PAYMENT_RATE)
+print('December 2025 embedded SORA + assumed 0.30-point spread (%):',SORA_3M['2025-12']+0.30)

```

## sec2b
Distinguish the fixed payment assumption from the monthly SORA-plus-spread illustration.
```diff
--- before review
+++ after review
@@ -2,3 +2,5 @@
 The chart now shows **2023–2025**. It prices the same hypothetical loan at each month’s SORA plus an assumed **0.30 percentage-point** bank spread. It does not track an actual mortgage or a particular bank offer.
 
 In 2025, SORA fell about **59%** and the illustrated monthly payment fell about **19%**. The assessed payment stayed at the **4% floor** because the assumed loan rate stayed below it. Banks use the higher of 4% and the thereafter interest rate (the highest applicable rate excluding introductory or promotional rates). Here we use SORA plus the assumed spread as a simple thereafter-rate proxy. This distinction also matters in 2023, when the illustrated rate briefly exceeded 4%.
+
+**Why the options use 1.6%.** The payment tables and recommendation cards use a separate, fixed 1.6% planning scenario so routes can be compared at one rate. December 2025’s embedded SORA plus the assumed spread is about 1.49%, as printed below. The scenario is not a quoted bank offer or a rounded value of that December rate.

```

## sec3
Separate near-ceiling districts consistently and explain why the standard-home map differs from actual comparable sales.
```diff
--- before review
+++ after review
@@ -2,7 +2,9 @@
 The map prices the same home in every district: a 1,050 sqft resale with 91 years of lease left, against the S\$2.18M budget.
 - **Most of the island is in reach:** 17 of 27 districts.
 - **The east is comfortable:** District 18 (Tampines/Pasir Ris, S\$1.80M) and the north-east towns (S\$1.87M). Bedok and Geylang/Eunos are about S\$1.94M.
-- **Just over:** Katong (S\$2.22M).
-- **Above this model budget:** Raffles Place, Tanjong Pagar, Queenstown, Sentosa/Telok Blangah, City Hall, Bugis, Orchard/River Valley, Bukit Timah/Holland and Newton/Novena. The shading is smoothed between district centres, so read the circled values, not the exact line.
+- **Just over in this model:** Sentosa/Telok Blangah (S\$2.20M, +0.6%), Tanjong Pagar (S\$2.21M, +1.3%) and Katong/Marine Parade (S\$2.22M, +1.8%). Small differences around the ceiling should not be treated as precise affordability cut-offs.
+- **Above this model budget:** Raffles Place, Queenstown, City Hall, Bugis, Orchard/River Valley, Bukit Timah/Holland and Newton/Novena. The shading is smoothed between district centres, so read the circled values, not the exact line.
 
 Place names on the map are readable labels for broad postal districts. They are not exact neighbourhood boundaries. “North-east towns” covers Serangoon, Hougang, Sengkang and Punggol. The coloured surface is an illustration between district estimates, not a street-level valuation.
+
+**A first screen, then a check against sales.** These are district-level predictions for one standard home, without MRT walking time. Step 5 checks particular groups of comparable sales: Geylang/Eunos is about S\$1.94M in the model but S\$2.40M in route G’s observed sample. Project mix, MRT access and unrecorded unit features can differ. We cannot assign the discrepancy to MRT alone. Use observed comparables and available listings to check the budget.

```

## sec4d
Choose one headline and give a reading guide for all new-sale estimates rather than presenting them as equivalent premiums.
```diff
--- before review
+++ after review
@@ -1,3 +1,5 @@
-**Is a brand-new launch worth its premium?** New launches sell 55% above resales per sqft. Matched to resales in the same district, size band, floor band and quarter (6,235 of 9,730 new units matched), the gap is still **+42%**. That's a conditional association, not the effect of newness: matched homes can still differ in project quality, and lease and newness can't be separated. New launches have 92–99 years left and no resale has more than 94. In the only 3 projects with both kinds of sale, the gap is +6%, with too few units to decide.
+**Is a brand-new launch worth its premium?** In the 2025 99-year sample, new launches have a raw geometric-mean price-per-sqft gap of 55% above resales. Matched to resales in the same district, size band, floor band and quarter (6,235 of 9,730 new units matched), the gap is still **+42%**. That's a conditional association, not the effect of newness: matched homes can still differ in project quality, and lease and newness can't be separated. New launches have 92–99 years left and no resale has more than 94. In the only 3 projects with both kinds of sale, the gap is +6%, with too few units to decide.
 
 **How to read the four rows:** they are different comparisons, not a sequence that isolates the causes of the premium. The raw gap has no uncertainty interval shown. Matching still leaves unrecorded differences; adding lease requires extrapolation; the same-project comparison has little overlap.
+
+**One headline, several questions.** Use the **42% matched gap** as the main 2025 comparison. The 55% raw gap describes the whole 99-year new/resale sample before matching; the 15% estimate adds lease controls and requires extrapolation; the 6% same-project estimate has very little overlap. The 26% coefficient in Appendix A uses the broader hedonic model, while Step 8’s annual matched gaps omit floor bands. None measures a pure effect of buying new. Appendix C puts the estimates, intervals and comparison types in one reference table.

```

## sec5
Reconcile routes E, F and G with their model prices and state which prices govern affordability.
```diff
--- before review
+++ after review
@@ -6,4 +6,6 @@
 - **Not enough evidence:** D (Bedok, older lease) has only 2 similar sales, so it's shown for completeness only.
 - **The catch with B and C:** their similar sales are a median 22 and 11 minutes' estimated walk from the MRT. F is about 12 minutes, and E and G about 3. B's 21 comparables split between Pasir Ris (11) and Tampines (10); town mix and walking distance both matter. The MRT association in Step 3b is not a causal price adjustment.
 
+**Why the map and shortlist differ.** Route G’s S\$2.40M observed median is above its S\$1.94M model prediction; F is S\$1.91M versus S\$1.80M, and E is S\$2.36M versus S\$2.18M. These are different quantities, not interchangeable prices. The observed medians determine the route’s upfront costs and budget status. Their discrepancies are a reason to inspect actual projects rather than assume a model-priced home is available. The comparison table below prints both.
+
 **The district average hides different choices.** Within B, 11 Pasir Ris sales had a median S\$1.54M; 10 Tampines sales had a median S\$1.67M. Within C, the 9 Serangoon sales had a median S\$2.21M (just over budget), versus about S\$1.62–1.73M in Hougang, Sengkang and Punggol. For E, Marine Parade alone had a S\$2.70M median. Appendix C separates the towns; the route medians should not be read as prices available everywhere in the district.
```

## options
Use the named fixed payment-rate assumption; numerical payments do not change.
```diff
--- before review
+++ after review
@@ -6,7 +6,7 @@
     comp_price = c_.price.median() if len(c_) else p
     rows.append({'route': code_, 'option': name, 'district': dist, 'sqft': sqft, 'lease left': left if left else 'freehold', 'district-centre km to CBD': round(km_to_cbd(dist), 1),
                  'model price': p, 'real median': c_.price.median(), 'real sales': len(c_), 'cash + CPF needed': 0.25 * comp_price + bsd(comp_price),
-                 'monthly @1.6%': payment(LTV['first loan'] * comp_price, 0.016, TENURE), 'fits budget': (c_.price.median() if len(c_) else p) <= BUDGET,
+                 'monthly @1.6%': payment(LTV['first loan'] * comp_price, PAYMENT_RATE, TENURE), 'fits budget': (c_.price.median() if len(c_) else p) <= BUDGET,
                  'walk to MRT (min)': round(c_.walk.median(), 1) if HAS_MRT and len(c_) else np.nan})
 opt = pd.DataFrame(rows).set_index('route')
 # A present-day sensitivity, not 2026 project transactions: shift 2025 comparables by the

```

## price-screen-check
Print the specific model/comparable discrepancies behind the wording corrections.
```diff
--- before review
+++ after review
@@ -0,0 +1,5 @@
+# Print both screening predictions and the observed medians used for affordability.
+SCREEN_CHECK=opt.loc[['E','F','G'],['option','model price','real median','real sales','fits budget']].copy()
+SCREEN_CHECK['observed vs model %']=(SCREEN_CHECK['real median']/SCREEN_CHECK['model price']-1)*100
+print('Model screen versus observed comparable sales; MRT walk is omitted from the screening model.')
+display(SCREEN_CHECK.round(2))

```

## sec7
Explain two stages of reproducibility and clarify that the 2024 supplied input is already reconstructed.
```diff
--- before review
+++ after review
@@ -1,4 +1,7 @@
 ## Step 7 · Five years of evidence (2020–2025)
 Steps 1–6 use 2025 sales. We also have the same kind of file for **August 2020 to December 2024**, so we can check whether the 2025 patterns hold over time and follow the same projects as they age. The same five-year table also drives Step 8.
 - **Cleaning:** in the 2020–23 file, March–July 2021 rows appeared an even number of times (2×, 4× or more), so the cleaner retained half of each exact-row group. August–October 2021 are missing and stay as gaps. Sub sales are only recorded from 2024, so they are left out of every comparison across years. 2024 prices were reconstructed from whole-dollar price per sqft times area; their last price digits are unreliable.
-- **What's left:** 106,449 sales with a floor band and, for 99-year homes, a lease start. All 544 projects found only in 2020–24 have supplied coordinates, so 99.3% of these sales have a walking time. A new station counts from the month after it opened. Because August–October 2021 are missing, 2021 Q3 (July only, 145 sales) and 2021 Q4 (November–December only) are partial quarters.+- **What's left:** 106,449 sales with a floor band and, for 99-year homes, a lease start. All 544 projects found only in 2020–24 have supplied coordinates, so 99.3% of these sales have a walking time. A new station counts from the month after it opened. Because August–October 2021 are missing, 2021 Q3 (July only, 145 sales) and 2021 Q4 (November–December only) are partial quarters.
+**How to reproduce preprocessing.** The GitHub repository now includes `clean_2020_2025.py`, its input CSVs and `cleaning_log.txt`. The 2024 input already contains reconstructed prices; the cleaner flags those rows rather than recovering original negotiated prices. Joining the eleven historical-file parts reproduces the supplied cleaned table. Running the cleaner checks the earlier transformations from the supplied inputs. File hashes and the recorded software versions are listed in `CLEANING_PROVENANCE.md`.
+
+**Repository files:** [cleaner](https://github.com/BIGBACKDIU/DAO2702_project/blob/main/clean_2020_2025.py), [cleaning log](https://github.com/BIGBACKDIU/DAO2702_project/blob/main/cleaning_log.txt) and [input hashes and provenance](https://github.com/BIGBACKDIU/DAO2702_project/blob/main/CLEANING_PROVENANCE.md). The supplied cleaned file is retained for consistent analysis; the verified rebuild has the same rows and flags with negligible floating-point round-trip differences, but its bytes need not have the same hash.

```

## mk-audit
Distinguish a recorded cleaning snapshot from recalculation on raw files.
```diff
--- before review
+++ after review
@@ -1,4 +1,5 @@
-# Reproduced cleaning log from clean_2020_2025.py (without changing this input file).
+# Recorded source-block counts from the published cleaning log; cleaned-row flags are counted below.
+# The raw inputs and cleaner are supplied in GitHub so these preprocessing counts can also be checked.
 MK_AUDIT = pd.Series({'raw source rows': 118615, 'Mar–Jul 2021 rows before halving': 19796,
                    'Mar–Jul 2021 rows after halving': 9898, 'clean rows': len(mk_raw),
                    'sub sales excluded from trends': int(mk_raw.sub_sale.sum()),

```

## sec7a
Qualify the nominal top-up and avoid attributing a realised financial outcome to a buyer who waited.
```diff
--- before review
+++ after review
@@ -2,4 +2,4 @@
 - **Their flat rose faster in % terms:** about 8.3% a year, against 7.2% for eastern condos.
 - **But the top-up still widened:** route B minus their flat is estimated at about **S\$0.62M** in August–September 2020 and **S\$0.85M** in late 2025, and route F from S\$0.82M to S\$1.14M. A faster rise on a smaller base still leaves a bigger dollar gap.
 - **Two versions of the same number:** Step 6's index-scaled illustration puts the end-2025 top-up at about S\$0.83M; built from our own sales it is S\$0.85M. The difference comes from the condo index used.
-- **What it means:** over these five years, waiting made the upgrade more expensive in dollars, not cheaper. That is history, not a forecast.+- **What it means:** over these five years, the illustrated upgrade gap increased in nominal dollars. This does not measure affordability relative to income: the history does not track this family’s earnings, savings, debts or outstanding flat loan. It is a historical price-gap illustration, not an estimate of the financial effect of waiting.
```

## sec7b
Connect the cross-section and panel to the holding period without turning either into a depreciation forecast.
```diff
--- before review
+++ after review
@@ -3,4 +3,5 @@
 - **Why the bands differ is uncertain:** the groups can differ in location, project quality and which units resell. We do not observe completion dates, so we cannot establish that a fading new-building premium explains the result.
 - **Market-wide check:** across all 99-year resales, the oldest-lease projects (under 75 years left) also gained a little faster than those with 85–94 years left.
 - **What can't be measured:** inside one project, lease used rises exactly one year per year, so a single yearly depreciation rate can't be separated from the market. What is measured is the difference between bands in the same years.
-- **For the family:** route B’s 85–88-year lease band showed no weaker appreciation than the longer-lease band in 2020–25; this does not forecast its future price.+- **For the family:** route B’s 85–88-year lease band showed no weaker appreciation than the longer-lease band in 2020–25; this does not forecast its future price.
+**Connect this to their eventual sale.** Step 4’s lease bands describe price differences between projects in 2025. Step 7’s panel compares appreciation between project groups in the observed years. Neither identifies the resale price of their chosen home after a ten-year stay. In particular, the roughly 13% lower price of today’s 75–79-year band cannot be applied as a future loss to an 85–88-year home. The planning check below tracks remaining lease and loan balance under explicit price scenarios instead.

```

## lease-ten-year-text
Explain calendar ageing at a 2026 purchase and the ten-year ownership trade-off.
```diff
--- before review
+++ after review
@@ -0,0 +1,3 @@
+**Plan ten years of ownership, not just the purchase price.** The lease bands elsewhere describe 2025 sales. For an illustrative 2026 purchase, subtract one further year before the ten-year stay: B and C would have about **74–77 years left** at exit, versus **78–82** for F. The printed table checks this calendar arithmetic; exact lease dates and the actual purchase year matter.
+
+The table below starts with each route’s **2026-Q3 market-index price proxy**. It assumes a 75% loan over the persona’s loan term, a constant 1.6% rate, regular repayments and no refinancing. It asks what equity remains if the sale price after ten years is **20% lower, unchanged or 20% higher** than that starting price. These are chosen stress scenarios, not estimated future price ranges. Equity means sale price minus outstanding loan before sale costs and CPF refunds; it is not cash available to spend. The historical lease discount is not subtracted again.

```

## lease-ten-year
Add loan-balance and equity arithmetic under transparent price assumptions, without forecasting lease depreciation.
```diff
--- before review
+++ after review
@@ -0,0 +1,35 @@
+# Ownership planning arithmetic, separate from the lease regressions: no estimated depreciation is extrapolated.
+LEASE_BASE_YEAR, PLANNING_PURCHASE_YEAR, OWNERSHIP_YEARS = 2025, 2026, 10
+LEASE_ROUTE_BANDS={'B':(85,88),'C':(85,88),'F':(89,93)}
+EXIT_PRICE_CHANGES=(-.20,0.,.20)  # Chosen stress scenarios, not confidence bounds.
+def outstanding_balance(principal,annual_rate,term_years,elapsed_years):
+    paid=int(elapsed_years*12); total=int(term_years*12)
+    if paid>=total:return 0.
+    r=annual_rate/12
+    if r==0:return principal*(total-paid)/total
+    m=payment(principal,annual_rate,term_years)
+    return max(0.,principal*(1+r)**paid-m*((1+r)**paid-1)/r)
+EXIT_ROWS=[];EXIT_LEASE_ROWS=[]
+for route,(a,b) in LEASE_ROUTE_BANDS.items():
+    calendar_shift=PLANNING_PURCHASE_YEAR-LEASE_BASE_YEAR
+    entry=opt.loc[route,'2026-Q3 index proxy'];loan=LTV['first loan']*entry
+    balance=outstanding_balance(loan,PAYMENT_RATE,TENURE,OWNERSHIP_YEARS)
+    EXIT_LEASE_ROWS.append({'option':route,'2025 lease band':f'{a}–{b}',
+                           'lease at 2026 purchase':f'{a-calendar_shift}–{b-calendar_shift}',
+                           'lease after 10-year stay':f'{a-calendar_shift-OWNERSHIP_YEARS}–{b-calendar_shift-OWNERSHIP_YEARS}'})
+    for change in EXIT_PRICE_CHANGES:
+        exit_price=entry*(1+change)
+        EXIT_ROWS.append({'option':route,'starting price proxy':entry,'price change assumption %':100*change,
+                         'sale-price scenario':exit_price,'outstanding loan':balance,'equity before costs and CPF':exit_price-balance})
+EXIT_LEASE=pd.DataFrame(EXIT_LEASE_ROWS).set_index('option')
+EXIT_DETAIL=pd.DataFrame(EXIT_ROWS).set_index(['option','price change assumption %'])
+EXIT_VIEW=EXIT_LEASE[['lease after 10-year stay']].copy()
+EXIT_VIEW['outstanding loan']=EXIT_DETAIL.xs(0.,level=1)['outstanding loan'].map(sgm)
+for change,label in [(-20.,'equity: price -20%'),(0.,'equity: price unchanged'),(20.,'equity: price +20%')]:
+    EXIT_VIEW[label]=EXIT_DETAIL.xs(change,level=1)['equity before costs and CPF'].map(sgm)
+EXIT_VIEW.index=['B · East, lower cost','C · North-east','F · East, more lease']
+print({'lease baseline year':LEASE_BASE_YEAR,'illustrative purchase year':PLANNING_PURCHASE_YEAR,
+       'years owned':OWNERSHIP_YEARS,'loan %':100*LTV['first loan'],'term years':TENURE,'constant rate %':100*PAYMENT_RATE,
+       'price-change scenarios %':[100*x for x in EXIT_PRICE_CHANGES]})
+display(EXIT_LEASE);display(EXIT_VIEW)
+print('Financial assumptions, not estimated effects. Confidence intervals and p-values do not apply. Detailed currency arithmetic is in Appendix C.')

```

## sec7e
Use association language and qualify the historical timing illustration.
```diff
--- before review
+++ after review
@@ -1,4 +1,4 @@
 **What five years add to the advice:**
 - **Sell first, buy a resale with 85–88 years left:** still holds. Those projects showed no clear shortfall against longer-lease ones over 2020–25.
-- **Timing:** the top-up widened by about S\$0.23M in dollars over five years. Waiting has not historically made the upgrade cheaper.
-- **MRT:** a short walk carries a lasting premium (about +7% to +17% depending on the year), but the TEL4 comparison detected no clear extra rise at opening.+- **Timing:** the top-up widened by about S\$0.23M in dollars over five years. That is a nominal price-gap illustration; it does not track this family’s income or savings.
+- **MRT:** a short walk is associated with higher prices in each observed year (about +7% to +17% depending on the year), but the TEL4 comparison detected no clear extra rise at opening.
```

## mkt-geo
Reconcile growth windows and samples and remove the incorrect explanation of the widening top-up.
```diff
--- before review
+++ after review
@@ -1,4 +1,5 @@
 **The east was among the fastest-rising areas.** Holding home features fixed:
 - **By segment:** the outer suburbs (OCR) rose about 46% from late 2020, against 34% in the city fringe (RCR) and 15% in the core central region (CCR).
 - **By district:** from Jan–Jun 2021 to Jan–Jun 2025, Tampines/Pasir Ris rose about **47%** (95% CI 44–51%), level with Upper Thomson at the top, and north-east towns about 41%, against about 8% in Raffles Place (confidence interval includes zero). The median district rose 34%.
-- **For the family:** their target homes sit in the fastest-rising part of the island, which helps explain why the top-up in Step 7 kept widening even though their flat rose faster in % terms.+- **Different growth comparisons:** Step 7’s 7.2% annual figure follows the same eastern family-size resale projects from 2020 Q3 to 2025 Q4. This district figure compares the wider sale sample in Jan–Jun 2021 and Jan–Jun 2025 using recorded-feature controls. Different homes, windows and models mean these figures need not match.
+- **For the family:** the east’s growth is market context. Step 7’s widening top-up follows the larger condo price base: a smaller percentage rise on a more expensive home can exceed a larger percentage rise on a cheaper flat. The district ranking does not explain that top-up by itself.
```

## advice
Carry ten-year exit uncertainty into the recommendation and distinguish the trade-offs of B/C and F.
```diff
--- before review
+++ after review
@@ -2,6 +2,8 @@
 
 **Sell the flat first, then choose among three resale routes.** The graphic below puts price, upfront funds, payment and MRT walk on one page. Route B keeps them in the east at lower cost; C widens the search to the north-east towns; F buys more years of lease at a higher price.
 
+**Plan the eventual sale too.** B and C cost less now but have less lease remaining at the end of a ten-year stay. F buys extra lease at a higher price. The Step 7 planning check shows how the loan balance and equity vary under illustrative price scenarios; historical lease-band performance does not settle the exit-value question.
+
 **Inspect before choosing.** The 2025 comparable sales for B span Tampines and Pasir Ris; many are roughly 20 minutes from MRT. Route C spans four north-east towns. Check the actual school trip, station route, unit condition and available listings.
 
 **Other routes:** the Katong/Marine Parade freehold resale (E) and Tampines/Pasir Ris new launch (A) are above this buyer's assumed budget. The older Bedok route (D) has too few comparable sales for a dependable price. Buying before selling would require 20% ABSD upfront, refundable only if all IRAS conditions are met. The 2026-Q3 figures below are market-index proxies, not observed project prices.

```

## advice-cards
Use the named fixed payment-rate assumption; numerical payments do not change.
```diff
--- before review
+++ after review
@@ -9,7 +9,7 @@
 for ax, (code_, heading_, place_, trade_, col_) in zip(axs, CARD_ROUTES):
     ax.axis('off'); row_ = opt.loc[code_]
     p_ = row_['2026-Q3 index proxy']; upfront_ = row_['cash + CPF at proxy']
-    monthly_ = payment(.75 * p_, .016, TENURE)
+    monthly_ = payment(.75 * p_, PAYMENT_RATE, TENURE)
     ax.add_patch(_V3Box((.01, .02), .98, .96, transform=ax.transAxes,
                         boxstyle='round,pad=0.012,rounding_size=0.035',
                         facecolor='#f7f9fc', edgecolor=C['grid'], lw=1.2))

```

## feng-b
Explain why the six-year display contains only four annual September tests.
```diff
--- before review
+++ after review
@@ -1,3 +1,4 @@
 **Lucky numbers and the Ghost Month, 2020–2025.**
 - **Price endings:** prices ending in 8 rose from 23% of resales (2020) to 29% (2025), against about 5% ending in 4. The 2024 tags are faded because those prices were rebuilt.
-- **September vs other months:** resale prices were +2.1% (2022, 0 festival days in September) and +1.6% (2024, 2 festival days in September) against other months in years when the Hungry Ghost Month barely touched September, but only +0.3% (2023, 14 festival days in September) and +0.1% (2025, 21 festival days in September) when it did. This pattern is suggestive, but four years of month-only dates cannot identify a festival effect. The calendar month is only a rough stand-in for the festival.+- **September vs other months (2022–2025 only):** resale prices were +2.1% (2022, 0 festival days in September) and +1.6% (2024, 2 festival days in September) against other months in years when the Hungry Ghost Month barely touched September, but only +0.3% (2023, 14 festival days in September) and +0.1% (2025, 21 festival days in September) when it did. This pattern is suggestive, but four years of month-only dates cannot identify a festival effect. The calendar month is only a rough stand-in for the festival.
+The price-ending panel spans 2020–2025, but the September price comparison requires all twelve months. It excludes 2020 because the file starts in August and 2021 because August–October are missing. September is a calendar-month contrast, not a direct festival treatment; the festival can fall mostly or entirely in August.

```

## limits
Grade the new ownership illustration honestly and distinguish equity from cash and return.
```diff
--- before review
+++ after review
@@ -10,9 +10,11 @@
 **Assumptions to flag:**
 - **The profile is illustrative:** income, flat value, CPF refund, costs and ages are assumptions.
 - **Income measure:** gross employment income excluding employer CPF, the income banks count.
-- **Prices and rates:** observed comparables are 2025 sales. The 2026-Q3 figures are market-index proxies, not current project transactions. Payments at 1.6% are illustrative. The 2025 rate illustration assumes SORA + 0.30%.
+- **Prices and rates:** observed comparables are 2025 sales. The 2026-Q3 figures are market-index proxies, not current project transactions. Payments at 1.6% are a separate fixed planning assumption; December 2025 SORA plus 0.30 points is about 1.49%. The 2025 rate illustration assumes SORA + 0.30%.
 - **Not in the CSV:** bedroom counts and building age. Project locations were added from OneMap (99% matched); walking times use straight-line distance × 1.3, not routed paths. MRT/LRT interchanges count as MRT, LRT-only stops do not, and 2026 CCL6 stations are excluded from the 2025 analysis.
 - **Duplicates:** the data includes 1,442 exact duplicate rows; results barely change without them.
 - **Five-year data:** August–October 2021 are missing; an even-multiplicity March–July 2021 block was halved; sub sales exist only from 2024 and are excluded from cross-year comparisons; 2024 prices are rebuilt from whole-dollar psf. The top-up history moves 2025 route medians back with an index, so it shows the trend for homes like these, not observed past prices of these exact units. Cooling-measure and station-opening comparisons are observational.
 - **Map precision:** the district heat maps smooth between broad reference locations. Planning-area outlines are not postal-district boundaries. The MRT price map uses actual project points but still relies on geocoding and a distance-to-walk approximation.
 - **Buying costs and reserves:** the budget assumes no other debts and full use of the stated eligible CPF. Purchase legal fees, renovation, ongoing maintenance, property tax and temporary housing are not priced. Confirm loan approval, CPF availability and actual walking routes before choosing a unit.
+
+- **Ten-year ownership scenarios:** the price changes and constant mortgage rate are assumptions, not forecasts. Equity is sale price minus outstanding loan before selling costs and CPF refunds; it is not spendable cash or an investment return. The 2026 starting price is a market-index proxy. Remaining lease is calendar arithmetic from the stated 2025 bands.

```

## poster
Make the reading summary reflect the family’s holding period.
```diff
--- before review
+++ after review
@@ -4,7 +4,7 @@
 1. **Order:** selling first releases the family’s funds and avoids paying additional buyer’s stamp duty upfront on a second property.
 2. **Budget:** the flat-sale proceeds constrain this profile more than its income does. Keep a reserve below the ceiling.
 3. **Location:** compare neighbourhoods and actual station routes, not just a broad district median.
-4. **Home:** compare observed resale options by upfront cost, lease left, space and walk to MRT. Treat model discounts as an inspection list.
+4. **Home:** compare observed resale options by upfront cost, lease left now and after ten years, space and walk to MRT. Treat model discounts as an inspection list.
 5. **Timing:** use the historical evidence to understand risk. Neither the trend forecast nor the station-opening comparisons promise a buying window.
 
 The appendices retain model diagnostics, sensitivity results and numerical tables. They support the guide rather than form a separate buyer story.

```

## mk-stability
Correct annual-fit chart labels: floor, size and new-sale coefficients are not annual price-growth rates.
```diff
--- before review
+++ after review
@@ -51,7 +51,7 @@
     a_.fill_between(yrs_s, d_.low, d_.high, color=col, alpha=0.15, lw=0); a_.plot(yrs_s, d_.pct, color=col, lw=2.2, marker='o', ms=5)
     a_.axhline(0, color=C['ink2'], lw=0.8); a_.set_xticks(yrs_s); a_.set_xticklabels([f"'{str(y)[2:]}" for y in yrs_s], fontsize=8.5)
     lo_, hi_ = d_.low.min(), d_.high.max(); pad_ = (hi_ - lo_) * 0.25 + 0.3; a_.set_ylim(min(lo_, 0) - pad_, max(hi_, 0) + pad_)
-    a_.set_title(f'{k}\n{d_.pct.min():+.1f}% to {d_.pct.max():+.1f}% a year', loc='left', fontsize=9.5, color=C['ink'], fontweight='bold')
+    a_.set_title(f'{k}\n{d_.pct.min():+.1f}% to {d_.pct.max():+.1f}% across years', loc='left', fontsize=9.5, color=C['ink'], fontweight='bold')
 for j_, (yr_t, r_t) in enumerate(MK_OOTT.iterrows()):
     a_ = AX_['efg'[j_]]; a_.axis('off'); a_.set_xlim(0, 1); a_.set_ylim(0, 1)
     a_.add_patch(FBP_((0.02, 0.05), 0.96, 0.9, boxstyle='round,pad=0,rounding_size=0.06', facecolor='#f4f6f8', edgecolor='none'))

```

## appendix-tables
Centralise differently defined new-sale premiums and print all new scenario and price-screen evidence.
```diff
--- before review
+++ after review
@@ -31,4 +31,16 @@
 display(hed_view.round(4).rename(columns={'pct': 'effect %', 'pct_lo': '95% low', 'pct_hi': '95% high', 'p': 'p-value'}))
 display(curve.round(1)); display(rmse.round(2).rename('typical forecast error, % points per quarter'))
 display(adj.round(3).rename('adjusted R2')); display(BOOT.round(2)); display(pd.Series({**{f'VIF {k}': round(v, 2) for k, v in VIF.items()}, 'max Cook distance': round(cook.max(), 4)}, name='diagnostics'))
-fc.round(1)+fc.round(1)
+# Put all new-sale estimates in one labelled reference table.
+PREMIUM_REFERENCE=causal[['gap %','low','high']].rename(columns={'gap %':'gap %','low':'95% low','high':'95% high'}).copy()
+PREMIUM_REFERENCE['comparison']='2025, 99-year units; see Step 4'
+PREMIUM_REFERENCE.loc['Broad hedonic model (all tenures)',:]=[hed.loc['sale_New Sale','pct'],hed.loc['sale_New Sale','pct_lo'],hed.loc['sale_New Sale','pct_hi'],'2025 market-wide coefficient, not the matched gap']
+display(PREMIUM_REFERENCE.round(2))
+for year,r in MK_PREM.iterrows():
+    PREMIUM_REFERENCE.loc[f'{int(year)} annual matching, no floor bands',:]=[r.premium,r.low,r.high,'All tenures; district × quarter × size-band matched OLS']
+for _,r in MK_STAB[MK_STAB.effect=='New sale'].iterrows():
+    PREMIUM_REFERENCE.loc[f'{int(r.year)} annual hedonic coefficient',:]=[r.pct,r.low,r.high,'All tenures; separate annual hedonic model']
+print('Central reference: the first five rows and annual rows use different samples, controls and weighting. They are not equivalent estimates.')
+display(PREMIUM_REFERENCE.round(2))
+display(SCREEN_CHECK.round(2));display(EXIT_LEASE);display(EXIT_DETAIL.round(0))

```
