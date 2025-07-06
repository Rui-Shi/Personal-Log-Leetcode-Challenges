# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
# Example 2:

# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
# Example 3:

# Input: numCourses = 1, prerequisites = []
# Output: [0]

from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [i for i in range(numCourses)]
        
        map = defaultdict(list)
        for a, b in prerequisites:
            map[a].append(b)
        
        res = []
        course_taken = set()
        for course in range(numCourses):
            if course not in map:
                res.append(course)
                course_taken.add(course)
                
        if not res:
            return []
        
        while len(res) < numCourses:
            courses_to_take = []
            for course, pres in map.items():
                if course not in course_taken:
                    add = True
                    for pre in pres:
                        if pre not in course_taken:
                            add = False
                            break
                    if add:
                        course_taken.add(course)
                        courses_to_take.append(course)
            if not courses_to_take:
                return []
            else:
                res += courses_to_take
        return res

# A much better one
from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        """
        Finds a valid course order using Kahn's algorithm for topological sorting.
        Returns a valid course order, or an empty list if a cycle exists.
        """
        
        # 1. Initialize graph and prerequisite counts.
        # adj: Adjacency list (prereq -> courses that depend on it).
        # in_degree: Count of prerequisites for each course.
        adj = defaultdict(list)
        in_degree = [0] * numCourses
        
        # 2. Build graph: for prereq [a, b], create edge b -> a.
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degree[course] += 1
            
        # 3. Enqueue all courses with no prerequisites (in-degree of 0).
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        result = []
        
        # 4. Process the queue.
        while queue:
            # Take a course with all prerequisites met.
            course = queue.popleft()
            result.append(course)
            
            # For each neighbor, decrease its prerequisite count.
            for neighbor in adj[course]:
                in_degree[neighbor] -= 1
                
                # If a neighbor has no more prerequisites, enqueue it.
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # 5. Check for cycles. If result length matches numCourses, the order is valid.
        # Otherwise, a cycle was detected, and no valid order exists.
        return result if len(result) == numCourses else []

# A much better one
from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj = defaultdict(list)
        in_degree = [0] * numCourses
        
        for course, pre in prerequisites:
            adj[pre].append(course)
            in_degree[course] += 1
        
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        res = []
        while queue:
            course = queue.popleft()
            res.append(course)
            
            for neighbor in adj[course]:
                in_degree[neighbor] -= 1
                
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return res if len(res) == numCourses else []
            


                    
                    
        
        