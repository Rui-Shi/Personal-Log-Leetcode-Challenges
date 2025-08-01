# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

# You may return the answer in any order.

 

# Example 1:

# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
# Example 2:

# Input: n = 1, k = 1
# Output: [[1]]
# Explanation: There is 1 choose 1 = 1 total combination.
 

# Constraints:

# 1 <= n <= 20
# 1 <= k <= n


# use backtracking
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        Given two integers n and k, return all possible combinations of k numbers
        chosen from the range [1, n].
        """
        result = []

        def backtrack(start, current_combination):
            # If the combination is of the desired length, add it to the result.
            if len(current_combination) == k:
                result.append(list(current_combination))
                return

            # Explore further numbers to add to the combination.
            for i in range(start, n + 1):
                current_combination.append(i)
                backtrack(i + 1, current_combination)
                current_combination.pop()  # Backtrack

        backtrack(1, [])
        return result 

# Time Complexity O(k * (n, k))
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
                    
        res = []
        
        def backtrack(start, current_combination):
            if len(current_combination) == k:
                res.append(list(current_combination))
        
            for i in range(start, n + 1):
                current_combination.append(i)
                backtrack(i + 1, current_combination)
                current_combination.pop()  # Backtrack
        
        backtrack(1, [])
        return res