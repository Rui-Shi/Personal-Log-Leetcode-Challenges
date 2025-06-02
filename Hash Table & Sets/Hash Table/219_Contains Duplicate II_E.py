# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# 0 <= k <= 105

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):  # Iterate up to the actual end of the list
            for j in range(i + 1, min(len(nums), i + k + 1)):  # Corrected min and + 1
                if nums[i] == nums[j]:
                    return True
        return False


# use set and dict, much faster
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
       
        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            else:
                seen[num] = i
        return False 
           
