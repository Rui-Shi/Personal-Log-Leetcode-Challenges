# A peak element is an element that is strictly greater than its neighbors.

# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

# You must write an algorithm that runs in O(log n) time.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:

# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

from typing import List
import math # Not strictly needed for the logic, but good practice if extending

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        Finds a peak element in a 0-indexed integer array nums using binary search.
        A peak element is strictly greater than its neighbors.
        Assumes nums[-1] = nums[n] = -infinity.
        Runs in O(log n) time.

        Args:
            nums: The input list of integers.

        Returns:
            The index of any peak element.
        """
        n = len(nums)
        low = 0
        high = n - 1

        # Binary search on the indices
        while low < high:
            # Calculate mid point, preventing potential overflow
            mid = low + (high - low) // 2

            # Compare middle element with its right neighbor
            # If nums[mid] is less than nums[mid + 1], it means the slope is
            # increasing, so a peak *must* exist on the right side (mid+1...high).
            if nums[mid] < nums[mid + 1]:
                low = mid + 1
            # Otherwise (nums[mid] >= nums[mid + 1]), the slope is
            # non-increasing (decreasing or flat). This means nums[mid]
            # could be a peak itself, or a peak exists to its left.
            # We narrow the search space to the left side including mid (low...mid).
            else:
                high = mid

        # When the loop terminates, low and high converge to the same index.
        # This index is guaranteed to be a peak element based on the comparisons made.
        return low # or return high, as low == high at this point

# Example usage (outside the class definition for testing):
sol = Solution()
nums1 = [2, 2, 2, 1, 2]
print(f"Input: {nums1}, Output: {sol.findPeakElement(nums1)}") # Output: 2
#
# nums2 = [1, 2, 1, 3, 5, 6, 4]
# print(f"Input: {nums2}, Output: {sol.findPeakElement(nums2)}") # Output: 5 (or 1)