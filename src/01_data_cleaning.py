cat << 'EOF' > src/01_data_cleaning.py
import pandas as pd
import numpy as np
import os

os.makedirs("data/processed", exist_ok=True)

# Load raw Kaggle dataset
raw_path = "data/raw/online_retail_II.csv"
print("Loading raw dataset...")
df = pd.read_csv(raw_path, encoding="latin-1")

# Standardize column names (handles 'Customer ID' vs 'CustomerID')
df.columns = [c.strip().replace(" ", "_") for c in df.columns]
if "CustomerID" in df.columns:
    df.rename(columns={"CustomerID": "Customer_ID"}, inplace=True)

print(f"Raw rows: {len(df):,}")

# 1. Remove exact duplicates
df.drop_duplicates(inplace=True)

# 2. Clean types
df["Invoice"] = df["Invoice"].astype(str).str.strip()
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["Customer_ID"] = df["Customer_ID"].dropna().astype(str).str.replace(".0", "", regex=False)

# 3. Separate Cancellations ('C' prefix) from Valid Transactions
is_cancelled = df["Invoice"].str.startswith("C")
returns_df = df[is_cancelled & (df["Price"] > 0)].copy()
returns_df["Return_Value"] = (returns_df["Quantity"] * returns_df["Price"]).abs()

# 4. Filter Valid Sales (Non-cancelled, Quantity > 0, Price > 0)
non_product_codes = ["POST", "DOT", "M", "BANK CHARGES", "ADJUST", "ADJUST2", "D", "CRUK"]
sales_df = df[
    (~is_cancelled) &
    (df["Quantity"] > 0) &
    (df["Price"] > 0) &
    (~df["StockCode"].isin(non_product_codes))
].copy()

# 5. Feature Engineering
sales_df["Revenue"] = sales_df["Quantity"] * sales_df["Price"]
sales_df["Year"] = sales_df["InvoiceDate"].dt.year
sales_df["Month"] = sales_df["InvoiceDate"].dt.month
sales_df["YearMonth"] = sales_df["InvoiceDate"].dt.to_period("M").astype(str)
sales_df["Date"] = sales_df["InvoiceDate"].dt.date

# Save processed datasets
sales_df.to_csv("data/processed/sales_clean.csv", index=False)
returns_df.to_csv("data/processed/returns_clean.csv", index=False)

print(f"Clean valid sales rows: {len(sales_df):,}")
print(f"Clean return/cancellation rows: {len(returns_df):,}")
print("Saved to data/processed/ successfully!")
EOF

python src/01_data_cleaning.py
