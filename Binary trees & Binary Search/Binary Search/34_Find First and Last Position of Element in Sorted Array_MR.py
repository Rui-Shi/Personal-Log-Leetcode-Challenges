# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        target_left = target - 0.01
        target_right = target + 0.01
        
        # looking for the left index:
        l, r = 0, len(nums) - 1
        
        while l < r - 1:
            mid = (l + r) // 2
            if nums[l] <= target_left < nums[mid]:
                r = mid
            else:
                l = mid
        
        if nums[r] == target:
            left = r
        else:
            return [-1, -1]
        
        # looking for the right index:
        l, r = 0, len(nums) - 1
        while l < r - 1:
            mid = (l + r) // 2
            if nums[l] <= target_right < nums[mid]:
                r = mid
            else:
                l = mid
        
        right = l
        
        return [left, right]

# a better version:

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Finds the starting and ending position of a given target value in a
        sorted array.

        This is achieved by running a modified binary search twice:
        1. The first search finds the leftmost occurrence of the target.
        2. The second search finds the rightmost occurrence of the target.

        Args:
            nums: A list of integers sorted in non-decreasing order.
            target: The value to find.

        Returns:
            A list containing the starting and ending index of the target.
            Returns [-1, -1] if the target is not found.
        """

        # Helper function to perform a modified binary search.
        # It finds either the first (leftmost) or the last (rightmost)
        # occurrence of the target.
        def find_bound(is_first: bool) -> int:
            left, right = 0, len(nums) - 1
            bound_index = -1
            
            while left <= right:
                # Standard binary search middle calculation
                mid = left + (right - left) // 2

                if nums[mid] < target:
                    # The target is in the right half
                    left = mid + 1
                elif nums[mid] > target:
                    # The target is in the left half
                    right = mid - 1
                else: # nums[mid] == target
                    # We found the target. Now we need to see if it's the
                    # first or last one.
                    bound_index = mid
                    if is_first:
                        # To find the first occurrence, we continue searching
                        # in the left half.
                        right = mid - 1
                    else:
                        # To find the last occurrence, we continue searching
                        # in the right half.
                        left = mid + 1
                        
            return bound_index

        # Find the leftmost and rightmost bounds by calling the helper
        left_bound = find_bound(True)
        right_bound = find_bound(False)

        return [left_bound, right_bound]
                
            
            
        
        