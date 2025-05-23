# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.



# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

# Two binary trees are considered leaf-similar if their leaf value sequence is the same.

# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

# Example 1:


# Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# Output: true
# Example 2:


# Input: root1 = [1,2,3], root2 = [1,3,2]
# Output: false
 

# Constraints:

# The number of nodes in each tree will be in the range [1, 200].
# Both of the given trees will have values in the range [0, 200].

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def DFS(root, leaves = []):
            if not root:
                return
            
            if not root.left and not root.right:
                leaves.append(root.val)
                return
            
            DFS(root.left, leaves)
            DFS(root.right, leaves)
        
        leaves1 = []
        leaves2 = []
        DFS(root1, leaves1)
        DFS(root1, leaves2)
        
        return leaves1 == leaves2
        
# Another way, similar efficiency 

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def getLeafSequence(root):
            # Base case 1: Empty node/subtree
            if not root:
                return []

            # Base case 2: Leaf node
            if not root.left and not root.right:
                return [root.val] # Return list with the leaf value

            # Recursive step: Internal node
            # Combine leaf sequences from left and right subtrees
            left_leaves = getLeafSequence(root.left)
            right_leaves = getLeafSequence(root.right)

            return left_leaves + right_leaves # Return the concatenated list

        # Get the leaf sequences for both trees
        leaves1 = getLeafSequence(root1)
        leaves2 = getLeafSequence(root2)

        # Compare the sequences
        return leaves1 == leaves2
    
    
            
            