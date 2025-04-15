# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

# Connect: A cell is connected to adjacent cells horizontally or vertically.
# Region: To form a region connect every 'O' cell.
# Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
# To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

 

# Example 1:

# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

# Explanation:


# In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

# Example 2:

# Input: board = [["X"]]

# Output: [["X"]]

 

# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.

from typing import List
from collections import deque  # Using deque for efficient queue operations

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Captures all 'O's surrounded by 'X's on a board.

        Args:
            board: The input board (modified in-place).
        """
        if not board or not board[0]:  # Handle empty board cases
            return

        nrows = len(board)
        ncols = len(board[0])
        visited = set()  # Keep track of visited cells
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # Possible movement directions

        def dfs(r, c):
            """
            Performs Depth-First Search to find connected 'O' regions.

            Args:
                r: Starting row.
                c: Starting column.
            """
            nonlocal visited  # Not strictly needed, but good practice
            q = deque([(r, c)])  # Use deque for efficient FIFO queue
            visited.add((r, c))
            is_surrounded = True  # Assume the region is surrounded initially

            region = []  # Store all cells in the connected 'O' region

            while q:
                row, col = q.popleft()  # Use popleft() for BFS
                region.append((row, col))


                # Check if the current cell is on the boundary
                if row == 0 or row == nrows - 1 or col == 0 or col == ncols - 1:
                    is_surrounded = False  # Not surrounded if on the boundary

                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc

                    # Check if the new coordinates are within bounds and haven't been visited
                    if 0 <= new_row < nrows and 0 <= new_col < ncols and \
                       (new_row, new_col) not in visited and board[new_row][new_col] == 'O':
                        visited.add((new_row, new_col))  # Mark as visited *before* adding to queue
                        q.append((new_row, new_col))  # Add to queue for further exploration

            # If the region is surrounded, flip all 'O's to 'X's
            if is_surrounded:
                for r, c in region:
                    board[r][c] = 'X'

        # Iterate through the board, starting DFS from unvisited 'O' cells
        for r in range(nrows):
            for c in range(ncols):
                if (r, c) not in visited and board[r][c] == 'O':
                    dfs(r, c)
                
        
        
                             
                
            
            
            