WITH groupby_date AS (
    SELECT
    transaction_id,
    product_id,
    user_id,
    spend,
    RANK() OVER (
        PARTITION BY
        user_id

        ORDER BY
        CAST(transaction_date AS DATE) DESC
    ) AS days_rank
    FROM user_transactions
)

SELECT
transaction_date,
COUNT(DISTINCT user_id) AS user_count,
COUNT(product_id) AS product_count
FROM groupby_date
WHERE days_rank = 1
GROUP BY transaction_date
ORDER BY transaction_date DESC;
