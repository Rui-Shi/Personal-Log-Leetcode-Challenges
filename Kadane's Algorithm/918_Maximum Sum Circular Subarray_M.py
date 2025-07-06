# Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

# A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

# A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

 

# Example 1:

# Input: nums = [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3.
# Example 2:

# Input: nums = [5,-3,5]
# Output: 10
# Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
# Example 3:

# Input: nums = [-3,-2,-3]
# Output: -2
# Explanation: Subarray [-2] has maximum sum -2.
 

# Constraints:

# n == nums.length
# 1 <= n <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104

from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        Calculates the maximum possible sum of a non-empty subarray of a circular array.
        """
        # Case 1: Find the maximum subarray sum for a non-circular array.
        # This is the standard Kadane's Algorithm.
        max_so_far = -float('inf')
        max_ending_here = 0
        for num in nums:
            max_ending_here += num
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
            if max_ending_here < 0:
                max_ending_here = 0

        # Case 2: Find the minimum subarray sum to calculate the circular max.
        # The logic is the same as Kadane's but tracks the minimum sum.
        min_so_far = float('inf')
        min_ending_here = 0
        for num in nums:
            min_ending_here += num
            if min_so_far > min_ending_here:
                min_so_far = min_ending_here
            if min_ending_here > 0:
                min_ending_here = 0

        total_sum = sum(nums)
        
        # If all numbers are negative, max_so_far will be the largest negative number.
        # The circular sum (total_sum - min_so_far) would incorrectly be 0.
        # In this case, the non-circular max is the answer.
        if max_so_far < 0:
            return max_so_far

        # The result is the maximum of the non-circular sum and the circular sum.
        # Circular sum = total_sum - (minimum subarray sum)
        return max(max_so_far, total_sum - min_so_far)
                
            
            
            