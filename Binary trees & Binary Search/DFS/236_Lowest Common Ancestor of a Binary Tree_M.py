# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

# Example 1:


# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# Example 2:


# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
# Example 3:

# Input: root = [1,2], p = 1, q = 2
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [2, 105].
# -109 <= Node.val <= 109
# All Node.val are unique.
# p != q
# p and q will exist in the tree.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def lowestCommonAncestor(self,
                             root: Optional[TreeNode],
                             p: TreeNode,
                             q: TreeNode
                            ) -> Optional[TreeNode]:
        
        # If the root is null, or it's one of the nodes we're looking for, return the root.
        if root in (None, p, q):
            return root
        
        # Recursively search for p and q in the left and right subtrees.
        left_result = self.lowestCommonAncestor(root.left, p, q)
        right_result = self.lowestCommonAncestor(root.right, p, q)
        
        # If both p and q are found in different subtrees, the current root is their LCA.
        if left_result and right_result:
            return root
        
        # Otherwise, the LCA is in the subtree where a node was found.
        else:
            return left_result or right_result

class Solution:
    def lowestCommonAncestor(self,
                           root: Optional[TreeNode],
                           p: TreeNode,
                           q: TreeNode
                          ) -> Optional[TreeNode]:
        
        if root in (None, p, q):
            return root
        
        else:
            left_result = self.lowestCommonAncestor(root.left, p, q)
            right_result = self.lowestCommonAncestor(root.right, p, q)
        
        if left_result and right_result:
            return root
        
        else: 
            return left_result or right_result # return the object that is not None