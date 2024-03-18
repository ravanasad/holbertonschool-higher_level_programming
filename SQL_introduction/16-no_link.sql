-- lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server
SELECT ST.SCORE, ST.NAME FROM second_table ST 
WHERE NAME != ""
ORDER BY `score` DESC;