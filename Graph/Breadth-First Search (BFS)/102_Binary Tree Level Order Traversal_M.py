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

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        
        def levelTraversal(node_list: List[TreeNode]) -> None:
            nonlocal res
            
            if len(node_list) > 0:
                val_list = []
                next_nodes = []
                
                for node in node_list:
                    val_list.append(node.val)
                    
                    if node.left:
                        next_nodes.append(node.left)
                    
                    if node.right:
                        next_nodes.append(node.right)
                
                if len(val_list) > 0:
                    res.append(val_list)
              
                levelTraversal(next_nodes)
                
        levelTraversal([root])
        
        return res   
        
        
        
        