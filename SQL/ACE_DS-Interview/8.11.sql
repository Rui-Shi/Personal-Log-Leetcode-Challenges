WITH tran_group_user AS (
    SELECT 
    user_id,
    spend,
    transaction_date,

    ROW_NUMBER() OVER (
        PARTITION BY 
        user_id

        ORDER BY
        CAST(transaction_date AS DATE) ASC
    ) AS tran_order
    FROM transactions
)

SELECT
user_id,
spend,
transaction_date
FROM tran_group_user
WHERE tran_order = 3;