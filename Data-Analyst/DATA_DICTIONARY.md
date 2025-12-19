# Data Dictionary (Multi-Domain Analytics Pack)

## Files
- netflix_titles_raw.csv / netflix_titles_clean.csv
- mn_interstate_traffic_raw.csv / mn_interstate_traffic_clean.csv
- sales_profitability_raw.csv / sales_profitability_clean.csv
- sales_customer_map.csv (Order ID ↔ Customer ID for DAX)

## Netflix (raw)
- show_id (string): Unique title id
- type (string): Dirty in raw (Movie/TV Show variations)
- rating (string): TV-MA, TV-14, etc. (null/blank in raw)
- release_year (int)
- date_added (string): mixed formats in raw
- duration (string): "89 min", "2 Seasons", or missing units
- country (string): comma-separated list (spacing issues in raw)
- listed_in (string): genres (comma-separated or pipe-delimited in raw)

## Netflix (clean)
- date_added_parsed (date)
- duration_value (int)
- duration_unit ("Minutes" | "Seasons")
- date_added_year (int)

## Traffic (raw)
- date_time: mixed datetime formats
- traffic_volume: may include invalid negatives
- temp_f: may include text
- weather_main: sometimes lowercase
- holiday: sometimes blank

## Traffic (clean)
- date_time_parsed, year, month_name, hour, day
- holiday normalized to "None"

## Sales (raw)
- Discount may be percent strings (e.g., "15%")
- Sales may be stored as text
- Profit may be blank
- Region may be lowercase
- State may contain extra spaces

## Sales (clean)
- Order Date Parsed
- Profit Ratio (Profit/Sales)
- Year, Month