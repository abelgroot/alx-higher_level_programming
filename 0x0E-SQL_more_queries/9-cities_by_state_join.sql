-- Query to list all cities along with their respective states
-- The results are sorted by cities.id in ascending order
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
