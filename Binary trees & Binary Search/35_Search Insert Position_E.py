# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        
        if nums[left] >= target: 
            return 0 # if the target is small or equal to the smallest number of the list
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] >= target:
                right = mid
            
            else:
                left = mid + 1
            
        return left
        
        
            
            
            
        