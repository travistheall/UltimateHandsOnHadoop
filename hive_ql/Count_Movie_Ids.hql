SELECT movieid, count(movieid) as ratingCount
FROM ratings
GROUP BY movieid
ORDER BY ratingCount
DESC;