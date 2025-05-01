from collections import deque
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid or not grid[0]:  # Handle empty board cases
            return 0
        
        nrows = len(grid)
        ncols = len(grid[0])
        visited = set()  # Keep track of visited cells
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # Possible movement directions
        area_max = 0
        
        def bfs_helper(r, c):
            nonlocal visited, area_max
            
            q = deque([(r, c)])
            visited.add((r, c))
            
            island = []
            
            while q:
                row, col = q.popleft()
                island.append([row, col])
                
                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc
                    if 0 <= new_row < nrows and 0 <= new_col < ncols and (new_row, new_col) not in visited and grid[new_row][new_col] == 1:
                        visited.add((new_row, new_col))
                        q.append((new_row, new_col))
            
            area_cur = len(island)
            area_max = area_cur if area_max < area_cur else area_max
        
        for r in range(nrows):
            for c in range(ncols):
                if (r, c) not in visited and grid[r][c] == 1:
                    bfs_helper(r, c)
        
        return area_max