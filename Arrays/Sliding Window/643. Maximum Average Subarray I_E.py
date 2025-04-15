# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000
 

# Constraints:

# n == nums.length
# 1 <= k <= n <= 105
# -104 <= nums[i] <= 104

# Instead of recalculating the sum for each window, 
# we update the sum by subtracting the element that's leaving the window and adding the element that's entering the window.
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        # Initialize the sum of the first 'k' elements.
        current_sum = sum(nums[0:k])
        res = current_sum / k  # Initialize 'res' with the average of the first 'k' elements

        # Iterate through the array using a sliding window approach.
        for i in range(1, len(nums) - k + 1):
            # Efficiently update the sum: subtract the outgoing element and add the incoming element.
            current_sum = current_sum - nums[i - 1] + nums[i + k - 1]
            avg_temp = current_sum / k  # Calculate the average of the current window.
            
            # Update 'res' if the current average is greater.
            if res < avg_temp:
                res = avg_temp

        return res

        