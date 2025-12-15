-- Business Question: Identify key performance drivers
SELECT category, SUM(revenue) revenue, SUM(profit) profit
FROM data GROUP BY category;