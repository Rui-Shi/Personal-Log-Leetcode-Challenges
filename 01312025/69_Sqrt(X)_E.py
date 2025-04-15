# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

# Example 1:

# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.
# Example 2:

# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        while i**2<=x:
            i += 1
        return i-1

# x**2 represent square in Python


def mySqrt(x: int) -> int:
    """
    Calculates the square root of a non-negative integer x, rounded down to the nearest integer.

    Args:
        x: The non-negative integer.

    Returns:
        The square root of x rounded down to the nearest integer.
    """

    if x == 0:
        return 0

    left, right = 1, x  # Initialize search range

    while left <= right:
        mid = left + (right - left) // 2  # Prevent potential overflow

        if mid * mid <= x:  # Check if mid*mid is less than or equal to x
            result = mid   # If it is, store mid as a potential result
            left = mid+1 # Try larger values for the square root
        else:
            right = mid-1# Try smaller values for the square root

    return result  # Return the final result (rounded down)