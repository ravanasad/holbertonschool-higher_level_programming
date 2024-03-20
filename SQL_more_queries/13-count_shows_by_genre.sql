-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each

SELECT G.name, COUNT(G.name) FROM tv_shows TS
JOIN tv_show_genres TSG
ON TS.id = TSG.show_id
JOIN tv_genres G
ON TSG.genre_id = G.id
GROUP BY G.name
ORDER BY COUNT(G.name) DESC;