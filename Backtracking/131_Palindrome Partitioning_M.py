# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

 

# Example 1:

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:

# Input: s = "a"
# Output: [["a"]]
 

# Constraints:

# 1 <= s.length <= 16
# s contains only lowercase English letters.

# Time O(n*2^n)
# Space: Pali_list: O(n), res: O(n*2^n)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack_helper(Pali_list, start):
            if start == len(s):
                res.append(Pali_list)
                return
            
            for i in range(start, len(s)):
                str = s[start:(i+1)]
                if str == str[::-1]: # if it is a Palindrome, add to the list
                    backtrack_helper(Pali_list + [str[:]], i + 1)
        
        backtrack_helper([], 0)
        
        return res
                