# Problem Statement

## Business Context
Superstore Retail Co. (based on the UCI Online Retail II dataset) is a UK-based online
retailer of gift-ware that sells to retail customers and wholesalers in 40+ countries.
It recorded over one million transaction lines between December 2009 and December 2011.

## Problem
Sales reporting is manual and scattered across spreadsheets. As a result:
- Management cannot quickly see revenue trends by month, country or product.
- Cancelled and returned orders are not tracked, so revenue loss is unclear.
- All customers receive the same marketing, because customers are not segmented.
- There is no sales forecast, so inventory planning relies on guesswork.
- Producing one monthly report takes about 2-3 days of manual effort.

## Business Objectives
1. Provide one dashboard with revenue, order and customer KPIs.
2. Measure and reduce revenue loss from cancellations and returns.
3. Segment customers using RFM analysis to support targeted marketing.
4. Provide a 6-month revenue forecast for planning.
5. Reduce reporting time from days to minutes.

## Success Metrics
- Dashboard totals match source data (100% reconciliation).
- All 5 user stories pass UAT.
- Customer segments delivered with downloadable lists.
- Forecast error (MAPE) reported and below an agreed threshold.

## Scope
**In scope:** revenue, orders, customers, products, countries, cancellations, RFM, forecast.
**Out of scope:** profit and cost analysis (no cost data available), real-time data,
payment or logistics data.

## Assumptions and Constraints
- Revenue = Quantity x Unit Price (in GBP).
- Rows without a Customer ID are excluded from customer-level analysis only.
- Invoices starting with "C" are treated as cancellations.
- Data is historical; refresh is monthly.

## Risks

| Risk | Impact | Mitigation |
|---|---|---|
| ~23% of rows have no Customer ID | Customer analysis covers fewer rows | Document it; use all rows for revenue KPIs |
| Outliers and negative quantities | Misleading totals | Define and apply cleaning rules |
| No cost data | Cannot measure profit | Declared out of scope |
