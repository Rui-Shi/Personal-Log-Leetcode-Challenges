SELECT u.city,
COUNT(DISTINCT t.order_id) AS order_num
FROM users u
INNER JOIN traders t
on u.user_id = t.user_id
GROUP BY u.city
ORDER BY order_num DESC
LIMIT 3;