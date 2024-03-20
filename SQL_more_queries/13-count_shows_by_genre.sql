-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each

SELECT G.name AS 'genre', COUNT(*) AS 'number_of_shows' 
FROM tv_genres G
    INNER JOIN tv_show_genres tsg
    ON G.id = TSG.genre_id
GROUP BY G.name
ORDER BY COUNT(*) DESC;