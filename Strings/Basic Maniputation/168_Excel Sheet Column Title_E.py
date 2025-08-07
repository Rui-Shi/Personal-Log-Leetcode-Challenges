# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
 

# Example 1:

# Input: columnNumber = 1
# Output: "A"
# Example 2:

# Input: columnNumber = 28
# Output: "AB"
# Example 3:

# Input: columnNumber = 701
# Output: "ZY"
 

# Constraints:

# 1 <= columnNumber <= 231 - 1

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        mapping = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', \
                   8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', \
                   14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', \
                   20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}
        
        res = ''
        reminder = columnNumber
        while reminder > 0:
            num = (reminder - 1) % 26
            reminder = (reminder - 1) // 26
            res += mapping[num + 1]
        
        return res[::-1]
            

# The reminder - 1 is needed because standard mathematical operations like modulo (%) 
# and integer division (//) work with a 0-indexed system, but Excel's column titles are a 1-indexed system.

# Subtracting 1 effectively converts the 1-based number into a 0-based one, allowing the math to work correctly.
            
            
            
        