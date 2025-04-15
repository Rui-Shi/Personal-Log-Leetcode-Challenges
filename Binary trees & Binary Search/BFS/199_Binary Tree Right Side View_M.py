# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

# Example 1:

# Input: root = [1,2,3,null,5,null,4]

# Output: [1,3,4]

# Explanation:



# Example 2:

# Input: root = [1,2,3,4,null,null,null,5]

# Output: [1,3,4,5]

# Explanation:



# Example 3:

# Input: root = [1,null,3]

# Output: [1,3]

# Example 4:

# Input: root = []

# Output: []


# Definition for a binary tree node.
from typing import Optional


from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # --- FIX 1: Handle the empty tree case explicitly ---
        if not root:
            return []
        # --- End Fix 1 ---

        # Helper function to perform BFS and return lists of nodes per level
        def bfs_helpter(node_list_arg):
            res_levels = [] # Renamed to avoid confusion

            current_level_nodes = list(node_list_arg) # Start with a copy
            next_level_nodes = []

            # Loop while there are nodes in the current level
            while current_level_nodes:

                # --- FIX 2: Append a COPY of the current level ---
                # This prevents later modifications via [:] from affecting stored levels
                res_levels.append(list(current_level_nodes))
                # --- End Fix 2 ---

                next_level_nodes.clear() # Clear list for the next level

                # Process each node in the current level
                for node in current_level_nodes:
                    # Add children to the next level list
                    if node.left:
                        next_level_nodes.append(node.left)
                    if node.right:
                        next_level_nodes.append(node.right)

                # Update current_level_nodes for the next iteration
                # Modifying in place is okay here since we appended a copy above
                current_level_nodes[:] = next_level_nodes

            return res_levels

        # Call the helper function (root is guaranteed not to be None here)
        bfs_res = bfs_helpter([root])
        # print(bfs_res) # For debugging: Now shows correct lists like [[Node1], [Node2, Node3], ...]

        right_view = []
        # Iterate through the list of node lists returned by the helper
        for node_list_level in bfs_res:
             # Safety check (optional but good practice)
            if node_list_level:
                # Append the value of the last node in the list (the rightmost one)
                right_view.append(node_list_level[-1].val) # Now node_list_level won't be empty

        return right_view
            
                    


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        def bfs_helpter(node_list):
            res = []
            
            current_level = node_list
            next_level = []
            
            while current_level:
                res.append(list(current_level))

                next_level.clear()
                for node in current_level:
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
                        
                current_level = list(next_level)
            return res
        
        bfs_res = bfs_helpter([root])
        right_view = []
        for node_list in bfs_res:
            right_view.append(node_list[-1].val)
            
        return right_view 