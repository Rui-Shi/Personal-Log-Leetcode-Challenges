# You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

# Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

 

# Example 1:


# Input: root = [4,2,7,1,3], val = 5
# Output: [4,2,7,1,3,5]
# Explanation: Another accepted tree is:

# Example 2:

# Input: root = [40,20,60,10,30,50,70], val = 25
# Output: [40,20,60,10,30,50,70,null,null,25]
# Example 3:

# Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
# Output: [4,2,7,1,3,5]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Function to insert a value 'val' into a Binary Search Tree (BST) rooted at 'root'.
        # It returns the root of the modified BST (which might be the same or a new root if the tree was initially empty).

        if not root:
            # Base case: If the current root is None (empty tree or reached an empty leaf position),
            # it means we have found the place to insert the new node.
            return TreeNode(val) # Create a new TreeNode with the value 'val' and return it.
                                 # This new node will be the root of a new single-node subtree,
                                 # which will be attached to the parent in the recursive calls.

        if val < root.val:
            # If the value 'val' to be inserted is less than the current root's value,
            # it should be inserted into the left subtree because of the BST property
            # (all values in the left subtree are smaller than the root).
            root.left = self.insertIntoBST(root.left, val)
            # Recursively call insertIntoBST on the left child of the current root.
            # The result of this recursive call will be the new root of the left subtree
            # (which might be the same as before if no insertion happened in the left subtree's root itself,
            # or a new left subtree root if insertion happened at the root of the left subtree).
            # We update the 'left' pointer of the current root to point to this potentially new left subtree root.

        else: # val >= root.val:
            # If the value 'val' is greater than or equal to the current root's value,
            # it should be inserted into the right subtree because of the BST property
            # (all values in the right subtree are greater than or equal to the root).
            root.right = self.insertIntoBST(root.right, val)
            # Recursively call insertIntoBST on the right child of the current root.
            # Similar to the left subtree case, the result is the potentially new root of the right subtree,
            # and we update the 'right' pointer of the current root.

        return root
        # After inserting the value (either by creating a new node if the initial root was None,
        # or by inserting in the left or right subtree and adjusting pointers),
        # we return the current root.
        # Importantly, in most cases, the root of the entire BST remains the same,
        # unless we are inserting into an initially empty tree, in which case the new node becomes the root.
        # In other recursive calls, returning the 'root' in each step allows for proper linking
        # in the previous (higher-level) recursive call by updating either 'root.left' or 'root.right'.