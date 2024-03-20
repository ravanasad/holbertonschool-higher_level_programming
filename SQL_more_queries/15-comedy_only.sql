-- lists all Comedy shows in the database

SELECT TS.title FROM tv_genres G
JOIN tv_show_genres TSG
ON G.id = TSG.genre_id
JOIN tv_shows TS
ON TSG.show_id = TS.id
WHERE G.name = 'Comedy'
ORDER BY TS.title ASC;