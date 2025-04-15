# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

# Example 1:


# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:

# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:

# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        
        nrow = len(grid)
        ncol = len(grid[0])
        
        q = deque() # the cell to explore
        
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
        
        while q:
            r, c, cur_step = q.popleft()
            for dr, dc in dirs:
                r_new = r + dr
                c_new = c + dc
                
                if 0<= r_new < nrow and 0<= c_new < ncol and grid[r_new][c_new] == 1:
                    grid[r_new][c_new] = 2
                    q.append((r_new, c_new, cur_step + 1))
        
        for row in grid:
            for element in row:
                if element == 1:
                    return -1
        try:
            return cur_step
        except NameError:
            return 0
                    
        
        
        
        