-- Script to count the number of records with the same score and sort by the count
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
