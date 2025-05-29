# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

 

# Example 1:


# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
# Example 2:

# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        dp = list(grid)
        for i in range(1, len(dp[0])):
            dp[0][i] += dp[0][i - 1]
        
        for j in range(1, len(dp)):
            dp[j][0] += dp[j - 1][0]
            
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] += min(dp[i - 1][j], dp[i][j - 1])
        
        return dp[-1][-1]