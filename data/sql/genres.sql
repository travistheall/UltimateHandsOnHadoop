BEGIN;

DROP TABLE IF EXISTS genres;
CREATE TABLE genres
(
    id   integer NOT NULL,
    name varchar(255),
    PRIMARY KEY (id)
);
INSERT INTO genres
VALUES (1, 'Action'),
       (2, 'Adventure'),
       (3, 'Animation'),
       (4, 'Children''s'),
       (5, 'Comedy'),
       (6, 'Crime'),
       (7, 'Documentary'),
       (8, 'Drama'),
       (9, 'Fantasy'),
       (10, 'Film-Noir'),
       (11, 'Horror'),
       (12, 'Musical'),
       (13, 'Mystery'),
       (14, 'Romance'),
       (15, 'Sci-Fi'),
       (16, 'Thriller'),
       (17, 'War'),
       (18, 'Western');
       
COMMIT;