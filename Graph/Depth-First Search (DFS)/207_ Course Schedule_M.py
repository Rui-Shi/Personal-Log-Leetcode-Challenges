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

# use DFS
def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    # 1. Build the adjacency list
    adj = {i: [] for i in range(numCourses)}
    for course, prereq in prerequisites:
        adj[prereq].append(course)

    # 2. Initialize visited array (0: unvisited, 1: visiting, 2: visited)
    visited = [0] * numCourses

    def dfs(course: int) -> bool:
        # Mark as visiting
        visited[course] = 1

        for neighbor in adj[course]:
            if visited[neighbor] == 1:
                # Cycle detected
                return False
            if visited[neighbor] == 0:
                if not dfs(neighbor):
                    return False
        
        # Mark as visited
        visited[course] = 2
        return True

    # 3. Iterate through all courses to handle disconnected graph components
    for i in range(numCourses):
        if visited[i] == 0:
            if not dfs(i):
                return False
    
    # 4. If all DFS traversals complete, no cycle was found
    return True

# Example 1:
numCourses1 = 2
prerequisites1 = [[1, 0]]
print(f"Output for Example 1: {canFinish(numCourses1, prerequisites1)}")  # Expected: true

# Example 2:
numCourses2 = 2
prerequisites2 = [[1, 0], [0, 1]]
print(f"Output for Example 2: {canFinish(numCourses2, prerequisites2)}")  # Expected: false                     
                    
# Time complexity: O(V + E)
from collections import deque
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = len(prerequisites)
        
        if n <= 1 or numCourses <= 1:
            return True
        
        graph = defaultdict(list)
        for course, prere in prerequisites:
            graph[prere].append(course)
        
        visited = [0] * numCourses
        
        def dfs_helper(i):
            visited[i] = 1
            
            for neighbor in graph[i]:
                # a cycle found
                if visited[neighbor] == 1:
                    return False
                
                if visited[neighbor] == 0: 
                    if not dfs_helper(neighbor):
                        return False
            
            visited[i] = 2
            return True
        
        for i in range(numCourses):
            if visited[i] == 0:
                if not dfs_helper(i):
                    return False
        return True
            
                   
                
        
        
                
                