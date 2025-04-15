# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

 

# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.

from typing import List


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 0
        if len(nums)==0:
            return k
        k = 1
        i = 1
        while i<= len(nums)-1:
            if nums[i]==nums[i-1]:
                nums.pop(i)
            else:
                k += 1
                i += 1
        return k
    
s = Solution()
nums=[0,0,1,1,1,2,2,3,3,4]
s.removeDuplicates(nums)
print(nums)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
    
        """
        :type nums: List[int]
        :rtype: int
        """
        # Dictionary to track the frequency of elements (not actually used for counting in the final solution)
        d = {}
        
        # Loop over the input list to build the dictionary
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        # Overwrite the input list with the unique elements in their original order
        # nums[:] = ... modifies the list in place, preserving its identity
        nums[:] = list(d.keys())  # `d.keys()` gives the unique elements 

        # Return the length of the list after removing duplicates
        return len(nums)
    
# Function 2 has a linear time complexity (O(n)), while Function 1 has a quadratic time complexity (O(n^2)) due to .pop() 
