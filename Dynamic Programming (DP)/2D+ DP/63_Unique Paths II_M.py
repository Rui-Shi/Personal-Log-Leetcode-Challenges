# You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The testcases are generated so that the answer will be less than or equal to 2 * 109.

 

# Example 1:


# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
# Example 2:


# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1
 

# Constraints:

# m == obstacleGrid.length
# n == obstacleGrid[i].length
# 1 <= m, n <= 100
# obstacleGrid[i][j] is 0 or 1.

from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0 for _ in obstacleGrid[0]] for _ in obstacleGrid]
        
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                
                elif i == 0 and j == 0:
                    dp[i][j] = 1
                
                elif i == 0:
                    dp[i][j] = dp[i][j-1]
                
                elif j == 0:
                    dp[i][j] = dp[i-1][j]                  
                    
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[-1][-1]
                
# test cases:
s = Solution()
grid1 = [[0,0,0],[0,1,0],[0,0,0]]
grid2 = [[0,1],[0,0]]

print(s.uniquePathsWithObstacles(grid1))
print(s.uniquePathsWithObstacles(grid2))

from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0 for _ in obstacleGrid[0]] for _ in obstacleGrid]
        dp[0][0] = 1
        
        for i in len(obstacleGrid):
            for j in len(obstacleGrid[0]):
                
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                
                elif i == 0 and j == 0:
                    dp[i][j] = 1
                
                elif i == 0 or j == 0:
                    if i == 0:
                        dp[i][j] = dp[i][j - 1]
                    else:
                        dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[-1][-1]
                    
                