# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:


# Input: root = [2,1,3]
# Output: true
# Example 2:


# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low=-float('inf'), high=float('inf')):
            # Empty trees are valid BSTs.
            if not node:
                return True

            # The current node's value must be between low and high.
            if not (low < node.val < high):
                return False

            # Recursively check the left and right subtrees.
            # For the left subtree, the upper bound is the current node's value.
            # For the right subtree, the lower bound is the current node's value.
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))

        return validate(root)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low=-float('inf'), high=float('inf')):
            if not node:
                return True
            
            if not (low < node.val < high):
                return False
            
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        return validate(root)

