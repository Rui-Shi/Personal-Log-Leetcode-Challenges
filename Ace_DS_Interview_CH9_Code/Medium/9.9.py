# determine the longest path of a tree

from typing import Optional

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def max_depth(root: Optional[TreeNode]) -> int:
    """Calculates the maximum depth (height) of a binary tree.

    Args:
        root: The root node of the binary tree (or None for an empty tree).

    Returns:
        The maximum depth of the tree (0 for an empty tree).
    """
    if not root:  # if the root is None
        return 0

    return 1 + max(max_depth(root.left), max_depth(root.right))

# --- Example Usage and Testing ---

# Create a sample tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.left.left.left = TreeNode(7)

# Calculate the maximum depth
depth = max_depth(root)
print(f"The maximum depth of the tree is: {depth}")  # Output: 4

# Test with an empty tree
empty_tree_depth = max_depth(None)
print(f"The maximum depth of an empty tree is: {empty_tree_depth}")  # Output: 0

#Test with a single-node tree
single_node_tree = TreeNode(10)
print(f"The maximum depth of a one node tree is {max_depth(single_node_tree)}") # Output: 1