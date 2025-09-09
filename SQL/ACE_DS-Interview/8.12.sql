WITH trans_2020 AS (
    SELECT *
    FROM prodect_spend
    WHERE CAST(transaction_date AS DATE) >= '2020-01-01' -- it is better to use single quote for string and date
    AND CAST(transaction_date AS DATE) < '2021-01-01'
)

SELECT category_id, product_id, SUM(spend) AS total_grossing
FROM trans_2020
GROUP BY category_id, product_id
ORDER BY total_grossing DESC
LIMIT 3;