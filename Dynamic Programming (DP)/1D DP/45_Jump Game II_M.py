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
    """
    Calculates the minimum number of jumps to reach the last index of an array.

    Args:
        nums: An integer array representing jump lengths.

    Returns:
        The minimum number of jumps.
    """

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
        