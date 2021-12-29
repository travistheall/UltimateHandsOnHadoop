SELECT m.title, COUNT(r.movie_id) AS ratingCount
FROM movies m
INNER JOIN ratings r
ON m.id = r.movie_id
GROUP BY m.title
ORDER BY ratingCount;