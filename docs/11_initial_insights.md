# Initial Insights (from KPI analysis)

total_revenue   = sales["revenue"].sum()
total_orders    = sales["invoice"].nunique()
total_customers = sales["customer_id"].nunique()
total_units     = sales["quantity"].sum()
aov             = total_revenue / total_orders

cancel_value    = cancels["revenue"].abs().sum()
cancel_invoices = cancels["invoice"].nunique()
cancel_rate_val = cancel_value / total_revenue * 100
cancel_rate_ord = cancel_invoices / (total_orders + cancel_invoices) * 100

orders_per_cust = sales.dropna(subset=["customer_id"]).groupby("customer_id")["invoice"].nunique()
repeat_pct      = (orders_per_cust >= 2).mean() * 100

kpis = pd.DataFrame({
    "KPI": ["Total Revenue (£)", "Total Orders", "Total Customers", "Units Sold",
            "Average Order Value (£)", "Cancelled Value (£)", "Cancelled Invoices",
            "Cancellation Rate by Value (%)", "Cancellation Rate by Orders (%)",
            "Repeat Customer (%)"],
    "Value": [total_revenue, total_orders, total_customers, total_units,
              aov, cancel_value, cancel_invoices,
              cancel_rate_val, cancel_rate_ord, repeat_pct]
})
os.makedirs("../outputs/reports", exist_ok=True)
kpis.to_csv("../outputs/reports/kpi_summary.csv", index=False)
kpis


monthly = sales.groupby("month").agg(revenue=("revenue", "sum"),
                                     orders=("invoice", "nunique"),
                                     customers=("customer_id", "nunique")).reset_index()
monthly["mom_growth_pct"] = monthly["revenue"].pct_change() * 100

canc_m = cancels.groupby("month")["revenue"].apply(lambda s: s.abs().sum()).rename("cancel_value")
monthly = monthly.merge(canc_m, on="month", how="left").fillna({"cancel_value": 0})
monthly["cancel_rate_pct"] = monthly["cancel_value"] / monthly["revenue"] * 100

monthly.to_csv("../outputs/reports/monthly_kpis.csv", index=False)
monthly


country = (sales.groupby("country")
                .agg(revenue=("revenue", "sum"), orders=("invoice", "nunique"),
                     customers=("customer_id", "nunique"))
                .sort_values("revenue", ascending=False).reset_index())
country["share_pct"] = country["revenue"] / country["revenue"].sum() * 100
country.to_csv("../outputs/reports/country_kpis.csv", index=False)

prod = (sales[sales["is_product"]]
        .groupby(["stockcode", "description"], dropna=False)
        .agg(revenue=("revenue", "sum"), units=("quantity", "sum")).reset_index())
top10    = prod.sort_values("revenue", ascending=False).head(10)
bottom10 = prod[prod["revenue"] > 0].sort_values("revenue").head(10)
prod.to_csv("../outputs/reports/product_kpis.csv", index=False)

print("Top countries:"); display(country.head(10))
print("Top 10 products:"); display(top10)
print("Bottom 10 products:"); display(bottom10)



| # | Finding (with numbers) | Business meaning | Possible action |
|---|---|---|---|
| 1 | Total revenue was £[ ] across [ ] orders and [ ] customers | Size of the business | Baseline for targets |
| 2 | The United Kingdom contributes [ ]% of revenue | Heavy dependence on one market | Test growth in top 3 non-UK countries: [ ] |
| 3 | Revenue peaks in [months] each year | Seasonal demand | Build inventory ahead of [months] |
| 4 | Cancellation rate is [ ]% by value (highest in [month]) | Revenue lost to returns | Investigate causes in high months |
| 5 | Repeat-customer rate is [ ]% | Customer loyalty level | Retention campaign for one-time buyers |
| 6 | Top 10 products give [ ]% of product revenue | Concentration in a few products | Protect stock of top sellers |
| 7 | Revenue peaks in [months] in both years | Strong seasonality | Build stock ahead of the peak |
| 8 | Forecast shows £[ ] for the next 6 months (back-test MAPE [ ]%) | Planning baseline | Use as a guide with the 80% range |
