--  lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT s.title
FROM tv_genres g
    INNER JOIN tv_show_genres tv
        ON g.id = tv.genre_id
    INNER JOIN tv_shows s
        ON tv.show_id = s.id
WHERE g.name = 'Comedy'
ORDER BY s.title;
