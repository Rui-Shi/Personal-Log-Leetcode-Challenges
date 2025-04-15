# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

# Example 1:

# Input: num1 = "11", num2 = "123"
# Output: "134"
# Example 2:

# Input: num1 = "456", num2 = "77"
# Output: "533"
# Example 3:

# Input: num1 = "0", num2 = "0"
# Output: "0"
 

# Constraints:

# 1 <= num1.length, num2.length <= 104
# num1 and num2 consist of only digits.
# num1 and num2 don't have any leading zeros except for the zero itself.

# My solution
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        carry = 0  # More descriptive name than 'stack'

        while p1 >= 0 or p2 >= 0:  # Combine the loops
            digit1 = int(num1[p1]) if p1 >= 0 else 0  # Handle cases where one string is shorter
            digit2 = int(num2[p2]) if p2 >= 0 else 0
            digit_sum = digit1 + digit2 + carry
            digit_curr = digit_sum % 10
            carry = digit_sum // 10
            res += str(digit_curr)
            p1 -= 1
            p2 -= 1

        if carry:  # Add the final carry if any
            res += str(carry)

        return res[::-1]  # Reverse the result
            
        
        
        