import pandas as pd
import numpy as np

RAW_PATH = "../data/raw/netflix_titles_raw.csv"
OUT_PATH = "../data/clean/netflix_titles_clean.csv"

df = pd.read_csv(RAW_PATH).drop_duplicates(subset=["show_id"])

df["country"] = df["country"].fillna("Unknown").astype(str).str.strip().str.title()
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce").fillna(pd.to_datetime("2019-01-01"))
df["year_added"] = df["date_added"].dt.year.astype(int)
df["month_added"] = df["date_added"].dt.month.astype(int)

missing = df["duration"].isna() | (df["duration"].astype(str).str.strip() == "")
df.loc[missing & (df["type"]=="Movie"), "duration"] = "90 min"
df.loc[missing & (df["type"]=="TV Show"), "duration"] = "1 Season"

def parse_minutes(x: str):
    x = str(x)
    return int(x.split()[0]) if "min" in x else np.nan

def parse_seasons(x: str):
    x = str(x)
    return int(x.split()[0]) if "Season" in x else np.nan

df["duration_min"] = df["duration"].apply(parse_minutes)
df["seasons"] = df["duration"].apply(parse_seasons)
df["primary_genre"] = df["listed_in"].astype(str).str.split(",").str[0].str.strip()

df.to_csv(OUT_PATH, index=False)
print(f"Saved cleaned dataset to: {OUT_PATH}")
