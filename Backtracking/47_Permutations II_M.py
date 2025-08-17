# Given a collection of numbers, nums, 
# that might contain duplicates, return all possible unique permutations in any order.

 

# Example 1:

# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
# Example 2:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

# Constraints:

# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10

# Time: O(n * n!) worst case
# Space: O(n * n!)
# auxiliary space: O(n) for cur_comb
import collections
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        freq_dic = collections.defaultdict(int)
        for num in nums:
            freq_dic[num] += 1 # space: O(n)
            
        res = []
        def backtrack(cur_comb, freq_dic):  # cur_comb space: O(n)
            
            if len(cur_comb) == len(nums):
                res.append(cur_comb[:])
            
            else:
                for num in freq_dic:
                    if freq_dic[num] > 0:
                        cur_comb.append(num)
                        freq_dic[num] -= 1
                        backtrack(cur_comb, freq_dic)
                        freq_dic[num] += 1
                        cur_comb.pop()
            
        backtrack([], freq_dic)
        return res # space: O(n * n!)
        
        
            