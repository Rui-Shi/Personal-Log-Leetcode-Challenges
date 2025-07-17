# Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

# Example 1:

# Input: root = [1,null,2,3]

# Output: [1,3,2]

# Explanation:



# Example 2:

# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

# Output: [4,2,6,5,7,1,3,9,8]

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
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, node: Optional[TreeNode]) -> List[int]:
        
        if not node:
            return []

        result = []  # Initialize the list to store the inorder traversal
        result = result + self.inorderTraversal(node.left)
        result = result + [node.val]
        result = result + self.inorderTraversal(node.right)

        return result  # Return the list containing the inorder traversal

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        res = []
        if root:
            res += self.inorderTraversal(root.left)
            res += [root.val]
            res += self.inorderTraversal(root.right)
        
        return res
        
