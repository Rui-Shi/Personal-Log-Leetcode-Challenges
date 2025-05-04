# Given an integer n, return true if it is a power of four. Otherwise, return false.

# An integer n is a power of four, if there exists an integer x such that n == 4x.

 

# Example 1:

# Input: n = 16
# Output: true
# Example 2:

# Input: n = 5
# Output: false
# Example 3:

# Input: n = 1
# Output: true
 

# Constraints:

# -231 <= n <= 231 - 1

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        else:
            x = math.log(n, 4)
            if 4**round(x) == n:
                return True
            else:
                return False

# optional solution without using the build in function:
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True

        while n > 1:
            if n % 4 != 0:
                return False
            n //= 4

        return True