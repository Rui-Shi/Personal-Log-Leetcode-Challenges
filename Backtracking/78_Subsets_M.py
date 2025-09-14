# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]
 

# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.

# Time: O(n * 2^n)
# Space: res: O(n * 2^n), cur_comb: O(n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def backtrack(cur_comb, start_point):
            res.append(cur_comb[:])
            if len(cur_comb) == n:
                pass
            
            else:
                for i in range(start_point, n):
                    cur_comb.append(nums[i])
                    backtrack(cur_comb, i + 1)
                    cur_comb.pop() 
        backtrack([], 0)
        return res 
        