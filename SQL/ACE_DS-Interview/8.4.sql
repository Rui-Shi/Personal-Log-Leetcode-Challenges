SELECT product_id,
SUM(spend),
MAX(trans_date) AS date
FROM total_trans
GROUP BY product_id
ORDER BY date DESC



SELECT product_id,
SUM(spend) OVER
(PARTITION BY product_id
ORDER BY trans_date)
AS cum_spend
FROM total_trans
