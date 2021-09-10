.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet
  FROM students
  WHERE color = "blue" and pet = "dog";

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song
  FROM students
  WHERE color = "blue" and pet = "dog";


CREATE TABLE matchmaker AS
  SELECT a.pet, a.song, a.color, b.color
  FROM students as a, students as b
  WHERE a.pet = b.pet and
        a.song = b.song and
        a.time < b.time;


CREATE TABLE sevens AS
  SELECT s.seven
  FROM students as s, numbers as n
  WHERE s.number = 7 and
        n."7" = "True" and
        s.time = n.time;


CREATE TABLE favpets AS
  SELECT pet, COUNT(*) as count
  FROM students
  GROUP BY pet
  ORDER BY count DESC
  LIMIT 10;

CREATE TABLE dog AS
  SELECT pet, count
  FROM favpets
  WHERE pet = "dog";


CREATE TABLE bluedog_agg AS
  SELECT song, COUNT(*) as count
  FROM bluedog_songs
  GROUP BY song
  ORDER BY count DESC;

CREATE TABLE instructor_obedience AS
  SELECT seven, instructor, COUNT(*)
  FROM students
  WHERE seven = '7'
  GROUP BY instructor;

