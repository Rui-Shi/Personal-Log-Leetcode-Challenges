# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

# Example 1:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Example 2:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
# Example 3:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
 

# Constraints:

# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        nrow = len(board)
        ncol = len(board[0])
        
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        
        def backtrack_dfs(cur_row, cur_col, visited, cur_str, target):
            if cur_str == target:
                return True
            
            else:
                n = len(cur_str)
                
                for dr, dc in directions:
                    r_new = cur_row + dr
                    c_new = cur_col + dc
                    
                    if 0 <= r_new < nrow and 0 <= c_new < ncol and (r_new, c_new) not in visited \
                        and board[r_new][c_new] == target[n]:
                            visited.add((r_new, c_new))
                            if backtrack_dfs(r_new, c_new, visited, cur_str + board[r_new][c_new], target):
                                return True
                            visited.remove((r_new, c_new))
            return False
        
        for i in range(nrow):
            for j in range(ncol):
                if board[i][j] == word[0]:
                    if backtrack_dfs(i, j, set([(i, j)]), board[i][j], word):
                        return True
        
        return False
    

# a better one:

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        nrow = len(board)
        ncol = len(board[0])
        # Use a single set for the entire search path
        path = set()

        def backtrack_dfs(r, c, i):
            # i is the index in 'word' we're looking for
            
            # Base Case: Success
            if i == len(word):
                return True
            
            # Failure cases (out of bounds, wrong char, or already visited)
            if (r < 0 or c < 0 or
                r >= nrow or c >= ncol or
                word[i] != board[r][c] or
                (r, c) in path):
                return False

            # --- Backtracking Logic ---
            # 1. Choose: Add the current cell to the path
            path.add((r, c))
            
            # 2. Explore: Recurse in all 4 directions for the next character (i + 1)
            res = (backtrack_dfs(r + 1, c, i + 1) or
                   backtrack_dfs(r - 1, c, i + 1) or
                   backtrack_dfs(r, c + 1, i + 1) or
                   backtrack_dfs(r, c - 1, i + 1))
            
            # 3. Un-choose: Remove the cell to backtrack for other paths
            path.remove((r, c))
            
            return res

        # Start the search from every cell on the board
        for r in range(nrow):
            for c in range(ncol):
                if backtrack_dfs(r, c, 0):
                    return True
        
        return False
                
                        