# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

# Example 1:

# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# Example 2:


# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 
# Constraints:

# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -231 <= matrix[i][j] <= 231 - 1

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_zero = set()
        col_zero = set()
        
        rows = len(matrix) # len() returns the number of rows by default
        cols = len(matrix(0))
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    row_zero.add(i) # the method to add a element to a set
                    col_zero.add(j)
                    
        for i in row_zero:
            matrix[i] = [0]*rows
        
        for j in col_zero:
            for i in range(rows):
                matrix[i][j] = 0

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        row_zero = set()
        col_zero = set()
        
        nr = len(matrix)
        nc = len(matrix[0])
        
        for i in range(nr):
            for j in range(nc):
                row_zero.add(i)
                col_zero.add(j)
                
        for i in row_zero:
            matrix[i] = [0] * nr
        
        for j in col_zero:
            for i in range(nr):
                matrix[i][j] = 0
        
                