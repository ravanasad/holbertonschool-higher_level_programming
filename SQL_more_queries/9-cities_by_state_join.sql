-- lists all cities contained in the database hbtn_0d_usa

SELECT C.id, C.name, S.name FROM cities C
JOIN states S
ON S.id = C.state_id