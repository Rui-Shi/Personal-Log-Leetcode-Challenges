# Given a binary array nums, you should delete one element from it.

# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

# Example 1:

# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
# Example 2:

# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
# Example 3:

# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = 1 # number of zero allowed
        n = len(nums)
        
        l = 0
        
        for r in range(n):
            if nums[r] == 0:
                k -= 1
            
            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
        return r - l
    
s = Solution()
nums = [1,1,0,0,1,0,1,0,0,1]
print(s.longestSubarray(nums))
                
        
        
        