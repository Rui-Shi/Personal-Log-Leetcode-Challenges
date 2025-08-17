# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.


# Hint: So, we essentially need to find three numbers x, y, and z 
# such that they add up to the given value. If we fix one of the numbers say x, 
# we are left with the two-sum problem at hand!

# The primary performance bottleneck in your code is the if list_temp not in result: 
# check.  Checking for membership in a list is an O(n) operation, and you're doing 
# this inside a nested loop, leading to a worst-case time complexity of O(n^3).

# use hashmap
from typing import List

from typing import List

# Time O(n^2)
# Space O(n^2)
class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    result = []  # Stores unique triplets.
    
    seen_trips = {}
    
    for i in range(len(nums)-2):
        num1 = nums[i]
        target = 0 - num1
        map = {}
        for j in range(i + 1, len(nums)):
            num2 = nums[j]
            compli = target - num2
            if compli in map:
                trips = tuple(sorted([num1, num2, compli]))
                if trips not in seen_trips:
                    seen_trips[trips] = True
                    result.append([num1, num2, compli])
            map[num2] = True
    return result


# better solution 
# Time: sorting O(nlogn), loop O(n^2)
# Space: O(1) no additional space is needed other than the result
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()  # Sort the input array (O(n log n))

        for i in range(len(nums) - 2):  # Iterate up to the third-to-last element
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate starting numbers
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
                else:  # Found a triplet that sums to zero
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicate numbers for the second and third elements
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1  # Move to the next potential triplet
                    right -= 1

        return result
