# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# Example 2:


# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

import List # Note: Usually "from typing import List" is needed at the top of the file

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotates an n x n 2D matrix by 90 degrees clockwise in-place.

        Args:
            matrix: A list of lists representing the n x n matrix.

        Returns:
            None. The matrix is modified directly.

        The rotation is achieved in two steps:
        1. Transpose the matrix: Swap elements across the main diagonal (top-left to bottom-right).
           An element at matrix[row][col] is swapped with matrix[col][row].
        2. Reverse each row: Reverse the order of elements in each row horizontally.
        """
        n = len(matrix)

        # Step 1: Transpose the matrix
        # Iterate through the rows
        for r in range(n):
            # Iterate through the columns starting from the current row index + 1
            # This ensures we only process the upper triangle of the matrix
            # (elements above the main diagonal) to avoid swapping twice.
            for c in range(r + 1, n):
                # Swap the element matrix[r][c] with matrix[c][r]
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        # Step 2: Reverse each row
        # Iterate through each row of the transposed matrix
        for r in range(n):
            # Use the built-in reverse() method for lists to reverse the row in-place
            matrix[r].reverse()

            # Alternatively, manually reverse the row using two pointers:
            # left, right = 0, n - 1
            # while left < right:
            #     matrix[r][left], matrix[r][right] = matrix[r][right], matrix[r][left]
            #     left += 1
            #     right -= 1

# Example Usage:
# Example 1
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
solver = Solution()
solver.rotate(matrix1)
print(f"Example 1 Output: {matrix1}") # Expected: [[7,4,1],[8,5,2],[9,6,3]]

# Example 2
matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
solver.rotate(matrix2)
print(f"Example 2 Output: {matrix2}") # Expected: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        # step 1: transpose the matrix
        for r in range(n):
            for c in range(r + 1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        # step 2: reverse each row to get the right answer
        for i in range(n):
            matrix[i].reverse()