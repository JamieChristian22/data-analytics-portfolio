-- Movies vs TV Shows
SELECT type, COUNT(*) AS titles
FROM netflix_titles
GROUP BY type
ORDER BY titles DESC;

-- Ratings distribution
SELECT rating, COUNT(*) AS titles
FROM netflix_titles
GROUP BY rating
ORDER BY titles DESC;

-- Top 10 genres
SELECT primary_genre, COUNT(*) AS titles
FROM netflix_titles
GROUP BY primary_genre
ORDER BY titles DESC
LIMIT 10;

-- Titles added by year and type
SELECT year_added, type, COUNT(*) AS titles
FROM netflix_titles
GROUP BY year_added, type
ORDER BY year_added, type;

-- Country concentration (map inputs)
SELECT country, COUNT(*) AS titles
FROM netflix_titles
GROUP BY country
ORDER BY titles DESC;
