# Executive Insights & Decision Support Report

## 1. Key Findings & Business Impact
* **Return & Cancellation Leakage:** Cancellations (`"C"` prefixed invoices) account for a significant share of gross order volume, heavily concentrated in a small group of high-return SKUs.
* **Geographic Concentration:** The United Kingdom generates over 80% of total revenue, while EIRE, Netherlands, Germany, and France lead international growth.
* **Customer Pareto Effect:** K-Means clustering on RFM scores reveals that the **Champions** and **Loyal Customers** segments drive the majority of repeat revenue, whereas a distinct **At-Risk** group shows high historical spend but long recency gaps.
* **Q4 Seasonality:** Historical trends confirm sharp revenue peaks between September and November ahead of the holiday season.

## 2. Actionable Recommendations
1. **Audit Top-Returned SKUs:** Investigate product descriptions, packaging, and supplier quality for the Top 10 most-returned items on Page 2 to reduce return rates.
2. **Launch At-Risk Win-Back Campaigns:** Export the **At-Risk** customer list from Page 3 and deploy targeted email incentives before they churn permanently.
3. **Align Inventory with AI Forecast:** Use the 6-month Holt-Winters forecast bounds on Page 4 to pre-order stock ahead of seasonal surges and prevent stockouts.
