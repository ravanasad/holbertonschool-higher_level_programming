-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each

SELECT G.name AS 'genre', COUNT(G.name) AS 'number_of_shows' 
FROM tv_genres G
    INNER JOIN `tv_show_genres` AS t
    ON g.`id` = t.`genre_id`
GROUP BY G.name
ORDER BY COUNT(G.name) DESC;