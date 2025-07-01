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
        
        if not board or not board[0]:  # Handle empty board cases
            return

        nrows = len(board)
        ncols = len(board[0])
        visited = set()  # Keep track of visited cells
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # Possible movement directions

        def bfs(r, c):
            nonlocal visited
            q = deque([(r, c)])
            visited.add((r, c))
            surround = True
            region = []  # Store all cells in the connected 'O' region
            while q:
                r_cur, c_cur = q.popleft()
                region.append((r_cur, c_cur))
                
                if r_cur == 0 or r_cur == nrows - 1 or c_cur == 0 or c_cur == ncols - 1:
                    surround = False
                    
                for dr, dc in directions:
                    r_new = r_cur + dr
                    c_new = c_cur + dc
                    
                    if 0 <= r_new < nrows and 0 <= c_new < ncols and board[r_new][c_new] == 'O' and \
                        (r_new, c_new) not in visited:
                        visited.add((r_new, c_new))
                        q.append((r_new, c_new))
            if surround:
                for r, c in region:
                    board[r][c] = 'X'
                    
        # Iterate through the board, starting DFS from unvisited 'O' cells
        for r in range(nrows):
            for c in range(ncols):
                if (r, c) not in visited and board[r][c] == 'O':
                    bfs(r, c)

from typing import List
from collections import deque  # Using deque for efficient queue operations


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        nrow = len(board)
        ncol = len(board[0])
        
        if nrow == 1 or ncol == 1:
            return
        
        visited = set()
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        
        def bfs_helper(r, c):
            nonlocal visited
            q = deque([(r, c)])
            surrounded = True
            region = []
            
            while q:
                r, c = q.popleft()
                if r == 0 or r == nrow - 1 or c == 0 or c == ncol - 1:
                    surrounded = False
                
                visited.add((r, c))
                region.append((r, c))
                
                for dr, dc in directions:
                    r_new = r + dr
                    c_new = c + dc
                
                    if 0 <= r_new < nrow and 0 <= c_new < ncol and board[r_new][c_new] == 'O' and \
                            (r_new, c_new) not in visited:
                                q.append((r_new, c_new))
                         
            if surrounded:
                for r, c in region:
                    board[r][c] = "X"
        
        for r in range(nrow):
            for c in range(ncol):
                if (r, c) not in visited and board[r][c] == "O":
                    bfs_helper(r, c)
                
                
                
            
                
        
        
                             
                
            
            
            