-- a script that lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT t.title, IFNULL(SUM(r.rate), 0) AS rating
FROM tv_shows AS t
LEFT JOIN tv_show_ratings AS r
ON t.id = r.show_id
GROUP BY t.title
ORDER BY rating DESC;
