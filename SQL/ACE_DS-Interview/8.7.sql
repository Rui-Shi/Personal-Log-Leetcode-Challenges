SELECT
COUNT(DISTINCT user_id)
FROM (
    SELECT 
    user_id,
    RANK() OVER (
        PARTITION BY 
        user_id,
        product_id
        ORDER BY purchase_time
    ) AS purchase_num
    FROM purchases
) t
WHERE purchase_num = 2;
