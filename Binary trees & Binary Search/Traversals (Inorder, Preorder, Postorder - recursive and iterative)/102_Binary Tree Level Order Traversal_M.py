# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000


from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Performs a level-order traversal of a binary tree and returns the result as a list of lists.

        Args:
            root: The root node of the binary tree (can be None).

        Returns:
            A list of lists, where each inner list represents a level of the tree, 
            containing the node values from left to right.
        """

        res = []  # Initialize an empty list to store the level-order traversal result.

        def levelTraversal(node_list: List[TreeNode]) -> None:
            """
            Recursively traverses the tree level by level.

            Args:
                node_list: A list of TreeNode objects representing the nodes at the current level.
            """

            nonlocal res  # Indicate that 'res' is a variable in the enclosing scope.

            if len(node_list) > 0:  # Check if the current level has any nodes.
                val_list = []  # Initialize an empty list to store the values of the current level.
                node_list_next = []  # Initialize an empty list to store the nodes of the next level.

                for node in node_list:  # Iterate through the nodes at the current level.
                    if node:  # Check if the node is not None.
                        val_list.append(node.val)  # Append the node's value to the current level's value list.

                        if node.left:  # Check if the node has a left child.
                            node_list_next.append(node.left)  # Append the left child to the next level's node list.

                        if node.right:  # Check if the node has a right child.
                            node_list_next.append(node.right)  # Append the right child to the next level's node list.

                if len(val_list) > 0: # Checks if the val_list has any values. This prevents empty lists from being appended.
                    res.append(val_list)  # Append the current level's value list to the result.

                levelTraversal(node_list_next)  # Recursively call levelTraversal with the next level's node list.

        levelTraversal([root])  # Start the level-order traversal from the root node.

        return res  # Return the level-order traversal result.


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        
        def dfs_helper(node_list):
            nonlocal res
            
            if not node_list:
                return []
            
            cur_level_nodeval = []
            node_list_next = []
            
            for node in node_list:
                if node:
                    cur_level_nodeval.append(node.val)
                
                    if node.left:
                        node_list_next.append(node.left)
                
                    if node.right:
                        node_list_next.append(node.right)
            
            res.append(list(cur_level_nodeval))
            dfs_helper(node_list_next)
        
        dfs_helper([root])
        
        return res
            
            
            
                
                            
            
            