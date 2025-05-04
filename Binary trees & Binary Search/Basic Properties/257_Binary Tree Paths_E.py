# Given the root of a binary tree, return all root-to-leaf paths in any order.


# A leaf is a node with no children.

 


# Example 1:



# Input: root = [1,2,3,null,5]

# Output: ["1->2->5","1->3"]

# Example 2:


# Input: root = [1]

# Output: ["1"]
 


# Constraints:


# The number of nodes in the tree is in the range [1, 100].

# -100 <= Node.val <= 100


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return None
        else:
            start = f"{root.val}"
            
        if root.left and root.right:
            path_list_left = [start + "->" + path for path in self.binaryTreePaths(root.left)]
            path_list_right = [start + "->" + path for path in self.binaryTreePaths(root.right)]
        elif root.left and not root.right:
            path_list_left = [start + "->" + path for path in self.binaryTreePaths(root.left)]
            path_list_right = []
        elif not root.left and root.right:
            path_list_left = []
            path_list_right = [start + "->" + path for path in self.binaryTreePaths(root.right)]
        else:
            path_list_left = [start]
            path_list_right = []

        return path_list_left + path_list_right
            
        
        