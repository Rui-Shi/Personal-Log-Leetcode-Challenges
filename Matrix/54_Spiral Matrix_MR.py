# Given an m x n matrix, return all elements of the matrix in spiral order.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:


# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100

import collections # Assuming List is from collections.typing or typing
from typing import List # More standard import for List

class Solution:
    """
    This class provides a method to return all elements of a matrix in spiral order.
    """
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Given an m x n matrix, returns all elements of the matrix in spiral order.

        Args:
            matrix: A list of lists of integers representing the m x n matrix.

        Returns:
            A list of integers containing the elements of the matrix in spiral order.
        """
        # Handle empty matrix edge case
        if not matrix or not matrix[0]:
            return []

        rows, cols = len(matrix), len(matrix[0])
        result = [] # List to store the spiral order elements

        # Define boundaries for the spiral traversal
        top, bottom = 0, rows - 1
        left, right = 0, cols - 1

        # Continue traversal as long as the boundaries are valid
        while left <= right and top <= bottom:
            # Traverse Right
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1

            # Traverse Down
            if top <= bottom: # Check if there's still a valid row range
                for i in range(top, bottom + 1):
                    result.append(matrix[i][right])
                right -= 1

            # Traverse Left
            # Important: Check if boundaries crossed *after* potentially modifying them above
            if left <= right and top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1

            # Traverse Up
            # Important: Check if boundaries crossed *after* potentially modifying them above
            if left <= right and top <= bottom: # <-- THIS CHECK WAS MISSING/IMPLICIT IN ORIGINAL
                for i in range(bottom, top - 1, -1): # Iterate backwards
                    result.append(matrix[i][left])
                left += 1 # Move the left boundary right

        return result

# Example Usage:
sol = Solution()

# Example 1
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
print(f"Input: {matrix1}")
print(f"Output: {sol.spiralOrder(matrix1)}") # Output: [1,2,3,6,9,8,7,4,5]

# Example 2
matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(f"Input: {matrix2}")
print(f"Output: {sol.spiralOrder(matrix2)}") # Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# Example 3: Single row
matrix3 = [[1, 2, 3]]
print(f"Input: {matrix3}")
print(f"Output: {sol.spiralOrder(matrix3)}") # Output: [1, 2, 3]

# Example 4: Single column
matrix4 = [[1], [2], [3]]
print(f"Input: {matrix4}")
print(f"Output: {sol.spiralOrder(matrix4)}") # Output: [1, 2, 3]

# Example 5: 2x2 matrix
matrix5 = [[1, 2], [3, 4]]
print(f"Input: {matrix5}")
print(f"Output: {sol.spiralOrder(matrix5)}") # Output: [1, 2, 4, 3]