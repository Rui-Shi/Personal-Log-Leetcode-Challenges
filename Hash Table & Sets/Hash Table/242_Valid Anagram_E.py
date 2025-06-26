# Given two strings s and t, return true if t is an 
# anagram
#  of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = defaultdict(int)
        t_count = defaultdict(int)
        
        for char in s:
            s_count[char] += 1
        
        for char in t:
            t_count[char] += 1
        
        return s_count == t_count # check if two dicts are the same
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        