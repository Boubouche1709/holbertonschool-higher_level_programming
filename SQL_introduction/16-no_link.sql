-- Lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
-- Only rows where the name column contains a value.
-- Results display score and name, sorted by descending score.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
