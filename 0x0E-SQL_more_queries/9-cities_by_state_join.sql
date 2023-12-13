--  a script that lists all cities contained in the database hbtn_0d_usa.
SELECT al.`id`, al.`name`, ooo.`name`
FROM `cities` AS al
INNER JOIN `states` AS ooo ON al.`state_id` = ooo.`id`
ORDER BY al.`id`;
