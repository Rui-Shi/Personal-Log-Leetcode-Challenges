WITH ranked_tran AS (
    SELECT user_id,
    spend,
    transaction_date,
    ROW_NUMBER() OVER (
        PARTITION BY
        user_id
        ORDER BY
        transaction_date ASC
    ) AS time_rank
    FROM user_transactions
)

SELECT user_id,
spend
FROM ranked_tran
WHERE spend >= 50
AND time_rank = 1
