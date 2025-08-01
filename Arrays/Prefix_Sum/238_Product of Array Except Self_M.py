# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

from math import prod  # Imports the prod function from the math module (Python 3.8+)
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)  # Get the length of the input list 'nums'.
        
        # Optimization: If there are more than one zero, all results will be zero.
        if nums.count(0) > 1:  
            return [0] * n  # Return a list of zeros with the same length as 'nums'.

        nums_temp = nums # Create a copy of nums. This line is unnecessary and doesn't affect the algorithm
        product_cum = prod(nums)  # Calculate the product of ALL elements in 'nums' using math.prod.
                                  # This includes zeros, which will make product_cum zero if any zeros exist.
        res = []  # Initialize an empty list to store the results.

        for i, num in enumerate(nums):  # Iterate through 'nums' with both index (i) and value (num).
            if num != 0:  # If the current element is NOT zero:
                res.append(int(product_cum / num))  # Divide the total product by the current element and append to 'res'.
                                                    # This is where potential division by zero could occur if product_cum is very large and num is very small
            else:  # If the current element IS zero:
                if i != n - 1:  # If it's NOT the last element:
                    res.append(prod(nums[:i] + nums[i+1:]))  # Calculate the product of all elements *except* the current one
                                                        # by slicing the list before and after the current index and concatenating.
                                                        # This is VERY inefficient (O(n) within the loop, making the overall complexity O(n^2)).
                else:  # If it's the last element:
                    res.append(prod(nums[:i]))  # Calculate the product of all elements before the last one.
                                                #  Still inefficient, but slightly less so than the previous case.
        return res  # Return the result list.


# A better one

from typing import List
import math  # Import the math module (though prod isn't strictly needed here, it could be used)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)  # Get the length of the input list.
        zero_count = nums.count(0)  # Count the number of zeros in the list.

        # Optimization: If there are more than one zero, the result is all zeros.
        if zero_count > 1:
            return [0] * n  # Return a list of zeros.

        total_product = 1  # Initialize the product to 1 (multiplicative identity).
        for x in nums:  # Iterate through the list.
            if x != 0:  # Calculate the product of NON-ZERO elements ONLY.
                total_product *= x

        result = []  # Initialize an empty list for the results.
        for x in nums:  # Iterate through the list AGAIN.
            if zero_count == 0:  # If there were NO zeros in the original list:
                result.append(total_product // x)  # Integer division to get the product except self.
            elif x == 0:  # If the current element IS zero, and there's only one zero:
                result.append(total_product)  # The result is the product of all non-zero elements.
            else:  # If the current element is NOT zero, but there was a zero elsewhere:
                result.append(0)  # The result is zero.
        return result  # Return the result list.

# Time complexity: O(n)

class Solution:
    def productExceptSelf(self,nums):
        pre_fix = [1] * len(nums)
        pre_fix_inverse = [1] * len(nums)
        nums_inverse = nums[::-1]
        
        for i in range(1, len(nums)):
            pre_fix[i] = pre_fix[i-1] * nums[i-1]
            pre_fix_inverse[i] = pre_fix_inverse[i-1] * nums_inverse[i-1]
        
        pre_fix_inverse = pre_fix_inverse[::-1]
        
        res = []
        
        for i in range(len(nums)):
            res.append(pre_fix[i] * pre_fix_inverse[i])
        
        return res


class Solution:
    def productExceptSelf(self,nums):
        """
        Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
        You must write an algorithm that runs in O(n) time and without using the division operation.

        Args:
            nums: A list of integers.

        Returns:
            A list of integers.
        """
        n = len(nums)
        answer = [1] * n
        
        # Calculate prefix products
        prefix = 1
        for i in range(1, n):
            prefix *= nums[i - 1]
            answer[i] *= prefix
        
        # Calculate suffix products and multiply with prefix products
        suffix = 1
        for i in range(n - 2, -1, -1):
            suffix *= nums[i + 1]
            answer[i] *= suffix
        
        return answer
    


        
    