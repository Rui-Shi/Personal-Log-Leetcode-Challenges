# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

# An interleaving of two strings s and t is a configuration where s and t are divided into n and m substrings respectively, such that:

# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
# Note: a + b is the concatenation of strings a and b.

 

# Example 1:


# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
# Explanation: One way to obtain s3 is:
# Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
# Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
# Since s3 can be obtained by interleaving s1 and s2, we return true.
# Example 2:

# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
# Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.
# Example 3:

# Input: s1 = "", s2 = "", s3 = ""
# Output: true

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False
        
        if not s1 and not s2 and not s3:
            return True
        
        s1_split = 0
        s2_split = 0
        
        i, j= 0, 0
        
        s1_cur = False
        s2_cur = False
        
        for k in range(n3):
            if i < n1 and s3[k] == s1[i]:
                if not s1_cur:
                    s1_split += 1
                    s1_cur = True
                    s2_cur = False
                i += 1
            
            elif j < n2 and s3[k] == s2[i]:
                if not s2_cur:
                    s2_split += 1
                    s2_cur = True
                    s1_cur = False
                j += 1
            
            else:
                return False
            
            print([i, j, k])
        
        return abs(s1_split - s2_split) <= 1

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        
        # If the lengths don't add up, it's impossible.
        if n1 + n2 != n3:
            return False
        
        # dp[i][j] is true if s1's first i chars and s2's first j chars
        # can interleave to form s3's first i+j chars.
        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]
        
        # Base case: two empty strings can form an empty string.
        dp[0][0] = True
        
        # Fill the first column (interleaving s1 with an empty s2)
        for i in range(1, n1 + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
            
        # Fill the first row (interleaving s2 with an empty s1)
        for j in range(1, n2 + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
            
        # Fill the rest of the DP table
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                # The current character in s3 we are trying to match
                s3_char = s3[i + j - 1]
                
                # Case 1: The current char of s3 matches s1's char, and the previous state (without this char) was valid.
                from_s1 = dp[i - 1][j] and s1[i - 1] == s3_char
                
                # Case 2: The current char of s3 matches s2's char, and the previous state (without this char) was valid.
                from_s2 = dp[i][j - 1] and s2[j - 1] == s3_char
                
                dp[i][j] = from_s1 or from_s2
                
        # The final answer is in the bottom-right cell of the DP table.
        return dp[n1][n2]

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        
        if n1 + n2 != n3:
            return False
        
        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]
        
        dp[0][0] = True
        
        for i in range(n1):
            dp[0][i] = dp[0][i - 1] and s1[i] == s3[i]
        
        for j in range(n2):
            dp[j][0] = dp[j - 1][0] and s2[j] == s3[j]
            
        for i in range(1, n1):
            for j in range(1, n2):
                from_s1 = dp[j][i - 1] and s1[i - 1] == s3[i + j -1]
                from_s2 = dp[j - 1][i] and s2[j - 1] == s3[i + j -1]
                
                dp[i][j] = from_s1 or from_s2
        
        return dp[n1][n2]
                
        