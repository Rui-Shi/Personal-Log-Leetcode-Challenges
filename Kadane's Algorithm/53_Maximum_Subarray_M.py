# Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # `max_ending_here` stores the max sum of a subarray ending at the current position.
        max_ending_here = 0
        
        # `max_so_far` stores the overall maximum sum found so far.
        # It's initialized to negative infinity to handle arrays of all negative numbers.
        max_so_far = -float('inf')
        
        for num in nums:
            # Add the current number to the current subarray sum.
            max_ending_here += num
            
            # Update the overall maximum sum if the current subarray sum is greater.
            max_so_far = max(max_so_far, max_ending_here)
            
            # If the current subarray sum is negative, it won't contribute to a larger
            # future sum, so we start a new subarray by resetting it to 0.
            if max_ending_here < 0:
                max_ending_here = 0
                
        return max_so_far