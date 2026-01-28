import pandas as pd

DATA_PATH = "../data/clean/orders_clean.csv"
df = pd.read_csv(DATA_PATH, parse_dates=["order_date"])

kpis = {
    "Sales": df["sales"].sum(),
    "Profit": df["profit"].sum(),
    "Profit Ratio": df["profit"].sum() / df["sales"].sum(),
    "Profit per Order": df["profit"].mean(),
    "Sales per Customer": df.groupby("customer_id")["sales"].sum().mean(),
    "Avg Discount": df["discount"].mean(),
    "Quantity": df["quantity"].sum()
}
print("Executive KPIs")
for k,v in kpis.items():
    print(k, round(v, 4))

print("\nTop 10 states by profit:")
print(df.groupby("state")["profit"].sum().sort_values(ascending=False).head(10))

print("\nMonthly sales trend:")
print(df.groupby(df["order_date"].dt.to_period("M"))["sales"].sum().tail(12))
