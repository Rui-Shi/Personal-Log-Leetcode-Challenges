# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

# Example 1:

# Input: x = 2.00000, n = 10
# Output: 1024.00000
# Example 2:

# Input: x = 2.10000, n = 3
# Output: 9.26100
# Example 3:

# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

# Constraints:

# -100.0 < x < 100.0
# -231 <= n <= 231-1
# n is an integer.
# Either x is not zero or n > 0.
# -104 <= xn <= 104

class Solution:
    def myPow(self, x: float, n: int) -> float:
        reci = False
        if n < 0:
            reci = not reci
        
        n = abs(n)
        res = 1

        if x == 1:
            return res
        
        if x == -1:
            return 1 if n % 2 == 0 else -1

        for i in range(n):
            if res == 0 or res == res * x:
                break
            else:
                res *= x

        return 1/res if reci else res

# a much better one with recursive halfing n
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base case: if n is 0, x^0 is 1.
        if n == 0:
            return 1.0
        
        # Handle negative exponents by inverting x and making n positive.
        if n < 0:
            x = 1 / x
            n = -n
            
        # Recursive step using exponentiation by squaring.
        # If n is even, x^n = (x*x)^(n/2).
        if n % 2 == 0:
            return self.myPow(x * x, n // 2)
        # If n is odd, x^n = x * x^(n-1).
        else:
            return x * self.myPow(x * x, (n - 1) // 2)
        