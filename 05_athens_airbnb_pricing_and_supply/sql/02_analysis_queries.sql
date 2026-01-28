-- Average price by neighborhood (bar chart)
SELECT neighborhood, ROUND(AVG(price_eur),2) AS avg_price_eur, COUNT(*) AS listings
FROM athens_listings
GROUP BY neighborhood
ORDER BY avg_price_eur DESC;

-- Supply density by neighborhood (map bubble sizing)
SELECT neighborhood, COUNT(*) AS listings
FROM athens_listings
GROUP BY neighborhood
ORDER BY listings DESC;

-- Room type mix by neighborhood
SELECT neighborhood, room_type, COUNT(*) AS listings
FROM athens_listings
GROUP BY neighborhood, room_type
ORDER BY neighborhood, listings DESC;
