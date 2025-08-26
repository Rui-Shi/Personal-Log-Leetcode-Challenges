# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
 

# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:

# Input: s = "A", numRows = 1
# Output: "A"


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Handle edge cases where no conversion is needed or possible.
        # This also prevents a ZeroDivisionError if numRows is 1.
        if numRows <= 1 or numRows >= len(s):
            return s

        zig_num = numRows * 2 - 2
        
        row_num = [0] * len(s)
        
        for i in range(len(s)):
            remainder = i % zig_num 
            if remainder < numRows:
                row_num[i] = remainder
            
            else:
                # This calculates the row for the "upward" part of the zigzag
                row_num[i] = zig_num - remainder
                
        # --- Start of the completed code ---
        
        res = ''
        
        # Iterate from row 0 to the last row
        for r in range(numRows):
            # Iterate through the original string's characters
            for i in range(len(s)):
                # If the character at index 'i' belongs in the current row 'r'
                if row_num[i] == r:
                    # Append that character to the result string
                    res += s[i]
            
        return res
            
    

s = Solution()
print(s.convert("abcdefghijsdfasdfsdfasd", 5))


# a much more efficent one:

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1 or numRows >= len(s):
            return s

        rows = [''] * numRows  # Create a list to hold the string for each row
        zig_num = numRows * 2 - 2

        for i in range(len(s)):
            remainder = i % zig_num
            row_index = 0
            
            if remainder < numRows:
                row_index = remainder
            else:
                row_index = zig_num - remainder
            
            rows[row_index] += s[i]

        # Join all the row strings together for the final result
        return "".join(rows)

# Time: O(n)
# Space: O(n)
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s
        
        rows = [''] * numRows
        
        zig_cycle = 2 * numRows - 2
        
        for index, char in enumerate(s):
            reminder = index % zig_cycle
            
            if reminder < numRows:
                row_index = reminder
            
            else:
                row_index = zig_cycle - reminder
            
            rows[row_index] += s[index]
        
        # Join all the row strings together for the final result
        return "".join(rows)    
            