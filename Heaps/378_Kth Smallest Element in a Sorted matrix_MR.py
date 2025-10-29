# Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# You must find a solution with a memory complexity better than O(n2).

 

# Example 1:

# Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# Output: 13
# Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
# Example 2:

# Input: matrix = [[-5]], k = 1
# Output: -5
 

# Constraints:

# n == matrix.length == matrix[i].length
# 1 <= n <= 300
# -109 <= matrix[i][j] <= 109
# All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
# 1 <= k <= n2
 
# O(klogn), O(n)
import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        min_heap = []

        # Initially, push the first element of each row into the min-heap.
        # The tuple format is (value, row_index, col_index)
        for r in range(n):
            heapq.heappush(min_heap, (matrix[r][0], r, 0))

        # We need to find the k-th smallest element.
        # We will pop from the heap k-1 times to discard the smaller elements.
        # The k-th pop will give us the answer.
        result = 0
        for _ in range(k):
            result, r, c = heapq.heappop(min_heap)
            
            # If the popped element is not the last in its row,
            # push the next element from the same row into the heap.
            # pushing matrix[r + 1][c], r + 1, c may lead to duplicates
            if c + 1 < n:
                heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))
        
        return result
    
# Time: O(nlogn + klogn)
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        min_heap = []
        
        for r in range(n):
            heapq.heappush(min_heap, (matrix[r][0], r, 0)) # log n
        
        for _ in range(k):
            result, r, c = heapq.heappop(min_heap)
            
            if c + 1 < n:
                heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1)) # log n
        
        return result    