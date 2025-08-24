# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
 

# Example 1:


# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
# Example 2:

# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

import collections
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Determines if a 9x9 Sudoku board is valid according to the rules.

        Args:
            board: A 9x9 list of lists of strings, where each string is 
                   a digit '1'-'9' or '.' for empty cells.

        Returns:
            True if the board is valid according to the rules for filled cells, 
            False otherwise.
        """

        # Use sets to efficiently check for duplicates
        rows = collections.defaultdict(set)  # Dictionary where keys are row indices (0-8) and values are sets of digits found in that row
        cols = collections.defaultdict(set)  # Dictionary where keys are col indices (0-8) and values are sets of digits found in that col
        boxes = collections.defaultdict(set) # Dictionary where keys are box indices (0-8) and values are sets of digits found in that box
        
        for r in range(9):
            for c in range(9):
                
                # Calculate the index for the 3x3 box
                # Integer division groups rows/cols into blocks of 3 (0,1,2 -> 0; 3,4,5 -> 1; 6,7,8 -> 2)
                # box_idx = (r // 3) * 3 + (c // 3) maps (row, col) to a unique box index 0-8
                # Example: (0,0) -> box 0; (1,4) -> box 1; (4,7) -> box 5; (8,8) -> box 8
                box_idx = (r // 3) * 3 + (c // 3)
                
                digit = board[r][c]

                if digit == ".":
                    continue
                
                if digit in rows[r]:
                    return False
                
                if digit in cols[c]:
                    return False
                
                if digit in boxes[box_idx]:
                    return False
                
            rows[r].add(digit)
            cols[c].add(digit)
            boxes[box_idx].add(digit)        

        # If the loops complete without finding any duplicates, the board is valid
        return True

# Time: O(1): loop through 81 cells O(81)
# Space: O(1): each dic store up to 81 elements: O(81) for each and O(243) in total. 
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                box_id = (r // 3) * 3 + c // 3
            
            digit = board[r][c]
            
            if digit == ".":
                    continue
                
            elif digit in rows[r] or digit in cols[c] or digit in boxes[box_id]:
                return False
            
            else:
                rows[r].add(digit)
                cols[c].add(digit)     
                boxes[box_id].add(digit)
        
        return True   
                    