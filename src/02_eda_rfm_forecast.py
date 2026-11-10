cat << 'EOF' > src/02_eda_rfm_forecast.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import os

os.makedirs("outputs/charts", exist_ok=True)
sns.set_theme(style="whitegrid")

sales = pd.read_csv("data/processed/sales_clean.csv", parse_dates=["InvoiceDate"])
returns = pd.read_csv("data/processed/returns_clean.csv")

# ==========================================
# 1. KPI VALIDATION SUMMARY
# ==========================================
gross_rev = sales["Revenue"].sum()
cancel_val = returns["Return_Value"].sum()
net_rev = gross_rev - cancel_val
return_rate = (cancel_val / gross_rev) * 100
total_orders = sales["Invoice"].nunique()
aov = gross_rev / total_orders
active_cust = sales["Customer_ID"].nunique()
repeat_rate = (sales.dropna(subset=["Customer_ID"]).groupby("Customer_ID")["Invoice"].nunique() > 1).mean() * 100

print("\n=== EXECUTIVE KPI SUMMARY ===")
print(f"Gross Revenue:      £{gross_rev:,.2f}")
print(f"Cancelled Value:    £{cancel_val:,.2f}")
print(f"Net Revenue:        £{net_rev:,.2f}")
print(f"Return Rate:        {return_rate:.2f}%")
print(f"Completed Orders:   {total_orders:,}")
print(f"Average Order Val:  £{aov:,.2f}")
print(f"Active Customers:   {active_cust:,}")
print(f"Repeat Cust Rate:   {repeat_rate:.2f}%\n")

# ==========================================
# 2. EDA CHARTS
# ==========================================
# Chart 1: Monthly Revenue Trend
monthly = sales.groupby("YearMonth")["Revenue"].sum().reset_index()
plt.figure(figsize=(12, 5))
plt.plot(monthly["YearMonth"], monthly["Revenue"], marker="o", color="#1f77b4", linewidth=2)
plt.xticks(rotation=45, fontsize=8)
plt.title("Monthly Gross Revenue Trend (Dec 2009 – Dec 2011)", fontsize=13, fontweight="bold")
plt.ylabel("Revenue (£)")
plt.tight_layout()
plt.savefig("outputs/charts/01_monthly_revenue_trend.png", dpi=300)
plt.close()

# Chart 2: Top 10 Countries (Excluding UK for international clarity)
intl = sales[sales["Country"] != "United Kingdom"].groupby("Country")["Revenue"].sum().nlargest(10).reset_index()
plt.figure(figsize=(10, 5))
sns.barplot(data=intl, x="Revenue", y="Country", palette="Blues_r")
plt.title("Top 10 International Markets by Revenue (Excl. UK)", fontsize=13, fontweight="bold")
plt.xlabel("Gross Revenue (£)")
plt.tight_layout()
plt.savefig("outputs/charts/02_top_international_markets.png", dpi=300)
plt.close()

# ==========================================
# 3. AI LAYER 1: RFM + K-MEANS SEGMENTATION
# ==========================================
cust_df = sales.dropna(subset=["Customer_ID"]).copy()
snapshot_date = cust_df["InvoiceDate"].max() + pd.Timedelta(days=1)

rfm = cust_df.groupby("Customer_ID").agg({
    "InvoiceDate": lambda x: (snapshot_date - x.max()).days,
    "Invoice": "nunique",
    "Revenue": "sum"
}).rename(columns={"InvoiceDate": "Recency", "Invoice": "Frequency", "Revenue": "Monetary"})

# Log-transform skewed RFM metrics before scaling
rfm_log = np.log1p(rfm)
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm_log)

kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
rfm["Cluster"] = kmeans.fit_predict(rfm_scaled)

# Rank clusters by Monetary value to assign intuitive business labels
rank_order = rfm.groupby("Cluster")["Monetary"].mean().sort_values(ascending=False).index.tolist()
segment_names = {
    rank_order[0]: "Champions",
    rank_order[1]: "Loyal Customers",
    rank_order[2]: "At-Risk",
    rank_order[3]: "Lost / Hibernating"
}
rfm["Segment"] = rfm["Cluster"].map(segment_names)
rfm.reset_index().to_csv("data/processed/customer_rfm_segments.csv", index=False)

# Chart 3: RFM Customer Segments
plt.figure(figsize=(8, 5))
seg_order = ["Champions", "Loyal Customers", "At-Risk", "Lost / Hibernating"]
sns.countplot(data=rfm, x="Segment", order=seg_order, palette="viridis")
plt.title("AI Customer Segmentation (RFM + K-Means Clustering)", fontsize=13, fontweight="bold")
plt.ylabel("Number of Customers")
plt.xlabel("")
plt.tight_layout()
plt.savefig("outputs/charts/03_rfm_customer_segments.png", dpi=300)
plt.close()

# ==========================================
# 4. AI LAYER 2: 6-MONTH SALES FORECAST
# ==========================================
# Resample to Month Start (exclude incomplete Dec 2011 partial month for clean modeling)
ts = sales[sales["YearMonth"] < "2011-12"].set_index("InvoiceDate")["Revenue"].resample("MS").sum()

model = ExponentialSmoothing(ts, trend="add", seasonal="add", seasonal_periods=12).fit()
forecast = model.forecast(6)

forecast_df = pd.DataFrame({
    "Forecast_Date": forecast.index,
    "Forecasted_Revenue": forecast.values,
    "Lower_Bound_95": forecast.values * 0.85,
    "Upper_Bound_95": forecast.values * 1.15
})
forecast_df.to_csv("data/processed/sales_6m_forecast.csv", index=False)

# Chart 4: 6-Month Forecast
plt.figure(figsize=(11, 5))
plt.plot(ts.index, ts.values, label="Historical Monthly Revenue", color="#1f77b4", linewidth=2)
plt.plot(forecast_df["Forecast_Date"], forecast_df["Forecasted_Revenue"], label="6-Month AI Forecast", color="#ff7f0e", linestyle="--", marker="o")
plt.fill_between(forecast_df["Forecast_Date"], forecast_df["Lower_Bound_95"], forecast_df["Upper_Bound_95"], color="#ff7f0e", alpha=0.2, label="Confidence Range")
plt.title("6-Month Revenue Forecast (Holt-Winters Seasonal Model)", fontsize=13, fontweight="bold")
plt.ylabel("Monthly Revenue (£)")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/charts/04_sales_6m_forecast.png", dpi=300)
plt.close()

print("Saved all EDA charts, RFM segments, and 6-month forecast CSVs!")
EOF

python src/02_eda_rfm_forecast.py
