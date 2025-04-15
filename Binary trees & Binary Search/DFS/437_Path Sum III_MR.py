# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

 

# Example 1:


# Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# Output: 3
# Explanation: The paths that sum to 8 are shown.
# Example 2:

# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: 3
 

# Constraints:

# The number of nodes in the tree is in the range [0, 1000].
# -109 <= Node.val <= 109
# -1000 <= targetSum <= 1000

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional

# Definition for a binary tree node (assuming standard definition)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # Instance variable to store the total count of valid paths.
        self.total_paths = 0

        # Dictionary to store frequency of prefix sums encountered on the current path.
        # Initialized with {0: 1} for the path before the root (handles paths starting at the root).
        prefix_sums = {0: 1}

        # --- Depth-First Search Helper Function ---
        # node: current node being visited
        # current_sum: the cumulative sum from the actual root down to the *parent* of this node.
        def dfs_helper(node, current_parent_sum):
            if not node:
                return # Base case: stop if node is null

            # 1. Calculate cumulative sum *including* the current node.
            current_cumulative_sum = current_parent_sum + node.val

            # 2. Check for paths ending at the current node.
            # Find the complement needed to reach the targetSum.
            complement = current_cumulative_sum - targetSum
            # If this complement exists as a prefix sum earlier on the path,
            # add its frequency to the total path count.
            self.total_paths += prefix_sums.get(complement, 0)

            # 3. Update the prefix_sum map for the current path.
            # Increment the frequency of the current cumulative sum *before* visiting children.
            prefix_sums[current_cumulative_sum] = prefix_sums.get(current_cumulative_sum, 0) + 1

            # 4. Recurse for left and right children.
            # Pass the cumulative sum that *includes* the current node.
            dfs_helper(node.left, current_cumulative_sum)
            dfs_helper(node.right, current_cumulative_sum)

            # 5. Backtrack: Crucial Step!
            # After visiting the node and its children, decrement the frequency
            # of the current cumulative sum before returning to the parent.
            # This removes the effect of the current node's path sum from the map,
            # ensuring sibling branches are evaluated correctly.
            prefix_sums[current_cumulative_sum] -= 1
            if prefix_sums[current_cumulative_sum] == 0: del prefix_sums[current_cumulative_sum]

        # --- Main function execution ---
        # Start DFS from the root with an initial parent sum of 0.
        dfs_helper(root, 0)

        # Return the final accumulated count.
        return self.total_paths
        
            