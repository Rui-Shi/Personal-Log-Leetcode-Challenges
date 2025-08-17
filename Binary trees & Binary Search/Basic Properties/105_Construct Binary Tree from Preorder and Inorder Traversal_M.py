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

# Time: O(n^2)
# Space: O(n^2)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        root_val = preorder[0]
        root = TreeNode(root_val)
        split_index = inorder.index(root_val) # get the index of the spliting point time: O(n)
        
        root.left = self.buildTree(preorder[1:(1 + split_index)], inorder[0:split_index]) # Slicing O(n)
        root.right = self.buildTree(preorder[(1 + split_index):], inorder[(1 + split_index):])
        
        return root

# Recursion Stack Depth: The depth of recursive calls is equal to the height of the tree, H. 
# In the worst case of a skewed tree, H=N, so the stack itself requires O(N) space.

# Storage for Slices: This is the main contributor. At each level of recursion, 
# new lists are created and stored in memory for the next call. In the worst case of a skewed tree, 
# you have recursive calls with lists of size N, N−1, N−2, ..., down to 1. The total space consumed by 
# all these stored slices across the entire call stack is also an arithmetic series, resulting in O(N^2) space

        
        
        
    