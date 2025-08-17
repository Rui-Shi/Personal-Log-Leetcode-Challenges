# Given an integer array nums, 
# move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1

# O(n) and O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Moves all zeros in-place to the end of the array while maintaining
        the relative order of non-zero elements.

        Args:
            nums: The input list of integers.

        Returns:
            None. Modifies nums in-place.
        """

        left = 0  # Pointer to track the position for the next non-zero element

        for right in range(len(nums)):  # Iterate through the array using the right pointer
            if nums[right]!= 0:  # Check if the current element is non-zero
                nums[left], nums[right] = nums[right], nums[left]  # Swap elements
                left += 1  # Move the left pointer to the next position

        # After the loop, all non-zero elements are before 'left', and all zeros are after.
        # No explicit action is needed to place zeros at the end because they are shifted there by the swaps.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write_index = 0
        
        n = len(nums)
        
        for read_index in range(n):
            if nums[read_index] != 0:
                nums[write_index] = nums[read_index]
                write_index += 1
        
        nums[write_index:] = [0] * (len(nums) - write_index)
        
