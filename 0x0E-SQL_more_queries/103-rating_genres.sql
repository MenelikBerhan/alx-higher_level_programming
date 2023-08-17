-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT g.name, SUM(tr.rate) AS rating
FROM tv_show_ratings tr, tv_shows s, tv_show_genres tv, tv_genres g
WHERE tr.show_id = s.id AND s.id = tv.show_id AND tv.genre_id = g.id
GROUP BY g.name
ORDER BY rating DESC;
