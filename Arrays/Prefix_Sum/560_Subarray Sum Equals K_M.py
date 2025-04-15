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
        n = len(nums)
        count = 0  # Initialize the count of subarrays.
        curr_sum = 0  # Initialize the current cumulative sum.
        sum_freq = defaultdict(int)  # Dictionary to store frequencies of cumulative sums. creates a dictionary-like object where, 
        # if you try to access a key that doesn't exist, it automatically creates that key and assigns it a default value of 0.
        sum_freq[0] = 1  # Initialize with a frequency of 1 for a sum of 0 (important for subarrays starting at index 0).

        for i in range(n):
            curr_sum += nums[i]  # Update the current cumulative sum.

            # If (curr_sum - k) is present in sum_freq, it means there's a previous subarray
            # whose sum, when added to k, equals curr_sum.  Therefore, the subarray between
            # that previous point and the current index has a sum of k.
            if curr_sum - k in sum_freq:
                count += sum_freq[curr_sum - k]

            # Update the frequency of the current cumulative sum.
            sum_freq[curr_sum] += 1  # Increment the frequency. Using defaultdict avoids KeyError.

        return count