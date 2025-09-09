SELECT user_id,
COUNT(DISTINCT product_id) AS total_product
FROM user_transactions
GROUP BY user_id
HAVING SUM(spend) >= 1000 -- Corrected line
ORDER BY total_product DESC
LIMIT 10;

