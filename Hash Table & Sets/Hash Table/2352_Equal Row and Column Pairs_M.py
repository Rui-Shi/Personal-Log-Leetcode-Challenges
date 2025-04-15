# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

# A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

 

# Example 1:


# Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
# Output: 1
# Explanation: There is 1 equal row and column pair:
# - (Row 2, Column 1): [2,7,7]
# Example 2:


# Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
# Output: 3
# Explanation: There are 3 equal row and column pairs:
# - (Row 0, Column 0): [3,1,2,2]
# - (Row 2, Column 2): [2,4,2,2]
# - (Row 3, Column 2): [2,4,2,2]
 

# Constraints:

# n == grid.length == grid[i].length
# 1 <= n <= 200
# 1 <= grid[i][j] <= 105

import numpy as np
from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        matrix = np.array(grid)
        hash_table = {}
        count = 0

        for row in matrix:
            # Convert NumPy array to a tuple for hashing
            row_tuple = tuple(row)
            if row_tuple not in hash_table:
                hash_table[row_tuple] = 1
            else:
                hash_table[row_tuple] += 1  # Increment count if row already exists

        for col in matrix.T:
            # Convert NumPy array to a tuple for lookup
            col_tuple = tuple(col)
            if col_tuple in hash_table:
                count += hash_table[col_tuple]  # Add the count of matching rows

        return count

# Hashable Keys (Tuples): 
# Lists are mutable and therefore not hashable. 
# You cannot use a list as a key in a dictionary.  
# The most common and efficient solution is to convert the NumPy arrays (rows and columns) 
# to tuples before using them as keys. Tuples are immutable and hashable.