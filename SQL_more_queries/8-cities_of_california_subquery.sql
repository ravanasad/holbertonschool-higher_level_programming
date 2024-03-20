-- lists all the cities of California that can be found in the database hbtn_0d_usa

SELECT C.id, C.name FROM cities C
JOIN states S
ON S.id = C.state_id