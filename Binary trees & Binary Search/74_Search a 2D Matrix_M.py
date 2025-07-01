# ou are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

 

# Example 1:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        nrow = len(matrix)
        ncol = len(matrix[0])
        
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        top = 0
        bottom = nrow - 1
        
        while top < bottom - 1:
            mid = (top + bottom) // 2
            if matrix[mid][0] <= target:
                top = mid
            else:
                bottom = mid
        
        target_row = top if target < matrix[bottom][0] else bottom
        
        left = 0
        right = ncol - 1
        
        while left < right - 1:
            mid = (left + right) // 2
            if matrix[target_row][mid] <= target:
                left = mid
            else:
                right = mid
        
        return matrix[target_row][left] == target or matrix[target_row][right] == target