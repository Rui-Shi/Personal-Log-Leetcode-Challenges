# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

from typing import List
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        def bfs(r, c):
            q = deque([])
            visited.add((r, c))
            q.append((r, c))
            
            while q:
                row, col = q.popleft()
                
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and grid[r][c] == "1":
                        q.append((r, c))
                        visited.add((r, c))
                        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    bfs(r, c)
    
        return islands
    
# Dfs: O(N x M)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = {}
        count = 0
        nrow = len(grid)
        ncol = len(grid[0])

        def dfs_helper(r, c):
            nonlocal visited

            if grid[r][c] == "0":
                return
            else:
                visited[(r, c)] = 1
            for dr, dc in dir:
                r_new = r + dr
                c_new = c + dc
                if 0<=r_new<nrow and 0<=c_new<ncol and (r_new, c_new) not in visited and grid[r_new][c_new] == "1":
                    dfs_helper(r_new, c_new)


        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == "1" and (i, j) not in visited:
                    count += 1
                    dfs_helper(i, j)
        return count
            