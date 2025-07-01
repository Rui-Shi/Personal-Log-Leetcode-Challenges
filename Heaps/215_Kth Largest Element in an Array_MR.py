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
    # Initialize a min-heap (Python's heapq is a min-heap)
    min_heap = []
        
    for num in nums:
      heapq.heappush(min_heap, num) # Pushes the `item` onto the `heap`, maintaining the heap invariant 
      if len(min_heap) > k:
        heapq.heappop(min_heap) # used to remove and return the smallest item from the heap, ensuring the heap invariant is maintained afterward.
      
    return min_heap[0]
        