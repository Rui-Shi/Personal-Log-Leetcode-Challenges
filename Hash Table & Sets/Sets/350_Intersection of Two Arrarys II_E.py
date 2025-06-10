# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000

from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_counts = Counter(nums1)
        nums2_counts = Counter(nums2)
        
        res = []
        for num in nums1_counts:
            if num in nums2_counts:
                res += min(nums1_counts[num], nums2_counts[num])*[num]
        return res

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_count = Counter(nums1)
        nums2_count = Counter(nums2)
        
        res = []
        for num in nums1_count:
            if num in nums2_count:
                res += min(nums1_count[num], nums2_count[num])*[num]
            
        
        