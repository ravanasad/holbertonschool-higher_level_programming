-- lists all shows contained in hbtn_0d_tvshows

SELECT TS.title, TSG.genre_id FROM tv_shows TS
JOIN tv_show_genres TSG
ON TS.id = TSG.show_id
ORDER BY TS.title, TSG.genre_id