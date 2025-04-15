# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

# Return the answers to all queries. If a single answer cannot be determined, return -1.0.

# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

# Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

 

# Example 1:

# Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
# Explanation: 
# Given: a / b = 2.0, b / c = 3.0
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
# return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
# note: x is undefined => -1.0
# Example 2:

# Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# Output: [3.75000,0.40000,5.00000,0.20000]
# Example 3:

# Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
# Output: [0.50000,2.00000,-1.00000,-1.00000]

from typing import List

import collections
# import sys
# sys.setrecursionlimit(2000) # Optional: Increase recursion depth if needed

import collections # <-- Added import

class Solution:
    def calcEquation(self, equations, values, queries):
        """
        Calculates the result of division queries based on a set of known equations.

        Args:
            equations: A list of pairs of strings, e.g., [["a", "b"], ["b", "c"]].
            values: A list of floats, corresponding values for equations, e.g., [2.0, 3.0].
            queries: A list of pairs of strings representing the queries, e.g., [["a", "c"], ["b", "a"]].

        Returns:
            A list of floats containing the results for each query. 
            Returns -1.0 for queries that cannot be answered.
        """

        # Renamed helper function for clarity (Depth-First Search)
        def dfs_helper(graph, cur_node, tar_node, visited, cur_product):
            """Helper function to perform DFS and calculate product along the path."""
            
            # Mark current node as visited for this specific DFS path
            visited.add(cur_node) 
            
            # Base case: Found the target node
            if cur_node == tar_node:
                return cur_product

            # Explore neighbors
            if cur_node in graph: # Check if cur_node exists in the graph keys
                for neighbor, value in graph[cur_node].items():
                    if neighbor not in visited: # Only explore unvisited neighbors
                        result = dfs_helper(graph, neighbor, tar_node, visited, cur_product * value)
                        
                        # If a valid path is found through this neighbor, return the result immediately
                        if result != -1.0:
                            return result
            
            # Backtrack: If no path found from cur_node or its unexplored neighbors
            # No need to explicitly remove from visited here, as a fresh set is used for each query.
            return -1.0

        # Build the graph: graph[node] -> {neighbor: value} where value = node / neighbor
        graph = collections.defaultdict(dict)
        variables = set()

        for i, (u, v) in enumerate(equations):
            if values[i] != 0: # Avoid division by zero if a value is 0
                graph[u][v] = values[i]
                graph[v][u] = 1.0 / values[i]
            variables.add(u)
            variables.add(v)

        # Remove redundant initialization: visited = {} 

        results = []

        for u, v in queries:
            # Check 1: If either variable is not in the graph at all
            if u not in variables or v not in variables:
                results.append(-1.0) # Append result for this query
                continue # Move to the next query <--- Fix: Use continue instead of return

            # Check 2: If query is like "a" / "a"
            elif u == v:
                results.append(1.0) # Append result for this query
                continue # Move to the next query <--- Fix: Use continue instead of return

            # Check 3: Perform DFS for valid queries
            else:
                visited = set() # Reset visited set for each new query's DFS
                # Start DFS from u, aiming for v, with initial product 1.0
                answer = dfs_helper(graph, u, v, visited, 1.0)
                results.append(answer) # Append the DFS result

        return results # <-- Added final return statement
                
            
            
       

# Example Usage (kept for clarity, can be removed)
# sol = Solution()
# equations1 = [["a","b"],["b","c"]]
# values1 = [2.0,3.0]
# queries1 = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# print(f"Example 1 Output (DFS, less notation): {sol.calcEquation(equations1, values1, queries1)}")