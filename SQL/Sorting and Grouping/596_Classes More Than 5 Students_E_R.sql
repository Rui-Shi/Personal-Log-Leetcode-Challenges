-- SQL Schema
-- Pandas Schema
-- Table: Courses

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | student     | varchar |
-- | class       | varchar |
-- +-------------+---------+
-- (student, class) is the primary key (combination of columns with unique values) for this table.
-- Each row of this table indicates the name of a student and the class in which they are enrolled.
--  

-- Write a solution to find all the classes that have at least five students.

-- Return the result table in any order.

-- The result format is in the following example.

# Write your MySQL query statement below

-- When filtering on aggregates, you must use the HAVING clause instead. 
-- Here's the corrected query:

SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(*) >= 5;

-- The error lies in the placement of the WHERE clause. In SQL, WHERE filters rows before they are grouped. When you want to filter groups based on aggregate functions (like COUNT(*)), you need to use the HAVING clause, which is specifically designed for filtering grouped results.

-- Here's a breakdown:

-- WHERE clause:
-- Filters individual rows before any grouping or aggregation occurs.
-- Cannot be used with aggregate functions because those functions operate on grouped data.
-- HAVING clause:
-- Filters groups after grouping and aggregation have been performed.
-- Is used to filter groups based on the results of aggregate functions.