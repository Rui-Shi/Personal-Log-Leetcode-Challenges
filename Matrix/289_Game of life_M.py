# According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.

# Given the current state of the board, update the board to reflect its next state.

# Note that you do not need to return anything.

 

# Example 1:


# Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
# Example 2:


# Input: board = [[1,1],[1,0]]
# Output: [[1,1],[1,1]]
 

# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 25
# board[i][j] is 0 or 1.

# Follow up:

# Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?

from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        # We need to solve this in-place, which means we cannot use a copy of the board
        # to store the next state. The challenge is that all cells must be updated
        # simultaneously based on the *original* state of the board.
        #
        # To achieve this, we can use intermediate states to mark the cells.
        # The original states are 0 (dead) and 1 (live).
        #
        # Let's introduce two new states:
        # -1: A live cell that will die in the next state (1 -> 0)
        #  2: A dead cell that will become live in the next state (0 -> 1)
        
        m = len(board)
        n = len(board[0])
        
        # Helper function to count live neighbors for a given cell.
        # A neighbor is considered "live" if its original state was 1.
        # Since we are modifying the board, we check abs(value) == 1,
        # because a cell marked as -1 was originally 1.
        def count_live_neighbors(r, c):
            count = 0
            # Iterate through the 8 neighbors of the cell (r, c)
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    # Check for boundary conditions and skip the cell itself
                    if (i == r and j == c) or i < 0 or j < 0 or i >= m or j >= n:
                        continue
                    
                    # If the neighbor was originally live (i.e., 1 or -1)
                    if abs(board[i][j]) == 1:
                        count += 1
            return count

        # --- Phase 1: Mark cells for their next state ---
        for r in range(m):
            for c in range(n):
                live_neighbors = count_live_neighbors(r, c)
                
                # Rule 1 & 3: Any live cell with < 2 or > 3 live neighbors dies.
                if board[r][c] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        # Mark as a live cell that will die.
                        board[r][c] = -1
                
                # Rule 4: Any dead cell with exactly 3 live neighbors becomes a live cell.
                elif board[r][c] == 0:
                    if live_neighbors == 3:
                        # Mark as a dead cell that will become live.
                        board[r][c] = 2

        # --- Phase 2: Apply the changes to the final state ---
        # Now, update the board to the final 0s and 1s.
        for r in range(m):
            for c in range(n):
                # A cell that was live and is now dying becomes dead.
                if board[r][c] == -1:
                    board[r][c] = 0
                # A cell that was dead and is now reviving becomes live.
                elif board[r][c] == 2:
                    board[r][c] = 1

from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        nrow = len(board)
        ncol = len(board[0])
        
        def neighbor_count(r, c):
            count = 0
            # Iterate through all 8 neighbors and the cell itself
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    # Check for boundary conditions AND ensure it's not the cell itself
                    if i >= 0 and i < nrow and j >= 0 and j < ncol and (i, j) != (r, c):
                        if board[i][j] == 1:
                            count += 1
            return count

        change_grid = [[0 for _ in range(ncol)] for _ in range(nrow)]
        
        for i in range(nrow):
            for j in range(ncol):
                nei_count = neighbor_count(i, j)
                
                # Rule 4: A dead cell with exactly three live neighbours becomes a live cell.
                if board[i][j] == 0 and nei_count == 3:
                    change_grid[i][j] = 1 # Becomes alive
                
                elif board[i][j] == 1 and (nei_count == 2 or nei_count == 3):
                    change_grid[i][j] = 1 # Stays alive

        for i in range(nrow):
            for j in range(ncol):
                board[i][j] = change_grid[i][j]