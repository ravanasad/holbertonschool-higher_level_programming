-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter

SELECT G.name FROM tv_genres G
JOIN tv_show_genres TSG
ON G.id = TSG.genre_id
JOIN tv_shows TS
ON TSG.show_id = TS.id
WHERE TS.title = 'Dexter'
ORDER BY G.name ASC;