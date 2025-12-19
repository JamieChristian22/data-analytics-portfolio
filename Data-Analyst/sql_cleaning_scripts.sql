-- ==========================
-- CLEANING SCRIPTS (ALL DATASETS)
-- ==========================

-- NETFLIX CLEANING (SQL Server-style TRY_CONVERT; adapt as needed)
CREATE VIEW netflix_titles_clean AS
SELECT
  show_id,
  CASE
    WHEN LOWER(LTRIM(RTRIM(type))) = 'movie' THEN 'Movie'
    WHEN LOWER(LTRIM(RTRIM(type))) IN ('tv show','tvshow','tv') THEN 'TV Show'
    ELSE NULL
  END AS type,
  title,
  NULLIF(LTRIM(RTRIM(rating)),'') AS rating,
  release_year,
  COALESCE(
    TRY_CONVERT(date, date_added, 107),  -- "Month dd, yyyy"
    TRY_CONVERT(date, date_added, 101),  -- "mm/dd/yyyy"
    TRY_CONVERT(date, date_added, 23)    -- "yyyy-mm-dd"
  ) AS date_added,
  CASE
    WHEN LOWER(duration) LIKE '%season%' THEN TRY_CONVERT(int, LEFT(LTRIM(RTRIM(duration)), CHARINDEX(' ', LTRIM(RTRIM(duration))+' ') - 1))
    WHEN LOWER(duration) LIKE '%min%'    THEN TRY_CONVERT(int, LEFT(LTRIM(RTRIM(duration)), CHARINDEX(' ', LTRIM(RTRIM(duration))+' ') - 1))
    ELSE TRY_CONVERT(int, LTRIM(RTRIM(duration)))
  END AS duration_value,
  CASE
    WHEN LOWER(duration) LIKE '%season%' THEN 'Seasons'
    WHEN LOWER(duration) LIKE '%min%'    THEN 'Minutes'
    ELSE NULL
  END AS duration_unit,
  NULLIF(REPLACE(LTRIM(RTRIM(country)),' , ',', '),'') AS country,
  REPLACE(listed_in, '|', ',') AS listed_in,
  description
FROM netflix_titles_raw;


-- MINNESOTA INTERSTATE TRAFFIC CLEANING
CREATE VIEW mn_interstate_traffic_clean AS
SELECT
  COALESCE(
    TRY_CONVERT(datetime, date_time, 120), -- "yyyy-mm-dd hh:mi:ss"
    TRY_CONVERT(datetime, date_time, 101)  -- "mm/dd/yyyy hh:mi"
  ) AS date_time,
  CASE WHEN TRY_CONVERT(int, traffic_volume) < 0 THEN NULL ELSE TRY_CONVERT(int, traffic_volume) END AS traffic_volume,
  TRY_CONVERT(float, temp_f) AS temp_f,
  TRY_CONVERT(float, rain_1h) AS rain_1h,
  TRY_CONVERT(float, snow_1h) AS snow_1h,
  TRY_CONVERT(int, clouds_all) AS clouds_all,
  UPPER(LEFT(LOWER(NULLIF(weather_main,'')),1)) + SUBSTRING(LOWER(NULLIF(weather_main,'')),2,50) AS weather_main,
  COALESCE(NULLIF(holiday,''),'None') AS holiday
FROM mn_interstate_traffic_raw;


-- SALES + PROFITABILITY CLEANING
CREATE VIEW sales_profitability_clean AS
SELECT
  [Order ID],
  COALESCE(
    TRY_CONVERT(date, [Order Date], 101),
    TRY_CONVERT(date, [Order Date], 23),
    TRY_CONVERT(date, [Order Date], 120)
  ) AS order_date,
  UPPER(LEFT(LOWER(LTRIM(RTRIM([Region]))),1)) + SUBSTRING(LOWER(LTRIM(RTRIM([Region]))),2,50) AS region,
  LTRIM(RTRIM([State])) AS state,
  [Segment],
  [Category],
  [Sub-Category] AS sub_category,
  TRY_CONVERT(int, [Quantity]) AS quantity,
  CASE
    WHEN RIGHT(LTRIM(RTRIM([Discount])),1) = '%' THEN TRY_CONVERT(float, LEFT(LTRIM(RTRIM([Discount])), LEN(LTRIM(RTRIM([Discount])))-1))/100.0
    ELSE TRY_CONVERT(float, [Discount])
  END AS discount,
  TRY_CONVERT(float, [Sales]) AS sales,
  TRY_CONVERT(float, NULLIF([Profit],'')) AS profit,
  TRY_CONVERT(float, NULLIF([Profit],'')) / NULLIF(TRY_CONVERT(float,[Sales]),0) AS profit_ratio
FROM sales_profitability_raw;