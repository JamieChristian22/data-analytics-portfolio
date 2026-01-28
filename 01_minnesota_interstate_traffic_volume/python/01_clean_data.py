import pandas as pd

RAW_PATH = "../data/raw/traffic_volume_2018_raw.csv"
OUT_PATH = "../data/clean/traffic_volume_2018_clean.csv"

df = pd.read_csv(RAW_PATH)
df["date_time"] = pd.to_datetime(df["date_time"], errors="coerce")
df = df.dropna(subset=["date_time"]).drop_duplicates(subset=["date_time"])

df["weather_main"] = df["weather_main"].fillna(df["weather_main"].mode()[0])
df["temp_f"] = pd.to_numeric(df["temp_f"], errors="coerce").fillna(df["temp_f"].median())
df["traffic_volume"] = pd.to_numeric(df["traffic_volume"], errors="coerce").interpolate().fillna(df["traffic_volume"].median()).round().astype(int)
df["holiday"] = df["holiday"].fillna("None")

df["year"] = df["date_time"].dt.year
df["month"] = df["date_time"].dt.month
df["day"] = df["date_time"].dt.day
df["hour"] = df["date_time"].dt.hour
df["day_name"] = df["date_time"].dt.day_name()
df["is_weekend"] = df["date_time"].dt.dayofweek.isin([5,6]).astype(int)

df.to_csv(OUT_PATH, index=False)
print(f"Saved cleaned dataset to: {OUT_PATH}")
