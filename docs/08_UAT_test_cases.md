# User Acceptance Testing (UAT) Sign-Off Log

# User Acceptance Testing (UAT) Test Cases and Results

**Tester:** Dasari Pallavi | **Date:** 11-Nov-2026 | **Environment:** Power BI Desktop

| ID | Requirement | Test step | Expected result | Actual result | Status |
|---|---|---|---|---|---|
| UAT-01 | FR-01 | Compare Total Revenue, Orders, Customers and AOV cards with kpi_summary.csv | All four values match exactly | All 4 KPI cards matched `kpi_summary.csv` 100% | Passed |
| UAT-02 | FR-02, NFR-01 | Select year 2010 in the slicer | All visuals update within 5 seconds | All visuals updated in ~1.2 seconds | Passed |
| UAT-03 | FR-02 | Select country "Germany" | Revenue and orders match the Germany row in country_kpis.csv | Matched Germany row in `country_kpis.csv` | Passed |
| UAT-04 | FR-03 | Add monthly revenue values and compare with total | Sum of months equals Total Revenue | Verified via automated check (`PASS`) | Passed |
| UAT-05 | FR-03 | Open MoM growth chart | Growth % is displayed for each month | MoM Growth % bars rendered across all months | Passed |
| UAT-06 | FR-04 | Check UK revenue share against country_kpis.csv | Values match | UK share matched `country_kpis.csv` | Passed |
| UAT-07 | FR-05 | Compare top 10 products with product_kpis.csv | Same products and values; no postage or fee codes | Top 10 matched; non-product codes excluded | Passed |
| UAT-08 | FR-05 | Apply a year filter on Products page | Both top 10 and bottom 10 lists update | Both charts updated dynamically | Passed |
| UAT-09 | FR-06 | Compare cancellation cards with kpi_summary.csv | Values match | Cancelled Value, Invoices & Rate % matched | Passed |
| UAT-10 | FR-06 | Run src/uat_checks.py | No cancellation invoices in the sales data | Verified `0` `'C'` invoices in `sales_clean.csv` | Passed |
| UAT-11 | FR-07 | Open Customer Segments page | 4 or more segments shown with counts and spend | 6 RFM segments & 4 K-Means clusters shown | Passed |
| UAT-12 | FR-08 | Open rfm_customers.csv and the segment table | Customer list can be exported by segment | Verified Copy Table in Power BI & CSV export | Passed |
| UAT-13 | FR-09 | Open Forecast page | 6 forecast months with a range and MAPE displayed | 6 months, 80% bounds & MAPE card displayed | Passed |
| UAT-14 | US-04 | Look for limitations text on the Forecast page | Assumptions and limits are stated | Limitations note clearly visible on Page 5 | Passed |
| UAT-15 | FR-10 | Compare Repeat Customer % with kpi_summary.csv | Values match | Repeat Customer % matched `kpi_summary.csv` | Passed |
| UAT-16 | NFR-01 | Open each page and time the load | Each page loads within 5 seconds | All 5 pages loaded in under 2 seconds | Passed |
| UAT-17 | NFR-04 | Check docs/06_kpi_definitions.md | Every dashboard metric is defined | All metrics & RFM rules documented in `docs/06` | Passed |

## Automated checks
Results saved in `outputs/reports/uat_automated_checks.csv`: **13 of 13 passed**.

## Defect log

| ID | Found in | Description | Cause | Fix | Re-test |
|---|---|---|---|---|---|
| D-01 | UAT-04 | Line chart initially grouped `YearMonth` by Year only | Power BI defaulted to Date Hierarchy on X-axis | Switched X-axis field from Date Hierarchy to plain `MonthStart` | Passed |
| D-02 | UAT-13 | `Forecast MAPE` measure threw table-not-found error | `revenue_forecast.csv` was not yet renamed to `forecast` | Imported CSV and renamed table to `forecast` | Passed |

## Sign-off
Tests passed: **17 / 17**. All Must requirements passed: **Yes**.  
Open issues: **0**

| D-03 | UAT-01 | `Total orders equals KPI file` failed in automated UAT script with `DtypeWarning` | `pd.read_csv()` inferred mixed types (`int` and `str`) for `invoice`, double-counting unique orders | Added `dtype={"invoice": str}` on CSV import in `src/uat_checks.py` | Passed (13/13) |
