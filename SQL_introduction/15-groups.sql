-- lists the number of records with the same score in the table second_table of the database hbtn_0c_0
SELECT SCORE, COUNT(SCORE) FROM second_table GROUP BY SCORE ORDER BY SCORE DESC;