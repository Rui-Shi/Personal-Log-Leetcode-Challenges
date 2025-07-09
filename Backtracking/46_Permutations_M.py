# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:

# Input: nums = [1]
# Output: [[1]]
 

# Constraints:

# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 0:
            return []
        
        if n == 1:
            return [nums]
        
        nums_set = set(nums)
        
        res = []
        
        def backtrack(nums_set, cur_comb):
            if len(cur_comb) == n:
                res.append(cur_comb)
                
            else:
                for num in nums_set:
                    backtrack(nums_set - {num}, cur_comb + [num])
                    
        backtrack(nums_set, [])
        
        return res
        
        