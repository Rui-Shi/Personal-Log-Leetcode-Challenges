# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

# Example 1:


# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# Example 2:

# Input: preorder = [-1], inorder = [-1]
# Output: [-1]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder:
            return None
        
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        split_index = inorder.index(root_val)
        
        root.left = self.buildTree(preorder[1:(1+split_index)], inorder[0:split_index])
        root.right = self.buildTree(preorder[(1+split_index):], inorder[(split_index+1):])
        
        return root
        
        
        
    