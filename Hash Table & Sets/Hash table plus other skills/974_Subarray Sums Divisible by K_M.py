# Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

# A subarray is a contiguous part of an array.

 

# Example 1:

# Input: nums = [4,5,0,-2,-3,1], k = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by k = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
# Example 2:

# Input: nums = [5], k = 9
# Output: 0

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        
        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += nums[j]
                if curr_sum % k == 0:
                    count += 1
        return count
    
# a better solution:

from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum_counts = defaultdict(int)
        prefix_sum_counts[0] = 1  # Initialize count for remainder 0 to 1 (empty subarray)
        curr_sum = 0
        count = 0

        for num in nums:
            curr_sum = (curr_sum + num) % k  # Keep track of prefix sum modulo k
            # Crucially, curr_sum can be negative in python. Add k to bring it to non-negative
            if curr_sum < 0:
                curr_sum += k

            count += prefix_sum_counts[curr_sum]  # Add counts of previous same remainders
            prefix_sum_counts[curr_sum] += 1     # Increment count for current remainder

        return count