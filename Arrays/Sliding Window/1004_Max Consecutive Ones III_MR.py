# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Example 2:

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=r=0
        max_len = 0 
        for r in range(len(nums)):
            if nums[r] == 0:
                k-=1
            while k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len

nums = [1,1,1,0,0,0,1,1,1,1,0,0,0,0]
s = Solution()
print(s.longestOnes(nums, 2))
                

        