SELECT n.title, count(r.movieid) as ratingCount
FROM ratings r
JOIN names n
ON r.movieid = n.movieid
GROUP BY n.title
HAVING ratingCount > 10
ORDER BY ratingCount DESC;