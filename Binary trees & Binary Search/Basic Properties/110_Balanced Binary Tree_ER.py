# Given a binary tree, determine if it is 
# height-balanced
# .

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Example 2:


# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:

# Input: root = []
# Output: true
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:  # Use 'class Solution:' instead of 'def Solution:'
    def isBalanced(self, root):
        """
        Determines if a binary tree is height-balanced.

        A height-balanced binary tree is defined as:
        a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

        Args:
            root: The root of the binary tree.

        Returns:
            True if the tree is height-balanced, False otherwise.
        """
        def check(root):
            if not root:
                return 0, True
            
            l_height, l_balanced = check(root.left)
            r_height, r_balanced = check(root.right)
            
            if not l_balanced or not r_balanced:
                return -1, False
            
            if abs(l_height - r_height) > 1:
                return -1, False
            
            return 1 + max(l_height, r_height), True
        return check(root)[1]  # Return the second element of the tuple (is_balanced)



class Solution(object):
    def isBalanced(self, root):
        """
        Determines if a binary tree is height-balanced.

        Args:
          root: The root of the binary tree.

        Returns:
          True if the tree is height-balanced, False otherwise.
        """
        return (self.Height(root) >= 0)  # Tree is balanced if Height() doesn't return -1

    def Height(self, root):
        """
        Calculates the height of the tree and checks for balance.

        Args:
          root: The root of the current subtree.

        Returns:
          The height of the subtree if balanced, -1 otherwise.
        """
        if root is None:
            return 0  # Base case: empty tree has height 0

        leftheight, rightheight = self.Height(root.left), self.Height(root.right)  # Recursively get heights of subtrees

        # Check for imbalance in subtrees or height difference > 1
        if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1:
            return -1  # Indicate imbalance

        return max(leftheight, rightheight) + 1  # Return height of current subtree