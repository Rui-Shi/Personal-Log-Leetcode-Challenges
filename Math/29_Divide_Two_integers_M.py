# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

# The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

# Return the quotient after dividing dividend by divisor.

# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

 

# Example 1:

# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = 3.33333.. which is truncated to 3.
# Example 2:

# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = -2.33333.. which is truncated to -2.
 

# Constraints:

# -231 <= dividend, divisor <= 231 - 1
# divisor != 0

# Time Complexity: O(log N/M)
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        dividend_pos = abs(dividend)
        divisor_pos = abs(divisor)
        
        MIN = -2 ** 31
        MAX = 2 ** 31 - 1
        
        quo = 0
        temp = 0
        while temp <= dividend_pos:
            temp += divisor_pos
            quo += 1
        
        quo -= 1
        if (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0):
            pass
        else:
            quo *= -1
        
        if quo <= MIN:
            quo = MIN
        elif quo >= MAX:
            quo = MAX
        else:
            pass
        
        return quo

# Optimizer one, bit computation
# Time Complexity O(log N)
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        # Define integer limits for a 32-bit system
        MIN = -2**31
        MAX = 2**31 - 1
        
        # Handle the specific overflow edge case
        if dividend == MIN and divisor == -1:
            return MAX
            
        # Determine the sign of the result. Using XOR (^) is a concise way
        # to check if the signs are different.
        is_negative = (dividend < 0) ^ (divisor < 0)
        
        # Work with positive numbers for the division logic
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)
        
        quotient = 0
        
        # This loop is the core of the optimization.
        # It repeatedly finds the largest power-of-two multiple of the divisor
        # that can be subtracted from the dividend.
        while abs_dividend >= abs_divisor:
            # Start with the divisor itself (divisor * 2^0)
            temp_divisor = abs_divisor
            multiple = 1
            
            # Keep doubling the temp_divisor and the multiple as long as the
            # doubled value is still less than or equal to the dividend.
            # Using a left bit shift (<< 1) is a fast way to multiply by 2.
            while abs_dividend >= (temp_divisor << 1):
                temp_divisor <<= 1  # temp_divisor *= 2
                multiple <<= 1    # multiple *= 2
            
            # Subtract the largest multiple found from the dividend
            abs_dividend -= temp_divisor
            # Add the corresponding multiple (which is a power of 2) to the quotient
            quotient += multiple

        # Apply the negative sign if necessary
        if is_negative:
            return -quotient
        else:
            return quotient

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Define integer limits for a 32-bit system
        MIN = -2**31
        MAX = 2**31 - 1
        
        # to check if the signs are different.
        is_negative = (dividend < 0) ^ (divisor < 0)
        
        # Work with positive numbers for the division logic
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)
        
        quotient = 0
        
        while abs_dividend >= abs_divisor:
            temp_divisor = abs_divisor
            multiple = 1
            
            while abs_dividend >= (temp_divisor * 2):
                temp_divisor *= 2
                multiple *= 2
            
            abs_dividend -= temp_divisor
            
            quotient += multiple
            
        if is_negative:
            return -quotient
        else:
            return quotient