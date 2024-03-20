-- Lists all genres from the database hbtn_0d_tvshows along with the number of
-- shows linked to each.
-- Does not display genres without linked shows.
-- Records are ordered by descending number of shows linked.

SELECT G.name AS 'genre', COUNT(*) AS 'number_of_shows' 
FROM tv_genres G
    INNER JOIN tv_show_genres tsg
    ON G.id = TSG.genre_id
GROUP BY G.name
ORDER BY COUNT(*) DESC;