-- Query to list all cities of California from the cities table
-- The state_id is determined by a subquery that retrieves the id of California
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
