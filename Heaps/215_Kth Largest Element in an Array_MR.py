# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

 

# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
 

# Constraints:

# 1 <= k <= nums.length <= 105
# -104 <= nums[i] <= 104

import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        """
        Finds the kth largest element using a min-heap.

        Args:
          nums: The list of integers.
          k: The position 'k'.

        Returns:
          The kth largest element.
        """
        # Initialize a min-heap (Python's heapq is a min-heap)
        min_heap = []

        for num in nums:
            # Add the current number to the heap
            # The heappush function ensures that the heap property 
            # (smallest element at the root) is maintained after the insertion.
            heapq.heappush(min_heap, num)

            if len(min_heap) > k:
              # this line removes and returns the smallest element from the min_heap
              heapq.heappop(min_heap)

        # The root of the heap (min_heap[0]) is the kth largest element
        return min_heap[0]

# --- Example Usage ---
solver_heap = Solution()
nums1 = [3, 2, 1, 5, 6, 4]
k1 = 2
print(f"Input: nums = {nums1}, k = {k1}")
print(f"Output (Heap): {solver_heap.findKthLargest(nums1, k1)}") # Output: 5

nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k2 = 4
print(f"\nInput: nums = {nums2}, k = {k2}")
print(f"Output (Heap): {solver_heap.findKthLargest(nums2, k2)}") # Output: 4
        