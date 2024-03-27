-- This SQL script lists all records of the second_table in my MySQL server from values name and score in Desc way

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
