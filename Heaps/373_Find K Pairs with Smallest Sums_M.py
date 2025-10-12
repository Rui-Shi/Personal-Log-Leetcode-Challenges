# You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

# Define a pair (u, v) which consists of one element from the first array and one element from the second array.

# Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

 

# Example 1:

# Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# Output: [[1,2],[1,4],[1,6]]
# Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
# Example 2:

# Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# Output: [[1,1],[1,1]]
# Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 105
# -109 <= nums1[i], nums2[i] <= 109
# nums1 and nums2 both are sorted in non-decreasing order.
# 1 <= k <= 104
# k <= nums1.length * nums2.length

import heapq
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # Handle edge cases: empty inputs or k=0
        if not nums1 or not nums2 or k == 0:
            return []
        
        heap = [] # Min-heap: stores (sum, idx1, idx2)
        n1, n2 = len(nums1), len(nums2)
        
        # Initialize heap with pairs (nums1[i], nums2[0]) for i in [0, min(k-1, n1-1)]
        # This covers the smallest possible sums for each element in nums1
        for i in range(min(k, n1)):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))
        
        res = [] # Stores the k smallest pairs (actual values)

        # Extract k pairs from the heap
        while k > 0 and heap:
            current_sum, i, j = heapq.heappop(heap) # Get smallest sum pair
            res.append([nums1[i], nums2[j]]) # Add actual pair to result
            k -= 1 # Decrement count of remaining pairs needed

            # If there's a next element in nums2 for nums1[i], add it to heap
            if j + 1 < n2:
                heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j + 1))
            
        return res

import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k == 0:
            return []
        
        heap = []
        n1, n2 = len(nums1), len(nums2)
        
        for i in range(min(k, n1)):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))
            
            res = []
        
        while k > 0 and heap:
            current_sum, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])   
            k -= 1
            
            if j + 1 < n2:
                heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j + 1))
        
        return res
            
            
            
        
        
        
        