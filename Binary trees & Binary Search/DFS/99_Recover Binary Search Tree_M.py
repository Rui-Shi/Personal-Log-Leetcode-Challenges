# You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

 

# Example 1:


# Input: root = [1,3,null,null,2]
# Output: [3,1,null,null,2]
# Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
# Example 2:


# Input: root = [3,1,4,null,null,2]
# Output: [2,1,4,null,null,3]
# Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
 

# Constraints:

# The number of nodes in the tree is in the range [2, 1000].
# -231 <= Node.val <= 231 - 1
 

# Follow up: A solution using O(n) space is pretty straight-forward. Could you devise a constant O(1) space solution?


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        # Pointers to store the two nodes that need their values swapped.
        self.first = None
        self.second = None
        # Pointer to track the previously visited node in the in-order traversal.
        self.prev = None

        # Helper function to perform in-order traversal.
        def inorder(node: Optional[TreeNode]):
            # Base case for the recursion.
            if not node:
                return

            # 1. Traverse the left subtree.
            inorder(node.left)

            # 2. Process the current node.
            # This is the core logic to find the swapped nodes.
            # In a valid BST, prev.val should always be less than node.val.
            if self.prev and self.prev.val > node.val:
                # A violation is found!
                
                # If this is the first violation we've found, it means 'self.prev'
                # is the first of the two swapped nodes.
                if not self.first:
                    self.first = self.prev
                
                # The 'second' node is the current 'node'. This handles both adjacent
                # and non-adjacent swaps. If it's a non-adjacent swap, this
                # pointer will be updated again when we find the second violation.
                self.second = node
            
            # Update 'prev' to the current node before moving to the right subtree.
            self.prev = node

            # 3. Traverse the right subtree.
            inorder(node.right)

        # Start the in-order traversal from the root.
        inorder(root)

        # After the traversal, 'first' and 'second' hold the two incorrect nodes.
        # Swap their values to recover the BST.
        self.first.val, self.second.val = self.second.val, self.first.val

# Time: O(n)
# Space: O(h) the height of the tree, 
# and the maximum amount of space it needs is determined by the depth of the recursion call stack.
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.first = self.second = self.prev = None
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            
            if self.prev and self.prev.val > node.val: # violation found
                if not self.first: # if no violation found previously
                    self.first = self.prev
                
                self.second = node # update second violation if exist
            self.prev = node
            inorder(node.right)
        
        inorder(root)
        
        self.first.val, self.second.val = self.second.val, self.first.val
        
        
            
            
                
        
