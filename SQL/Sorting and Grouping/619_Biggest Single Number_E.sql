-- Table: MyNumbers

-- +-------------+------+
-- | Column Name | Type |
-- +-------------+------+
-- | num         | int  |
-- +-------------+------+
-- This table may contain duplicates (In other words, there is no primary key for this table in SQL).
-- Each row of this table contains an integer.
--  

-- A single number is a number that appeared only once in the MyNumbers table.

-- Find the largest single number. If there is no single number, report null.

-- The result format is in the following example.

--  

-- Example 1:

-- Input: 
-- MyNumbers table:
-- +-----+
-- | num |
-- +-----+
-- | 8   |
-- | 8   |
-- | 3   |
-- | 3   |
-- | 1   |
-- | 4   |
-- | 5   |
-- | 6   |
-- +-----+
-- Output: 
-- +-----+
-- | num |
-- +-----+
-- | 6   |
-- +-----+
-- Explanation: The single numbers are 1, 4, 5, and 6.
-- Since 6 is the largest single number, we return it.
-- Example 2:

-- Input: 
-- MyNumbers table:
-- +-----+
-- | num |
-- +-----+
-- | 8   |
-- | 8   |
-- | 7   |
-- | 7   |
-- | 3   |
-- | 3   |
-- | 3   |
-- +-----+
-- Output: 
-- +------+
-- | num  |
-- +------+
-- | null |
-- +------+
-- Explanation: There are no single numbers in the input table so we return null.

# Write your MySQL query statement below

-- you can solve this by finding all single numbers, ordering them from largest to smallest, and then taking the first one using LIMIT 1
-- SELECT (...) AS num: The entire query is wrapped as a scalar subquery. If the inner query finds a number, it's returned. If the inner query finds no single numbers and returns an empty set, the scalar subquery evaluates to NULL, satisfying the problem's requirement.
SELECT
    (
        SELECT
            num
        FROM
            MyNumbers
        GROUP BY
            num
        HAVING
            COUNT(num) = 1
        ORDER BY
            num DESC
        LIMIT 1
    ) AS num;


-- To find the largest single number, you can first identify all numbers that appear only once and then select the maximum value from that group.

SELECT
    MAX(num) AS num
FROM
    (
        SELECT
            num
        FROM
            MyNumbers
        GROUP BY
            num
        HAVING
            COUNT(num) = 1
    ) AS single_numbers;