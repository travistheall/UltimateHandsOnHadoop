CREATE VIEW IF NOT EXISTS avgRatings AS
SELECT movieid, avg(rating) as avgRating, count(movieid) as ratingCount
FROM ratings
GROUP BY movieid
ORDER BY avgRating DESC;

SELECT n.title, a.avgRating
FROM avgRatings a
JOIN names n 
ON a.movieid = n.movieid
WHERE a.ratingCount > 10;