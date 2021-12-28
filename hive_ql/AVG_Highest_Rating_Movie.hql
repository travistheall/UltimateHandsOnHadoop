SELECT r.movieid, n.title, avg(r.rating) as avg_rating, count(r.movieid) as ratingCount
FROM ratings r
JOIN names n
ON r.movieid = n.movieid
GROUP BY r.movieid, n.title
HAVING ratingCount > 10
ORDER BY avg_rating DESC;