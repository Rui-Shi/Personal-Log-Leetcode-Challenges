# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

# Constraints:

# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals) == 0:
            return []
        
        if len(intervals) == 1:
            return intervals
        
        res = []
        
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        
        a = sorted_intervals[0][0]
        b = sorted_intervals[0][1]
        
        for i in range(1, len(intervals)):
            if b >= sorted_intervals[i][0]:
                b = max(sorted_intervals[i][1], b)
            
            else:
                res.append([a, b])
                a = sorted_intervals[i][0]
                b = sorted_intervals[i][1]
            
        res.append([a, b])
        
        return res
            
            
            
        
        
        
