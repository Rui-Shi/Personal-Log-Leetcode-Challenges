# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:

# Input: rowIndex = 0
# Output: [1]
# Example 3:

# Input: rowIndex = 1
# Output: [1,1]
 

# Constraints:

# 0 <= rowIndex <= 33
 

# Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            newRow = [1]
        elif rowIndex == 1:
            newRow = [1,1]
        else: 
            Pas_tri = [[1], [1,1]]
            for i in range(2, rowIndex+1):
                newRow = [1]
                for j in range(len(Pas_tri[-1]) - 1):
                    newNum = Pas_tri[-1][j]+Pas_tri[-1][j+1]
                    newRow.append(newNum)
                newRow.append(1)
                Pas_tri.append(list(newRow))
                newRow = Pas_tri[-1]
        return newRow