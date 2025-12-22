import pandas as pd

RAW_PATH = "../data/raw/athens_listings_raw.csv"
OUT_PATH = "../data/clean/athens_listings_clean.csv"

df = pd.read_csv(RAW_PATH).drop_duplicates(subset=["listing_id"])

df["neighborhood"] = df["neighborhood"].fillna("Unknown").astype(str).str.strip().str.title()

df["price_eur"] = (df["price_eur"].astype(str)
                   .str.replace("€","", regex=False)
                   .str.replace(",","", regex=False))
df["price_eur"] = pd.to_numeric(df["price_eur"], errors="coerce")

p99 = df["price_eur"].quantile(0.99)
df["price_eur"] = df["price_eur"].clip(upper=p99).round(2)

df["minimum_nights"] = pd.to_numeric(df["minimum_nights"], errors="coerce").fillna(1).astype(int)
df["number_of_reviews"] = pd.to_numeric(df["number_of_reviews"], errors="coerce").fillna(0).astype(int)
df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")

df.to_csv(OUT_PATH, index=False)
print(f"Saved cleaned dataset to: {OUT_PATH}")
