# User Acceptance Testing (UAT) Sign-Off Log

| Test ID | Linked FR | Test Scenario | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| **TC-01** | FR-01 | Reconcile Power BI KPI cards against `outputs/reports/kpi_summary.csv` | Exact match for Revenue, Orders, Customers & AOV | Matched 100% | **Pass** |
| **TC-02** | FR-02 | Select `2011` and `United Kingdom` slicers on Pages 1–3 | All visuals update in < 5 seconds without errors | Updated in < 2s | **Pass** |
| **TC-03** | FR-03 | Verify Monthly Revenue & MoM Growth charts on Page 1 | Displays 24 complete months + incomplete Dec 2011 note | Verified | **Pass** |
| **TC-04** | FR-04 | Verify Top Countries excluding UK chart on Page 1 | UK excluded cleanly; international rankings accurate | Verified | **Pass** |
| **TC-05** | FR-05 | Check Page 2 (`is_product = True`) Top 10 & Bottom 10 charts | Non-product codes excluded; Bottom 10 shows Revenue > 0 | Verified | **Pass** |
| **TC-06** | FR-06 | Verify Cancellations page (`'C'` invoices isolated) | Cancellation Rate % and Country chart reconcile with Python | Verified | **Pass** |
| **TC-07** | FR-07 | Filter Page 4 by `Champions` and `At Risk` segments | Customer count, cluster donut, and table filter accurately | Verified | **Pass** |
| **TC-08** | FR-08 | Right-click Customer Table → Copy Table & verify CSV export | Customer ID list exports cleanly for Marketing campaigns | Verified | **Pass** |
| **TC-09** | FR-09 | Inspect Page 5 Forecast line chart, table & MAPE card | Shows 6-month forecast, 80% bounds, MAPE & limitations | Verified | **Pass** |
| **TC-10** | FR-10 | Validate Repeat Customer % card on Page 1 | Matches `kpi_summary.csv` repeat-buyer percentage | Verified | **Pass** |

| D-03 | UAT-01 | `Total orders equals KPI file` failed in automated UAT script with `DtypeWarning` | `pd.read_csv()` inferred mixed types (`int` and `str`) for `invoice`, double-counting unique orders | Added `dtype={"invoice": str}` on CSV import in `src/uat_checks.py` | Passed (13/13) |
