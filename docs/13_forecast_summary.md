# Revenue Forecast Summary

Failed: Holt-Winters (additive trend + season) -> Cannot compute initial seasonals using heuristic method with less than two full seasonal cycles in the data.
Failed: Holt-Winters (damped trend + season) -> Cannot compute initial seasonals using heuristic method with less than two full seasonal cycles in the data.

Best model: Seasonal naive (same month last year) | back-test MAPE: 6.1%
6-Month Total Forecasted Revenue: £4,056,290.26


## Purpose
Support inventory and demand planning (US-04, FR-09, BO-4).

## Data
- Monthly revenue, Dec 2009 to Nov 2011 (24 months).
- Dec 2011 excluded because the data ends on 9 Dec 2011 (incomplete month).

## Method
1. Compared 4 models by hiding the last 4 months and measuring prediction error.
2. Selected the model with the lowest MAPE: **[best model name]**.
3. Re-fitted on all 24 months and forecast 6 months (Dec 2011 to May 2012).
4. Range shown is an approximate 80% interval based on past residuals.

## Model Comparison (Back-Test on Last 4 Months)

| Model | MAPE % | MAE £ |
|---|---|---|
| [paste all 4 rows from forecast_model_comparison.csv] | | |

Acceptance threshold agreed with stakeholders (assumption): MAPE <= 20%.  
Result: **[met / not met]**, MAPE = [ ]%.

## Forecast (GBP)

| Month | Forecast | Lower 80% | Upper 80% |
|---|---|---|---|
| [paste all 6 rows from revenue_forecast.csv] | | | |

## Business Use
- Expected peak months: [e.g., Dec 2011]. Plan stock 4–6 weeks ahead.
- Expected slow months: [e.g., Jan–Feb 2012]. Use for promotions and cash planning.

## Limitations
- Only two full seasonal cycles, so seasonal patterns are not firmly proven.
- The data has no promotions, prices or economic factors, which also drive revenue.
- The forecast shows direction and rough size, not exact values.
- Re-run monthly as new data arrives, and compare forecast with actual to improve it.
