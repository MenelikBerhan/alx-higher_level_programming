-- uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT g.name AS name
FROM tv_genres g
    INNER JOIN tv_show_genres tv
        ON g.id = tv.genre_id
EXCEPT
SELECT g.name
FROM tv_genres g
    INNER JOIN tv_show_genres tv
        ON g.id = tv.genre_id
WHERE tv.show_id = (SELECT s.id FROM tv_shows s WHERE s.title = 'Dexter')
ORDER BY name;
