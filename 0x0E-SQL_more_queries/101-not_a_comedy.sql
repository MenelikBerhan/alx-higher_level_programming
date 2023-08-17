--  lists all shows without the genre Comedy in the database hbtn_0d_tvshows.

-- SELECT title FROM
-- tv_shows
-- EXCEPT
-- SELECT s.title
-- FROM tv_shows s
--     INNER JOIN tv_show_genres tv
--         ON s.id = tv.show_id
-- WHERE tv.genre_id = (SELECT id FROM tv_genres WHERE name = 'Comedy')
-- ORDER BY title;
SELECT DISTINCT s.title
FROM tv_shows s
    LEFT JOIN tv_show_genres tv
    ON s.id = tv.show_id
    LEFT JOIN tv_genres g
    ON tv.genre_id = g.id

    WHERE tv.show_id NOT IN (SELECT t.show_id FROM tv_show_genres t WHERE t.genre_id = 
    (SELECT tv_genres.id FROM tv_genres WHERE tv_genres.name = "Comedy"))
    ;
