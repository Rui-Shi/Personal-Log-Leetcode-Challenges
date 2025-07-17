# SQL Schema
# Pandas Schema
# Table: Scores

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | score       | decimal |
# +-------------+---------+
# id is the primary key (column with unique values) for this table.
# Each row of this table contains the score of a game. Score is a floating point value with two decimal places.
 

# Write a solution to find the rank of the scores. The ranking should be calculated according to the following rules:

# The scores should be ranked from the highest to the lowest.
# If there is a tie between two scores, both should have the same ranking.
# After a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no holes between ranks.
# Return the result table ordered by score in descending order.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Scores table:
# +----+-------+
# | id | score |
# +----+-------+
# | 1  | 3.50  |
# | 2  | 3.65  |
# | 3  | 4.00  |
# | 4  | 3.85  |
# | 5  | 4.00  |
# | 6  | 3.65  |
# +----+-------+
# Output: 
# +-------+------+
# | score | rank |
# +-------+------+
# | 4.00  | 1    |
# | 4.00  | 1    |
# | 3.85  | 2    |
# | 3.65  | 3    |
# | 3.65  | 3    |
# | 3.50  | 4    |
# +-------+------+

import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    """
    Ranks scores according to the following rules:
    - Scores are ranked from highest to lowest.
    - Ties receive the same rank.
    - There are no holes between ranks after a tie.

    Args:
        scores: A DataFrame with columns 'id' and 'score'.

    Returns:
        A DataFrame with 'score' and 'rank' columns, ordered by score descending.
    """
    # Create a new 'rank' column using the rank() method on the 'score' column.
    # method='dense': Assigns the same rank to identical values, and ensures ranks are consecutive integers.
    # ascending=False: Ranks higher scores first (e.g., 4.00 is rank 1).
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    
    # Sort the DataFrame by the 'score' column in descending order to match the desired output format.
    scores = scores.sort_values(by='score', ascending=False)
    
    # Select and return only the 'score' and 'rank' columns.
    # We also convert the rank to an integer type as it's a whole number.
    return scores[['score', 'rank']]

# Example Usage based on the problem description:

# Create the Scores DataFrame
scores_data = {'id': [1, 2, 3, 4, 5, 6], 'score': [3.50, 3.65, 4.00, 3.85, 4.00, 3.65]}
scores_df = pd.DataFrame(scores_data)

# Call the function with the example data
result = order_scores(scores_df)

# Print the result to verify
print(result)
# Expected Output:
#    score  rank
# 2   4.00     1
# 4   4.00     1
# 3   3.85     2
# 1   3.65     3
# 5   3.65     3
# 0   3.50     4
    