-- Monthly traffic volume (line chart)
SELECT year, month, SUM(traffic_volume) AS monthly_traffic
FROM traffic_volume
GROUP BY year, month
ORDER BY year, month;

-- Traffic by weather type (bar chart)
SELECT weather_main, SUM(traffic_volume) AS total_traffic
FROM traffic_volume
GROUP BY weather_main
ORDER BY total_traffic DESC;

-- Hour-of-day heatmap inputs (avg by day-of-month + hour)
SELECT EXTRACT(MONTH FROM date_time) AS month,
       EXTRACT(DAY FROM date_time)   AS day,
       hour,
       AVG(traffic_volume)           AS avg_traffic
FROM traffic_volume
GROUP BY month, day, hour
ORDER BY month, day, hour;

-- Holiday impact (compare holiday vs non-holiday)
SELECT CASE WHEN holiday <> 'None' THEN 'Holiday' ELSE 'Non-Holiday' END AS day_type,
       AVG(traffic_volume) AS avg_traffic
FROM traffic_volume
GROUP BY day_type;
