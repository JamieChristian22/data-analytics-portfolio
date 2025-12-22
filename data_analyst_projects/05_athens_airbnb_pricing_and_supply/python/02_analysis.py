import pandas as pd

DATA_PATH = "../data/clean/athens_listings_clean.csv"
df = pd.read_csv(DATA_PATH)

avg_price = (df.groupby("neighborhood")["price_eur"]
               .mean()
               .sort_values(ascending=False))

print("Top 10 neighborhoods by average price:")
print(avg_price.head(10).round(2))

supply = df["neighborhood"].value_counts().head(10)
print("\nTop 10 neighborhoods by listing count:")
print(supply)
