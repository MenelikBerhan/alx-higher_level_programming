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
WHERE s.title NOT IN (
    SELECT s.title
    FROM tv_genres g
    INNER JOIN tv_show_genres tv
        ON g.id = tv.genre_id
    INNER JOIN tv_shows s
        ON tv.show_id = s.id
    WHERE g.name = 'Comedy'
)
ORDER BY s.title;
