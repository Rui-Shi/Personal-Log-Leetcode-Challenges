SELECT user_id,
COUNT(tweet_id) AS total_post
FROM tweets
WHERE tweet_data >='2020-01-01'
AND tweet_data <'2021-01-01'
GROUP BY user_id;