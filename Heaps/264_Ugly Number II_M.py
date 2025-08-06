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

# time complexity: O(nlogn) due to heap at each heapq.pop(): logn
import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        
        factors = [2, 3, 5]
        count = 0
        min_heap = [1]
        nums_seen = set([1])
        
        while count < n:
            count += 1
            cur_num = heapq.heappop(min_heap) # O(log n) worst case
            for factor in factors:
                next_num = cur_num * factor
                if next_num not in nums_seen:
                    nums_seen.add(next_num)
                    heapq.heappush(min_heap, next_num) # O(log n) worst case
        
        return cur_num
                    
        
        
        
        
        
        
        