# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

 

# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]
 

# Constraints:

# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30

# Time complexity O(2^N)
class Solution:
  def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    res = []
    seen_comb = []
    def backtrack(start, cur_comb, cur_sum):
      if cur_sum == target:
        if set(cur_comb) not in seen_comb:
          res.append(cur_comb[:])
          seen_comb.append(set(cur_comb))
        return
      
      elif cur_sum > target:
        return
      
      else:
        for i in range(start, len(candidates)):
          candidate = candidates[i]
          cur_comb.append(candidate)
          backtrack(i + 1, cur_comb, cur_sum + candidate)
          cur_comb.pop()
    backtrack(0, [], 0)
    return res

# Time complexity O(2^N)
# a better one
from typing import List

class Solution:
  def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    # Sort candidates to handle duplicates and for pruning optimizations.
    candidates.sort()
    
    result = []
    
    def backtrack(start_index: int, current_path: List[int], remaining_target: int):
      # Base case: A valid combination is found.
      if remaining_target == 0:
        result.append(list(current_path))
        return
      
      # Iterate through the candidates starting from the given index.
      for i in range(start_index, len(candidates)):
        # Pruning: If the current candidate is larger than the remaining target,
        # all subsequent candidates will also be too large, so we can stop.
        if candidates[i] > remaining_target:
          break
        
        # *** Key step to avoid duplicate combinations ***
        # If the current element is the same as the previous one, and it's not the
        # first element in the current recursive step, skip it. This ensures
        # that for a set of duplicates, we only start a new path with the first one.
        if i > start_index and candidates[i] == candidates[i-1]:
          continue
        
        # --- Choose the element ---
        current_path.append(candidates[i])
        
        # --- Recurse ---
        # Move to the next index (i + 1) because each number can be used only once.
        backtrack(i + 1, current_path, remaining_target - candidates[i])
        
        # --- Unchoose the element (backtrack) ---
        current_path.pop()

    # Start the backtracking process.
    backtrack(0, [], target)
    return result
        
      