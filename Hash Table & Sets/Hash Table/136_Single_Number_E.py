# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,1]

# Output: 1

# Example 2:

# Input: nums = [4,1,2,1,2]

# Output: 4

# Example 3:

# Input: nums = [1]

# Output: 1

 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.

def singleNumber(nums):
    """
    Finds the single number using a dictionary.

    Args:
        nums: A list of integers.

    Returns:
        The single integer that appears only once.
    """
    counts = {}
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    for num, count in counts.items():
        if count == 1:
            return num
        
# Looping Through Both Keys and Values Using .items() 
my_dict = {"a": 1, "b": 2, "c": 3}

for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

import collections

class Solution:
    def singleNumber(self, nums):
        counts = collections.defaultdict(int)
        
        for num in nums:
            counts[num] += 1
        
        for num, count in counts.items():
            if count == 1:
                return num