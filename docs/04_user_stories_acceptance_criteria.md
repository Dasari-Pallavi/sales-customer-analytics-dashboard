# User Stories and Acceptance Criteria

| ID | Epic | Priority | Points | Linked FR |
|---|---|---|---|---|
| US-01 | Dashboard | Must | 5 | FR-01, 02, 03, 04 |
| US-02 | Analysis | Must | 3 | FR-06 |
| US-03 | AI Models | Must | 8 | FR-07, 08 |
| US-04 | AI Models | Should | 5 | FR-09 |
| US-05 | Dashboard | Must | 3 | FR-05 |

---
## US-01: Revenue by country and month
**As a** Sales Head, **I want** to see revenue and orders by country and month,
**so that** I can find weak markets and slow months.

**Acceptance criteria**
- **Given** the dashboard is open, **when** I select a year, **then** all KPI cards, charts and the map update within 5 seconds.
- **Given** the dashboard is open, **when** I select a country, **then** revenue and orders show only that country.
- **Given** any filter selection, **when** I compare totals with the cleaned data, **then** they match exactly.
- **Given** the trend chart, **when** I view it, **then** month-on-month growth % is displayed.

## US-02: Cancellation rate
**As a** Finance Manager, **I want** to see the cancellation rate, **so that** I can control revenue loss.

**Acceptance criteria**
- **Given** the cancellation page, **when** I open it, **then** I see cancelled invoices, cancelled value and cancellation rate %.
- **Given** a month or country filter, **when** I apply it, **then** cancellation figures update accordingly.
- **Given** invoice numbers starting with "C", **when** the data is loaded, **then** they are counted as cancellations and not as sales.

## US-03: Customer segments
**As a** Marketing Manager, **I want** customers grouped into segments, **so that** I can run targeted campaigns.

**Acceptance criteria**
- **Given** the segment page, **when** I open it, **then** at least 4 named segments (for example Champions, Loyal, At-Risk, Lost) are shown.
- **Given** each segment, **when** I view it, **then** I see customer count, average spend, average order frequency and recency.
- **Given** a segment, **when** I click export, **then** I can download its customer ID list.
- **Given** the RFM method, **when** it is documented, **then** the scoring rules are written in docs/06_kpi_definitions.md.

## US-04: Revenue forecast
**As an** Operations Manager, **I want** a 6-month revenue forecast, **so that** I can plan inventory.

**Acceptance criteria**
- **Given** the forecast page, **when** I open it, **then** I see actual and forecast revenue for the next 6 months with a confidence range.
- **Given** the forecast model, **when** it is validated, **then** the error (MAPE) is reported on the page.
- **Given** forecast limitations, **when** a user reads the page, **then** assumptions and limits are stated.

## US-05: Top and bottom products
**As a** Sales Head, **I want** to see top and bottom products by revenue, **so that** I can manage the product range.

**Acceptance criteria**
- **Given** the products page, **when** I open it, **then** the top 10 and bottom 10 products by revenue are shown.
- **Given** a year or country filter, **when** I apply it, **then** both lists update.
- **Given** non-product codes (postage, bank charges, samples), **when** the data is cleaned, **then** they are excluded from product rankings.

## Definition of Done (applies to every story)
- Requirement written, reviewed and linked to a Jira ticket
- Analysis or dashboard element built and checked against source data
- Acceptance criteria all passed
- Documentation updated and pushed to GitHub