import pandas as pd

DATA_PATH = "../data/clean/traffic_volume_2018_clean.csv"
df = pd.read_csv(DATA_PATH, parse_dates=["date_time"])

month_totals = (df.groupby(df["date_time"].dt.to_period("M"))["traffic_volume"]
                  .sum()
                  .reset_index()
                  .rename(columns={"date_time":"month"}))

weather_totals = (df.groupby("weather_main")["traffic_volume"]
                    .sum()
                    .sort_values(ascending=False))

hour_avg = df.groupby("hour")["traffic_volume"].mean().round(0)

print("Top weather categories by total traffic:")
print(weather_totals.head(10))
print("\nAvg traffic by hour:")
print(hour_avg)
