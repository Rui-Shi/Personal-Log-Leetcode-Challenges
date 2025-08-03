# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

# For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.

# The replacement must be in place and use only constant extra memory.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [1,3,2]
# Example 2:

# Input: nums = [3,2,1]
# Output: [1,2,3]
# Example 3:

# Input: nums = [1,1,5]
# Output: [1,5,1]
 

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100
# Seen this question in a real interview before?
# 1/5

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Finds the next lexicographical permutation of nums in-place.
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return

        # Step 1: Find the first element from the right that is smaller than the element to its right.
        # This is the "pivot".
        pivot_index = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot_index = i
                break
        
        # If no such element is found, the array is the last permutation (e.g., [3, 2, 1]).
        # Reverse it to get the first permutation (e.g., [1, 2, 3]).
        if pivot_index == -1:
            nums.reverse()
            return
            
        # Step 2: Find the smallest element to the right of the pivot that is greater than the pivot.
        for j in range(n - 1, pivot_index, -1):
            if nums[j] > nums[pivot_index]:
                # Step 3: Swap the pivot with this successor element.
                nums[pivot_index], nums[j] = nums[j], nums[pivot_index]
                break
        
        # Step 4: Reverse the portion of the array to the right of the pivot's position.
        # This ensures the new suffix is the smallest possible permutation.
        left, right = pivot_index + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


## The Logic Explained with an Example
# Let's use the array nums = [1, 5, 4, 3, 2].

# 1. Before the Reversal Step
# Find Pivot: The pivot is 1 (since 1 < 5, and everything to the right of 1 is in descending order).

# Find Successor: The smallest number to the right of 1 that's bigger than 1 is 2.

# Swap: Swap the pivot (1) and the successor (2).

# At this point, just before Step 4, our array looks like this: [2, 5, 4, 3, 1]

# 2. Why This Isn't the Answer
# The array [2, 5, 4, 3, 1] is definitely larger than the original [1, 5, 4, 3, 2]. But is it the very next one?

# No. The prefix is now 2, which is correct. But the suffix [5, 4, 3, 1] is in descending order, making it the largest possible arrangement of those four numbers. We want the smallest possible arrangement to ensure our final number is the smallest possible increase.

# 3. The Solution: Reverse! 💡
# To make the suffix [5, 4, 3, 1] as small as possible, we need to sort it in ascending order.

# A key insight of the algorithm is that the suffix after the swap is always in descending order. The easiest way to sort a descending sequence into an ascending one is to simply reverse it.

# Reverse [5, 4, 3, 1] to get [1, 3, 4, 5].

# Now, attach this smallest possible suffix to our new prefix:

# Final Result: [2, 1, 3, 4, 5]

# This is the true "next permutation" after [1, 5, 4, 3, 2].
        