-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT g.name
FROM tv_genres g
    INNER JOIN tv_show_genres tv
        ON g.id = tv.genre_id
    INNER JOIN tv_shows s
        ON tv.show_id = s.id
WHERE s.title = 'Dexter'
ORDER BY g.name;
