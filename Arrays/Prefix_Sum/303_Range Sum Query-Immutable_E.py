# Given an integer array nums, handle multiple queries of the following type:

# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:

# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

# Example 1:

# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]

# Explanation
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
# numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
# numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
 

# Constraints:

# 1 <= nums.length <= 104
# -105 <= nums[i] <= 105
# 0 <= left <= right < nums.length
# At most 104 calls will be made to sumRange.

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        
    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# another solution, compute the cumulative sum in advance.
from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        """
        Initialize the NumArray with a list of integers and precompute
        the prefix sums for fast range sum queries.

        Args:
            nums (List[int]): The list of integers.
        
        The prefix sum array (self.prefix) is built such that:
            self.prefix[i] = nums[0] + nums[1] + ... + nums[i]
        """
        # Initialize the prefix sum array with the first element of nums.
        self.prefix = [nums[0]]

        # Build the prefix sum array by iterating through the remaining elements.
        for i in range(1, len(nums)):
            # Append the sum of the current element and the previous prefix sum.
            self.prefix.append(nums[i] + self.prefix[i - 1])

    def sumRange(self, left: int, right: int) -> int:
        """
        Calculate the sum of the subarray nums[left:right+1] using the prefix sum array.

        Args:
            left (int): The starting index of the range (inclusive).
            right (int): The ending index of the range (inclusive).

        Returns:
            int: The sum of elements in nums between indices left and right.

        Explanation:
            - If left is 0, the result is simply self.prefix[right].
            - Otherwise, subtract self.prefix[left - 1] from self.prefix[right]
              to get the sum of the range.
        """
        # If the range starts from the first element, no subtraction is needed.
        if left == 0:
            return self.prefix[right]
        else:
            # Otherwise, compute the range sum by subtracting the prefix sum just before 'left'
            return self.prefix[right] - self.prefix[left - 1]


class NumArray:

    def __init__(self, nums: List[int]):
        self.pre_fix = [nums[0]]
        
        for i in range(1, len(nums)):
            self.pre_fix.append(self.pre_fix[i - 1] + nums[i])
        

    def sumRange(self, left: int, right: int) -> int:
        
        if left == 0:
            return self.pre_fix[right]
        
        else:
            return self.pre_fix[right] - self.pre_fix[left - 1]