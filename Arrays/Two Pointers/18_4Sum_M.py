# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
 

# Constraints:

# 1 <= nums.length <= 200
# -109 <= nums[i] <= 109
# -109 <= target <= 109

# Time complexity O(N^3)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        if n < 4:
            return []
        
        nums.sort() # sort nums for two pointer algo
        
        for i in range(n):
            # ❗ FIX: Skip duplicate values for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                # ❗ FIX: Skip duplicate values for the second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                complement = target - nums[i] - nums[j]
                # two pointer O(N)
                left = j + 1
                right = n - 1
                
                while left < right:
                    if nums[left] + nums[right] == complement:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    
                    elif nums[left] + nums[right] < complement:
                        left += 1
                    
                    else:
                        right -= 1
        
        return res
                        
                
        