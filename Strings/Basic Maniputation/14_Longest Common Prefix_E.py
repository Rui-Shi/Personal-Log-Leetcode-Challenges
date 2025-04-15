# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length_min = min(map(len, strs)) # efficient way to find the length of the shortest string within a list of strings

        if length_min == 0: return ""
        i = 0
        while i < length_min:
            letter = strs[0][i]
            for str in strs:
                if str[i] != letter: return str[0:i]
            i += 1
        return strs[0][0:length_min] # Handle cases where the loop finishes