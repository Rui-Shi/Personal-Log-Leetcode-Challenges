# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

# Only numbers 1 through 9 are used.
# Each number is used at most once.
# Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

 

# Example 1:

# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Explanation:
# 1 + 2 + 4 = 7
# There are no other valid combinations.
# Example 2:

# Input: k = 3, n = 9
# Output: [[1,2,6],[1,3,5],[2,3,4]]
# Explanation:
# 1 + 2 + 6 = 9
# 1 + 3 + 5 = 9
# 2 + 3 + 4 = 9
# There are no other valid combinations.
# Example 3:

# Input: k = 4, n = 1
# Output: []
# Explanation: There are no valid combinations.
# Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.

from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        results = []  # This will store all valid combinations found

        def backtrack(start_num, count, current_sum, current_combination):
            nonlocal results
            
            if count == k and current_sum == n:
                results.append(current_combination[:])
                return
            
            if count > k or start_num > 9:
                return
            
            if current_sum > n:
                return
            
            for i in range(start_num, 10):
                if current_sum + i > n:
                    break
                
                current_combination.append(i)
                
                backtrack(i + 1, count + 1, current_sum + i, current_combination)
            
                # backtracking
                current_combination.pop()
            
                
        backtrack(start_num=1, count=0, current_sum=0, current_combination=[])
        
        return results

# --- Example Usage (outside the class definition) ---

# Create an instance of the Solution class
solver = Solution()

# Example 1:
k1, n1 = 3, 7
output1 = solver.combinationSum3(k1, n1)
print(f"Input: k = {k1}, n = {n1}")
print(f"Output: {output1}")
# Expected: [[1, 2, 4]]

# Example 2:
k2, n2 = 3, 9
output2 = solver.combinationSum3(k2, n2)
print(f"\nInput: k = {k2}, n = {n2}")
print(f"Output: {output2}")
# Expected: [[1, 2, 6], [1, 3, 5], [2, 3, 4]] (order of combinations may vary)

# Example 3:
k3, n3 = 4, 1
output3 = solver.combinationSum3(k3, n3)
print(f"\nInput: k = {k3}, n = {n3}")
print(f"Output: {output3}")
# Expected: []

# Example 4 (Edge case):
k4, n4 = 9, 45
output4 = solver.combinationSum3(k4, n4)
print(f"\nInput: k = {k4}, n = {n4}")
print(f"Output: {output4}")
# Expected: [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
                    