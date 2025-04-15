# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107

from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cum_sum = 0
        sum_freq = defaultdict(int)
        sum_freq[0] = 1
        count = 0
        
        for i in range(n):
            cum_sum += nums[i]
        
            if cum_sum - k in sum_freq:
                count += sum_freq[cum_sum - k]
            sum_freq[cum_sum] += 1 # no need to check if the key exist with "defaultdict"
        
        return count