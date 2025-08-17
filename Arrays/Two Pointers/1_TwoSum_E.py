# Given an array of integers nums and an integer target, return indices of 
# the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
# Time Complexity: O(n^2)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
        # Return an empty list if no solution is found
        return []
    

# Test
s = Solution()
nums = [2,7,11,15]; target = 9
print(s.twoSum(nums, target))

# optional solusion: using hashmap: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numMap={}
        for i in range(len(nums)):
            curr = nums[i]
            x = target - curr
            if x in numMap:
                return [numMap[x],i]
            else:
                numMap[curr]=i

        return []
    
# The code iterates through the nums list only once using a for loop.  Inside the loop, the operations performed 
# (checking for x in numMap, accessing and storing values in numMap) 
# take constant time on average, thanks to the use of a hash map (dictionary in Python). 
# Hash map lookups, insertions, and deletions have an average time complexity of O(1).

# Since the loop runs n times, and each iteration takes constant time, the overall time complexity is O(n) * O(1) = O(n).

# Time: O(n)
# Space: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i, num in enumerate(nums):
            if target - num in numMap:
                return[numMap[target - num], i]
            
            numMap[num] = i
        return []

# Two pointer
# Time: O(n log n) comes from nums.sort()
# Space: O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        
        left, right = 0, len(nums) - 1
        
        while left < right:
            if nums[left] + nums[right] == target:
                return [left, right]
            
            elif nums[left] + nums[right] < target:
                left += 1
            
            else:
                right -= 1
        
        return []