# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

 

# Example 1:


# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# Example 2:

# Input: root = [1,2]
# Output: 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# My solution
class Solution:
    def height(self, Node):
        if not Node:
            return 0
        return max(self.height(Node.left), self.height(Node.right)) + 1
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        
        diameter_through_root = left_height + right_height
        
        left_diameter = self.diameterOfBinaryTree(root.left)
        right_diameter = self.diameterOfBinaryTree(root.right)
        
        return max(diameter_through_root, left_diameter, right_diameter)

# A better solution which traversal each node for only once
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Calculates the diameter of a binary tree.

        The diameter of a binary tree is the length of the longest path between
        any two nodes in a tree. This path may or may not pass through the root.

        Args:
            root: The root node of the binary tree.

        Returns:
            The diameter of the binary tree.
        """
        res = 0  # Initialize the variable to store the maximum diameter found so far.

        # Inner helper function (depth-first search)
        def dfs(root: Optional[TreeNode]) -> int:
            """
            Performs a depth-first search to calculate the depth of each subtree
            and update the maximum diameter.

            Args:
                root: The current node being visited.

            Returns:
                The depth of the subtree rooted at the current node.
            """
            # Without nonlocal, if you tried to assign a new value to res within the nested function, 
            # Python would treat it as a new local variable.
            nonlocal res  # Allows modification of the 'res' variable in the outer scope

            if not root:  # Base case: If the current node is None (empty subtree)
                return 0  # The depth of an empty subtree is 0

            # Recursive calls to calculate the depths of the left and right subtrees
            left = dfs(root.left)
            right = dfs(root.right)

            # Update the maximum diameter:
            #   - The diameter passing through the current node is the sum of the
            #     depths of its left and right subtrees.
            #   - We take the maximum of the current 'res' and this new diameter.
            res = max(res, left + right)

            # Return the depth of the current subtree:
            #   - It's 1 (for the current node) + the maximum depth of its left or right subtree.
            return 1 + max(left, right)

        dfs(root)  # Start the depth-first search from the root node
        return res  # Return the final maximum diameter
            
            