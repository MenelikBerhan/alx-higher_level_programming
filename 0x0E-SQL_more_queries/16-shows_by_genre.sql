-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT s.title, g.name
FROM tv_shows s
    LEFT JOIN tv_show_genres tv
        ON s.id = tv.show_id
    LEFT JOIN tv_genres g
        ON tv.genre_id = g.id
ORDER BY s.title, g.name;
