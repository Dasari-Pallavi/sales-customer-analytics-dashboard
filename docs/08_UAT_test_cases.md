# User Acceptance Testing (UAT) Sign-Off Log

| Test ID | Test Case Description | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- |
| **TC-01** | Reconcile Gross Revenue card with Python/SQL output | Exact match to 2 decimal places | Verified exact match | **Pass** |
| **TC-02** | Verify `'C'` prefixed invoices are isolated in Return Rate % | Cancelled orders excluded from Gross Revenue; Return Rate % accurate | Verified exact match | **Pass** |
| **TC-03** | Test Country Slicer filtering on Executive Overview | Selecting any country updates all KPI cards in < 3 seconds | Updated in 1.2 seconds | **Pass** |
| **TC-04** | Validate Customer RFM Cluster assignment | 100% of non-null `Customer_ID` records assigned to 1 of 4 clusters | 0 null clusters found | **Pass** |
| **TC-05** | Verify 6-Month Forecast display | Displays 6 monthly forecast points with upper/lower confidence bounds | Rendered accurately | **Pass** |
