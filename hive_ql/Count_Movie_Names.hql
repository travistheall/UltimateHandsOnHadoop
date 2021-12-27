SELECT n.name as movieName, count(r.movie_id) as ratingCount
FROM ratings r
JOIN movie_names n
ON r.movie_id = n.movie_id
GROUP BY n.name
ORDER BY ratingCount DESC;