# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}  # Dictionary to store element counts
        for num in nums:
            counts[num] = counts.get(num, 0) + 1  # Increment or initialize count, if num is found, 
            # it returns its corresponding value, if not found, it returns the second argument you provided, which is 0.

        # Sort items by frequency (descending), The sorted() function returns a sorted list of the specified iterable object.
        sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)
        # In Python, sorted() is a built-in function that returns a new sorted list from the items in any iterable.
        # lambda item: item[1] is an anonymous function, which return item[1], 
        # key: Optional. A Function to execute to decide the order. Default is None

        result = []
        for i in range(k):
            result.append(sorted_counts[i][0])  # Add element to result

        return result
        
# the use of lambda and key with a few more examples, focusing on different scenarios:
words = ["apple", "banana", "kiwi", "grape", "orange"]
sorted_words = sorted(words, key=lambda word: len(word))
print(sorted_words)  # Output: ['kiwi', 'grape', 'apple', 'banana', 'orange']

