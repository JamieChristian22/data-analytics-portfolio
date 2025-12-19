# ============================================
# Multi-Domain Analytics – Python EDA Pipeline
# Netflix | Traffic | Sales
# Author: Jamie Christian
# ============================================

import pandas as pd
import numpy as np

# --------------------
# NETFLIX ANALYSIS
# --------------------
netflix = pd.read_csv("netflix_titles_clean.csv")

# Basic checks
print(netflix.info())
print(netflix.isna().mean().sort_values(ascending=False))

# Titles by type
titles_by_type = netflix.groupby("type")["show_id"].nunique()

# Titles by year added
titles_by_year = (
    netflix.dropna(subset=["date_added_year"])
           .groupby("date_added_year")["show_id"]
           .nunique()
           .sort_index()
)

# Ratings distribution
ratings_dist = netflix["rating"].value_counts()

# --------------------
# TRAFFIC ANALYSIS
# --------------------
traffic = pd.read_csv("mn_interstate_traffic_clean.csv")

traffic["date_time_parsed"] = pd.to_datetime(traffic["date_time_parsed"])

# Monthly traffic
monthly_traffic = (
    traffic.groupby("month_name")["traffic_volume"]
           .mean()
           .sort_values(ascending=False)
)

# Hourly traffic
hourly_traffic = traffic.groupby("hour")["traffic_volume"].mean()

# Weather impact
weather_traffic = traffic.groupby("weather_main")["traffic_volume"].mean()

# Holiday vs non-holiday
holiday_traffic = traffic.groupby("holiday")["traffic_volume"].mean()

# --------------------
# SALES / PROFITABILITY
# --------------------
sales = pd.read_csv("sales_profitability_clean.csv")

# KPI calculations
total_sales = sales["Sales"].sum()
total_profit = sales["Profit"].sum()
profit_ratio = total_profit / total_sales

# Segment performance
segment_sales = sales.groupby("Segment")["Sales"].sum()
segment_profit = sales.groupby("Segment")["Profit"].sum()

# Category margin
category_margin = (
    sales.groupby("Category")
         .apply(lambda x: x["Profit"].sum() / x["Sales"].sum())
)

# --------------------
# EXPORT SUMMARY
# --------------------
summary = {
    "Total Sales": total_sales,
    "Total Profit": total_profit,
    "Profit Ratio": profit_ratio
}

summary_df = pd.DataFrame.from_dict(summary, orient="index", columns=["Value"])
summary_df.to_csv("python_kpi_summary.csv")

print("Python EDA complete. KPIs exported.")