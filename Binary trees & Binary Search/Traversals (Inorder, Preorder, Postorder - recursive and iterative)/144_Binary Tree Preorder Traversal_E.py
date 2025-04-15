# Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

# Example 1:

# Input: root = [1,null,2,3]

# Output: [1,2,3]

# Explanation:



# Example 2:

# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

# Output: [1,2,4,5,6,7,3,8,9]

# Explanation:



# Example 3:

# Input: root = []

# Output: []

# Example 4:

# Input: root = [1]

# Output: [1]

 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
class TreeNode:
    """
    Represents a node in a binary tree.

    Attributes:
        val: The value of the node.
        left: The left child of the node.
        right: The right child of the node.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Performs a preorder traversal of a binary tree.

        Args:
            root: The root of the binary tree.

        Returns:
            A list containing the values of the nodes visited in preorder.
        """
        result = [] # Initialize an empty list to store the result
        if root:
            result.append(root.val)  # Visit the root node (add its value to the result)
            result = result + self.preorderTraversal(root.left)  # Recursively traverse the left subtree and add its result
            result = result + self.preorderTraversal(root.right)  # Recursively traverse the right subtree and add its result
        return result  # Return the final result list