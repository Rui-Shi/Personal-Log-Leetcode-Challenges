# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0  # Left pointer of the sliding window
        max_length = 0  # Stores the maximum length found so far
        char_set = set()  # Stores the characters in the current window (using a set for fast lookups)

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left]) # remove a element in a set
                left += 1
            
            char_set.add(s[right])
            max_length = max(max_length, len(char_set))
        return max_length
    
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        char_set = set()
        
        for right in range(len(s)):
            if s[right] not in char_set:
                char_set.add(s[right])
            
            else:
                while s[right] in char_set:
                    char_set.remove(s[left])
                    left += 1
                char_set.add(s[right])
            
            max_length = max(max_length, right - left + 1)
        
        return max_length
        
        

            
            

        