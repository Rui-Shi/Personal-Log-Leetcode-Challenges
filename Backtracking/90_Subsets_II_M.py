# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]
 

# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10

# Time: O(n * 2^n)
# Space: res: O(n * 2^n), cur_comb: O(n)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort() # necessary to avoid duplicates set
        res = []
        def backtrack(cur_comb, start_point):
            res.append(cur_comb[:])
            if len(cur_comb) == n:
                pass
            
            else:
                for i in range(start_point, n):
                    if nums[i] == nums[i - 1] and i != start_point: # avoid duplicates
                        continue
                    
                    cur_comb.append(nums[i])
                    backtrack(cur_comb, i + 1)
                    cur_comb.pop() 
        backtrack([], 0)
        return res 
