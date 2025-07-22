# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:

# Input: candidates = [2], target = 1
# Output: []
 

# Constraints:

# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements of candidates are distinct.
# 1 <= target <= 40

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combo_seen = set()
        
        def backtrack(candidates, cur_combo):
            if sum(cur_combo) == target:
                cur_combo.sort()
                if tuple(cur_combo) not in combo_seen:
                    res.append(cur_combo)
                    combo_seen.add(tuple(cur_combo))
            
            elif sum(cur_combo) < target:
                for candiate in candidates:
                    backtrack(candidates, cur_combo + [candiate])
            
            else:
                return
        
        backtrack(candidates, [])
        
        return res
    
# optimize in time complexity:

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        # The backtrack function now takes an index to control the search
        def backtrack(start_index: int, cur_combo: List[int], current_sum: int):
            # Base case: successful combination found
            if current_sum == target:
                res.append(cur_combo[:])  # Append a copy of the combination
                return

            # Base case: combination is invalid, stop this path
            if current_sum > target:
                return

            # Explore further combinations
            for i in range(start_index, len(candidates)):
                candidate = candidates[i]
                
                # 1. Choose a candidate
                cur_combo.append(candidate)
                
                # 2. Recurse
                # Pass `i` (not `i + 1`) to allow the same number to be reused
                backtrack(i, cur_combo, current_sum + candidate)
                
                # 3. Backtrack (un-choose)
                cur_combo.pop()

        backtrack(0, [], 0)
        return res

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(start_index, cur_comb, current_sum):
            if current_sum == target:
                res.append(cur_comb[:])
            
            elif current_sum > target:
                return
            
            else:
                for i in range(start_index, len(candidates)):
                    num_new = candidates[i]
                    
                    cur_comb.append(num_new)
                    
                    backtrack(i, cur_comb, current_sum + num_new)
                    
                    cur_comb.pop()
        backtrack(0, [], 0)
        return res  
            