-- lists all the cities of California that can be found in the database hbtn_0d_usa

SELECT C.id, C.name FROM cities AS C
WHERE C.state_id = (SELECT S.id FROM states AS S WHERE S.name = 'California');
