-- lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0
-- ordered by score in descending order
SELECT ST.SCORE, ST.NAME FROM second_table ST WHERE score >= 10 ORDER BY SCORE DESC;