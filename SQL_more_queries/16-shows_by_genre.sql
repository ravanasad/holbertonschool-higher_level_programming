-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows

SELECT TS.title, G.name FROM tv_genres G
JOIN tv_show_genres TSG
ON G.id = TSG.genre_id
RIGHT JOIN tv_shows TS
ON TSG.show_id = TS.id
ORDER BY TS.title ASC, G.name ASC;