# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

# Given an integer n, return the nth ugly number.

 

# Example 1:

# Input: n = 10
# Output: 12
# Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
# Example 2:

# Input: n = 1
# Output: 1
# Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
 

# Constraints:

# 1 <= n <= 1690
# Seen this question in a real interview before?
# 1/5
# Yes
# No

# time complexity: O(n) due to heap at each heapq.pop(): logn

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        
        i2, i3, i5 = 0, 0, 0 # the indexes of the last number we mutiply by 2, 3 or 5
        
        for i in range(1, n):
            next_num_i2 = dp[i2] * 2
            next_num_i3 = dp[i3] * 3
            next_num_i5 = dp[i5] * 5
            
            next_num = min([next_num_i2, next_num_i3, next_num_i5])
            
            dp[i] = next_num
            
            # use three if to avoid creating duplicates
            if next_num == next_num_i2:
                i2 += 1
            
            if next_num == next_num_i3:
                i3 += 1
            
            if next_num == next_num_i5:
                i5 += 1
        
        return dp[n - 1]
                    
        
        
        
        
        
        
        