# LeetCode 159, "Longest Substring with At Most Two Distinct Characters," is a problem that challenges you to find the length of the longest possible contiguous substring within a given string that contains no more than two unique characters.

# Problem Breakdown
# Input: A string, s.

# Goal: Find the maximum length of a substring of s.

# Constraint: The substring must contain at most two different characters.

# For instance:

# If the input is "eceba", the longest substring that meets the criteria is "ece", which has a length of 3 (the distinct characters are 'e' and 'c').

# If the input is "ccaabbb", the longest substring is "aabbb", with a length of 5 (the distinct characters are 'a' and 'b').

# Time: O(n)
# Space: O(n)

import collections

class solution:
    def LongestSubstring(self, s):
        
        if len(s) <= 2:
            return len(s)
        
        count_dict = collections.defaultdict()
        
        left = 0
        max_length = 0
        for right in range(len(s)):
            char = s[right]
            count_dict[char] += 1
            
            while count_dict[char] > 2:
                count_dict[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length
            
            
# Time: O(n)
# Space: O(1) (count_dict will never hold more than 3 keys)

import collections

class solution:
    def LongestSubstring(self, s):
        
        if len(s) <= 2:
            return len(s)
        
        count_dict = collections.defaultdict(int)
        
        left = 0
        max_length = 0
        for right in range(len(s)):
            char_right = s[right]
            count_dict[char_right] += 1
            
            while len(count_dict) > 2:
                char_left = s[left]
                count_dict[char_left] -= 1
                
                if count_dict[char_left] <= 0:
                    del count_dict[char_left]
                
                left += 1
                    
            max_length = max(max_length, right - left + 1)
        
        return max_length