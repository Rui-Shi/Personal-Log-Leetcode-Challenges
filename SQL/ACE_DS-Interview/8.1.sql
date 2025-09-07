SELECT app_id,
SUM(IF(event_id = "click", 1, 0)) / COUNT(app_id) AS click_rate
FROM events
WHERE timestamp >= '2019-01-01'
AND timestamp < '2020-01-01' -- how to select date
GROUP BY app_id;