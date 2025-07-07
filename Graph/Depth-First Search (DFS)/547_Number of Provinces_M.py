# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

 

# Example 1:


# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
# Example 2:


# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3

from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        n = len(isConnected)
        res = 0
        
        def dfs_helper(i):
            visited.add(i)
            for j, value in enumerate(isConnected[i]):
                if value == 1 and j not in visited:
                    dfs_helper(j)
        
        for i in range(n):
            if i not in visited:
                res += 1
                dfs_helper(i)
        
        return res


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        
        n = len(isConnected)
        
        if n == 1:
            return 1
        
        def dfs_helper(start):
            nonlocal visited
            visited.add(start)
            for neighbor in range(n):
                if neighbor not in visited and isConnected[start][neighbor] ==:
                    dfs_helper(neighbor)
        
        count = 0
        for i in range(n):
            if i not in visited:
                dfs_helper(i)
                count += 1
        
        return count
            
        
        
        
            
        
                    
                    