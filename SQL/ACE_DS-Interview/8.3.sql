SELECT 
SUM(IF(device_type = "laptop", 1, 0)) AS laptop_view,
SUM(IF(device_type = "phone" OR device_type = "tablet"), 1, 0) AS mobile_view
FROM viewership