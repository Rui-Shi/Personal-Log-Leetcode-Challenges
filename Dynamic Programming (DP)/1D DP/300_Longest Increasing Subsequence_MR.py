# Given an integer array nums, return the length of the longest strictly increasing subsequence.

 

# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 104

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            v = nums[i]
            for j in range(i):
                v2 = nums[j]
                if v2 < v:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Calculates the Length of the Longest Increasing Subsequence (LIS).
        
        Let A be the input array `nums`.
        Let L(i) be the length of the LIS ending at index i.
        
        The recurrence relation is:
        L(i) = 1 + max({L(j) | 0 <= j < i and A[j] < A[i]} U {0})
        
        The final answer is max(L).
        """
        n = len(nums)
        if n == 0:
            return 0
            
        # dp[i] represents L(i), the length of the LIS ending at nums[i].
        # Initialize L(i) = 1 for all i, as each element is an LIS of length 1.
        dp = [1] * n
        
        # Iterate through each element of the array to compute L(i).
        for i in range(n):
            # Let v = A[i]
            v = nums[i]
            
            # Find max({L(j) | 0 <= j < i and A[j] < A[i]}).
            # Iterate through all previous elements to find the best subsequence to extend.
            for j in range(i):
                # Let v2 = A[j]
                v2 = nums[j]
                
                # The condition: A[j] < A[i]
                if v2 < v:
                    # Update L(i) = max(L(i), 1 + L(j))
                    dp[i] = max(dp[i], dp[j] + 1)
                    
        # The result is max(L) for all i from 0 to n-1.
        return max(dp)