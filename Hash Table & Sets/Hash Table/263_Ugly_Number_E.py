# An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.

# Given an integer n, return true if n is an ugly number.

 

# Example 1:

# Input: n = 6
# Output: true
# Explanation: 6 = 2 × 3
# Example 2:

# Input: n = 1
# Output: true
# Explanation: 1 has no prime factors.
# Example 3:

# Input: n = 14
# Output: false
# Explanation: 14 is not ugly since it includes the prime factor 7.

class Solution:
    def isUgly(self, n: int) -> bool:
        """
        Checks if a number is an ugly number.

        Args:
            n: The integer to check.

        Returns:
            True if n is an ugly number, False otherwise.
        """

        # Handle non-positive numbers: Ugly numbers must be positive.
        if n <= 0:
            return False

        # Repeatedly divide by 2, 3, and 5 until no longer divisible.
        # This effectively removes all factors of 2, 3, and 5.
        while n % 2 == 0:  # While n is divisible by 2
            n //= 2       # Integer division by 2

        while n % 3 == 0:  # While n is divisible by 3
            n //= 3       # Integer division by 3

        while n % 5 == 0:  # While n is divisible by 5
            n //= 5       # Integer division by 5
        
        return n == 1

        # If n is 1 after removing all factors of 2, 3, and 5, it'
# the fundamental theorem of arithmetic: every integer greater than 1 can be uniquely expressed as a product of prime numbers