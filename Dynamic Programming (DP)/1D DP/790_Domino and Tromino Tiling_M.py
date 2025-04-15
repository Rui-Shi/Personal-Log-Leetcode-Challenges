# You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.


# Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.

# In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

 

# Example 1:


# Input: n = 3
# Output: 5
# Explanation: The five different ways are show above.
# Example 2:

# Input: n = 1
# Output: 1

class Solution:
    def numTilings(self, n: int) -> int:
        # the number of ways to tile are 1, 2, 5 when n = 1, 2, 3
        dp = [1, 2, 5, 16]
        
        for i in range(4, n):
            num = dp[i-4] * 16 + dp[i-3] * 5 + dp[i-2] * 2 + dp[i-3] * 1
            dp.append[num]
            
        return dp[n-1]