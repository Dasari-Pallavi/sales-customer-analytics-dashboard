cat << 'EOF' > docs/10_data_dictionary.md
# Data Dictionary & Quality Rules (Online Retail II)

| Column Name | Data Type | Description | Data Quality Issue & BA Resolution |
| :--- | :--- | :--- | :--- |
| **Invoice** | String | 6-digit transaction number. Prefixed with `'C'` for cancellations. | Separate `'C'` invoices into `returns_clean.csv` to compute Return Rate % without distorting sales. |
| **StockCode** | String | 5-digit unique product code. | Filter out non-product codes (`POST`, `DOT`, `M`, `BANK CHARGES`, `ADJUST`) from SKU rankings. |
| **Description** | String | Product name. | Standardize text whitespace and uppercase formatting; drop rows with null descriptions and `Price = 0`. |
| **Quantity** | Integer | Units purchased per line item. | Negative quantities on non-`'C'` invoices represent inventory write-offs/damages; exclude from sales. |
| **InvoiceDate** | Datetime | Timestamp of transaction (`2009-12-01` to `2011-12-09`). | Parse into `Date`, `Year`, `Month`, `YearMonth`, and `DayOfWeek` for time-series analysis. |
| **Price** | Float | Unit price in British Pounds (£). | Remove rows where `Price <= 0` (free samples or system adjustments). |
| **Customer ID** | String | 5-digit unique customer identifier. | ~243K rows are null (guest orders). Keep in `sales_clean.csv` for store KPIs; filter out for RFM clustering. |
| **Country** | String | Customer country of residence. | Retain all 41 countries; group minor markets into "Other" for executive charts if needed. |
EOF
