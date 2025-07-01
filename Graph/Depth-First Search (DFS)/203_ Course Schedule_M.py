# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

# Constraints:

# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.

from collections import deque
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = len(prerequisites)
        
        if n <= 1 or numCourses <= 1:
            return True
        
        map = defaultdict(set)
        
        for a, b in prerequisites:
            map[b].add(a)
        
        taken = set()
        
        for course in range(numCourses):
            if course not in map:
                taken.add(course)
        
        if not taken:
            return False
        
        else:
            stop = False
            while not stop:
                stop = True
                for course in map:
                    if course not in taken:
                        if sum([pre_req in taken for pre_req in map[course]]) == len(map[course]):
                            taken.add(course)
                            stop = False
        return len(taken) == numCourses
                        
                    
                
                
        
        
                
                