"""Automated data-level UAT checks.
Run from the project root:  python src/uat_checks.py
"""
import pandas as pd

sales   = pd.read_csv("data/processed/sales_clean.csv", dtype={"invoice": str})
kpi     = pd.read_csv("outputs/reports/kpi_summary.csv").set_index("KPI")["Value"]
monthly = pd.read_csv("outputs/reports/monthly_kpis.csv")
country = pd.read_csv("outputs/reports/country_kpis.csv")
rfm     = pd.read_csv("outputs/reports/rfm_customers.csv")
fc      = pd.read_csv("outputs/reports/revenue_forecast.csv")

results = []
def check(name, ok, detail=""):
    results.append({"check": name, "result": "PASS" if ok else "FAIL", "detail": detail})

total_rev = sales["revenue"].sum()

# Data rules (docs/10 cleaning decisions)
check("CR-01 no duplicate rows in sales", not sales.duplicated().any())
check("CR-02 no cancellation invoices in sales", not sales["invoice"].astype(str).str.startswith("C").any())
check("CR-03 no price <= 0 in sales", (sales["price"] > 0).all())
check("No negative quantity in sales", (sales["quantity"] > 0).all())

# Reconciliation (UAT-01, 04, 06)
kpi_rev = kpi["Total Revenue (£)"]
check("Total revenue equals KPI file", abs(total_rev - kpi_rev) < 1, f"{total_rev:,.2f} vs {kpi_rev:,.2f}")
check("Sum of monthly revenue equals total", abs(monthly["revenue"].sum() - total_rev) < 1)
check("Sum of country revenue equals total", abs(country["revenue"].sum() - total_rev) < 1)
check("Total orders equals KPI file", sales["invoice"].nunique() == int(kpi["Total Orders"]))

# Segments (UAT-11)
check("RFM has one row per customer", rfm["customer_id"].is_unique)
check("At least 4 RFM segments", rfm["segment"].nunique() >= 4, f"{rfm['segment'].nunique()} segments")
check("RFM scores within 1-5", rfm[["r_score", "f_score", "m_score"]].stack().between(1, 5).all())

# Forecast (UAT-13)
check("Forecast has 6 months", len(fc) == 6)
check("Forecast sits inside its range", ((fc["lower_80"] <= fc["forecast"]) & (fc["forecast"] <= fc["upper_80"])).all())

out = pd.DataFrame(results)
out.to_csv("outputs/reports/uat_automated_checks.csv", index=False)
print(out.to_string(index=False))
print("\nPassed:", (out["result"] == "PASS").sum(), "of", len(out))
