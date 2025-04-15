# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Example 3:

# Input: nums = [1,0,1,2]
# Output: 3
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        map_num = {} # use dict to reduce the time complexity
        k = 0
        for num in nums_set:
            if num in map_num:
                continue
            k_temp = 1
            num_backward = num - 1
            num_forward = num + 1
            while num_backward in nums_set:
                map_num[num_backward] = 0
                k_temp += 1
                num_backward -= 1
            
            while num_forward in nums_set:
                map_num[num_forward] = 0
                k_temp += 1
                num_forward += 1
            
            k = k_temp if k_temp > k else k
        
        return k
    
        
        