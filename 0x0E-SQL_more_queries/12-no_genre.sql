-- a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT tvs.`title`, tvg.`genre_id`
  FROM `tv_shows` AS tvs
       LEFT JOIN `tv_show_genres` AS tvg
       ON tvs.`id` = tvg.`show_id`
       WHERE tvg.`genre_id` IS NULL
 ORDER BY tvs.`title`, tvg.`genre_id`;
