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

# My solution: O(n^2)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sum_cum = [nums[0]]
        for i in range(1, n):
            sum_cum.append(nums[i] + sum_cum[i - 1])
        sum_cum[:] = [0] + sum_cum[:]
        
        res = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                if sum_cum[j] - sum_cum[i] == k:
                    res += 1
        return res

# A better one in O(n)
from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        sum_freq = defaultdict(int)
        sum_freq[0] = 1
        cum_sum = 0
        
        freq = 0
        
        for num in nums:
            cum_sum += num
            sum_freq[cum_sum] += 1
            
            complement = cum_sum - k
            if complement in sum_freq:
                freq += sum_freq[complement]
            
        return freq

            
            
        
        