# KPI Definitions

| KPI | Definition | Formula | Data used | Linked requirement |
|---|---|---|---|---|
| Total Revenue | Value of valid sales in GBP | SUM(quantity x price) | Clean sales rows | FR-01 |
| Total Orders | Number of distinct sales invoices | COUNT DISTINCT invoice | Clean sales rows | FR-01 |
| Total Customers | Distinct customers with an ID | COUNT DISTINCT customer_id | Rows with customer ID | FR-01 |
| Average Order Value (AOV) | Average revenue per order | Total Revenue / Total Orders | Clean sales rows | FR-01 |
| MoM Growth % | Revenue change vs previous month | (This month - Last month) / Last month x 100 | Monthly revenue | FR-03 |
| Cancelled Value | Value of cancelled invoices | SUM(ABS(quantity x price)) for invoices starting with C | Cancellation rows | FR-06 |
| Cancellation Rate % | Revenue lost to cancellations | Cancelled Value / Total Revenue x 100 | Both tables | FR-06 |
| Repeat Customer % | Customers with 2+ orders | Customers with 2+ invoices / Total Customers x 100 | Rows with customer ID | FR-10 |
| Revenue Share by Country | Country contribution | Country revenue / Total Revenue x 100 | Clean sales rows | FR-04 |

## Notes
- The last month in the data (Dec 2011) is incomplete and is excluded from growth and forecasting.
- Customer-based KPIs use only rows with a Customer ID (see CR-05).
- RFM scoring rules will be added in the next step.
