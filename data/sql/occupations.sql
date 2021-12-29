BEGIN;

DROP TABLE IF EXISTS occupations;
CREATE TABLE occupations
(
    id   integer NOT NULL,
    name varchar(255),
    PRIMARY KEY (id)
);
INSERT INTO occupations
VALUES (1, 'Administrator'),
       (2, 'Artist'),
       (3, 'Doctor'),
       (4, 'Educator'),
       (5, 'Engineer'),
       (6, 'Entertainment'),
       (7, 'Executive'),
       (8, 'Healthcare'),
       (9, 'Homemaker'),
       (10, 'Lawyer'),
       (11, 'Librarian'),
       (12, 'Marketing'),
       (13, 'None'),
       (14, 'Other'),
       (15, 'Programmer'),
       (16, 'Retired'),
       (17, 'Salesman'),
       (18, 'Scientist'),
       (19, 'Student'),
       (20, 'Technician'),
       (21, 'Writer');

COMMIT;