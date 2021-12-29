BEGIN;

DROP TABLE IF EXISTS ratings;
CREATE TABLE ratings (
  id integer NOT NULL,
  user_id integer,
  movie_id integer,
  rating integer,
  rated_at timestamp,
  PRIMARY KEY (id)
);

COMMIT;