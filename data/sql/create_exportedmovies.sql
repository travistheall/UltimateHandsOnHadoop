BEGIN;

use movielens;
CREATE TABLE exported_movies
(
    id           integer,
    title        varchar(255),
    release_date date,
    PRIMARY KEY (id)
);

COMMIT;
