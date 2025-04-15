# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.

 

# Example 1:

# Input: nums1 = [1,2,3], nums2 = [2,4,6]
# Output: [[1,3],[4,6]]
# Explanation:
# For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
# For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].
# Example 2:

# Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
# Output: [[3],[]]
# Explanation:
# For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
# Every integer in nums2 is present in nums1. Therefore, answer[1] = [].

from typing import List


def find_distinct_integers(nums1, nums2):
    """
    Finds distinct integers in two arrays that are not present in the other.

    Args:
        nums1: The first list of integers.
        nums2: The second list of integers.

    Returns:
        A list of two lists:
        - The first list contains distinct integers in nums1 not present in nums2.
        - The second list contains distinct integers in nums2 not present in nums1.
    """

    set1 = set(nums1)
    set2 = set(nums2)

    answer = []
    answer.append(list(set1 - set2))  # Elements in set1 but not in set2
    answer.append(list(set2 - set1))  # Elements in set2 but not in set1

    return answer


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # Convert arrays to sets
        h1 = set(nums1)
        h2 = set(nums2)

        # Remove common elements
        for num in nums2:
            if num in h1:
                h1.discard(num) # Remove an element from a set if it is a member.
                h2.discard(num)

        # Return the remaining unique elements
        return [list(h1), list(h2)]
        