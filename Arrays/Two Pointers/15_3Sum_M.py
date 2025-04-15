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

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()  # Sort the input array (O(n log n))
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate starting numbers
                continue # jump to the next cycle
            
            target = 0 - nums[i]
            num_map = {}
            
            for j in range(i+1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]: # Skip duplicate starting numbers
                    continue
                
                curr = nums[j]
                x = target - curr
                if x in num_map:
                    list_temp = [nums[i], x, nums[j]]
                    list_temp.sort()
                    result.append(list_temp)
                else:
                    num_map[curr] = j
        return result


# better solution O(nlogn):
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
