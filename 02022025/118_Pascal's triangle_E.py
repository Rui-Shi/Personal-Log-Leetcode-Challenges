# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]
 

# Constraints:

# 1 <= numRows <= 30

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            Pas_tri = []
        elif numRows == 1:
            Pas_tri = [[1]]
        elif numRows == 2:
            Pas_tri = [[1], [1,1]]
        else: 
            Pas_tri = [[1], [1,1]]
            for i in range(3, numRows+1):
                newRow = [1]
                for j in range(len(Pas_tri[-1]) - 1):
                    newNum = Pas_tri[-1][j]+Pas_tri[-1][j+1]
                    newRow.append(newNum)
                newRow.append(1)
                Pas_tri.append(newRow)
        return Pas_tri
            
        