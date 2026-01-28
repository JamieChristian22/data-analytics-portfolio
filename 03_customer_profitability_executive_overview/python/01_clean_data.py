import pandas as pd
import numpy as np

RAW_PATH = "../data/raw/orders_raw.csv"
OUT_PATH = "../data/clean/orders_clean.csv"

df = pd.read_csv(RAW_PATH).drop_duplicates(subset=["order_id"])

df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
df = df.dropna(subset=["order_date"])

df["state"] = df["state"].astype(str).str.title()
df["discount"] = pd.to_numeric(df["discount"], errors="coerce").fillna(0.0)
df["sales"] = pd.to_numeric(df["sales"], errors="coerce").fillna(0.0)
df["profit"] = pd.to_numeric(df["profit"], errors="coerce")

med_margin = (df.dropna(subset=["profit"])
                .assign(margin=lambda d: d["profit"] / d["sales"].replace(0, np.nan))
                .groupby("category")["margin"]
                .median())

missing = df["profit"].isna()
df.loc[missing, "profit"] = (df.loc[missing, "sales"] * df.loc[missing, "category"].map(med_margin).fillna(0.12)).round(2)

df["profit_ratio"] = np.where(df["sales"]!=0, (df["profit"] / df["sales"]).round(4), 0.0)
df["profit_per_order"] = df["profit"]
df["sales_per_customer"] = df.groupby("customer_id")["sales"].transform("sum").round(2)
df["year"] = df["order_date"].dt.year.astype(int)
df["month"] = df["order_date"].dt.to_period("M").astype(str)

df.to_csv(OUT_PATH, index=False)
print(f"Saved cleaned dataset to: {OUT_PATH}")
