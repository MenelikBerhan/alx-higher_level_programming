--  lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT title FROM
tv_shows
EXCEPT
SELECT s.title
FROM tv_shows s
    INNER JOIN tv_show_genres tv
        ON s.id = tv.show_id
WHERE tv.genre_id = (SELECT id FROM tv_genres WHERE name = 'Comedy')
ORDER BY title;
