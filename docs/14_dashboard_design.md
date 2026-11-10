# Dashboard Design

**Tool:** Power BI Desktop | **Audience:** Sales Head, Marketing, Finance, Operations

## Page Map

| Page | Purpose | Main visuals | Requirements |
|---|---|---|---|
| Executive Overview | Business health at a glance | KPI cards, monthly trend, MoM growth, country chart | FR-01, 02, 03, 04, 10 |
| Products | Range management | Top 10 and bottom 10 products | FR-05 |
| Cancellations | Revenue loss control | Cancel rate trend, cancel value by country | FR-06 |
| Customer Segments | Targeted marketing | RFM segments, cluster view, customer table | FR-07, 08 |
| Forecast | Planning | Actual vs forecast with range, MAPE | FR-09 |

## Design Decisions
- Same slicers (Year, Country) on pages 1 to 3 so users keep their context.
- Titles describe the content; a text note flags the incomplete last month.
- One main colour with an accent for warnings (cancellations, risk segments).
- Measures are defined once in a `_Measures` table to keep numbers consistent.

## Data Model
Star-style model: DimDate -> sales and cancellations; rfm -> sales by customer_id.

## Known Limitations
- Customer-level visuals cover only rows with a Customer ID (about 77% of rows).
- Export of the customer list uses Copy Table in Desktop, or the CSV in outputs/reports.
- No profit or cost data available (out of scope).
