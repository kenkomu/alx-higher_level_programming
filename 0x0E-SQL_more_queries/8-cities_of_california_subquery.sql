-- lists all the cities of California that can be found in the database
SELECT c.id, c.name FROM cities c INNER JOIN states s ON c.state_id = s.id WHERE s.name = 'California';
