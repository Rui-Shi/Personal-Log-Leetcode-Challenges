# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

 

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = 10**10
        sum = 0
        nums.sort()  # Sort the input array (O(n log n))
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum_temp = nums[i] + nums[left] + nums[right]
                
                diff_temp = abs(sum_temp - target)
                if diff_temp == 0:
                    return sum_temp
                
                sum = sum_temp if diff_temp < diff else sum
                diff = diff_temp if diff_temp < diff else diff
                
                if sum_temp > target:
                    right -= 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                else:
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
        return sum
             
             