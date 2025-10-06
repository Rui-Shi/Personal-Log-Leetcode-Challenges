# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [2,3,0,1,4]
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 104
# 0 <= nums[i] <= 1000
# It's guaranteed that you can reach nums[n - 1].

def jump(nums):

    n = len(nums)
    if n <= 1:
        return 0

    jumps = 0
    current_reach = 0
    farthest_reach = 0

    for i in range(n - 1):
        farthest_reach = max(farthest_reach, i + nums[i])
        if i == current_reach:
            jumps += 1
            current_reach = farthest_reach

    return jumps

# Test case
nums = [2, 2, 0, 1, 4]
result = jump(nums)
print(result)

class Solution:
    def jump(self, nums):
        n = len(nums)
        # If the array has 1 or 0 elements, we're already at the end.
        if n <= 1:
            return 0
        
        # jumps: The number of jumps we've taken so far.
        jumps = 0
        # current_reach: The farthest index we can reach with the current number of jumps.
        current_reach = 0
        # farthest_reach: The absolute farthest index we can reach from any position
        #                 within the current jump's range.
        farthest_reach = 0
        
        # We iterate up to n-1 because we don't need to jump from the last element.
        for i in range(n - 1):
            # At each position 'i', calculate how far we could jump and update
            # the farthest possible reach for our *next* jump.
            farthest_reach = max(farthest_reach, i + nums[i])
            
            # If our loop index 'i' has reached the boundary of our current jump...
            if current_reach == i:
                # ...it's time to make the next jump.
                jumps += 1
                # The new boundary becomes the farthest reach we calculated.
                current_reach = farthest_reach
                
                # An optimization: if the new boundary already reaches or surpasses
                # the end of the array, we can stop and return the answer.
                if current_reach >= n - 1:
                    return jumps
            
        return jumps

class Solution:
    def jump(self, nums):
        n = len(nums)
        if n <= 1:
            return 0
        
        jumps = 0
        current_reach = 0
        farthest_reach = 0
        
        for i in range(n - 1):
            farthest_reach = max(farthest_reach, i + nums[i])
            if current_reach == i:
                jumps += 1
                current_reach = farthest_reach
            if current_reach >= n - 1:
                return jumps
            
        return jumps
    
        