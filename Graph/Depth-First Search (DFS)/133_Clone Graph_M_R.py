# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
 

# Test case format:

# For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

# An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

# The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

 

# Example 1:


# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# Example 2:


# Input: adjList = [[]]
# Output: [[]]
# Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
# Example 3:

# Input: adjList = []
# Output: []
# Explanation: This an empty graph, it does not have any nodes.
 

# Constraints:

# The number of nodes in the graph is in the range [0, 100].
# 1 <= Node.val <= 100
# Node.val is unique for each node.
# There are no repeated edges and no self-loops in the graph.
# The Graph is connected and all nodes can be visited starting from the given node.



# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Clones a graph given its starting node.

        Args:
            node: The starting node of the graph to clone.

        Returns:
            The starting node of the cloned graph, or None if the input graph is empty.
        """

        if not node:  # Handle empty graph
            return None

        old_to_new = {}  # Dictionary to store mappings between original and cloned nodes

        def dfs(node):
            """
            Performs a Depth-First Search (DFS) to clone the graph.

            Args:
                n: The current node being visited in the DFS.

            Returns:
                The cloned copy of the node n.
            """

            if node in old_to_new:  # If node is already cloned, return its clone
                return old_to_new[node]

            copy = Node(node.val)  # Create a new node with the same value
            old_to_new[node] = copy  # Store the mapping between original and cloned node

            # Recursively clone the neighbors and assign them to the copy's neighbors
            copy.neighbors = [dfs(neighbor) for neighbor in node.neighbors]
            return copy  # Return the copy 
        return dfs(node)  # Start the DFS from the given node

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        old_to_new_mapping = {}
        
        def dfs_helper(node):
            nonlocal old_to_new_mapping
            if node in old_to_new_mapping:
                return old_to_new_mapping[node]
            else:
                node_copy = Node(node.val)
                old_to_new_mapping[node] = node_copy
                node_copy.neighbors = [dfs_helper(node_neighbor) for node_neighbor in node.neighbors]
            
            return node_copy
        
        return dfs_helper(node)
        