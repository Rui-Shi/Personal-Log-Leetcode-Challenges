# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
 

# Constraints:

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105

# My solusion
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n # handle k > n
        nums_rotate = nums
        if k == 0: 
            return None
        for i in range(k):
            nums_rotate = [nums_rotate[-1]] + nums_rotate[:n-1]
        nums[:] = nums_rotate
        
# Better one
# Time complexity: O(n) ]
# Space complexity: O(n)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n # handle k > n
        nums[:] = nums[-k:] + nums[:-k]  # O(n) In-place modification using slice assignment "nums=..." does not work!!!
        # the space complexity of nums[-k:] + nums[:-k] is O(n)
         
# nums = ... (incorrect): This simply changes what the local variable nums (inside the function) points to. 
# It makes nums point to the same list object that nums_rotate points to. 
# The original list object that was passed into the function remains unchanged. 
# It's like changing a label, not the object the label points to.
            