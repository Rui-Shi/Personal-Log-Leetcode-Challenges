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
        start = 0
        if x_str[0] == "-":
            start = 1
            
        if start == 0:
            X_inverse = int(x_str[start:][::-1])
        else:
            X_inverse = int("-" + x_str[start:][::-1])
        
        if X_inverse < -1 * bound or X_inverse >= bound:
            return 0
        
        return X_inverse
