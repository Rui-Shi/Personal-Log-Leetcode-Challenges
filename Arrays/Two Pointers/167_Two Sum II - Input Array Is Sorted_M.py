# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

 

# Example 1:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
# Example 2:

# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
# Example 3:

# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

# using hashmap: O(n)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numMap = {}
        for i in range(len(numbers)):
            curr = numbers[i]
            x = target - curr
            if x in numMap:
                return [numMap[x]+1, i+1]
            else:
                numMap[curr] = i
        return []

# The code iterates through the nums list only once using a for loop.  Inside the loop, the operations performed 
# (checking for x in numMap, accessing and storing values in numMap) 
# take constant time on average, thanks to the use of a hash map (dictionary in Python). 
# Hash map lookups, insertions, and deletions have an average time complexity of O(1).

# Since the loop runs n times, and each iteration takes constant time, the overall time complexity is O(n) * O(1) = O(n).

# use two pointer:
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            if numbers[left] + numbers[right] < target:
                while left < right and numbers[left] == numbers[left + 1]:
                    left += 1
                left += 1
            
            elif numbers[left] + numbers[right] > target:
                while left < right and numbers[right] == numbers[right - 1]:
                    right -= 1
                right -= 1
            
            else:
                return [left + 1, right + 1]
        
        return []