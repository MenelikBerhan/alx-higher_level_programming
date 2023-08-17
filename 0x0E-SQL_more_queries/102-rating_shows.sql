-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating
FROM tv_show_ratings, tv_shows
WHERE tv_show_ratings.show_id = tv_shows.id
GROUP BY tv_show_ratings.show_id
ORDER BY rating DESC;
