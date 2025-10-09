# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

# If the fractional part is repeating, enclose the repeating part in parentheses

# If multiple answers are possible, return any of them.

# It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

# Note that if the fraction can be represented as a finite length string, you must return it.

 

# Example 1:

# Input: numerator = 1, denominator = 2
# Output: "0.5"
# Example 2:

# Input: numerator = 2, denominator = 1
# Output: "2"
# Example 3:

# Input: numerator = 4, denominator = 333
# Output: "0.(012)"
 

# Constraints:

# -231 <= numerator, denominator <= 231 - 1
# denominator != 0

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        res = []
        
        # Determine the sign
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")
        
        numerator, denominator = abs(numerator), abs(denominator)
        
        # Append integer part
        integer_part = numerator // denominator
        res.append(str(integer_part))
        
        remainder = numerator % denominator
        if remainder == 0:
            return "".join(res)  # no fractional part
        
        res.append(".")
        # Map to store remainder positions to detect cycles
        rem_pos = {}
        
        while remainder != 0:
            if remainder in rem_pos:
                # Insert parentheses around repeating part
                idx = rem_pos[remainder]
                res.insert(idx, "(")
                res.append(")")
                break
            rem_pos[remainder] = len(res)
            remainder *= 10
            quotient = remainder // denominator
            res.append(str(quotient))
            remainder %= denominator
        
        return "".join(res)
