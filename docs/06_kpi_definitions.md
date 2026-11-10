cat << 'EOF' > docs/06_kpi_definitions.md
# KPI Definitions & Business Logic

1. **Gross Revenue (£):** `SUM(Quantity * Price)` for all valid non-cancelled orders (`Quantity > 0` and `Price > 0`).
2. **Cancelled / Return Value (£):** `ABS(SUM(Quantity * Price))` for invoices starting with `'C'`.
3. **Net Revenue (£):** `Gross Revenue - Cancelled Value`.
4. **Return / Cancellation Rate (%):** `(Cancelled Value / Gross Revenue) * 100`.
5. **Total Completed Orders:** `COUNT(DISTINCT Invoice)` excluding `'C'` prefixed invoices.
6. **Average Order Value (AOV):** `Gross Revenue / Total Completed Orders`.
7. **Active Identifiable Customers:** `COUNT(DISTINCT Customer ID)` where `Customer ID IS NOT NULL`.
8. **Repeat Customer Rate (%):** `(Customers with >1 distinct Invoice / Total Identifiable Customers) * 100`.
9. **Month-over-Month (MoM) Revenue Growth (%):** `((Current Month Revenue - Prior Month Revenue) / Prior Month Revenue) * 100`.
10. **Customer Lifetime Value (Historical):** `SUM(Quantity * Price)` per unique `Customer ID`.
EOF