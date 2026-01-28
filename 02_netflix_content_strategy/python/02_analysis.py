import pandas as pd

DATA_PATH = "../data/clean/netflix_titles_clean.csv"
df = pd.read_csv(DATA_PATH, parse_dates=["date_added"])

print("Movies vs TV Shows:")
print(df["type"].value_counts())

print("\nTop 10 countries:")
print(df["country"].value_counts().head(10))

print("\nTop 10 primary genres:")
print(df["primary_genre"].value_counts().head(10))

print("\nTitles added by year (last 10 years):")
print(df.groupby("year_added")["show_id"].count().tail(10))
