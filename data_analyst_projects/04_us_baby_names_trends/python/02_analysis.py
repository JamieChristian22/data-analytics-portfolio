import pandas as pd

DATA_PATH = "../data/clean/baby_names_clean.csv"
df = pd.read_csv(DATA_PATH)

# Top 10 names overall by total occurrences
top = (df.groupby(["gender","name"])["occurrences"].sum()
         .reset_index()
         .sort_values("occurrences", ascending=False)
         .groupby("gender")
         .head(10))

print("Top 10 names by gender:")
print(top)

# Trend for the top male + top female
top_m = top[top["gender"]=="M"].iloc[0]["name"]
top_f = top[top["gender"]=="F"].iloc[0]["name"]

trend = df[df["name"].isin([top_m, top_f])].pivot_table(index="year", columns=["gender","name"], values="occurrences", aggfunc="sum")
print("\nTrend sample:")
print(trend.tail(10))
