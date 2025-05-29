# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

# You have the following three operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character
 

# Example 1:

# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# Example 2:

# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        # Create a DP table of size (n+1) x (m+1)
        # dp[i][j] will store the minimum operations to convert word1[:i] to word2[:j]
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Initialize the DP table
        # If word2 is empty, convert word1[:i] to "" by deleting i characters
        for i in range(n + 1):
            dp[i][0] = i
        
        # If word1 is empty, convert "" to word2[:j] by inserting j characters
        for j in range(m + 1):
            dp[0][j] = j

        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # If characters match, no operation needed for these characters
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # Characters don't match, consider insert, delete, or replace
                    # 1 + min(insert, delete, replace)
                    dp[i][j] = 1 + min(dp[i][j - 1],    # Insert (from word1[:i] to word2[:j-1], then insert word2[j-1])
                                       dp[i - 1][j],    # Delete (from word1[:i-1] to word2[:j], then delete word1[i-1])
                                       dp[i - 1][j - 1]) # Replace (from word1[:i-1] to word2[:j-1], then replace word1[i-1] with word2[j-1])
        
        return dp[n][m]
    

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        
        for i in range(n + 1):
            dp[i][0] = i
        
        for j in range(m + 1):
            dp[0][j] = j
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j - 1],
                                       dp[i - 1][j],
                                       dp[i - 1][j - 1])
        return dp[n][m]
        