# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

# Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

# Example 1:

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Inserts a new interval into a sorted list of non-overlapping intervals,
        merging if necessary.

        Args:
            intervals: A list of non-overlapping intervals sorted by start time.
            newInterval: The interval to insert.

        Returns:
            A new list of intervals with the new interval inserted and merged.
        """
        res = []
        a = newInterval[0]
        b = newInterval[1]
        n = len(intervals)
        
        i = 0
        while i < n and a > intervals[i][1]:
            res.append(intervals[i])
            i += 1
        
        while i < n and b >= intervals[i][0]:
            a = min(a, intervals[i][0])
            b = max(b, intervals[i][1])
            i += 1
            
        res.append([a, b])
        
        while i < n:
            res.append(intervals[i])
            i += 1
        
        return res
            
        
        

# Helper function to test the solution (optional)
def run_tests():
    solution = Solution()

    # Example 1
    intervals1 = [[1,3],[6,9]]
    newInterval1 = [2,5]
    expected1 = [[1,5],[6,9]]
    result1 = solution.insert(intervals1, newInterval1)
    print(f"Test 1 - Input: {intervals1}, {newInterval1}")
    print(f"Result: {result1}, Expected: {expected1}")
    print(f"Passed: {result1 == expected1}\n")

    # Example 2
    intervals2 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval2 = [4,8]
    expected2 = [[1,2],[3,10],[12,16]]
    result2 = solution.insert(intervals2, newInterval2)
    print(f"Test 2 - Input: {intervals2}, {newInterval2}")
    print(f"Result: {result2}, Expected: {expected2}")
    print(f"Passed: {result2 == expected2}\n")

    # Edge case: Empty intervals list
    intervals3 = []
    newInterval3 = [5,7]
    expected3 = [[5,7]]
    result3 = solution.insert(intervals3, newInterval3)
    print(f"Test 3 - Input: {intervals3}, {newInterval3}")
    print(f"Result: {result3}, Expected: {expected3}")
    print(f"Passed: {result3 == expected3}\n")

    # Edge case: New interval before all others
    intervals4 = [[3,5],[7,9]]
    newInterval4 = [1,2]
    expected4 = [[1,2],[3,5],[7,9]]
    result4 = solution.insert(intervals4, newInterval4)
    print(f"Test 4 - Input: {intervals4}, {newInterval4}")
    print(f"Result: {result4}, Expected: {expected4}")
    print(f"Passed: {result4 == expected4}\n")

    # Edge case: New interval after all others
    intervals5 = [[1,3],[6,9]]
    newInterval5 = [10,12]
    expected5 = [[1,3],[6,9],[10,12]]
    result5 = solution.insert(intervals5, newInterval5)
    print(f"Test 5 - Input: {intervals5}, {newInterval5}")
    print(f"Result: {result5}, Expected: {expected5}")
    print(f"Passed: {result5 == expected5}\n")

    # Edge case: New interval completely covers an existing interval
    intervals6 = [[1,5]]
    newInterval6 = [2,3]
    expected6 = [[1,5]]
    result6 = solution.insert(intervals6, newInterval6)
    print(f"Test 6 - Input: {intervals6}, {newInterval6}")
    print(f"Result: {result6}, Expected: {expected6}")
    print(f"Passed: {result6 == expected6}\n")

    # Edge case: New interval merges multiple intervals
    intervals7 = [[1,2],[4,6],[8,10]]
    newInterval7 = [3,9]
    expected7 = [[1,2],[3,10]]
    result7 = solution.insert(intervals7, newInterval7)
    print(f"Test 7 - Input: {intervals7}, {newInterval7}")
    print(f"Result: {result7}, Expected: {expected7}")
    print(f"Passed: {result7 == expected7}\n")

# Uncomment to run tests
# run_tests()
                