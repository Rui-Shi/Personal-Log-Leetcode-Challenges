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