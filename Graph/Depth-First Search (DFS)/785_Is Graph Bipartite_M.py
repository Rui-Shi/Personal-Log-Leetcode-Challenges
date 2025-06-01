# There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

# There are no self-edges (graph[u] does not contain u).
# There are no parallel edges (graph[u] does not contain duplicate values).
# If v is in graph[u], then u is in graph[v] (the graph is undirected).
# The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
# A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

# Return true if and only if it is bipartite.

 

# Example 1:


# Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
# Output: false
# Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.
# Example 2:


# Input: graph = [[1,3],[0,2],[1,3],[0,2]]
# Output: true
# Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.
 

# Constraints:

# graph.length == n
# 1 <= n <= 100
# 0 <= graph[u].length < n
# 0 <= graph[u][i] <= n - 1
# graph[u] does not contain u.
# All the values of graph[u] are unique.
# If graph[u] contains v, then graph[v] contains u.

class Solution:
    def isBipartite(self, graph):
        """
        Checks if the given graph is bipartite.

        A graph is bipartite if its nodes can be divided into two disjoint and independent sets, U and V,
        such that every edge connects a node in U to one in V.
        In other words, we can color the graph with two colors such that no two adjacent nodes have the same color.

        Args:
            graph: A list of lists representing the adjacency list of the graph.
                   graph[i] is a list of neighbors of node i.

        Returns:
            True if the graph is bipartite, False otherwise.
        """
        color = {} # Initialize a dictionary to store the color of each node.
                    # color[node] = 0 or 1, representing two different colors.
                    # Nodes not in color dictionary are uncolored.

        def dfs(pos):
            """
            Depth First Search function to color the graph and check for bipartiteness.

            Args:
                pos: The current node being visited.

            Returns:
                True if the subgraph explored from 'pos' is bipartite, False otherwise.
            """
            for neighbor in graph[pos]: # Iterate through all neighbors of the current node 'pos'. Let's rename 'i' to 'neighbor' for clarity.
                if neighbor in color: # Check if the neighbor has already been colored.
                    if color[neighbor] == color[pos]: # If the neighbor is colored and has the same color as the current node,
                                                      # then the graph is not bipartite because there is an edge between two nodes of the same color.
                        return False # Return False, indicating the graph is not bipartite.
                else: # If the neighbor is not colored yet.
                    color[neighbor] = 1 - color[pos] # Assign the opposite color to the neighbor.
                                                      # If current node 'pos' is color 0, neighbor gets color 1, and vice-versa.
                    if not dfs(neighbor): # Recursively call DFS on the neighbor to continue coloring the graph.
                                        # If the recursive call returns False, it means a conflict was found down the path,
                                        # so we propagate False upwards.
                        return False # Return False, indicating the graph is not bipartite.
            return True # If the loop finishes without finding any conflict for the current node 'pos',
                         # it means the subgraph explored from 'pos' is bipartite so far.

        for i in range(len(graph)): # Iterate through all nodes in the graph.
                                    # This loop is important to handle disconnected graphs.
            if i not in color: # Check if the current node 'i' is already colored.
                                # If not colored, it means we are starting a DFS from a new component or a single node.
                color[i] = 0 # Start coloring the current component by assigning color 0 to the starting node 'i'.
                if not dfs(i): # Start DFS from node 'i'. If DFS returns False, it means the graph is not bipartite.
                    return False # Return False, indicating the graph is not bipartite.

        return True # If all components are checked and no conflict is found, it means the graph is bipartite.
    
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        
        def dfs_helper(node):
            nonlocal color
            
            for neigh in graph[node]:
                if neigh in color:
                    if color[neigh] == color[node]:
                        return False
                else:
                    color[neigh] = 1 - color[node]
                    if not dfs_helper(neigh):
                        return False
            return True
                                
                
        for i in range(len(graph)): # Iterate through all nodes in the graph, This loop is important to handle disconnected graphs.
            if i not in color:
                color[i] = 0
                if not dfs_helper(i):
                    return False
        return True
                            
                
                
                
                
            
        