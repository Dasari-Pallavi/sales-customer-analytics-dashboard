# Data Dictionary and Data Quality Report

**Source:** Online Retail II (Kaggle / UCI), https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci  
**Period:** [min date] to [max date] | **Rows:** [total] | **Columns:** 8

## 1. Data Dictionary

| Column | Type | Description | Business meaning | Quality notes |
|---|---|---|---|---|
| invoice | Text | Invoice number; starts with "C" for cancellations | One order / one cancellation | [x]% are cancellations |
| stockcode | Text | Product code (5 digits) | Product identifier | Non-5-digit codes are fees/postage/samples |
| description | Text | Product name | Product label | [x] missing |
| quantity | Integer | Units per line | Units sold (negative = return) | [x] negative rows |
| invoicedate | Datetime | Date and time of the invoice | Order time | No missing values |
| price | Decimal | Unit price in GBP (£) | Selling price per unit | [x] rows <= 0 |
| customer_id | Number | Customer identifier | Who bought | [x]% missing |
| country | Text | Customer's country | Market | [x] countries |

**Derived field:** revenue = quantity x price

## 2. Data Quality Findings

| # | Issue | Rows | % of data | Impact |
|---|---|---|---|---|
| 1 | Missing Customer ID | [ ] | [ ] | Customer analysis (RFM) cannot use these rows |
| 2 | Duplicate rows | [ ] | [ ] | Inflates revenue and orders |
| 3 | Cancellations (invoice starts with C) | [ ] | [ ] | Needed for cancellation KPI; must not count as sales |
| 4 | Zero or negative price | [ ] | [ ] | Not real sales (adjustments, free items) |
| 5 | Non-product stock codes | [ ] | [ ] | Distort product rankings |
| 6 | Missing description | [ ] | [ ] | Mostly zero-price or adjustment rows |

## 3. Cleaning Decisions (Decision Log)

| ID | Rule | Reason | Applies to |
|---|---|---|---|
| CR-01 | Remove exact duplicate rows | Double counting | All analysis |
| CR-02 | Separate cancellations (invoice starts with C) into their own table | Needed for cancellation KPI, excluded from sales KPIs | Sales KPIs |
| CR-03 | Remove rows with price <= 0 | Not real sales | All analysis |
| CR-04 | Exclude non-product stock codes from product rankings | Not products | Product analysis |
| CR-05 | Keep rows with missing Customer ID for revenue KPIs; exclude for RFM | Avoids losing real revenue while keeping RFM valid | Revenue vs Customer KPIs |
| CR-06 | Revenue = quantity x price | No sales amount column provided | All KPIs |

## 4. Open Questions for Stakeholders
- Do missing Customer IDs represent guest checkouts or system errors?
- Should wholesale customers be analysed separately from retail customers?
- Should postage fees count as revenue?
