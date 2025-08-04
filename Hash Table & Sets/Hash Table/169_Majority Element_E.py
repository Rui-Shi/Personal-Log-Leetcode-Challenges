# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 

# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
 

# Follow-up: Could you solve the problem in linear time and in O(1) space?


from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        bound = len(nums)//2
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        
        for num, count in dict.items():
            if count > bound:
                return num

# Solution 2: much more effienent
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)// 2]
    
s = Solution()
test_case = [1, 2, 3, 4, 4]
print(s.majorityElement(test_case))


import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.defaultdict(int)
        
        bound = len(nums) // 2
        
        for num in nums:
            counts[num] += 1
            if counts[num] > bound:
                return num
        