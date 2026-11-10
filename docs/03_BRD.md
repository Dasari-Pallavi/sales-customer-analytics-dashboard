cat << 'EOF' > docs/03_BRD.md
# Business Requirements Document (BRD)
**Project Name:** AI-Powered Sales & Customer Analytics Dashboard  
**Dataset:** Online Retail II (UCI / Kaggle)  
**Document Version:** 1.0  
**Author:** Dasari Pallavi (Business Analyst)  

---

## 1. Executive Summary
A UK-based online giftware retailer processes over 1.06 million transactions across 2009–2011. Leadership currently relies on manual spreadsheet consolidation, resulting in delayed reporting, unquantified return losses, and generic marketing campaigns. This project delivers an automated, AI-powered Power BI dashboard featuring clean revenue KPIs, return-rate tracking, RFM customer segmentation, and a 6-month statistical sales forecast.

## 2. Business Objectives
* **Eliminate Manual Reporting:** Reduce monthly reporting turnaround from 3 business days to automated self-service views.
* **Quantify Return Leakage:** Isolate cancelled invoices (prefixed with `"C"`) to measure true Net Revenue and identify high-return SKUs.
* **Enable Precision Marketing:** Group ~4,300+ identifiable customers into actionable behavioral clusters (Champions, Loyal, At-Risk, Lost).
* **Support Inventory Planning:** Provide a 6-month revenue forecast to prepare stock levels for Q4 seasonal spikes.

## 3. Scope & Data Constraints
* **In-Scope:** Gross Revenue, Cancellations/Returns, Net Revenue (`Quantity × Price`), Average Order Value (AOV), Country-level performance, Repeat Customer Rate, RFM + K-Means clustering, and 6-month time-series forecasting.
* **Out-of-Scope (Data Constraint):** The source dataset lacks Cost of Goods Sold (COGS) and supplier margin fields. Therefore, Gross Profit and Net Profit Margin KPIs are excluded from this release.
* **Data Governance Rule:** Transactions with missing `Customer ID` (~243,000 guest checkouts) are retained for store-wide revenue totals but excluded from customer-level RFM segmentation.

## 4. Functional Requirements (FR)
* **FR-01 (Executive KPIs):** The dashboard shall display Net Revenue, Total Orders, Active Customers, AOV, and Cancellation Rate %, filterable by Year, Month, and Country.
* **FR-02 (Product & Return Analysis):** The dashboard shall rank the Top 10 revenue-generating products and Top 10 most-returned products by cancelled value.
* **FR-03 (Geographic Breakdown):** The dashboard shall compare UK domestic revenue against international markets (e.g., EIRE, Netherlands, Germany, France).
* **FR-04 (AI Customer Segmentation):** The system shall score identifiable customers on Recency, Frequency, and Monetary value and cluster them into 4 segments using K-Means.
* **FR-05 (AI Revenue Forecasting):** The dashboard shall display a 6-month forward revenue forecast with upper and lower confidence intervals.

## 5. Non-Functional Requirements (NFR)
* **NFR-01 (Performance):** Dashboard slicers and visual cross-filters must update in under 5 seconds.
* **NFR-02 (Reconciliation):** Dashboard Net Revenue and Order Counts must match validated SQL/Python outputs with 0% variance.
* **NFR-03 (Usability):** Visuals must follow a 4-page executive layout with clear titles and AI Smart Narrative summaries.
EOF
