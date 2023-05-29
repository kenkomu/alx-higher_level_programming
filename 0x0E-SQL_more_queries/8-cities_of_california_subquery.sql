-- lists all the cities of California that can be found in the database
USE hbtn_0d_usa;
SELECT cities.*
FROM cities, states
WHERE cities.state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY cities.id ASC;