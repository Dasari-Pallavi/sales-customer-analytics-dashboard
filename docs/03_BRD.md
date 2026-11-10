# Business Requirements Document (BRD)
**Project:** AI-Powered Sales & Customer Analytics Dashboard
**Version:** 1.0 | **Author:** [Pallavi Dasari], Business Analyst | **Date:** 10-Nov-2026
**Status:** Draft for stakeholder review

## 1. Document Control
| Version | Date | Author | Change |
|---|---|---|---|
| 0.1 | 10-Nov-2026 | [Pallavi Dasari] | First draft |
| 1.0 | 10-Nov-2026 | [Pallavi Dasari] | Ready for review |

## 2. Executive Summary
Reporting at Superstore Retail Co. is manual and slow, and the business cannot see
revenue trends, cancellation losses or customer segments. This project delivers a
self-service dashboard with KPIs, RFM customer segmentation and a 6-month revenue
forecast, built on the Online Retail II dataset.

## 3. Business Problem and Objectives
See docs/01_problem_statement.md.

| ID | Objective | Measure of success |
|---|---|---|
| BO-1 | One dashboard for revenue, orders and customer KPIs | Dashboard totals reconcile 100% with source data |
| BO-2 | Track revenue lost to cancellations | Cancellation rate shown by month and country |
| BO-3 | Segment customers for targeted marketing | 4+ segments with downloadable lists |
| BO-4 | Provide a revenue forecast | 6-month forecast with error (MAPE) reported |
| BO-5 | Reduce reporting effort | Report time drops from ~3 days to minutes |

## 4. Scope
**In scope:** revenue, orders, customers, products, countries, cancellations, RFM, forecast.
**Out of scope:** profit and cost analysis, real-time data, payment and logistics data.

## 5. Stakeholders
See docs/02_stakeholder_analysis.md.

## 6. Current State (As-Is) and Future State (To-Be)
**As-Is:** Export data > clean manually in Excel > build pivot tables > email report (about 3 days).
**To-Be:** Data loaded and cleaned by script > dashboard refreshes > managers filter and
explore on their own (minutes).

## 7. Functional Requirements
| ID | Requirement | Priority | Objective |
|---|---|---|---|
| FR-01 | Show total revenue, total orders, total customers and average order value as KPI cards | Must | BO-1 |
| FR-02 | Allow filtering by year, month, country and product | Must | BO-1 |
| FR-03 | Show monthly revenue trend with month-on-month growth % | Must | BO-1 |
| FR-04 | Show revenue by country (map or bar chart) | Must | BO-1 |
| FR-05 | Show top 10 and bottom 10 products by revenue | Must | BO-1 |
| FR-06 | Show cancellation count, cancelled value and cancellation rate % | Must | BO-2 |
| FR-07 | Classify each customer into an RFM segment | Must | BO-3 |
| FR-08 | Show segment size, average spend and a downloadable customer list | Should | BO-3 |
| FR-09 | Show a 6-month revenue forecast with a confidence range | Should | BO-4 |
| FR-10 | Show repeat-customer % | Could | BO-1 |

## 8. Non-Functional Requirements
| ID | Requirement |
|---|---|
| NFR-01 | Each dashboard page loads within 5 seconds |
| NFR-02 | Dashboard works in Power BI Desktop and as an exported PDF |
| NFR-03 | Data refresh is monthly |
| NFR-04 | All metric definitions are documented (docs/06_kpi_definitions.md) |
| NFR-05 | Dashboard is readable on a standard laptop screen |

## 9. Data Requirements
- **Source:** Online Retail II (Kaggle / UCI), 1,067,371 rows, Dec 2009 to Dec 2011.
- **Fields:** Invoice, StockCode, Description, Quantity, InvoiceDate, Price, Customer ID, Country.
- **Business rules:**
  - Revenue = Quantity x Price (GBP).
  - Invoice starting with "C" = cancellation.
  - Rows with missing Customer ID are excluded from customer-level analysis only.
  - Rows with Price <= 0 are excluded.
  - Duplicate rows are removed.
- **Data quality:** see docs/10_data_dictionary.md.

## 10. Assumptions, Constraints, Dependencies
- Historical data represents normal business behaviour.
- No cost data exists, so profit analysis is not possible.
- Power BI Desktop (free) is the dashboard tool.

## 11. Risks
See docs/01_problem_statement.md.

## 12. Acceptance and Sign-off
The project is accepted when all Must requirements pass UAT (docs/08_UAT_test_cases).

| Name | Role | Signature | Date |
|---|---|---|---|
| | Sales Head | | |
| | Marketing Manager | | |
| | Finance Manager | | |