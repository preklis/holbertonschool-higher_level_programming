-- This is an SQL script

SELECT score, COUNT(*) as number
FROM second_table
GROUP BY score
ORDER BY number DESC;
