WITH daily_tweet_counts AS (
  -- Step 1: Count the number of tweets for each user per day.
  SELECT
    user_id,
    CAST(tweet_date AS DATE) AS tweet_day, -- CAST is a SQL function that converts a value from one data type to another.
    COUNT(tweet_id) AS tweet_count
  FROM
    tweets
  GROUP BY
    user_id,
    CAST(tweet_date AS DATE)
)
-- Step 2: Calculate the 7-day rolling average from the daily counts.
SELECT
  user_id,
  tweet_day,
  AVG(tweet_count) OVER (
    PARTITION BY
      user_id
    ORDER BY
      tweet_day ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
  ) AS rolling_avg_7_days
FROM
  daily_tweet_counts
ORDER BY
  user_id,
  tweet_day;





WITH daily_tweet_counts AS (
    SELECT
    user_id,
    CAST(tweet_date AS DATE) AS tweet_day,
    COUNT(tweet_id) AS tweet_count

    FROM tweets

    GROUP BY
    user_id,
    CAST(tweet_date AS DATE)
)

SELECT
user_id,
tweet_day,
AVG(tweet_count) OVER (
    PARTITION BY
    user_id
    ORDER BY
    tweet_day ROWS BETWEEN 6 PRECEDING and 
    CURRENT ROW -- select the preceding 6 rows and current rows
) AS rolling_ave_7
FROM daily_tweet_counts
ORDER BY
  user_id,
  tweet_day;