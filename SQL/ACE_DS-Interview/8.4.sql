SELECT product_id,
SUM(spend) OVER
(PARTITION BY product_id
ORDER BY trans_date)
AS cum_spend
FROM total_trans
