# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

 

# Example 1:

# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# Example 2:

# Input: n = 2
# Output: false

class Solution:
    def isHappy(self, n: int) -> bool:
        list_sum_sqrt = []
        sum_sqrt = None
        str_n = n
        while sum_sqrt not in list_sum_sqrt:
            list_sum_sqrt.append(sum_sqrt)
            str_n = str(str_n)
            square_list = [int(digit)**2 for digit in str_n]
            sum_sqrt = sum(square_list)
            if sum_sqrt==1:
                return True
            str_n = sum_sqrt
        return False
    
s = Solution()
s.isHappy(19)