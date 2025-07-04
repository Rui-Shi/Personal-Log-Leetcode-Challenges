# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

# Example 1:


# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
# Example 2:


# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
# Example 3:

# Input: root = [2,1], p = 2, q = 1
# Output: 2

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # Make sure p's value is smaller than q's value for easier comparison
        if p.val > q.val:
            p, q = q, p

        current = root
        while current:
            if p.val <= current.val <= q.val:
                # If current.val is between p.val and q.val (inclusive),
                # then current is the LCA.  This handles the case where
                # current is p or q itself (a node can be its own ancestor).
                return current
            elif current.val < p.val:
                # If both p and q are greater than current.val,
                # the LCA must be in the right subtree.
                current = current.right
            else:  # current.val > q.val
                # If both p and q are smaller than current.val,
                # the LCA must be in the left subtree.
                current = current.left

        return None  # Should not reach here for a valid BST and p, q in the BST


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
        
        current = root
        while current:
            if p.val <= current.val <= q.val:
                return current
            elif current.val < p.val:
                current = current.right
            else:
                current = current.left
        return None
                

        