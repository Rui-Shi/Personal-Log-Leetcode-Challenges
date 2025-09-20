# Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

 

# Example 1:


# Input: n = 3
# Output: 5
# Example 2:

# Input: n = 1
# Output: 1
 

# Constraints:

# 1 <= n <= 19
 
# Time: O(n^2)
# Space: O(n)
class Solution:
    def numTrees(self, n: int) -> int:
        # The number of unique BSTs with n nodes is the n-th Catalan number.
        # We can calculate it iteratively using the formula:
        # C_i = C_{i-1} * 2 * (2*i - 1) / (i + 1)
        
        # Base case: C_0 = 1 (one way to have an empty tree)
        
        if n == 1:
            return 1
        
        dp = [0, 1]
        
        for i in range(2, n + 1): # i: the number of nodes in total
            new_count = 0
            for j in range(0, i): # j: the number of nodes on the left
                if j == 0 or j == i - 1:
                    new_count += dp[i-1]
                else:
                    new_count += dp[j] * dp[i-j-1]
            dp.append(new_count)
        return dp[-1]
        
        