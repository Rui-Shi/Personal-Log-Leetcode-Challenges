# SQL Schema
# Pandas Schema
# Table: Employee

# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | salary      | int  |
# +-------------+------+
# id is the primary key (column with unique values) for this table.
# Each row of this table contains information about the salary of an employee.
 

# Write a solution to find the second highest distinct salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

# The result format is in the following example.

 

# Example 1:

# Input: 
# Employee table:
# +----+--------+
# | id | salary |
# +----+--------+
# | 1  | 100    |
# | 2  | 200    |
# | 3  | 300    |
# +----+--------+
# Output: 
# +---------------------+
# | SecondHighestSalary |
# +---------------------+
# | 200                 |
# +---------------------+
# Example 2:

# Input: 
# Employee table:
# +----+--------+
# | id | salary |
# +----+--------+
# | 1  | 100    |
# +----+--------+
# Output: 
# +---------------------+
# | SecondHighestSalary |
# +---------------------+
# | null                |
# +---------------------+

import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    """
    Finds the second highest distinct salary from the Employee table.

    Args:
        employee: A DataFrame with columns 'id' and 'salary'.

    Returns:
        A new DataFrame with a single column 'SecondHighestSalary' containing
        the second highest salary, or None if it does not exist.
    """
    # Remove duplicate salaries to consider only distinct values
    unique_salaries = employee['salary'].drop_duplicates()
    
    # Check if there are at least two unique salaries
    if len(unique_salaries) < 2:
        # If not, there is no second highest salary
        return pd.DataFrame({'SecondHighestSalary': [None]})
    else:
        # Sort the unique salaries in descending order and get the second one (at index 1)
        second_highest = unique_salaries.nlargest(2).iloc[-1]
        return pd.DataFrame({'SecondHighestSalary': [second_highest]})