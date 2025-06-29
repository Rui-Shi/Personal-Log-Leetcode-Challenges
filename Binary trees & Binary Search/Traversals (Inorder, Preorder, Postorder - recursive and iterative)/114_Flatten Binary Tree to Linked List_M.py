# Given the root of a binary tree, flatten the tree into a "linked list":

# The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 

# Example 1:


# Input: root = [1,2,5,3,4,null,6]
# Output: [1,null,2,null,3,null,4,null,5,null,6]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [0]
# Output: [0]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def pre_order_helper(root):
            res = []
            
            if not root:
                return res
            
            res.append(root.val)
            res += pre_order_helper(root.left)
            res += pre_order_helper(root.right)
            
            return res
            
        pre_order_list = pre_order_helper(root)
        
        dummy = TreeNode()
        dummy.right = root
        cur = dummy
        
        for num in pre_order_list:
            cur = cur.right
            cur.val = num
            cur.left = None
            cur.right = TreeNode()
        
        
        cur.right = None
        
        return root
        
        
class Solution:
    def preorder_helper(self, root):
        res = []
        if not root:
            return res
        
        res.append(root.val)
        res += self.preorder_helper[root.left]
        res += self.preorder_helper[root.right]
        
        return res
    
    def flatten(self, root: Optional[TreeNode]) -> None:
        value_list = self.preorder_helper(root)
        
        cur = root
        for val in value_list:
            cur.left = None
            cur.val = val
            if cur.right:
                continue
            else:
                cur.right = TreeNode()
                cur = cur.right
        
        cur.right = None
        return root
            
            
            
            
            
        
        
        
        
        