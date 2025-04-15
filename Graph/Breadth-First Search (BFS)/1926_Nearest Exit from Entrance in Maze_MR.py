# You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

# In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

# Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

 

# Example 1:


# Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
# Output: 1
# Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
# Initially, you are at the entrance cell [1,2].
# - You can reach [1,0] by moving 2 steps left.
# - You can reach [0,2] by moving 1 step up.
# It is impossible to reach [2,3] from the entrance.
# Thus, the nearest exit is [0,2], which is 1 step away.
# Example 2:


# Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
# Output: 2
# Explanation: There is 1 exit in this maze at [1,2].
# [1,0] does not count as an exit since it is the entrance cell.
# Initially, you are at the entrance cell [1,0].
# - You can reach [1,2] by moving 2 steps right.
# Thus, the nearest exit is [1,2], which is 2 steps away.
# Example 3:


# Input: maze = [[".","+"]], entrance = [0,0]
# Output: -1
# Explanation: There are no exits in this maze.

from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = {(entrance[0], entrance[1]):1}
        
        nrow = len(maze)
        ncol = len(maze[0])
        
        res = []
        
        def dfs_helper(r, c, maze, current_steps, visited):
            nonlocal res
            for dr, dc in dirs:
                r_new = r + dr
                c_new = c + dc
                
                if 0<= r_new < nrow and 0<= c_new < ncol and maze[r_new][c_new] == "." and (r_new, c_new) not in visited:
                    visited[(r_new, c_new)] = 1
                    if r_new == nrow - 1 or c_new == ncol - 1 or r_new == 0 or c_new == 0:
                        res.append(current_steps + 1)
                    
                    else:
                        dfs_helper(r_new, c_new, maze, current_steps + 1, visited)
        
        dfs_helper(entrance[0], entrance[1], maze, 0, visited)
        
        if not res:
            return -1
        
        else:
            return min(res)

# a better one, which use bfs:

import collections

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        nrow = len(maze)
        ncol = len(maze[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Use a queue for BFS: store (row, col, steps)
        # collections.deque is efficient for queue operations
        q = collections.deque([(entrance[0], entrance[1], 0)])

        # Use a set to keep track of visited cells
        visited = set([(entrance[0], entrance[1])])

        while q:
            r, c, steps = q.popleft()

            # Check neighbors
            for dr, dc in dirs:
                r_new = r + dr
                c_new = c + dc

                # Check if the new cell is valid and not visited
                if 0 <= r_new < nrow and 0 <= c_new < ncol and \
                   maze[r_new][c_new] == '.' and (r_new, c_new) not in visited:

                    # Check if it's an exit (on the border)
                    # Important: It must NOT be the starting entrance cell itself
                    # Since we start BFS from entrance and only check neighbors,
                    # any border cell found here cannot be the original entrance.
                    if r_new == 0 or r_new == nrow - 1 or c_new == 0 or c_new == ncol - 1:
                        # Found the shortest path to an exit
                        return steps + 1

                    # Mark as visited and add to the queue for further exploration
                    visited.add((r_new, c_new))
                    q.append((r_new, c_new, steps + 1))

        # If the queue becomes empty and no exit was found
        return -1
                    
                    
            
        