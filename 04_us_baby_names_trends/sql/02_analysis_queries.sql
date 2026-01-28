-- Top 10 female names (sum across years)
SELECT name, SUM(occurrences) AS occurrences
FROM baby_names
WHERE gender='F'
GROUP BY name
ORDER BY occurrences DESC
LIMIT 10;

-- Top 10 male names (sum across years)
SELECT name, SUM(occurrences) AS occurrences
FROM baby_names
WHERE gender='M'
GROUP BY name
ORDER BY occurrences DESC
LIMIT 10;

-- Yearly trend for a specific name (parameterize)
-- Example: 'Mary'
SELECT year, gender, SUM(occurrences) AS occurrences
FROM baby_names
WHERE name = 'Mary'
GROUP BY year, gender
ORDER BY year;
