# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
 

# Constraints:

# -231 <= x <= 231 - 1

class Solution:
    def reverse(self, x: int) -> int:
        bound = 2 ** 31
        
        x_str = str(x)
        
        negative = False
        
        if x_str[0] == "-":
            negative = not negative
        
        if negative:
            x_inverse = -1 * int(x_str[1:][::-1])
        
        else:
            x_inverse = int(x_str[::-1])
        
        if x_inverse >= -1 * bound and x_inverse < bound:
            return x_inverse
        
        else:
            return 0

# Time and Space complexity: O(n)
# Str is immutable 
        
        
        
            
