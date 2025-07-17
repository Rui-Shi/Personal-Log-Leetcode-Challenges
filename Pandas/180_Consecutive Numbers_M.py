# SQL Schema
# Pandas Schema
# Table: Logs

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | num         | varchar |
# +-------------+---------+
# In SQL, id is the primary key for this table.
# id is an autoincrement column starting from 1.
 

# Find all numbers that appear at least three times consecutively.

# Return the result table in any order.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Logs table:
# +----+-----+
# | id | num |
# +----+-----+
# | 1  | 1   |
# | 2  | 1   |
# | 3  | 1   |
# | 4  | 2   |
# | 5  | 1   |
# | 6  | 2   |
# | 7  | 2   |
# +----+-----+
# Output: 
# +-----------------+
# | ConsecutiveNums |
# +-----------------+
# | 1               |
# +-----------------+
# Explanation: 1 is the only number that appears consecutively for at least three times.

import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    """
    Finds all numbers that appear at least three times consecutively.

    Args:
        logs: A DataFrame with columns 'id' and 'num'.

    Returns:
        A DataFrame with a single column 'ConsecutiveNums' containing
        the numbers that appear at least three times consecutively.
    """
    # Create an empty list to store the consecutive numbers
    consecutive_nums = []
    
    # Check if the DataFrame has at least 3 rows
    if len(logs) >= 3:
        # Iterate through the DataFrame using a rolling window of size 3
        for i in range(len(logs) - 2):
            # Check if the number is the same in the current row and the next two rows
            if (logs['num'].iloc[i] == logs['num'].iloc[i+1] and 
                logs['num'].iloc[i+1] == logs['num'].iloc[i+2]):
                # Add the number to our list
                consecutive_nums.append(logs['num'].iloc[i])
    
    # Get the unique numbers from the list and create the result DataFrame
    result_df = pd.DataFrame({'ConsecutiveNums': pd.Series(consecutive_nums).unique()})
    
    return result_df

# Alternative, more "pandas-idiomatic" solution using shift:
def consecutive_numbers_optimized(logs: pd.DataFrame) -> pd.DataFrame:
    """
    Finds all numbers that appear at least three times consecutively using an optimized method.

    Args:
        logs: A DataFrame with columns 'id' and 'num'.

    Returns:
        A DataFrame with a single column 'ConsecutiveNums' containing
        the numbers that appear at least three times consecutively.
    """
    # Create boolean masks to check for equality with the previous and next row
    is_same_as_prev = logs['num'] == logs['num'].shift(1)
    is_same_as_next = logs['num'] == logs['num'].shift(-1)
    
    # Find the numbers where both conditions are true
    consecutive = logs[is_same_as_prev & is_same_as_next]['num'].unique()
    
    # Create the result DataFrame
    return pd.DataFrame({'ConsecutiveNums': consecutive})


# Example Usage based on the problem description:

# Create the Logs DataFrame
logs_data = {'id': [1, 2, 3, 4, 5, 6, 7], 'num': [1, 1, 1, 2, 1, 2, 2]}
logs_df = pd.DataFrame(logs_data)

# Call the function with the example data
result = consecutive_numbers_optimized(logs_df)

# Print the result to verify
print(result)
# Expected Output:
#    ConsecutiveNums
# 0                1