-- lists all shows contained in the database hbtn_0d_tvshows

SELECT TS.title, TSG.genre_id FROM tv_shows TS
LEFT JOIN tv_show_genres TSG
ON TS.id = TSG.show_id
ORDER BY TS.title, TSG.genre_id