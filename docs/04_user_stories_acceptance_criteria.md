cat << 'EOF' > docs/04_user_stories_acceptance_criteria.md
# User Stories & Acceptance Criteria

| Story ID | Epic | User Story | Acceptance Criteria (Given / When / Then) |
| :--- | :--- | :--- | :--- |
| **US-01** | SCAD-E2 | As a **Commercial Director**, I want cancelled orders separated from valid sales so that I can see true Net Revenue and Return Rate %. | **Given** raw invoice data containing `"C"` prefixes, **When** the dashboard loads, **Then** Gross Revenue, Cancelled Value, and Net Revenue are displayed separately and match the cleaned dataset. |
| **US-02** | SCAD-E3 | As a **Regional Sales Lead**, I want to filter revenue and order volume by Country so that I can track international growth outside the UK. | **Given** the Executive Overview page, **When** I select "Germany" or "Netherlands" in the Country slicer, **Then** all KPI cards and trend lines update within 5 seconds. |
| **US-03** | SCAD-E3 | As a **CRM & Marketing Lead**, I want customers grouped into RFM clusters so that I can target Champions and win back At-Risk buyers. | **Given** the Customer Analytics page, **When** I click the "At-Risk" segment, **Then** I see the exact customer count, average spend, and a filterable customer table. |
| **US-04** | SCAD-E3 | As a **Supply Chain Manager**, I want a 6-month revenue forecast so that I can plan inventory ahead of Q4 holiday peaks. | **Given** the AI Forecast page, **When** I view the time-series chart, **Then** historical monthly revenue connects smoothly to a 6-month forecast showing 95% confidence bounds. |
| **US-05** | SCAD-E4 | As a **Merchandising Manager**, I want to see the top products by revenue and by cancellation volume so that I can fix quality issues. | **Given** the Product & Returns page, **When** I inspect the bar charts, **Then** the Top 10 best-sellers and Top 10 returned SKUs are clearly ranked. |
EOF